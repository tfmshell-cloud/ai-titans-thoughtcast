#!/usr/bin/env python3
"""
Generate Master FCPXML and Assemble Complete EP01 Timeline in DaVinci Resolve Studio 19
Tracks:
  - Audio A1 (Lane -1): 17 Voiceover takes (Broadcast 48k/24b WAV)
  - Audio A2 (Lane -2): 4-Act Suno 92 BPM orchestral music & drone stems
  - Video V1 (Lane 1): 10 Google Flow / Veo 4K renders (Optical Flow 24fps)
  - Video V2 (Lane 2): 5 Authentic Historical Archives + 5 4K Documentary Dossiers
"""

import os
import sys
import json
import wave
import xml.etree.ElementTree as ET

REPO_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
VO_DIR = os.path.join(REPO_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN")
SUNO_DIR = os.path.join(REPO_ROOT, "03_AUDIO/suno_stems/EP01_ALTMAN_SMART_BINS")
FLOW_DIR = os.path.join(REPO_ROOT, "05_RAW_FOOTAGE/flow_renders")
ARCH_DIR = os.path.join(REPO_ROOT, "05_RAW_FOOTAGE/archives")
DOC_DIR = os.path.join(REPO_ROOT, "05_RAW_FOOTAGE/dossiers_press")
PORT_DIR = os.path.join(REPO_ROOT, "05_RAW_FOOTAGE/speaker_portraits")
OUT_FCPXML = os.path.join(REPO_ROOT, "06_DAVINCI_PROJECTS/EP01_Altman_Master_Timeline_Complete_24fps.fcpxml")

# 1. Planned Start Offsets (seconds) for 17 Voiceover Takes
VO_STARTS = [
    0.0,    # Take 01: [00:00] Intro Hook
    15.0,   # Take 02: [00:15] Macintosh LC II
    58.0,   # Take 03: [00:58] John Burroughs Safe Space
    100.0,  # Take 04: [01:40] Stanford Drop-out & Loopt
    150.0,  # Take 05: [02:30] YC Batch 1 Scurvy Grit
    215.0,  # Take 06: [03:35] Compound Interest
    285.0,  # Take 07: [04:45] YC President at 28 (Act 2 opening)
    345.0,  # Take 08: [05:45] Rosewood Hotel Dinner & Threat
    420.0,  # Take 09: [07:00] OpenAI Founding Dec 2015
    495.0,  # Take 10: [08:15] Capped-Profit & Bill Gates
    570.0,  # Take 11: [09:30] ChatGPT Launch & 100M (Act 3 opening)
    645.0,  # Take 12: [10:45] Friday Board Coup Nov 17
    735.0,  # Take 13: [12:15] 120 Hours Drama & Guest Badge
    825.0,  # Take 14: [13:45] 730 Signatures Triumphant Return
    930.0,  # Take 15: [15:30] Stargate & Helion Fusion (Act 4 opening)
    1020.0, # Take 16: [17:00] 3 Rules of Exponential Life
    1110.0  # Take 17: [18:30] Future is Created Now Outro
]

def build_fcpxml():
    with open(os.path.join(VO_DIR, "SEGMENTS_MANIFEST_EN.json")) as f:
        manifest = json.load(f)

    # XML Root
    fcpxml = ET.Element("fcpxml", version="1.9")
    resources = ET.SubElement(fcpxml, "resources")

    # Format 4K 24fps
    ET.SubElement(resources, "format", {
        "id": "r1",
        "name": "FFVideoFormat3840x2160p24",
        "frameDuration": "100/2400s",
        "width": "3840",
        "height": "2160",
        "colorSpace": "1-1-1 (Rec. 709)"
    })

    # Voiceover Assets
    vo_clip_meta = []
    for i, it in enumerate(manifest):
        asset_id = f"a_vo{i+1:02d}"
        wav_file = it["wav_file"]
        wav_path = os.path.join(VO_DIR, wav_file)
        with wave.open(wav_path, "rb") as w:
            dur = w.getnframes() / float(w.getframerate())
        
        ET.SubElement(resources, "asset", {
            "id": asset_id,
            "name": os.path.splitext(wav_file)[0],
            "src": f"file://{wav_path}",
            "start": "0s",
            "duration": f"{dur:.3f}s",
            "hasAudio": "1",
            "audioSources": "1",
            "audioChannels": "1",
            "audioRate": "48000"
        })
        vo_clip_meta.append({
            "id": asset_id,
            "name": f"VO_Take_{i+1:02d}",
            "start": VO_STARTS[i],
            "dur": dur,
            "title": it.get("title", f"Take #{i+1}")
        })

    # Music Assets
    suno_tracks = [
        {"id": "a_mus1", "name": "EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro", "file": "EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav", "offset": 0.0, "dur": 285.0},
        {"id": "a_amb2", "name": "EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension", "file": "EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension.wav", "offset": 285.0, "dur": 285.0},
        {"id": "a_mus3", "name": "EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion", "file": "EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav", "offset": 570.0, "dur": 360.0},
        {"id": "a_mus4", "name": "EP01_MUS_15_ACT4_92BPM_Future_Horizon_Finale", "file": "EP01_MUS_15_ACT4_92BPM_Future_Horizon_Finale.wav", "offset": 930.0, "dur": 270.0}
    ]
    for s in suno_tracks:
        ET.SubElement(resources, "asset", {
            "id": s["id"],
            "name": s["name"],
            "src": f"file://{os.path.join(SUNO_DIR, s['file'])}",
            "start": "0s",
            "duration": f"{s['dur']:.1f}s",
            "hasAudio": "1",
            "audioSources": "1",
            "audioChannels": "2",
            "audioRate": "48000"
        })

    # Flow Video Assets (10 clips)
    flow_clips = [
        {"id": "v_fl01", "name": "ep01_flow_01_mac_chassis", "offset": 0.0, "dur": 8.0},
        {"id": "v_fl02", "name": "ep01_flow_02_crt_code", "offset": 18.0, "dur": 8.0},
        {"id": "v_fl03", "name": "ep01_flow_03_silicon_laser", "offset": 100.0, "dur": 8.0},
        {"id": "v_fl04", "name": "ep01_flow_04_exponential_line", "offset": 215.0, "dur": 8.0},
        {"id": "v_fl05", "name": "ep01_flow_05_neural_lattice", "offset": 285.0, "dur": 8.0},
        {"id": "v_fl06", "name": "ep01_flow_06_server_monolith", "offset": 420.0, "dur": 8.0},
        {"id": "v_fl07", "name": "ep01_flow_07_boardroom_noir", "offset": 645.0, "dur": 8.0},
        {"id": "v_fl08", "name": "ep01_flow_08_golden_signatures", "offset": 825.0, "dur": 8.0},
        {"id": "v_fl09", "name": "ep01_flow_09_fusion_torus", "offset": 930.0, "dur": 8.0},
        {"id": "v_fl10", "name": "ep01_flow_10_earth_horizon", "offset": 1110.0, "dur": 8.0}
    ]
    for fc in flow_clips:
        ET.SubElement(resources, "asset", {
            "id": fc["id"],
            "name": fc["name"],
            "src": f"file://{os.path.join(FLOW_DIR, fc['name'] + '.mp4')}",
            "start": "0s",
            "duration": "8s",
            "hasVideo": "1",
            "hasAudio": "1",
            "format": "r1"
        })

    # Archives Assets
    arch_clips = [
        {"id": "v_ar03", "name": "EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT", "offset": 28.0, "dur": 8.0},
        {"id": "v_ar04", "name": "EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs", "offset": 115.0, "dur": 8.0},
        {"id": "v_ar05", "name": "EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture", "offset": 330.0, "dur": 8.0},
        {"id": "v_ar01", "name": "EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup", "offset": 570.0, "dur": 8.0},
        {"id": "v_ar02", "name": "EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement", "offset": 582.0, "dur": 8.0}
    ]
    for ac in arch_clips:
        ET.SubElement(resources, "asset", {
            "id": ac["id"],
            "name": ac["name"],
            "src": f"file://{os.path.join(ARCH_DIR, ac['name'] + '.mp4')}",
            "start": "0s",
            "duration": "8s",
            "hasVideo": "1",
            "hasAudio": "1",
            "format": "r1"
        })

    # 4K Dossier Assets
    doc_clips = [
        {"id": "img_d01", "name": "EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program", "offset": 160.0, "dur": 10.0},
        {"id": "img_d02", "name": "EP01_DOC_02_ACT2_OpenAI_Introducing_Dec11_2015", "offset": 390.0, "dur": 12.0},
        {"id": "img_d03", "name": "EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023", "offset": 690.0, "dur": 12.0},
        {"id": "img_d04", "name": "EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023", "offset": 780.0, "dur": 10.0},
        {"id": "img_d05", "name": "EP01_DOC_05_ACT3_730_Employees_Open_Letter", "offset": 872.0, "dur": 12.0}
    ]
    for dc in doc_clips:
        ET.SubElement(resources, "asset", {
            "id": dc["id"],
            "name": dc["name"],
            "src": f"file://{os.path.join(DOC_DIR, dc['name'] + '.png')}",
            "start": "0s",
            "duration": f"{dc['dur']:.1f}s",
            "hasVideo": "1",
            "format": "r1"
        })

    # Portrait Asset
    ET.SubElement(resources, "asset", {
        "id": "img_port",
        "name": "EP01_PHOTO_01_Sam_Altman_Archival_Portrait",
        "src": f"file://{os.path.join(PORT_DIR, 'EP01_PHOTO_01_Sam_Altman_Archival_Portrait.jpg')}",
        "start": "0s",
        "duration": "8s",
        "hasVideo": "1",
        "format": "r1"
    })

    # Library / Project / Sequence
    library = ET.SubElement(fcpxml, "library")
    event = ET.SubElement(library, "event", name="AI_Titans_EP01_Event")
    project = ET.SubElement(event, "project", name="EP01_Altman_Master_Timeline_Complete_24fps")
    sequence = ET.SubElement(project, "sequence", {
        "format": "r1",
        "duration": "1200s",
        "tcStart": "0s",
        "tcFormat": "NDF",
        "audioLayout": "stereo",
        "audioRate": "48k"
    })
    spine = ET.SubElement(sequence, "spine")
    gap = ET.SubElement(spine, "gap", name="Master_Spine_Gap_20min", offset="0s", duration="1200s", start="0s")

    # 1. Connected Video V1 (Lane 1): Flow 4K Videos
    for fc in flow_clips:
        ET.SubElement(gap, "asset-clip", {
            "name": fc["name"],
            "ref": fc["id"],
            "lane": "1",
            "offset": f"{fc['offset']:.1f}s",
            "duration": f"{fc['dur']:.1f}s",
            "start": "0s",
            "audioRole": "effects"
        })

    # 2. Connected Video V2 (Lane 2): Archives, Dossiers, Portrait
    for ac in arch_clips:
        ET.SubElement(gap, "asset-clip", {
            "name": ac["name"],
            "ref": ac["id"],
            "lane": "2",
            "offset": f"{ac['offset']:.1f}s",
            "duration": f"{ac['dur']:.1f}s",
            "start": "0s",
            "audioRole": "effects"
        })
    for dc in doc_clips:
        ET.SubElement(gap, "video", {
            "name": dc["name"],
            "ref": dc["id"],
            "lane": "2",
            "offset": f"{dc['offset']:.1f}s",
            "duration": f"{dc['dur']:.1f}s",
            "start": "0s"
        })
    ET.SubElement(gap, "video", {
        "name": "Altman_Archival_Portrait",
        "ref": "img_port",
        "lane": "2",
        "offset": "235.0s",
        "duration": "8.0s",
        "start": "0s"
    })

    # 3. Connected Audio A1 (Lane -1): 17 Voiceover Takes
    for vm in vo_clip_meta:
        ET.SubElement(gap, "asset-clip", {
            "name": vm["name"],
            "ref": vm["id"],
            "lane": "-1",
            "offset": f"{vm['start']:.1f}s",
            "duration": f"{vm['dur']:.3f}s",
            "start": "0s",
            "role": "dialogue"
        })

    # 4. Connected Audio A2 (Lane -2): 4-Act Suno 92 BPM Music
    for s in suno_tracks:
        ET.SubElement(gap, "asset-clip", {
            "name": s["name"],
            "ref": s["id"],
            "lane": "-2",
            "offset": f"{s['offset']:.1f}s",
            "duration": f"{s['dur']:.1f}s",
            "start": "0s",
            "role": "music"
        })

    # 5. Narrative Beat Markers
    markers = [
        (0.0, "ACT I: St. Louis 1993 — Macintosh LC II (Rule of Non-Conformity)"),
        (58.0, "ACT I: John Burroughs School — The Safe Space Speech"),
        (100.0, "ACT I: Stanford CS & Loopt Genesis"),
        (150.0, "ACT I: Y Combinator S05 Batch & Paul Graham"),
        (215.0, "ACT I: The Exponential Compound Interest Rule"),
        (285.0, "ACT II: YC President at 28 — The Architect of Tech"),
        (345.0, "ACT II: Rosewood Hotel Secret Dinner — Google vs Humanity"),
        (420.0, "ACT II: Dec 11, 2015 — OpenAI Non-Profit Founding"),
        (495.0, "ACT II: The Microsoft $1B Deal & Capped-Profit"),
        (570.0, "ACT III: Nov 30, 2022 — ChatGPT Explosion & Senate Testimony"),
        (645.0, "ACT III: Friday Board Coup — 12:00 Google Meet Ouster"),
        (735.0, "ACT III: 120 Hours of Chaos & Guest Badge"),
        (825.0, "ACT III: 730 Signatures — Triumphant Reinstatement"),
        (930.0, "ACT IV: Project Stargate & Helion Fusion Energy"),
        (1020.0, "ACT IV: The Three Rules of Exponential Life"),
        (1110.0, "ACT IV: Outro — The Future is Created Now")
    ]
    for sec, val in markers:
        ET.SubElement(gap, "marker", {
            "start": f"{sec:.1f}s",
            "duration": "100/2400s",
            "value": val
        })

    # Write formatted XML
    tree = ET.ElementTree(fcpxml)
    ET.indent(tree, space="  ", level=0)
    tree.write(OUT_FCPXML, encoding="utf-8", xml_declaration=True)
    print(f"✓ Master FCPXML generated: {OUT_FCPXML}")
    return OUT_FCPXML

def import_to_davinci(fcpxml_path):
    print("🎬 Connecting to DaVinci Resolve Studio 19...")
    RESOLVE_SCRIPT_API = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
    RESOLVE_SCRIPT_LIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
    MODULES_PATH = os.path.join(RESOLVE_SCRIPT_API, "Modules")
    os.environ["RESOLVE_SCRIPT_API"] = RESOLVE_SCRIPT_API
    os.environ["RESOLVE_SCRIPT_LIB"] = RESOLVE_SCRIPT_LIB
    if MODULES_PATH not in sys.path:
        sys.path.append(MODULES_PATH)

    import DaVinciResolveScript as bmd
    resolve = bmd.scriptapp("Resolve")
    if not resolve:
        print("❌ Could not connect to DaVinci Resolve. Is it running?")
        sys.exit(1)

    pm = resolve.GetProjectManager()
    project = pm.GetCurrentProject()
    if not project or project.GetName() != "AI_Titans_EP01_Sam_Altman":
        project = pm.LoadProject("AI_Titans_EP01_Sam_Altman")
        if not project:
            project = pm.CreateProject("AI_Titans_EP01_Sam_Altman")

    mp = project.GetMediaPool()
    
    # Switch to 06_TIMELINES folder
    root = mp.GetRootFolder()
    tl_folder = None
    for sub in root.GetSubFolderList():
        if sub.GetName() == "06_TIMELINES":
            tl_folder = sub
            break
    if tl_folder:
        mp.SetCurrentFolder(tl_folder)

    print(f"📥 Importing master timeline from: {fcpxml_path}...")
    imported_tl = mp.ImportTimelineFromFile(fcpxml_path)
    if imported_tl:
        print(f"🎉 Successfully imported timeline: '{imported_tl.GetName()}'")
        project.SetCurrentTimeline(imported_tl)
        v_count = imported_tl.GetTrackCount("video")
        a_count = imported_tl.GetTrackCount("audio")
        print(f"📊 Timeline Tracks: {v_count} Video Tracks / {a_count} Audio Tracks")
        for a_idx in range(1, a_count + 1):
            items = imported_tl.GetItemListInTrack("audio", a_idx)
            print(f"   Audio Track A{a_idx}: {len(items)} clips")
        for v_idx in range(1, v_count + 1):
            items = imported_tl.GetItemListInTrack("video", v_idx)
            print(f"   Video Track V{v_idx}: {len(items)} clips")
    else:
        print("⚠️ Direct import returned None, checking current timeline...")

    pm.SaveProject()
    print("💾 DaVinci Resolve Project saved!")

if __name__ == "__main__":
    fcpxml_file = build_fcpxml()
    import_to_davinci(fcpxml_file)
