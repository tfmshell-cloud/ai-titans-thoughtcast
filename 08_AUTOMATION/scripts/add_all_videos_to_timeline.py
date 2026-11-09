#!/usr/bin/env python3
"""
AI TITANS: EPISODE 01 — SAM ALTMAN
OPEN MASTER VIDEO FOLDER & ADD ALL VIDEO FILES TO TIMELINE
1. Creates / sets active Media Pool folder: '00_ALL_EP01_VIDEO_VAULT' with all unique video files.
2. Adds all unique video files to Track V1 on timeline 'EP01_MASTER_DIRECTORS_CUT_COMPLETE'.
3. Opens the raw footage folder in macOS Finder.
"""

import sys, os, subprocess
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def tc_to_frames(tc):
    parts = [int(p) for p in tc.split(':')]
    return parts[0]*3600*24 + parts[1]*60*24 + parts[2]*24 + parts[3]

def run():
    resolve = bmd.scriptapp('Resolve')
    if not resolve:
        print("✗ ERROR: Cannot connect to DaVinci Resolve!")
        sys.exit(1)

    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    if not proj or proj.GetName() != "AI_Titans_EP01_Sam_Altman":
        proj = pm.LoadProject("AI_Titans_EP01_Sam_Altman")

    mp = proj.GetMediaPool()
    root = mp.GetRootFolder()

    tl_name = "EP01_MASTER_DIRECTORS_CUT_COMPLETE"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print(f"✗ ERROR: Timeline {tl_name} not found!")
        sys.exit(1)

    print("==================================================================")
    print("🎬 OPENING VIDEO FOLDER IN MEDIA POOL & ADDING ALL VIDEOS TO TIMELINE")
    print("==================================================================")

    # 1. Locate 02_EP01_ALTMAN_MEDIA
    p_altman = None
    for sf in root.GetSubFolderList():
        if sf.GetName() == "02_EP01_ALTMAN_MEDIA":
            p_altman = sf
            break

    if not p_altman:
        p_altman = root

    # Create or get master video vault bin
    video_bin_name = "00_ALL_EP01_VIDEO_VAULT"
    video_bin = None
    for sf in p_altman.GetSubFolderList():
        if sf.GetName() == video_bin_name:
            video_bin = sf
            break

    if not video_bin:
        video_bin = mp.AddSubFolder(p_altman, video_bin_name)

    # Collect all unique video clips across the project
    unique_videos = {}
    def scan_for_videos(folder):
        for c in folder.GetClipList() or []:
            c_type = c.GetClipProperty("Type")
            c_name = c.GetName()
            if c_type in ("Video", "Video + Audio") and c_name.endswith((".mp4", ".mov")):
                if c_name not in unique_videos:
                    unique_videos[c_name] = c
        for sf in folder.GetSubFolderList() or []:
            scan_for_videos(sf)

    scan_for_videos(p_altman)
    print(f"  ✓ Found {len(unique_videos)} unique EP01 video clips in Media Pool.")

    # Move clips into video_bin so it holds all videos
    clips_to_move = [c for c in unique_videos.values()]
    mp.MoveClips(clips_to_move, video_bin)
    print(f"  ✓ Placed all {len(clips_to_move)} video clips into folder '{video_bin_name}'.")

    # Set active folder in Media Pool to this video vault
    mp.SetCurrentFolder(video_bin)
    print(f"  ✓ Active Media Pool folder set to: '{video_bin_name}'")

    # 2. Clear previous video clips on Track V1/V2
    for vi in range(1, tl.GetTrackCount("video") + 1):
        v_items = tl.GetItemListInTrack("video", vi) or []
        if v_items:
            tl.DeleteClips(v_items)
            print(f"  ✓ Cleared {len(v_items)} existing clips from video track {vi}")

    tl.SetTrackName("video", 1, "ALL_VIDEO_FILES_V1")

    # 3. Sort video clips in narrative story order
    # Priority order:
    # Act 1: Childhood & Macintosh -> Burroughs School -> Stanford -> Loopt & WWDC -> Compound Interest
    # Act 2: YC President -> Longevity & Rosewood -> OpenAI founding -> Capped profit
    # Act 3: ChatGPT launch -> Senate hearing -> Friday Coup -> 120 Hours drama -> 730 Signatures
    # Act 4: Stargate & Fusion -> Three rules -> Plastic reality & Closers
    def sort_key(name):
        n = name.lower()
        if "authentic_histo" in n or "screwdriver" in n or "computer_m_clip" in n or "mac_chassis" in n or "childhood_mac" in n or "crt_code" in n or "phosphor" in n:
            return (1, name)
        if "burroughs" in n or "school" in n or "portrait" in n:
            return (2, name)
        if "dynamic_camera" in n or "stanford" in n or "dorm" in n or "silicon_laser" in n or "silicon_wafer" in n:
            return (3, name)
        if "digital_hud" in n or "loopt" in n or "wwdc" in n or "jobs" in n or "grit" in n or "garage" in n:
            return (4, name)
        if "light_point_explodes_into_streaks_0827" in n or "exponential" in n:
            return (5, name)
        if "spark_disruption" in n or "cs183b" in n or "disrupt_2014" in n or "startup_engine" in n:
            return (6, name)
        if "zygote" in n or "prenatal" in n or "rosewood" in n or "sutskever_tau" in n or "singularity" in n:
            return (7, name)
        if "neuron_morphs" in n or "neural_lattice" in n or "robotic" in n or "swarm" in n:
            return (8, name)
        if "server_monolith" in n or "server_matrix" in n or "disrupt_2019" in n or "metropolis" in n:
            return (9, name)
        if "mouse_click" in n or "plunges_into_terminal" in n or "chatgpt_launch" in n or "senate" in n:
            return (10, name)
        if "four_men" in n or "orbiting_desk" in n or "boardroom_noir" in n or "chess_king" in n:
            return (11, name)
        if "nadella" in n or "strobe" in n or "window_rain" in n or "ted_2023" in n:
            return (12, name)
        if "accelerating_through_lett" in n or "golden_signatures" in n or "seamless_stylis_12_34" in n or "stabilizing" in n or "letter" in n:
            return (13, name)
        if "physical_matter" in n or "fusion_torus" in n or "tesla_coil" in n or "arctic_parka" in n or "blackwell" in n:
            return (14, name)
        if "slow,_powerful" in n or "seamless_stylis_11_32" in n or "streaks_c712" in n or "obsessive" in n or "gold_melting" in n or "laser_forms" in n:
            return (15, name)
        if "horizon" in n or "boy_aging" in n or "closer" in n or "finale" in n:
            return (16, name)
        if "card" in n or "doc" in n:
            return (17, name)
        return (20, name)

    sorted_video_names = sorted(list(unique_videos.keys()), key=sort_key)
    print(f"\n--- 2. Appending {len(sorted_video_names)} Video Clips to Track V1 ---")

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)
    curr_frame = start_frame

    placed_count = 0
    for name in sorted_video_names:
        c = unique_videos[name]
        dur_tc = c.GetClipProperty("Duration")
        if not dur_tc:
            dur_f = 240 # default 10s
        else:
            dur_f = tc_to_frames(dur_tc)

        app = {
            "mediaPoolItem": c,
            "mediaType": 1, # Video
            "trackIndex": 1,
            "recordFrame": curr_frame
        }
        res = mp.AppendToTimeline([app])
        if res:
            sec_start = (curr_frame - start_frame) / FPS
            m_s, sec_s = divmod(sec_start, 60)
            placed_count += 1
            if placed_count <= 10 or placed_count >= len(sorted_video_names) - 5:
                print(f"  🎥 [{m_s:02.0f}:{sec_s:04.1f}] V1: {name} ({dur_f/FPS:.1f}s)")
            elif placed_count == 11:
                print(f"  ... [placing clips {placed_count} through {len(sorted_video_names)-5}] ...")
            curr_frame += dur_f

    total_video_dur = curr_frame - start_frame
    tm, ts = divmod(total_video_dur / FPS, 60)
    print(f"\n✓ Placed {placed_count} video clips on Track V1.")
    print(f"✓ Total Video Duration: {total_video_dur} frames ({tm:02.0f}:{ts:04.1f})")

    # 4. Open macOS Finder folder
    user_ai_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/user_ai_generations"
    try:
        subprocess.run(["open", user_ai_dir], check=False)
        print(f"  ✓ Opened folder in macOS Finder: {user_ai_dir}")
    except Exception as e:
        print(f"  ⚠️ Could not open Finder: {e}")

    pm.SaveProject()
    print("✓ Project Saved Successfully.")

if __name__ == '__main__':
    run()
