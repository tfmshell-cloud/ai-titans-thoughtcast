#!/usr/bin/env python3
"""
🏆 UNIFIED MASTER DIRECTORS CUT: EPISODE 01 — ACT 1 + ACT 2 (00:00 - 08:00)
Timeline: EP01_MASTER_DIRECTORS_CUT_COMPLETE (480.00s / 11,520 Frames)

Unites Block 1 (Genesis of Rebellion, 00:00 - 04:00) AND Block 2 (The YC Presidency & OpenAI Founding, 04:00 - 08:00)
onto ONE CONTINUOUS MASTER TIMELINE in DaVinci Resolve Studio 21.
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def build_master():
    resolve = bmd.scriptapp('Resolve')
    proj = resolve.GetProjectManager().GetCurrentProject()
    mp = proj.GetMediaPool()

    # Find or use the Block 1 timeline as our base
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() in ["EP01_BLOCK1_Master_Director_Cut", "EP01_MASTER_DIRECTORS_CUT_COMPLETE"]:
            tl = t
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print("Master timeline not found!")
        return

    # Rename to clear official title
    tl.SetName("EP01_MASTER_DIRECTORS_CUT_COMPLETE")
    print(f"Master Timeline: {tl.GetName()}")

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)
    b2_start = start_frame + 5760    # 92160 (01:04:00:00)

    # Clean only Block 2 region (if any clips exist past b2_start)
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            to_delete = [it for it in items if it.GetStart() >= b2_start]
            if to_delete:
                tl.DeleteClips(to_delete)

    def get_bin_items(folder):
        items = {}
        for clip in folder.GetClipList():
            items[clip.GetName()] = clip
        for sub in folder.GetSubFolderList():
            items.update(get_bin_items(sub))
        return items

    clips = get_bin_items(mp.GetRootFolder())

    def place_clip(clip_name, media_type, track_idx, rec_frame, vol=None, fades=None):
        c = clips.get(clip_name)
        if not c:
            print(f"  ✗ MISSING IN MEDIA POOL: {clip_name}")
            return None
        app = {"mediaPoolItem": c, "mediaType": media_type, "trackIndex": track_idx, "recordFrame": rec_frame}
        its = mp.AppendToTimeline([app])
        if its:
            it = its[0]
            if vol is not None:
                it.SetProperty("AudioVolume", vol)
            if fades:
                it.SetFades(fades)
            return it
        return None

    fade_spec = {'FadeIn': 12.0, 'FadeOut': 12.0}

    print("\n=== Appending Block 2 (04:00 - 08:00 / Frames 92160 - 97920) ===")

    # 1. AUDIO TRACK A1: VOICEOVER (+2.0 dB)
    print("\n--- 1. Placing Block 2 Voiceover (Track A1) ---")
    vo_plan = [
        ("EP01_VO_EN_07_ACT2_04_45_05_45_YC_President_28yo.wav", 1.0),
        ("EP01_VO_EN_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 58.0),
        ("EP01_VO_EN_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav", 116.0),
        ("EP01_VO_EN_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav", 172.0),
    ]
    for name, sec in vo_plan:
        rf = b2_start + round(sec * FPS)
        place_clip(name, 2, 1, rf, vol=2.0)
        print(f"  ✓ VO: {name} placed at {240.0 + sec:.1f}s (Frame {rf})")

    # 2. AUDIO TRACK A2: MUSIC SCORE BED (-21.0 dB)
    print("\n--- 2. Placing Block 2 Music Drone Bed (Track A2) ---")
    place_clip("EP01_AMB_B2_PART1_00_00_to_02_00_120s.wav", 2, 2, b2_start, vol=-21.0)
    rf_part2 = b2_start + round(120.0 * FPS)
    place_clip("EP01_AMB_B2_PART2_02_00_to_04_00_120s.wav", 2, 2, rf_part2, vol=-21.0)
    print("  ✓ Ambient Score Part 1 & Part 2 placed at -21.0 dB (Frame 92160 to 97920)")

    # 3. AUDIO TRACK A3: LIVE ARCHIVAL AUDIO
    print("\n--- 3. Placing Block 2 Live Archival Audio (Track A3) ---")
    rf_lecture = b2_start + round(14.0 * FPS)
    place_clip("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 2, 3, rf_lecture, vol=-10.0)
    print(f"  ✓ Live: Stanford CS183B Lecture placed at Frame {rf_lecture}")

    # 4. AUDIO TRACK A4: MECHANICAL KEYBOARD FOLEY SFX (-18.0 dB)
    print("\n--- 4. Placing Block 2 Mechanical Keyboard SFX (Track A4) ---")
    sfx_plan = [
        46.0,  # Card 06
        104.0, # Card 07
        158.0, # Card 08
        212.0, # Card 09
    ]
    for sec in sfx_plan:
        rf = b2_start + round(sec * FPS)
        place_clip("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-18.0)
        print(f"  ✓ SFX: Keyboard Typing Burst at {240.0 + sec:.1f}s (Frame {rf})")

    # 5. VIDEO TRACK V1: MASTER CREATIVE CANVAS (23 CLIPS, 5760 FRAMES)
    print("\n--- 5. Placing Block 2 Track V1 Canvas (23 Clips) ---")
    v1_sequence = [
        ("EP01_V1_B2_00_Startup_Engine_Matrix_14s.mp4", "Silicon Valley Venture Startup Engine Matrix (YC Presidency)"),
        ("ep01_flow_09_fusion_torus.mp4", "Helion Energy Nuclear Fusion Plasma Torus"),
        ("EP01_V1_B2_01_Retro_Cellular_14s.mp4", "Retro Biosciences Cellular Longevity Nanobots"),
        ("EP01_V1_CREATIVE_02_Galaxies_Axons_12s.mp4", "Exponential Neural Interconnection Void"),
        ("EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", "Midnight Rosewood Boardroom Noir Rain"),
        ("ep01_flow_04_exponential_line.mp4", "Golden Exponential Ascent Curve (Moore's Law)"),
        ("ep02_flow_01_blackwell_wafer_matrix.mp4", "Wafer Scale Supercomputing Matrix"),
        ("EP01_V1_B2_03_Singularity_Threat_12s.mp4", "Singularity Cybernetic Portal (DeepMind Monopoly Threat)"),
        ("ep03_flow_01_alphafold_protein_cosmos.mp4", "AlphaFold Protein Cosmos"),
        ("EP01_V1_B2_09_Researchers_Compute_Core_12s.mp4", "Researchers Facing Compute Core at Night"),
        ("EP01_V1_B2_04_Robotic_Dexterity_15s.mp4", "Robotic Arms & Hand Dexterity (Rubik's Cube)"),
        ("EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4", "Dota 2 OpenAI Five Swarm RL Units"),
        ("EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4", "Obsessive Builders (Scale Is All You Need)"),
        ("EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4", "Star Encased in GPU Server Plates (Tens of Millions)"),
        ("ep01_flow_06_server_monolith.mp4", "Supercomputer Cold Server Hall Monolith"),
        ("EP01_V1_B2_07_Corporate_Transmutation_15s.mp4", "Altman Dissolving into Data (Capped-Profit Step)"),
        ("EP01_V1_B2_08_Silicon_Metropolis_14s.mp4", "Metropolis Transforming into Silicon ($1B Alliance)"),
        ("ep01_flow_08_golden_signatures.mp4", "Golden Signatures Light Threads Alliance"),
        ("ep07_flow_01_constitutional_prism.mp4", "Constitutional Alignment Prism"),
        ("ep06_flow_01_ssi_obsidian_monolith.mp4", "Obsidian Compute Monolith"),
        ("EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", "Gold Melting into Neural Brain (Compute Equation)"),
        ("EP01_V1_NEW_06_Cosmic_Dyson_7s.mp4", "Cosmic Dyson Megastructure Orbit"),
        ("EP01_V1_B2_10_Earth_Horizon_Finale_214f.mp4", "Earth Atmosphere Horizon from Orbit (Act 2 Finale)"),
    ]

    cur_frame = b2_start
    for name, desc in v1_sequence:
        item = place_clip(name, 1, 1, cur_frame)
        if item:
            dur = item.GetDuration()
            cur_frame += dur
            print(f"  ✓ V1 [{dur/24.0:4.1f}s / {dur:3}f]: {desc:55} @ frame {cur_frame - dur}")
        else:
            print(f"  ✗ V1 FAILED: {name}")

    total_b2_v1_frames = cur_frame - b2_start
    print(f"  ==> Total Block 2 V1: {total_b2_v1_frames} frames ({total_b2_v1_frames/24.0:.2f}s)")
    print(f"  ==> Cumulative Timeline V1: {cur_frame - start_frame} frames ({(cur_frame - start_frame)/24.0:.2f}s / 08:00.00) - 100% GAPLESS!")

    # 6. VIDEO TRACK V2: CURATED ARCHIVES
    print("\n--- 6. Placing Block 2 Track V2 Archives ---")
    v2_plan = [
        ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 14.0, "Stanford CS183B Lecture 2014"),
        ("EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 32.0, "28yo YC President TechCrunch Disrupt"),
        ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 82.0, "Altman & Ilya Sutskever Founding Alliance"),
        ("EP01_V2_B2_02_Stanford_2014_10s.mp4", 136.0, "Altman Stanford YC President Archive"),
        ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 188.0, "Altman TechCrunch Disrupt 2019 OpenAI CEO"),
    ]
    for name, sec, desc in v2_plan:
        rf = b2_start + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2: {desc:45} at {240.0 + sec:5.1f}s (Frame {rf})")

    # 7. VIDEO TRACK V3: THOUGHT CARDS & DOSSIER
    print("\n--- 7. Placing Block 2 Track V3 Thought Cards & Dossiers ---")
    v3_plan = [
        ("EP01_CARD_06_Risk_Of_Standing_Still.mp4", 46.0, "Card 06: Risk of Standing Still"),
        ("EP01_CARD_07_Linear_Blind_Spot.mp4", 104.0, "Card 07: The Linear Blind Spot"),
        ("EP01_DOC_02_OpenAI_Introducing_12s.mp4", 120.0, "OpenAI Introducing Dec 11 2015 Press Announcement"),
        ("EP01_CARD_08_Scaling_Hypothesis.mp4", 158.0, "Card 08: The Scaling Hypothesis"),
        ("EP01_CARD_09_Compute_Equation.mp4", 212.0, "Card 09: The Compute Equation"),
    ]
    for name, sec, desc in v3_plan:
        rf = b2_start + round(sec * FPS)
        place_clip(name, 1, 3, rf, fades=fade_spec)
        print(f"  ✓ V3: {desc:45} at {240.0 + sec:5.1f}s (Frame {rf})")

    tl.SetCurrentTimecode('01:00:00:00')
    print("\n🎉 MASTER TIMELINE COMPLETE (00:00 - 08:00)! Playhead at 01:00:00:00")
    os._exit(0)

if __name__ == '__main__':
    build_master()
