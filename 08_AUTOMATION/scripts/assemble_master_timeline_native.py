#!/usr/bin/env python3
"""
Native Master Timeline Assembly for AI Titans EP01 (Sam Altman)
Direct programmatic construction using DaVinci Resolve Studio 19 Python API.
Accurately accounts for Timeline Start Frame (e.g. 86400 / 01:00:00:00).
Lays out:
  - Video Track V1: 10 Google Flow / Veo 4K clips (generative science)
  - Video Track V2: 5 Authentic Historical Archives (WWDC 2008, Stanford, Senate)
  - Video Track V3: 5 4K Documentary Dossier plates (YC 2005, OpenAI 2015, Coup, 730 Letter)
  - Audio Track A1: 17 Voiceover takes (Broadcast 48k/24b WAV • 115 WPM)
  - Audio Track A2: 4-Act Suno 92 BPM orchestral music & drone stems
  - Audio Track A3: Ambience & SFX bus
  - Narrative Beat Markers: 17 colored chapter markers aligned with start_frame
"""

import os
import sys
import json

# Ensure Resolve Scripting API environment
RESOLVE_SCRIPT_API = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
RESOLVE_SCRIPT_LIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
MODULES_PATH = os.path.join(RESOLVE_SCRIPT_API, "Modules")

os.environ["RESOLVE_SCRIPT_API"] = RESOLVE_SCRIPT_API
os.environ["RESOLVE_SCRIPT_LIB"] = RESOLVE_SCRIPT_LIB
if MODULES_PATH not in sys.path:
    sys.path.append(MODULES_PATH)

import DaVinciResolveScript as bmd

REPO_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
VO_DIR = os.path.join(REPO_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN")

FPS = 24.0

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

    # Find Subfolders
    folders = {}
    for sub in root.GetSubFolderList():
        folders[sub.GetName()] = sub

    vo_folder = folders.get("01_VOICEOVER_A1")
    mus_folder = folders.get("02_MUSIC_A2")
    flow_folder = folders.get("03_FLOW_VIDEO_V1")
    arch_folder = folders.get("04_ARCHIVES_BROLL_V2")
    doc_folder = folders.get("05_DOSSIERS_VFX_V3")
    tl_folder = folders.get("06_TIMELINES")

    if not all([vo_folder, mus_folder, flow_folder, arch_folder, doc_folder]):
        print("❌ Media pool folders missing. Run assemble_davinci_ep01.py first.")
        sys.exit(1)

    master_tl_name = "EP01_Altman_Master_Cinematic_Timeline"
    
    # Clean up older test timelines
    timelines_to_delete = []
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() in [master_tl_name, "TEST_TIMELINE", "EP01_Voiceover_Assembly_Track_A1", "EP01_Altman_Master_Assembly_24fps"]:
            timelines_to_delete.append(t)
    
    if timelines_to_delete:
        print(f"🧹 Cleaning up {len(timelines_to_delete)} temporary/previous timelines...")
        mp.DeleteTimelines(timelines_to_delete)

    # 1. Create Pristine Master Timeline
    print(f"🎬 Creating Master Timeline: '{master_tl_name}'...")
    if tl_folder:
        mp.SetCurrentFolder(tl_folder)

    tl = mp.CreateEmptyTimeline(master_tl_name)
    if not tl:
        print(f"❌ Failed to create timeline '{master_tl_name}'")
        sys.exit(1)

    proj.SetCurrentTimeline(tl)
    start_frame = tl.GetStartFrame()
    print(f"✓ Timeline initialized with Start Frame = {start_frame} ({tl.GetStartTimecode()})")

    # 2. Configure Tracks
    while tl.GetTrackCount("video") < 3:
        tl.AddTrack("video")
    tl.SetTrackName("video", 1, "FLOW_4K_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_BROLL_V2")
    tl.SetTrackName("video", 3, "DOSSIERS_TITLES_V3")

    while tl.GetTrackCount("audio") < 3:
        tl.AddTrack("audio", "stereo")
    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_92BPM_A2")
    tl.SetTrackName("audio", 3, "AMBIENCE_FX_A3")

    print("✓ Tracks configured:")
    print("   V1: FLOW_4K_V1 | V2: ARCHIVES_BROLL_V2 | V3: DOSSIERS_TITLES_V3")
    print("   A1: VOICEOVER_A1 | A2: MUSIC_92BPM_A2 | A3: AMBIENCE_FX_A3")

    # 3. Assemble Track A1: 17 Voiceover Takes
    print("\n🎙️ Assembling Audio Track A1 (17 Voiceover Takes)...")
    vo_clips_map = {c.GetName(): c for c in vo_folder.GetClipList()}
    vo_append_batch = []
    for vt in VO_TIMINGS:
        num = vt["num"]
        prefix = f"EP01_VO_EN_{num:02d}"
        matched = [c for name, c in vo_clips_map.items() if name.startswith(prefix)]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(vt["sec"] * FPS)
            vo_append_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 2,          # Audio only
                "trackIndex": 1,         # Audio Track A1
                "recordFrame": rec_frame
            })
            print(f"   Take #{num:02d} @ {vt['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")

    appended_vo = mp.AppendToTimeline(vo_append_batch)
    print(f"✓ Appended {len(appended_vo)} Voiceover takes to Track A1.")

    # 4. Assemble Track A2: 4-Act Suno 92 BPM Music
    print("\n🎵 Assembling Audio Track A2 (4-Act Suno 92 BPM Music)...")
    mus_clips_map = {c.GetName(): c for c in mus_folder.GetClipList()}
    music_cues = [
        {"pattern": "MUS_01_ACT1", "sec": 0.0,    "name": "Act 1: Introspection (92 BPM)"},
        {"pattern": "AMB_07_ACT2", "sec": 285.0,  "name": "Act 2: Tension Drone (92 BPM)"},
        {"pattern": "MUS_09_ACT3", "sec": 570.0,  "name": "Act 3: Crisis & ChatGPT (92 BPM)"},
        {"pattern": "MUS_15_ACT4", "sec": 930.0,  "name": "Act 4: Future Horizon Finale (92 BPM)"}
    ]
    mus_append_batch = []
    for mc in music_cues:
        matched = [c for name, c in mus_clips_map.items() if mc["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(mc["sec"] * FPS)
            mus_append_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 2,          # Audio only
                "trackIndex": 2,         # Audio Track A2
                "recordFrame": rec_frame
            })
            print(f"   {mc['name']} @ {mc['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")

    appended_mus = mp.AppendToTimeline(mus_append_batch)
    print(f"✓ Appended {len(appended_mus)} Music stems to Track A2.")

    # 5. Assemble Track V1: 10 Google Flow 4K Videos
    print("\n🚀 Assembling Video Track V1 (10 Google Flow 4K Renders)...")
    flow_clips_map = {c.GetName(): c for c in flow_folder.GetClipList()}
    flow_cues = [
        {"num": 1,  "sec": 0.0},
        {"num": 2,  "sec": 18.0},
        {"num": 3,  "sec": 100.0},
        {"num": 4,  "sec": 215.0},
        {"num": 5,  "sec": 285.0},
        {"num": 6,  "sec": 420.0},
        {"num": 7,  "sec": 645.0},
        {"num": 8,  "sec": 825.0},
        {"num": 9,  "sec": 930.0},
        {"num": 10, "sec": 1110.0}
    ]
    flow_append_batch = []
    for fc in flow_cues:
        prefix = f"ep01_flow_{fc['num']:02d}"
        matched = [c for name, c in flow_clips_map.items() if name.startswith(prefix)]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(fc["sec"] * FPS)
            flow_append_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,          # Video only
                "trackIndex": 1,         # Video Track V1
                "recordFrame": rec_frame
            })
            print(f"   Flow #{fc['num']:02d} @ {fc['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")

    appended_flow = mp.AppendToTimeline(flow_append_batch)
    print(f"✓ Appended {len(appended_flow)} Flow clips to Track V1.")

    # 6. Assemble Track V2: 5 Authentic Archives
    print("\n📼 Assembling Video Track V2 (5 Authentic Historical Archives)...")
    arch_clips_map = {c.GetName(): c for c in arch_folder.GetClipList()}
    arch_cues = [
        {"pattern": "ARCH_03", "sec": 28.0,  "name": "Apple Macintosh 1992 CRT"},
        {"pattern": "ARCH_04", "sec": 115.0, "name": "Altman WWDC 2008 with Steve Jobs"},
        {"pattern": "ARCH_05", "sec": 330.0, "name": "Stanford CS183B Lecture"},
        {"pattern": "ARCH_01", "sec": 570.0, "name": "Altman Senate Oath Closeup"},
        {"pattern": "ARCH_02", "sec": 582.0, "name": "Altman Senate Statement on AI"}
    ]
    arch_append_batch = []
    for ac in arch_cues:
        matched = [c for name, c in arch_clips_map.items() if ac["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(ac["sec"] * FPS)
            arch_append_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,          # Video only
                "trackIndex": 2,         # Video Track V2
                "recordFrame": rec_frame
            })
            print(f"   {ac['name']} @ {ac['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")

    appended_arch = mp.AppendToTimeline(arch_append_batch)
    print(f"✓ Appended {len(appended_arch)} Archives to Track V2.")

    # 7. Assemble Track V3: 5 4K Documentary Dossiers
    print("\n🗂️ Assembling Video Track V3 (5 4K Documentary Dossiers)...")
    doc_clips_map = {c.GetName(): c for c in doc_folder.GetClipList()}
    doc_cues = [
        {"pattern": "DOC_01", "sec": 160.0, "name": "YC 2005 Program"},
        {"pattern": "DOC_02", "sec": 390.0, "name": "OpenAI Dec 2015 Introducing"},
        {"pattern": "DOC_03", "sec": 690.0, "name": "Board Ouster Nov 17 2023"},
        {"pattern": "DOC_04", "sec": 780.0, "name": "Sutskever Regret Post Nov 20"},
        {"pattern": "DOC_05", "sec": 872.0, "name": "730 Employees Open Letter"}
    ]
    doc_append_batch = []
    for dc in doc_cues:
        matched = [c for name, c in doc_clips_map.items() if dc["pattern"] in name]
        if matched:
            clip = matched[0]
            rec_frame = start_frame + round(dc["sec"] * FPS)
            doc_append_batch.append({
                "mediaPoolItem": clip,
                "mediaType": 1,          # Video only
                "trackIndex": 3,         # Video Track V3
                "recordFrame": rec_frame
            })
            print(f"   {dc['name']} @ {dc['sec']:6.1f}s (Frame {rec_frame}): {clip.GetName()}")

    appended_doc = mp.AppendToTimeline(doc_append_batch)
    print(f"✓ Appended {len(appended_doc)} Dossiers to Track V3.")

    # 8. Add Chapter / Beat Markers (M)
    print("\n🔖 Setting Narrative Beat Markers on Timeline...")
    valid_colors = ['Blue', 'Cyan', 'Green', 'Yellow', 'Red', 'Pink', 'Purple', 'Fuchsia', 'Rose', 'Lavender', 'Sky', 'Mint', 'Lemon', 'Sand', 'Cocoa', 'Cream']
    for vt in VO_TIMINGS:
        frame_id = start_frame + round(vt["sec"] * FPS)
        marker_color = vt.get("color", "Cyan")
        if marker_color not in valid_colors:
            marker_color = "Cyan"
        tl.AddMarker(frame_id, marker_color, f"Take #{vt['num']:02d}", vt["marker"], 24)

    print(f"✓ Added {len(VO_TIMINGS)} beat markers.")

    # 9. Set Playhead to Start and Open Edit Page
    tl.SetCurrentTimecode(tl.GetStartTimecode())
    resolve.OpenPage("edit")

    # 10. Save Project
    pm.SaveProject()
    print("💾 DaVinci Resolve Project successfully saved!")

    # Verification Report
    print("\n" + "="*65)
    print("🎉 MASTER TIMELINE ASSEMBLY COMPLETE IN DAVINCI RESOLVE STUDIO 19")
    print("="*65)
    print(f"Timeline Name : {tl.GetName()}")
    print(f"Start Frame   : {tl.GetStartFrame()} ({tl.GetStartTimecode()})")
    print(f"End Frame     : {tl.GetEndFrame()} ({tl.GetCurrentTimecode()})")
    print(f"Total Duration: {(tl.GetEndFrame() - tl.GetStartFrame()) / FPS:.1f}s (~{(tl.GetEndFrame() - tl.GetStartFrame()) / FPS / 60:.2f} min)")
    print(f"Track V1      : {len(tl.GetItemListInTrack('video', 1))} Flow 4K Clips")
    print(f"Track V2      : {len(tl.GetItemListInTrack('video', 2))} Historical Archives")
    print(f"Track V3      : {len(tl.GetItemListInTrack('video', 3))} 4K Dossier Plates")
    print(f"Track A1      : {len(tl.GetItemListInTrack('audio', 1))} Voiceover Takes (Adam 48k WAV)")
    print(f"Track A2      : {len(tl.GetItemListInTrack('audio', 2))} Suno 92 BPM 4-Act Stems")
    print(f"Track A3      : {len(tl.GetItemListInTrack('audio', 3))} Ambience & SFX Sub-bus")
    print(f"Beat Markers  : {len(tl.GetMarkers())} Chapter Markers on Timeline")
    print("="*65)

if __name__ == "__main__":
    main()
