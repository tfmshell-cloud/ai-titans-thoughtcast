#!/usr/bin/env python3
"""Чернетка трейлера сезону 1 «Архітектори Розуму / AI Titans» (UA) — на рушії EP01.

Сітка 92 BPM (такт 2,61 с), склейки в такт, 10 героїв у порядку епізодів, текстові картки з фразами
сценарію (02_SCRIPTS/trailer_s1/TRAILER_S1_SCRIPT.md), музика з бібліотеки Suno проєкту.
Озвучки ще немає: репліки диктора стоять маркерами на таймлайні.
    python3 08_AUTOMATION/build_trailer_s1.py [--resolve]
"""
import argparse
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ep01_engine as E                      # noqa: E402

F = E.FPS
B = E.bar
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CARD_DIR = os.path.join(E.BASE, "05_RAW_FOOTAGE", "claude_graphics", "trailer_s1")
TIMELINE = "TRAILER_S1_UA_Draft"
MIX = os.path.join(E.BASE, "03_AUDIO", "claude_mix", "TRAILER_S1_MUS_UA_Draft.wav")

# ---------------------------------------------------------------- текстові картки (4K)
CARDS = {
    "01": ("КОЖНА ЕПОХА", "МАЄ СВОЇХ АРХІТЕКТОРІВ", ""),
    "02": ("НАША —", "БУДУЄ РОЗУМ,", "СИЛЬНІШИЙ ЗА ЛЮДСЬКИЙ"),
    "03": ("ВОНИ КИНУЛИ ВИКЛИК", "УСЬОМУ СВІТУ", ""),
    "04": ("П'ЯТНИЦЯ,", "17 ЛИСТОПАДА", ""),
    "05": ("ХТО ПРИБОРКАЄ ВОГОНЬ,", "ЩО ВМІЄ ДУМАТИ?", ""),
    "TITLE": ("АРХІТЕКТОРИ РОЗУМУ", "AI TITANS", "СЕЗОН 1"),
    "END": ("10 ЕПІЗОДІВ", "ДЕСЯТЬ ЛЮДЕЙ. ОДНА ТЕХНОЛОГІЯ.", "ПІДПИШИСЬ"),
}


def card_html(a, b, c, title=False):
    big = 230 if title else 150
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:3840px;height:2160px;background:radial-gradient(ellipse at 50% 45%,#1C1F26 0%,#0B0D10 62%);}}
.w{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;text-transform:uppercase;text-align:center}}
.a{{color:#E8E2D0;font-weight:300;font-size:{int(big * .62)}px;letter-spacing:.18em;margin-bottom:28px}}
.b{{color:#D4AF37;font-weight:600;font-size:{big}px;letter-spacing:.08em;text-shadow:0 0 60px rgba(212,175,55,.35)}}
.c{{color:#00F5D4;font-weight:400;font-size:{int(big * .40)}px;letter-spacing:.42em;margin-top:56px;opacity:.9}}
.line{{width:900px;height:2px;margin:70px auto 0;background:linear-gradient(90deg,transparent,#D4AF37,transparent)}}
</style></head><body><div class="w"><div class="a">{a}</div><div class="b">{b}</div>
{'<div class="line"></div>' if title else ''}<div class="c">{c}</div></div></body></html>"""


def make_cards():
    os.makedirs(CARD_DIR, exist_ok=True)
    tmp = os.path.join(CARD_DIR, "_html")
    os.makedirs(tmp, exist_ok=True)
    for k, (a, b, c) in CARDS.items():
        png = os.path.join(CARD_DIR, f"TRAILER_S1_CARD_{k}_UA.png")
        if os.path.exists(png):
            continue
        h = os.path.join(tmp, f"{k}.html")
        open(h, "w", encoding="utf-8").write(card_html(a, b, c, title=(k == "TITLE")))
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=3840,2160",
                        "--force-device-scale-factor=1", f"--screenshot={png}", "file://" + h],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("  картка", os.path.basename(png))


def card(k):
    return f"TRAILER_S1_CARD_{k}_UA.png"


# ---------------------------------------------------------------- план (такт, файл/префікс, вхід с, нотатка)
ORIGINS = [   # 1 такт на героя, порядок епізодів
    ("EP01_V2_ARCH_06_Childhood_Mac_10s.mp4", 1.0, "01 Альтман — хлопчик і перший Macintosh"),
    ("EP02_VID_ARCH_04", 4.0, "02 Хуанг — посудомийник у Denny's"),
    ("EP03_VID_ARCH_03", 3.0, "03 Гассабіс — шаховий вундеркінд у 4 роки"),
    ("EP04_VID_ARCH_07", 5.0, "04 Гінтон — нейронаука 1980-х"),
    ("EP05_VID_ARCH_04", 5.0, "05 ЛеКун — згорткова мережа 1989"),
    ("EP06_VID_ARCH_03", 5.0, "06 Суцкевер — студент Гінтона в Торонто"),
    ("EP07_VID_ARCH_02", 5.0, "07 Амодей — шлях через біофізику"),
    ("EP08_VID_ARCH_04", 5.0, "08 Фей-Фей Лі — пральня між лекціями"),
    ("EP09_VID_ARCH_05", 37.0, "09 Бенжіо — «зима ШІ», мережі покинуті"),
    ("EP10_VID_ARCH_02", 5.0, "10 Ин — Stanford CS229, 2008"),
]
WAR = [       # пів такту
    ("EP04_VID_ARCH_09", 4.0, "AlexNet: аукціон DNNresearch"),
    ("Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4", 3.0, "нейрон → чип GPU"),
    ("EP02_VID_ARCH_01", 1.0, "Хуанг виходить на сцену GTC"),
    ("EP02_VID_ARCH_02", 2.0, "пластина Blackwell"),
    ("EP03_VID_ARCH_02", 1.0, "AlphaGo, хід 37 — реакція залу"),
    ("EP03_VID_ARCH_14", 26.0, "AlphaFold — згортання білка"),
    ("EP08_VID_ARCH_01", 1.0, "ImageNet на сцені"),
    ("EP09_VID_ARCH_09", 8.0, "Бенжіо — механізм уваги"),
    ("EP06_VID_ARCH_12", 6.0, "Суцкевер — емерджентна поведінка GPT"),
    ("EP07_VID_ARCH_05", 6.0, "Амодей — закони масштабування"),
    ("EP10_VID_ARCH_05", 6.0, "Ин — народження Google Brain"),
    ("EP05_VID_ARCH_10", 6.0, "ЛеКун — FAIR і PyTorch, відкритий код"),
]
NOW = [       # пів такту, сьогодення; Альтман — останній
    ("EP02_VID_ARCH_14", 1.0, "Хуанг"), ("EP03_VID_ARCH_01", 1.0, "Гассабіс, Нобелівська лекція"),
    ("EP04_VID_ARCH_16", 4.0, "Гінтон, Нобелівський банкет 2024"), ("EP05_VID_ARCH_16", 6.0, "ЛеКун, Давос 2026"),
    ("EP06_VID_ARCH_15", 4.0, "Суцкевер, 2025"), ("EP07_VID_ARCH_11", 6.0, "Амодей"),
    ("EP08_VID_ARCH_15", 6.0, "Фей-Фей Лі, World Labs"), ("EP09_VID_ARCH_14", 20.0, "Бенжіо, TED 2024"),
    ("EP10_VID_ARCH_16", 6.0, "Ин"), ("EP01_VID_ARCH_05", 4.0, "Альтман"),
]
# репліки диктора (з TRAILER_S1_SCRIPT.md) — маркери, такт старту
VO_LINES = [
    (0, "01", "Кожна епоха має своїх архітекторів."), (2, "02", "Наша — будує розум, сильніший за людський."),
    (3, "03", "Хлопчик, який розібрав свій перший Macintosh."), (4, "04", "Іммігрант, що мив посуд у закусочній Denny's."),
    (5, "05", "Шахове диво, яке в чотири роки обігравало дорослих."), (6, "06", "Тесля, якого наука відкидала тридцять років."),
    (10, "07", "Дівчина, що між лекціями Прінстона прасувала сорочки в пральні."), (13, "08", "Вони кинули виклик усьому світу."),
    (15, "09", "Тридцять днів до банкрутства."), (16, "10", "Хід тридцять сім."),
    (18, "11", "Сто мільйонів людей за два місяці."), (20, "12", "П'ятниця, сімнадцяте листопада. Його звільнено."),
    (22, "13-14", "А потім той, з кого все почалося, сказав: «Частина мене шкодує про справу всього мого життя»."),
    (24, "15", "Одні б'ють на сполох. Інші будують гальма."), (26, "16", "Хто приборкає вогонь, що вміє думати?"),
    (27, "17", "Десять людей. Одна технологія. Майбутнє, яке вже не зупинити."), (33, "18", "Архітектори розуму."),
]


def resolve_name(idx, key):
    if key in idx:
        return key
    hits = sorted(n for n in idx if n.startswith(key + "_") and n.lower().endswith((".mp4", ".mov")))
    if not hits:
        sys.exit(f"не знайдено кліп {key}")
    return hits[0]


def plan(idx):
    v1 = []

    def add(bar_pos, name, si, note):
        v1.append((B(bar_pos), resolve_name(idx, name), si, None, note))
    # холодний вхід
    add(0, card("01"), 0, "Картка: Кожна епоха має своїх архітекторів")
    add(1, "EP01_V1_CREATIVE_08_Gold_Melting_Brain_15s.mp4", 2.0, "Золотий мозок")
    add(2, card("02"), 0, "Картка: Наша — будує розум")
    # походження
    for i, (n, si, note) in enumerate(ORIGINS):
        add(3 + i, n, si, note)
    add(13, card("03"), 0, "Картка: Вони кинули виклик усьому світу")
    for i, (n, si, note) in enumerate(WAR):
        add(14 + i / 2, n, si, note)
    add(20, card("04"), 0, "Картка: П'ятниця, 17 листопада")
    add(21, "EP01_V1_B3_01_Chess_King_Falling_12s.mp4", 2.0, "Падіння шахового короля — Альтмана звільнено")
    # ставка
    add(22, "EP04_VID_ARCH_12", 18.0, "NYT: «Хрещений батько ШІ йде з Google і попереджає» (BBC 2023)")
    add(23, "EP04_VID_ARCH_14", 12.0, "Гінтон крупно — «60 Minutes»")
    add(24, "EP01_VID_ARCH_01", 2.0, "Альтман у Сенаті — присяга")
    add(25, "EP09_VID_ARCH_01", 1.0, "Бенжіо в Сенаті")
    add(25.5, "EP07_VID_ARCH_14", 12.0, "Амодей у Сенаті")
    add(26, card("05"), 0, "Картка: Хто приборкає вогонь")
    # кульмінація: 10 облич
    for i, (n, si, note) in enumerate(NOW):
        add(27 + i / 2, n, si, "Сьогодні: " + note)
    add(32, "EP01_V1_B2_10_Earth_Horizon_Finale_550f.mp4", 4.0, "Земля з орбіти")
    add(33, card("TITLE"), 0, "Назва серіалу")
    add(35, card("END"), 0, "Фінальна картка: 10 епізодів · Підпишись")
    end = B(37)
    music = [
        ("Deep Water Pressure.wav", 0.0, 0, B(3), 1.0),                 # холодний вхід, удар на старті
        ("Clockwork Dread-2.wav", 0.0, B(3), B(22), 0.8),               # походження → війна, наростання
        ("Clockwork Dread-2.wav", 148.0, B(22), B(32), 0.6),            # провал (ставка) → повторний удар на такті 27
        ("Celestial Ascent-2.wav", 160.0, B(32), end, 3.0),             # фінал і назва
    ]
    markers = [(B(b), "Yellow", f"VO {n}", txt) for b, n, txt in VO_LINES]
    markers += [(B(b), "Purple", nm, "") for b, nm in ((0, "ХОЛОДНИЙ ВХІД"), (3, "ПОХОДЖЕННЯ"), (13, "ВІЙНА"),
                                                     (22, "СТАВКА"), (27, "КУЛЬМІНАЦІЯ · 10 ОБЛИЧ"), (32, "ФІНАЛ"))]
    return dict(name="Трейлер S1", end_f=end, vo={}, v1=v1, music=music, markers=markers,
                dissolves={B(3): 8, B(32): 12, B(33): 12, B(35): 12})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve", action="store_true")
    a = ap.parse_args()
    make_cards()
    idx = E.index_files()
    act = plan(idx)
    E.mix_music(act, idx, MIX, gap_db=0.0, duck_db=0.0)   # голосу ще немає — музика на рівні джерела
    idx = E.index_files()
    xml, probs, paths = E.build_fcpxml([(act, 0, MIX)], idx, TIMELINE, fade_in=12, fade_out=36)
    p = os.path.join(E.BASE, "06_DAVINCI_PROJECTS", f"{TIMELINE}.fcpxml")
    open(p, "w", encoding="utf-8").write(xml)
    print(f"Трейлер: {len(act['v1'])} планів, {act['end_f'] / F:.1f} с → {p}")
    for pr in probs:
        print("  УВАГА:", pr)
    for row in E.build_fcpxml.report:
        if row[3] == "сповільнено":
            print(f"    сповільнено ×{row[2]}  {row[1][:60]}")
    if a.resolve:
        E.to_resolve(p, paths, TIMELINE, act["markers"], replace=True)


if __name__ == "__main__":
    main()
