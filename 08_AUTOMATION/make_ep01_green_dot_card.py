#!/usr/bin/env python3
"""Картка «$43 млн · Green Dot · 2012» для EP01 Акт I (дубль 05), 3840x2160,
у стилі українських карток-цитат (EP01_UA_CARD_*)."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "05_RAW_FOOTAGE", "claude_graphics", "EP01_UA_CARD_09_Green_Dot_43M_2012.png")
W, H, K = 3840, 2160, 1.92          # K: масштаб від макета 2000x1125

def f(path, size, idx=0):
    return ImageFont.truetype(path, int(size * K), index=idx)

MONO = "/System/Library/Fonts/Menlo.ttc"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
s = lambda v: int(v * K)

im = Image.new("RGB", (W, H), (10, 11, 15))
d = ImageDraw.Draw(im)
for x in range(0, W, s(62)):                      # ледь помітна сітка
    d.line([(x, 0), (x, H)], fill=(16, 18, 23), width=2)
for y in range(0, H, s(62)):
    d.line([(0, y), (W, y)], fill=(16, 18, 23), width=2)
for cx, cy in ((250, 213), (1750, 213), (250, 912), (1750, 912)):   # хрестики
    d.line([(s(cx - 13), s(cy)), (s(cx + 13), s(cy))], fill=(70, 74, 82), width=3)
    d.line([(s(cx), s(cy - 13)), (s(cx), s(cy + 13))], fill=(70, 74, 82), width=3)
d.rounded_rectangle([s(261), s(225), s(1739), s(901)], radius=s(18), fill=(190, 184, 172))
d.rounded_rectangle([s(271), s(235), s(1729), s(891)], radius=s(12), fill=(25, 28, 34))
d.rectangle([s(271), s(235), s(1729), s(239)], fill=(242, 140, 30))
ORANGE, WHITE, GREY, DIM = (242, 150, 40), (236, 236, 236), (170, 174, 182), (88, 94, 106)
d.text((s(333), s(282)), "// ДОСЬЄ LOOPT // ВИХІД, 2012", font=f(MONO, 20), fill=ORANGE)
d.line([(s(333), s(315)), (s(1667), s(315))], fill=(45, 49, 57), width=2)
d.text((s(333), s(370)), "$43 000 000", font=f(SANS, 150, 1), fill=WHITE)
d.text((s(338), s(570)), "Корпорація Green Dot купує Loopt", font=f(SANS, 40), fill=WHITE)
d.text((s(338), s(630)), "Сім років роботи · скромний результат для венчурного ринку:", font=f(SANS, 28), fill=GREY)
d.text((s(338), s(672)), "інвестори ледве повернули вкладене", font=f(SANS, 28), fill=GREY)
d.text((s(333), s(812)), "— LOOPT · 2005–2012", font=f(SANS, 25), fill=(200, 204, 210))
d.text((s(333), s(855)), "THOUGHTCAST 4K // AI TITANS // EP01: SAM ALTMAN", font=f(MONO, 15), fill=DIM)
d.text((s(1426), s(855)), "MASTER ARCHIVAL RECORD", font=f(MONO, 15), fill=DIM)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
im.save(OUT)
print(OUT)
