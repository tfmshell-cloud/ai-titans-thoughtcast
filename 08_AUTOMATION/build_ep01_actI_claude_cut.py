#!/usr/bin/env python3
"""
EP01 «Сем Альтман», Акт I — режисерська версія Claude: «РОЗМИТА МЕЖА».

Концепція
  Альтман пише про Mac: «Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою
  реальністю». Це і є візуальна граматика акту: внутрішній світ показано анімацією,
  зовнішній — фотореалізмом і архівом. Кожен поворотний момент героя — це морфінг
  анімації в реальність (кліпи seedance з user_ai_generations):
     Д02  анімований хлопчик біля Mac  → реальний хлопчик розбирає системний блок (на словах цитати)
     Д03  аніме-підліток у церкві з листом → реальний підліток біля мікрофона (coming-out)
     Д04  мультяшний гуртожиток → нічний Стенфорд, рюкзак на плечі («зачиняє двері гуртожитку»)
     Д05  аніме-око → виснажений реальний кодер («межа фізичного виснаження»)
  Фінал акту: хлопчик дорослішає до лідера в серверній → людина, що входить у світловий тунель →
  слово EXPONENTIAL розчиняється у вирі й світанку над містом.

Звук (так Resolve розкладає доріжки після імпорту)
  A1  музика: власний мікс з автоматичним «даккінгом» під голос (див. duck_music)
  A2  живий звук кліпів (CRT, прохід у плату, шурхіт сторінок, вибухи світла, осцилограф)
      + бібліотечні SFX (CRT, клавіатура); звук підлітка біля мікрофона вимкнено
  A3  голос UA (на тактах 2, 9, 27, 46, 61, 83 — 2 такти холодного відкриття)
Картинка
  V1  плани, V2  MGFX-плашки (ProRes 4444), V3  титри (PNG з альфою)

Запуск:
  python3 build_ep01_actI_claude_cut.py            # мікс музики + FCPXML
  python3 build_ep01_actI_claude_cut.py --resolve  # + імпорт у відкритий проєкт SEM
"""
import argparse
import array
import math
import os
import sys
import wave
from urllib.parse import quote
from xml.sax.saxutils import quoteattr

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "06_DAVINCI_PROJECTS", "EP01_ActI_UA_Claude_DirectorsCut.fcpxml")
TIMELINE = "EP01_ActI_UA_Claude_DirectorsCut"
FPS = 24
BAR_F = 60.0 / 92 * 4 * FPS
MUSIC_SRC = "EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav"
MUSIC_MIX = os.path.join(BASE, "03_AUDIO", "claude_mix", "EP01_MUS_01_ACT1_ducked_DirectorsCut.wav")
END_F = int(238.36 * FPS)

VO = {  # файл, такт старту, тривалість с
    1: ("EP01_VO_UA_01_ACT1_00_00_00_15_Pressure_Of_Rules.wav", 2, 14.03),
    2: ("EP01_VO_UA_02_ACT1_00_15_00_45_Macintosh_LC_II_Indifference.wav", 9, 43.89),
    3: ("EP01_VO_UA_03_ACT1_00_45_01_30_John_Burroughs_School.wav", 27, 45.64),
    4: ("EP01_VO_UA_04_ACT1_01_30_02_30_Stanford_Loopt_Genesis.wav", 46, 34.93),
    5: ("EP01_VO_UA_05_ACT1_02_30_03_30_YC_Batch1_Scurvy_Grit.wav", 61, 53.39),
    6: ("EP01_VO_UA_06_ACT1_03_30_04_45_Compound_Interest_Mindset.wav", 83, 16.51),
}


def vo_f(n):
    return int(round(VO[n][1] * BAR_F))


def at(n, rel):
    """Кадр склейки під слово дубля n на rel секунді (різ на 3 кадри раніше слова)."""
    return vo_f(n) + int(round(rel * FPS)) - 3


U = "user_ai_generations/"
# V1: (старт, файл, вхід у джерело с, довжина джерела в кадрах | None=стилл, живий звук dB | None, примітка)
V1 = [
    # ХОЛОДНЕ ВІДКРИТТЯ (2 такти): макро корпусу Mac, логотип виходить на титр «АКТ I»
    (0,             "ep01_flow_01_mac_chassis.mp4", 1.7, 190, None, "холодне відкриття: корпус Macintosh LC II (після стрибка кадру на 1,0–1,3 с джерела)"),
    # Д01 — система
    (at(1, 0.0),    "EP01_CLIP_STILL_Neural_Lattice_10s.mp4", 0, 241, None, "Д01 «тиск правил… коридори середньої школи»"),
    (at(1, 5.84),   "EP01_CLIP_STILL_Young_Altman_Portrait_5s.mp4", 0, 120, None, "Д01 «оцінки… зауваження дорослих і страх»"),
    (at(1, 10.8),   "EP01_V1_CREATIVE_04_Mind_Radiating_Light_12s.mp4", 0, 288, None, "Д01 «карається соромом» — тріснута порцеляна"),
    # Д02 — Macintosh: перша межа
    (at(2, -0.3),   "EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 0, 240, None, "Д02 «У 1993 році…» справжній LC II"),
    (at(2, 2.6),    "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4", 0.6, 239, -12, "Д02 «перший комп'ютер» — CRT вмикається"),
    (at(2, 8.06),   "Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4", 0, 239, -13, "Д02 «Macintosh LC II» → камера всередину → «до материнської плати»"),
    (at(2, 15.88),  "ep01_flow_02_crt_code.mp4", 1.0, 240, None, "Д02 «Через тридцять років він напише»"),
    (at(2, 17.1),   "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4", 0, 121, -12, "Д02 ЦИТАТА «розмила лінію…» — МОРФІНГ анімація→реальність"),
    (at(2, 22.1),   "ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4", 0.6, 121, -15, "Д02 «продовженням моєї думки» — хлопчик розбирає Mac"),
    (at(2, 26.46),  "EP01_CLIP_V1_06_Boy_Room_12s.mp4", 0, 288, None, "Д02 «Комп'ютер навчив його…»"),
    (at(2, 31.72),  "EP01_CLIP_STILL_Boy_Watching_Code_5s.mp4", 0, 120, None, "Д02 «байдужа до авторитетів»"),
    (at(2, 36.22),  "ep01_flow_02_crt_code.mp4", 3.0, 240, None, "Д02 «синтаксична помилка»"),
    (at(2, 40.9),   "EP01_CLIP_V1_07_Phosphor_12s.mp4", 0, 288, None, "Д02 «баг… переписати за п'ять хвилин»"),
    # Д03 — сцена: друга межа
    (at(3, 0.0),    "EP01_V2_ARCH_05_Burroughs_Campus_12s.mp4", 0, 288, None, "Д03 «Джон Берроуз Скул»"),
    (at(3, 5.98),   "EP01_V1_CREATIVE_01_Equations_Void_8s.mp4", 0, 192, None, "Д03 «зрізала кути індивідуальності» — фігура під аркою"),
    (at(3, 10.18),  "EP01_RESTORED_Church_Wide_PushIn_6s.mp4", 0, 144, None, "Д03 «У шістнадцять років…» — крихітна постать у соборі (відновлено 4K)"),
    (at(3, 13.6),   "ElevenLabs_video_seedance-2-5_Slow,_powerful__2026-11-09T12_52_53.mp4", 0, 121, -14, "Д03 «виходить на сцену» — МОРФІНГ аніме→реальність"),
    (at(3, 18.6),   "Teenage_boy_speaking_into_microp…_9259f8fe_1080p.mp4", 0, 239, None, "Д03 «християнською спільнотою… гомосексуальність»"),
    (at(3, 26.16),  "EP01_CLIP_STILL_Math_Decision_Tree_8s.mp4", 0, 185, None, "Д03 «стратегічний розрахунок»"),
    # Young_Altman_School_Auditorium_Microphone_2001_2K.png — JPEG з розширенням .png, Resolve показував битий кадр
    (at(3, 30.18),  "EP01_RESTORED_Church_FrontMic_PushIn_6s.mp4", 0, 144, None, "Д03 «найбільш вразливу правду» — погляд у камеру (відновлено 4K)"),
    (at(3, 34.5),   "EP01_V1_CREATIVE_02_Galaxies_Axons_12s.mp4", 0, 288, None, "Д03 «страх розсіюється»"),
    (at(3, 42.0),   "ep01_flow_08_golden_signatures.mp4", 0, 190, None, "Д03 цитата автономії: вибух світла"),
    # Д04 — Стенфорд: третя межа
    (at(4, 0.0),    "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4", 0, 239, -16, "Д04 «Далі був Стенфорд» — ч/б фото оживає"),
    (at(4, 6.32),   "Walls_dissolving_into_textbook_v…_de18897e_1080p.mp4", 0.4, 239, -13, "Д04 «лекції, семестрові цикли, іспити» — стіни розлітаються"),
    (at(4, 15.76),  "ep01_flow_04_exponential_line.mp4", 0.4, 240, -14, "Д04 «дихав експонентою» — лінія злітає вгору"),
    (at(4, 19.9),   "ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4", 0, 121, -13, "Д04 «зачиняє двері гуртожитку» — МОРФІНГ"),
    (at(4, 24.9),   "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4", 6.0, 239, None, "Д04 «Йому дев'ятнадцять»"),
    (at(4, 27.76),  "EP01_V1_NEW_04_Smartphone_Loopt_16s.mp4", 0, 384, None, "Д04 «засновує Loopt»"),
    (at(4, 31.36),  "Light_point_explodes_into_streaks_0827d703_1080p.mp4", 1.0, 239, -9, "Д04 «геолокація» → мережа світу"),
    # Д05 — Loopt: четверта межа
    (at(5, 0.0),    "EP01_DOC_01_YC_2005_Program_10s.mp4", 0, 240, None, "Д05 «Пол Грем… Y Combinator»"),
    (at(5, 7.26),   "EP01_V2_ARCH_07_Loopt_Founder_12s.mp4", 0, 288, None, "Д05 «перший набір літа 2005»"),
    (at(5, 12.98),  "ElevenLabs_video_seedance-2-5_Intense_macro_r_2026-11-09T12_58_53.mp4", 0, 121, -13, "Д05 «межа виснаження» — МОРФІНГ аніме-око→реальність"),
    (at(5, 17.98),  "EP01_V1_NEW_03_Window_Rain_16s.mp4", 0, 384, None, "Д05 «спить на підлозі офісу, цинга»"),
    (at(5, 24.1),   "EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4", 6.0, 314, None, "Д05 «бореться з операторами» — WWDC 2008 (архів 640x480)"),
    (at(5, 27.2),   "EP01_UA_CARD_09_Green_Dot_43M_2012.png", 0, None, None, "Д05 $43 млн Green Dot"),
    (at(5, 33.5),   "EP01_CLIP_STILL_Altman_2009_Loopt_6s.mp4", 0, 142, None, "Д05 «скромний результат»"),
    (at(5, 39.3),   "EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", 0, 360, None, "Д05 «школа інженерії волі» — золото стає розумом"),
    (at(5, 43.98),  "Laser_forms_text_words_89a267cd_1080p.mp4", 1.0, 239, -14, "Д05 ЦИТАТА — осцилограф пише фразу"),
    (at(5, 47.5),   "EP01_UA_CLIP_CARD_02_Psychological_Friction_18s.mp4", 0, 436, None, "Д05 ЦИТАТА — українська картка"),
    # Д06 — експонента
    (at(6, 0.0),    "Boy_aging_into_tech_leader_cd380219_1080p.mp4", 0, 239, -16, "Д06 «виходить із Loopt…» — хлопчик дорослішає до лідера"),
    (at(6, 6.14),   "EP01_CLIP_V1_19_CurveHero_17s.mp4", 0, 408, None, "Д06 «лінійні проекти на 10%»"),
    (at(6, 10.5),   "Light_point_explodes_into_streaks_c712a46e_1080p.mp4", 0, 239, -10, "Д06 «Справжня сила…» — екран вибухає світлом"),
    (at(6, 16.6),   "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4", 0, 239, -7, "ФІНАЛ: EXPONENTIAL → вир → світанок"),
]

# V2: MGFX-плашки з альфою
V2 = [
    (at(3, 19.5), "EP01_MGFX_01_Burroughs_Turning_Point_10s.mov", 240),
    (at(3, 39.48), "EP01_MGFX_02_Autonomy_Axiom_Quote_12s.mov", None),   # до Д04
]
# V3: титри (PNG з альфою): старт, файл, тривалість с
V3 = [
    (10, "EP01_SUPER_00_Act_I_Title.png", 4.6),
    (at(2, 0.2), "EP01_SUPER_01_St_Louis_1993.png", 3.6),
    (at(4, 0.4), "EP01_SUPER_02_Stanford_2003.png", 3.6),
    (at(5, 7.5), "EP01_SUPER_03_Loopt_2005_2012.png", 4.0),
]
# A4 бібліотечні SFX: старт, файл, тривалість с, dB
SFX = [
    (0, "EP01_ARCH_AUDIO_Macintosh_1992_CRT_Scan.wav", 8.01, -4),
    (at(2, 26.46), "EP01_SFX_Keyboard_Typing_Burst_4s.wav", 4.0, -2),
    (at(5, 17.98), "EP01_SFX_Mechanical_Keyboard_Typing.wav", 6.0, -6),
]
MARKERS = [
    (at(2, 17.1), "Green", "МОРФІНГ 1", "Mac: анімація → реальність точно на словах цитати"),
    (at(3, 13.6), "Green", "МОРФІНГ 2", "Сцена: аніме → реальний підліток біля мікрофона"),
    (at(4, 19.9), "Green", "МОРФІНГ 3", "Гуртожиток → нічний Стенфорд"),
    (at(5, 12.98), "Green", "МОРФІНГ 4", "Аніме-око → виснажений засновник"),
    (at(5, 24.1), "Yellow", "АРХІВ 640x480", "WWDC 2008: справжній рух важливіший за роздільність; за бажання — рамка «архів»"),
    (END_F - 30, "Yellow", "КІНЕЦЬ АКТУ I", "За бажання: Dip to Black 12 кадрів"),
]


# ---------------------------------------------------------------- звук
def find(idx, name):
    """Шлях до файлу; превізи низької роздільності беремо лише якщо іншого немає."""
    ps = sorted(idx.get(name) or [], key=lambda p: ("previs" in p or "alternate" in p, p))
    return ps[0] if ps else None


def read_mono_env(path, block):
    """RMS-обвідна (лінійна) по блоках з частотою 48 кГц."""
    w = wave.open(path)
    ch, sw, sr = w.getnchannels(), w.getsampwidth(), w.getframerate()
    assert sw == 2
    a = array.array("h", w.readframes(w.getnframes()))
    step = int(block * sr / 48000) * ch
    env = []
    for i in range(0, len(a), step):
        seg = a[i:i + step:ch * 3]
        env.append(math.sqrt(sum(x * x for x in seg) / len(seg)) / 32768 if seg else 0)
    return env


def duck_music(idx, log=print):
    """Новий файл музики з даккінгом під голос: -4 dB у паузах, -13 dB під голосом,
    атака 0.15 с, відпуск 0.9 с, упередження 0.12 с, згасання в кінці 3 с. Оригінал не змінюється."""
    src = find(idx, MUSIC_SRC)
    w = wave.open(src)
    ch, sr, n = w.getnchannels(), w.getframerate(), w.getnframes()
    music = array.array("h", w.readframes(n))
    BL = 480                                  # 10 мс
    nb = n // BL + 1
    active = [False] * nb
    for k, (name, bar, secs) in VO.items():
        env = read_mono_env(find(idx, name), BL)
        start_b = int(round(vo_f(k) / FPS * sr / BL))
        for j, v in enumerate(env):
            if v > 10 ** (-42 / 20):
                b = start_b + j
                for q in range(max(0, b - 12), min(nb, b + 1)):   # 120 мс наперед
                    active[q] = True
    g_db, cur = [], -4.0
    att, rel = 9.0 / 15, 9.0 / 90             # dB за блок
    for b in range(nb):
        tgt = -13.0 if active[b] else -4.0
        cur = max(tgt, cur - att) if tgt < cur else min(tgt, cur + rel)
        g_db.append(cur)
    fade_b = int(3.0 * sr / BL)
    for b in range(nb - fade_b, nb):
        g_db[b] += 20 * math.log10(max(1e-4, (nb - b) / fade_b))
    out = array.array("h", bytes(len(music) * 2))
    for b in range(nb):
        g = 10 ** (g_db[b] / 20)
        i0, i1 = b * BL * ch, min(len(music), (b + 1) * BL * ch)
        out[i0:i1] = array.array("h", (int(x * g) for x in music[i0:i1]))
    os.makedirs(os.path.dirname(MUSIC_MIX), exist_ok=True)
    o = wave.open(MUSIC_MIX, "wb")
    o.setnchannels(ch), o.setsampwidth(2), o.setframerate(sr)
    o.writeframes(out.tobytes())
    o.close()
    log(f"Мікс музики: {MUSIC_MIX}")
    return n / sr


# ---------------------------------------------------------------- FCPXML
def t(f):
    return f"{int(f) * 100}/2400s"


def index_files():
    idx = {}
    for sub in ("03_AUDIO", "05_RAW_FOOTAGE"):
        for dp, _, fns in os.walk(os.path.join(BASE, sub)):
            for fn in fns:
                if not fn.startswith("."):
                    idx.setdefault(fn, []).append(os.path.join(dp, fn))
    return idx


def build(idx):
    problems, assets, order = [], {}, []

    def asset(name, kind, dur_f=0, chans=2, path=None):
        key = (name, kind)
        if key in assets:
            return assets[key][0]
        p = path or find(idx, name)
        if not p:
            problems.append(f"не знайдено файл: {name}")
            return None
        if not path and len(idx[name]) > 1 and not all("previs" in q or "alternate" in q for q in idx[name][1:] if q != p):
            problems.append(f"кілька файлів {name}, беру {p}")
        aid = f"r{len(assets) + 2}"
        src, nm = quoteattr("file://" + quote(p)), quoteattr(os.path.splitext(name)[0])
        if kind == "still":
            x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="0s" hasVideo="1" format="r1"/>'
        elif kind == "video":
            x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur_f)}" hasVideo="1" format="r1"/>'
        elif kind == "av":
            x = (f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur_f)}" hasVideo="1" hasAudio="1" '
                 f'audioSources="1" audioChannels="2" audioRate="48000" format="r1"/>')
        else:
            x = (f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur_f)}" hasAudio="1" '
                 f'audioSources="1" audioChannels="{chans}" audioRate="48000"/>')
        assets[key] = (aid, x)
        order.append(key)
        return aid

    spine = []
    for i, (f0, name, src_in, src_len, db, note) in enumerate(V1):
        f1 = V1[i + 1][0] if i + 1 < len(V1) else END_F
        dur, in_f = f1 - f0, int(round(src_in * FPS))
        if dur <= 0:
            problems.append(f"{name}: нульова тривалість")
            continue
        if src_len is not None and in_f + dur > src_len:
            problems.append(f"{name} ({note}): потрібно {dur} кадрів, у джерелі {src_len - in_f}")
        kind = "still" if src_len is None else ("av" if db is not None else "video")
        aid = asset(name, kind, src_len or 0)
        if not aid:
            continue
        tag = "video" if kind == "still" else "asset-clip"
        head = f'<{tag} ref="{aid}" offset="{t(f0)}" name={quoteattr(os.path.splitext(name)[0])} start="{t(in_f)}" duration="{t(dur)}"'
        if kind == "av":
            head += ' audioRole="effects"'
        kids = [f'<adjust-volume amount="{db}dB"/>'] if kind == "av" else []
        spine.append([f0, dur, in_f, head, tag, kids])

    def attach(frame, xml):
        p = next((s for s in spine if s[0] <= frame < s[0] + s[1]), spine[-1])
        p[5].append(xml.replace("@OFF@", t(p[2] + frame - p[0])))

    for f0, name, dur in V2:
        dur = dur or (at(4, 0.0) - f0)
        aid = asset(name, "video", 288)
        if aid:
            attach(f0, f'<asset-clip ref="{aid}" lane="1" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(dur)}"/>')
    for f0, name, secs in V3:
        aid = asset(name, "still")
        if aid:
            attach(f0, f'<video ref="{aid}" lane="2" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(int(secs * FPS))}"/>')
    for n, (name, bar, secs) in VO.items():
        aid = asset(name, "audio", int(round(secs * FPS)), chans=1)
        if aid:
            attach(vo_f(n), f'<asset-clip ref="{aid}" lane="-1" offset="@OFF@" name="VO_UA_{n:02d}" start="0s" duration="{t(int(secs * FPS))}" audioRole="dialogue"/>')
    aid = asset(os.path.basename(MUSIC_MIX), "audio", END_F, path=MUSIC_MIX)
    if aid:
        attach(0, f'<asset-clip ref="{aid}" lane="-2" offset="@OFF@" name="MUS_01_Act1_ducked" start="0s" duration="{t(END_F)}" audioRole="music"/>')
    for f0, name, secs, db in SFX:
        aid = asset(name, "audio", int(round(secs * FPS)))
        if aid:
            attach(f0, f'<asset-clip ref="{aid}" lane="-3" offset="@OFF@" name={quoteattr(os.path.splitext(name)[0])} start="0s" duration="{t(int(secs * FPS))}" audioRole="effects"><adjust-volume amount="{db}dB"/></asset-clip>')

    body = []
    for f0, dur, in_f, head, tag, kids in spine:
        body += ([head + ">"] + ["  " + k for k in kids] + [f"</{tag}>"]) if kids else [head + "/>"]
    res = "\n    ".join(assets[k][1] for k in order)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.8">
  <resources>
    <format id="r1" name="FFVideoFormat3840x2160p24" frameDuration="100/2400s" width="3840" height="2160" colorSpace="1-1-1 (Rec. 709)"/>
    {res}
  </resources>
  <library>
    <event name="SEM_EP01_Claude_DC">
      <project name="{TIMELINE}">
        <sequence format="r1" duration="{t(END_F)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
            {(chr(10) + "            ").join(body)}
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
    paths = [MUSIC_MIX] + [find(idx, n) for _, n, *_ in V1 + V2 + V3 + SFX] + [find(idx, v[0]) for v in VO.values()]
    return xml, problems, sorted({p for p in paths if p})


# ---------------------------------------------------------------- Resolve
def to_resolve(xml_path, paths):
    sys.path.append("/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules")
    import DaVinciResolveScript as bmd
    r = bmd.scriptapp("Resolve")
    if r is None:
        sys.exit("Resolve не відповідає: відкрийте його й увімкніть External scripting = Local.")
    pm = r.GetProjectManager()
    p = pm.GetCurrentProject()
    if not p or p.GetName() != "SEM":
        p = pm.LoadProject("SEM")
    mp = p.GetMediaPool()
    root = mp.GetRootFolder()
    folders, have = [], set()

    def walk(f):
        folders.append(f)
        for c in f.GetClipList() or []:
            fp = c.GetClipProperty("File Path")
            if fp:
                have.add(fp)
        for s in f.GetSubFolderList() or []:
            walk(s)
    walk(root)
    missing = [x for x in paths if x not in have]
    if missing:      # нові файли (мікс, титри) — у окремий бін
        b = next((s for s in root.GetSubFolderList() if s.GetName() == "21_CLAUDE_DIRECTORS_CUT"), None) \
            or mp.AddSubFolder(root, "21_CLAUDE_DIRECTORS_CUT")
        mp.SetCurrentFolder(b)
        mp.ImportMedia(missing)
        folders = []
        walk(root)
    mp.SetCurrentFolder(root)
    names = {p.GetTimelineByIndex(i).GetName() for i in range(1, p.GetTimelineCount() + 1)}
    name, k = TIMELINE, 2
    while name in names:
        name, k = f"{TIMELINE}_v{k}", k + 1
    tl = mp.ImportTimelineFromFile(xml_path, {"timelineName": name, "importSourceClips": False,
                                              "sourceClipsFolders": folders})
    if not tl:
        sys.exit(f"Імпорт не вдався. Вручну: File > Import > Timeline > {xml_path}")
    s0 = tl.GetStartFrame()
    for n in VO:
        tl.AddMarker(s0 + vo_f(n), "Blue", f"Д{n:02d}", VO[n][0], 1)
    for f0, col, nm, note in MARKERS:
        tl.AddMarker(s0 + f0, col, nm, note, 1)
    items = [i for kk in ("video", "audio") for nn in range(1, tl.GetTrackCount(kk) + 1)
             for i in (tl.GetItemListInTrack(kk, nn) or [])]
    bad = [i.GetName() for i in items if i.GetMediaPoolItem() is None]
    p.SetCurrentTimeline(tl)
    pm.SaveProject()
    print(f"✓ Таймлайн «{name}» у проєкті SEM; без медіа: {bad or 'немає'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--skip-mix", action="store_true", help="не перераховувати мікс музики")
    a = ap.parse_args()
    idx = index_files()
    if not (a.skip_mix and os.path.exists(MUSIC_MIX)):
        duck_music(idx)
    xml, problems, paths = build(idx)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"FCPXML: {OUT}  ({len(V1)} планів, {END_F / FPS:.1f} с)")
    for pr in problems:
        print("УВАГА:", pr)
    if a.resolve:
        to_resolve(OUT, paths)


if __name__ == "__main__":
    main()
