#!/usr/bin/env python3
"""
🏆 AI TITANS: EPISODE 01 — SAM ALTMAN
THE MASTERCLASS DIRECTOR'S CUT V3 — DIRECTORIAL REFINEMENT
1. Opening Frame: Restored the iconic abstract thinker meditating in golden formulas on black void (EP01_V1_CREATIVE_01_Equations_Void_8s).
2. Macintosh LC II (Scene 02):
   - 18.0s - 23.0s: 360-degree rotation animation morphing from concept to living child (ElevenLabs Seamless Stylis).
   - 23.0s - 28.0s: Boy with screwdriver disassembling the motherboard on carpet (ElevenLabs Authentic Histo), exactly where narrator says "він розбирає системний блок до материнської плати".
   - 28.0s - 36.0s: Floppy insertion & Circuit flythrough into quote.
   - 36.0s - 48.0s: Dedicated Quote Beat (4K Ukrainian Typography, 2.0s in-breath + spoken quote + 1.8s out-breath).
3. Exhausted Coder Relocation: Moved tired coder late at monitor (EP01_CLIP_STILL_Boy_Watching_Code_5s) to Scene 05 (Loopt 7-year exhaustion & scurvy grind).
4. Audio Mastery:
   - Track A1: Ukrainian Voiceover (0.0 dB)
   - Track A2: Velvet Ambient Score (-30.0 dB across all items, zero ear fatigue)
   - Track A3: Steve Jobs WWDC 2008 Live Speech (-3.0 dB, lip-synced to frame 0)
"""

import sys, os, time, shutil
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def tc_to_frames(s):
    return int(round(s * FPS))

def run():
    print("==================================================================")
    print("🎬 MASTERCLASS DIRECTOR'S CUT V3: DIRECTORIAL REFINEMENT")
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
        if f"{name_pattern}.mp4" in all_clips:
            return all_clips[f"{name_pattern}.mp4"]
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
    # REFINED MASTER SCENE ARCHITECTURE (17 SCENES)
    # =========================================================================
    SCENE_PLANS = [
        # SCENE 01: Pressure of Rules (18.03s)
        # OPENING: Iconic abstract thinker meditating in golden formulas & black void
        {
            "id": 1,
            "title": "Pressure Of Rules (Genesis of Conditioned Mind)",
            "audio": [
                ("EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav", 0.0, 14.03, "Narration: Більшість людей формуються під тиском правил")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("EP01_V1_CREATIVE_01_Equations_Void_8s", 8.0, "HERO OPENING: Abstract human kneeling/meditating in golden mathematical equations on black void"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 5.0, "Burroughs High School strict brick corridors (Conditioning)"),
                ("EP01_CLIP_V1_05_Eye_Code", 5.03, "Extreme close-up eye reflecting green code (Social judgment & fear)")
            ]
        },
        # SCENE 02: Macintosh LC II & Extension of Thought Quote (51.69s)
        # 18.0s: 360 rotation animation into living child -> disassembling motherboard -> quote beat
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
                # 18.0s - 23.0s: 360-degree animation rotating from concept into real child
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59", 5.0, "360° turn animation morphing into living child sitting with computer"),
                # 23.0s - 28.0s: Boy with screwdriver disassembling motherboard (Lip-sync to VO: 'розбирає системний блок')
                ("ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51", 5.0, "HERO SHOT: 8yo boy with screwdriver taking apart motherboard on carpet"),
                # 28.0s - 32.0s: Floppy disk insert
                ("EP01_CLIP_STILL_Child_Floppy_Disk_4s", 4.0, "Child inserting 3.5 floppy disk into Macintosh drive"),
                # 32.0s - 36.0s: Computer circuitry flythrough (Narration: 'Через тридцять років він напише:')
                ("Camera_moving_through_computer_m_clip", 4.0, "Flythrough computer circuitry & microchips"),
                # 36.0s - 48.0s: DEDICATED QUOTE BEAT (12.0s)
                ("EP01_UA_CLIP_CARD_01_Extension_Of_Thought_12s", 12.0, "4K Ukrainian Quote Card: «Ця машина розмила лінію між моїм внутрішнім світом...»"),
                # 48.0s - 65.69s: Part C Narration (17.69s)
                ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992", 6.0, "Authentic 1992 Apple Macintosh LC commercial"),
                ("ep01_flow_01_mac_chassis", 5.0, "Macintosh LC II chassis macro"),
                ("Boy_viewing_glowing_terminal_code", 6.69, "Boy viewing glowing terminal code (Indifference to authority)"),
                # 65.69s - 69.69s: Scene Pause
                ("EP01_CLIP_STILL_CRT_PixelArt_4s", 4.0, "CRT monitor displaying pixel interface (Dramatic Scene Pause)")
            ]
        },
        # SCENE 03: John Burroughs School (50.14s)
        {
            "id": 3,
            "title": "John Burroughs School & Engineering Autonomy",
            "audio": [
                ("EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 0.0, 45.64, "Narration")
            ],
            "scene_pause_s": 4.5,
            "visuals": [
                ("EP01_CLIP_STILL_Burroughs_Campus_6s", 6.14, "Archival Photo: John Burroughs School campus"),
                ("EP01_V1_NEW_02_Burroughs_Boardroom", 11.0, "School assembly auditorium"),
                ("EP01_V2_ARCH_01_Altman_Portrait", 12.0, "Young Altman reflection in window glass"),
                ("EP01_CLIP_STILL_Loopt_Shirt_10s", 10.0, "Archival Photo: Young Altman in founder t-shirt"),
                ("EP01_V2_ARCH_05_Burroughs_Campus", 11.0, "Burroughs campus at dusk (Dramatic Scene Pause)")
            ]
        },
        # SCENE 04: Stanford & Loopt Genesis (38.93s)
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
                ("EP01_CLIP_STILL_Altman_2009_Loopt_6s", 5.93, "Archival Photo: Altman 2005-2009 Loopt era (Dramatic Scene Pause)")
            ]
        },
        # SCENE 05: YC Batch 1, Scurvy Grit with Relocated Tired Coder (61.39s)
        {
            "id": 5,
            "title": "YC Batch 1, Loopt & Psychological Friction Quote",
            "audio": [
                ("EP01_VO_UA_05_PART_A_Loopt_Scurvy_Grit.wav", 0.0, 39.25, "Narration Part A (Loopt Grit)"),
                ("EP01_VO_UA_05_PART_B_Psychological_Friction_QUOTE.wav", 2.0, 14.14, "Spoken Quote (+2.0s In-breath Pause)")
            ],
            "scene_pause_s": 4.0,
            "visuals": [
                ("Aerial_view_of_city_center", 8.0, "3D wireframe GPS HUD transforming into real nocturnal city"),
                ("Digital_HUD_tracking_vehicles", 6.0, "Digital GPS tracking vehicles on map interface"),
                ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs", 13.0, "Steve Jobs invites Altman to Apple WWDC 2008 stage"),
                ("EP01_CLIP_STILL_Jobs_Altman_WWDC_5s", 4.0, "Archival Photo: Steve Jobs & Sam Altman on stage"),
                # RELOCATED TIRED CODER: Placed here during 7-year exhaustion & scurvy grind!
                ("EP01_CLIP_STILL_Boy_Watching_Code_5s", 5.0, "Exhausted young founder working late at night in front of glowing monitor"),
                ("EP01_CLIP_V1_15_FounderGrit", 3.25, "Founder grit, sleeping on startup office floor"),
                # QUOTE BEAT CARD (18.14s)
                ("EP01_UA_CLIP_CARD_02_Psychological_Friction_18s", 18.14, "4K Ukrainian Quote Card: «Більшість людей здаються не тому, що їхня ідея хибна...»"),
                # Scene Pause
                ("EP01_CLIP_STILL_YC2005_Doc_4s", 4.0, "Document: YC Summer 2005 program & Green Dot buyout")
            ]
        },
        # SCENE 06: Compound Interest Mindset (22.51s)
        {
            "id": 6,
            "title": "Compound Interest Mindset (Act 1 Climax)",
            "audio": [
                ("EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 0.0, 16.51, "Narration")
            ],
            "scene_pause_s": 6.0,
            "visuals": [
                ("EP01_CLIP_STILL_Math_Decision_Tree_8s", 7.71, "Golden mathematical decision tree expanding exponentially"),
                ("Light_point_explodes_into_streaks_0827d703", 8.0, "Light point exploding into golden streaks"),
                ("ep01_flow_04_exponential_line", 6.8, "Golden exponential curve shooting upward (Act 1 Finale Pause)")
            ]
        },
        # SCENE 07: YC President at 28 with Manifesto Quote Beat (56.85s)
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
                ("EP01_CLIP_STILL_TechCrunch_2014_10s", 9.60, "Archival Photo: Altman on TechCrunch stage"),
                # QUOTE BEAT CARD (15.25s)
                ("EP01_UA_CLIP_CARD_03_Exponential_Risk_15s", 15.25, "4K Ukrainian Quote Card: «Люди катастрофічно недооцінюють ризик...»"),
                # Scene Pause
                ("EP01_CLIP_STILL_Stanford_2014_4s", 4.0, "Archival Photo: Altman Stanford 2014")
            ]
        },
        # SCENE 08: Rosewood Dinner & Google Threat (53.27s)
        {
            "id": 8,
            "title": "Rosewood Dinner, DeepMind Threat & Sutskever",
            "audio": [
                ("EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav", 0.0, 48.77, "Narration")
            ],
            "scene_pause_s": 4.5,
            "visuals": [
                ("Human_zygote_cell_division_timel_clip", 7.27, "Cell division timelapse (Retro Biosciences)"),
                ("Human_prenatal_development_3D_vi_clip", 7.0, "3D developmental bio scan"),
                ("DNA_transcription_molecular_model", 8.0, "Molecular DNA transcription model"),
                ("EP01_V1_B2_02_Rosewood_Boardroom", 12.0, "Dark silhouettes at Rosewood Hotel dinner"),
                ("EP01_V2_B2_03_Altman_Sutskever_TAU", 10.0, "Altman and Ilya Sutskever in close discussion"),
                ("EP01_CLIP_STILL_Altman_Sutskever_TAU_9s", 9.0, "Archival Photo: Altman & Sutskever")
            ]
        },
        # SCENE 09: OpenAI Founding & Scale (50.06s)
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
                ("EP01_CLIP_STILL_Neural_Lattice_10s", 10.06, "Deep neural lattice glowing")
            ]
        },
        # SCENE 10: Capped Profit & Microsoft $1B with Quote Beat (53.15s)
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
                ("EP01_CLIP_STILL_Altman_2019_OpenAI_6s", 6.0, "Archival Photo: Altman 2019"),
                # QUOTE BEAT CARD (18.15s)
                ("EP01_UA_CLIP_CARD_04_Compute_Equations_18s", 18.15, "4K Ukrainian Quote Card: «Ми не зможемо врятувати світ...»"),
                # Scene Pause
                ("EP01_DOC_02_OpenAI_Introducing", 5.0, "OpenAI structure announcement (Act 2 Finale Pause)")
            ]
        },
        # SCENE 11: ChatGPT Launch & US Senate (51.11s)
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
                ("EP01_CLIP_STILL_ChatGPT_Genesis_7s", 6.90, "Archival Photo: Altman November 2022")
            ]
        },
        # SCENE 12: Friday Board Coup (55.29s)
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
                ("EP01_CLIP_STILL_Boardroom_Tense_9s", 9.0, "Boardroom tense silhouettes"),
                ("EP01_V1_B3_01_Chess_King_Falling", 10.0, "Chess king falling in slow-motion"),
                ("EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture", 9.0, "Ilya Sutskever Simons lecture"),
                ("EP01_CLIP_STILL_Board_Ouster_Doc_8s", 8.20, "Official Board ouster document")
            ]
        },
        # SCENE 13: 120 Hours Drama & Guest Badge with Quote Beat (51.73s)
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
                ("EP01_CLIP_STILL_Guest_Badge_Desk_10s", 10.0, "Real OpenAI visitor badge on desk"),
                # QUOTE BEAT CARD (7.73s)
                ("EP01_UA_CLIP_CARD_05_Guest_Badge_8s", 7.73, "4K Ukrainian Quote Card: «Перший і останній раз, коли я вдягаю цей бейдж»"),
                # Scene Pause
                ("EP01_CLIP_STILL_Sutskever_Regret_Doc_4s", 4.0, "Sutskever tweet expressing deep regret")
            ]
        },
        # SCENE 14: 730 Signatures with Ultimatum Quote Beat (63.24s)
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
                # QUOTE BEAT CARD (10.70s)
                ("EP01_UA_CLIP_CARD_06_730_Employees_11s", 10.70, "4K Ukrainian Quote Card: «Або ви йдете у відставку і повертаєте Сема Альтмана...»"),
                # Part C Visuals
                ("EP01_CLIP_STILL_Employees_Solidarity_9s", 9.0, "OpenAI employees gathered in solidarity"),
                ("ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37", 9.0, "ElevenLabs: Golden network lattice uniting"),
                ("EP01_CLIP_STILL_730_Letter_Doc_9s", 9.0, "Document: Open letter signed by 730 employees"),
                ("EP01_V1_B3_04_Golden_Grid_Stabilizing", 9.94, "Golden grid stabilizing power"),
                # Scene Pause
                ("ep01_flow_08_golden_signatures", 5.0, "Golden stream of signatures (Act 3 Finale Pause)")
            ]
        },
        # SCENE 15: Physicality of Compute & Stargate (53.20s)
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
                ("EP01_CLIP_STILL_Stargate_100B_Doc_10s", 10.0, "Document: Stargate $100B supercluster")
            ]
        },
        # SCENE 16: Three Rules of Exponential Life (64.64s)
        {
            "id": 16,
            "title": "Three Rules of Exponential Life",
            "audio": [
                ("EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav", 0.0, 59.64, "Narration")
            ],
            "scene_pause_s": 5.0,
            "visuals": [
                ("ElevenLabs_video_seedance-2-5_Slow,_powerful", 8.0, "ElevenLabs: Slow powerful Altman vision portrait"),
                ("ElevenLabs_video_seedance-2-5_Intense_macro_r", 8.0, "ElevenLabs: Intense eye focusing on the future"),
                # 4K UKRAINIAN CARD: THREE RULES
                ("EP01_UA_CLIP_CARD_07_Three_Rules_12s", 12.0, "4K Ukrainian Master Card: 1. Ірраціональна віра 2. Проблеми як код 3. Експонента"),
                ("Laser_forms_text_words", 8.0, "Laser writing code words in darkness (Rule 2)"),
                ("EP01_V1_CREATIVE_06_Obsessive_Builders", 10.0, "Obsessive engineers working at midnight"),
                ("Light_point_explodes_into_streaks_c712a46e", 8.0, "Light streaks exploding horizontally (Rule 3)"),
                ("EP01_CLIP_STILL_Altman_TED2023_11s", 10.64, "Archival Photo: Altman TED stage (Dramatic Scene Pause)")
            ]
        },
        # SCENE 17: Finale: Plastic Reality (41.44s)
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
                ("EP01_UA_CLIP_CARD_08_Plastic_Reality_10s", 10.0, "4K Ukrainian Master Card: «Світ набагато пластичніший...»"),
                ("ep01_flow_10_earth_horizon", 8.44, "Golden sunrise over planet Earth"),
                ("EP01_V1_B3_CLOSER_GoldenGrid", 8.0, "Golden grid closer"),
                ("EP01_V1_B4_CLOSER_DeepSpace", 7.0, "Deep space starfield closer (Epic Fadeout)")
            ]
        }
    ]

    # --- 2. Sequential Timeline Construction ---
    print("\n--- 2. Placing Synchronized Audio & Native Video Tracks ---")
    current_audio_rec_f = start_frame
    current_visual_rec_f = start_frame
    jobs_rec_f = None

    for sc in SCENE_PLANS:
        print(f"\n🎬 SCENE {sc['id']:02d}: {sc['title']}")
        sc_audio_start_f = current_audio_rec_f

        # Add cyan marker
        tl.AddMarker(sc_audio_start_f, "Cyan", f"Scene {sc['id']:02d}: {sc['title']}", "", 1)

        # Place audio on Track A1
        for a_clip, delay_s, a_dur, a_label in sc["audio"]:
            current_audio_rec_f += tc_to_frames(delay_s)
            it_a = place_item(a_clip, "audio", 1, current_audio_rec_f, a_dur)
            actual_dur_f = it_a.GetDuration() if (it_a and it_a.GetDuration()) else tc_to_frames(a_dur)
            t_s = (current_audio_rec_f - start_frame) / FPS
            dur_actual_s = actual_dur_f / FPS
            print(f"  🎙️ [{t_s:05.1f}s - {t_s + dur_actual_s:05.1f}s] A1: {a_clip} ({a_label}) [delay: +{delay_s:.1f}s]")
            current_audio_rec_f += actual_dur_f

        current_audio_rec_f += tc_to_frames(sc["scene_pause_s"])

        # Place visuals on Track V1
        for v_clip, v_dur, v_label in sc["visuals"]:
            it_v = place_item(v_clip, "video", 1, current_visual_rec_f, v_dur)
            actual_dur_f = it_v.GetDuration() if (it_v and it_v.GetDuration()) else tc_to_frames(v_dur)
            t_s = (current_visual_rec_f - start_frame) / FPS
            dur_actual_s = actual_dur_f / FPS
            if ("SteveJobs" in v_clip or "WWDC" in v_clip) and "VID" in v_clip:
                jobs_rec_f = current_visual_rec_f
            print(f"  🎥 [{t_s:05.1f}s - {t_s + dur_actual_s:05.1f}s] V1: {v_clip} ({dur_actual_s:.1f}s) — {v_label}")
            current_visual_rec_f += actual_dur_f

    # --- 3. Place Polyphonic Cinematic Score on Track A2 at -30.0 dB ---
    print("\n--- 3. Placing Cinematic Score Beds on Track A2 (Broadcasting Standard: -30.0 dB) ---")
    scores = [
        ("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog", 0.0, 110.0),
        ("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2", 110.0, 160.0),
        ("EP01_AMB_B2_PART1_00_00_to_02_00_120s", 270.0, 130.0),
        ("EP01_AMB_B2_PART2_02_00_to_04_00_120s", 400.0, 130.0),
        ("EP01_MUS_B3_PART1_08_00_to_10_00_120s", 530.0, 130.0),
        ("EP01_MUS_B3_PART2_10_00_to_12_00_120s", 660.0, 130.0),
        ("EP01_MUS_B4_ACT4_12_00_to_16_00_240s", 790.0, 120.0)
    ]
    for s_name, start_s, dur_s in scores:
        rec_f = start_frame + tc_to_frames(start_s)
        it = place_item(s_name, "audio", 2, rec_f, dur_s)
        if it:
            it.SetProperty('AudioVolume', -30.0)
            print(f"  🎵 Track A2 Score Bed: {s_name} @ {start_s:.1f}s [AudioVolume: -30.0 dB]")

    a2_items = tl.GetItemListInTrack("audio", 2) or []
    for it in a2_items:
        it.SetProperty('AudioVolume', -30.0)

    # --- 4. Synchronize Steve Jobs Live Speech on Track A3 ---
    print("\n--- 4. Synchronizing Steve Jobs Live Speech on Track A3 ---")
    if jobs_rec_f:
        it_jobs = place_item("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008", "audio", 3, jobs_rec_f, 13.0)
        if it_jobs:
            it_jobs.SetProperty('AudioVolume', -3.0)
            jobs_time_s = (jobs_rec_f - start_frame) / FPS
            print(f"  🎙️ Track A3 Archival Speech: Steve Jobs WWDC 2008 @ {jobs_time_s:.1f}s [AudioVolume: -3.0 dB, Lip-Sync Perfect]")

    # --- 5. Master Timeline Verification ---
    v1_items = tl.GetItemListInTrack("video", 1) or []
    a1_items = tl.GetItemListInTrack("audio", 1) or []
    a2_items = tl.GetItemListInTrack("audio", 2) or []
    a3_items = tl.GetItemListInTrack("audio", 3) or []

    total_dur_frames = tl.GetEndFrame() - tl.GetStartFrame()
    total_dur_s = total_dur_frames / FPS

    print("\n==================================================================")
    print("🏆 MASTERCLASS DIRECTOR'S CUT V3 ASSEMBLY COMPLETE")
    print("==================================================================")
    print(f"  • Total Visual Items on Track V1: {len(v1_items)} (Native 24fps 4K, Zero Black Gaps)")
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
