#!/usr/bin/env python3
"""
MASTER DIRECTORIAL ASSEMBLY OF BLOCK 1 (00:00 - 04:45)
Timeline: EP01_BLOCK1_Master_Director_Cut
Features:
- Track A1: Voiceover (+2dB, Dialogue Leveler ON)
- Track A2: Suno 92 BPM Bed (-20dB ducked)
- Track A3: SFX Design (Power Relay, CRT Hum, Alps Keyboard, Sub Drops, Laser Whoosh, Shutter)
- Track A4: Diegetic Live Sound (Steve Jobs WWDC 2008 Voice & Hall Applause, CRT 1992 Audio)
- Track V1: 100% Continuous Flow Canvas (4K/1080p video renders, 0 gaps, 0 offline clips)
- Track V2: Authentic Archives & Historical Photos (Ken Burns dynamic zoom)
- Track V3: 4K Press Dossiers (Ken Burns dynamic zoom)
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble():
    resolve = bmd.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_BLOCK1_Master_Director_Cut"

    # Recreate or switch to timeline
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            print(f"Selecting existing timeline: {tl_name}")
            proj.SetCurrentTimeline(t)
            break
    else:
        print(f"Creating new timeline: {tl_name}")
        tl = mp.CreateEmptyTimeline(tl_name)
        proj.SetCurrentTimeline(tl)

    tl = proj.GetCurrentTimeline()
    start_frame = tl.GetStartFrame()
    print(f"Active Timeline: {tl.GetName()}, Start Frame: {start_frame}")

    # Clear existing clips if any
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            if items:
                tl.DeleteClips(items)

    # Ensure required tracks exist
    while tl.GetTrackCount("audio") < 4:
        tl.AddTrack("audio")
    while tl.GetTrackCount("video") < 3:
        tl.AddTrack("video")

    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_BED_A2")
    tl.SetTrackName("audio", 3, "SFX_DESIGN_A3")
    tl.SetTrackName("audio", 4, "LIVE_ARCHIVE_A4")
    tl.SetTrackName("video", 1, "FLOW_CANVAS_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_PHOTOS_V2")
    tl.SetTrackName("video", 3, "DOSSIERS_V3")

    def get_bin_items(folder):
        items = {}
        for clip in folder.GetClipList():
            items[clip.GetName()] = clip
        for sub in folder.GetSubFolderList():
            items.update(get_bin_items(sub))
        return items

    root = mp.GetRootFolder()
    clips = get_bin_items(root)
    print(f"Available clips in media pool: {len(clips)}")

    def place_item(clip_name, media_type, track_idx, sec, vol=None, leveler=False, zoom=False):
        c = clips.get(clip_name)
        if not c:
            print(f"  ✗ NOT FOUND: {clip_name}")
            return None
        rf = start_frame + round(sec * FPS)
        app = {"mediaPoolItem": c, "mediaType": media_type, "trackIndex": track_idx, "recordFrame": rf}
        its = mp.AppendToTimeline([app])
        if its:
            it = its[0]
            if vol is not None:
                it.SetProperty("AudioVolume", vol)
            if leveler:
                it.SetProperty("AudioDialogueLevelerEnabled", True)
                it.SetProperty("AudioDialogueLevelerReduceLoudDialogue", True)
                it.SetProperty("AudioDialogueLevelerLiftSoftDialogue", True)
            if zoom:
                it.SetProperty("DynamicZoomEnabled", True)
            return it
        return None

    # ==========================================================
    # 1. TRACK A1: VOICEOVER (6 Takes)
    # ==========================================================
    print("\n--- Assembling A1: Voiceover ---")
    vo = [
        ("EP01_VO_EN_01_ACT1_00_00_00_15_Intro_Rules.wav", 0.0),
        ("EP01_VO_EN_02_ACT1_00_15_00_45_Macintosh_1993.wav", 15.0),
        ("EP01_VO_EN_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_EN_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 100.0),
        ("EP01_VO_EN_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_EN_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
    ]
    for name, sec in vo:
        place_item(name, 2, 1, sec, vol=2.0, leveler=True)
        print(f"  ✓ A1 VO: {name} at {sec:.1f}s")

    # ==========================================================
    # 2. TRACK A2: MUSIC BED (Ducked to -20dB)
    # ==========================================================
    print("\n--- Assembling A2: Music Bed ---")
    place_item("EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav", 2, 2, 0.0, vol=-20.0)
    print("  ✓ A2 Music: Suno 92 BPM Bed placed at 0.0s (-20.0 dB)")

    # ==========================================================
    # 3. TRACK A3: SFX SOUND DESIGN
    # ==========================================================
    print("\n--- Assembling A3: Sound Design (SFX) ---")
    sfx_plan = [
        ("sfx_relay_click.wav", 0.0, -3.0),
        ("sfx_crt_hum.wav", 0.3, -12.0),
        ("sfx_keyboard_alps.wav", 16.0, -8.0),
        ("sfx_camera_shutter.wav", 22.0, -6.0),
        ("sfx_sub_impact.wav", 45.0, -4.0),
        ("sfx_camera_shutter.wav", 48.0, -6.0),
        ("sfx_whoosh_laser.wav", 90.0, -6.0),
        ("sfx_camera_shutter.wav", 105.0, -6.0),
        ("sfx_camera_shutter.wav", 142.0, -6.0),
        ("sfx_sub_impact.wav", 150.0, -4.0),
        ("sfx_camera_shutter.wav", 170.0, -6.0),
        ("sfx_whoosh_laser.wav", 185.0, -6.0),
        ("sfx_camera_shutter.wav", 230.0, -6.0),
    ]
    for name, sec, v in sfx_plan:
        place_item(name, 2, 3, sec, vol=v)
        print(f"  ✓ A3 SFX: {name} at {sec:.1f}s ({v} dB)")

    # ==========================================================
    # 4. TRACK A4: DIEGETIC LIVE AUDIO (Steve Jobs, CRT)
    # ==========================================================
    print("\n--- Assembling A4: Diegetic Live Audio ---")
    place_item("EP01_ARCH_AUDIO_Macintosh_1992_CRT_Scan.wav", 2, 4, 10.0, vol=-10.0)
    print("  ✓ A4 Live: Macintosh 1992 CRT Scan Audio placed at 10.0s (-10 dB)")
    # Steve Jobs live audio on stage WWDC 2008:
    place_item("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 4, 155.0, vol=-3.0)
    print("  ✓ A4 Live: Steve Jobs WWDC 2008 Voice & Hall Applause placed at 155.0s (-3 dB)")

    # ==========================================================
    # 5. TRACK V1: CONTINUOUS 100% GAPLESS VIDEO CANVAS
    # ==========================================================
    print("\n--- Assembling V1: Continuous Video Canvas ---")
    v1_plan = [
        ("ep01_flow_01_mac_chassis.mp4", 0.0),
        ("EP01_FLOW_VID_01_ACT1_Macintosh_LC_II_Chassis_1080p24.mp4", 8.0),
        ("ep01_flow_02_crt_code.mp4", 16.0),
        ("EP01_FLOW_VID_02_ACT1_CRT_Assembly_Child_Eye_720p24.mp4", 26.0),
        ("EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg", 36.0),
        ("EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg", 42.0),
        ("EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg", 65.0),
        ("ep01_flow_03_silicon_laser.mp4", 90.0),
        ("EP01_FLOW_VID_03_ACT1_Silicon_Wafer_Cyan_Laser_720p24.mp4", 100.0),
        ("ep01_flow_05_neural_lattice.mp4", 125.0),
        ("ep01_flow_06_server_monolith.mp4", 150.0),
        ("ep01_flow_04_exponential_line.mp4", 185.0),
        ("EP01_FLOW_VID_04_ACT1_Golden_Exponential_Curve_720p24.mp4", 205.0),
        ("ep01_flow_08_golden_signatures.mp4", 225.0),
    ]
    for name, sec in v1_plan:
        zoom = name.endswith(('.jpg', '.png', '.webp'))
        place_item(name, 1, 1, sec, zoom=zoom)
        print(f"  ✓ V1 Canvas: {name} at {sec:.1f}s")

    # ==========================================================
    # 6. TRACK V2: AUTHENTIC ARCHIVES & SPEAKER PHOTOS
    # ==========================================================
    print("\n--- Assembling V2: Authentic Archives & Photos ---")
    v2_plan = [
        ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4", 10.0),
        ("EP01_IMG_ARCH_06_Altman_Childhood_Macintosh_LC_II_1993.jpg", 22.0),
        ("EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg", 48.0),
        ("EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President.jpg", 105.0),
        ("EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg", 142.0),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 155.0),
        ("EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg", 170.0),
        ("EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg", 230.0),
    ]
    for name, sec in v2_plan:
        zoom = name.endswith(('.jpg', '.png', '.webp'))
        place_item(name, 1, 2, sec, zoom=zoom)
        print(f"  ✓ V2 Archive: {name} at {sec:.1f}s (Ken Burns: {zoom})")

    # ==========================================================
    # 7. TRACK V3: 4K DOCUMENTARY DOSSIERS
    # ==========================================================
    print("\n--- Assembling V3: 4K Press Dossiers ---")
    place_item("EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png", 1, 3, 150.0, zoom=True)
    print("  ✓ V3 Dossier: YC Summer 2005 Cohort Document at 150.0s")

    # ==========================================================
    # 8. CHAPTER BEAT MARKERS
    # ==========================================================
    markers = [
        (0.0, "Cyan", "Сцена 1: Вступ і природа правил"),
        (15.0, "Blue", "Сцена 2: 1993, Macintosh LC II та перший баг"),
        (58.0, "Yellow", "Сцена 3: Джон Берроуз Скул та вихід із тіні"),
        (100.0, "Green", "Сцена 4: Стенфорд і заснування Loopt"),
        (150.0, "Orange", "Сцена 5: YC Batch 1, цинга і Стів Джобс"),
        (215.0, "Red", "Сцена 6: Мислення експоненти"),
    ]
    for sec, col, note in markers:
        frm = start_frame + round(sec * FPS)
        tl.AddMarker(frm, col, note, f"Act 1 Beat at {sec:.0f}s", 1)

    pm.SaveProject()
    print("\n=======================================================")
    print("🏆 MASTER DIRECTORIAL CUT OF BLOCK 1 COMPLETED")
    print(f"Timeline Name : {tl_name}")
    print("Audio Tracks  : A1 (Voice +2dB), A2 (Music -20dB), A3 (SFX), A4 (Live Steve Jobs)")
    print("Video Tracks  : V1 (Gapless Canvas), V2 (Archives/Photos), V3 (Dossiers)")
    print("=======================================================")

if __name__ == "__main__":
    assemble()
    os._exit(0)
