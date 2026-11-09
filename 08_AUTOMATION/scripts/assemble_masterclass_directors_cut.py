#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE MASTERCLASS DIRECTOR'S CUT (HOLLYWOOD / OSCAR GRADE)
Timeline: EP01_MASTER_DIRECTORS_CUT_COMPLETE

DIRECTORIAL SPECIFICATIONS:
1. PURE VIDEO ONLY:
   Only authentic user AI video generations, internet archival footage, and core Flow video renders.
   Zero text cards, zero document images, zero static PNG/JPEGs.
2. SURGICAL SEMANTIC SYNCHRONIZATION:
   Every video clip is placed at the exact second where its subject is spoken by the Ukrainian narrator.
3. PRESERVED INTENTIONAL GAPS:
   Where no perfect video exists, clean gaps are left for upcoming image/document insertions.
4. POLYPHONIC AUDIO DESIGN:
   - Track A1: Ukrainian Voiceover (0.0 dB, pristine dialogue)
   - Track A2: 4-Act Cinematic Score (-22.0 dB, ducked under speech)
   - Track A3: Authentic Live Archival Speeches (Steve Jobs WWDC 2008 demo)
"""

import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def tc_to_frames(tc):
    parts = [int(p) for p in tc.split(':')]
    return parts[0]*3600*24 + parts[1]*60*24 + parts[2]*24 + parts[3]

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
        sys.exit(1)

    print("==================================================================")
    print(f"🎬 ASSEMBLING MASTERCLASS DIRECTOR'S CUT: {tl.GetName()}")
    print("==================================================================")

    # 1. Reset timeline tracks
    print("\n--- 1. Resetting Timeline Video & Audio Auxiliary Tracks ---")
    for vi in range(1, tl.GetTrackCount("video") + 1):
        v_items = tl.GetItemListInTrack("video", vi) or []
        if v_items:
            tl.DeleteClips(v_items)
            print(f"  ✓ Cleared {len(v_items)} clips from video track V{vi}")

    for ai in range(2, tl.GetTrackCount("audio") + 1):
        a_items = tl.GetItemListInTrack("audio", ai) or []
        if a_items:
            tl.DeleteClips(a_items)
            print(f"  ✓ Cleared {len(a_items)} clips from auxiliary audio track A{ai}")

    tl.SetTrackName("video", 1, "MASTER_CINEMATIC_CANVAS_V1")
    if tl.GetTrackCount("video") >= 2:
        tl.SetTrackName("video", 2, "B_ROLL_OVERLAYS_V2")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_A1")
    if tl.GetTrackCount("audio") >= 2:
        tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    if tl.GetTrackCount("audio") >= 3:
        tl.SetTrackName("audio", 3, "LIVE_ARCHIVAL_SPEECH_A3")

    # 2. Collect all Media Pool clips
    all_clips = {}
    def scan_bin(folder):
        for c in folder.GetClipList() or []:
            all_clips[c.GetName()] = c
        for sf in folder.GetSubFolderList() or []:
            scan_bin(sf)
    scan_bin(root)

    def place_clip(clip_name, media_type, track_idx, rec_frame, vol=None):
        c = all_clips.get(clip_name)
        if not c:
            alt_name = clip_name.replace('_', ' ')
            c = all_clips.get(alt_name)
        if not c:
            print(f"  ✗ MISSING MEDIA POOL ITEM: {clip_name}")
            return None

        app = {
            "mediaPoolItem": c,
            "mediaType": media_type,
            "trackIndex": track_idx,
            "recordFrame": rec_frame
        }
        res = mp.AppendToTimeline([app])
        if res:
            it = res[0]
            if vol is not None:
                it.SetProperty("AudioVolume", vol)
            return it
        return None

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)

    # 3. Master Cut Specifications (Exact frame alignment to A1 voiceover)
    # Format: (Scene Num, Scene Start Frame, [(Clip Name, Offset Seconds, Max Duration Seconds, Label)])
    # Based on the exact timing of the 17 Ukrainian VO clips on Track A1
    director_cuts = [
        # SCENE 01: [00:00.0 - 00:14.0] (Pressure of rules)
        (1, start_frame + 0, [
            ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 0.0, 8.0, "Burroughs High School Campus (Internet Archive)"),
            ("EP01_CLIP_V1_05_Eye_Code_11s.mp4", 8.0, 6.0, "Eye Analyzing Rules & Code (AI Video)")
        ]),

        # SCENE 02: [00:15.0 - 00:58.9] (1993 Macintosh LC II, boy with screwdriver)
        (2, start_frame + 360, [
            ("Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4", 0.0, 8.0, "Boy Viewing Glowing CRT Monitor in Bedroom (User AI)"),
            ("ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4", 8.0, 5.0, "8yo Boy with Screwdriver Disassembling Motherboard (ElevenLabs)"),
            ("Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4", 13.0, 8.0, "Camera Moving Through Computer Circuitry (User AI)"),
            ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4", 21.0, 8.0, "Apple Macintosh 1992 CRT Commercial (Internet Archive)"),
            ("ep01_flow_01_mac_chassis.mp4", 29.0, 7.0, "Macintosh LC II Chassis (Flow Video)"),
            ("ep01_flow_02_crt_code.mp4", 36.0, 7.9, "Green Phosphor CRT Code (Flow Video)")
        ]),

        # SCENE 03: [00:59.9 - 01:45.5] (Burroughs School assembly & coming out)
        (3, start_frame + 1438, [
            ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 0.0, 8.0, "Burroughs School Brick Facade (Internet Archive)"),
            ("EP01_V1_NEW_02_Burroughs_Boardroom_15s.mp4", 8.0, 15.0, "Burroughs Assembly Auditorium (Internet Archive)"),
            ("EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 23.0, 12.0, "Young Altman Portrait Reflection in Glass (Internet Archive)")
            # [35.0 - 45.6s] -> GAP for 16yo Altman photo / yearbook!
        ]),

        # SCENE 04: [01:46.5 - 02:21.4] (Stanford campus & dropping out)
        (4, start_frame + 2556, [
            ("ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4", 0.0, 5.0, "Young Altman with Backpack in Stanford Arches (ElevenLabs)"),
            ("EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 5.0, 10.0, "Stanford University Quad & Palms (Internet Archive)"),
            ("EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4", 15.0, 10.0, "Stanford Dorm Room Night Silhouette (AI Video)"),
            ("ep01_flow_03_silicon_laser.mp4", 25.0, 9.9, "Silicon Wafer Laser Etching Pulse (Flow Video)")
        ]),

        # SCENE 05: [02:22.4 - 03:15.8] (Loopt, YC Batch 1, Steve Jobs WWDC 2008)
        (5, start_frame + 3418, [
            ("Digital_HUD_tracking_vehicles_d7d30811_1080p.mp4", 0.0, 10.0, "Digital HUD Vehicle GPS Tracking Loopt (User AI)"),
            ("EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 10.0, 12.0, "Altman at Loopt 2005 Startup Garage (Internet Archive)"),
            ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 22.0, 13.1, "Steve Jobs Introduces Altman at Apple WWDC 2008 (Internet Archive)"),
            ("EP01_CLIP_V1_15_FounderGrit_15s.mp4", 35.1, 12.0, "Founder Grit & Physical Exhaustion (AI Video)")
            # [47.1 - 53.4s] -> GAP for Green Dot acquisition press clipping!
        ]),

        # SCENE 06: [03:16.8 - 03:33.3] (Compound interest)
        (6, start_frame + 4723, [
            ("Light_point_explodes_into_streaks_0827d703_1080p.mp4", 0.0, 8.0, "Light Point Exploding into Golden Streaks (User AI)"),
            ("ep01_flow_04_exponential_line.mp4", 8.0, 8.5, "Golden Exponential Ascending Curve (Flow Video)")
        ]),

        # SCENE 07: [03:34.3 - 04:23.1] (YC President at 28)
        (7, start_frame + 5143, [
            ("Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4", 0.0, 10.0, "Corporate Leader in High-Rise Overlooking Rain (User AI)"),
            ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 10.0, 18.1, "Altman Lecturing Stanford CS183B (Internet Archive)"),
            ("EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 28.1, 10.0, "Altman on TechCrunch Disrupt 2014 Stage (Internet Archive)")
            # [38.1 - 48.8s] -> GAP for YC Research manifesto / Helion fusion concept!
        ]),

        # SCENE 08: [04:24.1 - 05:12.9] (Rosewood dinner, longevity, DeepMind threat)
        (8, start_frame + 6338, [
            ("Human_zygote_cell_division_timel_clip_063791c0_1080p.mp4", 0.0, 10.0, "Zygote Cell Division Exponential Growth (User AI)"),
            ("Human_prenatal_development_3D_vi_clip_8b0d0b01_1080p.mp4", 10.0, 10.0, "3D Developmental Bio Scan (User AI)"),
            ("EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", 20.0, 12.0, "Rosewood Dinner Table Silhouettes (AI Video)"),
            ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 32.0, 10.0, "Altman & Ilya Sutskever in Discussion (Internet Archive)")
            # [42.0 - 48.8s] -> GAP for DeepMind acquisition headline!
        ]),

        # SCENE 09: [05:13.9 - 05:59.4] (OpenAI founding & Scaling Hypothesis)
        (9, start_frame + 7532, [
            ("Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4", 0.0, 10.0, "Neuron Morphs into GPU Microchip (User AI)"),
            ("ep01_flow_05_neural_lattice.mp4", 10.0, 5.0, "Neural Network Lattice Pulse (Flow Video)"),
            ("EP01_V1_B2_04_Robotic_Dexterity_15s.mp4", 15.0, 12.0, "Robotic Hand Solving Rubik's Cube (AI Video)"),
            ("EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4", 27.0, 12.0, "Reinforcement Learning Swarm Dota 2 (AI Video)")
            # [39.0 - 45.5s] -> GAP for "Scale is all you need" quote!
        ]),

        # SCENE 10: [06:00.4 - 06:44.0] (Capped-profit & Microsoft $1B)
        (10, start_frame + 8650, [
            ("ep01_flow_06_server_monolith.mp4", 0.0, 5.0, "Server Monoliths in Obsidian Datacenter (Flow Video)"),
            ("EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4", 5.0, 15.0, "Server Matrix Billions Compute (AI Video)"),
            ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 20.0, 10.0, "Altman on TechCrunch Disrupt 2019 as OpenAI CEO (Internet Archive)")
            # [30.0 - 43.6s] -> GAP for Microsoft / Nadella contract photo!
        ]),

        # SCENE 11: [06:45.0 - 07:31.1] (ChatGPT launch & Senate hearing)
        (11, start_frame + 9720, [
            ("Mouse_click_triggers_flash_42a0e76f_1080p.mp4", 0.0, 10.0, "Mouse Click Triggers Cosmic Flash (User AI)"),
            ("Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4", 10.0, 10.0, "Camera Plunges into Terminal Screen Prompt (User AI)"),
            ("EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4", 20.0, 8.0, "ChatGPT Launch Milestone (Internet Archive)"),
            ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4", 28.0, 9.0, "Altman Taking Oath in US Senate (Internet Archive)"),
            ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 37.0, 9.1, "Altman Testifying for AI Regulation in US Senate (Internet Archive)")
        ]),

        # SCENE 12: [07:32.1 - 08:22.4] (Friday Nov 17 2023 Board Coup)
        (12, start_frame + 10850, [
            ("Four_men_sitting_at_table_3911bdbc_1080p.mp4", 0.0, 10.0, "Four Board Members Meeting at Table (User AI)"),
            ("Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4", 10.0, 10.0, "Camera Orbiting Desk Telephone Noir (User AI)"),
            ("ep01_flow_07_boardroom_noir.mp4", 20.0, 5.0, "Boardroom Noir Shadows (Flow Video)"),
            ("EP01_V1_B3_01_Chess_King_Falling_12s.mp4", 25.0, 12.0, "Chess King Falling in Slow Motion (AI Video)"),
            ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture.mp4", 37.0, 8.0, "Ilya Sutskever Simons Institute Lecture (Internet Archive)")
            # [45.0 - 50.2s] -> GAP for Breaking News stock crash banner!
        ]),

        # SCENE 13: [08:23.4 - 09:07.1] (120 Hours drama, Nadella, guest badge)
        (13, start_frame + 12080, [
            ("EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4", 0.0, 12.0, "Two Silhouettes Altman & Satya Nadella (AI Video)"),
            ("Photographic_strobe_inverting_image_81594c7e_1080p.mp4", 12.0, 10.0, "Photographic Strobe Flashes Inverting (User AI)"),
            ("EP01_V1_NEW_03_Window_Rain_16s.mp4", 22.0, 12.0, "Rainy Window Looking over San Francisco (AI Video)")
            # [34.0 - 43.7s] -> GAP for the iconic Guest Badge photograph!
        ]),

        # SCENE 14: [09:08.1 - 10:02.5] (730 Signatures & triumphant return)
        (14, start_frame + 13154, [
            ("Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4", 0.0, 10.0, "Camera Accelerating Through Letter Text (User AI)"),
            ("ep01_flow_08_golden_signatures.mp4", 10.0, 5.0, "Golden Signatures Flowing Stream (Flow Video)"),
            ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4", 15.0, 5.0, "Stylized Golden Network Grid (ElevenLabs)"),
            ("EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4", 20.0, 15.0, "Golden Grid Stabilizing Power (AI Video)")
            # [35.0 - 54.4s] -> GAP for the 730 employee signatures document!
        ]),

        # SCENE 15: [10:03.5 - 10:51.7] (Physicality of compute, Stargate $100B, fusion)
        (15, start_frame + 14484, [
            ("Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4", 0.0, 10.0, "Physical Matter Dissolves into Bits (User AI)"),
            ("ep01_flow_09_fusion_torus.mp4", 10.0, 5.0, "Fusion Torus Reactor Energy Core (Flow Video)"),
            ("EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4", 15.0, 15.0, "Tesla Coil Electric Power Discharges (Internet Archive)"),
            ("Man_wearing_tactical_arctic_parka_24ef8e34_1080p.mp4", 30.0, 6.0, "Leader in Arctic Tactical Parka at Datacenter (User AI)"),
            ("EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4", 36.0, 8.0, "Jensen Huang Reveals Blackwell Wafer (Internet Archive)")
            # [44.0 - 48.2s] -> GAP for Stargate supercomputer concept!
        ]),

        # SCENE 16: [10:52.7 - 11:52.3] (Three rules of exponential life)
        (16, start_frame + 15664, [
            ("ElevenLabs_video_seedance-2-5_Slow,_powerful__2026-11-09T12_52_53.mp4", 0.0, 5.0, "Slow Powerful Altman Vision Portrait (ElevenLabs)"),
            ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59.mp4", 5.0, 5.0, "Fluid Intelligence Dynamic Waves (ElevenLabs)"),
            ("Light_point_explodes_into_streaks_c712a46e_1080p.mp4", 10.0, 10.0, "Light Streaks Exploding Horizontally (User AI)"),
            ("EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4", 20.0, 12.0, "Obsessive Builders Working at Midnight (AI Video)"),
            ("Laser_forms_text_words_89a267cd_1080p.mp4", 32.0, 10.0, "Laser Writing Words in Darkness (User AI)")
            # [42.0 - 59.6s] -> GAP for Three Rules graphic / text card!
        ]),

        # SCENE 17: [11:53.3 - 12:19.7] (Plastic reality & finale)
        (17, start_frame + 17119, [
            ("Boy_aging_into_tech_leader_cd380219_1080p.mp4", 0.0, 10.0, "Boy Morphing into Modern Tech Leader (User AI)"),
            ("ep01_flow_10_earth_horizon.mp4", 10.0, 5.0, "Earth Horizon Sunrise from Orbit (Flow Video)"),
            ("EP01_V1_B3_CLOSER_GoldenGrid_340f.mp4", 15.0, 7.0, "Golden Grid Closer (Flow Closer)"),
            ("EP01_V1_B4_CLOSER_DeepSpace_154f.mp4", 22.0, 6.4, "Deep Space Starfield Closer (Flow Closer)")
        ])
    ]

    print("\n--- 2. Placing Master Semantic Video Cuts on Track V1 ---")
    total_placed_video = 0
    total_gaps_identified = 0

    for sc_num, sc_start_f, clips_spec in director_cuts:
        print(f"\n🎬 SCENE {sc_num:02d} (starts frame {sc_start_f} / {(sc_start_f-start_frame)/FPS:.1f}s):")
        last_clip_end_f = sc_start_f
        for clip_name, offset_s, dur_s, label in clips_spec:
            rec_f = sc_start_f + int(offset_s * FPS)
            dur_f = int(dur_s * FPS)
            it = place_clip(clip_name, 1, 1, rec_f)
            if it:
                total_placed_video += 1
                clip_dur_f = it.GetDuration() if (it and it.GetDuration()) else dur_f
                clip_start_s = (rec_f - start_frame) / FPS
                clip_end_s = (rec_f + clip_dur_f - start_frame) / FPS
                print(f"  🎥 [{clip_start_s:04.1f}s - {clip_end_s:04.1f}s] V1: {clip_name} ({clip_dur_f/FPS:.1f}s) — {label}")
                last_clip_end_f = rec_f + clip_dur_f

    # 4. Sound Design & Musical Architecture
    print("\n--- 3. Polishing Sound Design & Music Architecture ---")
    # Score on Track A2 (-22.0 dB, ambient foundation)
    score_tracks = [
        ("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog.wav", start_frame + 0),
        ("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2.wav", start_frame + 2352),
        ("EP01_AMB_B2_PART1_00_00_to_02_00_120s.wav", start_frame + 5760),
        ("EP01_AMB_B2_PART2_02_00_to_04_00_120s.wav", start_frame + 8640),
        ("EP01_MUS_B3_PART1_08_00_to_10_00_120s.wav", start_frame + 11520),
        ("EP01_MUS_B3_PART2_10_00_to_12_00_120s.wav", start_frame + 14400),
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s.wav", start_frame + 16000),
    ]
    for s_name, s_rf in score_tracks:
        it = place_clip(s_name, 2, 2, s_rf, vol=-22.0)
        if it:
            ss = (s_rf - start_frame) / FPS
            print(f"  🎵 Track A2 Score: {s_name} @ {ss:.1f}s (-22.0 dB)")

    # Live Archival Speech on Track A3 (Steve Jobs WWDC 2008 demo audio)
    # Aligned with the Jobs video clip in Scene 5 (start_frame + 3418 + 22*24 = start_frame + 3946)
    jobs_audio_f = start_frame + 3418 + int(22.0 * FPS)
    it_jobs = place_clip("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 3, jobs_audio_f, vol=-3.0)
    if it_jobs:
        print(f"  🎙️ Track A3 Archival Speech: Steve Jobs WWDC 2008 @ {(jobs_audio_f - start_frame)/FPS:.1f}s (-3.0 dB)")

    # 5. Verification
    print("\n--- 4. Verification of Masterclass Assembly ---")
    v1_count = len(tl.GetItemListInTrack("video", 1) or [])
    a1_count = len(tl.GetItemListInTrack("audio", 1) or [])
    a2_count = len(tl.GetItemListInTrack("audio", 2) or []) if tl.GetTrackCount("audio") >= 2 else 0
    a3_count = len(tl.GetItemListInTrack("audio", 3) or []) if tl.GetTrackCount("audio") >= 3 else 0

    print(f"  • Video Track V1 clips: {v1_count} (Pure video only, 0 text cards)")
    print(f"  • Audio Track A1 clips: {a1_count} (Ukrainian Voiceover across all 17 scenes)")
    print(f"  • Audio Track A2 clips: {a2_count} (Cinematic orchestral score ducked at -22 dB)")
    print(f"  • Audio Track A3 clips: {a3_count} (Steve Jobs live speech audio)")

    pm.SaveProject()
    print("\n🏆 MASTERCLASS DIRECTOR'S CUT ASSEMBLED & SAVED SUCCESSFULLY!")

if __name__ == '__main__':
    run()
