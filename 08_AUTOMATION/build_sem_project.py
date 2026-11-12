#!/usr/bin/env python3
"""
SEM / EP01 Акт I: створює проєкт у DaVinci Resolve, наповнює медіапул
і збирає таймлайн за планом EP01_UA_ActI_edit_plan.xlsx.

Що робить:
  1. Шукає медіа на диску за іменами файлів (шляхи вгадувати не треба).
  2. Вимірює реальні тривалості українських дублів і музики (модуль wave).
  3. Генерує FCPXML Акту I: візуали на V1, голос на A1, музика на A2,
     склейки на сітці 92 BPM, маркери для пропусків і графіки.
  4. У Resolve: створює проєкт SEM (24 fps, 3840x2160), створює бінси,
     імпортує медіа і імпортує таймлайн EP01_ActI_UA.

Перед запуском:
  * DaVinci Resolve Studio відкритий.
  * Resolve > Preferences > System > General > External scripting using: Local.
  * Українські WAV (папка EP01_ALTMAN_UA_MASTER із Google Drive) лежать десь
    у <base>/03_AUDIO/ (підпапка не важлива).

Запуск (у Terminal):
  python3 build_sem_project.py
  python3 build_sem_project.py --base "/інший/шлях/ai-titans-thoughtcast"
  python3 build_sem_project.py --dry-run     # без Resolve, лише перевірка й FCPXML
"""
import argparse
import math
import os
import re
import sys
import wave
from urllib.parse import quote
from xml.sax.saxutils import quoteattr

DEFAULT_BASE = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
PROJECT_NAME = "SEM"
TIMELINE_NAME = "EP01_ActI_UA"

FPS = 24
BAR_S = 60.0 / 92 * 4          # такт 92 BPM = 2.6087 с
BAR_F = BAR_S * FPS            # 62.6087 кадра


def fr(bar):
    return int(round(bar * BAR_F))


def t(frames):
    return f"{frames * 100}/2400s"


# --- План Акту I: (такт початку, такт кінця, тип, ім'я файлу або None, маркер) ---
FL = "ep01_flow_%s.mp4"
PLAN = [
    (0, 3, "video", "ep01_flow_01_mac_chassis.mp4", None),
    (3, 6, "video", "EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4", None),
    (6, 9, "still", "EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg", None),
    (9, 12, "still", "EP01_IMG_ARCH_06_Altman_Childhood_Macintosh_LC_II_1993.jpg", None),
    (12, 15, "still", "EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg", None),
    (15, 19, "still", "EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg",
     "ЦИТАТА Д02 (накладка тексту, бари 15-18): Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю"),
    (19, 22, "video", "ep01_flow_02_crt_code.mp4", None),
    (22, 25, "still", "EP01_FLOW_IMG_02_CRT_Code_Eye_Reflection_Hero.jpg", None),
    (25, 29, "still", "EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg", None),
    (29, 33, "still", "EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg",
     "ПРОПУСК Д03: потрібен кадр актової зали або сцени. Тимчасово повтор PHOTO 06 (інший кроп)"),
    (33, 37, "still", "EP01_FLOW_STUDY_02E_CRT_Computer_Boardroom_2K.jpg",
     "КОНЦЕПТ-ДОСЛІДЖЕННЯ: перевірте, чи підходить за тоном"),
    (37, 41, "still", "EP01_FLOW_STUDY_01D_Mac_Boardroom_StudyA_2K.jpg", None),
    (41, 44, "still", "EP01_FLOW_IMG_01_Macintosh_LC_II_Keyframe.jpg", None),
    (44, 47, "video", "ep01_flow_03_silicon_laser.mp4", None),
    (47, 51, "still", "EP01_FLOW_IMG_03_Silicon_Wafer_Cyan_Laser_Hero.png", None),
    (51, 55, "still", "EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg", None),
    (55, 59, "still", "EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg", None),
    (59, 64, "still", "EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png", None),
    (64, 69, "still", "EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg", None),
    (69, 73, "gfx", None, "ГРАФІКА Д05: плашка «$43 млн · Green Dot · 2012»"),
    (73, 79, "gfx", None,
     "ГРАФІКА Д05: цитатна плашка «Більшість людей здаються не тому, що їхня ідея хибна…»"),
    (79, 82, "video", "ep01_flow_04_exponential_line.mp4", None),
    (82, 87, "still", "EP01_FLOW_IMG_04_Golden_Exponential_Curve_Hero.png", None),
    (87, 90, "video", "EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4",
     "НИЗЬКА РОЗДІЛЬНІСТЬ: 640x480, апскейл або менший розмір у кадрі"),
    (90, 93, "video", "EP01_VID_ARCH_06_ACT1_24FPS_Altman_2009_Loopt_Era_Portrait.mp4", None),
    (93, 109, "gap", None,
     "РІШЕННЯ ПОТРІБНЕ: 16 тактів (близько 42 с) без голосу і без кадрів. Скоротити Акт I або додати 2-3 плани"),
]
TOTAL_BARS = 109

# Слоти зі сценарію (початок, с) і очікувані такти старту голосу з плану
VO_SLOT_START = {1: 0, 2: 15, 3: 45, 4: 90, 5: 150, 6: 210}
VO_EXPECT_BAR = {1: 0, 2: 7, 3: 25, 4: 44, 5: 59, 6: 81}
# Орієнтовні тривалості (с), якщо WAV не знайдено (лише для --dry-run)
VO_EST = {1: 14.0, 2: 43.9, 3: 45.6, 4: 34.9, 5: 53.4, 6: 16.5}
MUSIC_NAME = "EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav"
MUSIC_EST = 285.0


def index_files(base):
    idx = {}
    for sub in ("03_AUDIO", "05_RAW_FOOTAGE"):
        root = os.path.join(base, sub)
        for dp, _, fns in os.walk(root):
            for fn in fns:
                if fn.startswith("."):
                    continue
                idx.setdefault(fn, os.path.join(dp, fn))
    return idx


def find_vo(idx, n):
    pat = re.compile(rf"^EP01_VO_UA_{n:02d}_.*\.wav$")
    for name, path in sorted(idx.items()):
        if pat.match(name):
            return path
    return None


def wav_info(path):
    """(тривалість с, канали, частота) або None, якщо wave не читає файл."""
    try:
        with wave.open(path, "rb") as w:
            return w.getnframes() / float(w.getframerate()), w.getnchannels(), w.getframerate()
    except Exception:
        return None


def url(path):
    return "file://" + quote(os.path.abspath(path))


def build_fcpxml(base, idx, log):
    """Повертає (xml_text, попередження)."""
    warn = []
    total_f = fr(TOTAL_BARS)
    assets = {}     # id -> xml
    order = []
    next_id = [1]

    def asset_for(path, kind, dur_f, chans=2, rate=48000):
        key = (path, kind)
        if key in assets:
            return assets[key][0]
        aid = f"a{next_id[0]}"
        next_id[0] += 1
        name = quoteattr(os.path.splitext(os.path.basename(path))[0])
        src = quoteattr(url(path))
        if kind == "still":
            xml = (f'<asset id="{aid}" name={name} src={src} start="0s" duration="0s" hasVideo="1" format="r1"/>')
        elif kind == "video":
            xml = (f'<asset id="{aid}" name={name} src={src} start="0s" duration="{t(dur_f)}" '
                   f'hasVideo="1" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" format="r1"/>')
        else:
            xml = (f'<asset id="{aid}" name={name} src={src} start="0s" duration="{t(dur_f)}" '
                   f'hasAudio="1" audioSources="1" audioChannels="{chans}" audioRate="{rate}"/>')
        assets[key] = (aid, xml)
        order.append(key)
        return aid

    body = []
    missing = []

    # --- візуали (V1, lane 1)
    for b0, b1, kind, fname, marker in PLAN:
        f0, f1 = fr(b0), fr(b1)
        dur = f1 - f0
        if marker:
            body.append(f'<marker start="{t(f0)}" duration="100/2400s" value={quoteattr(marker)}/>')
        if kind in ("gfx", "gap"):
            continue
        path = idx.get(fname)
        if not path:
            missing.append(fname)
            body.append(f'<marker start="{t(f0)}" duration="100/2400s" value={quoteattr("НЕ ЗНАЙДЕНО ФАЙЛ: " + fname)}/>')
            continue
        aid = asset_for(path, kind, dur)
        nm = quoteattr(os.path.splitext(fname)[0])
        if kind == "still":
            body.append(f'<video ref="{aid}" lane="1" offset="{t(f0)}" name={nm} start="0s" duration="{t(dur)}"/>')
        else:
            body.append(f'<asset-clip ref="{aid}" lane="1" offset="{t(f0)}" name={nm} start="0s" '
                        f'duration="{t(dur)}" audioRole="effects"/>')

    # --- голос (A1, lane -1): старт = початок слота або наступний такт після попереднього дубля
    prev_end = 0.0
    vo_report = []
    for n in range(1, 7):
        path = find_vo(idx, n)
        info = wav_info(path) if path else None
        if info:
            dur_s, chans, rate = info
            real = True
        else:
            dur_s, chans, rate = VO_EST[n], 1, 48000
            real = False
            warn.append(f"Д{n:02d}: WAV не знайдено або не читається, взято оцінку {dur_s} с")
        if n == 1:
            start_bar = 0
        else:
            need = max(VO_SLOT_START[n], prev_end + BAR_S)
            start_bar = int(math.ceil(need / BAR_S - 1e-9))
        start_s = start_bar * BAR_S
        prev_end = start_s + dur_s
        if start_bar != VO_EXPECT_BAR[n]:
            warn.append(f"Д{n:02d}: старт на барі {start_bar}, у плані {VO_EXPECT_BAR[n]}. Візуали можуть не збігатися")
        vo_report.append((n, dur_s, start_bar, real))
        if not path:
            missing.append(f"EP01_VO_UA_{n:02d}_*.wav")
            continue
        dur_f = int(math.floor(dur_s * FPS))
        aid = asset_for(path, "audio", int(round(dur_s * FPS)), chans=chans, rate=rate)
        body.append(f'<asset-clip ref="{aid}" lane="-1" offset="{t(fr(start_bar))}" name="VO_UA_{n:02d}" '
                    f'start="0s" duration="{t(dur_f)}" audioRole="dialogue"/>')

    # --- музика (A2, lane -2)
    mpath = idx.get(MUSIC_NAME)
    if mpath:
        minfo = wav_info(mpath)
        mdur = minfo[0] if minfo else MUSIC_EST
        dur_f = min(total_f, int(math.floor(mdur * FPS)))
        aid = asset_for(mpath, "audio", int(round(mdur * FPS)), chans=minfo[1] if minfo else 2,
                        rate=minfo[2] if minfo else 48000)
        body.append(f'<asset-clip ref="{aid}" lane="-2" offset="0s" name="MUS_01_Act1" start="0s" '
                    f'duration="{t(dur_f)}" audioRole="music"/>')
    else:
        missing.append(MUSIC_NAME)

    # маркери голосу
    for n, dur_s, start_bar, real in vo_report:
        body.append(f'<marker start="{t(fr(start_bar))}" duration="100/2400s" value="Д{n:02d} старт (бар {start_bar})"/>')

    res = "\n    ".join(assets[k][1] for k in order)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<fcpxml version="1.8">
  <resources>
    <format id="r1" name="FFVideoFormat3840x2160p24" frameDuration="100/2400s" width="3840" height="2160" colorSpace="1-1-1 (Rec. 709)"/>
    {res}
  </resources>
  <library>
    <event name="SEM_EP01">
      <project name="{TIMELINE_NAME}">
        <sequence format="r1" duration="{t(total_f)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
            <gap name="Akt_I" offset="0s" start="0s" duration="{t(total_f)}">
              {chr(10).join("              " + x for x in body).strip()}
            </gap>
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
    if missing:
        warn.append("Не знайдено на диску: " + "; ".join(sorted(set(missing))))
    return xml, warn


def media_targets(base, idx):
    """Бін -> список файлів для імпорту в медіапул."""
    raw = os.path.join(base, "05_RAW_FOOTAGE")
    aud = os.path.join(base, "03_AUDIO")

    def listdir(path, pred=lambda f: True, exts=(".mp4", ".mov", ".jpg", ".jpeg", ".png", ".wav")):
        if not os.path.isdir(path):
            return []
        return [os.path.join(path, f) for f in sorted(os.listdir(path))
                if not f.startswith(".") and f.lower().endswith(exts) and pred(f)]

    vo = []
    for n in range(1, 18):
        p = find_vo(idx, n)
        if p:
            vo.append(p)
    return [
        ("01_VO_UA", vo),
        ("02_MUSIC", listdir(os.path.join(aud, "suno_stems", "EP01_ALTMAN_SMART_BINS"), exts=(".wav",))),
        ("03_FLOW_VIDEO", listdir(os.path.join(raw, "flow_renders"), lambda f: f.lower().startswith("ep01_"), exts=(".mp4",))),
        ("04_ARCHIVES", listdir(os.path.join(raw, "archives"), lambda f: f.startswith("EP01_VID_"), exts=(".mp4",))),
        ("05_KEYFRAMES", listdir(os.path.join(raw, "flow_images", "EP01_Altman", "01_primary_keyframes"))),
        ("06_BROLL_STUDIES", listdir(os.path.join(raw, "flow_images", "EP01_Altman", "02_broll_stills_and_studies"))),
        ("07_PORTRAITS", listdir(os.path.join(raw, "speaker_portraits", "young_altman"))
         + listdir(os.path.join(raw, "speaker_portraits"), lambda f: f.startswith("EP01_PHOTO_"))),
        ("08_DOSSIERS", listdir(os.path.join(raw, "dossiers_press"), lambda f: f.startswith("EP01_DOC_"))),
    ]


def connect_resolve():
    for p in ("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules",
              os.path.join(os.environ.get("RESOLVE_SCRIPT_API", ""), "Modules")):
        if p and p not in sys.path:
            sys.path.append(p)
    import DaVinciResolveScript as bmd
    return bmd.scriptapp("Resolve")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=DEFAULT_BASE)
    ap.add_argument("--xml-out", default=None, help="куди зберегти FCPXML")
    ap.add_argument("--dry-run", action="store_true", help="без Resolve")
    a = ap.parse_args()

    log = print
    if not os.path.isdir(a.base):
        log(f"Папку не знайдено: {a.base}")
        if not a.dry_run:
            sys.exit(1)
    idx = index_files(a.base) if os.path.isdir(a.base) else {}
    log(f"Проіндексовано файлів: {len(idx)}")

    xml, warn = build_fcpxml(a.base, idx, log)
    xml_out = a.xml_out or os.path.join(a.base if os.path.isdir(a.base) else ".", "EP01_ActI_UA.fcpxml")
    with open(xml_out, "w", encoding="utf-8") as f:
        f.write(xml)
    log(f"FCPXML збережено: {xml_out}")
    for w in warn:
        log("УВАГА: " + w)

    if a.dry_run:
        log("Dry-run: Resolve не чіпаю.")
        return

    resolve = connect_resolve()
    if resolve is None:
        log("Не вдалося підключитися до Resolve. Перевірте, що він відкритий і увімкнено External scripting (Local).")
        sys.exit(1)
    pm = resolve.GetProjectManager()
    proj = pm.CreateProject(PROJECT_NAME)
    if proj is None:
        log(f"Проєкт «{PROJECT_NAME}» уже існує, відкриваю його.")
        proj = pm.LoadProject(PROJECT_NAME)
    if proj is None:
        log("Не вдалося створити чи відкрити проєкт.")
        sys.exit(1)
    for k, v in (("timelineFrameRate", "24"), ("timelineResolutionWidth", "3840"),
                 ("timelineResolutionHeight", "2160")):
        proj.SetSetting(k, v)

    mp = proj.GetMediaPool()
    root = mp.GetRootFolder()

    def subfolder(parent, name):
        for s in parent.GetSubFolderList():
            if s.GetName() == name:
                return s
        return mp.AddSubFolder(parent, name)

    total = 0
    for bin_name, files in media_targets(a.base, idx):
        if not files:
            log(f"- {bin_name}: файлів не знайдено, пропускаю")
            continue
        mp.SetCurrentFolder(subfolder(root, bin_name))
        items = mp.ImportMedia(files)
        n = len(items) if items else 0
        total += n
        log(f"✓ {bin_name}: імпортовано {n} з {len(files)}")
    mp.SetCurrentFolder(root)

    name = TIMELINE_NAME
    existing = {proj.GetTimelineByIndex(i).GetName() for i in range(1, proj.GetTimelineCount() + 1)}
    k = 2
    while name in existing:
        name = f"{TIMELINE_NAME}_v{k}"
        k += 1
    tl = mp.ImportTimelineFromFile(xml_out, {"timelineName": name, "importSourceClips": True})
    if tl:
        proj.SetCurrentTimeline(tl)
        log(f"✓ Таймлайн «{name}» створено")
    else:
        log("Таймлайн не імпортовано автоматично. Зробіть вручну: File > Import > Timeline > "
            f"{xml_out}")
    pm.SaveProject()
    log(f"Готово. Імпортовано в медіапул: {total}. Проєкт «{PROJECT_NAME}» збережено.")


if __name__ == "__main__":
    main()
