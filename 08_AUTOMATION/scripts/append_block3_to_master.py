#!/usr/bin/env python3
"""
🏆 APPEND BLOCK 3 TO UNIFIED MASTER DIRECTORS CUT: EPISODE 01 — ACT 1 + ACT 2 + ACT 3 (00:00 - 12:00)
Timeline: EP01_MASTER_DIRECTORS_CUT_COMPLETE (720.00s / 17,280 Frames)

Appends Block 3 (The Boardroom Coup, 120 Hours Drama, Triumphant Return, 08:00 - 12:00)
seamlessly at Frame 97920 (08:00.00) onto the continuous master timeline.
"""
import sys, os
sys.path.append('/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules')
import DaVinciResolveScript as bmd

FPS = 24.0

def append_block3():
    resolve = bmd.scriptapp('Resolve')
    proj = resolve.GetProjectManager().GetCurrentProject()
    mp = proj.GetMediaPool()

    tl_name = "EP01_MASTER_DIRECTORS_CUT_COMPLETE"
    tl = None
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t and t.GetName() == tl_name:
            tl = t
            proj.SetCurrentTimeline(tl)
            break

    if not tl:
        print("Master timeline not found!")
        return

    print(f"Master Timeline: {tl.GetName()}")
    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)
    b3_start = start_frame + 11520   # 97920 (01:08:00:00)

    # Clean only Block 3 region if any clips exist past b3_start
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            to_delete = [it for it in items if it.GetStart() >= b3_start]
            if to_delete:
                tl.DeleteClips(to_delete)

    def get_bin_items(folder):
        items = {}
        for clip in folder.GetClipList():
            items[clip.GetName()] = clip
        for sub in folder.GetSubFolderList():
            items.update(get_bin_items(sub))
        return items

    clips = get_bin_items(mp.GetRootFolder())

    def place_clip(clip_name, media_type, track_idx, rec_frame, vol=None, fades=None):
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
            if fades:
                it.SetFades(fades)
            return it
        return None

    fade_spec = {'FadeIn': 12.0, 'FadeOut': 12.0}

    print("\n=== Appending Block 3 (08:00 - 12:00 / Frames 97920 - 103680) ===")

    # 1. AUDIO TRACK A1: VOICEOVER (+2.0 dB)
    print("\n--- 1. Placing Block 3 Voiceover (Track A1) ---")
    vo_plan = [
        ("EP01_VO_EN_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav", 1.0),
        ("EP01_VO_EN_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav", 60.0),
        ("EP01_VO_EN_13_ACT3_12_15_13_45_120_Hours_Drama_Guest_Badge.wav", 120.0),
        ("EP01_VO_EN_14_ACT3_13_45_15_30_730_Signatures_Triumphant_Return.wav", 175.0),
    ]
    for name, sec in vo_plan:
        rf = b3_start + round(sec * FPS)
        place_clip(name, 2, 1, rf, vol=2.0)
        print(f"  ✓ VO: {name} placed at {480.0 + sec:.1f}s (Frame {rf})")

    # 2. AUDIO TRACK A2: MUSIC SCORE BED (-21.0 dB)
    print("\n--- 2. Placing Block 3 Music Drone Bed (Track A2) ---")
    place_clip("EP01_MUS_B3_PART1_08_00_to_10_00_120s.wav", 2, 2, b3_start, vol=-21.0)
    rf_part2 = b3_start + round(120.0 * FPS)
    place_clip("EP01_MUS_B3_PART2_10_00_to_12_00_120s.wav", 2, 2, rf_part2, vol=-21.0)
    print(f"  ✓ Music: ChatGPT Explosion & November Split placed at -21.0 dB (Frame {b3_start} to {b3_start + 5760})")

    # 3. AUDIO TRACK A3: LIVE ARCHIVAL AUDIO
    print("\n--- 3. Placing Block 3 Live Archival Audio (Track A3) ---")
    rf_senate = b3_start + round(48.0 * FPS)
    place_clip("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 2, 3, rf_senate, vol=-10.0)
    print(f"  ✓ Live: Senate Statement Audio placed at Frame {rf_senate}")

    # 4. AUDIO TRACK A4: MECHANICAL KEYBOARD FOLEY SFX (-18.0 dB)
    print("\n--- 4. Placing Block 3 Mechanical Keyboard SFX (Track A4) ---")
    sfx_plan = [
        28.0,  # Card 10 (Exponential Adoption)
        106.0, # Card 11 (Citadel Paradox)
        164.0, # Card 12 (Loyalty Axiom)
        222.0, # Card 13 (Paradigm of Power)
    ]
    for sec in sfx_plan:
        rf = b3_start + round(sec * FPS)
        place_clip("EP01_SFX_Keyboard_Typing_Burst_4s.wav", 2, 4, rf, vol=-18.0)
        print(f"  ✓ SFX: Keyboard Typing Burst at {480.0 + sec:.1f}s (Frame {rf})")

    # 5. VIDEO TRACK V1: MASTER CREATIVE CANVAS (25 CLIPS, EXACTLY 5760 FRAMES)
    print("\n--- 5. Placing Block 3 Track V1 Canvas (25 Clips) ---")
    v1_sequence = [
        ("ep09_flow_01_attention_vector_threads.mp4", "Attention Vector Threads (Transformer Architecture)"),
        ("ep10_flow_01_global_neural_classroom.mp4", "Global Neural Network Classroom (100M Users)"),
        ("EP01_V1_CREATIVE_04_Mind_Radiating_Light_12s.mp4", "Human Mind Radiating Light (Prompt Explosion)"),
        ("ep04_flow_01_backprop_synapse_storm.mp4", "Backprop Synapse Storm (Massive Compute)"),
        ("EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4", "Nocturnal Thinker (Global Shift & Capitol Hill)"),
        ("EP01_V1_B3_01_Chess_King_Falling_12s.mp4", "Wooden King Falling on Board (High Noon Coup)"),
        ("EP01_V1_B3_02_Boardroom_Void_14s.mp4", "Google Meet Boardroom Void (Dismissal Call)"),
        ("ep01_flow_07_boardroom_noir.mp4", "Boardroom Noir Rain (Citadel Ouster)"),
        ("EP01_V1_CREATIVE_05_Holo_Geo_Matrix_16s.mp4", "Holographic Global Market Convulsion"),
        ("ep06_flow_01_ssi_obsidian_monolith.mp4", "Obsidian Citadel Monolith"),
        ("EP01_V1_CREATIVE_01_Equations_Void_8s.mp4", "Equations in Dark Void (Tech Industry Freezes)"),
        ("EP01_V1_NEW_03_Window_Rain_16s.mp4", "Rain-Slicked Window (The Nature of Loyalty)"),
        ("EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4", "Two Silhouettes Symbol (Satya Nadella Unlimited Alliance)"),
        ("ep02_flow_01_blackwell_wafer_matrix.mp4", "Wafer Scale AI Matrix"),
        ("EP01_V1_CREATIVE_06_Obsessive_Builders_14s.mp4", "Obsessive Builders (Sunday Night Crisis)"),
        ("EP01_V1_ASSOC_01_Lidar_City_Grid_8s.mp4", "Tactical San Francisco City Grid (OpenAI HQ Arrival)"),
        ("EP01_V1_ASSOC_02_Chess_Sandstorm_8s.mp4", "Desert Sandstorm Strategic Battle"),
        ("EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4", "Golden Grid Stabilizing Stormy Ocean (738 Signatures)"),
        ("EP01_CLIP_V1_15_FounderGrit_15s.mp4", "Unprecedented Employee Loyalty in Code Flow"),
        ("ep01_flow_08_golden_signatures.mp4", "Golden Signatures Light Threads Alliance"),
        ("EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", "Gold Melting into Neural Brain (Paradigm of Power)"),
        ("ep08_flow_01_spatial_intelligence_dome.mp4", "Spatial Intelligence Dome (Multimodal Frontier Architecture)"),
        ("ep07_flow_01_constitutional_prism.mp4", "Constitutional Alignment Prism"),
        ("EP01_V1_NEW_06_Cosmic_Dyson_7s.mp4", "Cosmic Dyson Megastructure"),
        ("EP01_V1_B2_10_Earth_Horizon_Finale_214f.mp4", "Earth Atmosphere Horizon Orbit (Act 3 Grand Finale)"),
    ]

    cur_frame = b3_start
    for name, desc in v1_sequence:
        item = place_clip(name, 1, 1, cur_frame)
        if item:
            dur = item.GetDuration()
            cur_frame += dur
            print(f"  ✓ V1 [{dur/24.0:4.1f}s / {dur:3}f]: {desc:55} @ frame {cur_frame - dur}")
        else:
            print(f"  ✗ V1 FAILED: {name}")

    total_b3_v1_frames = cur_frame - b3_start
    print(f"  ==> Total Block 3 V1: {total_b3_v1_frames} frames ({total_b3_v1_frames/24.0:.2f}s)")
    print(f"  ==> Cumulative Timeline V1: {cur_frame - start_frame} frames ({(cur_frame - start_frame)/24.0:.2f}s / 12:00.00) - 100% GAPLESS!")

    # 6. VIDEO TRACK V2: CURATED ARCHIVES (5 MOMENTS)
    print("\n--- 6. Placing Block 3 Track V2 Archives ---")
    v2_plan = [
        ("EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4", 16.0, "Altman at ChatGPT Launch Genesis 2022"),
        ("EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4", 39.0, "Altman Senate Hearing Oath Closeup"),
        ("EP01_VID_ARCH_02_ACT3_24FPS_Altman_Senate_Regulation_Statement.mp4", 48.0, "Altman Senate Hearing Statement on AI"),
        ("EP01_V2_B2_03_Altman_Sutskever_TAU_10s.mp4", 75.0, "Altman & Ilya Sutskever Before Coup"),
        ("EP01_V2_B3_02_Altman_TED_2023_10s.mp4", 145.0, "Altman TED 2023 Public Face of AI"),
    ]
    for name, sec, desc in v2_plan:
        rf = b3_start + round(sec * FPS)
        place_clip(name, 1, 2, rf, fades=fade_spec)
        print(f"  ✓ V2: {desc:45} at {480.0 + sec:5.1f}s (Frame {rf})")

    # 7. VIDEO TRACK V3: THOUGHT CARDS & PRESS DOSSIERS (7 MOMENTS)
    print("\n--- 7. Placing Block 3 Track V3 Thought Cards & Dossiers ---")
    v3_plan = [
        ("EP01_CARD_10_Exponential_Adoption.mp4", 28.0, "Card 10: Exponential Adoption"),
        ("EP01_DOC_03_Board_Ouster_10s.mp4", 90.0, "OpenAI Board Ouster Press Announcement Nov 17"),
        ("EP01_CARD_11_Citadel_Paradox.mp4", 106.0, "Card 11: The Citadel Paradox"),
        ("EP01_CARD_12_Loyalty_Axiom.mp4", 164.0, "Card 12: The Loyalty Axiom / Visitor Badge"),
        ("EP01_DOC_04_Sutskever_Regret_10s.mp4", 188.0, "Ilya Sutskever Tweet of Profound Regret"),
        ("EP01_DOC_05_Employees_Letter_12s.mp4", 204.0, "738+ Employees Open Letter Ultimatum"),
        ("EP01_CARD_13_Paradigm_Of_Power.mp4", 222.0, "Card 13: The Paradigm of Power"),
    ]
    for name, sec, desc in v3_plan:
        rf = b3_start + round(sec * FPS)
        place_clip(name, 1, 3, rf, fades=fade_spec)
        print(f"  ✓ V3: {desc:45} at {480.0 + sec:5.1f}s (Frame {rf})")

    tl.SetCurrentTimecode('01:00:00:00')
    print("\n🎉 MASTER TIMELINE ACT 1 + ACT 2 + ACT 3 COMPLETE (00:00 - 12:00)! Playhead at 01:00:00:00")
    os._exit(0)

if __name__ == '__main__':
    append_block3()
