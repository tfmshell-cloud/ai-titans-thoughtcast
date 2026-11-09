#!/usr/bin/env python3
"""
Render Dedicated 4K Master Assets for Episode 01, Block 3 (Act 3: The Boardroom Coup & 120 Hours Drama)
Renders Dossiers, Archival Motion Clips, Dynamic B-Roll, and 120s Music Stems.
"""
import os, sys, subprocess

FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
BASE = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"

v1_dir = os.path.join(BASE, "05_RAW_FOOTAGE", "flow_renders", "v1_block3_master")
v2_dir = os.path.join(BASE, "05_RAW_FOOTAGE", "archives", "v2_block3_master")
doc_dir = os.path.join(BASE, "05_RAW_FOOTAGE", "dossiers_press")
mus_dir = os.path.join(BASE, "03_AUDIO", "suno_stems", "EP01_ALTMAN_SMART_BINS")

os.makedirs(v1_dir, exist_ok=True)
os.makedirs(v2_dir, exist_ok=True)
os.makedirs(mus_dir, exist_ok=True)

def render_zoom(src_path, dst_path, dur, zoom_start=1.0, zoom_end=1.05):
    if os.path.exists(dst_path) and os.path.getsize(dst_path) > 100000:
        print(f"  ✓ Already exists: {os.path.basename(dst_path)}")
        return
    total_frames = int(dur * 24)
    vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.0002,{zoom_end})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", src_path,
        "-vf", vf,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "19",
        "-t", str(dur),
        "-pix_fmt", "yuv420p", "-r", "24", dst_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"  ✓ Rendered {os.path.basename(dst_path)} ({dur}s, 3840x2160 24fps)")

# 1. Dossiers Press Announcements
doc_tasks = [
    (os.path.join(BASE, "05_RAW_FOOTAGE", "dossiers_press", "EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023.png"), os.path.join(doc_dir, "EP01_DOC_03_Board_Ouster_10s.mp4"), 10),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "dossiers_press", "EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023.png"), os.path.join(doc_dir, "EP01_DOC_04_Sutskever_Regret_10s.mp4"), 10),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "dossiers_press", "EP01_DOC_05_ACT3_730_Employees_Open_Letter.png"), os.path.join(doc_dir, "EP01_DOC_05_Employees_Letter_12s.mp4"), 12),
]

print("=== 1. Rendering Block 3 Press Dossier Motion Clips ===")
for src, dst, dur in doc_tasks:
    render_zoom(src, dst, dur, zoom_end=1.03)

# 2. Archival Photos for Track V2
arch_tasks = [
    (os.path.join(BASE, "05_RAW_FOOTAGE", "speaker_portraits", "young_altman", "EP01_IMG_ARCH_11_Altman_November_2022_ChatGPT_Genesis.jpg"), os.path.join(v2_dir, "EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4"), 10),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "speaker_portraits", "young_altman", "EP01_IMG_ARCH_10_Altman_TED_Vancouver_2023_GPT4.jpg"), os.path.join(v2_dir, "EP01_V2_B3_02_Altman_TED_2023_10s.mp4"), 10),
]

print("\n=== 2. Rendering Block 3 Archival Photo Motion Clips ===")
for src, dst, dur in arch_tasks:
    render_zoom(src, dst, dur, zoom_end=1.05)

# 3. Dedicated B-Roll Clips for Track V1
broll_tasks = [
    (os.path.join(BASE, "05_RAW_FOOTAGE", "flow_images", "EP03_Hassabis", "01_primary_keyframes", "EP03_FLOW_IMG_01_Wooden_King_Falling_Chessboard_2K.jpg"), os.path.join(v1_dir, "EP01_V1_B3_01_Chess_King_Falling_12s.mp4"), 12),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "flow_images", "EP01_Altman", "02_broll_stills_and_studies", "EP01_FLOW_STUDY_07C_Computer_Boardroom_Void_2K.jpg"), os.path.join(v1_dir, "EP01_V1_B3_02_Boardroom_Void_14s.mp4"), 14),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "flow_images", "BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE", "EP09_FLOW_IMG_03_Two_Silhouettes_Connecting_Symbols_2K.jpg"), os.path.join(v1_dir, "EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4"), 12),
    (os.path.join(BASE, "05_RAW_FOOTAGE", "flow_images", "BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE", "EP09_FLOW_IMG_02_Golden_Grid_Stabilizing_Stormy_Ocean_2K.jpg"), os.path.join(v1_dir, "EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4"), 15),
]

print("\n=== 3. Rendering Block 3 Track V1 B-Roll Clips ===")
for src, dst, dur in broll_tasks:
    render_zoom(src, dst, dur, zoom_end=1.05)

# 4. Music Score Stems (120s each, 48kHz WAV)
print("\n=== 4. Rendering Block 3 Music Score Stems ===")
src_mus1 = os.path.join(BASE, "03_AUDIO", "suno_stems", "EP01_ALTMAN_SMART_BINS", "EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav")
dst_mus1 = os.path.join(mus_dir, "EP01_MUS_B3_PART1_08_00_to_10_00_120s.wav")
af1 = 'afade=t=in:ss=0:d=1,afade=t=out:st=117:d=3'
cmd1 = [FFMPEG, '-y', '-i', src_mus1, '-t', '120', '-af', af1, '-ar', '48000', dst_mus1]
subprocess.run(cmd1, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"  ✓ Rendered {os.path.basename(dst_mus1)} (120s)")

src_mus2 = os.path.join(BASE, "03_AUDIO", "suno_stems", "EP06_SUTSKEVER_SMART_BINS", "EP06_MUS_09_ACT3_92BPM_November_Split.wav")
dst_mus2 = os.path.join(mus_dir, "EP01_MUS_B3_PART2_10_00_to_12_00_120s.wav")
af2 = 'afade=t=in:ss=0:d=3,afade=t=out:st=117:d=3'
cmd2 = [FFMPEG, '-y', '-i', src_mus2, '-t', '120', '-af', af2, '-ar', '48000', dst_mus2]
subprocess.run(cmd2, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"  ✓ Rendered {os.path.basename(dst_mus2)} (120s)")

print("\n🎉 ALL BLOCK 3 MASTER ASSETS RENDERED SUCCESSFULLY!")
