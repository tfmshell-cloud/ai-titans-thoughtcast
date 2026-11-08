#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
DOWNLOADS = Path("/Users/volodymyrkatasonov/Downloads")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"

FLOW_RENDERS_DIR = ROOT / "05_RAW_FOOTAGE" / "flow_renders"
DASH_FLOW_PREV = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "flow"
DOCS_FLOW_PREV = ROOT / "docs" / "assets" / "video_previews" / "flow"
ALT_TAKES_DIR = ROOT / "05_RAW_FOOTAGE" / "archives" / "alternate_takes"

for d in [FLOW_RENDERS_DIR, DASH_FLOW_PREV, DOCS_FLOW_PREV, ALT_TAKES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Find exact files in Downloads
all_downloads = os.listdir(DOWNLOADS)

def find_file(pattern):
    for f in all_downloads:
        if pattern in f:
            return f
    return None

f_phone_en = find_file("Smartphone_lighting_up_on_table")
f_phone_alt = find_file("mnjbhvg.mp4")
f_neural_lattice = find_file("mknojihf.mp4")
f_servers = find_file(" bc.mp4")
f_particles = find_file("Particle_physics_simulation")
f_fusion = find_file("Magnetic_fusion_reactor")
f_earth = find_file("Earth_illuminated_by_neural")

mapping = [
    {
        "num": "05",
        "src_file": f_neural_lattice,
        "target_name": "ep01_flow_05_neural_lattice.mp4",
        "title": "Обсидіанова нейронна решітка (Camera moving through glowing nodes)",
        "specs": "1280×720 • 24 fps • 10.00s • H.264 • Obsidian Neural Lattice"
    },
    {
        "num": "06",
        "src_file": f_servers,
        "target_name": "ep01_flow_06_server_monolith.mp4",
        "title": "Монолітні сервери у холодному тумані (Supercomputer servers in cold hall)",
        "specs": "1280×720 • 24 fps • 10.00s • H.264 • Supercomputer Cold Hall"
    },
    {
        "num": "07",
        "src_file": f_phone_en,
        "target_name": "ep01_flow_07_boardroom_noir.mp4",
        "title": "Смартфон на столі ради директорів під дощем (Boardroom table at midnight)",
        "specs": "1920×1080 • 24 fps • 7.93s • H.264 • English Standard 1080p"
    },
    {
        "num": "08",
        "src_file": f_particles,
        "target_name": "ep01_flow_08_golden_signatures.mp4",
        "title": "730 золотих світлових ниток єдності інженерів OpenAI",
        "specs": "1920×1080 • 24 fps • 7.93s • H.264 • Particle Convergence Core"
    },
    {
        "num": "09",
        "src_file": f_fusion,
        "target_name": "ep01_flow_09_fusion_torus.mp4",
        "title": "Магнітний термоядерний реактор Helion (фіолетово-золота плазма)",
        "specs": "1920×1080 • 24 fps • 7.93s • H.264 • Helion Fusion Torus"
    },
    {
        "num": "10",
        "src_file": f_earth,
        "target_name": "ep01_flow_10_earth_horizon.mp4",
        "title": "Орбітальний горизонт нічної Землі в золотій нейромережі",
        "specs": "1920×1080 • 24 fps • 7.93s • H.264 • Planetary Neural Grid 1080p"
    }
]

print("=== Starting Batch 3 Ingestion ===")

transferred_sources = []

for item in mapping:
    src_name = item["src_file"]
    if not src_name:
        print(f"ERROR: source file for #{item['num']} not found!")
        continue
    
    src_path = DOWNLOADS / src_name
    dest_raw = FLOW_RENDERS_DIR / item["target_name"]
    dest_prev_dash = DASH_FLOW_PREV / item["target_name"]
    dest_prev_docs = DOCS_FLOW_PREV / item["target_name"]
    
    print(f"\nProcessing Scene #{item['num']}: {src_name} -> {item['target_name']}")
    shutil.copy2(src_path, dest_raw)
    print(f"  Copied to raw: {dest_raw} ({dest_raw.stat().st_size} bytes)")
    
    # Generate web preview (copy or transcode with faststart)
    cmd = [
        FFMPEG, "-y", "-i", str(dest_raw),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        "-c:a", "aac", "-b:a", "128k",
        str(dest_prev_dash)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  Generated web preview: {dest_prev_dash} ({dest_prev_dash.stat().st_size} bytes)")
        shutil.copy2(dest_prev_dash, dest_prev_docs)
    else:
        # Fallback to direct copy
        shutil.copy2(dest_raw, dest_prev_dash)
        shutil.copy2(dest_raw, dest_prev_docs)
        print(f"  Direct copy web preview: {dest_prev_dash}")
        
    transferred_sources.append(src_path)

# Backup alternative take of the phone
if f_phone_alt:
    alt_src = DOWNLOADS / f_phone_alt
    alt_dest = ALT_TAKES_DIR / "ep01_flow_07_boardroom_noir_ua_alt.mp4"
    shutil.copy2(alt_src, alt_dest)
    print(f"\nBacked up alternative phone video: {alt_src} -> {alt_dest}")
    transferred_sources.append(alt_src)

print(f"\nTotal files successfully ingested: {len(transferred_sources)}")
