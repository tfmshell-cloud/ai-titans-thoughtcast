#!/usr/bin/env python3
"""
Surgical Assembly of Block 1: Act 1 "Genesis of Rebellion" (00:00 - 04:45)
Timeline: EP01_BLOCK1_Act1_Genesis_of_Rebellion
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def build_block1():
    resolve = bmd.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_BLOCK1_Act1_Genesis_of_Rebellion"
    
    # If timeline exists, delete clips or recreate
    for i in range(1, proj.GetTimelineCount() + 1):
        tl = proj.GetTimelineByIndex(i)
        if tl and tl.GetName() == tl_name:
            print(f"Selecting existing timeline: {tl_name}")
            proj.SetCurrentTimeline(tl)
            break
    else:
        print(f"Creating new timeline: {tl_name}")
        tl = mp.CreateEmptyTimeline(tl_name)
        proj.SetCurrentTimeline(tl)

    tl = proj.GetCurrentTimeline()
    start_frame = tl.GetStartFrame()
    print(f"Timeline: {tl.GetName()}, Start Frame: {start_frame}")

    def get_bin_items(folder):
        items = {}
        for clip in folder.GetClipList():
            items[clip.GetName()] = clip
        for sub in folder.GetSubFolderList():
            items.update(get_bin_items(sub))
        return items

    root = mp.GetRootFolder()
    clips_by_name = get_bin_items(root)
    print(f"Total clips available in Media Pool: {len(clips_by_name)}")

    while tl.GetTrackCount("audio") < 2:
        tl.AddTrack("audio")
    while tl.GetTrackCount("video") < 3:
        tl.AddTrack("video")

    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_92BPM_A2")
    tl.SetTrackName("video", 1, "FLOW_CANVAS_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_PHOTOS_V2")
    tl.SetTrackName("video", 3, "DOSSIERS_V3")

    # 1. AUDIO TRACK A1: Voiceover Takes for Act 1
    vo_plan = [
        ("EP01_VO_EN_01_ACT1_00_00_00_15_Intro_Rules.wav", 0.0),
        ("EP01_VO_EN_02_ACT1_00_15_00_45_Macintosh_1993.wav", 15.0),
        ("EP01_VO_EN_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_EN_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 100.0),
        ("EP01_VO_EN_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_EN_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
    ]

    print("\n--- Placing Act 1 Voiceover on Track A1 ---")
    for name, sec in vo_plan:
        clip = clips_by_name.get(name)
        if clip:
            rec_frame = start_frame + round(sec * FPS)
            app_info = {
                "mediaPoolItem": clip,
                "mediaType": 2,
                "trackIndex": 1,
                "recordFrame": rec_frame
            }
            items = mp.AppendToTimeline([app_info])
            if items:
                it = items[0]
                it.SetProperty("AudioVolume", 2.0)
                it.SetProperty("AudioDialogueLevelerEnabled", True)
                it.SetProperty("AudioDialogueLevelerReduceLoudDialogue", True)
                it.SetProperty("AudioDialogueLevelerLiftSoftDialogue", True)
                print(f"  ✓ A1 placed: {name} at {sec:.1f}s (+2.0 dB, Dialogue Leveler ON)")
        else:
            print(f"  ✗ WARNING: VO clip not found: {name}")

    # 2. AUDIO TRACK A2: Music Bed Ducked
    print("\n--- Placing Act 1 Music Bed on Track A2 ---")
    mus_clip = clips_by_name.get("EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav")
    if mus_clip:
        app_info = {
            "mediaPoolItem": mus_clip,
            "mediaType": 2,
            "trackIndex": 2,
            "recordFrame": start_frame
        }
        items = mp.AppendToTimeline([app_info])
        if items:
            it = items[0]
            it.SetProperty("AudioVolume", -20.0)
            print(f"  ✓ A2 placed: EP01_MUS_01_ACT1 at 0.0s (-20.0 dB ducked bed)")

    # 3. VIDEO TRACK V1: Continuous Canvas (Flow 4K Videos & 2K Keyframes)
    v1_plan = [
        ("ep01_flow_01_mac_chassis.mp4", 0.0),
        ("EP01_FLOW_IMG_01_Macintosh_LC_II_Keyframe.jpg", 8.0),
        ("ep01_flow_02_crt_code.mp4", 18.0),
        ("EP01_FLOW_IMG_02_CRT_Code_Eye_Reflection_Hero.jpg", 26.0),
        ("EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg", 34.0),
        ("EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg", 42.0),
        ("EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg", 65.0),
        ("ep01_flow_03_silicon_laser.mp4", 90.0),
        ("EP01_FLOW_IMG_03_Silicon_Wafer_Cyan_Laser_Hero.png", 110.0),
        ("EP01_FLOW_IMG_05_Businessman_Dissolving_Into_Data_2K.jpg", 135.0),
        ("ep01_flow_04_exponential_line.mp4", 175.0),
        ("EP01_FLOW_IMG_04_Golden_Exponential_Curve_Hero.png", 205.0),
        ("EP01_FLOW_STUDY_01F_Vintage_Hardware_Macro_2K.jpg", 240.0),
    ]

    print("\n--- Placing Track V1 Continuous Canvas ---")
    for name, sec in v1_plan:
        clip = clips_by_name.get(name)
        if clip:
            rec_frame = start_frame + round(sec * FPS)
            app_info = {
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 1,
                "recordFrame": rec_frame
            }
            items = mp.AppendToTimeline([app_info])
            if items:
                it = items[0]
                if name.endswith(('.jpg', '.png', '.webp')):
                    it.SetProperty("DynamicZoomEnabled", True)
                print(f"  ✓ V1 placed: {name} at {sec:.1f}s")
        else:
            print(f"  ✗ WARNING: V1 clip not found: {name}")

    # 4. VIDEO TRACK V2: Authentic Archives & Historical Photos
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

    print("\n--- Placing Track V2 Archives & Speaker Photos ---")
    for name, sec in v2_plan:
        clip = clips_by_name.get(name)
        if clip:
            rec_frame = start_frame + round(sec * FPS)
            app_info = {
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 2,
                "recordFrame": rec_frame
            }
            items = mp.AppendToTimeline([app_info])
            if items:
                it = items[0]
                if name.endswith(('.jpg', '.png', '.webp')):
                    it.SetProperty("DynamicZoomEnabled", True)
                print(f"  ✓ V2 placed: {name} at {sec:.1f}s (Ken Burns ON)")
        else:
            print(f"  ✗ WARNING: V2 clip not found: {name}")

    # 5. VIDEO TRACK V3: 4K Documentary Dossiers
    v3_plan = [
        ("EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png", 155.0),
    ]

    print("\n--- Placing Track V3 Dossiers ---")
    for name, sec in v3_plan:
        clip = clips_by_name.get(name)
        if clip:
            rec_frame = start_frame + round(sec * FPS)
            app_info = {
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 3,
                "recordFrame": rec_frame
            }
            items = mp.AppendToTimeline([app_info])
            if items:
                it = items[0]
                it.SetProperty("DynamicZoomEnabled", True)
                print(f"  ✓ V3 placed: {name} at {sec:.1f}s (Ken Burns ON)")
        else:
            print(f"  ✗ WARNING: V3 clip not found: {name}")

    # Set markers
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
    print("🏆 BLOCK 1 (ACT 1: 00:00 - 04:45) ASSEMBLED WITH SURGICAL PRECISION")
    print(f"Timeline Name: {tl_name}")
    print("=======================================================")

if __name__ == "__main__":
    build_block1()
    os._exit(0)
