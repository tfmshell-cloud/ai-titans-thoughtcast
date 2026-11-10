#!/usr/bin/env python3
"""
Builds two unified studio data modules + lightweight 480x270 thumbnails:
  1) 07_DASHBOARD/data/project_vault_inventory.js (window.PROJECT_VAULT_INVENTORY)
     + 07_DASHBOARD/assets/vault_thumbs/epXX/*.jpg
  2) 07_DASHBOARD/data/flow_triads_pool.js (window.FLOW_TRIADS_POOL)
     + updates flow_queue inside 07_DASHBOARD/data/media_acquisition_pool.js
       so ALL 10 episodes share the exact 3-Prompt Triad standard (100% policy-safe).
Mirrors outputs to docs/data/ and docs/assets/vault_thumbs/.
"""
import os
import re
import ast
import sys
import json
import hashlib
import shutil
import subprocess
from datetime import datetime
from PIL import Image, ImageOps

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from triads_data.policy_safety import sanitize_flow_prompt, verify_policy_safe
from triads_data.ep01_altman_50_triads import EP01_TRIADS
from triads_data.ep02_huang_50_triads import EP02_TRIADS
from triads_data.ep04_to_10_triads import EP04_TO_10_TRIADS
from triads_data.media_cross_curator import (
    curate_cross_assets_for_inventory,
    get_display_title_override,
    is_hidden_non_project,
    link_cross_candidates_to_triads,
)
from build_50_scenes_data_part1 import SCENES_PART1
from build_50_scenes_data_part2 import SCENES_PART2

ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
DASH_DIR = os.path.join(ROOT, "07_DASHBOARD")
DOCS_DIR = os.path.join(ROOT, "docs")
THUMBS_DIR = os.path.join(DASH_DIR, "assets", "vault_thumbs")
DOCS_THUMBS_DIR = os.path.join(DOCS_DIR, "assets", "vault_thumbs")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"

EP_META = [
    ("01", "Сем Альтман", "Sam Altman", ["ep01", "altman"],
     "05_RAW_FOOTAGE/user_ai_generations/", "03_AUDIO/voiceover/EP01_ALTMAN/"),
    ("02", "Дженсен Хуанг", "Jensen Huang", ["ep02", "huang", "blackwell", "nvidia"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("03", "Деміс Хассабіс", "Demis Hassabis", ["ep03", "ep02_demis_hassabis", "hassabis"],
     "05_RAW_FOOTAGE/ep02_demis_hassabis/", "03_AUDIO/voiceover/"),
    ("04", "Джеффрі Хінтон", "Geoffrey Hinton", ["ep04", "hinton"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("05", "Ян Лекун", "Yann LeCun", ["ep05", "lecun"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("06", "Ілля Суцкевер", "Ilya Sutskever", ["ep06", "sutskever"],
     "05_RAW_FOOTAGE/flow_images/EP06_Sutskever/", "03_AUDIO/voiceover/"),
    ("07", "Даріо Амодей", "Dario Amodei", ["ep07", "amodei"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("08", "Фей-Фей Лі", "Fei-Fei Li", ["ep08", "feifei", "fei_fei", "fei-fei"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("09", "Йошуа Бенжіо", "Yoshua Bengio", ["ep09", "bengio"],
     "05_RAW_FOOTAGE/", "03_AUDIO/voiceover/"),
    ("10", "Ендрю Ин", "Andrew Ng", ["ep10", "andrew_ng", "_ng_"],
     "05_RAW_FOOTAGE/flow_images/EP10_Ng/", "03_AUDIO/voiceover/"),
]

# Shared policy sanitizer imported from triads_data.policy_safety


def classify_episode(rel_lower):
    if "ep02_demis_hassabis" in rel_lower:
        return "03"
    m_explicit = re.search(r"(?:^|[^a-z0-9])ep(0[1-9]|10)(?:[^0-9]|$)", rel_lower)
    if m_explicit:
        return m_explicit.group(1)
    if "user_ai_generations" in rel_lower or "user_ai_images" in rel_lower or "altman" in rel_lower or "test_typewriter" in rel_lower:
        return "01"
    for ep, _, _, kws, *_ in EP_META:
        if any(k in rel_lower for k in kws):
            return ep
    return None


def classify_media_category(rel_lower, is_video):
    if is_video:
        if "00_transatlantic_flight_morph" in rel_lower:
            return "flight", "✈️ Переліт Альтман → Хассабіс"
        if "01_origins_and_chess" in rel_lower:
            return "chess", "♟️ Шахи & Походження"
        if "02_zx_spectrum_and_games" in rel_lower:
            return "gaming", "🕹️ ZX Spectrum & Геймінг"
        if "03_neuroscience_and_ai" in rel_lower:
            return "neuro", "🧠 Нейронаука & AlphaGo"
        if "04_biology_and_alphafold" in rel_lower:
            return "alphafold", "🧬 AlphaFold & Біологія"
        if "05_go_and_gaming_strategy" in rel_lower:
            return "go_game", "⚪ Гра Go & Стратегія"
        if "archives" in rel_lower:
            return "archive", "📼 Реальний Архів"
        if "scientific_animations" in rel_lower:
            return "sci_vfx", "🔬 Наукові 3D-Анімації (VFX)"
        if "v1_gapless_master" in rel_lower:
            return "flow_gapless", "🎬 Master Таймлайн (V1 Gapless)"
        if "v1_creative_master" in rel_lower:
            return "flow_creative", "🎨 Креативні Flow-Рендери"
        if "v1_block2_master" in rel_lower:
            return "flow_b2", "🧱 Блок 2 Master"
        if "v1_block3_master" in rel_lower:
            return "flow_b3", "🧱 Блок 3 Master"
        if "flow_previs_animatics" in rel_lower or re.search(r"flow_renders/ep(0[2-9]|10)_flow_01_", rel_lower):
            return "previs", "📐 Превіз-макет (Схема)"
        if "flow_renders" in rel_lower or "flow_videos" in rel_lower:
            return "flow", "🚀 Google Flow / Veo"
        if "user_ai_generations" in rel_lower:
            return "ai_gen", "🎥 Авторські ШІ-Генерації"
        if "dossiers_press" in rel_lower or "rendered_cinematic_stills" in rel_lower:
            return "stills", "🗂️ 4K Пластини / Кіно-Відео"
        return "other_vid", "🎥 Інші Відео"
    else:
        if "00_transatlantic_flight_morph" in rel_lower:
            return "flight", "✈️ Переліт (Кадри)"
        if "01_origins_and_chess" in rel_lower:
            return "chess", "♟️ Шахи & Походження"
        if "02_zx_spectrum_and_games" in rel_lower:
            return "gaming", "🕹️ ZX Spectrum & Геймінг"
        if "03_neuroscience_and_ai" in rel_lower:
            return "neuro", "🧠 Нейронаука & AlphaGo"
        if "04_biology_and_alphafold" in rel_lower:
            return "alphafold", "🧬 AlphaFold & Біологія"
        if "05_go_and_gaming_strategy" in rel_lower:
            return "go_game", "⚪ Гра Go & Стратегія"
        if "batch3_gaming_chess_go_science" in rel_lower:
            return "batch3", "🎮 Ігри / Шахи / Наука (2K)"
        if "batch4_cosmic_scale_biology_hardware" in rel_lower:
            return "batch4", "🌌 Космос / Біологія / Кремній (2K)"
        if "01_primary_keyframes" in rel_lower:
            return "keyframes", "🖼️ Головні 2K Keyframes"
        if "02_broll_stills_and_studies" in rel_lower:
            return "broll_stills", "🎨 B-Roll Концепти & Дослідження"
        if "dossiers_press" in rel_lower:
            return "dossiers", "📰 4K Досьє & Преса"
        if "speaker_portraits" in rel_lower:
            return "portraits", "📸 Портрети Спікера"
        if "user_ai_images" in rel_lower or "images_vault" in rel_lower or "user_ai_generations" in rel_lower:
            return "ai_gen_img", "🎨 Авторські ШІ-Кадри"
        return "other_img", "🖼️ Інші Зображення"


def clean_display_name(fname):
    stem = os.path.splitext(fname)[0]
    # Remove long trailing hex UUID hashes for readability while keeping file exact
    cleaned = re.sub(r"_[0-9a-f]{6,12}(?:_\d+p)?$", "", stem, flags=re.I)
    cleaned = cleaned.replace("_", " ").strip()
    return cleaned[:92] if cleaned else stem


def build_pool_preview_lookup():
    """Map raw disk relative paths -> lightweight web previews from media_acquisition_pool.js."""
    lookup = {}
    mp_path = os.path.join(DASH_DIR, "data", "media_acquisition_pool.js")
    if not os.path.exists(mp_path):
        return lookup
    try:
        raw = open(mp_path, encoding="utf-8").read()
        mp = json.loads(raw[len("window.MEDIA_ACQUISITION_POOL = "):].rstrip(";\n "))
    except Exception:
        return lookup

    def reg(raw_p, prev_p):
        if raw_p and prev_p and os.path.exists(os.path.join(DASH_DIR, prev_p)):
            lookup[raw_p.lower()] = prev_p
            lookup[os.path.basename(raw_p).lower()] = prev_p

    for ep_data in mp.values():
        if not isinstance(ep_data, dict):
            continue
        for ph in ep_data.get("archival_photos", []):
            reg(ph.get("raw_file", ""), ph.get("web_preview", ""))
        for d in ep_data.get("dossiers", []):
            reg(d.get("raw_4k_png", ""), d.get("web_preview", ""))
        for g in ep_data.get("flow_gallery", []):
            reg(g.get("raw_path", ""), g.get("web_preview", ""))
        for sc in ep_data.get("scientific_vfx", []):
            reg(sc.get("raw_path", ""), sc.get("web_preview", ""))
        for ar in ep_data.get("archives", []):
            fn = ar.get("file", "")
            vp = ar.get("video_preview", "")
            if fn and vp:
                reg(f"05_RAW_FOOTAGE/archives/{fn}", vp)
    return lookup


def find_existing_web_preview(fname_lower, rel_lower="", pool_prev_map=None):
    """Map disk asset to lightweight preview inside 07_DASHBOARD/assets if present."""
    if pool_prev_map:
        if rel_lower and rel_lower in pool_prev_map:
            return pool_prev_map[rel_lower]
        if fname_lower in pool_prev_map:
            return pool_prev_map[fname_lower]

    candidates = [
        ("video_previews/flow", [".mp4"]),
        ("video_previews/archives", [".mp4"]),
        ("video_previews/science", [".mp4"]),
        ("video_previews/dossiers", [".mp4"]),
        ("video_previews/cards", [".mp4"]),
        ("archival_photos", [".jpg", ".jpeg", ".png"]),
        ("dossiers_preview", [".jpg", ".jpeg", ".png"]),
        ("cards_preview", [".jpg", ".jpeg", ".png"]),
        ("flow_keyframes", [".jpg", ".png"]),
        ("dossiers", [".png", ".jpg"]),
        ("speaker_photos", [".jpg", ".png"]),
    ]
    stem = os.path.splitext(fname_lower)[0]
    m_doc = re.match(r"^(ep\d+_doc_\d+)", stem)
    m_sci = re.match(r"^(ep\d+_sci_\d+)", stem)
    for sub, exts in candidates:
        folder = os.path.join(DASH_DIR, "assets", sub)
        if not os.path.isdir(folder):
            continue
        for f in os.listdir(folder):
            fl = f.lower()
            if fl == fname_lower or os.path.splitext(fl)[0] == stem:
                return f"assets/{sub}/{f}"
            if m_doc and sub in ("video_previews/dossiers", "dossiers_preview") and fl.startswith(m_doc.group(1)):
                return f"assets/{sub}/{f}"
            if m_sci and sub == "video_previews/science" and fl.startswith(m_sci.group(1)):
                return f"assets/{sub}/{f}"
    return ""


def make_thumbnail(src_path, ep, is_video):
    os.makedirs(os.path.join(THUMBS_DIR, f"ep{ep}"), exist_ok=True)
    h = hashlib.md5(src_path.encode("utf-8")).hexdigest()[:8]
    safe_stem = re.sub(r"[^a-zA-Z0-9_-]+", "_", os.path.splitext(os.path.basename(src_path))[0])[:48].strip("_")
    thumb_name = f"{h}_{safe_stem or 'media'}.jpg"
    thumb_abs = os.path.join(THUMBS_DIR, f"ep{ep}", thumb_name)
    thumb_rel = f"assets/vault_thumbs/ep{ep}/{thumb_name}"

    if os.path.exists(thumb_abs) and os.path.getsize(thumb_abs) > 600:
        if os.path.getmtime(thumb_abs) >= os.path.getmtime(src_path):
            return thumb_rel

    if is_video:
        for ss in ("1.0", "0.1"):
            cmd = [
                FFMPEG, "-y", "-ss", ss, "-i", src_path,
                "-vframes", "1", "-q:v", "5",
                "-vf", "scale=480:270:force_original_aspect_ratio=decrease,pad=480:270:(ow-iw)/2:(oh-ih)/2:color=#05070c",
                thumb_abs,
            ]
            res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if res.returncode == 0 and os.path.exists(thumb_abs) and os.path.getsize(thumb_abs) > 600:
                return thumb_rel
        # Last resort at t=0
        cmd0 = [
            FFMPEG, "-y", "-i", src_path, "-vframes", "1", "-q:v", "5",
            "-vf", "scale=480:270:force_original_aspect_ratio=decrease,pad=480:270:(ow-iw)/2:(oh-ih)/2:color=#05070c",
            thumb_abs,
        ]
        subprocess.run(cmd0, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return thumb_rel if os.path.exists(thumb_abs) and os.path.getsize(thumb_abs) > 0 else ""
    else:
        try:
            with Image.open(src_path) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                im.thumbnail((480, 270), Image.Resampling.LANCZOS)
                canvas = Image.new("RGB", (480, 270), (5, 7, 12))
                x = (480 - im.width) // 2
                y = (270 - im.height) // 2
                canvas.paste(im, (x, y))
                canvas.save(thumb_abs, "JPEG", quality=82, optimize=True)
            return thumb_rel
        except Exception as e:
            print(f"[WARN] Failed image thumb for {src_path}: {e}")
            return ""


TECH_CACHE_PATH = os.path.join(os.path.dirname(__file__), "media_tech_cache.json")


def load_tech_cache():
    if os.path.exists(TECH_CACHE_PATH):
        try:
            return json.load(open(TECH_CACHE_PATH, encoding="utf-8"))
        except Exception:
            pass
    return {}


def save_tech_cache(cache):
    try:
        json.dump(cache, open(TECH_CACHE_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    except Exception:
        pass


def probe_media_tech(fp, rel, is_vid, cache):
    mtime = round(os.path.getmtime(fp), 2)
    rec = cache.get(rel)
    if rec and rec.get("mtime") == mtime and rec.get("w") is not None:
        return rec

    with open(fp, "rb") as fh:
        md5 = hashlib.md5(fh.read()).hexdigest()[:8]
    w, h, dur = 0, 0, 0.0
    if is_vid:
        res = subprocess.run([FFMPEG, "-i", fp], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        m_dur = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", res.stderr)
        if m_dur:
            dur = int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))
        m_dim = re.search(r"Video:.*?,\s*(\d{3,4})x(\d{3,4})", res.stderr)
        if m_dim:
            w, h = int(m_dim.group(1)), int(m_dim.group(2))
    else:
        try:
            with Image.open(fp) as im:
                im = ImageOps.exif_transpose(im)
                w, h = im.size
        except Exception:
            pass

    is_portrait = bool(h > w and w > 0)
    if is_vid:
        if is_portrait:
            res_label = f"📱 9:16 ({w}×{h})"
        elif w >= 3800:
            res_label = "4K 16:9"
        elif w >= 1900:
            res_label = "1080p 16:9"
        elif w >= 1200:
            res_label = "720p 16:9"
        else:
            res_label = f"{w}×{h}" if w else "MP4"
        dur_label = f"{int(round(dur))}s" if dur >= 1 else ""
    else:
        if w >= 3800:
            res_label = "🖼️ 4K"
        elif w >= 1900:
            res_label = "🖼️ 2K"
        elif w:
            res_label = f"🖼️ {w}×{h}"
        else:
            res_label = "🖼️ IMG"
        dur_label = ""

    rec = {
        "mtime": mtime,
        "md5": md5,
        "w": w,
        "h": h,
        "dur": round(dur, 1),
        "is_portrait": is_portrait,
        "res_label": res_label,
        "dur_label": dur_label,
    }
    cache[rel] = rec
    return rec


EP_RESEARCH_DIRS = {
    "01": "sam_altman",
    "02": "jensen_huang",
    "03": "demis_hassabis",
    "04": "geoffrey_hinton",
    "05": "yann_lecun",
    "06": "ilya_sutskever",
    "07": "dario_amodei",
    "08": "fei_fei_li",
    "09": "yoshua_bengio",
    "10": "andrew_ng",
}


def collect_research_docs_for_ep(ep, name_ua):
    import unicodedata as _ud
    docs = []
    seen_rel = set()
    res_folder = EP_RESEARCH_DIRS.get(ep, "")
    hero_root = os.path.join(ROOT, "01_RESEARCH", res_folder) if res_folder else ""

    def extract_md_meta(fp):
        title, url, words = "", "", 0
        try:
            txt = open(fp, encoding="utf-8", errors="ignore").read()
            words = len(txt.split())
            for ln in txt.splitlines()[:30]:
                s = ln.strip()
                if not title and s.startswith("# "):
                    title = s[2:].strip()
                if not url:
                    m_u = re.search(r"https?://[^\s)\]>\"'`]+", s)
                    if m_u:
                        url = m_u.group(0).rstrip(".,;:`\"'")
        except Exception:
            pass
        return title, url, words

    if hero_root and os.path.exists(hero_root):
        for r, _, files in os.walk(hero_root):
            for f in sorted(files):
                if f.startswith("."):
                    continue
                fp = os.path.join(r, f)
                rel = os.path.relpath(fp, ROOT)
                rel_lower = rel.lower()
                ext = os.path.splitext(f)[1].lower()
                if ext not in (".md", ".txt", ".pdf", ".json"):
                    continue
                seen_rel.add(rel)
                if "/transcripts/" in rel_lower:
                    cat, cat_lbl = "transcript", "🎙️ Транскрипт"
                elif "/articles/" in rel_lower:
                    cat, cat_lbl = "article", "📰 Стаття / arXiv"
                elif "registry" in rel_lower:
                    cat, cat_lbl = "registry", "🗂️ Медіа-Реєстр"
                else:
                    cat, cat_lbl = "dossier", "🧬 Мастер-Досьє"
                title, url, words = extract_md_meta(fp) if ext in (".md", ".txt") else ("", "", 0)
                docs.append({
                    "file": f,
                    "title": title or clean_display_name(f),
                    "rel_path": rel,
                    "cat": cat,
                    "cat_label": cat_lbl,
                    "ext": ext.lstrip(".").upper(),
                    "word_count": words,
                    "size_kb": round(os.path.getsize(fp) / 1024.0, 1),
                    "source_url": url,
                })

    pdf_dir = os.path.join(ROOT, "01_RESEARCH", "source_pdfs_and_dossiers")
    if os.path.exists(pdf_dir):
        surname = _ud.normalize("NFC", name_ua.split()[-1].lower())
        aliases = [surname]
        if ep == "03":
            aliases.append("гассабіс")
        for f in sorted(os.listdir(pdf_dir)):
            if f.startswith("."):
                continue
            fn_norm = _ud.normalize("NFC", f.lower())
            matched = False
            if "епізод " in fn_norm:
                matched = (f"епізод {ep}" in fn_norm)
            elif f"ep{ep}" in fn_norm:
                matched = True
            else:
                for al in aliases:
                    stem = al[:-1] if len(al) > 4 else al
                    if stem and re.search(rf"(?<![a-zа-яіїєґ0-9]){re.escape(stem)}", fn_norm):
                        if len(al) <= 3:
                            matched = bool(re.search(rf"(?<![a-zа-яіїєґ0-9]){re.escape(al)}(?![a-zа-яіїєґ0-9])", fn_norm))
                        else:
                            matched = True
                        if matched:
                            break
            if not matched:
                continue
            fp = os.path.join(pdf_dir, f)
            rel = os.path.relpath(fp, ROOT)
            if rel in seen_rel:
                continue
            ext = os.path.splitext(f)[1].lower()
            title, url, words = extract_md_meta(fp) if ext in (".md", ".txt") else ("", "", 0)
            docs.append({
                "file": f,
                "title": title or clean_display_name(f),
                "rel_path": rel,
                "cat": "pdf_md",
                "cat_label": "📕 PDF/MD Досьє" if ext == ".pdf" else "📘 Джерело MD",
                "ext": ext.lstrip(".").upper(),
                "word_count": words,
                "size_kb": round(os.path.getsize(fp) / 1024.0, 1),
                "source_url": url,
            })

    cat_order = {"dossier": 0, "registry": 1, "transcript": 2, "article": 3, "pdf_md": 4}
    docs.sort(key=lambda d: (cat_order.get(d["cat"], 9), d["file"].lower()))
    return docs


def build_vault_inventory():
    inventory = {}
    hidden_non_project = []
    tech_cache = load_tech_cache()
    pool_prev_map = build_pool_preview_lookup()
    for ep, name_ua, name_en, _, primary_dir, vo_dir in EP_META:
        r_docs = collect_research_docs_for_ep(ep, name_ua)
        inventory[ep] = {
            "ep": ep,
            "name": name_ua,
            "latin": name_en,
            "primary_footage_dir": primary_dir,
            "vo_dir": vo_dir,
            "videos": [],
            "images": [],
            "audio": [],
            "research_docs": r_docs,
            "summary": {
                "videos_count": 0,
                "images_count": 0,
                "audio_count": 0,
                "vo_count": 0,
                "suno_count": 0,
                "other_audio_count": 0,
                "research_docs_count": len(r_docs),
                "transcripts_count": sum(1 for d in r_docs if d["cat"] == "transcript"),
                "articles_count": sum(1 for d in r_docs if d["cat"] == "article"),
                "research_words": sum(d["word_count"] for d in r_docs),
                "total_mb": 0.0,
            },
        }

    total_thumbs = 0
    for top in ["03_AUDIO", "04_ASSETS", "05_RAW_FOOTAGE"]:
        tp = os.path.join(ROOT, top)
        if not os.path.exists(tp):
            continue
        for r, _, files in os.walk(tp):
            for f in sorted(files):
                if f.startswith("."):
                    continue
                fp = os.path.join(r, f)
                rel = os.path.relpath(fp, ROOT)
                rel_lower = rel.lower()
                ext = os.path.splitext(f)[1].lower()

                ep = classify_episode(rel_lower)
                if not ep:
                    continue

                is_vid = ext in (".mp4", ".mov", ".mkv")
                is_img = ext in (".jpg", ".jpeg", ".png", ".webp")
                is_aud = ext in (".wav", ".mp3", ".m4a")
                if not (is_vid or is_img or is_aud):
                    continue

                sz = os.path.getsize(fp)
                sz_mb = round(sz / (1024.0 * 1024.0), 2)

                if (is_vid or is_img) and is_hidden_non_project(rel):
                    hidden_non_project.append({
                        "file": f,
                        "rel_path": rel,
                        "media_type": "video" if is_vid else "image",
                        "size_mb": sz_mb,
                    })
                    continue

                st = inventory[ep]["summary"]
                st["total_mb"] = round(st["total_mb"] + sz_mb, 2)

                if is_vid or is_img:
                    cat, cat_label = classify_media_category(rel_lower, is_vid)
                    thumb = make_thumbnail(fp, ep, is_vid)
                    if thumb:
                        total_thumbs += 1
                    web_prev = find_existing_web_preview(f.lower(), rel_lower, pool_prev_map)
                    tech = probe_media_tech(fp, rel, is_vid, tech_cache)
                    entry = {
                        "file": f,
                        "display_name": get_display_title_override(rel, clean_display_name(f)),
                        "rel_path": rel,
                        "web_src": "../../" + rel,
                        "preview_path": web_prev,
                        "thumb": thumb,
                        "cat": cat,
                        "cat_label": cat_label,
                        "size_mb": sz_mb,
                        "ext": ext.lstrip(".").upper(),
                        "md5": tech["md5"],
                        "res_label": tech["res_label"],
                        "dur_label": tech["dur_label"],
                        "is_portrait": tech["is_portrait"],
                        "is_dup_md5": False,
                        "is_cross": False,
                        "source_ep": ep,
                        "source_label": f"⭐ Власний асет EP{ep}",
                    }
                    if is_vid:
                        inventory[ep]["videos"].append(entry)
                        st["videos_count"] += 1
                    else:
                        inventory[ep]["images"].append(entry)
                        st["images_count"] += 1
                elif is_aud:
                    st["audio_count"] += 1
                    if "voiceover" in rel_lower:
                        acat, alabel = "vo", "🎙️ Дикторська доріжка (A1)"
                        st["vo_count"] += 1
                    elif "suno_stems" in rel_lower:
                        acat, alabel = "suno", "🎵 Саундтрек Suno (A2/A3)"
                        st["suno_count"] += 1
                    else:
                        acat, alabel = "other_audio", "🔊 Аудіо / Ембієнт"
                        st["other_audio_count"] += 1
                    inventory[ep]["audio"].append({
                        "file": f,
                        "display_name": clean_display_name(f),
                        "rel_path": rel,
                        "web_src": "../../" + rel,
                        "cat": acat,
                        "cat_label": alabel,
                        "size_mb": sz_mb,
                        "ext": ext.lstrip(".").upper(),
                    })

    save_tech_cache(tech_cache)

    # Mark byte-identical MD5 duplicates inside each hero's native vault (keep canonical primary first)
    def folder_priority(entry):
        rl = entry["rel_path"].lower()
        if "images_vault" in rl or "v1_gapless_master" in rl or "01_primary_keyframes" in rl:
            return 0
        if "user_ai_generations/" in rl or "flow_renders/v1_" in rl:
            return 1
        if "ep02_demis_hassabis" in rl and not re.search(r"[^\x20-\x7e]", entry["file"]):
            return 1
        return 2

    for ep in inventory:
        for arr_key in ("videos", "images"):
            arr = inventory[ep][arr_key]
            arr.sort(key=lambda x: (folder_priority(x), x["cat"], x["file"].lower()))
            seen_m = {}
            for it in arr:
                m = it.get("md5", "")
                if m and m in seen_m:
                    it["is_dup_md5"] = True
                    it["dup_of"] = seen_m[m]
                elif m:
                    seen_m[m] = it["file"]

    # Cross-curate visually verified abstract & clean assets across ALL 10 heroes (0 duplicates!)
    native_snapshot = {
        ep: {"videos": list(inventory[ep]["videos"]), "images": list(inventory[ep]["images"])}
        for ep in inventory
    }
    cross_by_ep, matched_rules = curate_cross_assets_for_inventory(native_snapshot)

    for ep in inventory:
        st = inventory[ep]["summary"]
        native_v = inventory[ep]["videos"]
        native_i = inventory[ep]["images"]
        cross_v = cross_by_ep[ep]["videos"]
        cross_i = cross_by_ep[ep]["images"]

        native_v.sort(key=lambda x: (1 if x.get("is_dup_md5") else 0, 1 if x.get("cat") == "previs" else 0, x["cat"], x["file"].lower()))
        native_i.sort(key=lambda x: (1 if x.get("is_dup_md5") else 0, x["cat"], x["file"].lower()))
        cross_v.sort(key=lambda x: (1 if x.get("is_portrait") else 0, x.get("source_ep", ""), x["file"].lower()))
        cross_i.sort(key=lambda x: (x.get("source_ep", ""), x["file"].lower()))

        st["native_videos_count"] = len(native_v)
        st["native_videos_unique"] = sum(1 for x in native_v if not x.get("is_dup_md5"))
        st["cross_videos_count"] = len(cross_v)
        st["videos_count"] = len(native_v) + len(cross_v)

        st["native_images_count"] = len(native_i)
        st["native_images_unique"] = sum(1 for x in native_i if not x.get("is_dup_md5"))
        st["cross_images_count"] = len(cross_i)
        st["images_count"] = len(native_i) + len(cross_i)

        inventory[ep]["videos"] = native_v + cross_v
        inventory[ep]["images"] = native_i + cross_i
        inventory[ep]["audio"].sort(key=lambda x: (x["cat"], x["file"].lower()))

    inventory["_meta"] = {
        "hidden_non_project": hidden_non_project,
        "hidden_videos_count": sum(1 for x in hidden_non_project if x["media_type"] == "video"),
        "hidden_images_count": sum(1 for x in hidden_non_project if x["media_type"] == "image"),
    }
    print(f"[VAULT] Inventory built. Verified {total_thumbs} thumbs. Excluded {len(hidden_non_project)} non-project/test files. Applied {matched_rules} clean cross-hero links.")
    return inventory


def build_ep03_hassabis_50():
    """Normalize 50 Demis Hassabis scenes from SCENES_PART1 + SCENES_PART2, sanitized + synced to EP03 VO chapters."""
    scenes = SCENES_PART1 + SCENES_PART2
    # Map scenes cleanly to EP03_VO_UA_ELEVENLABS_MASTER.txt timecodes & chapters
    def get_vo_meta(n_int):
        if n_int <= 2:
            return ("00:00 – 00:45", "Акт 1 • Лондон 1976", "👶 Коріння & Ремісництво", "Усе у всесвіті є інформацією... Північний Лондон... У богемній квартирі, де батько — музикант і автор пісень...")
        if n_int <= 6:
            return ("00:45 – 01:30", "Акт 1 • Шахи у 4 роки", "♟️ 64 Клітинки порядку", "Чотирирічний хлопчик мовчки стежить за руками батька... Через два тижні починає обігрувати дорослих... острів абсолютного порядку.")
        if n_int <= 14:
            return ("01:30 – 02:45", "Акт 2 • ZX Spectrum 48K", "🕹️ Асемблер Z80", "На призові гроші купує уживаний мікрокомп'ютер ZX Spectrum 48K... Чому біологічний мозок здатний на інтуїцію, а машина приречена на сліпий перебір?")
        if n_int <= 20:
            return ("02:45 – 04:00", "Акт 2 • Рейтинг Ело 2300", "🏆 Майстер ФІДЕ", "У тринадцять років стає майстром ФІДЕ з рейтингом 2300... Найвеличніші уми спалюють життя на дерев'яні фігурки... Час виходити у відкритий океан.")
        if n_int <= 26:
            return ("04:00 – 05:15", "Акт 3 • Bullfrog & Theme Park", "🎡 Перші ШІ-агенти", "У шістнадцять екстерном складає іспити... сам пише ядро культової гри Theme Park... тисячі цифрових агентів породжують живу екосистему.")
        if n_int <= 30:
            return ("05:15 – 06:00", "Акт 3 • Кембридж & Elixir", "🎓 Queens' College", "Закінчивши Кембридж із найвищою відзнакою Double First-Class Honours...")
        if n_int <= 36:
            return ("06:00 – 07:15", "Акт 4 • Нейронаука UCL (fMRI)", "🧠 Гіпокамп і уява", "Захищає докторську з когнітивної нейробіології в UCL... Люди, які втратили пам'ять про минуле, не здатні уявити майбутнє.")
        if n_int <= 40:
            return ("07:15 – 09:30", "Акт 4 • DeepMind 2010 & Breakout", "⚡ Розв'язати інтелект", "Разом із Леггом та Сулейманом засновує DeepMind... Через кілька годин машина сама відкриває в Breakout тунель за стіною цеглин...")
        if n_int <= 44:
            return ("09:30 – 12:15", "Акт 5 • Сеул: Хід 37 (AlphaGo)", "⚫⚪ Машинна креативність", "Березень 2016, Four Seasons Сеул... 37-й хід на 5-ту лінію... людство побачило народження іншопланетної машинної креативності.")
        if n_int <= 47:
            return ("12:15 – 16:45", "Акт 5 • AlphaFold (200 млн білків)", "🧬 Орігамі життя", "Ігри закінчилися... AlphaFold 2 видає точність ширини атома (92 GDT)... відкривають доступ до всіх 200 мільйонів білків людства.")
        if n_int == 48:
            return ("16:45 – 17:45", "Акт 5 • Токамак & GNoME", "⚛️ Термоядерна плазма", "Алгоритми утримують плазму 100 мільйонів градусів всередині Токамака і відкривають 2 млн нових кристалів.")
        if n_int == 49:
            return ("16:00 – 16:45", "Акт 5 • Стокгольм, Нобель 2024", "🏅 Нобелівська з хімії", "Восени 2024 року в Стокгольмі Демісу Гассабісу вручають Нобелівську премію з хімії.")
        return ("17:45 – 21:30", "Акт 5 • Нічна зміна 00:00–04:00", "🔭 Цифровий телескоп", "Працює щоночі з опівночі до четвертої... проектує живу клітину... життя починає читати власний вихідний код.")

    out = []
    for s in scenes:
        n_int = int(s["num"])
        tc, act, cat_lbl, vo_q = get_vo_meta(n_int)
        out.append({
            "num": str(s["num"]).zfill(2),
            "id": f"ep03_triad_{str(s['num']).zfill(2)}",
            "title_ua": s["title"],
            "title_en": f"Hassabis Scene #{s['num']} ({s['period']})",
            "vo_take": f"VO EP03 ({s['period']})",
            "tc": tc,
            "act": act,
            "cat_label": cat_lbl,
            "vo_quote": vo_q + " — " + s["narrative"],
            "symbol": s.get("symbol", ""),
            "concept": s["narrative"],
            "p1_start": sanitize_flow_prompt(s["p1_start"]),
            "p2_flow": sanitize_flow_prompt(s["p2_flow"]),
            "p3_end": sanitize_flow_prompt(s["p3_end"]),
            "davinci_recipe": s.get("davinci_recipe", ""),
            "sfx_cue": s.get("sfx_cue", ""),
            "status": "todo",
            "file": f"ep03_triad_{str(s['num']).zfill(2)}.mp4",
            "raw_video_path": "",
            "raw_image_path": "",
            "video_preview": "",
            "keyframe_preview": "",
            "specs": f"{s['period']} • 24fps",
        })
    return out


def normalize_rich_triad(ep, item):
    num = str(item["num"]).zfill(2)
    return {
        "num": num,
        "id": f"ep{ep}_triad_{num}",
        "title_ua": item["title_ua"],
        "title_en": item.get("title_en", ""),
        "vo_take": item.get("vo_take", f"VO EP{ep}"),
        "tc": item.get("tc", "00:00"),
        "act": item.get("act", "Акт"),
        "cat_label": item.get("cat_label", "🎬 Сцена"),
        "vo_quote": item.get("vo_quote", ""),
        "symbol": item.get("symbol", ""),
        "concept": item.get("vo_quote") or item.get("symbol") or "",
        "p1_start": sanitize_flow_prompt(item["p1_start"]),
        "p2_flow": sanitize_flow_prompt(item["p2_flow"]),
        "p3_end": sanitize_flow_prompt(item["p3_end"]),
        "davinci_recipe": item.get("davinci_recipe", ""),
        "sfx_cue": item.get("sfx_cue", ""),
        "status": "todo",
        "file": f"ep{ep}_triad_{num}.mp4",
        "raw_video_path": "",
        "raw_image_path": "",
        "video_preview": "",
        "keyframe_preview": "",
        "specs": f"{item.get('tc', '')} • 24fps",
    }


# Keyword affinity mapping so existing disk renders & 2K frames bind to the right chronological scene
ASSET_AFFINITY_MAP = {
    "01": {
        "03": ["mac_chassis", "mac_lcii", "macintosh"],
        "05": ["crt_code", "boy_watching", "child_eye", "phosphor"],
        "10": ["floppy", "burroughs", "dorm"],
        "17": ["exponential_line", "curvehero"],
        "20": ["fusion_torus", "helion", "fusion_star"],
        "23": ["golden_signatures", "rosewood"],
        "28": ["neural_lattice", "axons"],
        "31": ["server_monolith", "servercold", "compute_core"],
        "36": ["boardroom_noir", "boardroom_void"],
        "41": ["guest_badge"],
        "42": ["730_letter", "employees_solidarity"],
        "50": ["earth_horizon"],
    },
    "02": {
        "03": ["tamsui_1970", "ep02_img_arch_01"],
        "04": ["chm_oneida_kentucky", "oneida_kentucky", "ep02_img_arch_02"],
        "08": ["oneida_bathrooms", "ua_clip_card_01"],
        "09": ["dennys_dishwasher_notaskbeneath", "aloha_high", "stanford_keynote_portrait"],
        "10": ["ua_clip_card_02", "osu_campus", "ep02_img_arch_04"],
        "12": ["dennys_booth_founding", "dennys_berryessa", "ep02_img_arch_05"],
        "13": ["dennys_booth_inside", "dennys_founding", "ep02_doc_02"],
        "15": ["2013_no_business_plan", "acquired_dgx"],
        "16": ["2009_osu_we_failed", "nv1_die", "ep02_img_arch_06"],
        "20": ["chm_sega_generosity", "ep02_vid_arch_18"],
        "21": ["sega_lifeline", "sega_rescue", "ua_clip_card_03", "ep02_doc_03"],
        "22": ["riva_128", "ep02_img_arch_07"],
        "23": ["morris_chang", "ep02_img_arch_08", "riva_geforce", "ep02_doc_04"],
        "24": ["ua_clip_card_04", "ep02_doc_01"],
        "25": ["geforce_256", "ep02_img_arch_09", "gamer_digitized", "gaming_hardware"],
        "26": ["invented_cuda", "huang_2014_headshot"],
        "28": ["ua_clip_card_05", "huang_gtc_2016", "ep02_img_arch_13"],
        "29": ["evga_gtx580", "gf110_gtx580", "alexnet_gtx580", "developers_facing_gpu"],
        "30": ["acquired_dgx_scale", "ep02_vid_arch_19"],
        "31": ["gtc2016_dgx1", "dgx1_openai", "ep02_doc_06", "dgx_supercomputer"],
        "32": ["ua_clip_card_06", "huang_center_stanford"],
        "34": ["pain_and_suffering", "ua_clip_card_07", "ep02_vid_arch_11"],
        "35": ["blackwell_wafer_reveal", "golden_transistor_dust"],
        "39": ["run_dont_walk", "ua_clip_card_08", "ep02_vid_arch_12"],
        "43": ["nvlink_fiber_rack_pressroom"],
        "45": ["dgx_server_hallway_pressroom", "dgx_b200_hgx", "gpu_server_plates"],
        "49": ["stage_blackvoid_pressroom", "gtc_stage_walk", "ep02_vid_arch_01"],
        "50": ["endeavor_aerial_pressroom", "nvidia_endeavor_hq", "ep02_img_arch_16"],
    },
    "03": {
        "01": ["cradle", "finchley"],
        "02": ["planing", "timber", "plane_blade"],
        "03": ["wooden_king", "wooden_chess", "staunton", "chess_order", "chess_age4"],
        "04": ["chessboard", "chess_knight", "poiss", "childhood_chess", "playing_chess"],
        "05": ["skákborð", "skakbord", "chess_clock", "garde_clock", "staunton"],
        "06": ["chess_order", "chess_age4", "decision_tree"],
        "07": ["finger_slamming", "garde_clock", "playing_chess"],
        "08": ["chess_age4", "childhood_chess"],
        "09": ["wooden_chess", "chess_order", "garde_clock"],
        "10": ["childhood_chess", "chess_age4"],
        "11": ["zx_spectrum", "zx_keyboard", "zx_spectrum_intuition"],
        "12": ["zx_spectrum", "camera_tracking_vintage"],
        "13": ["assembly_code", "programmer_coding", "zx_keyboard"],
        "14": ["pixel_art", "crt_monitor", "playing_chess"],
        "15": ["childhood_chess", "garde_clock"],
        "16": ["playing_chess", "garde_clock"],
        "17": ["chess_age4", "childhood_chess"],
        "18": ["chess_age4", "playing_chess"],
        "19": ["chess_elo2300", "leaving_chess", "liechtenstein"],
        "20": ["leaving_chess", "liechtenstein", "chess_elo2300"],
        "21": ["cambridge_gatehouse", "math_bridge"],
        "22": ["bullfrog", "themepark", "cambridge_gatehouse"],
        "23": ["bullfrog", "themepark"],
        "24": ["programmer_coding", "bullfrog", "themepark"],
        "25": ["bullfrog", "themepark", "gamer_hand"],
        "26": ["themepark", "bullfrog"],
        "27": ["cambridge", "gothic", "library", "cambridge_gatehouse"],
        "28": ["math_bridge", "mathematical_bridge", "cambridge_gatehouse"],
        "29": ["cambridge", "math_bridge"],
        "30": ["cambridge_gatehouse", "hassabis_epfl"],
        "31": ["themepark", "deepmind_2014"],
        "32": ["neuroscience_brain", "ucl_main"],
        "33": ["ucl_main", "pnas", "ucl_hippocampus", "neuroscience_brain"],
        "34": ["fmri", "hippocampus", "neural", "ucl_main", "pnas_2007"],
        "35": ["pnas_2007", "ucl_hippocampus", "royal_society"],
        "36": ["pnas_2007", "neuroscience_brain", "deepmind_2014"],
        "37": ["solve_intelligence", "two_step", "deepmind_2014", "deepmind_kingscross"],
        "38": ["deepmind_2014", "hassabis_epfl", "two_step_plan"],
        "39": ["breakout", "atari", "deepmind_2014"],
        "40": ["google_650m", "military_ethics", "deepmind_kingscross"],
        "41": ["goban", "seoul", "alphago_seoul"],
        "42": ["go_stone", "goban", "seoul", "move_37", "move37"],
        "43": ["move37", "move_37", "seoul"],
        "44": ["move37", "breakout", "goban"],
        "45": ["alphafold_protein", "protein_fold", "alphafold_znf555"],
        "46": ["alphafold", "protein", "casp", "rna_polymerase"],
        "47": ["200m_proteins", "alphafold_gift", "alphafold2"],
        "48": ["tokamak", "plasma"],
        "49": ["nobel", "royal_society", "stockholm", "agi_horizon"],
        "50": ["golden_sphere", "galaxies", "source_code_finale", "agi_horizon"],
    },
    "04": {
        "01": ["ancestry_boole", "joan_los_alamos", "boole_everest", "george_boole", "mount_everest"],
        "02": ["cambridge_kingscollege", "carpenter_honesty", "error_geometry"],
        "03": ["london_carpentry", "carpenter_honesty", "boole_everest"],
        "04": ["edinburgh_informatics", "second_ai_winter", "thirty_years_winter"],
        "05": ["backprop", "synapse_storm", "boltzmann_machine", "backpropagation_nobel"],
        "06": ["sejnowski_1980s", "pentagon_toronto", "toronto_sandford", "boltzmann_1985"],
        "07": ["two_students_gpus", "alexnet", "toronto_bahen", "benchmarks_curve"],
        "08": ["dnnresearch_auction", "lake_tahoe_2012", "alexnet_2012"],
        "09": ["leaving_google", "bbc_regret", "digital_weights", "60minutes_species", "google_exit"],
        "10": ["nobel_warning", "banquet_existential", "uoft_students_nobel", "nobel_lecture", "hopfield_hinton"],
    },
    "05": {
        "01": ["paris_1977", "tektronix_475a", "mos_6502", "soldering_eye"],
        "02": ["chomsky_piaget", "esiee_paris", "piaget_constructivism"],
        "03": ["minsky_perceptrons", "minsky_pencil", "marvin_minsky", "sorbonne_paris"],
        "04": ["1989_convnet_restored", "hubel_wiesel", "bell_labs_holmdel", "young_bell_labs", "belllabs_1989"],
        "05": ["20_percent_us_checks", "lenet_checks", "bell_labs_dsp", "lenet5"],
        "06": ["neural_net_winter", "supersonic_exile", "courant_nyu", "minnesota_cnn"],
        "07": ["fair_pytorch", "gutenberg_printing_press", "gutenberg_openai", "meta_menlo_park", "gutenberg_press_mainz"],
        "08": ["house_cat", "no_agi_by_scaling", "cat_vs_llm", "cat_animal_locomotion"],
        "09": ["ep05_flow_01_jepa", "jepa_world_model", "jepa_architecture", "baby_3d"],
        "10": ["davos_2026_embodied", "sailing_badewind", "close_hauled_finale", "lecun_eu_2026"],
    },
    "06": {
        "01": ["gorky_winter_1986", "jerusalem_walls", "jerusalem_axion", "jerusalem_limestone"],
        "02": ["jerusalem_panorama", "uoft_university_college", "simons_lecture"],
        "03": ["studying_with_hinton", "room4306_toronto", "uoft_sandford_fleming", "hinton_door"],
        "04": ["seq2seq_scaling", "seq2seq_vector", "jensen_huang_alexnet", "gtx580_alexnet_die", "alexnet"],
        "05": ["openai_origins", "openai_pioneer_building", "stanford_quad_2012", "sutskever_googlebrain_2014"],
        "06": ["detective_novel_metaphor", "compression_learning", "agatha_christie"],
        "07": ["gpt_emergent_behaviors", "deep_learning_alchemy", "scaling_10x", "scaling_laws_servers", "next_token_dwarkesh"],
        "08": ["agi_effigy_bonfire", "bonfire_superalignment", "superalignment_safety"],
        "09": ["sutskever_tau_2023", "end_of_pretraining", "nov2023_rift", "sutskever_regret"],
        "10": ["ep06_flow_01_ssi_obsidian", "age_of_research_ssi", "ssi_scale_in_peace", "ssi_monolith", "brain_biological_computer", "convocation_hall_2025", "silent_sanctuary"],
    },
    "07": {
        "01": ["sf_mission_era", "tuscan_leather", "san_francisco_victorian", "leather_and_illness", "stanford_quad"],
        "02": ["leather_and_illness", "ep07_doc_02", "stanford_quad", "stanford_university_physics", "biophysics_physics_path"],
        "03": ["camera_traversing_human_retina", "retinal_ganglion", "princeton_icahn", "princeton_jadwin", "biophysics_physics_path", "princeton_retina_2011", "ep07_flow_img_01"],
        "04": ["scaling_laws_line", "ep07_doc_03", "scaling_power_laws", "scaling_smoothness", "baidu_shangdi", "googleplex43", "tpu_v3_scaling", "ep07_flow_img_02", "ilya_models_want_learn"],
        "05": ["silent_exodus_anthropic", "why_left_openai", "openai_pioneer", "cofounders_gpt2_safety", "ep07_doc_04"],
        "06": ["claude_shannon", "anthropic_howard", "ep07_doc_04", "race_to_the_top", "amodei_disrupt_2023", "white_house_2023", "downing_street_2023"],
        "07": ["constitutional_prism", "constitutional_ai_origin", "constitutional_ai_principles", "claude_shannon_prism", "ep07_doc_01", "ep07_flow_img_04"],
        "08": ["mech_interp_microscope", "ep07_doc_05", "chrisolah_mech_interp", "ep07_flow_img_05", "hands_cupping_levitating"],
        "09": ["asl_biosecurity_vow", "asl_levels_cofounders", "senate_biosecurity_hearing", "senate_testimony_human_level", "catastrophic_cbrn", "bsl4_containment", "ep07_doc_06", "amodei_tokyo_2025"],
        "10": ["loving_grace_finale", "cancer_dna_microscopes", "cancer_fluorescence", "nanobots_repairing_human_cell", "ep07_flow_img_03", "ep07_doc_06"],
    },
    "08": {
        "01": ["immigrant_20dollars", "chengdu_heritage", "english_chinese_dict", "laundry_silhouette", "father_camera_lens"],
        "02": ["ormont_double_life", "laundries_princeton", "ormont_iron_press", "princeton_einstein", "ep08_doc_02", "princeton_nassau"],
        "03": ["mother_blessing", "wall_street_nyse", "caltech_vision_phd", "caltech_beckman", "ep08_doc_03"],
        "04": ["dark_basement_data", "sleeping_cat_vision", "cambrian_trilobite", "cambrian_explosion", "ep08_flow_img_01", "asteroid_approaching"],
        "05": ["mechanical_turk", "imagenet_15m_bigdata", "imagenet_14m_miami", "cambrian_eye", "ep08_doc_01", "ep08_doc_04", "asteroid_entering"],
        "06": ["drycleaner_fund", "imagenet_stage", "imagenet_mturk", "ep08_doc_04", "stanford_gates_cs"],
        "07": ["maternity_ward_alexnet", "convolutional_net_hinton", "hinton_alexnet_toronto", "imagenet_curve", "ep08_doc_05", "googleplex_cloud"],
        "08": ["hospital_smart_sensors", "hai_human_dignity", "human_dignity_agency", "hospital_bedside", "stanford_hai_roundtable", "feifei_aiforgood", "robotic_arms"],
        "09": ["spatial_intelligence", "world_labs_mission", "ep08_doc_06", "ep08_flow_img_02", "world_labs_3d_lidar"],
        "10": ["spatial_north_star", "young_immigrants_voice", "humanitarian_award", "ep08_flow_img_03", "ep08_doc_06"],
    },
    "09": {
        "01": ["parents_freedom", "paris_latin_quarter", "paris_theatre_carlo", "isaac_asimov", "paris_mcgill_bell_labs"],
        "02": ["reading_hinton_mcgill", "mcgill_arts_phd", "bell_labs_holmdel", "udem_roger_gaudry", "academic_independence", "ep09_doc_02"],
        "03": ["ai_winter_abandoned", "montreal_winter_skyline", "ai_winter_family_lab", "ep09_doc_03"],
        "04": ["distributed_word_vectors", "neural_nlp_ten_years", "word_embeddings_board", "word_embeddings_cosmos", "ep09_doc_03", "ep09_flow_img_01"],
        "05": ["attention_vector", "attention_translating_book", "soft_attention_googletranslate", "attention_mechanism", "attention_2014", "ep09_doc_01", "ep09_flow_img_03"],
        "06": ["not_for_sale_mila", "academic_independence", "bengio_open_science", "ep09_doc_04"],
        "07": ["mila_medicine_climate", "saint_laurent_mila", "bengio_iclr_stage", "ep09_doc_04"],
        "08": ["grandson_diaryofaceo", "un_safety_report", "senate_testimony", "us_capitol_senate", "bletchley_summit", "un_security_council", "ep09_doc_05", "ep09_flow_img_02"],
        "09": ["scientistai_humility", "gflownets_molecules", "turing_pioneers_system2", "gflownet_molecules", "grandson_scientist_ai", "ep09_doc_05", "asteroid_coasting"],
        "10": ["introvert_love_future", "winter_bicycle_quebec", "canada_aurora_finale", "bicycle_moral_bastion", "conscience_compass", "ep09_doc_06", "asteroid_surface"],
    },
    "10": {"01": ["medical_textbook"], "05": ["global_neural_classroom"]},
}


def link_existing_media_to_triads(ep, triads, old_mp_ep, vault_ep):
    vault_vids = vault_ep.get("videos", [])
    vault_imgs = vault_ep.get("images", [])
    aff = ASSET_AFFINITY_MAP.get(ep, {})

    for t in triads:
        num_str = t["num"]
        kws = aff.get(num_str, [])
        if kws:
            for v in vault_vids:
                fl = (v["file"] + " " + v["rel_path"]).lower()
                if any(k in fl for k in kws):
                    t["raw_video_path"] = v["rel_path"]
                    t["file"] = v["file"]
                    if v.get("preview_path"):
                        t["video_preview"] = v["preview_path"]
                    t["keyframe_preview"] = v["thumb"]
                    t["status"] = "video_ready"
                    break
            for im in vault_imgs:
                fl = (im["file"] + " " + im["rel_path"]).lower()
                if any(k in fl for k in kws):
                    t["raw_image_path"] = im["rel_path"]
                    t["keyframe_preview"] = t["keyframe_preview"] or im["preview_path"] or im["thumb"]
                    if t["status"] == "todo":
                        t["status"] = "image_ready"
                    break


def main():
    os.makedirs(THUMBS_DIR, exist_ok=True)
    os.makedirs(DOCS_THUMBS_DIR, exist_ok=True)

    # 1. Vault inventory + thumbnails
    vault = build_vault_inventory()

    # Load existing media_acquisition_pool.js to preserve archives, dossiers, voiceover, audio, sci_vfx, flow_gallery
    mp_path = os.path.join(DASH_DIR, "data", "media_acquisition_pool.js")
    mp_raw = open(mp_path, encoding="utf-8").read()
    mp = json.loads(mp_raw[len("window.MEDIA_ACQUISITION_POOL = "):].rstrip(";\n "))

    # 2. Build 100% policy-safe documentary 3-Prompt Triads for ALL 10 episodes:
    #    EP01 = 50, EP02 = 50, EP03 = 50, EP04..EP10 = 10 each (Total 220 Triads / 660 Prompts)
    triads_pool = {}
    for ep, name_ua, name_en, *_ in EP_META:
        if ep == "01":
            triads = [normalize_rich_triad("01", it) for it in EP01_TRIADS]
        elif ep == "02":
            triads = [normalize_rich_triad("02", it) for it in EP02_TRIADS]
        elif ep == "03":
            triads = build_ep03_hassabis_50()
        else:
            triads = [normalize_rich_triad(ep, it) for it in EP04_TO_10_TRIADS[ep]]

        link_existing_media_to_triads(ep, triads, mp.get(ep, {}), vault.get(ep, {}))
        link_cross_candidates_to_triads(ep, triads, vault.get(ep, {}))

        # Verify 100% policy safety on ALL 3 prompts per triad
        for t in triads:
            verify_policy_safe(t["p1_start"], f"EP{ep} #{t['num']} P1")
            verify_policy_safe(t["p2_flow"], f"EP{ep} #{t['num']} P2")
            verify_policy_safe(t["p3_end"], f"EP{ep} #{t['num']} P3")

        triads_pool[ep] = triads

        # Synchronize media_acquisition_pool[ep].flow_queue with the exact same Triad items
        if ep in mp:
            synced_fq = []
            for t in triads:
                synced_fq.append({
                    "num": t["num"],
                    "status": t["status"],
                    "title": t["title_ua"],
                    "title_en": t["title_en"],
                    "file": t["file"],
                    "tc": t["tc"],
                    "act": t["act"],
                    "cat_label": t["cat_label"],
                    "vo_take": t.get("vo_take", ""),
                    "vo_quote": t.get("vo_quote", ""),
                    "symbol": t.get("symbol", ""),
                    "concept": t["concept"],
                    "specs": t["specs"],
                    "prompt": t["p2_flow"],
                    "p1_start": t["p1_start"],
                    "p2_flow": t["p2_flow"],
                    "p3_end": t["p3_end"],
                    "davinci_recipe": t["davinci_recipe"],
                    "sfx_cue": t["sfx_cue"],
                    "video_preview": t["video_preview"],
                    "keyframe_preview": t["keyframe_preview"],
                    "raw_video_path": t["raw_video_path"],
                    "raw_image_path": t["raw_image_path"],
                    "cross_candidates": t.get("cross_candidates", []),
                })
            mp[ep]["flow_queue"] = synced_fq

    # Write project_vault_inventory.js
    vault_js_out = "window.PROJECT_VAULT_INVENTORY = " + json.dumps(vault, ensure_ascii=False, indent=2) + ";\n"
    open(os.path.join(DASH_DIR, "data", "project_vault_inventory.js"), "w", encoding="utf-8").write(vault_js_out)
    open(os.path.join(DOCS_DIR, "data", "project_vault_inventory.js"), "w", encoding="utf-8").write(vault_js_out)

    # Write flow_triads_pool.js
    triads_js_out = "window.FLOW_TRIADS_POOL = " + json.dumps(triads_pool, ensure_ascii=False, indent=2) + ";\n"
    open(os.path.join(DASH_DIR, "data", "flow_triads_pool.js"), "w", encoding="utf-8").write(triads_js_out)
    open(os.path.join(DOCS_DIR, "data", "flow_triads_pool.js"), "w", encoding="utf-8").write(triads_js_out)

    # Update media_acquisition_pool.js in both 07_DASHBOARD/data and docs/data
    mp_out = "window.MEDIA_ACQUISITION_POOL = " + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n"
    open(mp_path, "w", encoding="utf-8").write(mp_out)
    open(os.path.join(DOCS_DIR, "data", "media_acquisition_pool.js"), "w", encoding="utf-8").write(mp_out)

    # Sync thumbnails directory cleanly to docs/assets/vault_thumbs/
    if os.path.exists(DOCS_THUMBS_DIR):
        shutil.rmtree(DOCS_THUMBS_DIR)
    shutil.copytree(THUMBS_DIR, DOCS_THUMBS_DIR)

    # Summary print + 08_METADATA manifests (EP01..EP06)
    print("\n=== SUMMARY ACROSS ALL 10 EPISODES ===")
    meta_dirs = {
        "01": "EP01_SAM_ALTMAN",
        "02": "EP02_JENSEN_HUANG",
        "03": "EP03_DEMIS_HASSABIS",
        "04": "EP04_GEOFFREY_HINTON",
        "05": "EP05_YANN_LECUN",
        "06": "EP06_ILYA_SUTSKEVER",
        "07": "EP07_DARIO_AMODEI",
        "08": "EP08_FEI_FEI_LI",
        "09": "EP09_YOSHUA_BENGIO",
    }
    for ep, name_ua, name_en, *_ in EP_META:
        s = vault[ep]["summary"]
        tr = triads_pool[ep]
        rdy_v = sum(1 for t in tr if t["status"] == "video_ready")
        rdy_i = sum(1 for t in tr if t["status"] == "image_ready")
        print(f"EP{ep} ({name_ua:15s}): {s['videos_count']:3d} vid | {s['images_count']:3d} img | {s['audio_count']:2d} aud | {len(tr):2d} Flow Triads (✅vid:{rdy_v}, 🖼️img:{rdy_i})")
        if ep in meta_dirs:
            mdir = os.path.join(ROOT, "08_METADATA", meta_dirs[ep])
            os.makedirs(mdir, exist_ok=True)
            mp_ep = mp.get(ep, {})
            manifest = {
                "episode_id": f"EP{ep}",
                "hero": name_en,
                "hero_ua": name_ua,
                "bpm": 92,
                "status": "ASSETS_INGESTED_AND_SYNCED",
                "updated_at": datetime.now().strftime("%Y-%m-%d"),
                "research_directory": f"01_RESEARCH/{EP_RESEARCH_DIRS.get(ep, '')}/",
                "summary": {
                    "research_docs_count": s.get("research_docs_count", 0),
                    "transcripts_count": s.get("transcripts_count", 0),
                    "articles_count": s.get("articles_count", 0),
                    "research_words": s.get("research_words", 0),
                    "videos_total": s.get("videos_count", 0),
                    "videos_native": s.get("native_videos_count", 0),
                    "images_total": s.get("images_count", 0),
                    "images_native": s.get("native_images_count", 0),
                    "archival_videos": len(mp_ep.get("archives", [])),
                    "archival_photos": len(mp_ep.get("archival_photos", [])),
                    "dossiers_4k": len(mp_ep.get("dossiers", [])),
                    "flow_triads": len(tr),
                    "audio_stems": len(mp_ep.get("audio", [])),
                },
                "research_sources": [
                    {"title": d["title"], "rel_path": d["rel_path"], "url": d["source_url"], "words": d["word_count"]}
                    for d in vault[ep].get("research_docs", [])
                ],
                "archival_clips": [a.get("file") for a in mp_ep.get("archives", [])],
                "archival_photos": [p.get("raw_file") for p in mp_ep.get("archival_photos", [])],
            }
            open(os.path.join(mdir, "manifest.json"), "w", encoding="utf-8").write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
