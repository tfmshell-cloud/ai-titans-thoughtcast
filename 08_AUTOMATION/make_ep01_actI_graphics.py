#!/usr/bin/env python3
"""Титри-накладки (PNG з альфою, 3840x2160) для EP01 Акт I «Розмита межа».
Стиль серії: тонка помаранчева лінія, моноширинний заголовок, білий гротеск."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "05_RAW_FOOTAGE", "claude_graphics")
W, H = 3840, 2160
MONO = "/System/Library/Fonts/Menlo.ttc"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
ORANGE = (242, 150, 40, 255)


def font(path, size, idx=0):
    return ImageFont.truetype(path, size, index=idx)


def shadowed(d, xy, text, f, fill):
    x, y = xy
    for dx, dy, a in ((0, 4, 150), (0, 2, 120)):
        d.text((x + dx, y + dy), text, font=f, fill=(0, 0, 0, a))
    d.text(xy, text, font=f, fill=fill)


def super_place(name, kicker, line):
    """Нижній лівий титр місця/року."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x, y = 230, 1700
    d.rectangle([x, y, x + 140, y + 6], fill=ORANGE)
    shadowed(d, (x, y + 40), kicker, font(MONO, 44), (242, 160, 60, 255))
    shadowed(d, (x, y + 110), line, font(SANS, 96, 1), (240, 240, 240, 255))
    im.save(os.path.join(OUT, name))


def act_title(name, act="АКТ I", subtitle="ПОХОДЖЕННЯ ТА КРЕМНІЄВИЙ ЩИТ", kicker="THOUGHTCAST // AI TITANS // EP01: СЕМ АЛЬТМАН"):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x, y = 230, 1480
    d.rectangle([x, y, x + 220, y + 7], fill=ORANGE)
    shadowed(d, (x, y + 45), kicker, font(MONO, 46), (210, 214, 220, 255))
    shadowed(d, (x - 8, y + 120), act, font(SANS, 230, 1), (245, 245, 245, 255))
    shadowed(d, (x, y + 390), subtitle, font(SANS, 84), (242, 160, 60, 255))
    im.save(os.path.join(OUT, name))


def rule_super(name, num, text):
    """Велике правило зліва: номер помаранчевим, текст білим."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x, y = 230, 1420
    shadowed(d, (x - 6, y), num, font(SANS, 300, 1), ORANGE)
    d.rectangle([x + 260, y + 120, x + 380, y + 126], fill=ORANGE)
    words, lines, cur = text.split(), [], ""
    for w in words:                       # перенос на 2 рядки
        if len(cur + " " + w) > 25 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    for i, ln in enumerate(lines):
        shadowed(d, (x + 260, y + 150 + i * 120), ln, font(SANS, 104, 1), (245, 245, 245, 255))
    im.save(os.path.join(OUT, name))


def end_card(name):
    im = Image.new("RGB", (W, H), (8, 9, 12))
    d = ImageDraw.Draw(im)
    cx = W // 2
    for txt, f, col, y in (("THOUGHTCAST // AI TITANS", font(MONO, 54), (150, 156, 166), 820),
                           ("СЕМ АЛЬТМАН", font(SANS, 210, 1), (245, 245, 245), 920),
                           ("АНАТОМІЯ ЕКСПОНЕНТИ", font(SANS, 92), (242, 160, 60), 1180),
                           ("ЕПІЗОД 01 / 10", font(MONO, 48), (110, 116, 126), 1360)):
        w = d.textlength(txt, font=f)
        d.text((cx - w / 2, y), txt, font=f, fill=col)
    d.rectangle([cx - 110, 1320, cx + 110, 1326], fill=ORANGE[:3])
    im.save(os.path.join(OUT, name))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    act_title("EP01_SUPER_00_Act_I_Title.png")
    act_title("EP01_SUPER_10_Act_II_Title.png", "АКТ II", "КОД ЕКСПОНЕНТИ ТА НАРОДЖЕННЯ OPENAI")
    act_title("EP01_SUPER_20_Act_III_Title.png", "АКТ III", "ЗЕМЛЕТРУС І П'ЯТЬ ДНІВ БУНТУ")
    act_title("EP01_SUPER_30_Act_IV_Title.png", "АКТ IV", "КОДЕКС БУДІВНИЧОГО ТА ГОРИЗОНТ AGI")
    super_place("EP01_SUPER_01_St_Louis_1993.png", "// МІССУРІ, США", "СЕНТ-ЛУЇС · 1993")
    super_place("EP01_SUPER_02_Stanford_2003.png", "// КАЛІФОРНІЯ, США", "СТЕНФОРД · 2003")
    super_place("EP01_SUPER_03_Loopt_2005_2012.png", "// МАУНТІН-В'Ю", "LOOPT · 2005–2012")
    super_place("EP01_SUPER_11_YC_2014.png", "// Y COMBINATOR", "ПРЕЗИДЕНТ YC · 2014")
    super_place("EP01_SUPER_12_Rosewood_2015.png", "// ГОТЕЛЬ ROSEWOOD", "МЕНЛО-ПАРК · 2015")
    super_place("EP01_SUPER_13_SF_2019.png", "// OPENAI LP", "САН-ФРАНЦИСКО · 2019")
    super_place("EP01_SUPER_21_ChatGPT_2022.png", "// RESEARCH PREVIEW", "30 ЛИСТОПАДА 2022")
    super_place("EP01_SUPER_22_Friday_Nov17.png", "// 12:00 ЗА ТИХООКЕАНСЬКИМ ЧАСОМ", "П'ЯТНИЦЯ · 17 ЛИСТОПАДА 2023")
    super_place("EP01_SUPER_23_120_Hours.png", "// КРЕМНІЄВА ДОЛИНА", "120 ГОДИН")
    super_place("EP01_SUPER_24_Wednesday_Nov22.png", "// ПОВЕРНЕННЯ", "СЕРЕДА · 22 ЛИСТОПАДА 2023")
    rule_super("EP01_RULE_A_Belief.png", "1", "Не бійтеся ірраціональної віри в себе")
    rule_super("EP01_RULE_B_Code.png", "2", "Дивіться на проблеми як на код")
    rule_super("EP01_RULE_C_Exponent.png", "3", "Обирайте експоненту")
    end_card("EP01_END_CARD.png")
    print("ok:", len([f for f in os.listdir(OUT) if f.startswith("EP01_")]))
