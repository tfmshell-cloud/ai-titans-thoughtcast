#!/usr/bin/env python3
"""
AI TITANS: EPISODE 01 — SAM ALTMAN
CLEAN AUDIO-ONLY MASTER TIMELINE
Removes ALL video clips and ALL photos from timeline.
Leaves ONLY the Ukrainian Voiceover audio track spanning the entire project (Scenes 1-17).
Adds timeline markers for each scene.
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
    print(f"🎬 CLEARING ALL VIDEO & PHOTOS -> LEAVING ONLY AUDIO TRACK: {tl.GetName()}")
    print("==================================================================")

    # 1. Clear all items from all video and audio tracks
    print("\n--- 1. Deleting all video, photo, and audio clips from timeline ---")
    for track_type in ["video", "audio"]:
        for t_idx in range(1, tl.GetTrackCount(track_type) + 1):
            items = tl.GetItemListInTrack(track_type, t_idx) or []
            if items:
                tl.DeleteClips(items)
                print(f"  ✓ Deleted {len(items)} clips from {track_type} track {t_idx}")

    # 2. Clear previous markers
    markers = tl.GetMarkers() or {}
    for f in list(markers.keys()):
        tl.DeleteMarkerAtFrame(f)
    print(f"  ✓ Cleared {len(markers)} old markers.")

    # 3. Label tracks
    tl.SetTrackName("video", 1, "EMPTY_VIDEO_CANVAS_V1")
    if tl.GetTrackCount("video") >= 2:
        tl.SetTrackName("video", 2, "EMPTY_ARCHIVES_V2")
    if tl.GetTrackCount("video") >= 3:
        tl.SetTrackName("video", 3, "EMPTY_GRAPHICS_V3")
    tl.SetTrackName("audio", 1, "UKRAINIAN_VOICEOVER_MASTER_A1")
    if tl.GetTrackCount("audio") >= 2:
        tl.SetTrackName("audio", 2, "CINEMATIC_SCORE_A2")
    if tl.GetTrackCount("audio") >= 3:
        tl.SetTrackName("audio", 3, "ARCHIVAL_AUDIO_A3")

    # 4. Scan Media Pool for Ukrainian VO clips
    def scan_bin(folder):
        res = {}
        for c in folder.GetClipList():
            res[c.GetName()] = c
        for s in folder.GetSubFolderList():
            res.update(scan_bin(s))
        return res

    clips = scan_bin(mp.GetRootFolder())

    # 17 Scenes Definition with Ukrainian Titles
    scenes = [
        {
            'num': 1,
            'title': 'Сцена 01: Тиск правил',
            'desc': 'Бунт проти догм та тиск суспільних правил',
            'vo': 'EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav'
        },
        {
            'num': 2,
            'title': 'Сцена 02: 1993 Сент-Луїс, Macintosh LC II',
            'desc': '8-річний Альтман розбирає комп’ютер викруткою, індиферентність',
            'vo': 'EP01_VO_UA_02_ACT1_00_15_00_45_Macintosh_LC_II_Indifference.wav'
        },
        {
            'num': 3,
            'title': 'Сцена 03: John Burroughs School, Камінг-аут',
            'desc': 'Виступ у 16 років на зборах школи, формула автономії',
            'vo': 'EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav'
        },
        {
            'num': 4,
            'title': 'Сцена 04: Стенфорд і Loopt',
            'desc': 'Стенфордський кампус, відрахування заради створення Loopt',
            'vo': 'EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav'
        },
        {
            'num': 5,
            'title': 'Сцена 05: YC Batch 1, Loopt, Джобс WWDC 2008',
            'desc': 'Перший батч Y Combinator 2005, презентація зі Стівом Джобсом',
            'vo': 'EP01_VO_UA_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav'
        },
        {
            'num': 6,
            'title': 'Сцена 06: Складний відсоток',
            'desc': 'Мислення складного відсотка та експоненційне зростання',
            'vo': 'EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav'
        },
        {
            'num': 7,
            'title': 'Сцена 07: Президент YC у 28 років',
            'desc': 'Керівництво найпотужнішим стартап-акселератором світу',
            'vo': 'EP01_VO_UA_07_ACT2_04_45_05_45_YC_President_28yo.wav'
        },
        {
            'num': 8,
            'title': 'Сцена 08: Rosewood, Довголіття, DeepMind',
            'desc': 'Вечеря в Rosewood, інвестиції в ядерну енергію та загроза Google',
            'vo': 'EP01_VO_UA_08_ACT2_05_45_07_00_Rosewood_Dinner_Google_Threat.wav'
        },
        {
            'num': 9,
            'title': 'Сцена 09: Заснування OpenAI, Scaling Hypothesis',
            'desc': 'Грудневий анонс 2015, гіпотеза масштабування та обчислення',
            'vo': 'EP01_VO_UA_09_ACT2_07_00_08_15_OpenAI_Founding_Dec2015.wav'
        },
        {
            'num': 10,
            'title': 'Сцена 10: Capped-Profit, Угода з Microsoft $1 млрд',
            'desc': 'Реструктуризація в комерційну модель та альянс із Сатьєю Наделла',
            'vo': 'EP01_VO_UA_10_ACT2_08_15_09_30_Capped_Profit_Microsoft_Bill.wav'
        },
        {
            'num': 11,
            'title': 'Сцена 11: Запуск ChatGPT, Сенат США',
            'desc': '30 листопада 2022, 100 млн користувачів, свідчення в Сенаті',
            'vo': 'EP01_VO_UA_11_ACT3_09_30_10_45_ChatGPT_Launch_100M_Users.wav'
        },
        {
            'num': 12,
            'title': 'Сцена 12: Заколот Ради директорів (17 листопада 2023)',
            'desc': 'П’ятничний переворот, звільнення Альтмана, падіння короля',
            'vo': 'EP01_VO_UA_12_ACT3_10_45_12_15_Friday_Board_Coup_Nov17.wav'
        },
        {
            'num': 13,
            'title': 'Сцена 13: 120 годин драми, Наделла, бейдж гостя',
            'desc': 'Криза вихідних, фото з гостьовим бейджем в офісі OpenAI',
            'vo': 'EP01_VO_UA_13_ACT3_12_15_13_45_120_Hours_Drama_Guest_Badge.wav'
        },
        {
            'num': 14,
            'title': 'Сцена 14: 730 підписів, тріумфальне повернення',
            'desc': 'Ультиматум команди, каяття Суцкевера, повернення на посаду CEO',
            'vo': 'EP01_VO_UA_14_ACT3_13_45_15_30_730_Signatures_Triumphant_Return.wav'
        },
        {
            'num': 15,
            'title': 'Сцена 15: Фізичність обчислень, Stargate $100B',
            'desc': 'Гігавати енергії, Helion термояд, датацентри та суперкомп’ютер Stargate',
            'vo': 'EP01_VO_UA_15_ACT4_15_30_17_00_Stargate_Helion_Energy_Physics.wav'
        },
        {
            'num': 16,
            'title': 'Сцена 16: Три правила експоненційного життя',
            'desc': 'Уроки Сема Альтмана для нової ери штучного інтелекту',
            'vo': 'EP01_VO_UA_16_ACT4_17_00_18_30_Three_Rules_Of_Exponential_Life.wav'
        },
        {
            'num': 17,
            'title': 'Сцена 17: Пластичність реальності, фінал',
            'desc': 'Майбутнє створюється сьогодні, аутро першого епізоду',
            'vo': 'EP01_VO_UA_17_ACT4_18_30_20_00_Future_Is_Created_Now_Outro.wav'
        }
    ]

    start_frame = tl.GetStartFrame() # 86400 (01:00:00:00)
    curr_frame = start_frame
    pause_frames = 24 # 1.0 second natural breath pause

    print("\n--- 2. Placing Ukrainian Voiceover Clips on Track A1 ---")
    for s in scenes:
        vo_file = s['vo']
        c = clips.get(vo_file)
        if not c:
            print(f"  ✗ MISSING: {vo_file}")
            continue

        dur_tc = c.GetClipProperty('Duration')
        dur_f = tc_to_frames(dur_tc)

        # Append to Track A1
        app = {"mediaPoolItem": c, "mediaType": 2, "trackIndex": 1, "recordFrame": curr_frame}
        res = mp.AppendToTimeline([app])
        if res:
            it = res[0]
            it.SetProperty("AudioVolume", 0.0)

        # Add Marker
        sec_start = (curr_frame - start_frame) / FPS
        m_s, sec_s = divmod(sec_start, 60)
        tl.AddMarker(curr_frame, "Cyan", s['title'], s['desc'], 24)
        print(f"  🎙️ [{m_s:02.0f}:{sec_s:04.1f}] Marker + VO: {s['title']} ({dur_f/FPS:.1f}s)")

        curr_frame += dur_f + pause_frames

    total_frames = curr_frame - start_frame
    tm, ts = divmod(total_frames / FPS, 60)

    # 5. Verification
    print("\n--- 3. Final Verification of Timeline State ---")
    total_video_clips = sum(len(tl.GetItemListInTrack("video", vi) or []) for vi in range(1, tl.GetTrackCount("video") + 1))
    total_audio_clips = sum(len(tl.GetItemListInTrack("audio", ai) or []) for ai in range(1, tl.GetTrackCount("audio") + 1))
    a1_clips = len(tl.GetItemListInTrack("audio", 1) or [])

    print(f"  • Video tracks clip count: {total_video_clips} (Expected: 0)")
    print(f"  • Audio track A1 clip count: {a1_clips} (Expected: 17)")
    print(f"  • Total audio clips across all tracks: {total_audio_clips} (Expected: 17)")
    print(f"  • Total timeline duration: {total_frames} frames ({tm:02.0f}:{ts:04.1f})")

    if total_video_clips == 0 and a1_clips == 17:
        print("\n🎉 SUCCESS: 100% CLEAN AUDIO-ONLY MASTER CREATED!")
    else:
        print("\n⚠️ WARNING: Clip counts do not match expected clean state.")

    pm.SaveProject()
    print("✓ Project Saved Successfully.")

if __name__ == '__main__':
    run()
