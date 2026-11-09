#!/usr/bin/env python3
"""
Clean, Authentic Editorial Fix for Block 1
Removes all synthetic beep/sine SFX.
Removes irrelevant sci-fi renders (neural lattices in space).
Focuses 100% on authentic biographical narrative:
- Voiceover (Adam)
- Music bed (Suno 92 BPM)
- Real historical archives & photos
- Authentic vintage tech footage (Macintosh LC II, CRT)
- Real Steve Jobs audio at WWDC 2008
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def fix_block():
    resolve = bmd.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_BLOCK1_Master_Director_Cut"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            proj.SetCurrentTimeline(tl)
            break
            
    if not tl:
        print("Timeline not found!")
        return

    # Delete all items to rebuild with pure editorial taste
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            if items:
                tl.DeleteClips(items)

    start_frame = tl.GetStartFrame()

    def get_bin_items(folder):
        items = {}
        for clip in folder.GetClipList():
            items[clip.GetName()] = clip
        for sub in folder.GetSubFolderList():
            items.update(get_bin_items(sub))
        return items

    clips = get_bin_items(mp.GetRootFolder())

    def place(clip_name, media_type, track_idx, sec, vol=None, leveler=False, zoom=False):
        c = clips.get(clip_name)
        if not c:
            print(f"  Missing: {clip_name}")
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

    # 1. Clean Audio: Voiceover on A1
    vo = [
        ("EP01_VO_EN_01_ACT1_00_00_00_15_Intro_Rules.wav", 0.0),
        ("EP01_VO_EN_02_ACT1_00_15_00_45_Macintosh_1993.wav", 15.0),
        ("EP01_VO_EN_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_EN_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 100.0),
        ("EP01_VO_EN_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_EN_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
    ]
    for name, sec in vo:
        place(name, 2, 1, sec, vol=2.0, leveler=True)

    # 2. Clean Audio: Suno Music on A2 (-20dB)
    place("EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav", 2, 2, 0.0, vol=-20.0)

    # 3. Clean Audio: Only Authentic Live Archive Audio on A3 (NO FAKE SINE BEEPS!)
    # Steve Jobs live audio on stage
    place("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 3, 155.0, vol=-4.0)

    # 4. Video Track V1: Biographical & Period-Accurate Tech Visuals ONLY
    # NO space sci-fi neural networks!
    v1_clean = [
        ("ep01_flow_01_mac_chassis.mp4", 0.0),
        ("EP01_FLOW_VID_01_ACT1_Macintosh_LC_II_Chassis_1080p24.mp4", 8.0),
        ("ep01_flow_02_crt_code.mp4", 16.0),
        ("EP01_FLOW_VID_02_ACT1_CRT_Assembly_Child_Eye_720p24.mp4", 26.0),
        ("EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg", 36.0),
        ("EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg", 42.0),
        ("EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg", 65.0),
        ("ep01_flow_03_silicon_laser.mp4", 90.0),
        ("EP01_FLOW_VID_03_ACT1_Silicon_Wafer_Cyan_Laser_720p24.mp4", 100.0),
        ("EP01_FLOW_STUDY_01D_Mac_Boardroom_StudyA_2K.jpg", 125.0),
        ("ep01_flow_06_server_monolith.mp4", 150.0),
        ("ep01_flow_04_exponential_line.mp4", 185.0),
        ("EP01_FLOW_VID_04_ACT1_Golden_Exponential_Curve_720p24.mp4", 205.0),
    ]
    for name, sec in v1_clean:
        zoom = name.endswith(('.jpg', '.png', '.webp'))
        place(name, 1, 1, sec, zoom=zoom)

    # 5. Video Track V2: Real Historical Archives & Authentic Photos
    v2_clean = [
        ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4", 10.0),
        ("EP01_IMG_ARCH_06_Altman_Childhood_Macintosh_LC_II_1993.jpg", 22.0),
        ("EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg", 48.0),
        ("EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President.jpg", 105.0),
        ("EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg", 142.0),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 155.0),
        ("EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg", 170.0),
        ("EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg", 230.0),
    ]
    for name, sec in v2_clean:
        zoom = name.endswith(('.jpg', '.png', '.webp'))
        place(name, 1, 2, sec, zoom=zoom)

    # 6. Video Track V3: Real 4K Press Document
    place("EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png", 1, 3, 150.0, zoom=True)

    pm.SaveProject()
    print("✓ Successfully cleaned Block 1. Removed fake sine sounds and sci-fi misplacements.")

if __name__ == "__main__":
    fix_block()
    os._exit(0)
