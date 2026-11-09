#!/usr/bin/env python3
"""
Complete Global Media Ingestion for DaVinci Resolve Studio 21
Ingests ALL media across ALL 10 AI Titans:
- Chess, Go, AlphaGo Move 37, gaming, robotics, superclusters, Dyson swarms,
  scientific 3D animations, all historical archives, young portraits,
  press dossiers, Suno music stems for all 10 heroes, voiceovers, and mechanical keyboard sfx!
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

def ingest_master():
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
        # 1. Portraits & Archives
        ("07_ALL_10_TITANS_PORTRAITS", os.path.join(raw_dir, "speaker_portraits")),
        ("08_ALL_10_TITANS_ARCHIVES", os.path.join(raw_dir, "archives")),
        ("14_EP01_ALTMAN_ARCHIVE_PHOTOS", os.path.join(raw_dir, "speaker_portraits", "young_altman")),
        ("15_EP01_V2_MASTER_CLIPS", os.path.join(raw_dir, "archives", "v2_master_clips")),

        # 2. Scientific 3D VFX & Animations
        ("09_ALL_10_TITANS_SCIENTIFIC_VFX", os.path.join(raw_dir, "scientific_animations")),

        # 3. Flow Images (Chess, Go, Cosmic, Hardware, Science)
        ("11_ALL_10_TITANS_FLOW_BATCH3_GAMING_CHESS_GO", os.path.join(raw_dir, "flow_images", "BATCH3_GAMING_CHESS_GO_SCIENCE")),
        ("12_ALL_10_TITANS_FLOW_BATCH4_COSMIC_HARDWARE", os.path.join(raw_dir, "flow_images", "BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE")),
        ("17_EP01_ALTMAN_KEYFRAMES", os.path.join(raw_dir, "flow_images", "EP01_Altman", "01_primary_keyframes")),
        ("18_EP01_ALTMAN_BROLL_STUDIES", os.path.join(raw_dir, "flow_images", "EP01_Altman", "02_broll_stills_and_studies")),
        ("19_EP03_HASSABIS_CHESS_GO_HERO", os.path.join(raw_dir, "flow_images", "EP03_Hassabis", "01_primary_keyframes")),
        ("20_EP03_HASSABIS_BROLL_STUDIES", os.path.join(raw_dir, "flow_images", "EP03_Hassabis", "02_broll_stills_and_studies")),
        ("21_EP06_SUTSKEVER_KEYFRAMES", os.path.join(raw_dir, "flow_images", "EP06_Sutskever", "01_primary_keyframes")),
        ("22_EP06_SUTSKEVER_BROLL_STUDIES", os.path.join(raw_dir, "flow_images", "EP06_Sutskever", "02_broll_stills_and_studies")),
        ("23_EP10_NG_KEYFRAMES", os.path.join(raw_dir, "flow_images", "EP10_Ng", "01_primary_keyframes")),
        ("24_EP10_NG_BROLL_STUDIES", os.path.join(raw_dir, "flow_images", "EP10_Ng", "02_broll_stills_and_studies")),

        # 4. Videos & Renders
        ("13_ALL_10_TITANS_FLOW_RENDERS", os.path.join(raw_dir, "flow_renders")),
        ("03_FLOW_VIDEO_V1", os.path.join(raw_dir, "flow_renders", "v1_gapless_master")),
        ("25_EP01_ALTMAN_FLOW_VIDEOS", os.path.join(raw_dir, "flow_videos", "EP01_Altman")),
        ("26_ALL_TITANS_PREVIS_ANIMATICS", os.path.join(raw_dir, "flow_previs_animatics")),

        # 5. Typographic Dossiers & Thought Cards
        ("16_ALL_10_TITANS_PRESS_DOSSIERS", os.path.join(raw_dir, "dossiers_press")),

        # 6. Audio Stems for All 10 Heroes
        ("10_ALL_10_TITANS_MUSIC_STEMS", os.path.join(audio_dir, "suno_stems", "00_MASTER_POOL_ORIGINAL")),
        ("28_EP01_ALTMAN_MUSIC", os.path.join(audio_dir, "suno_stems", "EP01_ALTMAN_SMART_BINS")),
        ("29_EP02_HUANG_MUSIC", os.path.join(audio_dir, "suno_stems", "EP02_HUANG_SMART_BINS")),
        ("30_EP03_HASSABIS_MUSIC", os.path.join(audio_dir, "suno_stems", "EP03_HASSABIS_SMART_BINS")),
        ("31_EP04_HINTON_MUSIC", os.path.join(audio_dir, "suno_stems", "EP04_HINTON_SMART_BINS")),
        ("32_EP05_LECUN_MUSIC", os.path.join(audio_dir, "suno_stems", "EP05_LECUN_SMART_BINS")),
        ("33_EP06_SUTSKEVER_MUSIC", os.path.join(audio_dir, "suno_stems", "EP06_SUTSKEVER_SMART_BINS")),
        ("34_EP07_AMODEI_MUSIC", os.path.join(audio_dir, "suno_stems", "EP07_AMODEI_SMART_BINS")),
        ("35_EP08_FEIFEI_LI_MUSIC", os.path.join(audio_dir, "suno_stems", "EP08_LI_SMART_BINS")),
        ("36_EP09_BENGIO_MUSIC", os.path.join(audio_dir, "suno_stems", "EP09_BENGIO_SMART_BINS")),
        ("37_EP10_ANDREW_NG_MUSIC", os.path.join(audio_dir, "suno_stems", "EP10_NG_SMART_BINS")),

        # 7. Voiceover & Foley SFX
        ("01_VOICEOVER_A1", os.path.join(audio_dir, "voiceover", "EP01_ALTMAN")),
        ("27_SFX_FOLEY_LIBRARY", os.path.join(audio_dir, "sfx")),
    ]

    total_bins_processed = 0
    total_clips_imported = 0
    exts = ('.mp4', '.mov', '.jpg', '.jpeg', '.png', '.webp', '.wav', '.mp3', '.m4a')

    for bin_name, folder_path in targets:
        if not os.path.exists(folder_path):
            continue
        bin_folder = get_or_create_subfolder(root, bin_name)
        mp.SetCurrentFolder(bin_folder)

        # Existing clips in this bin
        existing_names = set(c.GetName() for c in bin_folder.GetClipList())

        files_to_import = []
        for f in sorted(os.listdir(folder_path)):
            if f.startswith('.'):
                continue
            if any(f.lower().endswith(e) for e in exts):
                if f not in existing_names:
                    files_to_import.append(os.path.join(folder_path, f))

        count = 0
        if files_to_import:
            items = mp.ImportMedia(files_to_import)
            count = len(items) if items else 0
            total_clips_imported += count

        total_bins_processed += 1
        print(f"✓ Bin '{bin_name:45}': {len(existing_names)} existing, {count} new imported")

    pm.SaveProject()
    print("\n" + "="*70)
    print(f"🏆 COMPLETE MASTER INGESTION ACROSS ALL 10 TITANS FINISHED")
    print(f"Bins Processed : {total_bins_processed}")
    print(f"New Imported   : {total_clips_imported} media files")
    print("="*70)

if __name__ == "__main__":
    ingest_master()
    os._exit(0)
