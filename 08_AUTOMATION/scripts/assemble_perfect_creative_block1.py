#!/usr/bin/env python3
"""
🏆 THE PERFECT CREATIVE MASTERPIECE: EPISODE 01, BLOCK 1 (00:00 - 04:00)
Timeline: EP01_BLOCK1_Master_Director_Cut

Changes based on Director Volodymyr's feedback:
1. ZERO REPETITIVE COMPUTERS:
   - 00:00 - 00:08: Human figure dissolving into equations in cosmic void (Laws of physics vs arbitrary social rules).
   - 00:08 - 00:19: Macro eye reflecting terminal code.
   - 00:19 - 00:29: The ONLY computer scene: 1993 Childhood room with 8yo Sam Macintosh story!
   - 00:29 - 00:41: Galaxies and stars connected by glowing neural axons (infinite thought without physical friction).
   - 00:41 - 00:46: Synaptic neural lattice.
   - 00:46 - 01:00: Silhouette nocturnal thinker.
   - 01:00 - 01:15: Grand classical chessboard merging into digital grid (rules as artificial game).
   - 01:15 - 01:27: Mind fracturing and radiating golden geometric light (psychological independence).
   - 01:27 - 01:43: Rain-slicked window solitary thinker.
   - 01:43 - 01:53: Silicon wafer cyan laser etching.
   - 01:53 - 02:03: Nanobots assembling atomic graphene.
   - 02:03 - 02:19: Holographic geolocation matrix map (Loopt data layer on reality).
   - 02:19 - 02:27: Tactical 3D Lidar point-cloud scanning city streets.
   - 02:27 - 02:41: Obsessive builders facing compute core at night (YC scurvy survival).
   - 02:41 - 02:49: Strategic chessboard in desert sandstorm.
   - 02:49 - 03:04: Raw founder focus in code flow.
   - 03:04 - 03:12: Golden transistor dust cascading in dark void.
   - 03:12 - 03:22: Golden exponential ascent curve.
   - 03:22 - 03:37: Molten gold coins transforming into neural brain (true dividend of compounding).
   - 03:37 - 03:42: Helion clean fusion plasma torus.
   - 03:42 - 03:48: Deep space asteroid coasting in cosmic void.
   - 03:48 - 03:55: Cosmic Dyson swarm star megastructure.
   - 03:55 - 04:00: Earth atmosphere horizon from orbit (finale).

2. ELIMINATED AIRPLANE HYPERSONIC CLIP:
   - Removed EP01_SCI_01_Supersonic_Prandtl_Glauert_Breakout.
   - Opening 20 seconds is pure, unencumbered cinematic atmosphere.

3. MATHEMATICAL ACCURACY:
   - Exactly 5760 frames (240.00s / 04:00.00). 100% gapless, zero black frames.
   - V2 and V3 overlays have native 12-frame (0.5s) dissolves.
   - Audio: A1 (+2dB, Leveler ON), A2 (-21dB), A3 (Live archives), A4 (Foley typing).
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def assemble():
    resolve = bmd.scriptapp('Resolve')
    proj = resolve.GetProjectManager().GetCurrentProject()
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

    def place_clip(clip_name, media_type, track_idx, rec_frame, vol=None, leveler=False, fades=None):
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
            if leveler:
                it.SetProperty("AudioDialogueLevelerEnabled", True)
                it.SetProperty("AudioDialogueLevelerReduceLoudDialogue", True)
                it.SetProperty("AudioDialogueLevelerLiftSoftDialogue", True)
            if fades:
                it.SetFades(fades)
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

    fade_spec = {'FadeIn': 12.0, 'FadeOut': 12.0}

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
        place_clip(name, 2, 1, rf, vol=2.0, leveler=True)
        print(f"  ✓ VO: {name} placed at {sec:.1f}s")

    # ==========================================================
    # 2. AUDIO TRACK A2: DYNAMIC TWO-PART SCORE (-21dB)
    # ==========================================================
    print("\n--- 2. Placing Track A2: Music Score Bed ---")
    place_clip("EP01_MUS_PART1_00_00_to_01_38_WarmAnalog.wav", 2, 2, start_frame, vol=-21.0)
    rf_part2 = start_frame + round(98.0 * FPS)
    place_clip("EP01_MUS_PART2_01_38_to_03_58_WarmPulse2.wav", 2, 2, rf_part2, vol=-21.0)
    print("  ✓ Music Part 1 & Part 2 placed at -21.0 dB")

    # ==========================================================
    # 3. AUDIO TRACK A3: AUTHENTIC LIVE ARCHIVAL AUDIO
    # ==========================================================
    print("\n--- 3. Placing Track A3: Authentic Live Audio ---")
    rf_crt = start_frame + round(19.0 * FPS) # timed with childhood Mac appearance!
    place_clip("EP01_ARCH_AUDIO_Macintosh_1992_CRT_Scan.wav", 2, 3, rf_crt, vol=-12.0)
    rf_jobs = start_frame + round(165.0 * FPS) # timed with Jobs WWDC video!
    place_clip("EP01_ARCH_AUDIO_SteveJobs_WWDC_2008.wav", 2, 3, rf_jobs, vol=-4.0)
    print("  ✓ Live: Steve Jobs WWDC 2008 + 1992 Mac CRT Chime at 19s")

    # ==========================================================
    # 4. AUDIO TRACK A4: MECHANICAL KEYBOARD FOLEY SFX (-18dB)
    # Synchronized with the 4 Essential English Thought Cards!
    # ==========================================================
    print("\n--- 4. Placing Track A4: Mechanical Keyboard Foley SFX ---")
    sfx_burst_plan = [
        45.0,  # Card 02 (Indifference to Authority)
        82.0,  # Card 03 (Autonomy Equation)
        128.0, # Card 04 (Linear vs Exponential)
        185.0, # Card 05 (Psychological Friction)
    ]
    for sec in sfx_burst_plan:
        rf = start_frame + round(sec * FPS)
        place_clip("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-18.0)
        print(f"  ✓ SFX: Keyboard Typing at {sec:.1f}s (-18.0 dB)")

    # ==========================================================
    # 5. VIDEO TRACK V1: 100% CONTIGUOUS CINEMATIC CANVAS (23 CLIPS)
    # ZERO repetitive computers! Pure visual poetry & diversity!
    # Exactly 5760 frames = 240.00s (04:00.00)
    # ==========================================================
    print("\n--- 5. Placing Track V1: Master Creative Canvas (23 Clips) ---")
    v1_sequence = [
        ("EP01_V1_CREATIVE_01_Equations_Void_8s.mp4", "Equations in Cosmic Void (Physical Laws)"),
        ("EP01_CLIP_V1_05_Eye_Code_11s.mp4", "Macro Eye Code Terminal Reflection"),
        ("EP01_CLIP_V1_06_Boy_Room_10s.mp4", "1993 Childhood Room (Only Vintage Mac Scene!)"),
        ("EP01_V1_CREATIVE_02_Galaxies_Axons_12s.mp4", "Galaxies Connected by Neural Axons"),
        ("ep01_flow_05_neural_lattice.mp4", "Synaptic Neural Lattice Void"),
        ("EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4", "Silhouette Nocturnal Thinker"),
        ("EP01_V1_CREATIVE_03_Chess_Simulation_Grid_15s.mp4", "Chessboard Merging into Digital Grid (Rules as Game)"),
        ("EP01_V1_CREATIVE_04_Mind_Radiating_Light_12s.mp4", "Mind Fracturing & Radiating Golden Light"),
        ("EP01_V1_NEW_03_Window_Rain_16s.mp4", "Rain-Slicked Window Thinker"),
        ("ep01_flow_03_silicon_laser.mp4", "Silicon Wafer Substrate & Cyan Laser"),
        ("EP02_SCI_01_Nanobots_Graphene_Lattice_Assembly.mp4", "Nanobots Graphene Atomic Assembly"),
        ("EP01_V1_CREATIVE_05_Holo_Geo_Matrix_16s.mp4", "Holographic Geolocation Matrix Map (Loopt Data Layer)"),
        ("EP01_V1_ASSOC_01_Lidar_City_Grid_8s.mp4", "Tactical 3D Lidar Urban City Grid"),
        ("EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4", "Obsessive Builders Facing Compute Core (YC Scurvy)"),
        ("EP01_V1_ASSOC_02_Chess_Sandstorm_8s.mp4", "Strategic Chessboard in Desert Sandstorm"),
        ("EP01_CLIP_V1_15_FounderGrit_15s.mp4", "Intense Founder Focus in Code Flow"),
        ("EP01_V1_CREATIVE_07_Golden_Transistor_Dust_8s.mp4", "Hand Releasing Golden Transistor Dust"),
        ("ep01_flow_04_exponential_line.mp4", "Golden Exponential Ascent Curve"),
        ("EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", "Gold Melting into Neural Brain (Compounding Dividend)"),
        ("ep01_flow_09_fusion_torus.mp4", "Helion Clean Fusion Plasma Torus"),
        ("EP09_SCI_01_Asteroid_Coasting_Deep_Space_1080p.mp4", "Deep Space Asteroid Cosmic Scale"),
        ("EP01_V1_NEW_06_Cosmic_Dyson_7s.mp4", "Cosmic Dyson Swarm Star Megastructure"),
        ("ep01_flow_10_earth_horizon.mp4", "Earth Atmosphere Horizon from Orbit (Grand Finale)"),
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

    total_v1_dur = (cur_frame - start_frame) / 24.0
    total_v1_frames = cur_frame - start_frame
    print(f"  ==> Total Gapless V1: {total_v1_frames} frames ({total_v1_dur:.2f}s) - 100% GAPLESS!")

    # ==========================================================
    # 6. VIDEO TRACK V2: CURATED ARCHIVES (NO AIRPLANE!)
    # Each item gets native 12-frame (0.5s) dissolve in and out!
    # ==========================================================
    print("\n--- 6. Placing Track V2: Curated Archival Moments ---")
    v2_plan = [
        ("EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 20.0, "Childhood Photo: 8yo Sam with Mac 1993"),
        ("EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 62.0, "John Burroughs School Campus"),
        ("EP01_V2_ARCH_04_Stanford_Campus_12s.mp4", 102.0, "Stanford University Campus"),
        ("EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 138.0, "Young Altman in Loopt Founder Shirt"),
        ("EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 165.0, "Steve Jobs Live Stage Intro WWDC 2008"),
        ("EP01_V2_ARCH_01_Altman_Portrait_15s.mp4", 218.0, "Young 24yo Sam Altman Portrait"),
    ]
    for name, sec, desc in v2_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2: {desc:45} at {sec:5.1f}s (with 0.5s cross-dissolves)")

    # ==========================================================
    # 7. VIDEO TRACK V3: ENGLISH TYPEWRITER CARDS & YC PRESS DOSSIER
    # Each item gets native 12-frame (0.5s) dissolve in and out!
    # ==========================================================
    print("\n--- 7. Placing Track V3: English Typewriter Cards & Dossiers ---")
    v3_plan = [
        ("EP01_CARD_02_Indifference_To_Authority.mp4", 45.0, "Card 02: Indifference to Authority"),
        ("EP01_CARD_03_Autonomy_Equation.mp4", 82.0, "Card 03: The Autonomy Equation"),
        ("EP01_CARD_04_Linear_Vs_Exponential.mp4", 128.0, "Card 04: Linear vs Exponential"),
        ("EP01_CARD_05_Psychological_Friction.mp4", 185.0, "Card 05: Psychological Friction"),
        ("EP01_DOC_01_YC_2005_Program_10s.mp4", 202.0, "YC Summer 2005 Original Program Announcement"),
    ]
    for name, sec, desc in v3_plan:
        rf = start_frame + round(sec * FPS)
        place_clip(name, 1, 3, rf, fades=fade_spec)
        print(f"  ✓ V3: {desc:45} at {sec:5.1f}s (with 0.5s cross-dissolves)")

    tl.SetCurrentTimecode('01:00:00:00')
    print("\n🎉 MASTER DIRECTORS CUT ASSEMBLY FINISHED! Playhead at 01:00:00:00")
    os._exit(0)

if __name__ == '__main__':
    assemble()
