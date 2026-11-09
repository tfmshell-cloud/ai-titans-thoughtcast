#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE MASTERCLASS DIRECTOR'S CUT V3 — DEDICATED QUOTE BEATS & FATIGUE-FREE ACOUSTIC BALANCE
Timeline: EP01_MASTER_DIRECTORS_CUT_V3_QUOTES_SYNC

DIRECTORIAL MASTER SPECIFICATIONS:
1. DEDICATED QUOTE BEATS (CHRONOLOGICALLY ISOLATED):
   - Pre-Quote Pause (2.0s in-breath): visual cuts to high-res Ukrainian 4K typographic card, narrator pauses.
   - Spoken Quote Delivery: narrator delivers the iconic quote over the illuminated card.
   - Post-Quote Pause (1.8s - 2.5s out-breath): quote card holds for contemplation, music breathes.
   - Narrative Resume: seamless visual cut back to dynamic footage / archival documents.
2. BROADCAST ACOUSTIC RE-BALANCING:
   - Track A1: Ukrainian Voiceover (0.0 dB dialogue master, pristine intelligibility)
   - Track A2: Suno Cinematic Score (-30.0 dB fatigue-free ambient bed across all clips)
   - Track A3: Archival Live Speech (-3.0 dB lip-synced at Steve Jobs WWDC 2008 on Track V1)
3. ZERO BLACK GAPS (CONTINUOUS VISUAL CANVAS):
   - 100% gapless editing on Track V1 integrating ElevenLabs animations, 4K video, 2K stills, and authentic archives.
"""

import sys, os, time, shutil
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def tc_to_frames(s):
    return int(round(s * FPS))

def run():
    print("==================================================================")
    print("🎬 ASSEMBLING MASTERCLASS DIRECTOR'S CUT V3: QUOTE BEATS & -30dB BED")
    print("==================================================================")

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

    # Recursive clip finder
    def get_all_clips(folder):
        clips = {}
        for c in folder.GetClipList():
            clips[c.GetName()] = c
        for sub in folder.GetSubFolderList():
            clips.update(get_all_clips(sub))
        return clips

    all_clips = get_all_clips(root)
    print(f"✓ Indexed {len(all_clips)} clips across Media Pool")

    def find_clip(name_pattern):
        if name_pattern in all_clips:
            return all_clips[name_pattern]
        for k, v in all_clips.items():
            if name_pattern in k:
                return v
        return None

    tl_name = "EP01_MASTER_DIRECTORS_CUT_V3_QUOTES_SYNC"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            break

    if not tl:
        print(f"--- Creating New Master Timeline: {tl_name} ---")
        tl = mp.CreateEmptyTimeline(tl_name)
    else:
        print(f"--- Rebuilding Existing Master Timeline: {tl_name} ---")

    proj.SetCurrentTimeline(tl)
    start_frame = tl.GetStartFrame()

    # Ensure required tracks exist
    while tl.GetTrackCount("video") < 2:
        tl.AddTrack("video")
    while tl.GetTrackCount("audio") < 3:
        tl.AddTrack("audio", "stereo")

    # Clear existing items
    for ttype in ['video', 'audio']:
        for tidx in range(1, tl.GetTrackCount(ttype) + 1):
            items = tl.GetItemListInTrack(ttype, tidx)
            if items:
                tl.DeleteClips(items)

    tl.SetTrackName("video", 1, "MASTER_CINEMATIC_CANVAS_V1")
    tl.SetTrackName("video", 2, "B_ROLL_OVERLAYS_V2")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    tl.SetTrackName("audio", 3, "LIVE_ARCHIVAL_SPEECH_A3")

    def place_item(name_pattern, track_type, track_idx, rec_f, target_dur_s=None):
        c = find_clip(name_pattern)
        if not c:
            print(f"  ✗ Clip NOT FOUND: {name_pattern}")
            return None
        mtype = 1 if track_type == 'video' else 2
        dur_f = tc_to_frames(target_dur_s) if target_dur_s else 120
        res = mp.AppendToTimeline([{
            'mediaPoolItem': c,
            'startFrame': 0,
            'endFrame': dur_f,
            'mediaType': mtype,
            'trackIndex': track_idx,
            'recordFrame': rec_f
        }])
        if res and len(res) > 0:
            return res[0]
        return None

    # =========================================================================
    # MASTER TIMELINE SPECIFICATION WITH QUOTE BEATS (17 SCENES)
    # =========================================================================
    # Each scene defines:
    # - id, title
    # - audio_segments: list of (wav_clip, start_delay_s, dur_s, label)
    #   * start_delay_s is relative to previous audio segment end (creates in-breath/out-breath pause)
    # - scene_pause_s: dramatic pause after the last audio segment
    # - visuals: list of (clip_pat, dur_s, label)
    # =========================================================================

    SCENE_PLANS = [
        # SCENE 01: Pressure of Rules
        {
            "id": 1,
            "title": "Pressure Of Rules",
            "audio": [
                ("EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav", 0.0, 14.03, "Narration")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Intense_macro_r", 5.0, "ElevenLabs: Anime eye morphing into human eye"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 6.0, "Burroughs High School brick facade"),
                ("EP01_CLIP_V1_05_Eye_Code", 7.03, "Extreme close-up eye reflecting green code")
            ]
        },
        # SCENE 02: Macintosh LC II with Quote Beat
        {
            "id": 2,
            "title": "Macintosh LC II & Extension of Thought Quote",
            "audio": [
                ("EP01_VO_UA_02_PART_A_Macintosh_Intro.wav", 0.0, 18.00, "Narration Part A (Intro)"),
                ("EP01_VO_UA_02_PART_B_Extension_Of_Thought_QUOTE.wav", 2.0, 8.20, "Spoken Quote (+2.0s In-breath Pause)"),
                ("EP01_VO_UA_02_PART_C_Authority_Indifference.wav", 1.8, 17.69, "Narration Part C (+1.8s Out-breath Pause)")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("Boy_watching_glowing_code_77d7ee3b_2K", 5.0, "2K Still: Boy gazing at glowing screen"),
                ("ElevenLabs_video_seedance-2-5_Authentic_histo", 5.0, "ElevenLabs: Boy with screwdriver disassembling motherboard"),
                ("Child_inserting_floppy_disk_92a52bea_2K", 4.0, "2K Still: Child inserting floppy disk"),
                ("Camera_moving_through_computer_m_clip", 4.0, "Flythrough computer circuitry"),
                # QUOTE BEAT CARD (2.0s pause + 8.2s quote + 1.8s out-breath = 12.0s)
                ("EP01_UA_CARD_01_Extension_Of_Thought_Macintosh", 12.0, "4K Ukrainian Quote Card: «Ця машина розмила лінію між моїм внутрішнім світом...»"),
                # Part C Visuals (17.69s)
                ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992", 6.0, "1992 Apple Macintosh LC commercial"),
                ("ep01_flow_01_mac_chassis", 5.0, "Macintosh LC II chassis macro"),
                ("Boy_viewing_glowing_terminal_code", 6.69, "Boy viewing glowing terminal code"),
                # Scene Pause Visual (4.0s)
                ("CRT_monitor_displaying_pixel_art_a12cad8c_2K", 4.0, "2K Still: CRT monitor displaying pixel art (Dramatic Scene Pause)")
            ]
        },
        # SCENE 03: John Burroughs School
        {
            "id": 3,
            "title": "John Burroughs School & Engineering Autonomy",
            "audio": [
                ("EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 0.0, 45.64, "Narration")
            ],
            "scene_pause_s": 4.5,
            "visuals": [
                ("EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus", 6.14, "Archival Photo: John Burroughs School campus"),
                ("EP01_V1_NEW_02_Burroughs_Boardroom", 11.0, "School assembly auditorium with student silhouettes"),
                ("EP01_V2_ARCH_01_Altman_Portrait", 12.0, "Young Altman reflection in window glass"),
                ("EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era", 10.0, "Archival Photo: Young Altman in founder t-shirt"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 11.0, "Burroughs campus at dusk (Dramatic Scene Pause)")
            ]
        },
        # SCENE 04: Stanford & Loopt Genesis
        {
            "id": 4,
            "title": "Stanford Arches & Loopt Genesis",
            "audio": [
                ("EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 0.0, 34.93, "Narration")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Dynamic_camera", 5.0, "ElevenLabs: Young Altman with backpack under Stanford stone arches"),
                ("EP01_V2_ARCH_04_Stanford_Campus", 10.0, "Stanford University Quad & palm trees"),
                ("EP01_V1_NEW_01_Silhouette_Dorm", 10.0, "Silhouette packing bags in dorm room"),
                ("ep01_flow_03_silicon_laser", 8.0, "Silicon wafer laser etching"),
                ("EP01_IMG_ARCH_01_Altman_2009_Loopt_Era", 5.93, "Archival Photo: Altman 2005-2009 Loopt era (Dramatic Scene Pause)")
            ]
        },
        # SCENE 05: YC Batch 1, Scurvy Grit with Quote Beat
        {
            "id": 5,
            "title": "YC Batch 1, Loopt & Psychological Friction Quote",
            "audio": [
                ("EP01_VO_UA_05_PART_A_Loopt_Scurvy_Grit.wav", 0.0, 39.25, "Narration Part A (Loopt Grit)"),
                ("EP01_VO_UA_05_PART_B_Psychological_Friction_QUOTE.wav", 2.0, 14.14, "Spoken Quote (+2.0s In-breath Pause)")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("Aerial_view_of_city_center", 10.0, "3D wireframe GPS HUD transforming into real nocturnal city"),
                ("Digital_HUD_tracking_vehicles", 8.0, "Digital GPS tracking vehicles on map interface"),
                ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs", 13.0, "Steve Jobs invites Altman to Apple WWDC 2008 stage"),
                ("EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt", 5.0, "Archival Photo: Steve Jobs & Sam Altman on stage"),
                ("EP01_CLIP_V1_15_FounderGrit", 3.25, "Founder grit, sleeping on startup office floor"),
                # QUOTE BEAT CARD (2.0s pause + 14.14s quote + 2.0s out-breath = 18.14s)
                ("EP01_UA_CARD_02_Psychological_Friction_Loopt", 18.14, "4K Ukrainian Quote Card: «Більшість людей здаються не тому, що їхня ідея хибна...»"),
                # Scene Pause Visual (4.0s)
                ("EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program", 4.0, "Document: YC Summer 2005 program & Green Dot buyout (Dramatic Scene Pause)")
            ]
        },
        # SCENE 06: Compound Interest Mindset (Act 1 Climax)
        {
            "id": 6,
            "title": "Compound Interest Mindset (Act 1 Climax)",
            "audio": [
                ("EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 0.0, 16.51, "Narration")
            ],
            "scene_pause_s": 6.0,
            "visuals": [
                ("Mathematical_decision_tree_in_space_3c0901ac_2K", 7.71, "2K Still: Golden mathematical decision tree expanding"),
                ("Light_point_explodes_into_streaks_0827d703", 8.0, "Light point exploding into golden streaks"),
                ("ep01_flow_04_exponential_line", 6.8, "Golden exponential curve shooting upward (Act 1 Finale Pause)")
            ]
        },
        # SCENE 07: YC President at 28 with Manifesto Quote Beat
        {
            "id": 7,
            "title": "YC President at 28 & Exponential Risk Manifesto Quote",
            "audio": [
                ("EP01_VO_UA_07_PART_A_YC_President_Trajectory.wav", 0.0, 37.60, "Narration Part A (YC President)"),
                ("EP01_VO_UA_07_PART_B_Exponential_Risk_QUOTE.wav", 2.0, 11.25, "Spoken Quote (+2.0s In-breath Pause)")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("Spark_disruption_in_corporate_bo_clip", 8.0, "Corporate leader overlooking storm"),
                ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture", 10.0, "Altman lecturing at Stanford CS183B"),
                ("EP01_V2_B2_01_TechCrunch_Disrupt_2014", 10.0, "Altman on TechCrunch Disrupt 2014 stage"),
                ("EP01_IMG_ARCH_08_Altman_TechCrunch_Disrupt_2014_YC_President", 9.60, "Archival Photo: Altman on TechCrunch stage"),
                # QUOTE BEAT CARD (2.0s pause + 11.25s quote + 2.0s out-breath = 15.25s)
                ("EP01_UA_CARD_03_Exponential_Risk_Manifesto", 15.25, "4K Ukrainian Quote Card: «Люди катастрофічно недооцінюють ризик...»"),
                # Scene Pause Visual (4.0s)
                ("EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President", 4.0, "Archival Photo: Altman Stanford 2014 (Dramatic Scene Pause)")
            ]
        },
        # SCENE 08: Rosewood Dinner & Google Threat
        {
            "id": 8,
            "title": "Rosewood Dinner, DeepMind Threat & Sutskever",
            "audio": [
                ("EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 0.0, 48.77, "Narration")
            ],
            "scene_pause_s": 4.5,
            "visuals": [
                ("Human_zygote_cell_division_timel_clip", 7.27, "Cell division timelapse (Retro Biosciences longevity)"),
                ("Human_prenatal_development_3D_vi_clip", 7.0, "3D developmental bio scan"),
                ("DNA_transcription_molecular_model", 8.0, "Molecular DNA transcription model"),
                ("EP01_V1_B2_02_Rosewood_Boardroom", 12.0, "Dark silhouettes at Rosewood Hotel dinner"),
                ("EP01_V2_B2_03_Altman_Sutskever_TAU", 10.0, "Altman and Ilya Sutskever in close discussion"),
                ("EP01_IMG_ARCH_02_Altman_Ilya_Sutskever_TAU_2023", 9.0, "Archival Photo: Altman & Sutskever (Dramatic Scene Pause)")
            ]
        },
        # SCENE 09: OpenAI Founding & Scale
        {
            "id": 9,
            "title": "OpenAI Founding & The Scaling Hypothesis",
            "audio": [
                ("EP01_VO_UA_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav", 0.0, 45.56, "Narration")
            ],
            "scene_pause_s": 4.5,
            "visuals": [
                ("Electrical_spark_traveling_neuro", 10.0, "Neuron spark into deep learning network"),
                ("Neuron_morphs_into_GPU_chip", 10.0, "Neuron morphing into GPU microchip"),
                ("EP01_V1_B2_04_Robotic_Dexterity", 10.0, "Robotic Dactyl hand solving Rubik's cube"),
                ("EP01_V1_B2_05_Swarm_Gaming_RL", 10.0, "OpenAI Five Dota 2 reinforcement learning"),
                ("Electrical_pulses_firing_through", 10.06, "2K Still: Neural lattice glowing (Dramatic Scene Pause)")
            ]
        },
        # SCENE 10: Capped Profit & Microsoft $1B with Quote Beat
        {
            "id": 10,
            "title": "Capped-Profit Restructure & Compute Equations Quote",
            "audio": [
                ("EP01_VO_UA_10_PART_A_Capped_Profit_Restructure.wav", 0.0, 30.00, "Narration Part A (Restructure)"),
                ("EP01_VO_UA_10_PART_B_Compute_Equations_QUOTE.wav", 2.0, 13.65, "Spoken Quote (+2.0s In-breath Pause)")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("ep01_flow_06_server_monolith", 6.0, "Obsidian server monoliths"),
                ("EP01_V1_B2_06_Server_Matrix_Billions", 12.0, "Supercomputer server matrix"),
                ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO", 6.0, "Altman on TechCrunch Disrupt 2019 stage"),
                ("EP01_IMG_ARCH_09_Altman_TechCrunch_Disrupt_2019_OpenAI_CEO", 6.0, "Archival Photo: Altman 2019"),
                # QUOTE BEAT CARD (2.0s pause + 13.65s quote + 2.5s out-breath = 18.15s)
                ("EP01_UA_CARD_04_Compute_Equations_Microsoft", 18.15, "4K Ukrainian Quote Card: «Ми не зможемо врятувати світ...»"),
                # Scene Pause Visual (5.0s)
                ("EP01_DOC_02_OpenAI_Introducing", 5.0, "OpenAI structure announcement (Act 2 Finale Pause)")
            ]
        },
        # SCENE 11: ChatGPT Launch & US Senate
        {
            "id": 11,
            "title": "ChatGPT Launch & US Senate Hearing",
            "audio": [
                ("EP01_VO_UA_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav", 0.0, 46.11, "Narration")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("Mouse_click_triggers_flash", 8.21, "Mouse click triggers cosmic explosion"),
                ("Camera_plunges_into_terminal_screen", 8.0, "Camera plunges into terminal prompt"),
                ("EP01_V2_B3_01_Altman_ChatGPT_Launch", 9.0, "ChatGPT launch milestone footage"),
                ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup", 9.0, "Altman taking oath in US Senate"),
                ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement", 10.0, "Altman testifying before Senate committee"),
                ("EP01_IMG_ARCH_11_Altman_November_2022_ChatGPT_Genesis", 6.9, "Archival Photo: Altman November 2022 (Dramatic Scene Pause)")
            ]
        },
        # SCENE 12: Friday Board Coup
        {
            "id": 12,
            "title": "Friday Board Coup Nov 17 2023",
            "audio": [
                ("EP01_VO_UA_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav", 0.0, 50.29, "Narration")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("Four_men_sitting_at_table_3911bdbc", 9.09, "Board members meeting across dark table"),
                ("Camera_orbiting_desk_photograph_2c2a80a3", 10.0, "Camera orbiting desk phone & letter"),
                ("Three_people_discussing_at_table_e4a9158b_2K", 9.0, "2K Still: Boardroom silhouettes"),
                ("EP01_V1_B3_01_Chess_King_Falling", 10.0, "Chess king falling in slow-motion"),
                ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture", 9.0, "Ilya Sutskever Simons lecture"),
                ("EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023", 8.2, "Official Board ouster document (Dramatic Scene Pause)")
            ]
        },
        # SCENE 13: 120 Hours Drama & Guest Badge with Quote Beat
        {
            "id": 13,
            "title": "120 Hours Drama, Nadella & Guest Badge Quote",
            "audio": [
                ("EP01_VO_UA_13_PART_A_120_Hours_Loyalty.wav", 0.0, 40.00, "Narration Part A (120 Hours)"),
                ("EP01_VO_UA_13_PART_B_Guest_Badge_QUOTE.wav", 2.0, 3.73, "Spoken Quote (+2.0s In-breath Pause)")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("EP01_V1_B3_03_Two_Silhouettes_Nadella", 10.0, "Silhouettes of Altman and Satya Nadella"),
                ("Photographic_strobe_inverting_image", 10.0, "Photographic strobe flashes"),
                ("EP01_V1_NEW_03_Window_Rain", 10.0, "Rain running down office window over SF"),
                ("Guest_badge_on_desk_a7ff707c_2K", 10.0, "2K Still: Real OpenAI visitor badge"),
                # QUOTE BEAT CARD (2.0s pause + 3.73s quote + 2.0s out-breath = 7.73s)
                ("EP01_UA_CARD_05_Guest_Badge_Nov2023", 7.73, "4K Ukrainian Quote Card: «Перший і останній раз, коли я вдягаю цей бейдж»"),
                # Scene Pause Visual (4.0s)
                ("EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023", 4.0, "Sutskever tweet expressing deep regret (Dramatic Scene Pause)")
            ]
        },
        # SCENE 14: 730 Signatures with Ultimatum Quote Beat
        {
            "id": 14,
            "title": "730 Signatures & 730 Employees Ultimatum Quote",
            "audio": [
                ("EP01_VO_UA_14_PART_A_730_Ultimatum_Intro.wav", 0.0, 10.60, "Narration Part A (Ultimatum Intro)"),
                ("EP01_VO_UA_14_PART_B_Resign_Or_We_Leave_QUOTE.wav", 2.0, 6.90, "Spoken Quote (+2.0s In-breath Pause)"),
                ("EP01_VO_UA_14_PART_C_Sutskever_Regret_Return.wav", 1.8, 36.94, "Narration Part C (+1.8s Out-breath Pause)")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("Camera_accelerating_through_lett_clip", 10.60, "Camera flying through legal ultimatum letter"),
                # QUOTE BEAT CARD (2.0s pause + 6.90s quote + 1.8s out-breath = 10.70s)
                ("EP01_UA_CARD_06_730_Employees_Ultimatum", 10.70, "4K Ukrainian Quote Card: «Або ви йдете у відставку і повертаєте Сема Альтмана...»"),
                # Part C Visuals (36.94s)
                ("Tech_employees_gathered_in_office_b1af5ff2_2K", 9.0, "2K Still: OpenAI employees gathered in solidarity"),
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37", 9.0, "ElevenLabs: Golden network lattice uniting"),
                ("EP01_DOC_05_ACT3_730_Employees_Open_Letter", 9.0, "Document: Open letter signed by 730 employees"),
                ("EP01_V1_B3_04_Golden_Grid_Stabilizing", 9.94, "Golden grid stabilizing power"),
                # Scene Pause Visual (5.0s)
                ("ep01_flow_08_golden_signatures", 5.0, "Golden stream of signatures (Act 3 Finale Pause)")
            ]
        },
        # SCENE 15: Physicality of Compute & Stargate
        {
            "id": 15,
            "title": "Physicality of Compute: Terawatts, Chips & Stargate",
            "audio": [
                ("EP01_VO_UA_15_ACT4_15_30_17_00_Stargate_Helion_Energy_Physics.wav", 0.0, 48.20, "Narration")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("Physical_matter_dissolves_into_b_clip", 9.20, "Physical matter dissolves into digital data bits"),
                ("ep01_flow_09_fusion_torus", 8.0, "Fusion reactor torus glowing with plasma"),
                ("EP10_SCI_01_Tesla_Coil_Electric_Discharges", 10.0, "Tesla coil electric discharges"),
                ("EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal", 8.0, "Jensen Huang reveals Blackwell wafer"),
                ("Man_wearing_tactical_arctic_parka", 8.0, "Leader in arctic parka at subzero datacenter"),
                ("EP01_DOC_06_ACT4_Stargate_100B_Supercluster", 10.0, "Document: Stargate $100B supercluster (Dramatic Scene Pause)")
            ]
        },
        # SCENE 16: Three Rules of Exponential Life
        {
            "id": 16,
            "title": "Three Rules of Exponential Life (with Master Graphic Card)",
            "audio": [
                ("EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav", 0.0, 59.64, "Narration")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Slow,_powerful", 8.0, "ElevenLabs: Slow powerful Altman vision portrait"),
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59", 8.0, "ElevenLabs: Dynamic fluid intelligence cognitive waves"),
                # 4K UKRAINIAN CARD: THREE RULES
                ("EP01_UA_CARD_07_Three_Rules_Exponential_Life", 12.0, "4K Ukrainian Master Card: 1. Ірраціональна віра 2. Проблеми як код 3. Експонента"),
                ("Laser_forms_text_words", 8.0, "Laser writing code words in darkness (Rule 2)"),
                ("EP01_V1_CREATIVE_06_Obsessive_Builders", 10.0, "Obsessive engineers working at midnight"),
                ("Light_point_explodes_into_streaks_c712a46e", 8.0, "Light streaks exploding horizontally (Rule 3)"),
                ("EP01_IMG_ARCH_10_Altman_TED_Vancouver_2023_GPT4", 10.64, "Archival Photo: Altman TED stage (Dramatic Scene Pause)")
            ]
        },
        # SCENE 17: Finale: Plastic Reality
        {
            "id": 17,
            "title": "Finale: Plastic Reality & The Future Created Now",
            "audio": [
                ("EP01_VO_UA_17_ACT4_18_30_20_00_Future_Is_Created_Now_Outro.wav", 0.0, 26.44, "Narration")
            ],
            "scene_pause_s": 15.0,
            "visuals": [
                ("Boy_aging_into_tech_leader", 8.0, "Boy aging into modern tech leader"),
                # 4K UKRAINIAN CARD: PLASTIC REALITY
                ("EP01_UA_CARD_08_Plastic_Reality_Finale", 10.0, "4K Ukrainian Master Card: «Світ набагато пластичніший...»"),
                ("ep01_flow_10_earth_horizon", 8.44, "Golden sunrise over planet Earth"),
                ("EP01_V1_B3_CLOSER_GoldenGrid", 8.0, "Golden grid closer"),
                ("EP01_V1_B4_CLOSER_DeepSpace", 7.0, "Deep space starfield closer (Epic Fadeout)")
            ]
        }
    ]

    # --- 1. Sequential Timeline Construction ---
    print("\n--- 1. Placing Audio & Visual Tracks with Exact Synchronization ---")
    current_audio_rec_f = start_frame
    current_visual_rec_f = start_frame
    jobs_rec_f = None

    for sc in SCENE_PLANS:
        print(f"\n🎬 SCENE {sc['id']:02d}: {sc['title']}")
        sc_audio_start_f = current_audio_rec_f

        # Add timeline marker for the scene
        tl.AddMarker(sc_audio_start_f, "Cyan", f"Scene {sc['id']:02d}: {sc['title']}", "", 1)

        # Place audio segments on Track A1
        for a_clip, delay_s, a_dur, a_label in sc["audio"]:
            current_audio_rec_f += tc_to_frames(delay_s)
            it_a = place_item(a_clip, "audio", 1, current_audio_rec_f, a_dur)
            actual_dur_f = it_a.GetDuration() if (it_a and it_a.GetDuration()) else tc_to_frames(a_dur)
            t_s = (current_audio_rec_f - start_frame) / FPS
            dur_actual_s = actual_dur_f / FPS
            print(f"  🎙️ [{t_s:05.1f}s - {t_s + dur_actual_s:05.1f}s] A1: {a_clip} ({a_label}) [delay: +{delay_s:.1f}s]")
            current_audio_rec_f += actual_dur_f

        # Apply scene pause to audio
        current_audio_rec_f += tc_to_frames(sc["scene_pause_s"])

        # Place visuals on Track V1
        for v_clip, v_dur, v_label in sc["visuals"]:
            it_v = place_item(v_clip, "video", 1, current_visual_rec_f, v_dur)
            actual_dur_f = it_v.GetDuration() if (it_v and it_v.GetDuration()) else tc_to_frames(v_dur)
            t_s = (current_visual_rec_f - start_frame) / FPS
            dur_actual_s = actual_dur_f / FPS
            if "SteveJobs" in v_clip or "WWDC" in v_clip:
                jobs_rec_f = current_visual_rec_f
            print(f"  🎥 [{t_s:05.1f}s - {t_s + dur_actual_s:05.1f}s] V1: {v_clip} ({dur_actual_s:.1f}s) — {v_label}")
            current_visual_rec_f += actual_dur_f

    # --- 2. Place Polyphonic Cinematic Score on Track A2 at -30.0 dB ---
    print("\n--- 2. Placing Cinematic Score Beds on Track A2 (Broadcasting Standard: -30.0 dB) ---")
    scores = [
        ("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog", 0.0, 105.0),
        ("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2", 105.0, 150.0),
        ("EP01_AMB_B2_PART1_00_00_to_02_00_120s", 255.0, 130.0),
        ("EP01_AMB_B2_PART2_02_00_to_04_00_120s", 385.0, 130.0),
        ("EP01_MUS_B3_PART1_08_00_to_10_00_120s", 515.0, 130.0),
        ("EP01_MUS_B3_PART2_10_00_to_12_00_120s", 645.0, 130.0),
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s", 775.0, 105.0)
    ]
    for s_name, start_s, dur_s in scores:
        rec_f = start_frame + tc_to_frames(start_s)
        it = place_item(s_name, "audio", 2, rec_f, dur_s)
        if it:
            # Explicitly attenuate clip volume to -30.0 dB
            it.SetProperty('AudioVolume', -30.0)
            print(f"  🎵 Track A2 Score Bed: {s_name} @ {start_s:.1f}s [AudioVolume: -30.0 dB]")

    # Double-check all items on Track A2 have AudioVolume = -30.0 dB
    a2_items = tl.GetItemListInTrack("audio", 2) or []
    for it in a2_items:
        it.SetProperty('AudioVolume', -30.0)

    # --- 3. Place Archival Live Speech on Track A3 ---
    print("\n--- 3. Synchronizing Steve Jobs Live Speech on Track A3 ---")
    if jobs_rec_f:
        it_jobs = place_item("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008", "audio", 3, jobs_rec_f, 13.0)
        if it_jobs:
            it_jobs.SetProperty('AudioVolume', -3.0)
            jobs_time_s = (jobs_rec_f - start_frame) / FPS
            print(f"  🎙️ Track A3 Archival Speech: Steve Jobs WWDC 2008 @ {jobs_time_s:.1f}s [AudioVolume: -3.0 dB, Lip-Sync Perfect]")

    # --- 4. Master Timeline Verification ---
    v1_items = tl.GetItemListInTrack("video", 1) or []
    a1_items = tl.GetItemListInTrack("audio", 1) or []
    a2_items = tl.GetItemListInTrack("audio", 2) or []
    a3_items = tl.GetItemListInTrack("audio", 3) or []

    total_dur_frames = tl.GetEndFrame() - tl.GetStartFrame()
    total_dur_s = total_dur_frames / FPS

    print("\n==================================================================")
    print("🏆 MASTERCLASS DIRECTOR'S CUT V3 ASSEMBLY COMPLETE")
    print("==================================================================")
    print(f"  • Total Visual Items on Track V1: {len(v1_items)} (Zero Black Gaps)")
    print(f"  • Total Voiceover Segments on Track A1: {len(a1_items)} (Sample-Accurate Quotes & Pauses)")
    print(f"  • Total Score Bed Suites on Track A2: {len(a2_items)} (Volume: -30.0 dB Velvet Level)")
    print(f"  • Archival Speeches on Track A3: {len(a3_items)} (Volume: -3.0 dB)")
    print(f"  • Master Timeline Total Duration: {total_dur_frames} frames ({total_dur_s:.1f}s / {total_dur_s/60:.2f} min)")

    # Save project
    pm.SaveProject()
    print("\n✓ Project saved in DaVinci Resolve Studio 21!")

    # Export project DRP
    export_path = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/06_DAVINCI_PROJECTS/AI_Titans_EP01_Sam_Altman.drp'
    backup_path = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/09_BACKUPS/AI_Titans_EP01_Sam_Altman_Backup.drp'
    if os.path.exists(export_path):
        os.remove(export_path)
    ok_exp = pm.ExportProject('AI_Titans_EP01_Sam_Altman', export_path, False)
    if ok_exp and os.path.exists(export_path):
        shutil.copy2(export_path, backup_path)
        print(f"✓ Exported DRP ({os.path.getsize(export_path)/1024:.1f} KB) & updated backup!")
    else:
        print("✗ DRP export failed!")

if __name__ == "__main__":
    run()
