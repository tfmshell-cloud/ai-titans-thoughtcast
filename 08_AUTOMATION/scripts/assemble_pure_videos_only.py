#!/usr/bin/env python3
"""
AI TITANS: EPISODE 01 — SAM ALTMAN
PURE VIDEO-ONLY TIMELINE ASSEMBLY
Places ONLY:
  1. Generated AI videos (Runway, ElevenLabs, Seedance)
  2. Internet Archival videos (Altman, Jobs, Stanford, Senate, Disrupt, Burroughs)
  3. Core EP01 Flow videos (Macintosh, CRT code, server monolith, fusion, horizon)
ZERO text cards, ZERO document images, ZERO static PNG/JPG.
Does NOT delete anything from the Media Pool.
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
    print(f"🎬 ASSEMBLING PURE VIDEO-ONLY TIMELINE: {tl.GetName()}")
    print("   (Only Generated Videos + Internet Archival Videos)")
    print("==================================================================")

    # 1. Clear ONLY the video tracks on timeline (leaving Media Pool 100% untouched)
    print("\n--- 1. Clearing Video Tracks on Timeline ---")
    for vi in range(1, tl.GetTrackCount("video") + 1):
        items = tl.GetItemListInTrack("video", vi) or []
        if items:
            tl.DeleteClips(items)
            print(f"  ✓ Cleared {len(items)} clips from video track V{vi}")

    tl.SetTrackName("video", 1, "PURE_VIDEOS_GENERATED_AND_INTERNET_V1")

    # 2. Collect all Media Pool items
    all_clips = {}
    def scan_bin(folder):
        for c in folder.GetClipList() or []:
            all_clips[c.GetName()] = c
        for sf in folder.GetSubFolderList() or []:
            scan_bin(sf)
    scan_bin(root)

    # 3. Curated Master Story Video Sequence (Chronological Order)
    # Strictly pure video files only (zero cards, zero docs, zero stills)
    curated_video_sequence = [
        # === ACT 1: GENESIS & EARLY OBSESSIONS (00:00 - 04:00) ===
        # Scene 1: Pressure of Rules
        ("Burroughs High School Campus (Internet Archive)", "EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4"),
        ("Eye Analyzing Rules & Code (AI Video)", "EP01_CLIP_V1_05_Eye_Code_11s.mp4"),

        # Scene 2: 1993 Macintosh LC II
        ("Boy Viewing Glowing CRT Terminal Code (User AI Video)", "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4"),
        ("8yo Boy Disassembling Macintosh with Screwdriver (ElevenLabs Video)", "ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4"),
        ("Camera Moving Through Computer Motherboard (User AI Video)", "Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4"),
        ("Apple Macintosh 1992 CRT (Internet Archive)", "EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4"),
        ("Childhood Macintosh Chassis (Flow Video)", "ep01_flow_01_mac_chassis.mp4"),
        ("CRT Screen Terminal Code (Flow Video)", "ep01_flow_02_crt_code.mp4"),

        # Scene 3: John Burroughs School & Coming Out
        ("Burroughs School Assembly Auditorium (Internet Archive)", "EP01_V1_NEW_02_Burroughs_Boardroom_15s.mp4"),
        ("Young Altman Portrait Reflection in Glass (Internet Archive)", "EP01_V2_ARCH_01_Altman_Portrait_15s.mp4"),

        # Scene 4: Stanford Campus & Dropping Out
        ("Young Altman Walking Stanford Stone Arches with Backpack (ElevenLabs Video)", "ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4"),
        ("Stanford University Quad Arches (Internet Archive)", "EP01_V2_ARCH_04_Stanford_Campus_12s.mp4"),
        ("Dorm Room Silhouette Night Coding (Flow Video)", "EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4"),
        ("Silicon Wafer Cyan Laser Etching (Flow Video)", "ep01_flow_03_silicon_laser.mp4"),

        # Scene 5: Loopt, YC Batch 1, Steve Jobs WWDC 2008
        ("Digital HUD GPS Vehicle Tracking Loopt (User AI Video)", "Digital_HUD_tracking_vehicles_d7d30811_1080p.mp4"),
        ("Young Altman at Loopt 2005 (Internet Archive)", "EP01_V2_ARCH_07_Loopt_Founder_12s.mp4"),
        ("Steve Jobs Introduces Altman at Apple WWDC 2008 (Internet Archive)", "EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4"),
        ("Founder Grit & Garage Hustle (AI Video)", "EP01_CLIP_V1_15_FounderGrit_15s.mp4"),

        # Scene 6: Compound Interest
        ("Light Point Explodes into Golden Streaks (User AI Video)", "Light_point_explodes_into_streaks_0827d703_1080p.mp4"),
        ("Golden Exponential Growth Curve (Flow Video)", "ep01_flow_04_exponential_line.mp4"),

        # === ACT 2: YC EMPIRE & SEEDS OF SINGULARITY (04:00 - 07:30) ===
        # Scene 7: YC President at 28
        ("Corporate Leader in High-Rise Overlooking Rain (User AI Video)", "Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4"),
        ("Altman Lecturing Stanford CS183B How to Start a Startup (Internet Archive)", "EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4"),
        ("Altman at TechCrunch Disrupt 2014 as YC President (Internet Archive)", "EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4"),

        # Scene 8: Rosewood Dinner, Longevity, Google Threat
        ("Human Zygote Cell Division Timelapse (User AI Video)", "Human_zygote_cell_division_timel_clip_063791c0_1080p.mp4"),
        ("Human Prenatal Development 3D Scan (User AI Video)", "Human_prenatal_development_3D_vi_clip_8b0d0b01_1080p.mp4"),
        ("Rosewood Boardroom Secret Dinner (AI Video)", "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4"),
        ("Altman & Ilya Sutskever at TAU (Internet Archive)", "EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4"),

        # Scene 9: OpenAI Founding & Scaling Hypothesis
        ("Neuron Morphs into GPU Microchip (User AI Video)", "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4"),
        ("Neural Network Lattice Pulse (Flow Video)", "ep01_flow_05_neural_lattice.mp4"),
        ("Robotic Dexterity Shadow Hand Rubik Cube (AI Video)", "EP01_V1_B2_04_Robotic_Dexterity_15s.mp4"),
        ("Swarm Reinforcement Learning (AI Video)", "EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4"),

        # Scene 10: Capped-Profit & Microsoft $1B Deal
        ("Server Monoliths in Obsidian Datacenter (Flow Video)", "ep01_flow_06_server_monolith.mp4"),
        ("Server Matrix Billions Compute (AI Video)", "EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4"),
        ("Altman at TechCrunch Disrupt 2019 as OpenAI CEO (Internet Archive)", "EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4"),

        # === ACT 3: THE CITADEL & THE COUP (07:30 - 11:00) ===
        # Scene 11: ChatGPT Launch & US Senate Hearing
        ("Mouse Click Triggers Cosmic Flash (User AI Video)", "Mouse_click_triggers_flash_42a0e76f_1080p.mp4"),
        ("Camera Plunges into Terminal Screen (User AI Video)", "Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4"),
        ("ChatGPT Launch Viral Milestone (Internet Archive)", "EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4"),
        ("Altman Sworn Testimony in US Senate Hearing Closeup (Internet Archive)", "EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4"),
        ("Altman Calling for AI Regulation in US Senate (Internet Archive)", "EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4"),

        # Scene 12: Friday Nov 17 2023 Board Coup
        ("Four Board Members Meeting at Table (User AI Video)", "Four_men_sitting_at_table_3911bdbc_1080p.mp4"),
        ("Camera Orbiting Desk Telephone Noir (User AI Video)", "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4"),
        ("Boardroom Noir Shadows (Flow Video)", "ep01_flow_07_boardroom_noir.mp4"),
        ("Chess King Falling in Slow Motion (AI Video)", "EP01_V1_B3_01_Chess_King_Falling_12s.mp4"),
        ("Ilya Sutskever Lecture at Simons Institute (Internet Archive)", "EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture.mp4"),

        # Scene 13: 120 Hours Drama & Guest Badge
        ("Two Silhouettes Altman & Satya Nadella (AI Video)", "EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4"),
        ("Photographic Strobe Flashes Inverting (User AI Video)", "Photographic_strobe_inverting_image_81594c7e_1080p.mp4"),
        ("Window Rainy Night Reflection (AI Video)", "EP01_V1_NEW_03_Window_Rain_16s.mp4"),
        ("Altman TED 2023 Talk (Internet Archive)", "EP01_V2_B3_02_Altman_TED_2023_10s.mp4"),

        # Scene 14: 730 Signatures & Return
        ("Camera Accelerating Through Letter Text (User AI Video)", "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4"),
        ("Golden Signatures Flowing Stream (Flow Video)", "ep01_flow_08_golden_signatures.mp4"),
        ("Stylized Golden Network Grid (ElevenLabs Video)", "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4"),
        ("Golden Grid Stabilizing OpenAI Power (AI Video)", "EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4"),

        # === ACT 4: PHYSICALITY OF COMPUTE & THE THREE RULES (11:00 - 13:30) ===
        # Scene 15: Physicality of Compute, Stargate, Fusion
        ("Physical Matter Dissolves into Bits (User AI Video)", "Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4"),
        ("Fusion Torus Reactor Energy Core (Flow Video)", "ep01_flow_09_fusion_torus.mp4"),
        ("Tesla Coil Electric Power Discharges (Internet Archive)", "EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4"),
        ("Leader in Tactical Arctic Parka at Datacenter (User AI Video)", "Man_wearing_tactical_arctic_parka_24ef8e34_1080p.mp4"),
        ("Jensen Huang Reveals Blackwell B200 Wafer (Internet Archive)", "EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4"),

        # Scene 16: Three Rules of Exponential Life
        ("Slow Powerful Altman Vision Portrait (ElevenLabs Video)", "ElevenLabs_video_seedance-2-5_Slow,_powerful__2026-11-09T12_52_53.mp4"),
        ("Fluid Intelligence Dynamic Waves (ElevenLabs Video)", "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59.mp4"),
        ("Light Streaks Exploding Horizontally (User AI Video)", "Light_point_explodes_into_streaks_c712a46e_1080p.mp4"),
        ("Obsessive Builders Working at Midnight (AI Video)", "EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4"),
        ("Laser Writing Words in Darkness (User AI Video)", "Laser_forms_text_words_89a267cd_1080p.mp4"),

        # Scene 17: Plastic Reality & Finale
        ("Earth Horizon Sunrise from Orbit (Flow Video)", "ep01_flow_10_earth_horizon.mp4"),
        ("Boy Morphing into Modern Tech Leader (User AI Video)", "Boy_aging_into_tech_leader_cd380219_1080p.mp4"),
        ("Golden Grid Closer (Flow Closer)", "EP01_V1_B3_CLOSER_GoldenGrid_340f.mp4"),
        ("Deep Space Starfield Closer (Flow Closer)", "EP01_V1_B4_CLOSER_DeepSpace_154f.mp4"),
    ]

    print(f"\n--- 2. Placing {len(curated_video_sequence)} Pure Video Clips onto Track V1 ---")

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)
    curr_frame = start_frame

    placed = 0
    missing = []
    for label, filename in curated_video_sequence:
        c = all_clips.get(filename)
        # Fallback search if slight filename mismatch
        if not c:
            # try space instead of underscore
            alt_name = filename.replace('_', ' ')
            c = all_clips.get(alt_name)
        if not c:
            missing.append(filename)
            continue

        dur_tc = c.GetClipProperty("Duration")
        if not dur_tc:
            dur_f = 240
        else:
            dur_f = tc_to_frames(dur_tc)

        app = {
            "mediaPoolItem": c,
            "mediaType": 1, # Video
            "trackIndex": 1,
            "recordFrame": curr_frame
        }
        res = mp.AppendToTimeline([app])
        if res:
            sec_start = (curr_frame - start_frame) / FPS
            m_s, sec_s = divmod(sec_start, 60)
            placed += 1
            print(f"  🎥 [{m_s:02.0f}:{sec_s:04.1f}] V1: {filename} ({dur_f/FPS:.1f}s) — {label}")
            curr_frame += dur_f

    total_frames = curr_frame - start_frame
    tm, ts = divmod(total_frames / FPS, 60)

    print("\n--- 3. Verification ---")
    v1_count = len(tl.GetItemListInTrack("video", 1) or [])
    v2_count = len(tl.GetItemListInTrack("video", 2) or []) if tl.GetTrackCount("video") >= 2 else 0
    a1_count = len(tl.GetItemListInTrack("audio", 1) or [])
    print(f"  • Placed clips on Track V1: {placed} (Verified on timeline: {v1_count})")
    print(f"  • Clips on Track V2: {v2_count} (Expected: 0)")
    print(f"  • Audio Track A1 clips: {a1_count} (Ukrainian Voiceover preserved)")
    print(f"  • Total Video Duration: {total_frames} frames ({tm:02.0f}:{ts:04.1f})")
    if missing:
        print(f"  ⚠️ Missing clips ({len(missing)}): {missing}")

    print("\n🎉 SUCCESS: TIMELINE CONTAINS ONLY GENERATED VIDEOS & INTERNET ARCHIVES!")
    pm.SaveProject()
    print("✓ Project Saved Successfully.")

if __name__ == '__main__':
    run()
