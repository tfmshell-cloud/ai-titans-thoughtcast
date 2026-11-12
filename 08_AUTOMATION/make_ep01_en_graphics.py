#!/usr/bin/env python3
"""Англійські версії всієї мовної графіки EP01 (той самий стиль, що й українська).

Титри місць і дат, назви актів, три правила, фінальна картка → 05_RAW_FOOTAGE/claude_graphics/*_EN.png
Картки-цитати → 05_RAW_FOOTAGE/dossiers_press/english_quote_cards/ + кліпи 4K у rendered_cinematic_stills_4k/
Плашки MGFX (ProRes 4444 з альфою) → rendered_cinematic_stills_4k/EP01_MGFX_0N_..._EN.mov
Тексти цитат — дослівно з 02_SCRIPTS/episode_01_altman/EP01_VO_EN_ELEVENLABS_MASTER.txt.
UA_TO_EN — відповідність файлів для build_ep01_en.py.
Запуск: python3 08_AUTOMATION/make_ep01_en_graphics.py
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "scripts"))
BASE = os.path.dirname(HERE)
CG = os.path.join(BASE, "05_RAW_FOOTAGE", "claude_graphics")
QC = os.path.join(BASE, "05_RAW_FOOTAGE", "dossiers_press", "english_quote_cards")
STILLS = os.path.join(BASE, "05_RAW_FOOTAGE", "rendered_cinematic_stills_4k")
FFMPEG = os.path.expanduser("~/Library/Python/3.9/bin/ffmpeg")
W, H = 3840, 2160
MONO = "/System/Library/Fonts/Menlo.ttc"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
GEORGIA_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
ORANGE = (242, 150, 40, 255)
ACCENT = (245, 185, 65, 255)

ACTS = [("EP01_SUPER_00_Act_I_Title", "ACT I", "ORIGINS AND THE SILICON SHIELD"),
        ("EP01_SUPER_10_Act_II_Title", "ACT II", "THE EXPONENTIAL CODE AND THE BIRTH OF OPENAI"),
        ("EP01_SUPER_20_Act_III_Title", "ACT III", "THE EARTHQUAKE AND FIVE DAYS OF REVOLT"),
        ("EP01_SUPER_30_Act_IV_Title", "ACT IV", "THE BUILDER'S CODE AND THE AGI HORIZON")]
PLACES = [("EP01_SUPER_01_St_Louis_1993", "// MISSOURI, USA", "ST. LOUIS · 1993"),
          ("EP01_SUPER_02_Stanford_2003", "// CALIFORNIA, USA", "STANFORD · 2003"),
          ("EP01_SUPER_03_Loopt_2005_2012", "// MOUNTAIN VIEW", "LOOPT · 2005–2012"),
          ("EP01_SUPER_11_YC_2014", "// Y COMBINATOR", "YC PRESIDENT · 2014"),
          ("EP01_SUPER_12_Rosewood_2015", "// ROSEWOOD HOTEL", "MENLO PARK · 2015"),
          ("EP01_SUPER_13_SF_2019", "// OPENAI LP", "SAN FRANCISCO · 2019"),
          ("EP01_SUPER_21_ChatGPT_2022", "// RESEARCH PREVIEW", "NOVEMBER 30, 2022"),
          ("EP01_SUPER_22_Friday_Nov17", "// 12:00 PACIFIC TIME", "FRIDAY · NOVEMBER 17, 2023"),
          ("EP01_SUPER_23_120_Hours", "// SILICON VALLEY", "120 HOURS"),
          ("EP01_SUPER_24_Wednesday_Nov22", "// THE RETURN", "WEDNESDAY · NOVEMBER 22, 2023")]
RULES = [("EP01_RULE_A_Belief", "1", "Do not fear irrational self-belief"),
         ("EP01_RULE_B_Code", "2", "Treat problems like code"),
         ("EP01_RULE_C_Exponent", "3", "Choose the exponential")]
# (UA png, UA кліп, EN назва, категорія, цитата, автор, колір, кегль)
CARDS = [
    ("EP01_UA_CARD_01_Extension_Of_Thought_Macintosh", "EP01_UA_CLIP_CARD_01_Extension_Of_Thought_12s", "EP01_EN_CARD_01_Extension_Of_Thought_Macintosh",
     "Childhood insight // 1993 Macintosh LC II", "“This machine blurred the line between my internal world and external reality. It became an extension of my thought.”", "— Sam Altman", (245, 185, 65), 66),
    ("EP01_UA_CARD_02_Psychological_Friction_Loopt", "EP01_UA_CLIP_CARD_02_Psychological_Friction_18s", "EP01_EN_CARD_02_Psychological_Friction_Loopt",
     "The Loopt years // Engineering of will", "“Most people do not quit because their idea is wrong. They quit because they cannot endure the psychological friction of relentless rejection.”", "— Sam Altman // 2012", (255, 170, 50), 64),
    ("EP01_UA_CARD_03_Exponential_Risk_Manifesto", "EP01_UA_CLIP_CARD_03_Exponential_Risk_15s", "EP01_EN_CARD_03_Exponential_Risk_Manifesto",
     "YC President's manifesto // 2014", "“People catastrophically underestimate the risk of standing still in an exponential world.”", "— Sam Altman // Manifesto", (64, 224, 208), 66),
    ("EP01_UA_CARD_04_Compute_Equations_Microsoft", "EP01_UA_CLIP_CARD_04_Compute_Equations_18s", "EP01_EN_CARD_04_Compute_Equations_Microsoft",
     "Restructuring OpenAI // 2019", "“We cannot save the world if we cannot afford the compute to verify our own equations.”", "— Sam Altman // The Microsoft deal", (50, 220, 150), 66),
    ("EP01_UA_CARD_05_Guest_Badge_Nov2023", "EP01_UA_CLIP_CARD_05_Guest_Badge_8s", "EP01_EN_CARD_05_Guest_Badge_Nov2023",
     "Crisis of November 17, 2023 // 120 Hours", "“First and last time I ever wear one of these.”", "— Sam Altman // San Francisco, November 19, 2023", (255, 90, 95), 70),
    ("EP01_UA_CARD_06_730_Employees_Ultimatum", "EP01_UA_CLIP_CARD_06_730_Employees_11s", "EP01_EN_CARD_06_730_Employees_Ultimatum",
     "An open ultimatum // November 20, 2023", "“Resign and reinstate Sam Altman, or we all walk out to join him.”", "— 730 of 770 OpenAI employees", (255, 215, 0), 66),
    ("EP01_UA_CARD_07_Three_Rules_Exponential_Life", "EP01_UA_CLIP_CARD_07_Three_Rules_12s", "EP01_EN_CARD_07_Three_Rules_Exponential_Life",
     "Lessons of a trajectory // Three exponential rules", "1. Do not fear irrational self-belief.\n2. Treat problems like code.\n3. Choose the exponential.", "— Laws for architecting your own life", (200, 225, 255), 66),
    ("EP01_UA_CARD_08_Plastic_Reality_Finale", "EP01_UA_CLIP_CARD_08_Plastic_Reality_10s", "EP01_EN_CARD_08_Plastic_Reality_Finale",
     "Finale // The malleability of reality", "“The world is far more malleable than you were taught as a child. Its rules were not etched in stone — they were authored by humans no smarter than you.”", "— Sam Altman // Episode finale", (255, 200, 80), 64),
]
MGFX = [("EP01_MGFX_01_Burroughs_Turning_Point_10s", 10.0, "title",
         "JOHN BURROUGHS SCHOOL  •  ST. LOUIS, 2001", "STRATEGIC TURNING POINT: DISARMING THE SYSTEM",
         "Coming out before the school assembly: taking away the levers of fear and the crowd's judgment",
         "DOCUMENTARY DOSSIER // ACT 1 // ARCHIVE 2001"),
        ("EP01_MGFX_02_Autonomy_Axiom_Quote_12s", 12.0, "quote",
         "AXIOM OF AUTONOMY  •  SAM ALTMAN (AGE 16)",
         "“True autonomy is seized the moment you strip the crowd of its power to evaluate your worth.”",
         "— The foundation of the future OpenAI founder's psychological resilience", "")]


def font(path, size, idx=0):
    return ImageFont.truetype(path, size, index=idx)


def ua_to_en():
    m = {}
    for n, *_ in ACTS + PLACES + RULES:
        m[n + ".png"] = n + "_EN.png"
    m["EP01_END_CARD.png"] = "EP01_END_CARD_EN.png"
    for ua_png, ua_clip, en, *_ in CARDS:
        m[ua_clip + ".mp4"] = ua_clip.replace("_UA_", "_EN_") + ".mp4"
    m["EP01_UA_CARD_09_Green_Dot_43M_2012.png"] = "EP01_EN_CARD_09_Green_Dot_43M_2012.png"
    for n, *_ in MGFX:
        m[n + ".mov"] = n + "_EN.mov"
    return m


UA_TO_EN = ua_to_en()


def supers():
    import make_ep01_actI_graphics as G
    G.OUT = CG
    for n, act, sub in ACTS:
        G.act_title(n + "_EN.png", act, sub, "THOUGHTCAST // AI TITANS // EP01: SAM ALTMAN")
    for n, kick, line in PLACES:
        G.super_place(n + "_EN.png", kick, line)
    for n, num, text in RULES:
        G.rule_super(n + "_EN.png", num, text)
    im = Image.new("RGB", (W, H), (8, 9, 12))
    d = ImageDraw.Draw(im)
    cx = W // 2
    for txt, f, col, y in (("THOUGHTCAST // AI TITANS", font(MONO, 54), (150, 156, 166), 820),
                           ("SAM ALTMAN", font(SANS, 210, 1), (245, 245, 245), 920),
                           ("ANATOMY OF THE EXPONENT", font(SANS, 92), (242, 160, 60), 1180),
                           ("EPISODE 01 / 10", font(MONO, 48), (110, 116, 126), 1360)):
        d.text((cx - d.textlength(txt, font=f) / 2, y), txt, font=f, fill=col)
    d.rectangle([cx - 110, 1320, cx + 110, 1326], fill=ORANGE[:3])
    im.save(os.path.join(CG, "EP01_END_CARD_EN.png"))


def cards():
    import render_ukrainian_quote_cards as Q
    os.makedirs(QC, exist_ok=True)
    Q.out_dir = QC
    import render_exact_cinematic_stills_to_video as R      # тривалості UA-кліпів
    durs = {os.path.splitext(c[1])[0]: c[2] for c in R.STILLS_MANIFEST}
    for ua_png, ua_clip, en, cat, q, a, col, fs in CARDS:
        Q.draw_quote_card(en + ".png", cat, q, a, col, fs)
        secs = durs.get(ua_clip) or clip_secs(os.path.join(STILLS, ua_clip + ".mp4"))
        out = os.path.join(STILLS, ua_clip.replace("_UA_", "_EN_") + ".mp4")
        frames = int(round(secs * 24))
        vf = (f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,"
              f"zoompan=z='min(zoom+0.00015,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=3840x2160:fps=24")
        subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-loop", "1", "-i", os.path.join(QC, en + ".png"),
                        "-vf", vf, "-frames:v", str(frames), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16",
                        "-preset", "medium", "-r", "24", out], check=True)
        print("  картка", os.path.basename(out), f"{secs:.2f} с")


def clip_secs(path):
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", path], capture_output=True, text=True).stderr
    import re
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def green_dot():
    src = open(os.path.join(HERE, "make_ep01_green_dot_card.py"), encoding="utf-8").read()
    for a, b in (("EP01_UA_CARD_09_Green_Dot_43M_2012.png", "EP01_EN_CARD_09_Green_Dot_43M_2012.png"),
                 ("// ДОСЬЄ LOOPT // ВИХІД, 2012", "// LOOPT DOSSIER // EXIT, 2012"),
                 ("Корпорація Green Dot купує Loopt", "Green Dot Corporation acquires Loopt"),
                 ("Сім років роботи · скромний результат для венчурного ринку:", "Seven years of work · a modest exit by Silicon Valley standards:"),
                 ("інвестори ледве повернули вкладене", "investors barely broke even")):
        assert a in src, a
        src = src.replace(a, b)
    exec(compile(src, "green_dot_en", "exec"), {"__file__": os.path.join(HERE, "make_ep01_green_dot_card.py"), "__name__": "__main__"})


def wrap(d, text, f, width):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = t
    return lines + [cur]


def mgfx():
    for name, secs, kind, head, main, sub, foot in MGFX:
        im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        x0, x1, y1 = 200, 2800 if kind == "quote" else 2500, 1980
        fh, fm, fs, ff = font(SANS, 38, 1), (font(GEORGIA_B, 62) if kind == "quote" else font(SANS, 56, 1)), font(SANS, 36, 2 if kind == "quote" else 0), font(SANS, 34, 1)
        ml = wrap(d, main, fm, x1 - x0 - 100)
        sl = wrap(d, sub, fs, x1 - x0 - 100)
        hgt = 60 + 50 + 30 + len(ml) * 84 + 20 + len(sl) * 50 + (50 if foot else 0) + 40
        y0 = y1 - hgt
        d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=(10, 14, 22, 225), outline=ACCENT, width=3)
        y = y0 + 44
        d.rectangle([x0 + 50, y + 12, x0 + 64, y + 26], fill=ACCENT)
        d.text((x0 + 84, y), head, font=fh, fill=ACCENT)
        y += 62
        d.line([(x0 + 40, y), (x1 - 40, y)], fill=(245, 185, 65, 160), width=2)
        y += 34
        for ln in ml:
            d.text((x0 + 50, y), ln, font=fm, fill=(255, 255, 255, 255))
            y += 84
        y += 16
        for ln in sl:
            d.text((x0 + 50, y), ln, font=fs, fill=(245, 185, 65, 255) if kind == "quote" else (200, 215, 235, 255))
            y += 50
        if foot:
            d.text((x0 + 50, y + 6), foot, font=ff, fill=(150, 160, 175, 255))
        png = os.path.join(STILLS, name.replace("_10s", "").replace("_12s", "") + "_EN_Base.png")
        im.save(png)
        out = os.path.join(STILLS, name + "_EN.mov")
        subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-loop", "1", "-i", png, "-t", str(secs),
                        "-vf", f"fade=t=in:st=0:d=0.6:alpha=1,fade=t=out:st={secs - 0.6}:d=0.6:alpha=1,format=yuva444p10le",
                        "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-r", "24", out], check=True)
        print("  плашка", os.path.basename(out))


if __name__ == "__main__":
    supers()
    print("✓ титри, назви актів, правила, фінальна картка")
    green_dot()
    print("✓ картка Green Dot")
    mgfx()
    cards()
    print("✓ готово:", len(UA_TO_EN), "мовних файлів мають англійську пару")
