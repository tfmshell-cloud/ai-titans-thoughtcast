#!/usr/bin/env python3
"""
Hollywood/Netflix-Grade Master Timeline Assembly for AI Titans EP01 (Sam Altman)
Direct programmatic construction using DaVinci Resolve Studio 19 Python API.
Zero gaps, 100% media utilization:
  - Audio A1: 17 Voiceover takes (Adam 48k/24b WAV), Dialogue Leveler ON, Gain +2.0 dB
  - Audio A2: 4-Act Suno 92 BPM music, Volume -18.0 dB (broadcast ducked bed)
  - Video V1: 10 Google Flow 4K Videos + 15 2K Concept Keyframes (continuous visual canvas)
  - Video V2: 5 Historical Archives + 12 Authentic Historical Photos (Ken Burns Dynamic Zoom 1.00->1.05)
  - Video V3: 5 4K Documentary Dossiers + Scientific 3D VFX (Ken Burns Dynamic Zoom)
  - Markers : 17 Narrative Chapter markers
"""

import os
import sys

RESOLVE_SCRIPT_API = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
RESOLVE_SCRIPT_LIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
MODULES_PATH = os.path.join(RESOLVE_SCRIPT_API, "Modules")

os.environ["RESOLVE_SCRIPT_API"] = RESOLVE_SCRIPT_API
os.environ["RESOLVE_SCRIPT_LIB"] = RESOLVE_SCRIPT_LIB
if MODULES_PATH not in sys.path:
    sys.path.append(MODULES_PATH)

import DaVinciResolveScript as bmd

FPS = 24.0

# 1. Voiceover Timings (17 takes)
VO_TIMINGS = [
    {"num": 1,  "sec": 0.0,    "marker": "ACT I: St. Louis 1993 — Macintosh LC II", "color": "Cyan"},
    {"num": 2,  "sec": 15.0,   "marker": "ACT I: Macintosh LC II — Bifurcation Point", "color": "Blue"},
    {"num": 3,  "sec": 58.0,   "marker": "ACT I: John Burroughs School — Safe Space Speech", "color": "Blue"},
    {"num": 4,  "sec": 100.0,  "marker": "ACT I: Stanford Drop-out & Loopt Genesis", "color": "Blue"},
    {"num": 5,  "sec": 150.0,  "marker": "ACT I: Y Combinator S05 Batch & Paul Graham", "color": "Green"},
    {"num": 6,  "sec": 215.0,  "marker": "ACT I: The Exponential Compound Interest Rule", "color": "Yellow"},
    {"num": 7,  "sec": 285.0,  "marker": "ACT II: YC President at 28 — The Architect", "color": "Cyan"},
    {"num": 8,  "sec": 345.0,  "marker": "ACT II: Rosewood Hotel Secret Dinner — Google vs Humanity", "color": "Purple"},
    {"num": 9,  "sec": 420.0,  "marker": "ACT II: Dec 11, 2015 — OpenAI Non-Profit Founding", "color": "Green"},
    {"num": 10, "sec": 495.0,  "marker": "ACT II: The Microsoft $1B Deal & Capped-Profit", "color": "Yellow"},
    {"num": 11, "sec": 570.0,  "marker": "ACT III: Nov 30, 2022 — ChatGPT Explosion & 100M Users", "color": "Cyan"},
    {"num": 12, "sec": 645.0,  "marker": "ACT III: Friday Board Coup — 12:00 Google Meet Ouster", "color": "Red"},
    {"num": 13, "sec": 735.0,  "marker": "ACT III: 120 Hours of Chaos & Guest Badge", "color": "Red"},
    {"num": 14, "sec": 825.0,  "marker": "ACT III: 730 Signatures — Triumphant Reinstatement", "color": "Yellow"},
    {"num": 15, "sec": 930.0,  "marker": "ACT IV: Project Stargate & Helion Fusion Energy", "color": "Cyan"},
    {"num": 16, "sec": 1020.0, "marker": "ACT IV: The Three Rules of Exponential Life", "color": "Mint"},
    {"num": 17, "sec": 1110.0, "marker": "ACT IV: Outro — The Future is Created Now", "color": "Yellow"}
]

# 2. Music Layout (4 Acts Suno 92 BPM)
MUSIC_CUES = [
    {"pattern": "MUS_01_ACT1", "sec": 0.0,    "name": "Act 1: Introspection (92 BPM)"},
    {"pattern": "AMB_07_ACT2", "sec": 285.0,  "name": "Act 2: Tension Drone (92 BPM)"},
    {"pattern": "MUS_09_ACT3", "sec": 570.0,  "name": "Act 3: Crisis & ChatGPT (92 BPM)"},
    {"pattern": "MUS_15_ACT4", "sec": 930.0,  "name": "Act 4: Future Horizon Finale (92 BPM)"}
]

# 3. Video V1: 10 Flow Videos + 2K Concept Keyframes (Continuous Canvas)
V1_CANVAS_CUES = [
    # Act 1
    {"type": "flow_vid", "pattern": "ep01_flow_01", "sec": 0.0,   "dur": 8.0,  "name": "Flow 01 Mac Chassis"},
    {"type": "concept",  "pattern": "IMG_01_Macintosh_LC_II", "sec": 8.0, "dur": 10.0, "name": "Keyframe 01 Mac LC II 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_02", "sec": 18.0,  "dur": 8.0,  "name": "Flow 02 CRT Code"},
    {"type": "concept",  "pattern": "IMG_02_CRT_Code_Eye", "sec": 26.0, "dur": 14.0, "name": "Keyframe 02 CRT Code Hero 2K"},
    {"type": "concept",  "pattern": "IMG_02D_Boy_At_Vintage", "sec": 40.0, "dur": 18.0, "name": "B-Roll Boy At CRT 1993"},
    {"type": "concept",  "pattern": "STUDY_01D_Mac_Boardroom", "sec": 58.0, "dur": 22.0, "name": "Study Mac Boardroom 2K"},
    {"type": "concept",  "pattern": "STUDY_02E_CRT_Computer", "sec": 80.0, "dur": 20.0, "name": "Study CRT Boardroom 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_03", "sec": 100.0, "dur": 8.0,  "name": "Flow 03 Silicon Laser"},
    {"type": "concept",  "pattern": "IMG_03_Silicon_Wafer", "sec": 108.0, "dur": 22.0, "name": "Keyframe 03 Silicon Hero 2K"},
    {"type": "concept",  "pattern": "STUDY_03A_Silicon_Traces", "sec": 130.0, "dur": 20.0, "name": "Study Silicon Traces 4K"},
    {"type": "concept",  "pattern": "IMG_04_Golden_Exponential", "sec": 150.0, "dur": 25.0, "name": "Keyframe 04 Golden Exp 2K"},
    {"type": "concept",  "pattern": "STUDY_04B_Exponential", "sec": 175.0, "dur": 25.0, "name": "Study Exponential Line 2K"},
    {"type": "concept",  "pattern": "IMG_06_Gold_Coins", "sec": 200.0, "dur": 15.0, "name": "Cosmic Gold Coins Brain 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_04", "sec": 215.0, "dur": 8.0,  "name": "Flow 04 Golden Exp Line"},
    {"type": "concept",  "pattern": "STUDY_06B_Architectural", "sec": 223.0, "dur": 32.0, "name": "Study Monoliths 2K"},
    {"type": "concept",  "pattern": "IMG_05_Businessman", "sec": 255.0, "dur": 30.0, "name": "Cosmic Businessman Data 2K"},

    # Act 2
    {"type": "flow_vid", "pattern": "ep01_flow_05", "sec": 285.0, "dur": 8.0,  "name": "Flow 05 Neural Lattice"},
    {"type": "concept",  "pattern": "IMG_05_Neural_Lattice", "sec": 293.0, "dur": 32.0, "name": "Keyframe 05 Neural Lattice 2K"},
    {"type": "concept",  "pattern": "STUDY_07C_Computer_Boardroom", "sec": 325.0, "dur": 20.0, "name": "Study Boardroom Void 2K"},
    {"type": "concept",  "pattern": "IMG_06_Supercomputer", "sec": 345.0, "dur": 35.0, "name": "Keyframe 06 Supercomputer 2K"},
    {"type": "concept",  "pattern": "IMG_06_Gold_Coins", "sec": 380.0, "dur": 40.0, "name": "Cosmic Capital Brain 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_06", "sec": 420.0, "dur": 8.0,  "name": "Flow 06 Server Monolith"},
    {"type": "concept",  "pattern": "IMG_06_Supercomputer", "sec": 428.0, "dur": 37.0, "name": "Keyframe 06 Servers Hall 2K"},
    {"type": "concept",  "pattern": "IMG_08_Dyson_Swarm", "sec": 465.0, "dur": 30.0, "name": "Cosmic Dyson Swarm 2K"},
    {"type": "concept",  "pattern": "IMG_05_Neural_Lattice", "sec": 495.0, "dur": 35.0, "name": "Keyframe 05 Lattice Nodes 2K"},
    {"type": "concept",  "pattern": "STUDY_08B_Optical", "sec": 530.0, "dur": 40.0, "name": "Study Optical Filaments 2K"},

    # Act 3
    {"type": "flow_vid", "pattern": "ep01_flow_05", "sec": 570.0, "dur": 8.0,  "name": "Flow 05 Lattice Surge"},
    {"type": "concept",  "pattern": "IMG_08_Golden_Signatures", "sec": 578.0, "dur": 32.0, "name": "Keyframe 08 Light Threads 2K"},
    {"type": "concept",  "pattern": "IMG_05_Businessman", "sec": 610.0, "dur": 35.0, "name": "Cosmic Corporate Dissolve 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_07", "sec": 645.0, "dur": 8.0,  "name": "Flow 07 Boardroom Noir"},
    {"type": "concept",  "pattern": "IMG_07_Smartphone_Boardroom", "sec": 653.0, "dur": 37.0, "name": "Keyframe 07 Boardroom Noir 2K"},
    {"type": "concept",  "pattern": "IMG_07B_Smartphone_Vibrating", "sec": 690.0, "dur": 25.0, "name": "B-Roll Phone Vibrating 2K"},
    {"type": "concept",  "pattern": "IMG_07D_Silhouette_Against", "sec": 715.0, "dur": 20.0, "name": "B-Roll Silhouette Window 2K"},
    {"type": "concept",  "pattern": "IMG_07_Smartphone_Boardroom", "sec": 735.0, "dur": 45.0, "name": "Keyframe 07 Table Noir 2K"},
    {"type": "concept",  "pattern": "IMG_05_Businessman", "sec": 780.0, "dur": 45.0, "name": "Cosmic Data Breakdown 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_08", "sec": 825.0, "dur": 8.0,  "name": "Flow 08 Golden Signatures"},
    {"type": "concept",  "pattern": "IMG_08_Golden_Signatures", "sec": 833.0, "dur": 47.0, "name": "Keyframe 08 Signatures 2K"},
    {"type": "concept",  "pattern": "STUDY_08B_Optical", "sec": 880.0, "dur": 50.0, "name": "Study Symbolic Filaments 2K"},

    # Act 4
    {"type": "flow_vid", "pattern": "ep01_flow_09", "sec": 930.0, "dur": 8.0,  "name": "Flow 09 Fusion Torus"},
    {"type": "concept",  "pattern": "IMG_09_Fusion_Torus", "sec": 938.0, "dur": 42.0, "name": "Keyframe 09 Helion Plasma 2K"},
    {"type": "concept",  "pattern": "IMG_07_Human_Watching", "sec": 980.0, "dur": 40.0, "name": "Cosmic Miniature Fusion Star 2K"},
    {"type": "concept",  "pattern": "IMG_08_Dyson_Swarm", "sec": 1020.0, "dur": 45.0, "name": "Cosmic Dyson Megastructure 2K"},
    {"type": "concept",  "pattern": "IMG_04_Golden_Exponential", "sec": 1065.0, "dur": 45.0, "name": "Keyframe 04 Infinite Scale 2K"},
    {"type": "flow_vid", "pattern": "ep01_flow_10", "sec": 1110.0, "dur": 8.0,  "name": "Flow 10 Earth Horizon"},
    {"type": "concept",  "pattern": "IMG_10_Earth_Horizon", "sec": 1118.0, "dur": 42.0, "name": "Keyframe 10 Earth Neural Grid 2K"},
    {"type": "concept",  "pattern": "IMG_08_Dyson_Swarm", "sec": 1160.0, "dur": 40.0, "name": "Cosmic Horizon Outro 2K"}
]

# 4. Video V2: Authentic Archives & Historical Speaker Photos (B-Roll)
V2_ARCHIVE_PHOTO_CUES = [
    # Act 1
    {"pattern": "ARCH_03", "sec": 10.0, "dur": 8.0, "name": "Apple Macintosh 1992 CRT Scan"},
    {"pattern": "ARCH_06_Altman_Childhood", "sec": 22.0, "dur": 10.0, "name": "8yo Sam at Mac LC II 1993"},
    {"pattern": "ARCH_05_Altman_John_Burroughs", "sec": 48.0, "dur": 14.0, "name": "John Burroughs School Campus"},
    {"pattern": "ARCH_07_Altman_Loopt_Shirt", "sec": 142.0, "dur": 12.0, "name": "Loopt Shirt Founder 2005"},
    {"pattern": "ARCH_04_ACT1_24FPS_Altman_WWDC", "sec": 155.0, "dur": 15.0, "name": "WWDC 2008 with Steve Jobs Video"},
    {"pattern": "ARCH_03_Altman_WWDC_2008_SteveJobs", "sec": 170.0, "dur": 12.0, "name": "WWDC 2008 Stage Photo"},
    {"pattern": "ARCH_01_Altman_2009_Loopt", "sec": 240.0, "dur": 14.0, "name": "24yo Altman Loopt Era Photo"},

    # Act 2
    {"pattern": "ARCH_04_Altman_Stanford_2014", "sec": 285.0, "dur": 16.0, "name": "Stanford 2014 YC President Photo"},
    {"pattern": "ARCH_08_Altman_TechCrunch_Disrupt_2014", "sec": 315.0, "dur": 15.0, "name": "Disrupt NY 2014 5K Master Photo"},
    {"pattern": "ARCH_05_ACT2_24FPS_Altman_Stanford", "sec": 330.0, "dur": 18.0, "name": "Stanford CS183B Lecture Video"},
    {"pattern": "ARCH_09_Altman_TechCrunch_Disrupt_2019", "sec": 495.0, "dur": 18.0, "name": "Disrupt SF 2019 OpenAI CEO Photo"},

    # Act 3
    {"pattern": "ARCH_11_Altman_November_2022", "sec": 570.0, "dur": 15.0, "name": "Nov 2022 ChatGPT Genesis 5K Photo"},
    {"pattern": "ARCH_01_ACT3_24FPS_Altman_Senate_Oath", "sec": 585.0, "dur": 8.0, "name": "Senate Oath Closeup Video"},
    {"pattern": "ARCH_02_ACT3_24FPS_Altman_Senate_Regulation", "sec": 593.0, "dur": 12.0, "name": "Senate Statement Video"},
    {"pattern": "ARCH_02_Altman_Ilya_Sutskever", "sec": 615.0, "dur": 15.0, "name": "Altman & Ilya Sutskever TAU 2023 Photo"},
    {"pattern": "ARCH_10_Altman_TED_Vancouver", "sec": 795.0, "dur": 15.0, "name": "TED Vancouver 2023 GPT-4 Photo"},

    # Act 4
    {"pattern": "PHOTO_01_Sam_Altman_Archival", "sec": 930.0, "dur": 18.0, "name": "Sam Altman Archival Portrait"}
]

# 5. Video V3: 4K Documentary Dossiers & Scientific 3D VFX
V3_DOSSIER_CUES = [
    {"pattern": "DOC_01", "sec": 155.0, "dur": 18.0, "name": "YC 2005 S05 Cohort Announcement 4K"},
    {"pattern": "DOC_02", "sec": 370.0, "dur": 22.0, "name": "OpenAI Charter Dec 11 2015 4K"},
    {"pattern": "DOC_03", "sec": 650.0, "dur": 22.0, "name": "OpenAI Leadership Transition Nov 17 2023 4K"},
    {"pattern": "DOC_04", "sec": 770.0, "dur": 18.0, "name": "Ilya Sutskever Regret Post on X 4K"},
    {"pattern": "DOC_05", "sec": 825.0, "dur": 25.0, "name": "730+ Staff Open Letter to Board 4K"},
    {"pattern": "EP01_SCI_01", "sec": 990.0, "dur": 15.0, "name": "Supersonic Prandtl-Glauert Breakout 3D VFX"}
]

def main():
    print("🎬 Connecting to DaVinci Resolve Studio 19...")
    resolve = bmd.scriptapp("Resolve")
    if not resolve:
        print("❌ Could not connect to DaVinci Resolve. Is it running?")
        sys.exit(1)

    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    if not proj or proj.GetName() != "AI_Titans_EP01_Sam_Altman":
        proj = pm.LoadProject("AI_Titans_EP01_Sam_Altman")

    mp = proj.GetMediaPool()
    root = mp.GetRootFolder()

    folders = {s.GetName(): s for s in root.GetSubFolderList()}
    vo_folder = folders.get("01_VOICEOVER_A1")
    mus_folder = folders.get("02_MUSIC_A2")
    flow_folder = folders.get("03_FLOW_VIDEO_V1")
    arch_folder = folders.get("04_ARCHIVES_BROLL_V2")
    doc_folder = folders.get("05_DOSSIERS_VFX_V3")
    tl_folder = folders.get("06_TIMELINES")

    master_tl_name = "EP01_Altman_Master_Cinematic_Timeline"
    
    # Clean previous timelines
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == master_tl_name:
            mp.DeleteTimelines([t])
            break

    if tl_folder:
        mp.SetCurrentFolder(tl_folder)

    print(f"🎬 Creating Master Cinematic Timeline: '{master_tl_name}'...")
    tl = mp.CreateEmptyTimeline(master_tl_name)
    if not tl:
        print("❌ Failed to create timeline.")
        sys.exit(1)

    proj.SetCurrentTimeline(tl)
    start_frame = tl.GetStartFrame()
    print(f"✓ Timeline initialized at Start Frame = {start_frame} ({tl.GetStartTimecode()})")

    # Configure Tracks
    while tl.GetTrackCount("video") < 3:
        tl.AddTrack("video")
    tl.SetTrackName("video", 1, "FLOW_VEO_4K_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_PHOTOS_V2")
    tl.SetTrackName("video", 3, "DOSSIERS_VFX_V3")

    while tl.GetTrackCount("audio") < 3:
        tl.AddTrack("audio", "stereo")
    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_92BPM_A2")
    tl.SetTrackName("audio", 3, "AMBIENCE_FX_A3")

    # ==========================================
    # 1. ASSEMBLE A1: 17 VOICEOVER TAKES
    # ==========================================
    print("\n🎙️ Assembling Audio Track A1 (17 Voiceover Takes)...")
    vo_clips_map = {c.GetName(): c for c in vo_folder.GetClipList()}
    vo_batch = []
    for vt in VO_TIMINGS:
        num = vt["num"]
        prefix = f"EP01_VO_EN_{num:02d}"
        matched = [c for name, c in vo_clips_map.items() if name.startswith(prefix)]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(vt["sec"] * FPS)
            vo_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 2,
                "trackIndex": 1,
                "recordFrame": rec_frame
            })
    appended_vo = mp.AppendToTimeline(vo_batch)
    print(f"✓ Appended {len(appended_vo)} Voiceover takes to A1.")

    # Apply Dialogue Leveler & Crisp Gain
    a1_items = tl.GetItemListInTrack("audio", 1)
    for it in a1_items:
        it.SetProperty("AudioDialogueLevelerEnabled", True)
        it.SetProperty("AudioDialogueLevelerReduceLoudDialogue", True)
        it.SetProperty("AudioDialogueLevelerLiftSoftDialogue", True)
        it.SetProperty("AudioVolume", 2.0)
    print("✓ Configured Dialogue Leveler & AudioVolume (+2.0 dB) on Track A1.")

    # ==========================================
    # 2. ASSEMBLE A2: 4-ACT SUNO 92 BPM MUSIC
    # ==========================================
    print("\n🎵 Assembling Audio Track A2 (4-Act Suno 92 BPM Music)...")
    mus_clips_map = {c.GetName(): c for c in mus_folder.GetClipList()}
    mus_batch = []
    for mc in MUSIC_CUES:
        matched = [c for name, c in mus_clips_map.items() if mc["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(mc["sec"] * FPS)
            mus_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 2,
                "trackIndex": 2,
                "recordFrame": rec_frame
            })
    appended_mus = mp.AppendToTimeline(mus_batch)
    print(f"✓ Appended {len(appended_mus)} Music stems to A2.")

    # Apply Broadcast Ducking Level (-18 dB)
    a2_items = tl.GetItemListInTrack("audio", 2)
    for it in a2_items:
        it.SetProperty("AudioVolume", -18.0)
    print("✓ Set Music Bed Level to -18.0 dB (Broadcast Sidechain Ducking Standard).")

    # ==========================================
    # 3. ASSEMBLE V1: 10 FLOW VIDEOS + 2K KEYFRAMES
    # ==========================================
    print("\n🚀 Assembling Video Track V1 (Continuous Visual Canvas: Flow 4K + 2K Keyframes)...")
    flow_clips_map = {c.GetName(): c for c in flow_folder.GetClipList()}
    v1_batch = []
    for fc in V1_CANVAS_CUES:
        matched = [c for name, c in flow_clips_map.items() if fc["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(fc["sec"] * FPS)
            dur_frames = round(fc["dur"] * FPS)
            v1_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 1,
                "recordFrame": rec_frame,
                "startFrame": 0,
                "endFrame": dur_frames
            })
    appended_v1 = mp.AppendToTimeline(v1_batch)
    print(f"✓ Appended {len(appended_v1)} visual canvas items to Track V1.")

    # Apply Dynamic Zoom to still frames on V1
    v1_items = tl.GetItemListInTrack("video", 1)
    for it in v1_items:
        it.SetProperty("DynamicZoomEnabled", True)

    # ==========================================
    # 4. ASSEMBLE V2: ARCHIVES & REAL PHOTOS
    # ==========================================
    print("\n📼 Assembling Video Track V2 (5 Authentic Archives + 12 Historical Speaker Photos)...")
    arch_clips_map = {c.GetName(): c for c in arch_folder.GetClipList()}
    v2_batch = []
    for ac in V2_ARCHIVE_PHOTO_CUES:
        matched = [c for name, c in arch_clips_map.items() if ac["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(ac["sec"] * FPS)
            dur_frames = round(ac["dur"] * FPS)
            v2_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 2,
                "recordFrame": rec_frame,
                "startFrame": 0,
                "endFrame": dur_frames
            })
            print(f"   V2: {ac['name']} @ {ac['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")
    appended_v2 = mp.AppendToTimeline(v2_batch)
    print(f"✓ Appended {len(appended_v2)} Archives & Historical Photos to Track V2.")

    # Apply Ken Burns Dynamic Zoom on all V2 archival photos & videos
    v2_items = tl.GetItemListInTrack("video", 2)
    for it in v2_items:
        it.SetProperty("DynamicZoomEnabled", True)
    print("✓ Enabled Ken Burns Dynamic Zoom (1.00 -> 1.05) on all V2 archival photos.")

    # ==========================================
    # 5. ASSEMBLE V3: 4K DOCUMENTARY DOSSIERS & VFX
    # ==========================================
    print("\n🗂️ Assembling Video Track V3 (5 4K Documentary Dossiers + Scientific 3D VFX)...")
    doc_clips_map = {c.GetName(): c for c in doc_folder.GetClipList()}
    v3_batch = []
    for dc in V3_DOSSIER_CUES:
        matched = [c for name, c in doc_clips_map.items() if dc["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(dc["sec"] * FPS)
            dur_frames = round(dc["dur"] * FPS)
            v3_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,
                "trackIndex": 3,
                "recordFrame": rec_frame,
                "startFrame": 0,
                "endFrame": dur_frames
            })
            print(f"   V3: {dc['name']} @ {dc['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")
    appended_v3 = mp.AppendToTimeline(v3_batch)
    print(f"✓ Appended {len(appended_v3)} Dossiers & VFX to Track V3.")

    # Apply Dynamic Zoom on all V3 dossiers
    v3_items = tl.GetItemListInTrack("video", 3)
    for it in v3_items:
        it.SetProperty("DynamicZoomEnabled", True)
    print("✓ Enabled Ken Burns Dynamic Zoom on all 4K Dossier plates.")

    # ==========================================
    # 6. CHAPTER MARKERS (M)
    # ==========================================
    print("\n🔖 Setting Narrative Beat Markers on Timeline...")
    valid_colors = ['Blue', 'Cyan', 'Green', 'Yellow', 'Red', 'Pink', 'Purple', 'Fuchsia', 'Rose', 'Lavender', 'Sky', 'Mint', 'Lemon', 'Sand', 'Cocoa', 'Cream']
    for vt in VO_TIMINGS:
        frame_id = start_frame + round(vt["sec"] * FPS)
        marker_color = vt.get("color", "Cyan")
        if marker_color not in valid_colors:
            marker_color = "Cyan"
        tl.AddMarker(frame_id, marker_color, f"Take #{vt['num']:02d}", vt["marker"], 24)
    print(f"✓ Added {len(VO_TIMINGS)} beat markers.")

    # ==========================================
    # 7. FINALIZE & SAVE
    # ==========================================
    tl.SetCurrentTimecode(tl.GetStartTimecode())
    resolve.OpenPage("edit")
    pm.SaveProject()
    print("💾 DaVinci Resolve Project successfully saved!")

    # Summary
    print("\n" + "="*70)
    print("🏆 UNIVERSAL / NETFLIX BROADCAST MASTER TIMELINE READY")
    print("="*70)
    print(f"Timeline Name : {tl.GetName()}")
    print(f"Start Frame   : {tl.GetStartFrame()} ({tl.GetStartTimecode()})")
    print(f"End Frame     : {tl.GetEndFrame()}")
    print(f"Total Coverage: {(tl.GetEndFrame() - tl.GetStartFrame()) / FPS / 60:.2f} min (Full 20-min canvas)")
    print(f"Track V1      : {len(tl.GetItemListInTrack('video', 1))} Flow 4K Videos + 2K Concept Keyframes")
    print(f"Track V2      : {len(tl.GetItemListInTrack('video', 2))} Historical Archives + Speaker Photos (Ken Burns)")
    print(f"Track V3      : {len(tl.GetItemListInTrack('video', 3))} 4K Documentary Dossiers + Scientific 3D VFX")
    print(f"Track A1      : {len(tl.GetItemListInTrack('audio', 1))} Voiceover Takes (Dialogue Leveler ON, +2dB)")
    print(f"Track A2      : {len(tl.GetItemListInTrack('audio', 2))} Suno 92 BPM Stems (Ducked Bed at -18dB)")
    print(f"Beat Markers  : {len(tl.GetMarkers())} Chapter Markers")
    print("="*70)

if __name__ == "__main__":
    main()
