#!/usr/bin/env python3
"""
Global Media Pool Ingestion for all 10 Titans into DaVinci Resolve Studio 19
- Sam Altman (EP01)
- Jensen Huang (EP02)
- Demis Hassabis (EP03)
- Geoffrey Hinton (EP04)
- Yann LeCun (EP05)
- Ilya Sutskever (EP06)
- Dario Amodei / Anthropic (EP07)
- Fei-Fei Li (EP08)
- Yoshua Bengio (EP09)
- Andrew Ng (EP10)
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

def ingest_all():
    resolve = bmd.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()
    root = mp.GetRootFolder()

    base_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
    raw_dir = os.path.join(base_dir, "05_RAW_FOOTAGE")
    audio_dir = os.path.join(base_dir, "03_AUDIO")

    def get_or_create_subfolder(parent, name):
        for sub in parent.GetSubFolderList():
            if sub.GetName() == name:
                return sub
        return mp.AddSubFolder(parent, name)

    targets = [
        ("07_ALL_10_TITANS_PORTRAITS", os.path.join(raw_dir, "speaker_portraits")),
        ("08_ALL_10_TITANS_ARCHIVES", os.path.join(raw_dir, "archives")),
        ("09_ALL_10_TITANS_SCIENTIFIC_VFX", os.path.join(raw_dir, "scientific_animations")),
        ("10_ALL_10_TITANS_MUSIC_STEMS", os.path.join(audio_dir, "suno_stems", "00_MASTER_POOL_ORIGINAL")),
        ("11_ALL_10_TITANS_FLOW_BATCH3_GAMING", os.path.join(raw_dir, "flow_images", "BATCH3_GAMING_CHESS_GO_SCIENCE")),
        ("12_ALL_10_TITANS_FLOW_BATCH4_COSMIC", os.path.join(raw_dir, "flow_images", "BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE")),
        ("13_ALL_10_TITANS_FLOW_RENDERS", os.path.join(raw_dir, "flow_renders")),
    ]

    total_imported = 0
    for bin_name, folder_path in targets:
        if not os.path.exists(folder_path):
            continue
        bin_folder = get_or_create_subfolder(root, bin_name)
        mp.SetCurrentFolder(bin_folder)
        
        files_to_import = []
        for f in sorted(os.listdir(folder_path)):
            if f.endswith(('.mp4', '.jpg', '.png', '.webp', '.wav')) and not f.startswith('.'):
                files_to_import.append(os.path.join(folder_path, f))

        if files_to_import:
            items = mp.ImportMedia(files_to_import)
            count = len(items) if items else 0
            total_imported += count
            print(f"✓ Bin '{bin_name}': imported {count} items from {folder_path}")

    pm.SaveProject()
    print(f"\n=======================================================")
    print(f"🏆 ALL 10 TITANS MEDIA ASSETS INGESTED: {total_imported} NEW CLIPS")
    print(f"=======================================================")

if __name__ == "__main__":
    ingest_all()
    os._exit(0)
