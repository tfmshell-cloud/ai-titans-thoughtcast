#!/usr/bin/env python3
"""
Assemble AI Titans EP01 (Sam Altman) in DaVinci Resolve Studio 19
Automated Smart Bin hierarchy, media pool ingestion, and master timeline setup.
"""

import os
import sys
import glob

# Ensure Resolve Scripting API environment
RESOLVE_SCRIPT_API = "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
RESOLVE_SCRIPT_LIB = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
MODULES_PATH = os.path.join(RESOLVE_SCRIPT_API, "Modules")

os.environ["RESOLVE_SCRIPT_API"] = RESOLVE_SCRIPT_API
os.environ["RESOLVE_SCRIPT_LIB"] = RESOLVE_SCRIPT_LIB
if MODULES_PATH not in sys.path:
    sys.path.append(MODULES_PATH)

try:
    import DaVinciResolveScript as bmd
except ImportError:
    print("❌ Failed to import DaVinciResolveScript module.")
    sys.exit(1)

def get_resolve():
    resolve = bmd.scriptapp("Resolve")
    if not resolve:
        # Check global environment (when running inside Fusion/Resolve console)
        try:
            resolve = bmd.scriptapp("Resolve")
        except Exception:
            pass
    return resolve

def find_or_create_subfolder(media_pool, parent_folder, name):
    for sub in parent_folder.GetSubFolderList():
        if sub.GetName() == name:
            return sub
    return media_pool.AddSubFolder(parent_folder, name)

def main():
    print("🎬 Connecting to DaVinci Resolve Studio 19...")
    resolve = get_resolve()
    if not resolve:
        print("❌ Could not connect to DaVinci Resolve. Ensure DaVinci Resolve Studio is running.")
        sys.exit(1)

    pm = resolve.GetProjectManager()
    if not pm:
        print("❌ Could not get ProjectManager.")
        sys.exit(1)

    project_name = "AI_Titans_EP01_Sam_Altman"
    print(f"📁 Opening / Creating project '{project_name}'...")
    
    current_proj = pm.GetCurrentProject()
    if current_proj and current_proj.GetName() == project_name:
        project = current_proj
        print(f"✓ Project '{project_name}' is already active.")
    else:
        project = pm.LoadProject(project_name)
        if not project:
            print(f"Creating new project '{project_name}'...")
            project = pm.CreateProject(project_name)
            if not project:
                print(f"❌ Failed to create project '{project_name}'. Using current project: {current_proj.GetName() if current_proj else 'None'}")
                project = current_proj

    if not project:
        print("❌ No valid project found.")
        sys.exit(1)

    # 1. Configure Cinematic Project Settings (4K 24fps)
    print("⚙️ Applying Project Settings: 3840x2160 UHD @ 24.000 fps...")
    settings = {
        "timelineFrameRate": "24",
        "timelineResolutionWidth": "3840",
        "timelineResolutionHeight": "2160",
        "videoMonitorFormat": "UHD 2160p 24",
        "superScale": "1",
        "audioSampleRate": "48000"
    }
    for k, v in settings.items():
        try:
            project.SetSetting(k, v)
        except Exception as e:
            pass
    print("✓ Project settings calibrated.")

    # 2. Setup Smart Bin Hierarchy
    mp = project.GetMediaPool()
    root = mp.GetRootFolder()

    bins_def = {
        "01_VOICEOVER_A1": {
            "path_glob": "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/voiceover/EP01_ALTMAN/*.wav",
            "desc": "17 broadcast 48k/24b WAV takes of Adam (Radio Announcer)"
        },
        "02_MUSIC_A2": {
            "path_glob": "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/suno_stems/EP01_ALTMAN_SMART_BINS/*.wav",
            "desc": "4-Act Suno 92 BPM orchestral/analog music and drone stems"
        },
        "03_FLOW_VIDEO_V1": {
            "path_glob": "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/flow_renders/ep01_flow_*.mp4",
            "desc": "10 Google Flow / Veo 4K/HD renders"
        },
        "04_ARCHIVES_BROLL_V2": {
            "path_glob": "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/archives/EP01_VID_ARCH_*.mp4",
            "desc": "Authentic historical archives (WWDC 2008, Stanford, Senate)"
        },
        "05_DOSSIERS_VFX_V3": {
            "path_glob": "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/dossiers_press/EP01_DOC_*.png",
            "desc": "4K historical dossier plates"
        },
        "06_TIMELINES": {
            "path_glob": None,
            "desc": "Master Assembly Timelines"
        }
    }

    imported_summary = {}

    for bin_name, binfo in bins_def.items():
        sub = find_or_create_subfolder(mp, root, bin_name)
        mp.SetCurrentFolder(sub)
        print(f"📁 Bin '{bin_name}': {binfo['desc']}")
        
        if binfo["path_glob"]:
            files = sorted(glob.glob(binfo["path_glob"]))
            if files:
                items = mp.ImportMedia(files)
                imported_summary[bin_name] = len(items) if items else len(files)
                print(f"   ↳ Imported {len(files)} files into '{bin_name}'")
            else:
                imported_summary[bin_name] = 0
                print(f"   ↳ No files matched pattern {binfo['path_glob']}")
        else:
            imported_summary[bin_name] = 0

    # 3. Create or Update Master Timeline
    timelines_folder = find_or_create_subfolder(mp, root, "06_TIMELINES")
    mp.SetCurrentFolder(timelines_folder)

    timeline_name = "EP01_Altman_Master_Assembly_24fps"
    existing_tl = None
    for i in range(1, project.GetTimelineCount() + 1):
        tl = project.GetTimelineByIndex(i)
        if tl and tl.GetName() == timeline_name:
            existing_tl = tl
            break

    if existing_tl:
        print(f"✓ Timeline '{timeline_name}' already exists.")
        project.SetCurrentTimeline(existing_tl)
    else:
        print(f"🎬 Creating Timeline '{timeline_name}'...")
        new_tl = mp.CreateEmptyTimeline(timeline_name)
        if new_tl:
            project.SetCurrentTimeline(new_tl)
            print(f"✓ Created and activated Timeline '{timeline_name}'.")

    # 4. Save Project
    pm.SaveProject()
    print("💾 DaVinci Resolve Project successfully saved!")

    print("\n" + "="*60)
    print("🎉 EP01 DAVINCI RESOLVE STUDIO 19 SETUP COMPLETE!")
    print("="*60)
    for b_name, count in imported_summary.items():
        print(f" • {b_name:<22}: {count} items imported")
    print("="*60)

if __name__ == "__main__":
    main()
