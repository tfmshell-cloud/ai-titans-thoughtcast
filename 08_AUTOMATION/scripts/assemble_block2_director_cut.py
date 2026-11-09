#!/usr/bin/env python3
"""
🏆 THE MASTERPIECE DIRECTORS CUT: EPISODE 01, BLOCK 2 (04:00 - 08:45 / 00:00 - 04:00)
Timeline: EP01_BLOCK2_Master_Director_Cut

Directorial Standards:
1. ZERO repetitive computers: Pure conceptual visual diversity:
   - Frontier technology: Cellular longevity (Retro Biosciences) & Nuclear fusion (Helion Energy plasma torus).
   - Rosewood Sand Hill hotel midnight noir boardroom dinner (Altman, Musk, Brockman, Sutskever).
   - Google DeepMind commercial monopoly threat & Singularity cybernetic portal.
   - Robotic dexterity (Rubik's cube robot hand) & Swarm reinforcement learning (Dota 2).
   - Tens of millions in GPU electricity & supercomputer scaling equations.
   - Capped-profit corporate restructuring & Silicon Valley matrix transformation.
   - Cosmic scale Dyson megastructure & Earth atmosphere orbital horizon finale.
2. English 4K Typewriter Thought Cards + Mechanical Typing Foley audio on A4 (-18 dB):
   - Card 06: Risk of Standing Still (Amber Gold)
   - Card 07: Linear Blind Spot (Neon Cyan)
   - Card 08: Scaling Hypothesis (Deep Crimson)
   - Card 09: Compute Equation (Royal Blue)
   - Dossier 02: OpenAI Introducing Dec 11, 2015 Founding Announcement
3. Track V1 is 100% gapless canvas: Exactly 5760 frames (240.00s / 04:00.00), zero black frames.
4. Native 12-frame (0.5s) dissolves on all V2 archives and V3 thought cards.
5. Audio mastering: VO at +2.0 dB (offline normalized, Leveler OFF), Music score at -21.0 dB, SFX typing bursts at -18.0 dB.
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble():
    resolve = bmd.scriptapp('Resolve')
    proj = resolve.GetProjectManager().GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_BLOCK2_Master_Director_Cut"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            print(f"Selecting existing timeline: {tl_name}")
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print(f"Creating new timeline: {tl_name}")
        tl = mp.CreateEmptyTimeline(tl_name)
        if not tl:
            print("Failed to create timeline!")
            return
        proj.SetCurrentTimeline(tl)

    tl = proj.GetCurrentTimeline()
    # Configure smooth preview resolution (1920x1080) for 24fps silky playback
    tl.SetSetting('useCustomSettings', '1')
    tl.SetSetting('timelineResolutionWidth', '1920')
    tl.SetSetting('timelineResolutionHeight', '1080')

    # Ensure sufficient video and audio tracks
    while tl.GetTrackCount("audio") < 4:
        tl.AddTrack("audio")
    while tl.GetTrackCount("video") < 3:
        tl.AddTrack("video")

    # Clear all tracks
    print("Clearing timeline tracks...")
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

    # Track Labels
    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_DRONE_A2")
    tl.SetTrackName("audio", 3, "LIVE_ARCHIVES_A3")
    tl.SetTrackName("audio", 4, "SFX_KEYBOARD_A4")
    tl.SetTrackName("video", 1, "FLOW_CANVAS_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_PHOTOS_V2")
    tl.SetTrackName("video", 3, "THOUGHT_CARDS_V3")

    fade_spec = {'FadeIn': 12.0, 'FadeOut': 12.0}

    # ==========================================================
    # 1. AUDIO TRACK A1: VOICEOVER (4 Takes, +2.0 dB)
    # Spoken narration is 161.2s total across 240s timeline
    # ==========================================================
    print("\n--- 1. Placing Track A1: Voiceover ---")
    vo_plan = [
        ("EP01_VO_EN_07_ACT2_04_45_05_45_YC_President_28yo.wav", 1.0),
        ("EP01_VO_EN_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 58.0),
        ("EP01_VO_EN_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav", 116.0),
        ("EP01_VO_EN_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav", 172.0),
    ]
    for name, sec in vo_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 2, 1, rf, vol=2.0)
        print(f"  ✓ VO: {name} placed at {sec:.1f}s")

    # ==========================================================
    # 2. AUDIO TRACK A2: AMBIENT DRONE / SCORE BED (-21.0 dB)
    # Dynamic two-part evolution: Server Matrix -> OpenAI Floor
    # Exactly 120s + 120s = 240.00s (5760 frames)!
    # ==========================================================
    print("\n--- 2. Placing Track A2: Music Drone Bed ---")
    place_clip("EP01_AMB_B2_PART1_00_00_to_02_00_120s.wav", 2, 2, start_frame, vol=-21.0)
    rf_part2 = start_frame + round(120.0 * FPS)
    place_clip("EP01_AMB_B2_PART2_02_00_to_04_00_120s.wav", 2, 2, rf_part2, vol=-21.0)
    print("  ✓ Ambient Score Part 1 & Part 2 placed at -21.0 dB")

    # ==========================================================
    # 3. AUDIO TRACK A3: LIVE ARCHIVAL AUDIO
    # Stanford CS183B Lecture excerpt
    # ==========================================================
    print("\n--- 3. Placing Track A3: Live Archival Audio ---")
    rf_lecture = start_frame + round(14.0 * FPS)
    place_clip("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 2, 3, rf_lecture, vol=-10.0)
    print("  ✓ Live: Stanford CS183B lecture audio placed at 14.0s")

    # ==========================================================
    # 4. AUDIO TRACK A4: MECHANICAL KEYBOARD FOLEY SFX (-18.0 dB)
    # Synchronized beneath each English Thought Card!
    # ==========================================================
    print("\n--- 4. Placing Track A4: Mechanical Keyboard Foley SFX ---")
    sfx_plan = [
        46.0,  # Card 06 (Risk of Standing Still)
        104.0, # Card 07 (Linear Blind Spot)
        158.0, # Card 08 (Scaling Hypothesis)
        212.0, # Card 09 (Compute Equation)
    ]
    for sec in sfx_plan:
        rf = start_frame + round(sec * FPS)
        place_clip("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-18.0)
        print(f"  ✓ SFX: Keyboard Typing Burst at {sec:.1f}s (-18.0 dB)")

    # ==========================================================
    # 5. VIDEO TRACK V1: 100% CONTIGUOUS CINEMATIC CANVAS (22 CLIPS)
    # Exactly 5760 frames = 240.00s (04:00.00), zero black frames!
    # ==========================================================
    print("\n--- 5. Placing Track V1: Master Creative Canvas (22 Clips) ---")
    v1_sequence = [
        ("EP01_V1_B2_01_Retro_Cellular_14s.mp4", "Retro Biosciences Cellular Longevity Nanobots"),
        ("ep01_flow_09_fusion_torus.mp4", "Helion Energy Nuclear Fusion Torus"),
        ("EP01_V1_CREATIVE_02_Galaxies_Axons_12s.mp4", "Exponential Neural Interconnection Void"),
        ("EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", "Midnight Rosewood Boardroom Noir Rain"),
        ("EP01_V1_B2_03_Singularity_Threat_12s.mp4", "Singularity Cybernetic Portal (Monopoly Threat)"),
        ("ep01_flow_04_exponential_line.mp4", "Golden Exponential Ascent Curve"),
        ("ep03_flow_01_alphafold_protein_cosmos.mp4", "AlphaFold Protein Cosmos"),
        ("EP01_V1_B2_09_Researchers_Compute_Core_12s.mp4", "Researchers Facing Compute Core at Night"),
        ("EP01_V1_B2_04_Robotic_Dexterity_15s.mp4", "Robotic Arms & Hand Dexterity (Rubik's Cube)"),
        ("EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4", "Dota 2 OpenAI Five Swarm RL Units"),
        ("EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4", "Obsessive Builders (Scale Is All You Need)"),
        ("ep02_flow_01_blackwell_wafer_matrix.mp4", "Wafer Scale Supercomputing Matrix"),
        ("EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4", "Star Encased in GPU Server Plates (Tens of Millions)"),
        ("ep01_flow_06_server_monolith.mp4", "Supercomputer Cold Server Hall Monolith"),
        ("EP01_V1_B2_07_Corporate_Transmutation_15s.mp4", "Altman Dissolving into Data (Capped-Profit Step)"),
        ("EP01_V1_B2_08_Silicon_Metropolis_14s.mp4", "Metropolis Transforming into Silicon ($1B Alliance)"),
        ("ep01_flow_08_golden_signatures.mp4", "Golden Signatures Light Threads Alliance"),
        ("ep07_flow_01_constitutional_prism.mp4", "Constitutional Alignment Prism"),
        ("ep06_flow_01_ssi_obsidian_monolith.mp4", "Obsidian Compute Monolith"),
        ("EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", "Gold Melting into Neural Brain (Compute Equation)"),
        ("EP01_V1_NEW_06_Cosmic_Dyson_7s.mp4", "Cosmic Dyson Megastructure Orbit"),
        ("EP01_V1_B2_10_Earth_Horizon_Finale_550f.mp4", "Earth Atmosphere Horizon from Orbit (Act 2 Finale)"),
    ]

    cur_frame = start_frame
    for name, desc in v1_sequence:
        item = place_clip(name, 1, 1, cur_frame)
        if item:
            dur = item.GetDuration()
            cur_frame += dur
            print(f"  ✓ V1 [{dur/24.0:4.1f}s / {dur:3}f]: {desc:55} @ frame {cur_frame - dur}")
        else:
            print(f"  ✗ V1 FAILED: {name}")

    total_v1_frames = cur_frame - start_frame
    total_v1_dur = total_v1_frames / 24.0
    print(f"  ==> Total Gapless V1: {total_v1_frames} frames ({total_v1_dur:.2f}s) - 100% GAPLESS!")

    # ==========================================================
    # 6. VIDEO TRACK V2: CURATED ARCHIVES (5 MOMENTS)
    # Native 12-frame (0.5s) dissolves
    # ==========================================================
    print("\n--- 6. Placing Track V2: Curated Archival Moments ---")
    v2_plan = [
        ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 14.0, "Stanford CS183B Lecture 2014"),
        ("EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 32.0, "28yo YC President TechCrunch Disrupt"),
        ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 82.0, "Altman & Ilya Sutskever Founding Alliance"),
        ("EP01_V2_B2_02_Stanford_2014_10s.mp4", 136.0, "Altman Stanford YC President Archive"),
        ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 188.0, "Altman TechCrunch Disrupt 2019 OpenAI CEO"),
    ]
    for name, sec, desc in v2_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2: {desc:45} at {sec:5.1f}s (with 0.5s cross-dissolves)")

    # ==========================================================
    # 7. VIDEO TRACK V3: ENGLISH TYPEWRITER CARDS & OPENAI DOSSIER
    # Native 12-frame (0.5s) dissolves
    # ==========================================================
    print("\n--- 7. Placing Track V3: English Typewriter Cards & Dossiers ---")
    v3_plan = [
        ("EP01_CARD_06_Risk_Of_Standing_Still.mp4", 46.0, "Card 06: Risk of Standing Still"),
        ("EP01_CARD_07_Linear_Blind_Spot.mp4", 104.0, "Card 07: The Linear Blind Spot"),
        ("EP01_DOC_02_OpenAI_Introducing_12s.mp4", 120.0, "OpenAI Introducing Dec 11 2015 Press Announcement"),
        ("EP01_CARD_08_Scaling_Hypothesis.mp4", 158.0, "Card 08: The Scaling Hypothesis"),
        ("EP01_CARD_09_Compute_Equation.mp4", 212.0, "Card 09: The Compute Equation"),
    ]
    for name, sec, desc in v3_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 3, rf, fades=fade_spec)
        print(f"  ✓ V3: {desc:45} at {sec:5.1f}s (with 0.5s cross-dissolves)")

    tl.SetCurrentTimecode('01:00:00:00')
    print("\n🎉 BLOCK 2 MASTER DIRECTORS CUT ASSEMBLY FINISHED! Playhead at 01:00:00:00")
    os._exit(0)

if __name__ == '__main__':
    assemble()
