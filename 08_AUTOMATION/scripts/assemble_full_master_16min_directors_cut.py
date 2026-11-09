#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE COMPLETE 16-MINUTE MASTER DIRECTOR'S CUT (ACTS 1 + 2 + 3 + 4)
Timeline: EP01_MASTER_DIRECTORS_CUT_COMPLETE
Total Duration: EXACTLY 23,040 Frames (960.00s / 16:00.00) @ 24.0 fps

Key Directorial Upgrades Implemented:
1. 100% UKRAINIAN VOICEOVER (Broadcast Level +2.0 dB) across all 17 takes.
2. ZERO DUPLICATE CLIPS: Every video clip on Track V1, V2, V3 appears EXACTLY ONCE.
3. ZERO MULTI-LAYER CONFLICTS: V2 (archives) and V3 (thought cards) are completely staggered.
   Never active at the same time. Never 3 stacked video layers.
4. 100% GAPLESS TRACK V1: Exactly 5760 frames in Block 1, 5760 in Block 2, 5760 in Block 3, 5760 in Block 4.
5. COMPLETE AUDIO ECOSYSTEM:
   - A1: Ukrainian Voiceover (+2.0 dB)
   - A2: 4-Act Continuous Drone & Pulse Score (-21.0 dB)
   - A3: Historical Live Speeches (Jobs WWDC 2008, Stanford CS183B, Senate AI Hearing)
   - A4: Mechanical Typewriter Keyboard SFX (-18.0 dB) synchronized with all 16 Thought Cards.
"""

import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble_master_16min():
    resolve = bmd.scriptapp('Resolve')
    if not resolve:
        print("✗ ERROR: Cannot connect to DaVinci Resolve!")
        os._exit(1)

    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    if not proj or proj.GetName() != "AI_Titans_EP01_Sam_Altman":
        proj = pm.LoadProject("AI_Titans_EP01_Sam_Altman")
    
    mp = proj.GetMediaPool()

    # Find or activate master timeline
    tl_name = "EP01_MASTER_DIRECTORS_CUT_COMPLETE"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print(f"✗ ERROR: Timeline {tl_name} not found!")
        os._exit(1)

    print(f"==================================================================")
    print(f"🎬 ASSEMBLING MASTER 16-MINUTE DIRECTOR'S CUT: {tl.GetName()}")
    print(f"==================================================================")

    # 1. Clear all existing items from all tracks
    print("\n--- 1. Resetting Timeline Tracks ---")
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            if items:
                tl.DeleteClips(items)
    print("  ✓ All tracks cleared.")

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)

    # Label Tracks
    tl.SetTrackName("video", 1, "MASTER_FLOW_CANVAS_V1")
    tl.SetTrackName("video", 2, "HISTORICAL_ARCHIVES_V2")
    tl.SetTrackName("video", 3, "THOUGHT_CARDS_PRESS_V3")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    tl.SetTrackName("audio", 3, "AUTHENTIC_LIVE_AUDIO_A3")
    tl.SetTrackName("audio", 4, "MECHANICAL_KEYBOARD_SFX_A4")

    # Load all media pool items
    def scan_bin(folder):
        res = {}
        for c in folder.GetClipList():
            res[c.GetName()] = c
        for s in folder.GetSubFolderList():
            res.update(scan_bin(s))
        return res

    clips = scan_bin(mp.GetRootFolder())
    print(f"  ✓ Indexed {len(clips)} items in DaVinci Media Pool.")

    def place_clip(clip_name, media_type, track_idx, rec_frame, vol=None, fades=None):
        c = clips.get(clip_name)
        if not c:
            print(f"  ✗ MISSING MEDIA POOL ITEM: {clip_name}")
            return None
        app = {"mediaPoolItem": c, "mediaType": media_type, "trackIndex": track_idx, "recordFrame": rec_frame}
        items = mp.AppendToTimeline([app])
        if items:
            it = items[0]
            if vol is not None:
                it.SetProperty("AudioVolume", vol)
            if fades:
                it.SetFades(fades)
            return it
        return None

    fade_spec = {'FadeIn': 12.0, 'FadeOut': 12.0}

    # =========================================================================
    # AUDIO TRACK A1: UKRAINIAN VOICEOVER (17 TAKES, BROADCAST LEVEL +2.0 dB)
    # =========================================================================
    print("\n--- 2. Placing Track A1: 100% Ukrainian Voiceover (17 Takes) ---")
    vo_plan = [
        # Block 1 (00:00 - 04:00)
        ("EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav", 0.0),
        ("EP01_VO_UA_02_ACT1_00_15_00_45_Macintosh_LC_II_Indifference.wav", 15.0),
        ("EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 95.0),
        ("EP01_VO_UA_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
        # Block 2 (04:00 - 08:00)
        ("EP01_VO_UA_07_ACT2_04_45_05_45_YC_President_28yo.wav", 241.0),
        ("EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 305.0),
        ("EP01_VO_UA_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav", 365.0),
        ("EP01_VO_UA_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav", 425.0),
        # Block 3 (08:00 - 12:00)
        ("EP01_VO_UA_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav", 481.0),
        ("EP01_VO_UA_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav", 540.0),
        ("EP01_VO_UA_13_ACT3_12_15_13_45_120_Hours_Drama_Guest_Badge.wav", 600.0),
        ("EP01_VO_UA_14_ACT3_13_45_15_30_730_Signatures_Triumphant_Return.wav", 655.0),
        # Block 4 (12:00 - 16:00)
        ("EP01_VO_UA_15_ACT4_15_30_17_00_Stargate_Helion_Energy_Physics.wav", 721.0), # 12:01.0
        ("EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav", 825.0), # 13:45.0
        ("EP01_VO_UA_17_ACT4_18_30_20_00_Future_Is_Created_Now_Outro.wav", 915.0),    # 15:15.0
    ]
    for name, sec in vo_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 2, 1, rf, vol=2.0)
        print(f"  ✓ VO: {name:65} @ {sec:6.1f}s (Frame {rf})")

    # =========================================================================
    # AUDIO TRACK A2: CINEMATIC SCORE BEDS (4 ACTS, -21.0 dB)
    # =========================================================================
    print("\n--- 3. Placing Track A2: 4-Act Cinematic Music Beds (-21.0 dB) ---")
    music_plan = [
        ("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog.wav", 0.0),
        ("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2.wav", 98.0),
        ("EP01_AMB_B2_PART1_00_00_to_02_00_120s.wav", 240.0),
        ("EP01_AMB_B2_PART2_02_00_to_04_00_120s.wav", 360.0),
        ("EP01_MUS_B3_PART1_08_00_to_10_00_120s.wav", 480.0),
        ("EP01_MUS_B3_PART2_10_00_to_12_00_120s.wav", 600.0),
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s.wav", 720.0), # 12:00 to 16:00
    ]
    for name, sec in music_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 2, 2, rf, vol=-21.0)
        print(f"  ✓ Score: {name:50} @ {sec:6.1f}s (Frame {rf})")

    # =========================================================================
    # AUDIO TRACK A3: AUTHENTIC LIVE ARCHIVAL AUDIO
    # =========================================================================
    print("\n--- 4. Placing Track A3: Authentic Live Archival Speeches ---")
    rf_jobs = start_frame + round(165.0 * FPS)
    place_clip("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 3, rf_jobs, vol=-4.0)
    rf_stanford = start_frame + round(254.0 * FPS)
    place_clip("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 2, 3, rf_stanford, vol=-6.0)
    rf_senate = start_frame + round(535.0 * FPS)
    place_clip("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 2, 3, rf_senate, vol=-8.0)
    print("  ✓ Live: Steve Jobs WWDC 2008 (165s), CS183B Lecture (254s), Senate AI Statement (535s)")

    # =========================================================================
    # AUDIO TRACK A4: MECHANICAL KEYBOARD FOLEY SFX (-18.0 dB)
    # =========================================================================
    print("\n--- 5. Placing Track A4: Keyboard SFX Bursts (16 Thought Cards) ---")
    sfx_seconds = [
        45.0, 82.0, 128.0, 185.0,        # Cards 2, 3, 4, 5
        286.0, 344.0, 398.0, 452.0,      # Cards 6, 7, 8, 9
        508.0, 586.0, 644.0, 702.0,      # Cards 10, 11, 12, 13
        755.0, 820.0, 885.0, 935.0       # Cards 14, 15, 16, 17
    ]
    for sec in sfx_seconds:
        rf = start_frame + round(sec * FPS)
        place_clip("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-18.0)
    print(f"  ✓ SFX: 16 keyboard bursts synchronized with thought cards.")

    # =========================================================================
    # VIDEO TRACK V3: 17 THOUGHT CARDS & PRESS DOSSIERS (ZERO OVERLAP WITH V2)
    # =========================================================================
    print("\n--- 6. Placing Track V3: Thought Cards & Primary Source Dossiers ---")
    v3_plan = [
        # Block 1 (00:00 - 04:00)
        ("EP01_CARD_02_Indifference_To_Authority.mp4", 45.0),
        ("EP01_CARD_03_Autonomy_Equation.mp4", 82.0),
        ("EP01_CARD_04_Linear_Vs_Exponential.mp4", 128.0),
        ("EP01_CARD_05_Psychological_Friction.mp4", 185.0),
        ("EP01_DOC_01_YC_2005_Program_10s.mp4", 202.0),
        # Block 2 (04:00 - 08:00)
        ("EP01_CARD_06_Risk_Of_Standing_Still.mp4", 286.0),
        ("EP01_CARD_07_Linear_Blind_Spot.mp4", 344.0),
        ("EP01_DOC_02_OpenAI_Introducing_12s.mp4", 360.0),
        ("EP01_CARD_08_Scaling_Hypothesis.mp4", 398.0),
        ("EP01_CARD_09_Compute_Equation.mp4", 452.0),
        # Block 3 (08:00 - 12:00)
        ("EP01_CARD_10_Exponential_Adoption.mp4", 508.0),
        ("EP01_DOC_03_Board_Ouster_10s.mp4", 570.0),
        ("EP01_CARD_11_Citadel_Paradox.mp4", 586.0),
        ("EP01_CARD_12_Loyalty_Axiom.mp4", 644.0),
        ("EP01_DOC_04_Sutskever_Regret_10s.mp4", 668.0),
        ("EP01_DOC_05_Employees_Letter_12s.mp4", 684.0),
        ("EP01_CARD_13_Paradigm_Of_Power.mp4", 702.0),
        # Block 4 (12:00 - 16:00)
        ("EP01_CARD_14_Physicality_Of_Compute.mp4", 755.0),
        ("EP01_DOC_06_Stargate_100B_Report_10s.mp4", 775.0),
        ("EP01_CARD_15_Seven_Trillion_Equation.mp4", 820.0),
        ("EP01_DOC_07_7_Trillion_Chip_Network_10s.mp4", 840.0),
        ("EP01_CARD_16_Builders_Code_Three_Rules.mp4", 885.0),
        ("EP01_CARD_17_Plastic_Reality_Finale.mp4", 935.0),
    ]
    for name, sec in v3_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 3, rf, fades=fade_spec)
        print(f"  ✓ V3: {name:50} @ {sec:6.1f}s (Frame {rf})")

    # =========================================================================
    # VIDEO TRACK V2: CURATED ARCHIVES (ZERO OVERLAP WITH V3!)
    # =========================================================================
    print("\n--- 7. Placing Track V2: Curated Archival Footage ---")
    v2_plan = [
        # Block 1 (00:00 - 04:00)
        ("EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 20.0),
        ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 62.0),
        ("EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 102.0),
        ("EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 142.0),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 165.0),
        ("EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 218.0),
        # Block 2 (04:00 - 08:00)
        ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 254.0),
        ("EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 273.0),
        ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 320.0),
        ("EP01_V2_B2_02_Stanford_2014_10s.mp4", 376.0),
        ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 428.0),
        # Block 3 (08:00 - 12:00)
        ("EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4", 494.0),
        ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4", 522.0),
        ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 535.0),
        ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture.mp4", 555.0),
        ("EP01_V2_B3_02_Altman_TED_2023_10s.mp4", 625.0),
        # Block 4 (12:00 - 16:00)
        ("EP02_VID_ARCH_01_ACT3_24FPS_Huang_GTC_Stage_Walk.mp4", 792.0),
        ("EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4", 860.0),
        ("EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024.mp4", 910.0),
    ]
    for name, sec in v2_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2: {name:60} @ {sec:6.1f}s (Frame {rf})")

    # =========================================================================
    # VIDEO TRACK V1: 100% GAPLESS MASTER CANVAS (EXACTLY 23,040 FRAMES)
    # ZERO DUPLICATE VIDEO CLIPS ACROSS ENTIRE TIMELINE!
    # =========================================================================
    print("\n--- 8. Placing Track V1: 100% Gapless Unique Canvas (23,040 Frames) ---")

    # Block 1 Canvas (5760 frames / 240.00s)
    b1_v1 = [
        "EP01_V1_CREATIVE_01_Equations_Void_8s.mp4",
        "EP01_CLIP_V1_05_Eye_Code_11s.mp4",
        "EP01_CLIP_V1_06_Boy_Room_10s.mp4",
        "EP01_V1_CREATIVE_02_Galaxies_Axons_12s.mp4",
        "ep01_flow_05_neural_lattice.mp4",
        "EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4",
        "EP01_V1_CREATIVE_03_Chess_Simulation_Grid_15s.mp4",
        "EP01_V1_CREATIVE_04_Mind_Radiating_Light_12s.mp4",
        "EP01_V1_NEW_03_Window_Rain_16s.mp4",
        "ep01_flow_03_silicon_laser.mp4",
        "EP02_SCI_01_Nanobots_Graphene_Lattice_Assembly.mp4",
        "EP01_V1_CREATIVE_05_Holo_Geo_Matrix_16s.mp4",
        "EP01_V1_ASSOC_01_Lidar_City_Grid_8s.mp4",
        "EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4",
        "EP01_V1_ASSOC_02_Chess_Sandstorm_8s.mp4",
        "EP01_CLIP_V1_15_FounderGrit_15s.mp4",
        "EP01_V1_CREATIVE_07_Golden_Transistor_Dust_8s.mp4",
        "ep01_flow_04_exponential_line.mp4",
        "EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4",
        "ep01_flow_09_fusion_torus.mp4",
        "EP09_SCI_01_Asteroid_Coasting_Deep_Space_1080p.mp4",
        "EP01_V1_NEW_06_Cosmic_Dyson_7s.mp4",
        "ep01_flow_10_earth_horizon.mp4",
    ]

    # Block 2 Canvas (5760 frames / 240.00s)
    b2_v1 = [
        "EP01_V1_B2_00_Startup_Engine_Matrix_14s.mp4",
        "Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4",
        "EP01_V1_B2_01_Retro_Cellular_14s.mp4",
        "EP01_CLIP_V1_07_Phosphor_12s.mp4",
        "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4",
        "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4",
        "ep02_flow_01_blackwell_wafer_matrix.mp4",
        "EP01_V1_B2_03_Singularity_Threat_12s.mp4",
        "ep03_flow_01_alphafold_protein_cosmos.mp4",
        "EP01_V1_B2_09_Researchers_Compute_Core_12s.mp4",
        "EP01_V1_B2_04_Robotic_Dexterity_15s.mp4",
        "EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4",
        "EP01_CLIP_V1_16_ServerCold_8s.mp4",
        "EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4",
        "ep01_flow_06_server_monolith.mp4",
        "EP01_V1_B2_07_Corporate_Transmutation_15s.mp4",
        "EP01_V1_B2_08_Silicon_Metropolis_14s.mp4",
        "ep01_flow_08_golden_signatures.mp4",
        "ep07_flow_01_constitutional_prism.mp4",
        "ep06_flow_01_ssi_obsidian_monolith.mp4",
        "EP01_CLIP_V1_08_Hardware_15s.mp4",
        "ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4",
        "EP01_V1_B2_CLOSER_EarthHorizon_289f.mp4", # Exact closer (289f)
    ]

    # Block 3 Canvas (5760 frames / 240.00s)
    b3_v1 = [
        "ep09_flow_01_attention_vector_threads.mp4",
        "ep10_flow_01_global_neural_classroom.mp4",
        "Laser_forms_text_words_89a267cd_1080p.mp4",
        "Mouse_click_triggers_flash_42a0e76f_1080p.mp4",
        "ep04_flow_01_backprop_synapse_storm.mp4",
        "Four_men_sitting_at_table_3911bdbc_1080p.mp4",
        "Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4",
        "EP01_V1_B3_01_Chess_King_Falling_12s.mp4",
        "EP01_V1_B3_02_Boardroom_Void_14s.mp4",
        "ep01_flow_07_boardroom_noir.mp4",
        "EP01_CLIP_V1_12_WaferHero_16s.mp4",
        "EP01_V1_NEW_04_Smartphone_Loopt_16s.mp4",
        "EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4",
        "EP01_CLIP_V1_09_Architecture_15s.mp4",
        "EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4",
        "EP01_V1_NEW_05_Founder_Data_15s.mp4",
        "ep08_flow_01_spatial_intelligence_dome.mp4",
        "ep05_flow_01_jepa_world_model_grid.mp4",
        "Light_point_explodes_into_streaks_0827d703_1080p.mp4",
        "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4",
        "EP01_V1_NEW_06_Cosmic_Dyson_12s.mp4",
        "EP01_CLIP_V1_13_Garage_14s.mp4",
        "EP01_V1_B3_CLOSER_GoldenGrid_340f.mp4", # Exact closer (340f)
    ]

    # Block 4 Canvas (5760 frames / 240.00s)
    b4_v1 = [
        "Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4",
        "EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4",
        "Light_point_explodes_into_streaks_c712a46e_1080p.mp4",
        "Photographic_strobe_inverting_image_81594c7e_1080p.mp4",
        "Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4",
        "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4",
        "EP06_SCI_01_Alcubierre_Warp_Drive_Metric.mp4",
        "EP04_SCI_01_Quantum_Double_Slit_Wave_Collapse.mp4",
        "EP07_SCI_01_Camera_Traversing_Human_Retina.mp4",
        "EP03_SCI_01_RNA_Polymerase_DNA_Transcription.mp4",
        "EP05_SCI_01_Belousov_Zhabotinsky_Oscillator.mp4",
        "EP01_CLIP_V1_19_CurveHero_17s.mp4",
        "EP01_V1_NEW_02_Burroughs_Monoliths_15s.mp4",
        "EP08_SCI_02_Asteroid_Entering_Earth_Atmosphere_1080p.mp4",
        "EP09_SCI_02_Asteroid_Surface_Micro_Structure_1080p.mp4",
        "EP02_SCI_02_Quantum_Levitation_Flux_Pinning.mp4",
        "Boy_aging_into_tech_leader_cd380219_1080p.mp4",
        "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4",
        "Digital_HUD_tracking_vehicles_d7d30811_1080p.mp4",
        "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4",
        "Man_wearing_tactical_arctic_parka_24ef8e34_1080p.mp4",
        "ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4",
        "ElevenLabs_video_seedance-2-5_Intense_macro_r_2026-11-09T12_58_53.mp4",
        "EP01_V1_B4_FINALE_DeepSpace_147f.mp4",
        "EP01_V1_B4_CLOSER_DeepSpace_154f.mp4", # Exact closer (154f)
    ]

    all_v1_blocks = [
        ("Block 1 (Genesis, 00:00 - 04:00)", b1_v1),
        ("Block 2 (The Scaling Frontier, 04:00 - 08:00)", b2_v1),
        ("Block 3 (The Boardroom Coup, 08:00 - 12:00)", b3_v1),
        ("Block 4 (The Builder's Code & AGI Horizon, 12:00 - 16:00)", b4_v1)
    ]

    cur_frame = start_frame
    for block_title, seq in all_v1_blocks:
        b_start = cur_frame
        print(f"\n  ► {block_title}:")
        for name in seq:
            it = place_clip(name, 1, 1, cur_frame)
            if it:
                dur = it.GetDuration()
                cur_frame += dur
                print(f"    ✓ V1 [{dur/24.0:4.1f}s / {dur:3}f]: {name:65} @ {cur_frame - dur}")
            else:
                print(f"    ✗ FAILED TO PLACE: {name}")
        b_frames = cur_frame - b_start
        print(f"    ==> Block Frames: {b_frames} ({b_frames/24.0:.2f}s) [Expected: 5760]")

    total_frames = cur_frame - start_frame
    total_seconds = total_frames / 24.0
    print(f"\n==================================================================")
    print(f"🎉 MASTER TIMELINE ASSEMBLY COMPLETE!")
    print(f"  • Total Duration: {total_frames} frames ({total_seconds:.2f}s / {total_seconds/60.0:.2f} min)")
    print(f"  • Expected Duration: 23040 frames (960.00s / 16:00.00)")
    print(f"  • Frame Accuracy: {'EXACT MATCH (100% GAPLESS)!' if total_frames == 23040 else 'DELTA: ' + str(total_frames - 23040)}")
    print(f"==================================================================")

    tl.SetCurrentTimecode("01:00:00:00")
    os._exit(0)

if __name__ == "__main__":
    assemble_master_16min()
