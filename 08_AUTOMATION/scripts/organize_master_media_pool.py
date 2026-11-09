#!/usr/bin/env python3
"""
AI TITANS THOUGHTCAST — DAVINCI RESOLVE MEDIA POOL RESTRUCTURING
Transforms 41 flat chaotic folders into a clean 5-pillar Hollywood studio hierarchy:
  00_TIMELINES
  01_AUDIO_VAULT
  02_EP01_ALTMAN_MEDIA
  03_FUTURE_EPISODES
  04_GLOBAL_SERIES_LIBRARY
"""

import sys, os, glob
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

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

    print("==================================================================")
    print("🎬 RESTRUCTURING DAVINCI RESOLVE MEDIA POOL TO 5-PILLAR STUDIO HIERARCHY")
    print("==================================================================")

    # 1. Existing subfolders in Master
    existing_folders = {sf.GetName(): sf for sf in root.GetSubFolderList()}
    print(f"  • Current root folders: {len(existing_folders)}")

    # Helper: get or create subfolder
    def get_or_create(parent, name):
        for sf in parent.GetSubFolderList():
            if sf.GetName() == name:
                return sf
        return mp.AddSubFolder(parent, name)

    # 2. Create the 5 Master Pillars
    p_timelines = get_or_create(root, "00_TIMELINES")
    p_audio     = get_or_create(root, "01_AUDIO_VAULT")
    p_altman    = get_or_create(root, "02_EP01_ALTMAN_MEDIA")
    p_future    = get_or_create(root, "03_FUTURE_EPISODES")
    p_global    = get_or_create(root, "04_GLOBAL_SERIES_LIBRARY")

    # 3. Create sub-bins inside pillars
    # Audio Vault
    bin_vo_ua      = get_or_create(p_audio, "01_VOICEOVER_UA_MASTER")
    bin_vo_en      = get_or_create(p_audio, "02_VOICEOVER_EN_ARCHIVE")
    bin_music_ep01 = get_or_create(p_audio, "03_EP01_ALTMAN_SCORE")
    bin_sfx_speech = get_or_create(p_audio, "04_SFX_AND_ARCHIVAL_SPEECH")
    bin_music_all  = get_or_create(p_audio, "05_ALL_TITANS_MUSIC_STEMS")

    # EP01 Altman Media
    bin_user_ai    = get_or_create(p_altman, "01_USER_AI_GENERATIONS")
    bin_archives   = get_or_create(p_altman, "02_HISTORICAL_ARCHIVES")
    bin_flow_vid   = get_or_create(p_altman, "03_FLOW_CINEMATIC_VIDEOS")
    bin_dossiers   = get_or_create(p_altman, "04_DOSSIERS_AND_TITLES")
    bin_stills     = get_or_create(p_altman, "05_KEYFRAMES_AND_STILLS")

    # Future Episodes
    bin_ep02_huang     = get_or_create(p_future, "EP02_HUANG_ASSETS")
    bin_ep03_hassabis  = get_or_create(p_future, "EP03_HASSABIS_CHESS")
    bin_ep06_sutskever = get_or_create(p_future, "EP06_SUTSKEVER_ASSETS")
    bin_ep10_ng        = get_or_create(p_future, "EP10_ANDREW_NG_ASSETS")

    # Global Series Library
    bin_portraits  = get_or_create(p_global, "01_TITANS_PORTRAITS")
    bin_g_archives = get_or_create(p_global, "02_TITANS_ARCHIVE_VAULT")
    bin_scivfx     = get_or_create(p_global, "03_SCIENTIFIC_VFX_ANIMATIONS")
    bin_concept    = get_or_create(p_global, "04_FLOW_CONCEPT_STUDIES")
    bin_previs     = get_or_create(p_global, "05_PREVIS_ANIMATICS")

    # Mapping of old folder name pattern -> destination sub-bin
    folder_mapping = {
        # Audio
        "01_VOICEOVER_UA": bin_vo_ua,
        "01_VOICEOVER_A1": bin_vo_en,
        "02_MUSIC_A2": bin_music_ep01,
        "28_EP01_ALTMAN_MUSIC": bin_music_ep01,
        "27_SFX_FOLEY_LIBRARY": bin_sfx_speech,
        "10_ALL_10_TITANS_MUSIC_STEMS": bin_music_all,
        "29_EP02_HUANG_MUSIC": bin_music_all,
        "30_EP03_HASSABIS_MUSIC": bin_music_all,
        "31_EP04_HINTON_MUSIC": bin_music_all,
        "32_EP05_LECUN_MUSIC": bin_music_all,
        "33_EP06_SUTSKEVER_MUSIC": bin_music_all,
        "34_EP07_AMODEI_MUSIC": bin_music_all,
        "35_EP08_FEIFEI_LI_MUSIC": bin_music_all,
        "36_EP09_BENGIO_MUSIC": bin_music_all,
        "37_EP10_ANDREW_NG_MUSIC": bin_music_all,

        # Timelines
        "06_TIMELINES": p_timelines,

        # EP01 Altman
        "05_USER_AI_GENERATIONS": bin_user_ai,
        "04_ARCHIVES_BROLL_V2": bin_archives,
        "15_EP01_V2_MASTER_CLIPS": bin_archives,
        "03_FLOW_VIDEO_V1": bin_flow_vid,
        "13_ALL_10_TITANS_FLOW_RENDERS": bin_flow_vid,
        "25_EP01_ALTMAN_FLOW_VIDEOS": bin_flow_vid,
        "05_DOSSIERS_VFX_V3": bin_dossiers,
        "16_ALL_10_TITANS_PRESS_DOSSIERS": bin_dossiers,
        "14_EP01_ALTMAN_ARCHIVE_PHOTOS": bin_stills,
        "17_EP01_ALTMAN_KEYFRAMES": bin_stills,
        "18_EP01_ALTMAN_BROLL_STUDIES": bin_stills,

        # Future episodes
        "19_EP03_HASSABIS_CHESS_GO_HERO": bin_ep03_hassabis,
        "20_EP03_HASSABIS_BROLL_STUDIES": bin_ep03_hassabis,
        "21_EP06_SUTSKEVER_KEYFRAMES": bin_ep06_sutskever,
        "22_EP06_SUTSKEVER_BROLL_STUDIES": bin_ep06_sutskever,
        "23_EP10_NG_KEYFRAMES": bin_ep10_ng,
        "24_EP10_NG_BROLL_STUDIES": bin_ep10_ng,

        # Global Series Library
        "07_ALL_10_TITANS_PORTRAITS": bin_portraits,
        "08_ALL_10_TITANS_ARCHIVES": bin_g_archives,
        "09_ALL_10_TITANS_SCIENTIFIC_VFX": bin_scivfx,
        "11_ALL_10_TITANS_FLOW_BATCH3_GAMING": bin_concept,
        "12_ALL_10_TITANS_FLOW_BATCH4_COSMIC": bin_concept,
        "11_ALL_10_TITANS_FLOW_BATCH3_GAMING_CHESS_GO": bin_concept,
        "12_ALL_10_TITANS_FLOW_BATCH4_COSMIC_HARDWARE": bin_concept,
        "26_ALL_TITANS_PREVIS_ANIMATICS": bin_previs,
    }

    print("\n--- 4. Moving clips to target bins & removing legacy folders ---")
    folders_to_delete = []

    # Refresh current root list
    current_folders = root.GetSubFolderList()
    protected_names = {"00_TIMELINES", "01_AUDIO_VAULT", "02_EP01_ALTMAN_MEDIA", "03_FUTURE_EPISODES", "04_GLOBAL_SERIES_LIBRARY"}

    for sf in current_folders:
        s_name = sf.GetName()
        if s_name in protected_names:
            continue

        target_bin = folder_mapping.get(s_name)
        if not target_bin:
            # Fallback based on name keywords
            if "VOICEOVER" in s_name or "AUDIO" in s_name or "MUSIC" in s_name:
                target_bin = p_audio
            elif "TIMELINE" in s_name:
                target_bin = p_timelines
            elif "HASSABIS" in s_name or "HUANG" in s_name or "SUTSKEVER" in s_name:
                target_bin = p_future
            elif "FLOW" in s_name or "ALTMAN" in s_name:
                target_bin = p_altman
            else:
                target_bin = p_global

        clips = sf.GetClipList() or []
        if clips:
            ok_move = mp.MoveClips(clips, target_bin)
            print(f"  ✓ Moved {len(clips)} clips from '{s_name}' -> '{target_bin.GetName()}' (Status: {ok_move})")

        # Also check if it has subfolders
        child_subf = sf.GetSubFolderList() or []
        for csf in child_subf:
            c_clips = csf.GetClipList() or []
            if c_clips:
                mp.MoveClips(c_clips, target_bin)
            folders_to_delete.append(csf)

        folders_to_delete.append(sf)

    # Delete all migrated old folders
    if folders_to_delete:
        ok_del = mp.DeleteFolders(folders_to_delete)
        print(f"  ✓ Deleted {len(folders_to_delete)} legacy empty folders (Status: {ok_del})")

    # 5. Move any remaining loose clips in Master to 02_EP01_ALTMAN_MEDIA / 03_FLOW_CINEMATIC_VIDEOS
    master_clips = root.GetClipList() or []
    if master_clips:
        mp.MoveClips(master_clips, bin_flow_vid)
        print(f"  ✓ Moved {len(master_clips)} loose root clips to '{bin_flow_vid.GetName()}'")

    # 6. Import newly downloaded Hassabis EP02 files
    ep02_dir = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE/ep02_demis_hassabis"
    if os.path.exists(ep02_dir):
        new_files = [os.path.join(ep02_dir, f) for f in os.listdir(ep02_dir) if not f.startswith('.')]
        if new_files:
            mp.SetCurrentFolder(bin_ep03_hassabis)
            imported = mp.ImportMedia(new_files)
            print(f"  ✓ Imported {len(imported) if imported else 0} new EP02/EP03 Hassabis assets into '{bin_ep03_hassabis.GetName()}'")

    # 7. Print final clean hierarchy
    print("\n==================================================================")
    print("🏆 FINAL MEDIA POOL HIERARCHY IN MASTER ROOT:")
    print("==================================================================")
    def print_tree(f, depth=0):
        ind = "  " * depth
        clips_count = len(f.GetClipList() or [])
        subf = f.GetSubFolderList() or []
        print(f"{ind}📁 {f.GetName()} [{clips_count} clips]")
        for sf in subf:
            print_tree(sf, depth + 1)

    print_tree(root)

    pm.SaveProject()
    print("\n✓ Media Pool Cleaned & Project Saved Successfully.")

if __name__ == '__main__':
    run()
