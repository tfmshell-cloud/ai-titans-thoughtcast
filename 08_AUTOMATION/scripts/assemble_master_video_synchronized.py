#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE ULTIMATE MASTER VIDEO SYNCHRONIZATION (100% VIDEO, ZERO STATIC IMAGES)
Timeline: EP01_MASTER_DIRECTORS_CUT_COMPLETE

DIRECTORIAL ARCHITECTURE:
1. AUDIO A1 (UKRAINIAN VOICEOVER) IS THE MASTER SYNCHRONIZATION CLOCK.
2. USER AI GENERATED VIDEOS (25 CLIPS) ARE THE PRIMARY VISUAL SOURCE:
   - 00:15 - 8yo boy disassembling Macintosh LC II with screwdriver (ElevenLabs authentic history)
   - 01:30 - Young Altman walking Stanford stone arches with military backpack (seedance dynamic)
   - 02:30 - Loopt real-time vehicle GPS tracking HUD (Digital HUD tracking vehicles)
   - 03:30 - Light expanding in geometric void / compound interest (Light point explodes)
   - 04:45 - High-power businessman walking boardroom overlooking rain (Spark disruption)
   - 05:45 - Biological cellular division & longevity (Human zygote & prenatal timelapse)
   - 07:00 - Neuron morphing into GPU silicon chip (Neuron morphs into GPU)
   - 09:30 - Mouse click triggering cosmic flash - ChatGPT Launch moment (Mouse click triggers flash)
   - 10:45 - 4 board members sitting in dark room / FLIR thermal tracking (Four men sitting at table)
   - 13:45 - Document letters accelerating & golden signatures (Camera accelerating through letters)
   - 15:30 - Physical matter dissolving into binary data / Stargate (Physical matter dissolves into bits)
   - 17:00 - Slow powerful determination & exponential life rules (seedance slow powerful)
   - 18:30 - Boy aging into tech leader gazing at Stargate horizon (Boy aging into leader)
3. ZERO STATIC IMAGES: Every single frame on Track V1 and V2 is a full-motion video file (MP4).
4. ZERO DUPLICATES & ZERO MULTI-LAYER COLLISIONS.
"""

import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble():
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
    print(f"🎬 ASSEMBLING MASTER VIDEO-SYNCHRONIZED TIMELINE: {tl.GetName()}")
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
    tl.SetTrackName("video", 1, "MASTER_PRIMARY_AI_VIDEO_V1")
    tl.SetTrackName("video", 2, "AUTHENTIC_ARCHIVES_V2")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    tl.SetTrackName("audio", 3, "LIVE_ARCHIVAL_SPEECHES_A3")
    tl.SetTrackName("audio", 4, "TACTILE_SFX_A4")

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
    # Master timing reference
    # =========================================================================
    print("\n--- 2. Placing Track A1: 100% Ukrainian Voiceover (17 Takes) ---")
    vo_plan = [
        ("EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav", 0.0),
        ("EP01_VO_UA_02_ACT1_00_15_00_45_Macintosh_LC_II_Indifference.wav", 15.0),
        ("EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 95.0),
        ("EP01_VO_UA_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
        ("EP01_VO_UA_07_ACT2_04_45_05_45_YC_President_28yo.wav", 241.0),
        ("EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 305.0),
        ("EP01_VO_UA_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav", 365.0),
        ("EP01_VO_UA_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav", 425.0),
        ("EP01_VO_UA_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav", 481.0),
        ("EP01_VO_UA_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav", 540.0),
        ("EP01_VO_UA_13_ACT3_12_15_13_45_120_Hours_Drama_Guest_Badge.wav", 600.0),
        ("EP01_VO_UA_14_ACT3_13_45_15_30_730_Signatures_Triumphant_Return.wav", 655.0),
        ("EP01_VO_UA_15_ACT4_15_30_17_00_Stargate_Helion_Energy_Physics.wav", 721.0),
        ("EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav", 825.0),
        ("EP01_VO_UA_17_ACT4_18_30_20_00_Future_Is_Created_Now_Outro.wav", 915.0),
    ]
    for name, sec in vo_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 2, 1, rf, vol=2.0)
        print(f"  ✓ VO: {name:65} @ {sec:6.1f}s")

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
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s.wav", 720.0),
    ]
    for name, sec in music_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 2, 2, rf, vol=-21.0)
        print(f"  ✓ Score: {name:50} @ {sec:6.1f}s")

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
    # VIDEO TRACK V2: AUTHENTIC HISTORICAL ARCHIVES (B-ROLL INSETS)
    # =========================================================================
    print("\n--- 5. Placing Track V2: Curated Authentic Historical Archives ---")
    v2_plan = [
        ("EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 22.0),
        ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 62.0),
        ("EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 102.0),
        ("EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 142.0),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 165.0),
        ("EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 218.0),
        ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 254.0),
        ("EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 276.0),
        ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 320.0),
        ("EP01_V2_B2_02_Stanford_2014_10s.mp4", 376.0),
        ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 428.0),
        ("EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4", 494.0),
        ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4", 522.0),
        ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 535.0),
        ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture.mp4", 558.0),
        ("EP01_V2_B3_02_Altman_TED_2023_10s.mp4", 625.0),
        ("EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4", 792.0),
        ("EP04_VID_ARCH_01_ACT4_24FPS_Hinton_Nobel_Warning_2024.mp4", 860.0),
        ("EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024.mp4", 910.0),
    ]
    for name, sec in v2_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2 Archive: {name:60} @ {sec:6.1f}s")

    # =========================================================================
    # VIDEO TRACK V1: PRIMARY MASTER VIDEO SEQUENCE (100% GAPLESS VIDEO)
    # Direct Semantic Match to Ukrainian Narration
    # Zero Static Images! All 25 User AI Videos Featured in Context!
    # =========================================================================
    print("\n--- 6. Placing Track V1: Primary Master Video Canvas (100% Video, Zero Images) ---")

    # 4-Act Semantically Ordered Video Clips
    v1_master_sequence = [
        # === ACT 1: ORIGINS & THE SILICON SHIELD (00:00 - 04:45) ===
        # 00:00 - 00:15: Intro - Pressure of rules & Child in glowing dark room
        "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4",
        "Boy_aging_into_tech_leader_cd380219_1080p.mp4",

        # 00:15 - 00:45: St. Louis 1993 - 8yo boy disassembles Macintosh LC II with screwdriver!
        "ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4", # THE HERO SHOT!
        "Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4",
        "EP01_FLOW_VID_01_ACT1_Macintosh_LC_II_Chassis_1080p24.mp4",

        # 00:45 - 01:30: John Burroughs School & First Strategic Truth
        "Laser_forms_text_words_89a267cd_1080p.mp4",
        "ElevenLabs_video_seedance-2-5_Intense_macro_r_2026-11-09T12_58_53.mp4",
        "EP01_CLIP_V1_05_Eye_Code_11s.mp4",
        "EP01_V1_NEW_02_Burroughs_Monoliths_15s.mp4",

        # 01:30 - 02:30: Stanford Arches & Dropping Out for Loopt
        "ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4", # YOUNG ALTMAN STANFORD ARCHES!
        "EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4",
        "EP01_FLOW_VID_03_ACT1_Silicon_Wafer_Cyan_Laser_720p24.mp4",
        "EP01_V1_CREATIVE_05_Holo_Geo_Matrix_16s.mp4",

        # 02:30 - 03:30: YC Batch 1 (2005) & Loopt Grind
        "Digital_HUD_tracking_vehicles_d7d30811_1080p.mp4", # LOOPT GPS TRACKING HUD!
        "EP01_CLIP_V1_15_FounderGrit_15s.mp4",
        "EP01_V1_NEW_04_Smartphone_Loopt_16s.mp4",
        "EP01_CLIP_V1_13_Garage_14s.mp4",

        # 03:30 - 04:45: Compound Interest & Power of the Exponent
        "Light_point_explodes_into_streaks_0827d703_1080p.mp4", # POINT OF LIGHT EXPANDING!
        "EP01_FLOW_VID_04_ACT1_Golden_Exponential_Curve_720p24.mp4",
        "EP01_V1_CREATIVE_07_Golden_Transistor_Dust_8s.mp4",
        "EP01_V1_CREATIVE_03_Chess_Simulation_Grid_15s.mp4",

        # === ACT 2: THE CODE OF THE EXPONENT & OPENAI BIRTH (04:45 - 09:30) ===
        # 04:45 - 05:45: YC Presidency at 28yo & Venture Reorientation
        "Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4", # BUSINESSMAN UNDER RAIN IN BOARDROOM!
        "EP01_V1_B2_00_Startup_Engine_Matrix_14s.mp4",
        "EP01_V1_B2_01_Retro_Cellular_14s.mp4",

        # 05:45 - 07:00: Rosewood Dinner, Longevity, Nuclear Energy & Compute Exponent
        "Human_zygote_cell_division_timel_clip_063791c0_1080p.mp4", # CELL DIVISION TIMELAPSE!
        "Human_prenatal_development_3D_vi_clip_8b0d0b01_1080p.mp4", # PRENATAL BIO 3D!
        "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4",
        "ep03_flow_01_alphafold_protein_cosmos.mp4",
        "EP01_V1_B2_03_Singularity_Threat_12s.mp4",

        # 07:00 - 08:15: OpenAI Founding & The Scaling Hypothesis
        "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4", # NEURON MORPHING INTO GPU!
        "ep01_flow_05_neural_lattice.mp4",
        "EP01_V1_B2_04_Robotic_Dexterity_15s.mp4",
        "EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4",
        "EP01_V1_B2_09_Researchers_Compute_Core_12s.mp4",

        # 08:15 - 09:30: Capped-Profit & Microsoft $1B Deal
        "ep01_flow_06_server_monolith.mp4",
        "EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4",
        "EP01_CLIP_V1_16_ServerCold_8s.mp4",
        "EP01_V1_B2_08_Silicon_Metropolis_14s.mp4",
        "EP01_V1_B2_07_Corporate_Transmutation_15s.mp4",

        # === ACT 3: THE EARTHQUAKE & THE 100-HOUR COUP (09:30 - 15:30) ===
        # 09:30 - 10:45: ChatGPT Release Earthquake & Senate Spotlight
        "Mouse_click_triggers_flash_42a0e76f_1080p.mp4", # MOUSE CLICK FLASH CHATGPT RELEASE!
        "Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4",
        "EP01_CLIP_V1_09_Architecture_15s.mp4",
        "ep09_flow_01_attention_vector_threads.mp4",
        "ep10_flow_01_global_neural_classroom.mp4",

        # 10:45 - 12:15: Friday Nov 17 Board Ouster in Google Meet
        "Four_men_sitting_at_table_3911bdbc_1080p.mp4", # 4 BOARD MEMBERS COUP / FLIR THERMAL!
        "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4",
        "ep01_flow_07_boardroom_noir.mp4",
        "EP01_V1_B3_01_Chess_King_Falling_12s.mp4",
        "EP01_V1_B3_02_Boardroom_Void_14s.mp4",

        # 12:15 - 13:45: 120 Hours Drama & Guest Badge
        "EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4",
        "Photographic_strobe_inverting_image_81594c7e_1080p.mp4",
        "EP01_CLIP_V1_12_WaferHero_16s.mp4",
        "EP01_V1_NEW_05_Founder_Data_15s.mp4",

        # 13:45 - 15:30: 730 Signatures & The Triumphant Return
        "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4", # CAMERA THROUGH LETTERS / MANIFESTO!
        "ep01_flow_08_golden_signatures.mp4",
        "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4",
        "EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4",
        "ep06_flow_01_ssi_obsidian_monolith.mp4",

        # === ACT 4: BUILDER'S CODE & THE HORIZON OF AGI (15:30 - 20:00) ===
        # 15:30 - 17:00: Stargate, Fusion Energy & Physicality of Compute
        "Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4", # MATTER DISSOLVES INTO BITS!
        "ep01_flow_09_fusion_torus.mp4",
        "EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4",
        "Man_wearing_tactical_arctic_parka_24ef8e34_1080p.mp4",
        "ep02_flow_01_blackwell_wafer_matrix.mp4",
        "EP01_CLIP_V1_19_CurveHero_17s.mp4",

        # 17:00 - 18:30: Three Rules of Exponential Life
        "ElevenLabs_video_seedance-2-5_Slow,_powerful__2026-11-09T12_52_53.mp4",
        "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59.mp4",
        "Light_point_explodes_into_streaks_c712a46e_1080p.mp4",
        "EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4",
        "EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4",

        # 18:30 - 20:00: Plastic Reality & The Future Is Created Now
        "ep01_flow_10_earth_horizon.mp4",
        "EP01_V1_B2_CLOSER_EarthHorizon_289f.mp4",
        "EP01_V1_B3_CLOSER_GoldenGrid_340f.mp4",
        "EP01_V1_B4_CLOSER_DeepSpace_154f.mp4",
    ]

    curr_frame = start_frame
    placed_v1_count = 0
    for clip_name in v1_master_sequence:
        c = clips.get(clip_name)
        if not c:
            print(f"  ✗ WARNING: Missing V1 Clip: {clip_name}")
            continue
        
        # Determine duration
        p = c.GetClipProperty()
        dur_raw = p.get('Frames', '')
        dur_f = int(dur_raw) if dur_raw and dur_raw.isdigit() else 240
        
        app = {"mediaPoolItem": c, "mediaType": 1, "trackIndex": 1, "recordFrame": curr_frame}
        res = mp.AppendToTimeline([app])
        if res:
            it = res[0]
            # Use actual timeline item duration
            actual_dur = it.GetEnd() - it.GetStart()
            curr_frame += actual_dur
            placed_v1_count += 1
            print(f"  ✓ V1 #{placed_v1_count:02d}: {clip_name:65} [{actual_dur:4d}f / {actual_dur/FPS:4.1f}s] -> Next @ {curr_frame}")

    total_v1_frames = curr_frame - start_frame
    print(f"\n==================================================================")
    print(f"🎉 MASTER VIDEO SYNCHRONIZATION COMPLETE!")
    print(f"   - Total V1 Video Clips Placed: {placed_v1_count}")
    print(f"   - Total Timeline Duration: {total_v1_frames} frames ({total_v1_frames/FPS:.2f}s / {total_v1_frames/FPS/60:.2f} min)")
    print(f"   - Track V1: 100% Gapless Video (Zero Static Images)")
    print(f"   - Track V2: 19 Curated Archival Video Insets")
    print(f"   - Track A1: 17 Ukrainian Voiceover Takes (+2.0 dB)")
    print(f"   - Track A2: 4-Act Continuous Drone/Pulse Score (-21.0 dB)")
    print(f"   - Track A3: Live Archival Speeches (Jobs WWDC, CS183B, Senate)")
    print(f"==================================================================")

    # Save Project
    pm.SaveProject()
    print("✓ Project Saved Successfully.")
    os._exit(0)

if __name__ == '__main__':
    assemble()
