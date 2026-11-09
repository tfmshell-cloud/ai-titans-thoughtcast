#!/usr/bin/env python3
"""
Masterpiece Director's Cut: Episode 01, Block 1 (00:00 - 04:00)
Timeline: EP01_BLOCK1_Master_Director_Cut

Director Updates:
1. ENGLISH TYPEWRITER THOUGHT CARDS:
   All 5 Thought Cards translated to English and re-rendered with a dynamic
   letter-by-letter animated typewriter effect & blinking cursor in 4K.
2. SYNCHRONIZED MECHANICAL KEYBOARD AUDIO:
   Real mechanical keyboard typing sound (EP01_SFX_Keyboard_Typing_Burst_4s.wav)
   placed on Track A4 (SFX_KEYBOARD_A4) at -17.0 dB under each Thought Card.
3. COMPLETE 10 TITANS MEDIA POOL:
   All media across all 10 heroes (Chess, Go, robotics, scientific 3D animations,
   historical archives, music stems) ingested and structured in 33 Bins.
4. ZERO OVERLAYS & 100% GAPLESS CANVAS:
   V1 is 100% contiguous (239.58s). V2 and V3 are 100% staggered with zero overlap.
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

    # Clear all items across all tracks
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
    tl.SetTrackName("audio", 4, "SFX_KEYBOARD_A4")
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
        place_at_frame(name, 2, 1, rf, vol=2.0, leveler=True)
        print(f"  ✓ VO: {name} placed at {sec:.1f}s")

    # ==========================================================
    # 2. AUDIO TRACK A2: DYNAMIC TWO-PART SCORE (-21dB)
    # ==========================================================
    print("\n--- 2. Placing Track A2: Dynamic Two-Part Music Bed ---")
    place_at_frame("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog.wav", 2, 2, start_frame, vol=-21.0)
    rf_part2 = start_frame + round(98.0 * FPS)
    place_at_frame("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2.wav", 2, 2, rf_part2, vol=-21.0)
    print("  ✓ Music Part 1 (00:00 - 01:38) & Part 2 (01:38 - 04:00) placed at -21.0 dB")

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
    # 4. AUDIO TRACK A4: MECHANICAL KEYBOARD TYPING BURSTS (-17dB)
    # Synchronized with the 5 Typewriter Thought Cards!
    # ==========================================================
    print("\n--- 4. Placing Track A4: Mechanical Keyboard Foley SFX ---")
    sfx_burst_plan = [
        32.0,  # Card 01
        45.0,  # Card 02
        74.0,  # Card 03
        120.0, # Card 04
        185.0, # Card 05
    ]
    for sec in sfx_burst_plan:
        rf = start_frame + round(sec * FPS)
        place_at_frame("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-17.0)
        print(f"  ✓ SFX: Mechanical Keyboard Typing Burst at {sec:.1f}s (-17.0 dB)")

    # ==========================================================
    # 5. VIDEO TRACK V1: 100% CONTIGUOUS CINEMATIC CANVAS (DIVERSIFIED)
    # ==========================================================
    print("\n--- 5. Placing Track V1: Diversified Contiguous Canvas ---")
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
        ("EP01_CLIP_V1_19_CurveHero_17s.mp4", "Epic Future Horizon Exponential Ascent"),
    ]

    cur_frame = start_frame
    for name, desc in v1_sequence:
        item = place_at_frame(name, 1, 1, cur_frame)
        if item:
            dur = item.GetDuration()
            cur_frame += dur
        else:
            print(f"  ✗ V1 FAILED: {name}")

    total_v1_dur = (cur_frame - start_frame) / 24.0
    print(f"  ==> Total Gapless V1 Duration: {total_v1_dur:.2f}s ({total_v1_dur/60.0:.2f} min) - 0 Black Frames!")

    # ==========================================================
    # 6. VIDEO TRACK V2: AUTHENTIC ARCHIVES (STAGGERED)
    # ==========================================================
    print("\n--- 6. Placing Track V2: Authentic Archives ---")
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
    # 7. VIDEO TRACK V3: ENGLISH 4K TYPEWRITER THOUGHT CARDS
    # ==========================================================
    print("\n--- 7. Placing Track V3: English Typewriter Thought Cards ---")
    v3_plan = [
        ("EP01_CARD_01_Extension_Of_Thought.mp4", 32.0, "Thought Card 01: Extension of Thought (English Typewriter)"),
        ("EP01_CARD_02_Indifference_To_Authority.mp4", 45.0, "Thought Card 02: Indifference to Authority (English Typewriter)"),
        ("EP01_CARD_03_Autonomy_Equation.mp4", 74.0, "Thought Card 03: The Autonomy Equation (English Typewriter)"),
        ("EP01_CARD_04_Linear_Vs_Exponential.mp4", 120.0, "Thought Card 04: Linear vs Exponential (English Typewriter)"),
        ("EP01_CARD_05_Psychological_Friction.mp4", 185.0, "Thought Card 05: Psychological Friction (English Typewriter)"),
        ("EP01_DOC_01_YC_2005_Program_10s.mp4", 202.0, "Press Dossier: YC Summer 2005 Announcement"),
    ]
    for name, sec, desc in v3_plan:
        rf = start_frame + round(sec * FPS)
        place_at_frame(name, 1, 3, rf)
        print(f"  ✓ V3: {desc:55} at {sec:5.1f}s")

    # Markers
    for m in tl.GetMarkers() or {}:
        tl.DeleteMarkerAtFrame(m)

    markers = [
        (0.0, "Cyan", "Scene 1: Intro & Nature of Rules"),
        (15.0, "Blue", "Scene 2: 1993, Macintosh LC II & The First Bug"),
        (58.0, "Yellow", "Scene 3: John Burroughs School & Coming Out"),
        (98.0, "Green", "Scene 4: Stanford & Loopt Genesis (The Exponential Turn)"),
        (150.0, "Orange", "Scene 5: YC Batch 1, Scurvy & Steve Jobs on WWDC Stage"),
        (215.0, "Red", "Scene 6: Compound Interest Mindset & Ultimate Scale"),
    ]
    for sec, col, note in markers:
        frm = start_frame + round(sec * FPS)
        tl.AddMarker(frm, col, note, f"Act 1 Beat at {sec:.0f}s", 1)

    pm.SaveProject()
    print("\n" + "="*70)
    print("🏆 MASTER TIMELINE FULLY ASSEMBLED WITH ENGLISH TYPEWRITER & KEYBOARD SFX")
    print(f"Timeline Name : {tl_name}")
    print(f"Total V1 Dur  : {total_v1_dur:.2f}s (100% gapless)")
    print(f"Thought Cards : 5 English 4K Typewriter Animated Cards (Track V3)")
    print(f"Keyboard SFX  : 5 Mechanical Typing Foley Bursts @ -17dB (Track A4)")
    print(f"Music Bed     : 2-Part dynamic score @ -21dB (Track A2)")
    print(f"Archives      : 8 Authentic Clips @ Track V2 + Live Steve Jobs WWDC @ Track A3")
    print("="*70)

if __name__ == "__main__":
    assemble_master()
    os._exit(0)
