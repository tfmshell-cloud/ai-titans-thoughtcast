#!/usr/bin/env python3
import subprocess, os

FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
base_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/speaker_portraits/young_altman"
out_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/archives/v2_master_clips"
os.makedirs(out_dir, exist_ok=True)

photos = [
    ("EP01_IMG_ARCH_06_Altman_Childhood_Macintosh_LC_II_1993.jpg", "EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 10),
    ("EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg", "EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 12),
    ("EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President.jpg", "EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 12),
    ("EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg", "EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 12),
    ("EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg", "EP01_V2_ARCH_03_Jobs_Stage_10s.mp4", 10),
    ("EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg", "EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 15),
]

for src_name, dst_name, dur in photos:
    src = os.path.join(base_dir, src_name)
    dst = os.path.join(out_dir, dst_name)
    if not os.path.exists(src):
        print(f"Missing {src}")
        continue
    total_frames = dur * 24
    vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.0002,1.05)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", src,
        "-vf", vf,
        "-c:v", "libx264", "-t", str(dur),
        "-pix_fmt", "yuv420p", "-r", "24", dst
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"✓ Rendered archive {dst_name} ({dur}s)")

print("All V2 archive clips rendered!")
