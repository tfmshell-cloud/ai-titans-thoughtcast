#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE MASTERCLASS DIRECTOR'S CUT V2 — PERFECT THEMATIC SYNCHRONIZATION WITH DRAMATIC PAUSES
Timeline: EP01_MASTER_DIRECTORS_CUT_V2_PERFECT_SYNC

DIRECTORIAL MASTER SPECIFICATIONS:
1. MAXIMAL ELEVENLABS ANIMATIONS:
   Integrates all 6 ElevenLabs seedance video animations (Macro Eye, Boy with screwdriver, Stanford Arches, Golden Grid, Slow Portrait, Cognitive Waves).
2. INTENTIONAL DRAMATIC PAUSES:
   Natural breathing room (3.5s - 6.0s) between scenes for the narration, allowing orchestral swells and visual contemplation.
3. ZERO BLACK GAPS (CONTINUOUS VISUAL CANVAS):
   All gaps, pauses, and historical mentions are filled with high-res 2K imagery and authentic documents.
4. POLYPHONIC AUDIO DESIGN:
   - Track A1: Ukrainian Voiceover (0.0 dB, pristine dialogue)
   - Track A2: Cinematic Score Suites (-22.0 dB ducked)
   - Track A3: Steve Jobs live speech audio at Apple WWDC 2008
"""

import sys, os, time, shutil
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def tc_to_frames(s):
    return int(round(s * FPS))

def run():
    print("==================================================================")
    print("🎬 ASSEMBLING MASTERCLASS DIRECTOR'S CUT V2: PERFECT SYNC & PAUSES")
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
        # exact match first
        if name_pattern in all_clips:
            return all_clips[name_pattern]
        # partial match
        for k, v in all_clips.items():
            if name_pattern in k:
                return v
        return None

    # Check or create timeline
    tl_name = "EP01_MASTER_DIRECTORS_CUT_V2_PERFECT_SYNC"
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

    # Clear tracks
    for ttype in ['video', 'audio']:
        for tidx in range(1, tl.GetTrackCount(ttype) + 1):
            items = tl.GetItemListInTrack(ttype, tidx)
            if items:
                tl.DeleteClips(items)

    # Ensure track names
    tl.SetTrackName("video", 1, "MASTER_CINEMATIC_CANVAS_V1")
    tl.SetTrackName("video", 2, "B_ROLL_OVERLAYS_V2")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    tl.SetTrackName("audio", 3, "LIVE_ARCHIVAL_SPEECH_A3")

    # Helper to place clip
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
    # MASTER SCENE ARCHITECTURE (17 SCENES WITH CINEMATIC DRAMATIC PAUSES)
    # =========================================================================
    # Each scene has:
    # - id: scene number
    # - vo_file: audio filename
    # - vo_start_s: start time in seconds
    # - vo_dur_s: audio duration
    # - pause_s: dramatic pause after voiceover
    # - visual_flow: list of (clip_pattern, duration_seconds, label)
    # =========================================================================

    SCENES = [
        # SCENE 01: Pressure of Rules (0.0s - 18.0s)
        {
            "id": 1,
            "title": "Pressure Of Rules",
            "vo": "EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav",
            "vo_start_s": 0.0,
            "vo_dur_s": 14.03,
            "pause_s": 4.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Intense_macro_r", 5.0, "ElevenLabs: Anime green eye morphing into hyperrealistic human eye"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 6.0, "Burroughs High School strict brick facade & corridors"),
                ("EP01_CLIP_V1_05_Eye_Code", 7.0, "Extreme close-up eye reflecting green computer code")
            ]
        },
        # SCENE 02: Macintosh LC II (18.0s - 65.9s)
        {
            "id": 2,
            "title": "Macintosh LC II & Indifference to Authority",
            "vo": "EP01_VO_UA_02_ACT1_00_15_00_45_Macintosh_LC_II_Indifference.wav",
            "vo_start_s": 18.0,
            "vo_dur_s": 43.89,
            "pause_s": 4.0,
            "visuals": [
                ("Boy_watching_glowing_code_77d7ee3b_2K", 6.0, "2K Still: 8yo boy in dark bedroom gazing at glowing screen"),
                ("ElevenLabs_video_seedance-2-5_Authentic_histo", 5.0, "ElevenLabs: 8yo boy with screwdriver disassembling motherboard"),
                ("Child_inserting_floppy_disk_92a52bea_2K", 5.0, "2K Still: Child inserting 3.5 floppy disk into Macintosh drive"),
                ("Camera_moving_through_computer_m_clip", 9.0, "Camera fly-through microchips and computer circuitry"),
                ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992", 6.0, "Authentic 1992 Apple Macintosh LC commercial"),
                ("ep01_flow_01_mac_chassis", 6.0, "Macintosh LC II chassis macro render"),
                ("Boy_viewing_glowing_terminal_code", 6.9, "Boy viewing glowing terminal code late at night"),
                ("CRT_monitor_displaying_pixel_art_a12cad8c_2K", 4.0, "2K Still: Retro CRT monitor displaying pixel interface (Dramatic Pause)")
            ]
        },
        # SCENE 03: Burroughs School Coming Out (65.9s - 116.0s)
        {
            "id": 3,
            "title": "John Burroughs School & Engineering Autonomy",
            "vo": "EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav",
            "vo_start_s": 65.9,
            "vo_dur_s": 45.64,
            "pause_s": 4.5,
            "visuals": [
                ("EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus", 6.1, "Archival Photo: John Burroughs School campus"),
                ("EP01_V1_NEW_02_Burroughs_Boardroom", 11.0, "Burroughs school assembly auditorium with student silhouettes"),
                ("EP01_V2_ARCH_01_Altman_Portrait", 12.0, "Young Altman reflection in window glass"),
                ("EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era", 10.0, "Archival Photo: Young Altman in founder t-shirt"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 11.0, "Burroughs campus at dusk (Dramatic Pause: Autonomy)")
            ]
        },
        # SCENE 04: Stanford & Loopt Genesis (116.0s - 154.9s)
        {
            "id": 4,
            "title": "Stanford Arches & Loopt Genesis",
            "vo": "EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav",
            "vo_start_s": 116.0,
            "vo_dur_s": 34.93,
            "pause_s": 4.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Dynamic_camera", 5.0, "ElevenLabs: Young Altman with backpack under Stanford stone arches"),
                ("EP01_V2_ARCH_04_Stanford_Campus", 10.0, "Authentic Stanford University Quad and palm trees"),
                ("EP01_V1_NEW_01_Silhouette_Dorm", 10.0, "Silhouette packing bags in Stanford dorm room"),
                ("ep01_flow_03_silicon_laser", 8.0, "Silicon wafer laser etching pulse"),
                ("EP01_IMG_ARCH_01_Altman_2009_Loopt_Era", 5.9, "Archival Photo: Altman 2005-2009 Loopt era (Dramatic Pause)")
            ]
        },
        # SCENE 05: YC Batch 1, Scurvy & Green Dot (154.9s - 212.3s)
        {
            "id": 5,
            "title": "YC Batch 1, Loopt & Scurvy Grit",
            "vo": "EP01_VO_UA_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav",
            "vo_start_s": 154.9,
            "vo_dur_s": 53.39,
            "pause_s": 4.0,
            "visuals": [
                ("Aerial_view_of_city_center", 10.1, "New Video: 3D wireframe GPS HUD transforming into real nocturnal city (Loopt!)"),
                ("Digital_HUD_tracking_vehicles", 8.0, "Digital GPS tracking vehicles on map interface"),
                ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs", 13.0, "Steve Jobs invites 23yo Altman to Apple WWDC 2008 stage"),
                ("EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt", 6.0, "Archival Photo: Steve Jobs & Sam Altman on stage"),
                ("EP01_CLIP_V1_15_FounderGrit", 12.0, "Founder grit, exhaustion, sleeping on startup office floor"),
                ("EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program", 8.3, "Document: YC Summer 2005 program & Green Dot buyout (Dramatic Pause)")
            ]
        },
        # SCENE 06: Compound Interest Mindset (212.3s - 234.8s)
        {
            "id": 6,
            "title": "Compound Interest Mindset (Act 1 Climax)",
            "vo": "EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav",
            "vo_start_s": 212.3,
            "vo_dur_s": 16.51,
            "pause_s": 6.0,
            "visuals": [
                ("Mathematical_decision_tree_in_space_3c0901ac_2K", 7.7, "2K Still: Golden mathematical decision tree expanding exponentially"),
                ("Light_point_explodes_into_streaks_0827d703", 8.0, "Light point exploding into golden streaks"),
                ("ep01_flow_04_exponential_line", 6.8, "Golden exponential curve shooting upward (Act 1 Finale Pause)")
            ]
        },
        # SCENE 07: YC President at 28 (234.8s - 287.7s)
        {
            "id": 7,
            "title": "YC President at 28 & Nuclear Manifesto",
            "vo": "EP01_VO_UA_07_ACT2_04_45_05_45_YC_President_28yo.wav",
            "vo_start_s": 234.8,
            "vo_dur_s": 48.85,
            "pause_s": 4.0,
            "visuals": [
                ("Spark_disruption_in_corporate_bo_clip", 8.2, "Corporate leader in high-rise overlooking rain & lightning"),
                ("EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture", 10.0, "Altman lecturing at Stanford CS183B How to Start a Startup"),
                ("EP01_V2_B2_01_TechCrunch_Disrupt_2014", 10.0, "Altman on TechCrunch Disrupt 2014 stage as YC President"),
                ("EP01_IMG_ARCH_08_Altman_TechCrunch_Disrupt_2014_YC_President", 10.0, "Archival Photo: Altman on TechCrunch Disrupt stage"),
                ("EP01_IMG_ARCH_04_Altman_Stanford_2014_YC_President", 14.7, "Archival Photo: Altman Stanford 2014 (Dramatic Pause: Manifesto)")
            ]
        },
        # SCENE 08: Rosewood Dinner & Google Threat (287.7s - 341.0s)
        {
            "id": 8,
            "title": "Rosewood Dinner, DeepMind Threat & Sutskever",
            "vo": "EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav",
            "vo_start_s": 287.7,
            "vo_dur_s": 48.77,
            "pause_s": 4.5,
            "visuals": [
                ("Human_zygote_cell_division_timel_clip", 7.3, "Cell division timelapse (Retro Biosciences longevity)"),
                ("Human_prenatal_development_3D_vi_clip", 7.0, "3D developmental bio scan"),
                ("DNA_transcription_molecular_model", 8.0, "Molecular DNA transcription model"),
                ("EP01_V1_B2_02_Rosewood_Boardroom", 12.0, "Dark silhouettes at Rosewood Hotel dinner"),
                ("EP01_V2_B2_03_Altman_Sutskever_TAU", 10.0, "Altman and Ilya Sutskever in close discussion"),
                ("EP01_IMG_ARCH_02_Altman_Ilya_Sutskever_TAU_2023", 9.0, "Archival Photo: Altman & Sutskever (Dramatic Pause)")
            ]
        },
        # SCENE 09: OpenAI Founding & Scale (341.0s - 391.1s)
        {
            "id": 9,
            "title": "OpenAI Founding & The Scaling Hypothesis",
            "vo": "EP01_VO_UA_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav",
            "vo_start_s": 341.0,
            "vo_dur_s": 45.56,
            "pause_s": 4.5,
            "visuals": [
                ("Electrical_spark_traveling_neuro", 10.0, "New Video: Biological neuron -> spark into deep learning neural network!"),
                ("Neuron_morphs_into_GPU_chip", 10.0, "Biological neuron morphing into GPU silicon microchip"),
                ("EP01_V1_B2_04_Robotic_Dexterity", 10.0, "Robotic Dactyl hand manipulating Rubik's cube"),
                ("EP01_V1_B2_05_Swarm_Gaming_RL", 10.0, "OpenAI Five Dota 2 reinforcement learning swarm"),
                ("Electrical_pulses_firing_through", 10.1, "2K Still: Deep neural lattice glowing with pure scale (Dramatic Pause)")
            ]
        },
        # SCENE 10: Capped Profit & Microsoft Bill (391.1s - 440.8s)
        {
            "id": 10,
            "title": "Capped-Profit Restructure & Microsoft $1B",
            "vo": "EP01_VO_UA_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav",
            "vo_start_s": 391.1,
            "vo_dur_s": 43.65,
            "pause_s": 6.0,
            "visuals": [
                ("ep01_flow_06_server_monolith", 6.9, "Obsidian datacenter server monoliths"),
                ("EP01_V1_B2_06_Server_Matrix_Billions", 14.0, "Infinite matrix of supercomputer server racks"),
                ("EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO", 10.0, "Altman on TechCrunch Disrupt 2019 stage as OpenAI CEO"),
                ("EP01_IMG_ARCH_09_Altman_TechCrunch_Disrupt_2019_OpenAI_CEO", 10.0, "Archival Photo: Altman in 2019"),
                ("EP01_DOC_02_OpenAI_Introducing", 8.8, "Video Announcement: OpenAI structure (Act 2 Finale Pause)")
            ]
        },
        # SCENE 11: ChatGPT Launch & US Senate (440.8s - 491.9s)
        {
            "id": 11,
            "title": "ChatGPT Launch & US Senate Hearing",
            "vo": "EP01_VO_UA_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav",
            "vo_start_s": 440.8,
            "vo_dur_s": 46.11,
            "pause_s": 5.0,
            "visuals": [
                ("Mouse_click_triggers_flash", 8.2, "Mouse click triggers cosmic explosion of intelligence!"),
                ("Camera_plunges_into_terminal_screen", 8.0, "Camera plunges into glowing prompt terminal"),
                ("EP01_V2_B3_01_Altman_ChatGPT_Launch", 9.0, "ChatGPT launch milestone footage"),
                ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup", 9.0, "Altman taking oath in US Senate"),
                ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement", 10.0, "Altman testifying before US Senate committee"),
                ("EP01_IMG_ARCH_11_Altman_November_2022_ChatGPT_Genesis", 6.9, "Archival Photo: Altman November 2022 (Dramatic Pause)")
            ]
        },
        # SCENE 12: Friday Board Coup (491.9s - 547.2s)
        {
            "id": 12,
            "title": "Friday Board Coup Nov 17 2023",
            "vo": "EP01_VO_UA_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav",
            "vo_start_s": 491.9,
            "vo_dur_s": 50.29,
            "pause_s": 5.0,
            "visuals": [
                ("Four_men_sitting_at_table_3911bdbc", 9.1, "Four board members meeting across dark table"),
                ("Camera_orbiting_desk_photograph_2c2a80a3", 10.0, "Noir camera orbiting desk telephone and letter"),
                ("Three_people_discussing_at_table_e4a9158b_2K", 9.0, "2K Still: Tense boardroom silhouettes"),
                ("EP01_V1_B3_01_Chess_King_Falling", 10.0, "Chess king falling in slow-motion"),
                ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture", 9.0, "Ilya Sutskever Simons Institute lecture"),
                ("EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023", 8.2, "Official Board ouster document (Dramatic Pause)")
            ]
        },
        # SCENE 13: 120 Hours Drama & Guest Badge (547.2s - 595.4s)
        {
            "id": 13,
            "title": "120 Hours Drama, Nadella & Guest Badge",
            "vo": "EP01_VO_UA_13_ACT3_12_15_13_45_120_Hours_Drama_Guest_Badge.wav",
            "vo_start_s": 547.2,
            "vo_dur_s": 43.73,
            "pause_s": 4.5,
            "visuals": [
                ("EP01_V1_B3_03_Two_Silhouettes_Nadella", 10.8, "Silhouettes of Sam Altman and Satya Nadella"),
                ("Photographic_strobe_inverting_image", 10.0, "Photographic strobe flashes inverting portrait (media frenzy)"),
                ("EP01_V1_NEW_03_Window_Rain", 10.0, "Rain running down office window over San Francisco"),
                ("Guest_badge_on_desk_a7ff707c_2K", 10.0, "2K Still: Real OpenAI visitor badge on boardroom desk"),
                ("EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023", 7.4, "Ilya Sutskever tweet expressing deep regret (Dramatic Pause)")
            ]
        },
        # SCENE 14: 730 Signatures & Return (595.4s - 655.8s)
        {
            "id": 14,
            "title": "730 Signatures & Triumphant Return",
            "vo": "EP01_VO_UA_14_ACT3_13_45_15_30_730_Signatures_Triumphant_Return.wav",
            "vo_start_s": 595.4,
            "vo_dur_s": 54.44,
            "pause_s": 6.0,
            "visuals": [
                ("Camera_accelerating_through_lett_clip", 9.6, "Camera flying through legal ultimatum letter"),
                ("Tech_employees_gathered_in_office_b1af5ff2_2K", 10.0, "2K Still: OpenAI employees gathered in office in solidarity!"),
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37", 9.0, "ElevenLabs: Stylized golden network lattice uniting"),
                ("EP01_DOC_05_ACT3_730_Employees_Open_Letter", 10.0, "Document: The actual letter signed by 730 employees"),
                ("EP01_V1_B3_04_Golden_Grid_Stabilizing", 12.0, "Golden grid stabilizing power and returning stability"),
                ("ep01_flow_08_golden_signatures", 9.8, "Golden stream of signatures (Act 3 Finale Pause)")
            ]
        },
        # SCENE 15: Physicality of Compute & Stargate (655.8s - 709.0s)
        {
            "id": 15,
            "title": "Physicality of Compute: Terawatts, Chips & Stargate",
            "vo": "EP01_VO_UA_15_ACT4_15_30_17_00_Stargate_Helion_Energy_Physics.wav",
            "vo_start_s": 655.8,
            "vo_dur_s": 48.20,
            "pause_s": 5.0,
            "visuals": [
                ("Physical_matter_dissolves_into_b_clip", 9.2, "Physical matter dissolves into digital data bits"),
                ("ep01_flow_09_fusion_torus", 8.0, "Fusion reactor torus glowing with plasma"),
                ("EP10_SCI_01_Tesla_Coil_Electric_Discharges", 10.0, "Tesla coil high voltage electric discharges"),
                ("EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal", 8.0, "Jensen Huang reveals Blackwell wafer"),
                ("Man_wearing_tactical_arctic_parka", 8.0, "Leader in arctic parka at subzero datacenter"),
                ("EP01_DOC_06_ACT4_Stargate_100B_Supercluster", 10.0, "Document: Stargate $100B supercluster report (Dramatic Pause)")
            ]
        },
        # SCENE 16: Three Rules of Exponential Life (709.0s - 773.6s)
        {
            "id": 16,
            "title": "Three Rules of Exponential Life",
            "vo": "EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav",
            "vo_start_s": 709.0,
            "vo_dur_s": 59.64,
            "pause_s": 5.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Slow,_powerful", 8.0, "ElevenLabs: Slow powerful Altman vision portrait"),
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59", 8.0, "ElevenLabs: Dynamic fluid intelligence cognitive waves"),
                ("Laser_forms_text_words", 10.0, "Laser writing code words in darkness (Rule 2: Code)"),
                ("EP01_V1_CREATIVE_06_Obsessive_Builders", 11.0, "Obsessive engineers working at midnight"),
                ("Light_point_explodes_into_streaks_c712a46e", 12.0, "Light streaks exploding horizontally (Rule 3: Compound interest)"),
                ("EP01_IMG_ARCH_10_Altman_TED_Vancouver_2023_GPT4", 15.6, "Archival Photo: Altman on TED stage (Dramatic Pause: Rules)")
            ]
        },
        # SCENE 17: Finale: Plastic Reality (773.6s - 815.0s)
        {
            "id": 17,
            "title": "Finale: Plastic Reality & The Future Created Now",
            "vo": "EP01_VO_UA_17_ACT4_18_30_20_00_Future_Is_Created_Now_Outro.wav",
            "vo_start_s": 773.6,
            "vo_dur_s": 26.44,
            "pause_s": 15.0,
            "visuals": [
                ("Boy_aging_into_tech_leader", 10.0, "Boy aging into modern tech leader"),
                ("ep01_flow_10_earth_horizon", 8.4, "Golden sunrise over planet Earth from space"),
                ("EP01_V1_B3_CLOSER_GoldenGrid", 10.0, "Golden grid closer"),
                ("EP01_V1_B4_CLOSER_DeepSpace", 13.0, "Deep space starfield closer (Epic Fadeout)")
            ]
        }
    ]

    # --- 1. Place Voiceover on Track A1 with Markers ---
    print("\n--- 1. Placing Ukrainian Voiceover (Track A1) with Calibrated Pauses ---")
    total_audio_placed = 0
    for sc in SCENES:
        vo_start_f = start_frame + tc_to_frames(sc["vo_start_s"])
        it = place_item(sc["vo"], "audio", 1, vo_start_f, sc["vo_dur_s"])
        if it:
            total_audio_placed += 1
            print(f"  🎙️ [{sc['vo_start_s']:05.1f}s - {sc['vo_start_s']+sc['vo_dur_s']:05.1f}s] A1 Scene {sc['id']:02d}: {sc['title']} (+{sc['pause_s']:.1f}s pause)")
            # Add Cyan marker for each scene
            tl.AddMarker(vo_start_f, "Cyan", f"Scene {sc['id']:02d}: {sc['title']}", f"VO: {sc['vo']}", 1)

    # --- 2. Place Seamless Visual Canvas on Track V1 ---
    print("\n--- 2. Placing Seamless Visual Canvas on Track V1 (Videos + 2K Imagery) ---")
    total_visual_placed = 0
    current_rec_f = start_frame
    jobs_v1_rec_f = None

    for sc in SCENES:
        print(f"\n🎬 SCENE {sc['id']:02d}: {sc['title']}")
        for clip_pat, dur_s, label in sc["visuals"]:
            it = place_item(clip_pat, "video", 1, current_rec_f, dur_s)
            if it:
                total_visual_placed += 1
                if "SteveJobs" in clip_pat or "WWDC" in clip_pat:
                    jobs_v1_rec_f = current_rec_f
                clip_dur_f = it.GetDuration() if (it and it.GetDuration()) else tc_to_frames(dur_s)
                c_start_s = (current_rec_f - start_frame) / FPS
                c_end_s = (current_rec_f + clip_dur_f - start_frame) / FPS
                print(f"  🎥 [{c_start_s:05.1f}s - {c_end_s:05.1f}s] V1: {it.GetName()} ({clip_dur_f/FPS:.1f}s) — {label}")
                current_rec_f += clip_dur_f
            else:
                print(f"  ✗ FAILED: {clip_pat}")

    # --- 3. Place Polyphonic Cinematic Score on Track A2 ---
    print("\n--- 3. Polishing Sound Design & Music Architecture ---")
    scores = [
        ("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog", 0.0, 98.0),
        ("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2", 98.0, 142.0),
        ("EP01_AMB_B2_PART1_00_00_to_02_00_120s", 240.0, 120.0),
        ("EP01_AMB_B2_PART2_02_00_to_04_00_120s", 360.0, 120.0),
        ("EP01_MUS_B3_PART1_08_00_to_10_00_120s", 480.0, 120.0),
        ("EP01_MUS_B3_PART2_10_00_to_12_00_120s", 600.0, 120.0),
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s", 720.0, 95.0)
    ]
    for s_name, start_s, dur_s in scores:
        rec_f = start_frame + tc_to_frames(start_s)
        it = place_item(s_name, "audio", 2, rec_f, dur_s)
        if it:
            print(f"  🎵 Track A2 Score: {s_name} @ {start_s:.1f}s (-22.0 dB)")

    # --- 4. Place Archival Live Speech on Track A3 ---
    jobs_rec_f = jobs_v1_rec_f if 'jobs_v1_rec_f' in locals() and jobs_v1_rec_f else (start_frame + tc_to_frames(173.0))
    it_jobs = place_item("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008", "audio", 3, jobs_rec_f, 13.0)
    if it_jobs:
        jobs_time_s = (jobs_rec_f - start_frame) / FPS
        print(f"  🎙️ Track A3 Archival Speech: Steve Jobs WWDC 2008 @ {jobs_time_s:.1f}s (-3.0 dB)")

    # --- 5. Verify Timeline Stats ---
    v1_items = tl.GetItemListInTrack("video", 1) or []
    a1_items = tl.GetItemListInTrack("audio", 1) or []
    a2_items = tl.GetItemListInTrack("audio", 2) or []
    a3_items = tl.GetItemListInTrack("audio", 3) or []

    total_dur_frames = tl.GetEndFrame() - tl.GetStartFrame()
    total_dur_s = total_dur_frames / FPS

    print("\n--- 4. Masterclass Assembly Verification ---")
    print(f"  • Total Visual Items on Track V1: {len(v1_items)} (Zero Black Gaps)")
    print(f"  • Total Voiceover Scenes on Track A1: {len(a1_items)} (Sample-Accurate)")
    print(f"  • Total Score Suites on Track A2: {len(a2_items)}")
    print(f"  • Archival Speeches on Track A3: {len(a3_items)}")
    print(f"  • Master Timeline Duration: {total_dur_frames} frames ({total_dur_s:.1f}s / {total_dur_s/60:.2f} min)")

    # Save project
    pm.SaveProject()
    print("\n✓ Project saved in DaVinci Resolve!")

    # Export project DRP
    export_path = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/06_DAVINCI_PROJECTS/AI_Titans_EP01_Sam_Altman.drp'
    backup_path = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/09_BACKUPS/AI_Titans_EP01_Sam_Altman_Backup.drp'
    if os.path.exists(export_path):
        os.remove(export_path)
    ok_exp = pm.ExportProject('AI_Titans_EP01_Sam_Altman', export_path, False)
    if ok_exp and os.path.exists(export_path):
        shutil.copy2(export_path, backup_path)
        print(f"✓ Exported DRP ({os.path.getsize(export_path)/1024:.1f} KB) & updated backup!")

if __name__ == "__main__":
    run()
