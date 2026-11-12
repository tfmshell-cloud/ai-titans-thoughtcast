#!/usr/bin/env python3
"""
Робочий стіл героя для хабу (07_DASHBOARD/index_claude.html).

Сканує ВСЮ медіабазу проєкту і збирає для кожного епізоду один файл даних:
  07_DASHBOARD/data/workbench/epNN.js  → window.WB["NN"]
  07_DASHBOARD/data/workbench/summary.js → window.WB_SUMMARY (готовність по етапах, лічильники)

Що потрапляє в епізод:
  • тексти ElevenLabs (02_SCRIPTS/*/EPNN_VO_*_ELEVENLABS_MASTER.txt), розбиті на блоки, + записані дублі;
  • промпти анімації (100 покадрових промптів, тріади Flow, ключові сцени Veo);
  • музика Suno (промпти, наявні файли, прев'ю);
  • медіа: власні файли героя + файли з загальної бази, підібрані до конкретних сцен сценарію
    (збіг слів назви файлу з промптами сцен; рідкісні слова важать більше);
  • документи дослідження (досьє, стенограми, статті) з посиланнями на GitHub.

Готовність рахується з реальних файлів, а не з галочок у браузері.
Запуск: python3 08_AUTOMATION/build_episode_workbench.py
Нічого не видаляє і не змінює в медіапапках; лише пише data/workbench/ та мініатюри assets/vault_thumbs/catalog/.
"""
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DASH = os.path.join(ROOT, "07_DASHBOARD")
OUT = os.path.join(DASH, "data", "workbench")
THUMBS = os.path.join(DASH, "assets", "vault_thumbs", "catalog")
VO_PREV = os.path.join(DASH, "assets", "audio_previews", "vo")
FFMPEG = os.path.expanduser("~/Library/Python/3.9/bin/ffmpeg")
EPS = [f"{i:02d}" for i in range(1, 11)]

VIDEO = {".mp4", ".mov", ".m4v"}
IMAGE = {".png", ".jpg", ".jpeg", ".webp", ".heic"}
AUDIO = {".wav", ".mp3", ".m4a", ".aif", ".aiff"}

# Прізвища героїв: файл, де згадано героя, корисний і в його епізоді
HERO_KEYS = {
    "01": ["altman", "loopt", "ycombinator", "openai_found"],
    "02": ["huang", "jensen", "nvidia", "cuda", "geforce", "dgx", "blackwell", "dennys"],
    "03": ["hassabis", "deepmind", "alphago", "alphafold", "leesedol", "lee_sedol"],
    "04": ["hinton", "backprop", "dnnresearch"],
    "05": ["lecun", "lenet", "convolution"],
    "06": ["sutskever", "ilya", "alexnet", "ssi_"],
    "07": ["amodei", "anthropic", "constitutional"],
    "08": ["feifei", "fei_fei", "imagenet"],
    "09": ["bengio", "mila"],
    "10": ["andrew_ng", "andrewng", "coursera", "google_brain", "googlebrain"],
}

STOP = set("""the of in a an into with through and at on to from by for its over var var2 under onto as is are
ep vid img flow clip still card ua en act v1 v2 v3 b2 b3 b4 master creative new gapless study keyframe keyframes
primary broll stills studies batch fps 24fps 1080p 720p 2k 4k 8k uhd hd mp4 mov png jpg jpeg final ref
s f ken burns kb archival arch photo portrait real version alt camera mov video view shot cinematic eleven labs
seedance dynamic authentic intense slow powerful close closeup wide inside function internally frame scene 09t12
histo lett clip render rendered octane imag image images user vault download from_downloads""".split())

# Словник понять: і назви файлів, і промпти сцен розширюються тегами #поняття
CONCEPTS = {
    "bio": "heart valve mitral neutrophil bacteri cell zygote prenatal embryo dna protein molecul enzyme organ blood biolog microscop tissue fold virus medic hospital",
    "brain": "brain neuron neural neuro synap axon cortex mind hippocamp thought memory",
    "eye": "eye retina iris pupil vision optic seeing imagenet photo picture",
    "cosmos": "star galax cosmic interstellar space planet orbit nebula universe astronaut earth dyson hole asteroid moon",
    "ice": "glacier iceberg ice frozen arctic snow cold",
    "ocean": "ocean sea whale shark wave water underwater jellyfish sail boat",
    "city": "city skyscraper metropol cyberpunk urban street building tower factory industrial",
    "chip": "gpu chip silicon wafer transistor server supercomputer circuit processor datacenter rack nvidia cuda hardware",
    "code": "code terminal screen computer keyboard program monitor crt pixel software digital",
    "game": "chess game board gamer controller play esport knight pawn",
    "danger": "dragon shark fire explos storm threat collapse shatter fractur abyss warning risk crack doom",
    "energy": "spark electric lightning energy plasma fusion tesla laser glow light power",
    "change": "emerg rise grow morph transform portal evolv aging dissolv birth",
    "child": "boy child kid young school girl",
    "learn": "book library classroom teach lecture student education chalk blackboard university campus",
    "money": "coin gold money dollar market stock bank",
    "data": "data binary matrix grid network lattice vector embedding algorithm equation math",
}
CONCEPT_PREFIX = [(w, c) for c, ws in CONCEPTS.items() for w in ws.split()]
# Теми героїв: які поняття найближчі до їхньої історії
THEMES = {
    "02": {"chip", "game", "code", "city", "danger", "money", "energy"},
    "03": {"game", "brain", "bio", "cosmos", "code", "child"},
    "04": {"brain", "danger", "learn", "data", "energy"},
    "05": {"eye", "code", "data", "ocean", "learn"},
    "06": {"chip", "cosmos", "brain", "danger", "data"},
    "07": {"bio", "danger", "eye", "brain", "learn"},
    "08": {"eye", "data", "learn", "child", "bio"},
    "09": {"danger", "brain", "learn", "data", "change"},
    "10": {"learn", "city", "energy", "data", "chip"},
}


# Кураторський вибір для кліпів, чиї назви надто образні для автоматичного збігу
MANUAL = {
    "Bioluminescent_jellyfish": (["04", "09"], "живе світіння нейромережі — метафора думки"),
    "Camera_moving_through_human_eye": (["08", "05"], "зір і комп'ютерне бачення"),
    "Cyberpunk_skyscrapers": (["10", "02"], "ШІ як нова електрика міст і індустрії"),
    "Glacier_shatters_into_jungle": (["06", "05"], "зсув парадигми: лід → життя"),
    "Human_heart_beating": (["08", "07"], "людський вимір: хвороба матері Фей-Фей, втрата батька Даріо"),
    "Ice_shark_breaches": (["09", "04"], "прихована загроза під поверхнею"),
    "Icebergs_floating_into_cloudy_sky": (["09", "04"], "засніжений Монреаль, холодна самотність науки"),
    "Interstellar_whale": (["06", "03"], "космічний масштаб надінтелекту"),
    "Mitral_valve": (["07", "03"], "біологія й медицина, стиснуте століття відкриттів"),
    "Mothership_descending": (["04", "09"], "Хінтон: «наче прибульці приземлилися»"),
    "Neutrophil_engulfing": (["07", "03"], "імунітет і медицина майбутнього"),
    "Serpentine_dragon_eye": (["04", "07"], "пробудження сили, яку важко приборкати"),
    "Titan_emerging_from_glacier": (["09", "02", "10"], "титан виходить із льоду — інтро/фінал сезону"),
}


def manual_for(f):
    for k, v in MANUAL.items():
        if f.startswith(k):
            return v
    return None


def expand(tk):
    tk = set(tk)
    for t in list(tk):
        for w, c in CONCEPT_PREFIX:
            if t.startswith(w):
                tk.add("#" + c)
    return tk


def load_js(path):
    s = open(path, encoding="utf-8").read()
    i = s.index("=") + 1
    return json.loads(s[i:].strip().rstrip(";"))


def stem(w):
    for suf in ("ing", "ed", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def tokens(text):
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    out = []
    for w in re.split(r"[^A-Za-z0-9]+", text.lower()):
        if not w or w in STOP or w.isdigit() or len(w) < 3:
            continue
        if re.fullmatch(r"[0-9a-f]{8}", w) or re.fullmatch(r"\d+[sfp]|\d{8,}|ep\d+|act\d|v\d+|b\d", w):
            continue
        w = stem(w)
        if w in STOP or w in ("mov", "mak", "show", "tak", "us"):
            continue
        out.append(w)
    return out


def rel(p):
    return os.path.relpath(p, ROOT)


def mmss_to_s(tc):
    m = re.match(r"(\d+):(\d+)", tc or "")
    return int(m.group(1)) * 60 + int(m.group(2)) if m else None


# ---------------------------------------------------------------- джерела
def load_sources():
    D = os.path.join(DASH, "data")
    season = load_js(os.path.join(D, "season1_index.js"))
    epdata = {ep: load_js(os.path.join(D, "episodes", f"ep{ep}.js")) for ep in EPS}
    vault = load_js(os.path.join(D, "project_vault_inventory.js"))
    acq = load_js(os.path.join(D, "media_acquisition_pool.js"))
    triads = load_js(os.path.join(D, "flow_triads_pool.js"))
    suno = load_js(os.path.join(D, "suno_master_pool.js"))
    veo = load_js(os.path.join(D, "veo_animation_pipeline.js"))
    mon = load_js(os.path.join(D, "montage_status.js"))
    return season, epdata, vault, acq, triads, suno, veo, mon


# ---------------------------------------------------------------- ElevenLabs
def parse_eleven(path):
    if not os.path.exists(path):
        return None
    raw = open(path, encoding="utf-8").read()
    head, settings = [], {}
    blocks = []
    cur = None
    for line in raw.splitlines():
        m = re.match(r"^\[(\d+:\d+)\s*-\s*(\d+:\d+)\]\s*(?:\((\d+)\s*сл[^)]*\))?", line)
        if m:
            cur = {"tc": f"{m.group(1)}–{m.group(2)}", "start": m.group(1), "end": m.group(2),
                   "words": int(m.group(3) or 0), "text": ""}
            blocks.append(cur)
            continue
        if cur is None:
            if line.strip() and not line.startswith("==="):
                head.append(line.strip())
            continue
        cur["text"] += line + "\n"
    for b in blocks:
        t = b["text"].replace("\\n", "\n").strip()
        b["text"] = re.sub(r"\n{3,}", "\n\n", t)
        clean = re.sub(r"\*\*?([^*]+)\*\*?", r"\1", b["text"])
        b["clean"] = clean
        if not b["words"]:
            b["words"] = len(clean.split())
    for h in head:
        if ":" in h:
            k, v = h.split(":", 1)
            settings[k.strip()] = v.strip()
    return {"settings": settings, "blocks": blocks, "file": rel(path)}


def recorded_vo(ep):
    """Записані дублі UA/EN: {мова: {номер блоку: [шляхи]}}"""
    res = {"UA": defaultdict(list), "EN": defaultdict(list)}
    base = os.path.join(ROOT, "03_AUDIO", "voiceover")
    for dp, _, fs in os.walk(base):
        if "SPLIT" in dp:
            continue
        for f in sorted(fs):
            m = re.match(rf"EP{ep}_VO_(UA|EN)_(\d\d)_.*\.(mp3|wav)$", f)
            if m:
                res[m.group(1)][int(m.group(2))].append(os.path.join(dp, f))
    return res


def vo_preview(path):
    """Web-прев'ю mp3 у assets/audio_previews/vo (копіюється, якщо ще немає)."""
    if not path.endswith(".mp3"):
        mp3 = os.path.splitext(path)[0] + ".mp3"
        if os.path.exists(mp3):
            path = mp3
        else:
            return ""
    dst = os.path.join(VO_PREV, os.path.basename(path))
    if not os.path.exists(dst):
        os.makedirs(VO_PREV, exist_ok=True)
        shutil.copy2(path, dst)
    return rel(dst).replace("07_DASHBOARD/", "")


# ---------------------------------------------------------------- медіа
def classify_folder(rp):
    r = rp.lower()
    if r.startswith("05_raw_footage/archives/"):
        return "archive", "Архівне відео", False
    if r.startswith("05_raw_footage/dossiers_press/"):
        return "doc", "Документ / преса", False
    if r.startswith("05_raw_footage/speaker_portraits/"):
        return "photo", "Фото героя", False
    if r.startswith("05_raw_footage/claude_graphics/"):
        return "graphic", "Титри й графіка", False
    if r.startswith("05_raw_footage/rendered_cinematic_stills_4k/"):
        if "card" in r:
            return "graphic", "Картка-цитата UA", False
        return "still", "Кінокадр 4K", True
    if r.startswith("05_raw_footage/scientific_animations/"):
        return "anim", "Наукова анімація", True
    if r.startswith("05_raw_footage/flow_images/"):
        return "flowimg", "Кадр Google Flow", True
    if r.startswith(("05_raw_footage/flow_renders/", "05_raw_footage/flow_videos/", "05_raw_footage/flow_previs")):
        return "anim", "Анімація Flow", True
    if r.startswith("05_raw_footage/ssd_ai_generations/"):
        return "ai", "ШІ-генерація з SSD", True
    if r.startswith("05_raw_footage/veo_clips/"):
        return "anim", "Veo", True
    return "ai", "Авторська ШІ-генерація", True


PERSONAL = re.compile(r"(card|super_|rule_|portrait|face|young_|_ref\b|typewriter|title|quote)", re.I)


def owner_ep(rp):
    r = rp.lower()
    if "ep02_demis_hassabis" in r:
        return "03"
    m = re.search(r"(?:^|[^a-z0-9])ep(0[1-9]|10)(?:[^0-9]|$)", r)
    if m:
        return m.group(1)
    if "ssd_ai_generations" in r:
        return None
    if "user_ai_generations" in r or "user_ai_images" in r or "altman" in r:
        return "01"
    for ep, keys in HERO_KEYS.items():
        if any(k in r for k in keys):
            return ep
    return None


def scan_media():
    roots = [os.path.join(ROOT, "05_RAW_FOOTAGE"), os.path.join(ROOT, "04_ASSETS")]
    items = []
    for base in roots:
        for dp, dns, fs in os.walk(base):
            dns[:] = [d for d in dns if not d.startswith(".") and d != "_cache"]
            for f in sorted(fs):
                if f.startswith(".") or f.endswith((".json", ".md", ".txt")):
                    continue
                ext = os.path.splitext(f)[1].lower()
                if ext not in VIDEO | IMAGE:
                    continue
                p = os.path.join(dp, f)
                items.append(p)
    return items


def thumb_for(path, known):
    rp = rel(path)
    if rp in known:
        return known[rp]
    h = hashlib.md5(rp.encode()).hexdigest()[:12]
    dst = os.path.join(THUMBS, h + ".jpg")
    web = "assets/vault_thumbs/catalog/" + h + ".jpg"
    if os.path.exists(dst):
        return web
    os.makedirs(THUMBS, exist_ok=True)
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in VIDEO:
            subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-ss", "1", "-i", path, "-frames:v", "1",
                            "-vf", "scale=480:-2", "-q:v", "5", dst], check=True, timeout=60)
        else:
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", "-Z", "480", path,
                            "--out", dst], check=True, capture_output=True, timeout=60)
        return web if os.path.exists(dst) else ""
    except Exception:
        return ""


def pretty_name(f):
    n = os.path.splitext(f)[0]
    n = re.sub(r"_(clip_)?[0-9a-f]{8}(_\d+p|_2K|_4K)?$", "", n)
    n = re.sub(r"_(\d{14})$", "", n)
    n = re.sub(r"_(1080p|720p|2K|4K)$", "", n)
    n = re.sub(r"^EP\d\d_", "", n)
    return n.replace("_", " ").replace("…", "…").strip()


# ---------------------------------------------------------------- зіставлення зі сценами
class SceneIndex:
    def __init__(self, epdata, triads):
        self.scenes = {}
        df = Counter()
        for ep in EPS:
            sc = []
            for p in epdata[ep].get("prompts_100", []):
                txt = p.get("prompt", "") + " " + p.get("filename", "")
                tk = expand(tokens(txt))
                sc.append({"kind": "prompt", "num": p["num"], "act": p.get("act"), "tc": p.get("tc", ""),
                           "cue": p.get("cue_ua", ""), "tk": tk})
            for t in triads.get(ep, []):
                txt = " ".join(str(t.get(k, "")) for k in ("title_en", "p1_start", "p2_flow", "p3_end"))
                tk = expand(tokens(txt))
                sc.append({"kind": "triad", "num": t.get("num"), "act": t.get("act"), "tc": t.get("tc", ""),
                           "cue": t.get("title_ua", ""), "tk": tk})
            self.scenes[ep] = sc
            for s in sc:
                df.update(s["tk"])
        n = sum(len(v) for v in self.scenes.values())
        self.idf = {w: math.log(n / (1 + c)) for w, c in df.items()}

    def best(self, ep, ftok):
        ftok = expand(ftok)
        if not ftok:
            return 0, None, []
        concepts = {t[1:] for t in ftok if t.startswith("#")}
        bonus = 2.0 * min(2, len(concepts & THEMES.get(ep, set())))
        best = (0, None, [])
        for s in self.scenes[ep]:
            common = ftok & s["tk"]
            if not common:
                continue
            sc = sum(self.idf.get(w, 0) * (0.9 if w.startswith("#") else 1) for w in common) / math.sqrt(len(ftok)) + bonus
            if sc > best[0]:
                best = (sc, s, sorted(common))
        return best


def act_label(a):
    if a in (None, ""):
        return ""
    m = re.search(r"(\d)", str(a))
    return f"Акт {m.group(1)}" if m else str(a)


# ---------------------------------------------------------------- головне
def main():
    season, epdata, vault, acq, triads, suno, veo, mon = load_sources()
    S = {e["ep"]: e for e in season}

    # мініатюри й метадані, що вже є у старому сховищі
    known_thumb, meta = {}, {}
    for ep, d in vault.items():
        if not isinstance(d, dict):
            continue
        for k in ("videos", "images"):
            for x in d.get(k, []) or []:
                if x.get("rel_path") and x.get("thumb"):
                    known_thumb.setdefault(x["rel_path"], x["thumb"])
                if x.get("rel_path"):
                    meta.setdefault(x["rel_path"], x)
    # українські назви й призначення з пулу архівів/фото/досьє
    by_file = {}
    for ep, d in acq.items():
        for x in d.get("archives", []) or []:
            by_file[x.get("file") or x.get("mp4_file")] = {"title": x.get("title"), "act": x.get("act"),
                "tc": x.get("timecode"), "use": x.get("davinci_usage") or x.get("note"), "src": x.get("source"),
                "url": x.get("url"), "prev": x.get("web_preview")}
        for x in d.get("archival_photos", []) or []:
            f = os.path.basename(x.get("raw_file", ""))
            by_file[f] = {"title": x.get("title"), "src": x.get("source"), "url": x.get("url"),
                          "thumb": x.get("web_preview")}
        for x in d.get("dossiers", []) or []:
            f = os.path.basename(x.get("raw_4k_png", ""))
            by_file[f] = {"title": x.get("title"), "act": x.get("act"), "tc": x.get("timecode"),
                          "use": x.get("highlight"), "src": x.get("source_label"), "thumb": x.get("web_preview"),
                          "prev": x.get("video_preview")}

    idx = SceneIndex(epdata, triads)
    files = scan_media()
    print(f"Медіафайлів у базі: {len(files)}")

    media = {ep: [] for ep in EPS}
    pool_stats = Counter()
    for p in files:
        rp = rel(p)
        f = os.path.basename(p)
        kind, label, generic = classify_folder(rp)
        if PERSONAL.search(f):
            generic = False
        ext = os.path.splitext(f)[1].lower()
        own = owner_ep(rp)
        info = by_file.get(f, {})
        m = meta.get(rp, {})
        ftok = tokens(os.path.splitext(f)[0] + " " + os.path.basename(os.path.dirname(p)))
        base = {
            "p": rp, "n": info.get("title") or pretty_name(f), "f": f, "k": kind, "c": label,
            "v": ext in VIDEO, "d": m.get("dur_label", ""), "r": m.get("res_label", ""),
            "mb": round(os.path.getsize(p) / 1e6, 1), "src": info.get("src", ""), "url": info.get("url", ""),
            "pv": info.get("prev") or m.get("preview_path") or "",
        }
        targets = {}
        if own:
            targets[own] = "own"
        low = rp.lower()
        for ep, keys in HERO_KEYS.items():
            if ep != own and any(k in low for k in keys):
                targets.setdefault(ep, "hero")
        if generic:
            cand = []
            for ep in EPS:
                if ep == "01" or ep in targets:
                    continue  # EP01 змонтовано — нові підбірки йдуть у наступні епізоди
                sc, s, common = idx.best(ep, ftok)
                if sc >= 4.5:
                    cand.append((sc, ep))
            cand.sort(reverse=True)
            for sc, ep in cand[:3]:
                if sc >= 0.75 * cand[0][0]:
                    targets[ep] = "pick"
        man = manual_for(f)
        if man:
            for ep in man[0]:
                targets.setdefault(ep, "pick")
        if not targets:
            pool_stats["без епізоду"] += 1
        thumb = None
        for ep, why in targets.items():
            sc, s, common = idx.best(ep, ftok)
            it = dict(base)
            it["why"] = why
            if s and sc >= 2.5:
                it["sc"] = {"t": s["kind"], "num": s["num"], "act": act_label(s["act"]), "tc": s["tc"],
                            "cue": (s["cue"] or "")[:160], "kw": [w for w in common if not w.startswith("#")][:4],
                            "cn": [w[1:] for w in common if w.startswith("#")][:3], "score": round(sc, 1)}
            elif info.get("act") or info.get("tc"):
                it["sc"] = {"t": "arch", "act": act_label(info.get("act")), "tc": info.get("tc") or ""}
            if info.get("use"):
                it["use"] = info["use"][:220]
            if man and ep in man[0]:
                it["use"] = "Кураторський вибір: " + man[1]
            if "ssd_ai_generations" in rp:
                it["src"] = "SSD «DaVinci KVV» → скопійовано в проєкт"
            if thumb is None:
                thumb = info.get("thumb") or thumb_for(p, known_thumb)
            it["t"] = thumb
            media[ep].append(it)
            pool_stats[why] += 1

    # ---------------- документи дослідження
    def docs_for(ep):
        e = epdata[ep]
        out = []
        rdir = os.path.join(ROOT, "01_RESEARCH", e.get("research_dir", ""))
        for dp, _, fs in os.walk(rdir):
            for f in sorted(fs):
                if f.startswith(".") or f == ".gitkeep":
                    continue
                sub = os.path.basename(dp)
                cat = {"transcripts": "Стенограма", "articles": "Стаття"}.get(sub, "Досьє")
                out.append({"p": rel(os.path.join(dp, f)), "n": pretty_name(f), "c": cat,
                            "kb": round(os.path.getsize(os.path.join(dp, f)) / 1024)})
        src = os.path.join(ROOT, "01_RESEARCH", "source_pdfs_and_dossiers")
        for f in sorted(os.listdir(src)) if os.path.isdir(src) else []:
            if re.search(rf"(EP{ep}|{e['latin'].split()[-1]})", f, re.I):
                out.append({"p": rel(os.path.join(src, f)), "n": pretty_name(f), "c": "Першоджерело",
                            "kb": round(os.path.getsize(os.path.join(src, f)) / 1024)})
        sdir = os.path.dirname(os.path.join(ROOT, e["script_md_path"]))
        for f in sorted(os.listdir(sdir)):
            if f.startswith("."):
                continue
            out.append({"p": rel(os.path.join(sdir, f)), "n": f, "c": "Сценарій / озвучка",
                        "kb": round(os.path.getsize(os.path.join(sdir, f)) / 1024)})
        for f in sorted(os.listdir(os.path.join(ROOT, "04_VIDEO_PROMPTS"))):
            if re.match(rf"(ep{ep}_|episode_{ep}_)", f, re.I):
                out.append({"p": "04_VIDEO_PROMPTS/" + f, "n": f, "c": "Промпти",
                            "kb": round(os.path.getsize(os.path.join(ROOT, "04_VIDEO_PROMPTS", f)) / 1024)})
        return out

    # ---------------- музика
    suno_dir = os.path.join(ROOT, "03_AUDIO", "suno_stems")
    suno_files = {}
    for dp, _, fs in os.walk(suno_dir):
        for f in fs:
            suno_files.setdefault(f, os.path.join(dp, f))
    previews = {}
    for t in suno:
        previews[t["smart_bin"]] = t
        for b in t.get("extra_bins") or []:
            previews.setdefault(b.get("smart_bin", ""), t)

    summary = {"generated": datetime.now().strftime("%Y-%m-%d %H:%M"), "eps": {}, "media_total": len(files),
               "pool": dict(pool_stats)}
    os.makedirs(OUT, exist_ok=True)

    for ep in EPS:
        e, s = epdata[ep], S[ep]
        slug = e["script_md_path"].split("/")[1]
        ua = parse_eleven(os.path.join(ROOT, "02_SCRIPTS", slug, f"EP{ep}_VO_UA_ELEVENLABS_MASTER.txt"))
        en = parse_eleven(os.path.join(ROOT, "02_SCRIPTS", slug, f"EP{ep}_VO_EN_ELEVENLABS_MASTER.txt"))
        rec = recorded_vo(ep)
        for lang, doc in (("UA", ua), ("EN", en)):
            if not doc:
                continue
            for i, b in enumerate(doc["blocks"], 1):
                fs = rec[lang].get(i, [])
                b["rec"] = [rel(x) for x in fs]
                b["play"] = vo_preview(fs[0]) if fs else ""
        n_blocks = len(ua["blocks"]) if ua else 0
        n_rec = sum(1 for b in (ua["blocks"] if ua else []) if b["rec"])

        music = []
        for r in e.get("suno_registry", []):
            fn = r["filename"]
            pv = previews.get(fn)
            music.append({"f": fn, "t": r.get("title_clean", ""), "act": act_label(r.get("act")),
                          "cat": r.get("category", ""), "track": r.get("davinci_track", ""),
                          "prompt": r.get("suno_prompt", ""), "have": rel(suno_files[fn]) if fn in suno_files else "",
                          "prev": ("assets/audio_previews/" + pv["preview"]) if pv else "",
                          "orig": pv["orig_name"] if pv else ""})
        n_mus = sum(1 for x in music if x["have"])

        prompts = [{"num": p["num"], "act": p.get("act"), "tc": p.get("tc"), "f": p.get("filename"),
                    "key": p.get("is_key", False), "cue": p.get("cue_ua", ""), "p": p.get("prompt", "")}
                   for p in e.get("prompts_100", [])]
        tri = [{"num": t.get("num"), "id": t.get("id"), "t": t.get("title_ua"), "tc": t.get("tc"),
                "act": t.get("act"), "vo": t.get("vo_quote", ""), "p1": t.get("p1_start", ""),
                "p2": t.get("p2_flow", ""), "p3": t.get("p3_end", ""), "dv": t.get("davinci_recipe", ""),
                "sfx": t.get("sfx_cue", ""), "kf": t.get("keyframe_preview", ""), "vp": t.get("video_preview", ""),
                "st": t.get("status", "")} for t in triads.get(ep, [])]
        vk = [v["id"] for v in veo if v.get("ep") == ep]

        med = media[ep]
        own_vis = [x for x in med if x["why"] == "own" and x["k"] in ("ai", "anim", "flowimg", "still", "archive", "photo")]
        picks = [x for x in med if x["why"] != "own"]
        med.sort(key=lambda x: ({"own": 0, "hero": 1, "pick": 2}[x["why"]],
                                -(x.get("sc", {}).get("score") or 0) if x["why"] != "own" else 0, x["p"]))

        m = mon.get(ep)
        stages = [
            {"id": "research", "t": "Дослідження", "w": 5, "pct": 100 if os.path.exists(os.path.join(ROOT, e["dossier_md_path"])) else 0,
             "d": "Мастер-досьє і стенограми", "tab": "docs"},
            {"id": "script", "t": "Сценарій", "w": 10, "pct": 100 if ua else 50,
             "d": f"{e.get('script_total_words') or s.get('script_words')} слів · {n_blocks} блоків ElevenLabs", "tab": "vo"},
            {"id": "vo", "t": "Озвучка", "w": 15, "pct": round(100 * n_rec / n_blocks) if n_blocks else 0,
             "d": f"записано {n_rec} з {n_blocks} блоків", "tab": "vo"},
            {"id": "music", "t": "Музика", "w": 10, "pct": 100 if m else round(100 * n_mus / max(1, len(music))),
             "d": ("музику зведено в монтажі" if m else f"{n_mus} з {len(music)} треків у бінах"), "tab": "music"},
            {"id": "visual", "t": "Візуал", "w": 20, "pct": 100 if m else min(100, round(100 * len(own_vis) / 100)),
             "d": (f"{m['total_shots']} планів у монтажі" if m else f"{len(own_vis)} власних кадрів · {len(picks)} підібрано з бази"), "tab": "media"},
            {"id": "montage", "t": "Монтаж", "w": 30, "pct": 100 if m else 0,
             "d": (f"{m['full_timeline']} · {m['total_duration']}" if m else "ще не почато"), "tab": "montage" if m else "media"},
            {"id": "master", "t": "Рендер і реліз", "w": 10, "pct": 0, "d": "фінальний мастер ще не зарендерено",
             "tab": "montage" if m else "overview"},
        ]
        pct = round(sum(x["w"] * x["pct"] / 100 for x in stages))
        nxt = []
        for st in stages:
            if st["pct"] >= 100:
                continue
            if st["id"] == "vo":
                nxt.append({"t": f"Озвучити в ElevenLabs {n_blocks - n_rec} блоків", "tab": "vo"})
            elif st["id"] == "music":
                nxt.append({"t": f"Згенерувати в Suno {len(music) - n_mus} треків за промптами", "tab": "music"})
            elif st["id"] == "visual":
                nxt.append({"t": f"Переглянути {len(picks)} підібраних файлів і догенерувати сцени Flow/Veo", "tab": "media"})
            elif st["id"] == "montage":
                nxt.append({"t": "Зібрати таймлайн у DaVinci Resolve за сценами", "tab": "media"})
            elif st["id"] == "master":
                nxt.append({"t": "Зарендерити мастер (Deliver, −14 LUFS) і зберегти" if m else "Рендер після монтажу", "tab": "montage" if m else "overview"})
        if m:
            nxt = [{"t": x, "tab": "montage"} for x in (m.get("next") or [])] + [x for x in nxt if x["tab"] == "montage"]

        counts = Counter(x["k"] for x in med)
        summary["eps"][ep] = {"pct": pct, "stages": stages, "next": nxt[:5],
                              "counts": {"media": len(med), "own": len(med) - len(picks), "picked": len(picks),
                                         "video": sum(1 for x in med if x["v"]), "image": sum(1 for x in med if not x["v"]),
                                         "vo_blocks": n_blocks, "vo_rec": n_rec, "music": len(music), "music_have": n_mus,
                                         "prompts": len(prompts), "triads": len(tri), "docs": 0, **counts}}
        docs = docs_for(ep)
        summary["eps"][ep]["counts"]["docs"] = len(docs)
        wb = {"ep": ep, "vo": {"ua": ua, "en": en, "settings_hero": e.get("vo_settings", ""), "tone": e.get("tone", ""),
                               "wpm": e.get("wpm", "")},
              "music": music, "prompts": prompts, "triads": tri, "veo": vk, "media": med, "docs": docs,
              "visual_key": e.get("visual_key", ""), "lens": e.get("camera_lens", ""), "bin_rule": e.get("smart_bin_rule", ""),
              "acts": [{"n": a.get("actNum"), "t": a.get("title"), "time": a.get("time"), "music": a.get("music_desc", "")}
                       for a in e.get("full_acts", [])]}
        with open(os.path.join(OUT, f"ep{ep}.js"), "w", encoding="utf-8") as fh:
            fh.write("// Згенеровано 08_AUTOMATION/build_episode_workbench.py — не редагувати вручну\n")
            fh.write(f'window.WB=window.WB||{{}};window.WB["{ep}"]=' + json.dumps(wb, ensure_ascii=False, separators=(",", ":")) + ";\n")
        print(f"EP{ep}: {pct:3d}% · медіа {len(med):3d} (власні {len(med)-len(picks)}, підібрано {len(picks)}) · "
              f"VO {n_rec}/{n_blocks} · музика {n_mus}/{len(music)} · документів {len(docs)}")

    with open(os.path.join(OUT, "summary.js"), "w", encoding="utf-8") as fh:
        fh.write("// Згенеровано 08_AUTOMATION/build_episode_workbench.py — не редагувати вручну\n")
        fh.write("window.WB_SUMMARY=" + json.dumps(summary, ensure_ascii=False, separators=(",", ":")) + ";\n")
    print("Розподіл:", dict(pool_stats))


if __name__ == "__main__":
    main()
