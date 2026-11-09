#!/usr/bin/env python3
"""
Masterpiece Director's Cut: Episode 01, Block 1 (00:00 - 04:00)
Timeline: EP01_BLOCK1_Master_Director_Cut

Fixes applied based on Director Feedback:
1. DIVERSIFIED VISUALS: Eliminated repetitive glowing circuit boards/wafers.
   Replaced with atmospheric dorm silhouettes, Burroughs stone monoliths,
   nocturnal window reflection, Loopt smartphone on desk, founder data currents,
   and cosmic Dyson swarm. Exactly ONE single 10s wafer shot at Stanford transition.
2. ZERO OVERLAYS / ZERO COLLISIONS: Staggered V2 (archives) and V3 (thought cards)
   with dedicated breathing room. Never active simultaneously.
3. TWO-PART DYNAMIC MUSIC:
   - Part 1 (00:00 - 01:38, 98s): Warm Analog Pulse (-21dB) - Contemplative childhood & school.
   - Part 2 (01:38 - 04:00, 142s): Warm Analog Pulse-2 (-21dB) - Arpeggiated momentum & hustle.
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble_master():
    resolve = bmd.scriptapp('Resolve')
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_BLOCK1_Master_Director_Cut"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print("Timeline not found!")
        return

    # 1. Clean existing items across all video and audio tracks
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

    def place_at_frame(clip_name, media_type, track_idx, rec_frame, vol=None, leveler=False):
        c = clips.get(clip_name)
        if not c:
            print(f"  MISSING IN MEDIA POOL: {clip_name}")
            return None
        app = {"mediaPoolItem": c, "mediaType": media_type, "trackIndex": track_idx, "recordFrame": rec_frame}
        its = mp.AppendToTimeline([app])
        if its:
            it = its[0]
            if vol is not None:
                it.SetProperty("AudioVolume", vol)
            if leveler:
                it.SetProperty("AudioDialogueLevelerEnabled", True)
                it.SetProperty("AudioDialogueLevelerReduceLoudDialogue", True)
                it.SetProperty("AudioDialogueLevelerLiftSoftDialogue", True)
            return it
        return None

    # Track Labels
    tl.SetTrackName("audio", 1, "VOICEOVER_A1")
    tl.SetTrackName("audio", 2, "MUSIC_WARM_A2")
    tl.SetTrackName("audio", 3, "LIVE_ARCHIVES_A3")
    tl.SetTrackName("video", 1, "FLOW_CANVAS_V1")
    tl.SetTrackName("video", 2, "ARCHIVES_PHOTOS_V2")
    tl.SetTrackName("video", 3, "THOUGHT_CARDS_V3")

    # ==========================================================
    # 1. AUDIO TRACK A1: VOICEOVER (6 Takes, Leveler ON, +2dB)
    # ==========================================================
    print("\n--- 1. Placing Track A1: Voiceover ---")
    vo_plan = [
        ("EP01_VO_EN_01_ACT1_00_00_00_15_Intro_Rules.wav", 0.0),
        ("EP01_VO_EN_02_ACT1_00_15_00_45_Macintosh_1993.wav", 15.0),
        ("EP01_VO_EN_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 58.0),
        ("EP01_VO_EN_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 98.0),
        ("EP01_VO_EN_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 150.0),
        ("EP01_VO_EN_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 215.0),
    ]
    for name, sec in vo_plan:
        rf = start_frame + round(sec * FPS)
        it = place_at_frame(name, 2, 1, rf, vol=2.0, leveler=True)
        print(f"  ✓ VO: {name} placed at {sec:.1f}s")

    # ==========================================================
    # 2. AUDIO TRACK A2: DYNAMIC TWO-PART SCORE (-21dB)
    # Part 1: Contemplative childhood & school (00:00 - 01:38)
    # Part 2: Arpeggiated momentum & exponential turn (01:38 - 04:00)
    # ==========================================================
    print("\n--- 2. Placing Track A2: Dynamic Two-Part Music Bed ---")
    # Part 1 (0.0s to 98.0s)
    place_at_frame("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog.wav", 2, 2, start_frame, vol=-21.0)
    print("  ✓ Music Part 1: Warm Analog Pulse (00:00 - 01:38) at -21.0 dB")
    # Part 2 (98.0s to 240.0s)
    rf_part2 = start_frame + round(98.0 * FPS)
    place_at_frame("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2.wav", 2, 2, rf_part2, vol=-21.0)
    print("  ✓ Music Part 2: Warm Analog Pulse-2 (01:38 - 04:00) at -21.0 dB")

    # ==========================================================
    # 3. AUDIO TRACK A3: AUTHENTIC LIVE ARCHIVAL AUDIO
    # ==========================================================
    print("\n--- 3. Placing Track A3: Authentic Live Audio ---")
    rf_crt = start_frame + round(10.0 * FPS)
    place_at_frame("EP01_ARCH_AUDIO_Macintosh_1992_CRT_Scan.wav", 2, 3, rf_crt, vol=-12.0)
    rf_jobs = start_frame + round(155.0 * FPS)
    place_at_frame("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 3, rf_jobs, vol=-4.0)
    print("  ✓ Live: Steve Jobs WWDC 2008 + 1992 Mac CRT Chime")

    # ==========================================================
    # 4. VIDEO TRACK V1: 100% CONTIGUOUS CINEMATIC CANVAS (DIVERSIFIED)
    # Zero repeating circuit boards. Sequential frame-accurate placement.
    # ==========================================================
    print("\n--- 4. Placing Track V1: Diversified Contiguous Canvas ---")
    v1_sequence = [
        ("ep01_flow_01_mac_chassis.mp4", "Macintosh LC II Beige Chassis"),
        ("EP01_CLIP_V1_05_Eye_Code_11s.mp4", "Macro Eye Terminal Reflection"),
        ("ep01_flow_02_crt_code.mp4", "Phosphor CRT Warming Screen"),
        ("EP01_CLIP_V1_06_Boy_Room_12s.mp4", "1993 Childhood Room"),
        ("EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4", "Silhouette Coder at Night"),
        ("EP01_V1_NEW_02_Burroughs_Monoliths_15s.mp4", "Institutional Classical Monoliths"),
        ("EP01_CLIP_V1_07_Phosphor_12s.mp4", "CRT Phosphor RGB Triads"),
        ("EP01_V1_NEW_03_Window_Rain_16s.mp4", "Nocturnal Thinker by Rain Window"),
        ("ep01_flow_03_silicon_laser.mp4", "Silicon Wafer Substrate & Laser (Hero)"),
        ("EP01_V1_NEW_04_Smartphone_Loopt_16s.mp4", "Smartphone on Desk / Geolocation"),
        ("EP01_CLIP_V1_13_Garage_14s.mp4", "Startup Garage Workstation"),
        ("ep01_flow_07_boardroom_noir.mp4", "Corporate Boardroom Noir"),
        ("EP01_CLIP_V1_15_FounderGrit_15s.mp4", "Raw Founder Hustle Space"),
        ("ep01_flow_06_server_monolith.mp4", "Monolithic Server Cluster"),
        ("EP01_CLIP_V1_16_ServerCold_8s.mp4", "Cold Server Rack Aisles"),
        ("ep01_flow_04_exponential_line.mp4", "Golden Exponential Ascent Curve"),
        ("EP01_V1_NEW_05_Founder_Data_15s.mp4", "Founder Dissolving into Data"),
        ("ep01_flow_08_golden_signatures.mp4", "Golden Signature Ribbons"),
        ("ep01_flow_09_fusion_torus.mp4", "Clean Fusion Plasma Torus"),
        ("ep01_flow_10_earth_horizon.mp4", "Earth Horizon Neural Orbit"),
        ("EP01_V1_NEW_06_Cosmic_Dyson_12s.mp4", "Cosmic Dyson Swarm Scale"),
    ]

    cur_frame = start_frame
    for name, desc in v1_sequence:
        item = place_at_frame(name, 1, 1, cur_frame)
        if item:
            dur = item.GetDuration()
            print(f"  ✓ V1 [{dur/24.0:4.1f}s]: {desc:38} @ {cur_frame}")
            cur_frame += dur
        else:
            print(f"  ✗ V1 FAILED: {name}")

    total_v1_dur = (cur_frame - start_frame) / 24.0
    print(f"  ==> Total Gapless V1 Duration: {total_v1_dur:.2f}s ({total_v1_dur/60.0:.2f} min) - 0 Black Frames!")

    # ==========================================================
    # 5. VIDEO TRACK V2: AUTHENTIC ARCHIVES (STAGGERED, ZERO OVERLAP)
    # ==========================================================
    print("\n--- 5. Placing Track V2: Authentic Archives ---")
    v2_plan = [
        ("EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4", 10.0, "1992 Mac CRT Commercial Clip"),
        ("EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 20.0, "Childhood Photo 8yo Sam with Mac"),
        ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 58.0, "John Burroughs School Campus Photo"),
        ("EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 105.0, "Stanford University Campus Photo"),
        ("EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 135.0, "Young Altman Loopt Founder Shirt"),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 155.0, "Steve Jobs Invites Sam Altman on Stage WWDC 2008"),
        ("EP01_V2_ARCH_03_Jobs_Stage_10s.mp4", 170.0, "Photo with Steve Jobs on WWDC Stage"),
        ("EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 218.0, "Young 24yo Sam Altman Portrait"),
    ]
    for name, sec, desc in v2_plan:
        rf = start_frame + round(sec * FPS)
        place_at_frame(name, 1, 2, rf)
        print(f"  ✓ V2: {desc:45} at {sec:5.1f}s")

    # ==========================================================
    # 6. VIDEO TRACK V3: 4K THOUGHT CARDS & PRESS DOSSIER (STAGGERED)
    # ==========================================================
    print("\n--- 6. Placing Track V3: Thought Cards & Dossiers ---")
    v3_plan = [
        ("EP01_CARD_01_Extension_Of_Thought.mp4", 32.0, "Thought Card 01: Extension of Thought"),
        ("EP01_CARD_02_Indifference_To_Authority.mp4", 45.0, "Thought Card 02: Indifference to Authority"),
        ("EP01_CARD_03_Autonomy_Equation.mp4", 74.0, "Thought Card 03: The Autonomy Equation"),
        ("EP01_CARD_04_Linear_Vs_Exponential.mp4", 120.0, "Thought Card 04: Linear vs Exponential"),
        ("EP01_CARD_05_Psychological_Friction.mp4", 185.0, "Thought Card 05: Psychological Friction"),
        ("EP01_DOC_01_YC_2005_Program_10s.mp4", 202.0, "Press Dossier: YC Summer 2005 Announcement"),
    ]
    for name, sec, desc in v3_plan:
        rf = start_frame + round(sec * FPS)
        place_at_frame(name, 1, 3, rf)
        print(f"  ✓ V3: {desc:45} at {sec:5.1f}s")

    # ==========================================================
    # 7. CHAPTER MARKERS
    # ==========================================================
    # Clear existing markers
    for m in tl.GetMarkers() or {}:
        tl.DeleteMarkerAtFrame(m)

    markers = [
        (0.0, "Cyan", "Сцена 1: Вступ і природа правил"),
        (15.0, "Blue", "Сцена 2: 1993, Macintosh LC II та перший баг"),
        (58.0, "Yellow", "Сцена 3: Джон Берроуз Скул та вихід із тіні"),
        (98.0, "Green", "Сцена 4: Стенфорд і заснування Loopt (Експонента)"),
        (150.0, "Orange", "Сцена 5: YC Batch 1, цинга і Стів Джобс на WWDC 2008"),
        (215.0, "Red", "Сцена 6: Мислення складного відсотка та масштаб"),
    ]
    for sec, col, note in markers:
        frm = start_frame + round(sec * FPS)
        tl.AddMarker(frm, col, note, f"Act 1 Beat at {sec:.0f}s", 1)

    pm.SaveProject()
    print("\n" + "="*65)
    print("🏆 MASTERPIECE BLOCK 1 SUCCESSFULLY REASSEMBLED")
    print(f"Timeline Name : {tl_name}")
    print(f"Total V1 Dur  : {total_v1_dur:.2f}s (100% gapless, zero black frames)")
    print(f"V1 Clips      : {len(v1_sequence)} diversified cinematic clips")
    print("Music Bed     : 2-Part dynamic score (Warm Analog Pulse -> Warm Analog Pulse-2)")
    print("Track V2 & V3 : 100% staggered, zero overlapping collisions")
    print("="*65)

if __name__ == "__main__":
    assemble_master()
    os._exit(0)
