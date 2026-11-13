#!/usr/bin/env python3
"""EP01 Акт III, «акції Microsoft падають»: анімований біржовий графік 4K (6 с, 24 к/с).
Денний графік MSFT 17.11.2023: спокійна сесія → новина про звільнення Альтмана → обвал.
Вихід: 05_RAW_FOOTAGE/claude_graphics/EP01_CLAUDE_MSFT_Crash_Nov17_6s.mp4"""
import math
import os
import random
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
LANG = "UA" if "--ua" in sys.argv else "EN"
OUT = os.path.join(BASE, "05_RAW_FOOTAGE", "claude_graphics",
                   "EP01_CLAUDE_MSFT_Crash_Nov17_UA_6s.mp4" if LANG == "UA" else "EP01_CLAUDE_MSFT_Crash_Nov17_6s.mp4")
T = {"EN": dict(sub="MICROSOFT CORP · FRI 17 NOV 2023 · INTRADAY", lab="15:28 ET · OPENAI BOARD OUSTS SAM ALTMAN", brk="BREAKING",
                msg="   OPENAI BOARD REMOVES CEO SAM ALTMAN  ·  MICROSOFT SHARES SLIDE ON THE NEWS  ·  SILICON VALLEY IN SHOCK  ·"),
     "UA": dict(sub="MICROSOFT CORP · ПТ 17.11.2023 · ТОРГИ", lab="15:28 (НЬЮ-ЙОРК) · РАДА OPENAI ЗВІЛЬНЯЄ АЛЬТМАНА", brk="ТЕРМІНОВО",
                msg="   РАДА OPENAI ЗВІЛЬНИЛА CEO СЕМА АЛЬТМАНА  ·  АКЦІЇ MICROSOFT ПАДАЮТЬ НА НОВИНІ  ·  КРЕМНІЄВА ДОЛИНА В ШОЦІ  ·"),
     }[LANG]
FFMPEG = os.path.expanduser("~/Library/Python/3.9/bin/ffmpeg")
W, H, FPS, SECS = 1920, 1080, 24, 6.0
MONO = "/System/Library/Fonts/Menlo.ttc"
SANS = "/System/Library/Fonts/HelveticaNeue.ttc"
BG, GRID, AMBER, RED, WHITE, DIM = (9, 11, 15), (24, 28, 36), (242, 160, 60), (232, 64, 64), (236, 236, 236), (120, 128, 140)

random.seed(17)
N = 260
CRASH = 238                      # точка новини (≈ 15:28 ET)
price, path = 100.0, []
for i in range(N):
    if i < CRASH:
        price += random.gauss(0.02, 0.10)
    else:
        k = i - CRASH
        price += -0.55 * math.exp(-k / 7) + random.gauss(0, 0.04)
    path.append(price)
lo, hi = min(path) - 0.4, max(path) + 0.3
X0, X1, Y0, Y1 = 150, 1770, 250, 860


def xy(i):
    return X0 + (X1 - X0) * i / (N - 1), Y1 - (Y1 - Y0) * (path[i] - lo) / (hi - lo)


def frame(t):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    for m in range(30, 391, 60):
        x = X0 + (X1 - X0) * m / 390
        d.line([(x, Y0 - 20), (x, Y1)], fill=GRID, width=1)
    for y in range(Y0, Y1 + 1, 76):
        d.line([(X0, y), (X1, y)], fill=GRID, width=1)
    for i, lab in enumerate(["09:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30", "16:00"]):
        mins = (int(lab[:2]) * 60 + int(lab[3:])) - 570
        d.text((X0 + (X1 - X0) * mins / 390 - 28, Y1 + 18), lab, font=ImageFont.truetype(MONO, 20), fill=DIM)
    d.text((X0, 120), "NASDAQ: MSFT", font=ImageFont.truetype(SANS, 54, 1), fill=WHITE)
    d.text((X0 + 430, 140), T["sub"], font=ImageFont.truetype(MONO, 26), fill=DIM)
    reveal = min(N - 1, int((N - 1) * min(1.0, t / 4.6)))
    pts = [xy(i) for i in range(reveal + 1)]
    crashed = reveal >= CRASH
    if len(pts) > 1:
        glow = Image.new("RGB", (W, H), (0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.line(pts[:CRASH + 1], fill=AMBER, width=10)
        if crashed:
            g.line(pts[CRASH:], fill=RED, width=12)
        im = Image.blend(im, Image.composite(glow.filter(ImageFilter.GaussianBlur(14)), im, glow.convert("L").filter(ImageFilter.GaussianBlur(14))), 0.55)
        d = ImageDraw.Draw(im)
        d.line(pts[:CRASH + 1], fill=AMBER, width=4, joint="curve")
        if crashed:
            d.line(pts[CRASH:], fill=RED, width=5, joint="curve")
        x, y = pts[-1]
        d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=RED if crashed else AMBER)
    if crashed:
        k = (reveal - CRASH) / (N - 1 - CRASH)
        cx, _ = xy(CRASH)
        d.line([(cx, Y0 - 20), (cx, Y1)], fill=(120, 40, 40), width=2)
        lab = T["lab"]
        lf = ImageFont.truetype(MONO, 22)
        d.text((cx - 12 - d.textlength(lab, font=lf), Y0 - 16), lab, font=lf, fill=RED)
        pct = -1.7 * min(1.0, k * 1.15)
        d.polygon([(X1 - 330, 132), (X1 - 282, 132), (X1 - 306, 172)], fill=RED)
        d.text((X1 - 268, 112), f"{pct:.1f}%".replace("-", "−"), font=ImageFont.truetype(SANS, 76, 1), fill=RED)
    # біжучий рядок новин
    d.rectangle([0, 930, W, 1000], fill=(18, 20, 26))
    d.rectangle([60, 930, 290, 1000], fill=RED)
    d.text((86, 946), T["brk"], font=ImageFont.truetype(SANS, 34 if LANG == "EN" else 30, 1), fill=WHITE)
    msg = T["msg"]
    f = ImageFont.truetype(MONO, 30)
    off = int(t * 260)
    tw = d.textlength(msg, font=f)
    for rep in range(3):
        d.text((310 - off % int(tw) + rep * tw, 950), msg, font=f, fill=WHITE)
    d.rectangle([0, 930, 60, 1000], fill=(18, 20, 26))
    d.rectangle([60, 930, 290, 1000], fill=RED)
    d.text((86, 946), T["brk"], font=ImageFont.truetype(SANS, 34 if LANG == "EN" else 30, 1), fill=WHITE)
    if crashed and int(t * 4) % 2 == 0:
        d.ellipse([X1 - 30, 60, X1 - 10, 80], fill=RED)
    z = 1.0 + 0.02 * t / SECS                                   # повільний наїзд
    zw, zh = int(W / z), int(H / z)
    return im.crop(((W - zw) // 2, (H - zh) // 2, (W - zw) // 2 + zw, (H - zh) // 2 + zh)).resize((W, H), Image.LANCZOS)


def main():
    cmd = [FFMPEG, "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-vf", "scale=3840:2160:flags=lanczos", "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(int(SECS * FPS)):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close()
    p.wait()
    print("✓", OUT)


if __name__ == "__main__":
    main()
