#!/usr/bin/env python3
"""
Ingests & organizes the newly generated Google Flow / Veo videos (#01-#04)
and generated images (#01-#07 + B-roll stills & 3D studies) from ~/Downloads
into cleanly separated Video vs Image directories in 05_RAW_FOOTAGE/,
creates web streaming assets in 07_DASHBOARD/assets/, and builds EP01_MEDIA_CATALOG.
"""

import json
import os
import shutil
import subprocess
from pathlib import Path
from PIL import Image

DL = Path("/Users/volodymyrkatasonov/Downloads")
ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
if not os.path.exists(FFMPEG):
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

# Separated Raw Media Directories
RAW_FLOW_RENDERS = ROOT / "05_RAW_FOOTAGE" / "flow_renders"
RAW_FLOW_VIDEOS = ROOT / "05_RAW_FOOTAGE" / "flow_videos" / "EP01_Altman"
RAW_FLOW_PREVIS_ARCHIVE = ROOT / "05_RAW_FOOTAGE" / "flow_previs_animatics"
RAW_FLOW_IMG_PRIMARY = ROOT / "05_RAW_FOOTAGE" / "flow_images" / "EP01_Altman" / "01_primary_keyframes"
RAW_FLOW_IMG_BROLL = ROOT / "05_RAW_FOOTAGE" / "flow_images" / "EP01_Altman" / "02_broll_stills_and_studies"

# Web Dashboard Preview Directories
WEB_FLOW_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "flow"
WEB_FLOW_IMG = ROOT / "07_DASHBOARD" / "assets" / "flow_keyframes"

for d in [
    RAW_FLOW_RENDERS,
    RAW_FLOW_VIDEOS,
    RAW_FLOW_PREVIS_ARCHIVE,
    RAW_FLOW_IMG_PRIMARY,
    RAW_FLOW_IMG_BROLL,
    WEB_FLOW_VID,
    WEB_FLOW_IMG,
]:
    d.mkdir(parents=True, exist_ok=True)

# Move old synthetic EP01 pre-vis animatics (#05-#10) out of flow_renders/ into flow_previs_animatics/
# so flow_renders/ strictly holds ONLY real rendered EP01 videos (#01-#04) (+ EP02-EP10 pre-vis until replaced)
for num in ["05", "06", "07", "08", "09", "10"]:
    for f in RAW_FLOW_RENDERS.glob(f"ep01_flow_{num}_*.mp4"):
        shutil.move(str(f), str(RAW_FLOW_PREVIS_ARCHIVE / f.name))

# 1. Process the 4 REAL Google Flow / Veo Videos (#01 - #04)
VIDEOS = [
    {
        "num": "01",
        "src": DL / "Apple_Macintosh_LC_II_chassis_cd592bb6_1080p.mp4",
        "smart_bin": "ep01_flow_01_mac_chassis.mp4",
        "archive_master": "EP01_FLOW_VID_01_ACT1_Macintosh_LC_II_Chassis_1080p24.mp4",
        "tc": "0:00–0:15",
        "title": "Macintosh LC II (1993) у променях бурштинового пилу",
        "res": "1920x1080",
        "fps": "24 fps",
        "duration": "7.93s",
    },
    {
        "num": "02",
        "src": DL / "vre.mp4",
        "smart_bin": "ep01_flow_02_crt_code.mp4",
        "archive_master": "EP01_FLOW_VID_02_ACT1_CRT_Assembly_Child_Eye_720p24.mp4",
        "tc": "0:15–0:45",
        "title": "Зелений фосфорний ЕПТ-екран із кодом Асемблера та оком дитини",
        "res": "1280x720",
        "fps": "24 fps",
        "duration": "10.03s",
    },
    {
        "num": "03",
        "src": DL / "bcx.mp4",
        "smart_bin": "ep01_flow_03_silicon_laser.mp4",
        "archive_master": "EP01_FLOW_VID_03_ACT1_Silicon_Wafer_Cyan_Laser_720p24.mp4",
        "tc": "1:30–2:30",
        "title": "Кремнієва пластина під когерентним ціановим лазером",
        "res": "1280x720",
        "fps": "24 fps",
        "duration": "10.03s",
    },
    {
        "num": "04",
        "src": DL / "nhgj k.mp4",
        "smart_bin": "ep01_flow_04_exponential_line.mp4",
        "archive_master": "EP01_FLOW_VID_04_ACT1_Golden_Exponential_Curve_720p24.mp4",
        "tc": "3:30–4:45",
        "title": "Золота експоненціальна лінія масштабування у темряві",
        "res": "1280x720",
        "fps": "24 fps",
        "duration": "10.03s",
    },
]

print("=== [1/3] Copying & Encoding 4 Real Google Flow / Veo Videos (#01–#04) ===")
for v in VIDEOS:
    assert v["src"].exists(), f"Missing video: {v['src']}"
    # Copy untouched original master into both flow_renders/ (for DaVinci V1) and flow_videos/EP01_Altman/
    shutil.copy2(v["src"], RAW_FLOW_RENDERS / v["smart_bin"])
    shutil.copy2(v["src"], RAW_FLOW_VIDEOS / v["archive_master"])

    # Transcode clean web-streaming 720p H.264 + 128k AAC stereo preview into 07_DASHBOARD/assets/video_previews/flow/
    web_dst = WEB_FLOW_VID / v["smart_bin"]
    cmd = [
        FFMPEG, "-y", "-i", str(v["src"]),
        "-vf", "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:black,fps=24",
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        str(web_dst),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  [OK] Video #{v['num']} -> {v['smart_bin']} (raw: {v['src'].stat().st_size//1024} KB, web: {web_dst.stat().st_size//1024} KB)")

# Extract crisp 1080p still keyframe for #01 from 00:04.4 of Apple_Macintosh_LC_II_chassis
kf01_raw = RAW_FLOW_IMG_PRIMARY / "EP01_FLOW_IMG_01_Macintosh_LC_II_Keyframe.jpg"
subprocess.run(
    [
        FFMPEG, "-y", "-ss", "00:00:04.40",
        "-i", str(DL / "Apple_Macintosh_LC_II_chassis_cd592bb6_1080p.mp4"),
        "-frames:v", "1", "-q:v", "2", str(kf01_raw),
    ],
    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
)

# 2. Organize All Generated Images (7 Primary Keyframes + 3 B-Roll Stills + 8 Canvas 3D Studies)
PRIMARY_IMAGES = [
    {
        "num": "01",
        "src": kf01_raw,
        "dst_name": "EP01_FLOW_IMG_01_Macintosh_LC_II_Keyframe.jpg",
        "web_name": "ep01_flow_kf_01_mac_chassis.jpg",
        "title": "Кадр #01 • Macintosh LC II у променях теплого пилу (1993)",
        "tc": "0:00–0:15",
        "status": "Відео готове (#01)",
    },
    {
        "num": "02",
        "src": DL / "hero_p31_crt_macro_1794080396768.jpg",
        "dst_name": "EP01_FLOW_IMG_02_CRT_Code_Eye_Reflection_Hero.jpg",
        "web_name": "ep01_flow_kf_02_crt_code.jpg",
        "title": "Кадр #02 • Зелений ЕПТ-екран з кодом Асемблера та оком дитини",
        "tc": "0:15–0:45",
        "status": "Відео готове (#02)",
    },
    {
        "num": "03",
        "src": DL / "bgt.png",
        "dst_name": "EP01_FLOW_IMG_03_Silicon_Wafer_Cyan_Laser_Hero.png",
        "web_name": "ep01_flow_kf_03_silicon_laser.jpg",
        "title": "Кадр #03 • Мікросхема кремнієвої пластини під ціановим лазером",
        "tc": "1:30–2:30",
        "status": "Відео готове (#03)",
    },
    {
        "num": "04",
        "src": DL / "bhf.png",
        "dst_name": "EP01_FLOW_IMG_04_Golden_Exponential_Curve_Hero.png",
        "web_name": "ep01_flow_kf_04_exponential_line.jpg",
        "title": "Кадр #04 • Золота експонента масштабування у темному просторі",
        "tc": "3:30–4:45",
        "status": "Відео готове (#04)",
    },
    {
        "num": "05",
        "src": DL / "Camera_moving_through_glowing_nodes_394ac512_2K.jpg",
        "dst_name": "EP01_FLOW_IMG_05_Neural_Lattice_Glowing_Nodes_2K.jpg",
        "web_name": "ep01_flow_kf_05_neural_lattice.jpg",
        "title": "Кадр #05 (2K) • Проліт камери крізь нейронні вузли в обсидіановій порожнечі",
        "tc": "7:00–8:15",
        "status": "Кадр 2K готовий • Очікує відео",
    },
    {
        "num": "06",
        "src": DL / "Supercomputer_servers_in_cold_hall_d85bb00a_2K.jpg",
        "dst_name": "EP01_FLOW_IMG_06_Supercomputer_Servers_Cold_Hall_2K.jpg",
        "web_name": "ep01_flow_kf_06_server_monolith.jpg",
        "title": "Кадр #06 (2K) • Монолітні стійки суперкомп'ютера у холодному тумані",
        "tc": "8:15–9:30",
        "status": "Кадр 2K готовий • Очікує відео",
    },
    {
        "num": "07",
        "src": DL / "Smartphone_on_dark_conference_table_144eb647_2K.jpg",
        "dst_name": "EP01_FLOW_IMG_07_Smartphone_Boardroom_Noir_Rain_2K.jpg",
        "web_name": "ep01_flow_kf_07_boardroom_noir.jpg",
        "title": "Кадр #07 (2K) • Смартфон на порожньому столі ради директорів під дощем",
        "tc": "10:45–12:15",
        "status": "Кадр 2K готовий • Очікує відео",
    },
]

BROLL_AND_STUDIES = [
    {
        "code": "02B",
        "src": DL / "child_eye_reflection_closeup_1794080397538.jpg",
        "dst_name": "EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg",
        "web_name": "ep01_flow_broll_02b_child_eye.jpg",
        "title": "Додатковий кінокадр Акту 1 • Макро дитячого ока з відображенням зеленого коду",
        "tc": "0:25–0:32",
        "web_export": True,
    },
    {
        "code": "02C",
        "src": DL / "phosphor_triad_subpixel_macro_1794080398409.jpg",
        "dst_name": "EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg",
        "web_name": "ep01_flow_broll_02c_phosphor_triad.jpg",
        "title": "Додатковий кінокадр Акту 1 • Мікроскоп зеленого люмінофора P31 за склом ЕПТ",
        "tc": "0:18–0:24",
        "web_export": True,
    },
    {
        "code": "02D",
        "src": DL / "vintage_crt_setup_environment_1794080399328.jpg",
        "dst_name": "EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg",
        "web_name": "ep01_flow_broll_02d_boy_crt_room.jpg",
        "title": "Додатковий кінокадр Акту 1 • 8-річний хлопчик перед монітором у кімнаті 1993 року",
        "tc": "0:33–0:45",
        "web_export": True,
    },
    {
        "code": "STUDY_01A",
        "src": DL / "Macintosh-LC-II-Macro-4K-1794125634527.png",
        "dst_name": "EP01_FLOW_STUDY_01A_Mac_ADB_Ports_Canvas_4K.png",
        "title": "3D-етюд портів ADB / Audio (Canvas 4K v1)",
        "web_export": False,
    },
    {
        "code": "STUDY_01B",
        "src": DL / "Macintosh-LC-II-Macro-4K-1794125748471.png",
        "dst_name": "EP01_FLOW_STUDY_01B_Mac_Texture_Canvas_4K.png",
        "title": "3D-етюд текстури корпусу (Canvas 4K v2)",
        "web_export": False,
    },
    {
        "code": "STUDY_01C",
        "src": DL / "Macintosh-LC-II-Macro-4K-1794125774819.png",
        "dst_name": "EP01_FLOW_STUDY_01C_Mac_Ports_Close_Canvas_4K.png",
        "title": "3D-етюд задньої панелі (Canvas 4K v3)",
        "web_export": False,
    },
    {
        "code": "STUDY_03A",
        "src": DL / "silicon-wafer-octane-macro-4k-1794080264643.png",
        "dst_name": "EP01_FLOW_STUDY_03A_Silicon_Traces_Canvas_4K_v1.png",
        "title": "3D-етюд мідних доріжок чіпа (Canvas 4K v1)",
        "web_export": False,
    },
    {
        "code": "STUDY_03B",
        "src": DL / "silicon-wafer-octane-macro-4k-1794080398160.png",
        "dst_name": "EP01_FLOW_STUDY_03B_Silicon_Traces_Canvas_4K_v2.png",
        "title": "3D-етюд мідних доріжок чіпа (Canvas 4K v2)",
        "web_export": False,
    },
    {
        "code": "STUDY_03C",
        "src": DL / "silicon-wafer-octane-macro-4k-1794080399419.png",
        "dst_name": "EP01_FLOW_STUDY_03C_Silicon_Traces_Canvas_4K_v3.png",
        "title": "3D-етюд мідних доріжок чіпа (Canvas 4K v3)",
        "web_export": False,
    },
    {
        "code": "STUDY_03D",
        "src": DL / "silicon-wafer-octane-macro-8k-1794080404332.png",
        "dst_name": "EP01_FLOW_STUDY_03D_Silicon_Traces_Canvas_8K_v4.png",
        "title": "3D-етюд мідних доріжок чіпа (Canvas 8K v4)",
        "web_export": False,
    },
    {
        "code": "STUDY_04B",
        "src": DL / "vtdsrea.png",
        "dst_name": "EP01_FLOW_STUDY_04B_Exponential_Line_Duplicate.png",
        "title": "Дубль концепт-кадру золотої експоненти",
        "web_export": False,
    },
]


def save_web_jpg(src_path: Path, dst_path: Path, max_w: int = 1600):
    with Image.open(src_path) as im:
        im = im.convert("RGB")
        if im.width > max_w:
            new_h = int(im.height * (max_w / float(im.width)))
            im = im.resize((max_w, new_h), Image.Resampling.LANCZOS)
        im.save(dst_path, "JPEG", quality=88, optimize=True)


print("=== [2/3] Organizing Separated Image Directories & Web Keyframes ===")
for item in PRIMARY_IMAGES:
    dst_raw = RAW_FLOW_IMG_PRIMARY / item["dst_name"]
    if item["src"] != dst_raw:
        shutil.copy2(item["src"], dst_raw)
    web_dst = WEB_FLOW_IMG / item["web_name"]
    save_web_jpg(dst_raw, web_dst)
    with Image.open(dst_raw) as im:
        item["dimensions"] = f"{im.width}x{im.height}"
    print(f"  [OK] Primary Keyframe #{item['num']} -> {dst_raw.name} ({item['dimensions']}) + web {web_dst.name}")

for b in BROLL_AND_STUDIES:
    if not b["src"].exists():
        continue
    dst_raw = RAW_FLOW_IMG_BROLL / b["dst_name"]
    shutil.copy2(b["src"], dst_raw)
    with Image.open(dst_raw) as im:
        b["dimensions"] = f"{im.width}x{im.height}"
    if b.get("web_export") and b.get("web_name"):
        save_web_jpg(dst_raw, WEB_FLOW_IMG / b["web_name"])
    print(f"  [OK] B-Roll / Study {b['code']} -> {dst_raw.name} ({b['dimensions']})")

# 3. Write Master Media Catalog (Markdown + JSON)
print("=== [3/3] Generating Master Media Catalog (EP01_MEDIA_CATALOG.md & .json) ===")
catalog_data = {
    "episode": "EP01 — Sam Altman",
    "updated_at": "2026-11-08",
    "summary": {
        "flow_videos_ready": 4,
        "flow_keyframes_only_ready": 3,
        "flow_in_development": 3,
        "extra_broll_stills": 3,
        "canvas_3d_studies": 8,
        "archival_broll_mp4": 3,
        "uhd_4k_dossiers": 5,
    },
    "directories": {
        "davinci_v1_smart_bin_videos": "05_RAW_FOOTAGE/flow_renders/",
        "master_flow_videos_archive": "05_RAW_FOOTAGE/flow_videos/EP01_Altman/",
        "primary_keyframes_images": "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/",
        "broll_stills_and_studies": "05_RAW_FOOTAGE/flow_images/EP01_Altman/02_broll_stills_and_studies/",
        "historical_archives_mp4": "05_RAW_FOOTAGE/archives/",
        "uhd_4k_dossiers_png": "05_RAW_FOOTAGE/dossiers_press/",
    },
    "videos_01_to_04": [
        {k: v for k, v in x.items() if k != "src"} for x in VIDEOS
    ],
    "primary_keyframes_01_to_07": [
        {k: v for k, v in x.items() if k != "src"} for x in PRIMARY_IMAGES
    ],
    "broll_and_studies": [
        {k: v for k, v in x.items() if k != "src"} for x in BROLL_AND_STUDIES
    ],
}

cat_json_path = ROOT / "05_RAW_FOOTAGE" / "EP01_MEDIA_CATALOG.json"
cat_json_path.write_text(json.dumps(catalog_data, ensure_ascii=False, indent=2), encoding="utf-8")

md_lines = [
    "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP01 (Сем Альтман) — Відео vs Зображення",
    "",
    "> **Статус Пріоритетної Черги Google Flow / Veo (10 базових сцен):**",
    "> - ✅ **Сцени #01–#04:** 4 фінальні відеокліпи `.mp4` (24 fps + стереозвук SFX/Drone) — **ГОТОВІ**",
    "> - 🖼️ **Сцени #05–#07:** 3 фотореалістичні концепт-кадри `2K` — **ГОТОВІ (очікують відео-анімації)**",
    "> - ⏳ **Сцени #08–#10:** **У РОЗРОБЦІ**",
    "",
    "---",
    "",
    "## 📂 Розділена структура директорій у `05_RAW_FOOTAGE/`",
    "",
    "| Призначення | Шлях у проєкті | Вміст |",
    "| :--- | :--- | :--- |",
    "| **Канонічні відео DaVinci V1** | `05_RAW_FOOTAGE/flow_renders/` | 4 готові `.mp4` під авто-імпорт (`ep01_flow_01`..`04`) |",
    "| **Архів відео-майстрів EP01** | `05_RAW_FOOTAGE/flow_videos/EP01_Altman/` | Іменовані майстер-копії відео з метаданими |",
    "| **Головні зображення (Keyframes #01–#07)** | `05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/` | 7 головних кадрів (включно з 2K сценами #05, #06, #07) |",
    "| **Додаткові кінокадри B-Roll та 3D-етюди** | `05_RAW_FOOTAGE/flow_images/EP01_Altman/02_broll_stills_and_studies/` | 3 фотореалістичні кадри Акту 1 + 8 технічних рендерів |",
    "| **Історичні відеоархіви B-Roll** | `05_RAW_FOOTAGE/archives/` | 3 архівні `.mp4` (Сенат США ×2, Macintosh 1992) |",
    "| **Документальні 4K-Досьє** | `05_RAW_FOOTAGE/dossiers_press/` | 5 пластин `3840×2160` PNG |",
    "",
    "---",
    "",
    "## 🎥 ЧАСТИНА 1: Готові Відеофайли Google Flow / Veo (#01–#04)",
    "",
    "| № | Таймкод | Канонічний файл у `flow_renders/` | Роздільність / FPS | Тривалість | Опис |",
    "| :--- | :--- | :--- | :--- | :--- | :--- |",
]
for v in VIDEOS:
    md_lines.append(f"| **#{v['num']}** | `{v['tc']}` | `{v['smart_bin']}` | `{v['res']} • {v['fps']}` | `{v['duration']}` | {v['title']} |")

md_lines += [
    "",
    "---",
    "",
    "## 🖼️ ЧАСТИНА 2: Головні Концепт-Зображення / Keyframes (#01–#07)",
    "",
    "| № | Таймкод | Файл у `01_primary_keyframes/` | Розмір | Статус | Опис |",
    "| :--- | :--- | :--- | :--- | :--- | :--- |",
]
for im_item in PRIMARY_IMAGES:
    md_lines.append(f"| **#{im_item['num']}** | `{im_item['tc']}` | `{im_item['dst_name']}` | `{im_item['dimensions']}` | **{im_item['status']}** | {im_item['title']} |")

md_lines += [
    "",
    "---",
    "",
    "## 🎞️ ЧАСТИНА 3: Додаткові Кінокадри B-Roll (Акт 1) та Технічні Етюди",
    "",
    "| Код | Файл у `02_broll_stills_and_studies/` | Розмір | Примітка |",
    "| :--- | :--- | :--- | :--- |",
]
for b in BROLL_AND_STUDIES:
    if "dimensions" in b:
        md_lines.append(f"| `{b['code']}` | `{b['dst_name']}` | `{b['dimensions']}` | {b['title']} |")

md_lines += [
    "",
    "---",
    "",
    "## ⏳ ЧАСТИНА 4: Сцени у розробці (#08–#10)",
    "",
    "1. **#08 (`13:45–15:30`)** — `ep01_flow_08_golden_signatures.mp4` *(730 золотих світлових ниток єдності інженерів OpenAI)*",
    "2. **#09 (`15:30–17:00`)** — `ep01_flow_09_fusion_torus.mp4` *(Магнітний термоядерний реактор Helion — фіолетово-золота плазма)*",
    "3. **#10 (`18:30–20:00`)** — `ep01_flow_10_earth_horizon.mp4` *(Орбітальний горизонт нічної Землі в золотій нейромережі)*",
    "",
]

cat_md_path = ROOT / "05_RAW_FOOTAGE" / "EP01_MEDIA_CATALOG.md"
cat_md_path.write_text("\n".join(md_lines), encoding="utf-8")
print(f"  [OK] Wrote {cat_md_path} and {cat_json_path}")
