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
    a = array.array("h", w.readframes(w.getnframes()))
    step = int(block * sr / 48000) * ch
    return [math.sqrt(sum(x * x for x in a[i:i + step:ch * 3]) / max(1, len(a[i:i + step:ch * 3]))) / 32768
            for i in range(0, len(a), step)]


def mix_music(act, idx, out_path, gap_db=None, duck_db=None, log=print):
    """Склеює сегменти музики акту, робить даккінг під голос і згасання в кінці."""
    sr, ch, BL = 48000, 2, 480
    total = int(act["end_f"] / FPS * sr)
    out = array.array("h", bytes(total * ch * 2))
    for name, src_in, f0, f1, fade in act["music"]:
        w = wave.open(find(idx, name))
        assert w.getframerate() == sr and w.getnchannels() == ch and w.getsampwidth() == 2
        w.setpos(int(src_in * sr))
        n = int((f1 - f0) / FPS * sr)
        seg = array.array("h", w.readframes(n))
        n = len(seg) // ch
        fi, fo = int(0.02 * sr), int(max(0.02, fade) * sr)
        t0 = int(f0 / FPS * sr)
        for i in range(n):
            g = min(1.0, i / fi, (n - i) / fo)
            j = (t0 + i) * ch
            if j + 1 < len(out):
                out[j] = int(seg[i * ch] * g)
                out[j + 1] = int(seg[i * ch + 1] * g)
    src_lv = sum(level_db(find(idx, m[0]), m[1], (m[3] - m[2]) / FPS) for m in act["music"]) / len(act["music"])
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


def media_frames(path):
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


def build_fcpxml(acts, idx, timeline):
    """acts: [(act, offset_f, music_mix_path)] — склеює акти в один таймлайн."""
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
    for act, off, mix in acts:
        v1 = act["v1"]
        vr = vo_ranges(act)
        for i, (f0, name, src_in, db, note) in enumerate(v1):
            f1 = v1[i + 1][0] if i + 1 < len(v1) else act["end_f"]
            dur, in_f = f1 - f0, int(round(src_in * FPS))
            if dur <= 0:
                problems.append(f"{act['name']}: {name} ({note}) — нульова тривалість")
                continue
            still = name.lower().endswith(STILL_EXT)
            ln = L.get(find(idx, name) or "")
            if not still and ln and in_f + dur > ln:
                problems.append(f"{act['name']}: {name} ({note}) — потрібно {dur} кадрів, у джерелі {ln - in_f}")
            if db is not None and not still:
                under = overlap(f0, f0 + dur, vr) > 0.3
                db = fx_gain(find(idx, name), src_in, dur / FPS, under)
                report.append((act["name"], name, db, "під голосом" if under else "пауза"))
            kind = "still" if still else ("av" if db is not None else "video")
            aid = asset(name, kind)
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
                attach(off + f0, f'<video ref="{aid}" lane="2" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(int(secs * FPS))}"/>')
        for n, (name, f0, secs) in act["vo"].items():
            aid = asset(name, "audio")
            if aid:
                g = round(VO_TARGET - level_db(find(idx, name), active_only=True), 1)
                report.append((act["name"], name, g, "голос"))
                attach(off + f0, f'<asset-clip ref="{aid}" lane="-1" offset="@OFF@" name="VO_UA_{n:02d}" start="0s" duration="{t(int(secs * FPS))}" audioRole="dialogue"><adjust-volume amount="{g}dB"/></asset-clip>')
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

    total = max(off + a["end_f"] for a, off, _ in acts)
    body = []
    for f0, dur, in_f, head, tag, kids in spine:
        body += ([head + ">"] + ["  " + k for k in kids] + [f"</{tag}>"]) if kids else [head + "/>"]
    res = "\n    ".join(assets[k][1] for k in order)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.8">
  <resources>
    <format id="r1" name="FFVideoFormat3840x2160p24" frameDuration="100/2400s" width="3840" height="2160" colorSpace="1-1-1 (Rec. 709)"/>
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
    build_fcpxml.report = report
    return xml, problems, sorted(p for p in paths if p)


# ------------------------------------------------------------------ Resolve
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
    bad = [i.GetName() for i in items if i.GetMediaPoolItem() is None]
    # звірка: кліп на таймлайні має посилатися саме на свій файл (Resolve іноді склеює PNG у послідовність)
    for i in items:
        m = i.GetMediaPoolItem()
        if m is not None:
            stem = os.path.splitext(i.GetName())[0].split("[")[0]
            fp = os.path.basename(m.GetClipProperty("File Path") or "")
            if stem and fp and not fp.startswith(stem[:20]) and not stem.startswith(("VO_UA", "EP01_MUS", "MUS_")):
                bad.append(f"{i.GetName()} → {fp}")
    p.SetCurrentTimeline(tl)
    pm.SaveProject()
    print(f"✓ Таймлайн «{name}»: {(tl.GetEndFrame() - s0 + 1) / FPS:.1f} с; без медіа: {bad or 'немає'}")
