#!/usr/bin/env python3
"""
Render exact-duration 24fps MP4 video clips with subtle slow cinematic drift
to ensure Track V1 has 100% GAPLESS coverage from 00:00 to 03:58 (238 seconds).
"""
import subprocess, os

FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
base_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE"
out_dir = os.path.join(base_dir, "flow_renders", "v1_gapless_master")
os.makedirs(out_dir, exist_ok=True)

tasks = [
    # (source_rel_path, target_filename, duration_sec)
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg", "EP01_CLIP_V1_05_Eye_Code_11s.mp4", 11),
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg", "EP01_CLIP_V1_06_Boy_Room_12s.mp4", 12),
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg", "EP01_CLIP_V1_07_Phosphor_12s.mp4", 12),
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_STUDY_01F_Vintage_Hardware_Macro_2K.jpg", "EP01_CLIP_V1_08_Hardware_15s.mp4", 15),
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_STUDY_01D_Mac_Boardroom_StudyA_2K.jpg", "EP01_CLIP_V1_09_Architecture_15s.mp4", 15),
    ("flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_03_Silicon_Wafer_Cyan_Laser_Hero.png", "EP01_CLIP_V1_12_WaferHero_16s.mp4", 16),
    ("flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_STUDY_02E_CRT_Computer_Boardroom_2K.jpg", "EP01_CLIP_V1_13_Garage_14s.mp4", 14),
    ("flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP01_FLOW_IMG_05_Businessman_Dissolving_Into_Data_2K.jpg", "EP01_CLIP_V1_15_FounderGrit_15s.mp4", 15),
    ("flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_06_Supercomputer_Servers_Cold_Hall_2K.jpg", "EP01_CLIP_V1_16_ServerCold_8s.mp4", 8),
    ("flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_04_Golden_Exponential_Curve_Hero.png", "EP01_CLIP_V1_19_CurveHero_17s.mp4", 17),
]

for rel_src, out_name, dur in tasks:
    src = os.path.join(base_dir, rel_src)
    dst = os.path.join(out_dir, out_name)
    if not os.path.exists(src):
        print(f"ERROR: missing {src}")
        continue
    # Render with slow zoom pan (1.00 -> 1.05) and 24fps
    total_frames = dur * 24
    vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.0002,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", src,
        "-vf", vf,
        "-c:v", "libx264", "-t", str(dur),
        "-pix_fmt", "yuv420p", "-r", "24", dst
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✓ Rendered {out_name} ({dur}s, 3840x2160 24fps)")

print("All V1 gapless clips successfully rendered!")
