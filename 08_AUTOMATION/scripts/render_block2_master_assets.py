#!/usr/bin/env python3
"""
Render Dedicated 4K Master Assets for Episode 01, Block 2 (Act 2: The YC Presidency & OpenAI Founding)
All video clips rendered at 3840x2160, 24fps, with cinematic slow zoom (1.00 -> 1.04) and precise frame counts.
"""
import os, sys, subprocess

FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
BASE = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE"

v1_dir = os.path.join(BASE, "flow_renders", "v1_block2_master")
v2_dir = os.path.join(BASE, "archives", "v2_block2_master")
os.makedirs(v1_dir, exist_ok=True)
os.makedirs(v2_dir, exist_ok=True)

# 1. Track V1 Dynamic B-Roll Clips
v1_tasks = [
    # (rel_src, target_name, duration_sec)
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP07_FLOW_IMG_03_Nanobots_Repairing_Human_Cell_2K.jpg", "EP01_V1_B2_01_Retro_Cellular_14s.mp4", 14),
    ("flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_07_Smartphone_Boardroom_Noir_Rain_2K.jpg", "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", 15),
    ("flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP06_FLOW_IMG_07_Cybernetic_Singularity_Portal_2K.jpg", "EP01_V1_B2_03_Singularity_Threat_12s.mp4", 12),
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP08_FLOW_IMG_04_Robotic_Arms_Weaving_Golden_Tapestry_2K.jpg", "EP01_V1_B2_04_Robotic_Dexterity_15s.mp4", 15),
    ("flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP03_FLOW_IMG_09_AlphaStar_Swarm_Units_StarCraft_2K.jpg", "EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4", 12),
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP02_FLOW_IMG_07_Star_Encased_By_GPU_Server_Plates_2K.jpg", "EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4", 15),
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP01_FLOW_IMG_05_Businessman_Dissolving_Into_Data_2K.jpg", "EP01_V1_B2_07_Corporate_Transmutation_15s.mp4", 15),
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP10_FLOW_IMG_05_Metropolis_Transforming_Into_Silicon_2K.jpg", "EP01_V1_B2_08_Silicon_Metropolis_14s.mp4", 14),
    ("flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP02_FLOW_IMG_03_Developers_Facing_GPU_Server_Core_2K.jpg", "EP01_V1_B2_09_Researchers_Compute_Core_12s.mp4", 12),
]

# 2. Track V2 Archival Motion Clips
v2_tasks = [
    ("speaker_portraits/young_altman/EP01_IMG_ARCH_08_Altman_TechCrunch_Disrupt_2014_YC_President.jpg", "EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 10),
    ("speaker_portraits/young_altman/EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President.jpg", "EP01_V2_B2_02_Stanford_2014_10s.mp4", 10),
    ("speaker_portraits/young_altman/EP01_IMG_ARCH_02_Altman_Ilya_Sutskever_TAU_2023.jpg", "EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 10),
    ("speaker_portraits/young_altman/EP01_IMG_ARCH_09_Altman_TechCrunch_Disrupt_2019_OpenAI_CEO.jpg", "EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 10),
]

# 3. Dossier Press Announcement
doc_tasks = [
    ("dossiers_press/EP01_DOC_02_ACT2_OpenAI_Introducing_Dec11_2015.png", os.path.join(BASE, "dossiers_press", "EP01_DOC_02_OpenAI_Introducing_12s.mp4"), 12)
]

def render_zoom(src_path, dst_path, dur):
    if os.path.exists(dst_path) and os.path.getsize(dst_path) > 100000:
        print(f"  ✓ Already exists: {os.path.basename(dst_path)}")
        return
    total_frames = dur * 24
    vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.0002,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", src_path,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
        "-t", str(dur),
        "-pix_fmt", "yuv420p", "-r", "24", dst_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Rendered {os.path.basename(dst_path)} ({dur}s, 3840x2160 24fps)")

print("=== Rendering Block 2 Track V1 Dynamic B-Roll Clips ===")
for rel_src, name, dur in v1_tasks:
    src = os.path.join(BASE, rel_src)
    dst = os.path.join(v1_dir, name)
    render_zoom(src, dst, dur)

print("\n=== Rendering Block 2 Track V2 Archival Motion Clips ===")
for rel_src, name, dur in v2_tasks:
    src = os.path.join(BASE, rel_src)
    dst = os.path.join(v2_dir, name)
    render_zoom(src, dst, dur)

print("\n=== Rendering Block 2 Dossier Motion Clip ===")
for rel_src, dst, dur in doc_tasks:
    src = os.path.join(BASE, rel_src)
    render_zoom(src, dst, dur)

print("\n🎉 ALL BLOCK 2 MASTER ASSETS RENDERED SUCCESSFULLY!")
