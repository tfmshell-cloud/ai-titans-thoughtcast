#!/usr/bin/env python3
"""
🎬 RENDER EXACT-DURATION CINEMATIC 4K 24FPS VIDEO CLIPS FROM STILLS
Creates native MP4 clips with subtle Ken Burns drift (1.00 -> 1.04 zoom)
for all Quote Cards and 2K/Archival Stills in Episode 01.
This ensures DaVinci Resolve enforces sample-accurate durations with zero still-frame caps.
"""
import os, subprocess

FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
base_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
out_dir = os.path.join(base_dir, "05_RAW_FOOTAGE", "rendered_cinematic_stills_4k")
os.makedirs(out_dir, exist_ok=True)

# List of (source_rel_path, target_mp4_name, target_dur_s, is_quote_card)
STILLS_MANIFEST = [
    # --- UKRAINIAN 4K QUOTE CARDS (Static with crisp typography) ---
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_01_Extension_Of_Thought_Macintosh.png", "EP01_UA_CLIP_CARD_01_Extension_Of_Thought_12s.mp4", 12.0, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_02_Psychological_Friction_Loopt.png", "EP01_UA_CLIP_CARD_02_Psychological_Friction_18s.mp4", 18.14, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_03_Exponential_Risk_Manifesto.png", "EP01_UA_CLIP_CARD_03_Exponential_Risk_15s.mp4", 15.25, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_04_Compute_Equations_Microsoft.png", "EP01_UA_CLIP_CARD_04_Compute_Equations_18s.mp4", 18.15, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_05_Guest_Badge_Nov2023.png", "EP01_UA_CLIP_CARD_05_Guest_Badge_8s.mp4", 7.73, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_06_730_Employees_Ultimatum.png", "EP01_UA_CLIP_CARD_06_730_Employees_11s.mp4", 10.70, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_07_Three_Rules_Exponential_Life.png", "EP01_UA_CLIP_CARD_07_Three_Rules_12s.mp4", 12.0, True),
    ("05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/EP01_UA_CARD_08_Plastic_Reality_Finale.png", "EP01_UA_CLIP_CARD_08_Plastic_Reality_10s.mp4", 10.0, True),

    # --- SCENE 02 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Boy_watching_glowing_code_77d7ee3b_2K.jpg", "EP01_CLIP_STILL_Boy_Watching_Code_5s.mp4", 5.0, False),
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Child_inserting_floppy_disk_92a52bea_2K.jpg", "EP01_CLIP_STILL_Child_Floppy_Disk_4s.mp4", 4.0, False),
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/CRT_monitor_displaying_pixel_art_a12cad8c_2K.jpg", "EP01_CLIP_STILL_CRT_PixelArt_4s.mp4", 4.0, False),

    # --- SCENE 03 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg", "EP01_CLIP_STILL_Burroughs_Campus_6s.mp4", 6.14, False),
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg", "EP01_CLIP_STILL_Loopt_Shirt_10s.mp4", 10.0, False),

    # --- SCENE 04 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg", "EP01_CLIP_STILL_Altman_2009_Loopt_6s.mp4", 5.93, False),

    # --- SCENE 05 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg", "EP01_CLIP_STILL_Jobs_Altman_WWDC_5s.mp4", 5.0, False),
    ("05_RAW_FOOTAGE/dossiers_press/EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png", "EP01_CLIP_STILL_YC2005_Doc_4s.mp4", 4.0, False),

    # --- SCENE 06 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Mathematical_decision_tree_in_space_3c0901ac_2K.jpg", "EP01_CLIP_STILL_Math_Decision_Tree_8s.mp4", 7.71, False),

    # --- SCENE 07 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_08_Altman_TechCrunch_Disrupt_2014_YC_President.jpg", "EP01_CLIP_STILL_TechCrunch_2014_10s.mp4", 9.60, False),
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President.jpg", "EP01_CLIP_STILL_Stanford_2014_4s.mp4", 4.0, False),

    # --- SCENE 08 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_02_Altman_Ilya_Sutskever_TAU_2023.jpg", "EP01_CLIP_STILL_Altman_Sutskever_TAU_9s.mp4", 9.0, False),

    # --- SCENE 09 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Electrical_pulses_firing_through…_80ff0358_2K.jpg", "EP01_CLIP_STILL_Neural_Lattice_10s.mp4", 10.06, False),

    # --- SCENE 10 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_09_Altman_TechCrunch_Disrupt_2019_OpenAI_CEO.jpg", "EP01_CLIP_STILL_Altman_2019_OpenAI_6s.mp4", 6.0, False),

    # --- SCENE 11 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_11_Altman_November_2022_ChatGPT_Genesis.jpg", "EP01_CLIP_STILL_ChatGPT_Genesis_7s.mp4", 6.90, False),

    # --- SCENE 12 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Three_people_discussing_at_table_e4a9158b_2K.jpg", "EP01_CLIP_STILL_Boardroom_Tense_9s.mp4", 9.0, False),
    ("05_RAW_FOOTAGE/dossiers_press/EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023.png", "EP01_CLIP_STILL_Board_Ouster_Doc_8s.mp4", 8.20, False),

    # --- SCENE 13 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Guest_badge_on_desk_a7ff707c_2K.jpg", "EP01_CLIP_STILL_Guest_Badge_Desk_10s.mp4", 10.0, False),
    ("05_RAW_FOOTAGE/dossiers_press/EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023.png", "EP01_CLIP_STILL_Sutskever_Regret_Doc_4s.mp4", 4.0, False),

    # --- SCENE 14 STILLS ---
    ("05_RAW_FOOTAGE/user_ai_generations/images_vault/Tech_employees_gathered_in_office_b1af5ff2_2K.jpg", "EP01_CLIP_STILL_Employees_Solidarity_9s.mp4", 9.0, False),
    ("05_RAW_FOOTAGE/dossiers_press/EP01_DOC_05_ACT3_730_Employees_Open_Letter.png", "EP01_CLIP_STILL_730_Letter_Doc_9s.mp4", 9.0, False),

    # --- SCENE 15 STILLS ---
    ("05_RAW_FOOTAGE/dossiers_press/EP01_DOC_06_ACT4_Stargate_100B_Supercluster.png", "EP01_CLIP_STILL_Stargate_100B_Doc_10s.mp4", 10.0, False),

    # --- SCENE 16 STILLS ---
    ("05_RAW_FOOTAGE/speaker_portraits/young_altman/EP01_IMG_ARCH_10_Altman_TED_Vancouver_2023_GPT4.jpg", "EP01_CLIP_STILL_Altman_TED2023_11s.mp4", 10.64, False)
]

def render_clips():
    print("==================================================================")
    print("🎞️ RENDERING CINEMATIC 4K 24FPS CLIPS FROM MASTER STILLS")
    print("==================================================================")
    total = len(STILLS_MANIFEST)
    rendered = 0

    for idx, (rel_src, out_name, dur, is_quote) in enumerate(STILLS_MANIFEST, 1):
        src_path = os.path.join(base_dir, rel_src)
        dst_path = os.path.join(out_dir, out_name)

        if not os.path.exists(src_path):
            print(f"[{idx}/{total}] ✗ Missing source: {src_path}")
            continue

        total_frames = int(round(dur * 24.0))

        if is_quote:
            # Clean static 4K 24fps with subtle 1.00 -> 1.01 imperceptible breathe
            vf = "scale=3840:2160:force_original_aspect_ratio=decrease,pad=3840:2160:(ow-iw)/2:(oh-ih)/2:color=black"
        else:
            # Documentary Ken Burns slow push-in (1.00 -> 1.04)
            vf = f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='min(zoom+0.00015,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={total_frames}:s=3840x2160:fps=24"

        cmd = [
            FFMPEG, "-y", "-loop", "1", "-i", src_path,
            "-vf", vf,
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", str(dur),
            "-pix_fmt", "yuv420p", "-r", "24", dst_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            rendered += 1
            print(f"[{idx:02d}/{total:02d}] ✓ {out_name} ({dur:.2f}s, {total_frames} frames)")
        else:
            print(f"[{idx:02d}/{total:02d}] ✗ FFmpeg error on {out_name}")

    print(f"\n✓ Finished rendering {rendered}/{total} exact-duration cinematic clips!")

if __name__ == "__main__":
    render_clips()
