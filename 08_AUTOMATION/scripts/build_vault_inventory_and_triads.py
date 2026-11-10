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
    is_off_topic,
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
        if "flow_previs_animatics" in rel_lower:
            return "previs", "🎞️ Превіз Аніматики"
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


def find_existing_web_preview(fname_lower):
    """Map disk asset to lightweight preview inside 07_DASHBOARD/assets if present."""
    candidates = [
        ("video_previews/flow", [".mp4"]),
        ("video_previews/archives", [".mp4"]),
        ("video_previews/scientific_vfx", [".mp4"]),
        ("video_previews/dossiers", [".mp4"]),
        ("flow_keyframes", [".jpg", ".png"]),
        ("dossiers", [".png", ".jpg"]),
        ("speaker_photos", [".jpg", ".png"]),
    ]
    stem = os.path.splitext(fname_lower)[0]
    for sub, exts in candidates:
        folder = os.path.join(DASH_DIR, "assets", sub)
        if not os.path.isdir(folder):
            continue
        for f in os.listdir(folder):
            fl = f.lower()
            if fl == fname_lower or os.path.splitext(fl)[0] == stem:
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


def build_vault_inventory():
    inventory = {}
    for ep, name_ua, name_en, _, primary_dir, vo_dir in EP_META:
        inventory[ep] = {
            "ep": ep,
            "name": name_ua,
            "latin": name_en,
            "primary_footage_dir": primary_dir,
            "vo_dir": vo_dir,
            "videos": [],
            "images": [],
            "audio": [],
            "summary": {
                "videos_count": 0,
                "images_count": 0,
                "audio_count": 0,
                "vo_count": 0,
                "suno_count": 0,
                "other_audio_count": 0,
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
                st = inventory[ep]["summary"]
                st["total_mb"] = round(st["total_mb"] + sz_mb, 2)

                if is_vid or is_img:
                    cat, cat_label = classify_media_category(rel_lower, is_vid)
                    if is_off_topic(rel):
                        cat, cat_label = "off_topic", "🗄️ Позапроєктний архів"
                    thumb = make_thumbnail(fp, ep, is_vid)
                    if thumb:
                        total_thumbs += 1
                    web_prev = find_existing_web_preview(f.lower())
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

    # Cross-curate visually verified reusable assets across ALL 10 heroes (resource efficiency!)
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

        native_v.sort(key=lambda x: (x["cat"], x["file"].lower()))
        native_i.sort(key=lambda x: (x["cat"], x["file"].lower()))
        cross_v.sort(key=lambda x: (x.get("source_ep", ""), x["cat"], x["file"].lower()))
        cross_i.sort(key=lambda x: (x.get("source_ep", ""), x["cat"], x["file"].lower()))

        st["native_videos_count"] = len(native_v)
        st["cross_videos_count"] = len(cross_v)
        st["videos_count"] = len(native_v) + len(cross_v)

        st["native_images_count"] = len(native_i)
        st["cross_images_count"] = len(cross_i)
        st["images_count"] = len(native_i) + len(cross_i)

        inventory[ep]["videos"] = native_v + cross_v
        inventory[ep]["images"] = native_i + cross_i
        inventory[ep]["audio"].sort(key=lambda x: (x["cat"], x["file"].lower()))

    print(f"[VAULT] Inventory built. Verified/generated {total_thumbs} thumbnails. Applied {matched_rules} cross-hero visual links.")
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
        "25": ["gamer_digitized", "gaming_hardware"],
        "29": ["developers_facing_gpu", "gtx", "server_core"],
        "35": ["golden_transistor_dust", "blackwell_wafer"],
        "45": ["blackwell", "gpu_server_plates", "supercomputer"],
    },
    "03": {
        "03": ["wooden_king"],
        "04": ["chessboard", "chess_knight"],
        "11": ["zx_spectrum"],
        "25": ["bullfrog", "themepark", "gamer_hand"],
        "27": ["cambridge", "gothic", "library"],
        "34": ["fmri", "hippocampus", "neural"],
        "39": ["breakout", "atari"],
        "42": ["go_stone", "seoul", "move_37"],
        "46": ["alphafold", "protein", "casp"],
        "48": ["tokamak", "plasma"],
        "50": ["golden_sphere", "galaxies"],
    },
    "04": {"05": ["backprop", "synapse_storm"]},
    "05": {"09": ["jepa", "world_model"]},
    "06": {"01": ["jerusalem"], "03": ["hinton_door"], "04": ["alexnet"], "10": ["ssi_obsidian"]},
    "07": {"07": ["constitutional_prism"]},
    "08": {"09": ["spatial_intelligence"]},
    "09": {"05": ["attention_vector"]},
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

    # Summary print
    print("\n=== SUMMARY ACROSS ALL 10 EPISODES ===")
    for ep, name_ua, *_ in EP_META:
        s = vault[ep]["summary"]
        tr = triads_pool[ep]
        rdy_v = sum(1 for t in tr if t["status"] == "video_ready")
        rdy_i = sum(1 for t in tr if t["status"] == "image_ready")
        print(f"EP{ep} ({name_ua:15s}): {s['videos_count']:3d} vid | {s['images_count']:3d} img | {s['audio_count']:2d} aud | {len(tr):2d} Flow Triads (✅vid:{rdy_v}, 🖼️img:{rdy_i})")


if __name__ == "__main__":
    main()
