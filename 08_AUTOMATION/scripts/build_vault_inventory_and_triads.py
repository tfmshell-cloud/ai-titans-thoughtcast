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
import json
import hashlib
import shutil
import subprocess
from datetime import datetime
from PIL import Image, ImageOps

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

# Policy-safe substitutions so no Flow / Veo minor safety triggers exist anywhere
SAFETY_PATTERNS = [
    (re.compile(r"\b(?:[1-9]|1[0-7])-year-old\s+(?:Caucasian\s+|Taiwanese-American\s+|British-Cypriot\s+|immigrant\s+|rugged\s+)?(?:boy|child|girl|kid|teenager|teen|grandmaster)'?s?\b", re.I), "young adult scholar"),
    (re.compile(r"\b(?:[1-9]|1[0-7])-year-old\b", re.I), "young college-age"),
    (re.compile(r"\b(?:four|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen)-year-old\s+(?:Caucasian\s+|Taiwanese-American\s+|British-Cypriot\s+|immigrant\s+|rugged\s+)?(?:boy|child|girl|kid|teenager|teen|grandmaster)'?s?\b", re.I), "young adult prodigy"),
    (re.compile(r"\b(?:a\s+|the\s+)?(?:young|little|small|lonely|innocent)\s+(?:Caucasian\s+|Taiwanese-American\s+)?(?:boy|child|kid|girl)'s\b", re.I), "a focused young student's"),
    (re.compile(r"\b(?:young|little|small|lonely|innocent)\s+(?:Caucasian\s+|Taiwanese-American\s+)?(?:boy|child|kid|girl|son)\b", re.I), "young adult student"),
    (re.compile(r"\bchild's\b", re.I), "student's"),
    (re.compile(r"\bboy's\b", re.I), "young strategist's"),
    (re.compile(r"\bgirl's\b", re.I), "young scholar's"),
    (re.compile(r"\bchildren's\b", re.I), "university students'"),
    (re.compile(r"\bchildren\b", re.I), "young scholars"),
    (re.compile(r"\bteenagers?\b", re.I), "young college students"),
    (re.compile(r"\bteens?\b", re.I), "young college students"),
    (re.compile(r"\bteen\b", re.I), "college-age"),
    (re.compile(r"\bkids\b", re.I), "young students"),
    (re.compile(r"\bkid\b", re.I), "young student"),
    (re.compile(r"\bboys\b", re.I), "young students"),
    (re.compile(r"\bboy\b", re.I), "young scholar"),
    (re.compile(r"\bgirls\b", re.I), "young students"),
    (re.compile(r"\bgirl\b", re.I), "young scholar"),
    (re.compile(r"\bchild\b", re.I), "young scholar"),
    (re.compile(r"\byoung son\b", re.I), "young apprentice"),
    (re.compile(r"\btoddler\b|\binfant\b|\bminor\b|\bminors\b", re.I), "young adult apprentice"),
]

FORBIDDEN_RE = re.compile(
    r"\b(boy|boys|boy's|girl|girls|girl's|child|children|child's|kid|kids|teen|teens|teenager|teenagers|toddler|infant|minor|minors|(?:[1-9]|1[0-7])-year-old)\b",
    re.I,
)


def sanitize_flow_prompt(text):
    if not text:
        return ""
    out = str(text).strip()
    for pat, repl in SAFETY_PATTERNS:
        out = pat.sub(repl, out)
    # Clean accidental doubled articles like "a a focused" or "an young"
    out = re.sub(r"\b(a|an)\s+(a|an)\s+", r"\1 ", out, flags=re.I)
    out = re.sub(r"\ban\s+(young|focused|college|university|older)\b", r"a \1", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def verify_policy_safe(prompt_text, label):
    m = FORBIDDEN_RE.search(prompt_text or "")
    if m:
        raise ValueError(f"Unsafe word '{m.group(0)}' detected in {label}: {prompt_text}")


def classify_episode(rel_lower):
    if "ep02_demis_hassabis" in rel_lower:
        return "03"
    m_explicit = re.search(r"(?:^|[^a-z0-9])ep(0[1-9]|10)(?:[^0-9]|$)", rel_lower)
    if m_explicit:
        return m_explicit.group(1)
    if "user_ai_generations" in rel_lower or "user_ai_images" in rel_lower or "altman" in rel_lower:
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
                    thumb = make_thumbnail(fp, ep, is_vid)
                    if thumb:
                        total_thumbs += 1
                    web_prev = find_existing_web_preview(f.lower())
                    entry = {
                        "file": f,
                        "display_name": clean_display_name(f),
                        "rel_path": rel,
                        "web_src": "../../" + rel,
                        "preview_path": web_prev,
                        "thumb": thumb,
                        "cat": cat,
                        "cat_label": cat_label,
                        "size_mb": sz_mb,
                        "ext": ext.lstrip(".").upper(),
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

    # Sort items inside each episode neatly by category & filename
    for ep in inventory:
        inventory[ep]["videos"].sort(key=lambda x: (x["cat"], x["file"].lower()))
        inventory[ep]["images"].sort(key=lambda x: (x["cat"], x["file"].lower()))
        inventory[ep]["audio"].sort(key=lambda x: (x["cat"], x["file"].lower()))

    print(f"[VAULT] Inventory built. Verified/generated {total_thumbs} thumbnails.")
    return inventory


def parse_ep01_triads():
    src = open(os.path.join(ROOT, "08_AUTOMATION/scripts/generate_cinematic_innovations_html.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    items = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == "INNOVATIONS":
                    items = ast.literal_eval(node.value)
                    break
    triads = []
    for it in items:
        triads.append({
            "num": str(it["num"]).zfill(2),
            "id": f"ep01_triad_{str(it['num']).zfill(2)}",
            "title_ua": it["name_ua"],
            "title_en": it["name_en"],
            "tc": it["tc"],
            "act": it["act"],
            "cat_label": it["cat_label"],
            "concept": it["concept"],
            "p1_start": sanitize_flow_prompt(it["p1_start"]),
            "p2_flow": sanitize_flow_prompt(it["p2_flow"]),
            "p3_end": sanitize_flow_prompt(it["p3_end"]),
            "davinci_recipe": it.get("davinci_recipe", ""),
            "sfx_cue": it.get("sfx_cue", ""),
            "status": "todo",
            "file": f"ep01_triad_{str(it['num']).zfill(2)}.mp4",
            "raw_video_path": "",
            "raw_image_path": "",
            "video_preview": "",
            "keyframe_preview": "",
            "specs": "",
        })
    return triads


def parse_markdown_triads(md_path, ep_code):
    raw = open(md_path, encoding="utf-8").read()
    # Split cleanly by ## #NN. headers
    blocks = re.split(r"(?=^## #\d+\.)", raw, flags=re.M)
    triads = []
    for b in blocks:
        m_hdr = re.match(r"^## #(\d+)\.\s+(.+?)\s*/\s*(.+?)\s*$", b, flags=re.M)
        if not m_hdr:
            continue
        num = m_hdr.group(1).zfill(2)
        title_ua = m_hdr.group(2).strip()
        title_en = m_hdr.group(3).strip()

        m_meta = re.search(r"\*\*Таймкод:\*\*\s*`([^`]+)`\s*\|\s*\*\*Акт:\*\*\s*([^|\n]+?)\s*\|\s*\*\*Категорія:\*\*\s*(.+)$", b, flags=re.M)
        tc = m_meta.group(1).strip() if m_meta else "00:00"
        act = m_meta.group(2).strip() if m_meta else "Акт"
        cat_label = m_meta.group(3).strip() if m_meta else "🎬 Сцена"

        m_conc = re.search(r"\*\*Концепція:\*\*\s*(.+)", b)
        concept = m_conc.group(1).strip() if m_conc else ""

        m_dav = re.search(r"\*\*✂️ DaVinci Resolve[^:]*:\*\*\s*(.+)", b)
        davinci = m_dav.group(1).strip() if m_dav else ""

        m_sfx = re.search(r"\*\*🔊 Fairlight SFX:\*\*\s*(.+)", b)
        sfx = m_sfx.group(1).strip() if m_sfx else ""

        # Extract the 3 code blocks in order
        prompts = re.findall(r"```(?:text)?\s*\n(.*?)\n\s*```", b, flags=re.S)
        p1 = sanitize_flow_prompt(prompts[0] if len(prompts) >= 1 else "")
        p2 = sanitize_flow_prompt(prompts[1] if len(prompts) >= 2 else "")
        p3 = sanitize_flow_prompt(prompts[2] if len(prompts) >= 3 else "")

        triads.append({
            "num": num,
            "id": f"ep{ep_code}_triad_{num}",
            "title_ua": title_ua,
            "title_en": title_en,
            "tc": tc,
            "act": act,
            "cat_label": cat_label,
            "concept": concept,
            "p1_start": p1,
            "p2_flow": p2,
            "p3_end": p3,
            "davinci_recipe": davinci,
            "sfx_cue": sfx,
            "status": "todo",
            "file": f"ep{ep_code}_triad_{num}.mp4",
            "raw_video_path": "",
            "raw_image_path": "",
            "video_preview": "",
            "keyframe_preview": "",
            "specs": "",
        })
    return triads


def derive_triad_from_key_prompt(ep, ep_js, kp, idx):
    """Build a vivid physical Frame A -> Flow Morph (A->B) -> End Frame B Triad from a script key beat."""
    num = str(idx + 1).zfill(2)
    lens = ep_js.get("camera_lens", "Panavision C-Series Anamorphic 40mm")
    vkey = ep_js.get("visual_key", "dramatic documentary lighting")
    tc = kp.get("tc", "00:00")
    act_num = kp.get("act", 1)
    act_titles = {a.get("actNum"): a.get("title", f"Акт {a.get('actNum')}") for a in ep_js.get("beat_acts", [])}
    act_label = act_titles.get(act_num, f"Акт {act_num}")
    cue = kp.get("cue_ua", "").strip()
    raw_prompt = sanitize_flow_prompt(kp.get("prompt", ""))

    # Clean trailing --ar or resolution tags so we compose clean A/B prompts
    base_clean = re.sub(r"\s*--ar\s+\d+:\d+", "", raw_prompt).strip().rstrip(".")

    title_short = cue[:62].rstrip(" ,.;:—-") + ("…" if len(cue) > 62 else "")
    title_en = clean_display_name(kp.get("filename", f"EP{ep}_Scene_{num}.mp4"))

    # Determine whether the existing beat prompt is predominantly an abstract/futuristic visual or a grounded scene
    is_abstract = any(k in base_clean.lower() for k in [
        "visualization", "holographic", "abstract", "matrix", "supernova",
        "orbital view", "neural network", "crystalline", "prism", "wave traveling",
        "splitting", "contrast:", "convergence", "macro visualization",
    ])

    if is_abstract:
        cat_label = "🌐 Нейро-Метафора"
        p1_start = sanitize_flow_prompt(
            f"Intimate physical anchor frame for {ep_js['latin']} ({tc}): "
            f"tactile documentary macro of authentic research notebooks, amber tungsten light, "
            f"handwritten mathematical equations on warm parchment beside vintage computing hardware, "
            f"{lens}, 35mm Kodak 2383 film grain --ar 16:9"
        )
        p2_flow = sanitize_flow_prompt(
            f"Seamless continuous optical push-in and particle metamorphosis from the physical desk into living computational geometry: "
            f"ink equations and paper fibers dissolve into glowing light vectors that assemble into ({base_clean}), "
            f"smooth parallax acceleration, 24fps."
        )
        p3_end = sanitize_flow_prompt(
            f"{base_clean}, hyper-detailed volumetric studio light, deep architectural scale, "
            f"photorealistic Octane cinema frame, 8k --ar 16:9"
        )
    else:
        cat_label = "🎬 Сценічний Морф"
        p1_start = sanitize_flow_prompt(
            f"{base_clean}, captured on {lens}, moody naturalistic lighting, crisp tactile textures --ar 16:9"
        )
        p2_flow = sanitize_flow_prompt(
            f"Slow controlled camera push-in and rack-focus through atmospheric dust motes: "
            f"as the subject holds steady, subtle bioluminescent azure and amber mathematical lattice filaments "
            f"emerge from the shadows and weave cleanly through the scene's geometry, transforming realism into conceptual vision, 24fps."
        )
        p3_end = sanitize_flow_prompt(
            f"Conceptual reverse synthesis following '{title_en}': architectural crystalline neural weights glowing in gold and cyan "
            f"hovering cleanly over dark obsidian studio space, echoing the physical geometry of the opening scene, "
            f"cinematic anamorphic framing, 4k --ar 16:9"
        )

    return {
        "num": num,
        "id": f"ep{ep}_triad_{num}",
        "title_ua": title_short or f"Сцена #{num}",
        "title_en": title_en,
        "tc": tc,
        "act": f"Акт {act_num} • {act_label}",
        "cat_label": cat_label,
        "concept": cue or f"Ключовий біт сценарію ({tc}) для {ep_js['name']} — {vkey}.",
        "p1_start": p1_start,
        "p2_flow": p2_flow,
        "p3_end": p3_end,
        "davinci_recipe": f"Edit Page: Optical Flow Smooth Cut між Start Frame A та AI Морфом (Timeline 2.39:1 • 24fps). Color Page: Node Balance -> Kodak 2383 LUT.",
        "sfx_cue": "Фонові дрони Suno 92 BPM (доріжка A3) + низькочастотний суб-імпульс 45Hz на точці морфу.",
        "status": "todo",
        "file": kp.get("filename", f"EP{ep}_VID_{num}.mp4"),
        "raw_video_path": "",
        "raw_image_path": "",
        "video_preview": "",
        "keyframe_preview": "",
        "specs": f"Таймкод {tc} • {lens}",
    }


def link_existing_media_to_triads(ep, triads, old_mp_ep, vault_ep):
    old_fq = old_mp_ep.get("flow_queue", [])
    vault_vids = vault_ep.get("videos", [])
    vault_imgs = vault_ep.get("images", [])

    # Preserve already matched ready items from existing flow_queue by index (1..N) or #num
    for idx, t in enumerate(triads):
        # 1. Check old flow_queue entry at same position
        if idx < len(old_fq):
            oq = old_fq[idx]
            if oq.get("video_preview"):
                t["video_preview"] = oq["video_preview"]
            if oq.get("raw_video_path"):
                t["raw_video_path"] = oq["raw_video_path"]
            if oq.get("raw_image_path"):
                t["raw_image_path"] = oq["raw_image_path"]
            if oq.get("keyframe_preview"):
                t["keyframe_preview"] = oq["keyframe_preview"]
            if oq.get("file"):
                t["file"] = oq["file"]
            if oq.get("specs"):
                t["specs"] = oq["specs"]
            if oq.get("status"):
                t["status"] = oq["status"]

        # 2. Match additional keyframes or flow renders from Vault by scene number token (e.g. _01_, IMG_02)
        num_str = t["num"]
        if not t["raw_video_path"]:
            for v in vault_vids:
                fl = v["file"].lower()
                if re.search(rf"(?:flow_|_){num_str}(?:_|\.|$)", fl):
                    t["raw_video_path"] = v["rel_path"]
                    t["file"] = v["file"]
                    if v.get("preview_path"):
                        t["video_preview"] = v["preview_path"]
                    t["keyframe_preview"] = t["keyframe_preview"] or v["thumb"]
                    t["status"] = "video_ready"
                    break

        if not t["raw_image_path"]:
            for im in vault_imgs:
                fl = im["file"].lower()
                if re.search(rf"(?:img_|kf_|_){num_str}[a-z]?(?:_|\.|$)", fl):
                    t["raw_image_path"] = im["rel_path"]
                    t["keyframe_preview"] = im["preview_path"] or im["thumb"]
                    if t["status"] == "todo":
                        t["status"] = "image_ready"
                    break

        # Ensure keyframe_preview exists if raw_image_path or video has a vault thumb
        if t["raw_video_path"] and not t["keyframe_preview"]:
            for v in vault_vids:
                if v["rel_path"] == t["raw_video_path"] and v["thumb"]:
                    t["keyframe_preview"] = v["thumb"]
                    break
        if t["raw_image_path"] and not t["keyframe_preview"]:
            for im in vault_imgs:
                if im["rel_path"] == t["raw_image_path"] and im["thumb"]:
                    t["keyframe_preview"] = im["thumb"]
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

    # 2. Build 100% policy-safe 3-Prompt Triads for ALL 10 episodes
    triads_pool = {}
    triad_builders = {
        "01": parse_ep01_triads,
        "02": lambda: parse_markdown_triads(os.path.join(ROOT, "04_VIDEO_PROMPTS/ep02_huang_20_triads.md"), "02"),
        "03": lambda: parse_markdown_triads(os.path.join(ROOT, "04_VIDEO_PROMPTS/ep03_hassabis_30_triads.md"), "03"),
    }

    for ep, name_ua, name_en, *_ in EP_META:
        if ep in triad_builders:
            triads = triad_builders[ep]()
        else:
            ep_js_path = os.path.join(DASH_DIR, "data", "episodes", f"ep{ep}.js")
            ep_js = json.loads(open(ep_js_path, encoding="utf-8").read()[len("window.EPISODE_DATA = "):].rstrip(";\n "))
            keys = [p for p in ep_js.get("prompts_100", []) if p.get("is_key")]
            triads = [derive_triad_from_key_prompt(ep, ep_js, kp, i) for i, kp in enumerate(keys)]

        # Link real disk assets
        link_existing_media_to_triads(ep, triads, mp.get(ep, {}), vault.get(ep, {}))

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
