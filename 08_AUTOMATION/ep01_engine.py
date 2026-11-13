#!/usr/bin/env python3
"""
Спільний «двигун» монтажу EP01: акт = словник зі списками планів, голосу, накладок і звуку.
Будує FCPXML (один акт або кілька актів підряд), робить мікс музики з даккінгом
і імпортує таймлайн у відкритий проєкт DaVinci Resolve (SEM).

Формат акту (усі кадри — відносно початку акту, 24 к/с):
  name      назва
  end_f     довжина акту в кадрах
  vo        {n: (файл, кадр_старту, тривалість_с)}
  v1        [(кадр, файл, вхід_с, живий_звук_dB | None, примітка)]   — стилли визначаються за розширенням
  v2        [(кадр, файл, тривалість_кадрів)]                         — MGFX з альфою
  v3        [(кадр, файл, тривалість_с)]                              — титри PNG
  sfx       [(кадр, файл, тривалість_с, dB)]
  music     [(файл, вхід_с, кадр_старту, кадр_кінця, згасання_с)]     — сегменти музики
  markers   [(кадр, колір, назва, примітка)]
"""
import array
import json
import math
import os
import sys
import wave
from urllib.parse import quote
from xml.sax.saxutils import quoteattr

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FPS = 24
BAR_F = 60.0 / 92 * 4 * FPS
STILL_EXT = (".png", ".jpg", ".jpeg")
_LEN = None


def bar(n):
    return int(round(n * BAR_F))


def lengths():
    global _LEN
    if _LEN is None:
        p = os.path.join(BASE, "08_AUTOMATION", "media_lengths.json")
        _LEN = json.load(open(p)) if os.path.exists(p) else {}
    return _LEN


def index_files():
    idx = {}
    for sub in ("03_AUDIO", "05_RAW_FOOTAGE"):
        for dp, _, fns in os.walk(os.path.join(BASE, sub)):
            for fn in fns:
                if not fn.startswith("."):
                    idx.setdefault(fn, []).append(os.path.join(dp, fn))
    return idx


def find(idx, name):
    ps = sorted(idx.get(name) or [], key=lambda p: ("previs" in p or "alternate" in p or "/docs/" in p, p))
    return ps[0] if ps else None


# ------------------------------------------------------------------ музика
def _env(path, block):
    w = wave.open(path)
    ch, sr = w.getnchannels(), w.getframerate()
    raw = w.readframes(w.getnframes())
    if w.getsampwidth() != 2:                 # 24/32-біт → 16 для оцінки огинаючої
        import audioop as _ao
        raw = _ao.lin2lin(raw, w.getsampwidth(), 2)
    a = array.array("h", raw)
    step = int(block * sr / 48000) * ch
    return [math.sqrt(sum(x * x for x in a[i:i + step:ch * 3]) / max(1, len(a[i:i + step:ch * 3]))) / 32768
            for i in range(0, len(a), step)]


def mix_music(act, idx, out_path, gap_db=None, duck_db=None, log=print):
    """Склеює сегменти музики акту, робить даккінг під голос і згасання в кінці."""
    sr, ch, BL = 48000, 2, 480
    total = int(act["end_f"] / FPS * sr)
    out = array.array("h", bytes(total * ch * 2))
    for m in act["music"]:
        name, src_in, f0, f1, fade = m[:5]
        fade_in = m[5] if len(m) > 5 else 0.02        # 6-й елемент — м'який вхід підкладки
        w = wave.open(find(idx, name))
        assert w.getframerate() == sr and w.getnchannels() == ch and w.getsampwidth() == 2
        w.setpos(int(src_in * sr))
        n = int((f1 - f0) / FPS * sr)
        seg = array.array("h", w.readframes(n))
        n = len(seg) // ch
        fi, fo = int(max(0.02, fade_in) * sr), int(max(0.02, fade) * sr)
        t0 = int(f0 / FPS * sr)
        for i in range(n):
            g = min(1.0, i / fi, (n - i) / fo)
            j = (t0 + i) * ch
            if j + 1 < len(out):
                out[j] = int(seg[i * ch] * g)
                out[j + 1] = int(seg[i * ch + 1] * g)
    main = [m for m in act["music"] if len(m) == 5] or act["music"]   # підкладки не змінюють рівень основної музики
    src_lv = sum(level_db(find(idx, m[0]), m[1], (m[3] - m[2]) / FPS) for m in main) / len(main)
    gap_db = MUS_GAP - src_lv if gap_db is None else gap_db
    duck_db = MUS_DUCK - src_lv if duck_db is None else duck_db
    nb = total // BL + 1
    active = [False] * nb
    for k, (name, f0, secs) in act["vo"].items():
        start_b = int(f0 / FPS * sr / BL)
        for j, v in enumerate(_env(find(idx, name), BL)):
            if v > 10 ** (-42 / 20):
                for q in range(max(0, start_b + j - 12), min(nb, start_b + j + 1)):
                    active[q] = True
    cur, gains = gap_db, []
    for b in range(nb):
        tgt = duck_db if active[b] else gap_db
        cur = max(tgt, cur - 0.6) if tgt < cur else min(tgt, cur + 0.1)
        gains.append(cur)
    log(f"  музика: джерело {src_lv:.1f} dBFS → паузи {src_lv + gap_db:.1f}, під голосом {src_lv + duck_db:.1f}")
    fb = int(3.0 * sr / BL)
    for b in range(max(0, nb - fb), nb):
        gains[b] += 20 * math.log10(max(1e-4, (nb - b) / fb))
    raw = out.tobytes()
    parts = []
    for b in range(nb):
        i0, i1 = b * BL * ch * 2, min(len(raw), (b + 1) * BL * ch * 2)
        if i0 < i1:
            parts.append(audioop.mul(raw[i0:i1], 2, 10 ** (gains[b] / 20)))
    out = array.array("h", b"".join(parts))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    o = wave.open(out_path, "wb")
    o.setnchannels(ch), o.setsampwidth(2), o.setframerate(sr)
    o.writeframes(out.tobytes())
    o.close()
    log(f"  мікс музики: {os.path.relpath(out_path, BASE)}")


# ------------------------------------------------------------------ гучність і тривалість
import aifc      # noqa: E402
import audioop   # noqa: E402
import hashlib   # noqa: E402
import subprocess  # noqa: E402

CACHE = os.path.join(BASE, "03_AUDIO", "claude_mix", "_cache")
# Цілі (dBFS RMS, приблизно): голос -20; музика в паузах -22, під голосом -32 (на 12 dB нижче голосу);
# живий звук кліпів і SFX: під голосом -36 (на 16 dB нижче), у паузах -28.
VO_TARGET, MUS_GAP, MUS_DUCK, FX_UNDER_VO, FX_GAP = -20.0, -22.0, -32.0, -36.0, -28.0


def mp4_frames(path):
    """Тривалість mp4/mov у кадрах з атома mvhd (без ffprobe)."""
    try:
        data = open(path, "rb").read()
        i = data.find(b"mvhd")
        if i < 0:
            return None
        ver = data[i + 4]
        if ver == 1:
            ts = int.from_bytes(data[i + 24:i + 28], "big"); du = int.from_bytes(data[i + 28:i + 36], "big")
        else:
            ts = int.from_bytes(data[i + 16:i + 20], "big"); du = int.from_bytes(data[i + 20:i + 24], "big")
        return int(du / ts * FPS)
    except Exception:
        return None


def still_ok(path):
    """Розширення має збігатися зі справжнім форматом (Resolve не читає JPEG з розширенням .png)."""
    head = open(path, "rb").read(8)
    if path.lower().endswith(".png"):
        return head.startswith(b"\x89PNG")
    return head.startswith(b"\xff\xd8")


def media_frames(path):
    if path.lower().endswith((".mp4", ".mov")):
        return lengths().get(path) or mp4_frames(path)
    if path.lower().endswith(".wav"):
        w = wave.open(path)
        return int(math.ceil(w.getnframes() / w.getframerate() * FPS))
    return lengths().get(path)


def wav_channels(path):
    try:
        return wave.open(path).getnchannels()
    except Exception:
        return 2


def _pcm(path):
    """(байти 16-біт little-endian, канали, частота) — для будь-якого аудіо/відео через afconvert."""
    try:
        w = wave.open(path)
        if w.getsampwidth() == 2:
            return w.readframes(w.getnframes()), w.getnchannels(), w.getframerate()
    except Exception:
        pass
    os.makedirs(CACHE, exist_ok=True)
    out = os.path.join(CACHE, hashlib.md5(path.encode()).hexdigest() + ".aif")
    if not os.path.exists(out):
        subprocess.run(["afconvert", "-f", "AIFF", "-d", "BEI16@48000", "-c", "1", path, out],
                       check=False, capture_output=True)
    if not os.path.exists(out):
        return b"", 1, 48000
    a = aifc.open(out)
    return audioop.byteswap(a.readframes(a.getnframes()), 2), 1, 48000


def level_db(path, src_in=0.0, dur=None, active_only=False):
    """RMS у dBFS для відрізка; active_only — лише блоки з сигналом (для мови)."""
    data, ch, sr = _pcm(path)
    bps = 2 * ch
    i0 = int(src_in * sr) * bps
    i1 = len(data) if dur is None else min(len(data), i0 + int(dur * sr) * bps)
    seg = data[i0:i1]
    if not seg:
        return -99.0
    if active_only:
        blk = int(0.05 * sr) * bps
        vals = [audioop.rms(seg[k:k + blk], 2) for k in range(0, len(seg) - blk, blk)]
        vals = [v for v in vals if v > 32768 * 10 ** (-45 / 20)]
        r = math.sqrt(sum(v * v for v in vals) / len(vals)) if vals else 0
    else:
        r = audioop.rms(seg, 2)
    return 20 * math.log10(max(r, 1) / 32768)


def fx_gain(path, src_in, dur_s, under_vo):
    lv = level_db(path, src_in, dur_s)
    if lv < -60:
        return None                       # у кліпі тиша — звук не потрібен
    tgt = FX_UNDER_VO if under_vo else FX_GAP
    return round(max(-40.0, min(6.0, tgt - lv)), 1)


def vo_ranges(act, off=0):
    return [(off + f0, off + f0 + int(secs * FPS)) for _, f0, secs in act["vo"].values()]


def overlap(f0, f1, ranges):
    tot = sum(max(0, min(f1, b) - max(f0, a)) for a, b in ranges)
    return tot / max(1, f1 - f0)


# ------------------------------------------------------------------ FCPXML
def t(f):
    return f"{int(f) * 100}/2400s"


DISSOLVE_UID = "FxPlug:4731E73A-8DAC-4113-9A30-AE85B1761265"
TITLE_FADE = 8          # кадрів наплаву на появу/зникнення титру
VO_LABEL = "VO_UA"      # для англійської версії build_ep01_en.py ставить "VO_EN"


def b_room_now(b):
    return b["ln"] - (b["in_f"] + b["f1"] - b["f0"])


RETIME_DIR = os.path.join(BASE, "05_RAW_FOOTAGE", "claude_graphics", "retime")


def retime(path, factor):
    """Сповільнена копія кліпу (×factor) з плавним змішуванням кадрів; кешується."""
    os.makedirs(RETIME_DIR, exist_ok=True)
    stem = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(RETIME_DIR, f"{stem}_slow{int(round(factor * 1000))}.mp4")
    if not os.path.exists(out):
        ff = os.path.expanduser("~/Library/Python/3.9/bin/ffmpeg")
        subprocess.run([ff, "-loglevel", "error", "-y", "-i", path, "-an",
                        "-vf", f"setpts={factor:.4f}*PTS,minterpolate=fps=24:mi_mode=blend",
                        "-r", "24", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", out], check=True)
    return out


def build_fcpxml(acts, idx, timeline, extra_dissolves=None, fade_in=0, fade_out=0, extra_sfx=None):
    """acts: [(act, offset_f, music_mix_path)] — склеює акти в один таймлайн.
    Наплави: act["dissolves"] = {кадр_склейки: півтривалість}, extra_dissolves — глобальні (межі актів).
    fade_in / fade_out — поява з чорного та затемнення (кадрів)."""
    problems, assets, order, spine = [], {}, [], []
    L = lengths()

    def asset(name, kind, path=None):
        key = (name, kind)
        if key in assets:
            return assets[key][0]
        p = path or find(idx, name)
        if not p:
            problems.append(f"не знайдено файл: {name}")
            return None
        aid = f"r{len(assets) + 2}"
        src, nm = quoteattr("file://" + quote(p)), quoteattr(os.path.splitext(name)[0])
        dur = media_frames(p) or FPS * 600
        if kind == "still":
            x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="0s" hasVideo="1" format="r1"/>'
        elif kind == "video":
            x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur)}" hasVideo="1" format="r1"/>'
        elif kind == "av":
            x = (f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur)}" hasVideo="1" hasAudio="1" '
                 f'audioSources="1" audioChannels="2" audioRate="48000" format="r1"/>')
        else:
            x = (f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur)}" hasAudio="1" '
                 f'audioSources="1" audioChannels="{wav_channels(p)}" audioRate="48000"/>')
        assets[key] = (aid, x)
        order.append(key)
        return aid

    report = []
    shots = []
    retimed = set()
    for act, off, mix in acts:
        v1 = act["v1"]
        vr = vo_ranges(act)
        for i, (f0, name, src_in, db, note) in enumerate(v1):
            f1 = v1[i + 1][0] if i + 1 < len(v1) else act["end_f"]
            path = find(idx, name)
            still = name.lower().endswith(STILL_EXT)
            if still and path and not still_ok(path):
                problems.append(f"{act['name']}: {name} — розширення не відповідає формату файлу (Resolve покаже битий кадр)")
            shots.append(dict(act=act, off=off, vr=vr, f0=f0, f1=f1, name=name, in_f=int(round(src_in * FPS)), db=db,
                              note=note, still=still, ln=None if still else (media_frames(path) if path else None)))
    diss = {}
    for act, off, mix in acts:
        for c, h in (act.get("dissolves") or {}).items():
            diss[off + c] = h
    diss.update(extra_dissolves or {})
    trans = {}
    for i in range(1, len(shots)):
        a, b = shots[i - 1], shots[i]
        c = b["off"] + b["f0"]
        if c not in diss:
            continue
        inf = 10 ** 6
        tail = inf if a["still"] or not a["ln"] else a["ln"] - (a["in_f"] + a["f1"] - a["f0"])
        need = diss[c]
        if tail < need and a["in_f"] > 0:          # беремо вихідний кліп трохи раніше — з'являється «хвіст»
            back = min(a["in_f"], need - tail)
            a["in_f"] -= back
            tail += back
        b_room = inf if b["still"] or not b["ln"] else b["ln"] - (b["in_f"] + b["f1"] - b["f0"])
        short = need - tail
        if 0 < short <= 14 and b_room >= short and a["f1"] - a["f0"] > short + FPS:
            # склейка на кілька кадрів раніше (голос не рухається) — місце для наплаву
            a["f1"] -= short
            b["f0"] -= short
            del diss[c]
            c -= short
            diss[c] = need
            tail = need
        if c not in diss:
            continue
        room = inf if b["still"] or not b["ln"] else b["ln"] - (b["in_f"] + b["f1"] - b["f0"])
        head = inf if b["still"] else b["in_f"] + room
        if tail < diss[c] and not a["still"] and a["ln"]:
            a["extra"] = diss[c] - tail             # сповільнимо вихідний кліп і на довжину наплаву
            tail = diss[c]
        if not b["still"] and b["ln"] and b["in_f"] + b_room_now(b) < diss[c]:
            b["extra"] = b.get("extra", 0) + diss[c]  # і вхідний — щоб на початку були кадри для наплаву
            head = diss[c] + b["in_f"]
        h = min(diss[c], tail, head)
        if h < 4:
            problems.append(f"наплав на {c / FPS:.1f} с ({b['name'][:40]}): замало кадрів у джерелі — лишаю склейку")
            continue
        if not b["still"] and b["in_f"] < h:
            b["in_f"] = h                     # зсуваємо вхід, щоб з'явилась «ручка»
        trans[c] = h
    for sh in shots:
        act, off, vr, f0, f1, name, in_f, db, note, still, ln = (sh[k] for k in ("act", "off", "vr", "f0", "f1", "name", "in_f", "db", "note", "still", "ln"))
        src_in = in_f / FPS
        dur = f1 - f0
        if dur <= 0:
            problems.append(f"{act['name']}: {name} ({note}) — нульова тривалість")
            continue
        still = name.lower().endswith(STILL_EXT)
        src_path = None
        extra = sh.get("extra", 0)
        if not still and ln and in_f + dur + extra > ln:
            factor = (in_f + dur + 6 + extra) / ln
            if factor <= 2.0:                       # плавне сповільнення замість чорного кадру
                src_path = retime(find(idx, name), factor)
                retimed.add(src_path)
                in_f = int(in_f * factor)
                name = os.path.basename(src_path)
                db = None                           # у сповільненої копії живого звуку немає
                report.append((act["name"], name, round(factor, 3), "сповільнено"))
            else:
                problems.append(f"{act['name']}: {name} ({note}) — потрібно {dur} кадрів, у джерелі {ln - in_f}")
        if db is not None and not still:
            under = overlap(f0, f0 + dur, vr) > 0.3
            db = fx_gain(find(idx, name), src_in, dur / FPS, under)
            report.append((act["name"], name, db, "під голосом" if under else "пауза"))
        kind = "still" if still else ("av" if db is not None else "video")
        aid = asset(name, kind, path=src_path)
        if not aid:
            continue
        tag = "video" if still else "asset-clip"
        head = (f'<{tag} ref="{aid}" offset="{t(off + f0)}" name={quoteattr(os.path.splitext(name)[0])} '
                f'start="{t(in_f)}" duration="{t(dur)}"' + (' audioRole="effects"' if kind == "av" else ""))
        kids = [f'<adjust-volume amount="{db}dB"/>'] if kind == "av" else []
        spine.append([off + f0, dur, in_f, head, tag, kids])

    def attach(frame, xml):
        p = next((s for s in spine if s[0] <= frame < s[0] + s[1]), spine[-1])
        p[5].append(xml.replace("@OFF@", t(p[2] + frame - p[0])))

    for act, off, mix in acts:
        cuts = sorted({r[0] for r in act["v1"]} | {act["end_f"]})
        vr = vo_ranges(act)
        for f0, name, dur in act.get("v2", []):
            aid = asset(name, "video")
            if aid:
                attach(off + f0, f'<asset-clip ref="{aid}" lane="1" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(dur)}"/>')
        for f0, name, secs in act.get("v3", []):
            c = max([c for c in cuts if 0 <= f0 - c <= 14], default=None)
            f0 = c if c is not None else f0
            f1 = f0 + int(secs * FPS)
            c2 = min(cuts, key=lambda c: abs(c - f1))
            if abs(c2 - f1) <= 18 and c2 > f0 + FPS:
                f1 = c2
            secs = (f1 - f0) / FPS
            aid = asset(name, "still")
            if aid:
                d = int(secs * FPS)
                n = min(TITLE_FADE, d // 4)
                fx = lambda o: (f'<transition name="Cross Dissolve" offset="{t(o)}" duration="{t(n)}">'
                                f'<filter-video ref="r1fx" name="Cross Dissolve"/></transition>')
                attach(off + f0, f'<spine lane="2" offset="@OFF@">' + fx(0) +
                       f'<video ref="{aid}" offset="0s" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(d)}"/>'
                       + fx(d - n) + '</spine>')
        for n, (name, f0, secs) in act["vo"].items():
            aid = asset(name, "audio")
            if aid:
                g = round(VO_TARGET - level_db(find(idx, name), active_only=True), 1)
                report.append((act["name"], name, g, "голос"))
                attach(off + f0, f'<asset-clip ref="{aid}" lane="-1" offset="@OFF@" name="{VO_LABEL}_{n:02d}" start="0s" duration="{t(int(secs * FPS))}" audioRole="dialogue"><adjust-volume amount="{g}dB"/></asset-clip>')
        aid = asset(os.path.basename(mix), "audio", path=mix)
        if aid:
            attach(off, f'<asset-clip ref="{aid}" lane="-2" offset="@OFF@" name={quoteattr(os.path.splitext(os.path.basename(mix))[0])} start="0s" duration="{t(act["end_f"])}" audioRole="music"/>')
        for f0, name, secs, db in act.get("sfx", []):
            db = fx_gain(find(idx, name), 0, secs, overlap(f0, f0 + int(secs * FPS), vr) > 0.3)
            report.append((act["name"], name, db, "SFX"))
            if db is None:
                continue
            aid = asset(name, "audio")
            if aid:
                attach(off + f0, f'<asset-clip ref="{aid}" lane="-3" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(int(secs * FPS))}" audioRole="effects"><adjust-volume amount="{db}dB"/></asset-clip>')

    for f0, name, secs in (extra_sfx or []):
        db = fx_gain(find(idx, name), 0, secs, False)
        report.append(("Епізод", name, db, "міст"))
        aid = asset(name, "audio")
        if aid and db is not None:
            attach(f0, f'<asset-clip ref="{aid}" lane="-4" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(int(secs * FPS))}" audioRole="effects"><adjust-volume amount="{db}dB"/></asset-clip>')

    total = max(off + a["end_f"] for a, off, _ in acts)
    fx_id = "r1fx"
    tr = lambda o, d: (f'<transition name="Cross Dissolve" offset="{t(o)}" duration="{t(d)}">'
                       f'<filter-video ref="{fx_id}" name="Cross Dissolve"/></transition>')
    body = []
    if fade_in:
        body.append(tr(0, fade_in))
    for f0, dur, in_f, head, tag, kids in spine:
        if f0 in trans:
            body.append(tr(f0 - trans[f0], 2 * trans[f0]))
        body += ([head + ">"] + ["  " + k for k in kids] + [f"</{tag}>"]) if kids else [head + "/>"]
    if fade_out:
        body.append(tr(total - fade_out, fade_out))
    build_fcpxml.transitions = trans
    res = "\n    ".join(assets[k][1] for k in order)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.8">
  <resources>
    <format id="r1" name="FFVideoFormat3840x2160p24" frameDuration="100/2400s" width="3840" height="2160" colorSpace="1-1-1 (Rec. 709)"/>
    <effect id="r1fx" name="Cross Dissolve" uid="{DISSOLVE_UID}"/>
    {res}
  </resources>
  <library>
    <event name="SEM_EP01_Claude">
      <project name="{timeline}">
        <sequence format="r1" duration="{t(total)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
            {(chr(10) + "            ").join(body)}
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
    paths = set()
    for a, off, mix in acts:
        paths.add(mix)
        for row in a["v1"] + a.get("v2", []) + a.get("v3", []) + a.get("sfx", []):
            paths.add(find(idx, row[1]))
        for v in a["vo"].values():
            paths.add(find(idx, v[0]))
    for row in (extra_sfx or []):
        paths.add(find(idx, row[1]))
    paths |= retimed                                # сповільнені копії теж мають бути в медіапулі
    build_fcpxml.report = report
    return xml, problems, sorted(p for p in paths if p)


# ------------------------------------------------------------------ Resolve
def fusion_title_fade(item, n=8, blur=10.0):
    """Fusion на титрі: розмиття на появі й зникненні (прозорість дає нативний наплав із FCPXML)."""
    comp = item.GetFusionCompByIndex(1) if item.GetFusionCompCount() else item.AddFusionComp()
    if not comp or comp.FindTool("TitleFade_Blur"):
        return 0
    a = comp.GetAttrs()
    s, e = int(a["COMPN_RenderStart"]), int(a["COMPN_RenderEnd"])
    comp.Lock()
    mi, mo = comp.FindTool("MediaIn1"), comp.FindTool("MediaOut1")
    bl = comp.AddTool("Blur", -32768, -32768)
    bl.SetAttrs({"TOOLS_Name": "TitleFade_Blur"})
    bl.Input = mi.Output
    mo.Input = bl.Output
    bl.AddModifier("XBlurSize", "BezierSpline")
    for fr, v in ((s, blur), (s + n, 0.0), (e - n, 0.0), (e, blur * 0.7)):
        bl.SetInput("XBlurSize", v, fr)
    comp.Unlock()
    return 1


def to_resolve(xml_path, paths, timeline, markers, replace=False):
    sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules")
    import DaVinciResolveScript as bmd
    r = bmd.scriptapp("Resolve")
    if r is None:
        sys.exit("Resolve не відповідає: відкрийте його й увімкніть External scripting = Local.")
    pm = r.GetProjectManager()
    p = pm.GetCurrentProject()
    if not p or p.GetName() != "SEM":
        p = pm.LoadProject("SEM")
    mp = p.GetMediaPool()
    root = mp.GetRootFolder()
    folders, have = [], set()

    def walk(f):
        folders.append(f)
        for c in f.GetClipList() or []:
            fp = c.GetClipProperty("File Path")
            if fp:
                have.add(fp)
        for s in f.GetSubFolderList() or []:
            walk(s)
    walk(root)
    missing = [x for x in paths if x not in have]
    if missing:
        b = next((s for s in root.GetSubFolderList() if s.GetName() == "21_CLAUDE_DIRECTORS_CUT"), None) \
            or mp.AddSubFolder(root, "21_CLAUDE_DIRECTORS_CUT")
        mp.SetCurrentFolder(b)
        mp.ImportMedia(missing)
        folders = []
        walk(root)
    mp.SetCurrentFolder(root)
    tls = [p.GetTimelineByIndex(i) for i in range(1, p.GetTimelineCount() + 1)]
    old = [x for x in tls if x.GetName() == timeline]
    if old and replace:
        p.SetCurrentTimeline(next(x for x in tls if x.GetName() != timeline))
        mp.DeleteTimelines(old)
        names = {x.GetName() for x in tls if x not in old}
    else:
        names = {x.GetName() for x in tls}
    name, k = timeline, 2
    while name in names:
        name, k = f"{timeline}_v{k}", k + 1
    tl = mp.ImportTimelineFromFile(xml_path, {"timelineName": name, "importSourceClips": False,
                                              "sourceClipsFolders": folders})
    if not tl:
        sys.exit(f"Імпорт не вдався. Вручну: File > Import > Timeline > {xml_path}")
    s0 = tl.GetStartFrame()
    for f0, col, nm, note in markers:
        tl.AddMarker(s0 + f0, col, nm, note, 1)
    items = [i for kk in ("video", "audio") for nn in range(1, tl.GetTrackCount(kk) + 1)
             for i in (tl.GetItemListInTrack(kk, nn) or [])]
    bad = [i.GetName() for i in items if i.GetMediaPoolItem() is None and "Dissolve" not in i.GetName()]
    # звірка: кліп на таймлайні має посилатися саме на свій файл (Resolve іноді склеює PNG у послідовність)
    for i in items:
        m = i.GetMediaPoolItem()
        if m is not None:
            stem = os.path.splitext(i.GetName())[0].split("[")[0]
            fp = os.path.basename(m.GetClipProperty("File Path") or "")
            if stem and fp and not fp.startswith(stem[:20]) and not stem.startswith(("VO_UA", "VO_EN", "EP01_MUS", "MUS_")):
                bad.append(f"{i.GetName()} → {fp}")
    animated = 0
    for kk in range(1, tl.GetTrackCount("video") + 1):
        for it in tl.GetItemListInTrack("video", kk) or []:
            if it.GetName().startswith(("EP01_SUPER", "EP01_RULE")):
                animated += fusion_title_fade(it)
    p.SetCurrentTimeline(tl)
    pm.SaveProject()
    print(f"  Титри: наплави з FCPXML; Fusion-розмиття додано на {animated} (у складених кліпах — пропускається)")
    print(f"✓ Таймлайн «{name}»: {(tl.GetEndFrame() - s0 + 1) / FPS:.1f} с; без медіа: {bad or 'немає'}")
