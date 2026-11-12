#!/usr/bin/env python3
"""EP01 Акт I: генерує FCPXML за планом (24 fps, 3840x2160, сітка 92 BPM)."""
import os, re, sys, math, wave, subprocess
from urllib.parse import quote
from xml.sax.saxutils import quoteattr

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
MAC = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
OUT = os.path.join(BASE, "06_DAVINCI_PROJECTS", "EP01_ActI_UA.fcpxml")
TL = "EP01_ActI_UA"
FPS = 24
BAR_S = 60.0 / 92 * 4
BAR_F = BAR_S * FPS
fr = lambda b: int(round(b * BAR_F))
t = lambda f: f"{f * 100}/2400s"

PLAN = [
 (0,3,"video","ep01_flow_01_mac_chassis.mp4",None),
 (3,6,"video","EP01_VID_ARCH_03_ACT1_24FPS_Apple_Macintosh_1992_CRT.mp4",None),
 (6,9,"still","EP01_FLOW_IMG_02C_Phosphor_Triad_Subpixel_Macro.jpg",None),
 (9,12,"still","EP01_IMG_ARCH_06_Altman_Childhood_Macintosh_LC_II_1993.jpg",None),
 (12,15,"still","EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg",None),
 (15,19,"still","EP01_FLOW_IMG_02B_Child_Eye_Green_Code_Macro.jpg","ЦИТАТА Д02 (накладка тексту, бари 15-18): Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю"),
 (19,22,"video","ep01_flow_02_crt_code.mp4",None),
 (22,25,"still","EP01_FLOW_IMG_02_CRT_Code_Eye_Reflection_Hero.jpg",None),
 (25,29,"still","EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg",None),
 (29,33,"still","EP01_IMG_ARCH_05_Altman_John_Burroughs_School_Campus.jpg","ПРОПУСК Д03: потрібен кадр актової зали або сцени. Тимчасово повтор PHOTO 06 (інший кроп)"),
 (33,37,"still","EP01_FLOW_STUDY_02E_CRT_Computer_Boardroom_2K.jpg","КОНЦЕПТ-ДОСЛІДЖЕННЯ: перевірте, чи підходить за тоном"),
 (37,41,"still","EP01_FLOW_STUDY_01D_Mac_Boardroom_StudyA_2K.jpg",None),
 (41,44,"still","EP01_FLOW_IMG_01_Macintosh_LC_II_Keyframe.jpg",None),
 (44,47,"video","ep01_flow_03_silicon_laser.mp4",None),
 (47,51,"still","EP01_FLOW_IMG_03_Silicon_Wafer_Cyan_Laser_Hero.png",None),
 (51,55,"still","EP01_IMG_ARCH_07_Altman_Loopt_Shirt_Founder_Era.jpg",None),
 (55,59,"still","EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg",None),
 (59,64,"still","EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png",None),
 (64,69,"still","EP01_IMG_ARCH_03_Altman_WWDC_2008_SteveJobs_Loopt.jpg",None),
 (69,73,"gfx",None,"ГРАФІКА Д05: плашка «$43 млн · Green Dot · 2012»"),
 (73,79,"gfx",None,"ГРАФІКА Д05: цитатна плашка «Більшість людей здаються не тому, що їхня ідея хибна…»"),
 (79,82,"video","ep01_flow_04_exponential_line.mp4",None),
 (82,87,"still","EP01_FLOW_IMG_04_Golden_Exponential_Curve_Hero.png",None),
 (87,90,"video","EP01_VID_ARCH_04_ACT1_24FPS_Altman_WWDC_2008_Loopt_SteveJobs.mp4","НИЗЬКА РОЗДІЛЬНІСТЬ: 640x480, апскейл або менший розмір у кадрі"),
 (90,93,"still","EP01_IMG_ARCH_01_Altman_2009_Loopt_Era.jpg","ARCH 06 (відео-паралакс) відсутнє на диску: тимчасово стоп-кадр PHOTO 01, додайте рух або замініть"),
 (93,109,"gap",None,"РІШЕННЯ ПОТРІБНЕ: 16 тактів (близько 42 с) без голосу і без кадрів. Скоротити Акт I або додати 2-3 плани"),
]
TOTAL_BARS = 109
SLOT = {1:0,2:15,3:45,4:90,5:150,6:210}
EXPECT = {1:0,2:7,3:25,4:44,5:59,6:81}
MUSIC = "EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav"

idx = {}
for sub in ("03_AUDIO", "05_RAW_FOOTAGE"):
    for dp, _, fns in os.walk(os.path.join(BASE, sub)):
        for fn in fns:
            if not fn.startswith("."):
                idx.setdefault(fn, os.path.join(dp, fn))

def macpath(p): return MAC + p[len(BASE):]
def url(p): return "file://" + quote(macpath(p))

def info(p):
    try:
        with wave.open(p, "rb") as w:
            return w.getnframes() / float(w.getframerate()), w.getnchannels(), w.getframerate()
    except Exception:
        r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration:stream=channels,sample_rate","-of","default=nw=1",p],capture_output=True,text=True)
        d = dict(l.split("=") for l in r.stdout.split() if "=" in l)
        return float(d["duration"]), int(d.get("channels",2)), int(d.get("sample_rate",48000))

assets, order, body, missing, warn = {}, [], [], [], []
def asset(p, kind, dur_f, ch=2, rate=48000):
    k = (p, kind)
    if k in assets: return assets[k][0]
    aid = f"a{len(assets)+1}"
    nm = quoteattr(os.path.splitext(os.path.basename(p))[0]); src = quoteattr(url(p))
    if kind == "still":
        x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="0s" hasVideo="1" format="r1"/>'
    elif kind == "video":
        x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur_f)}" hasVideo="1" hasAudio="1" audioSources="1" audioChannels="2" audioRate="48000" format="r1"/>'
    else:
        x = f'<asset id="{aid}" name={nm} src={src} start="0s" duration="{t(dur_f)}" hasAudio="1" audioSources="1" audioChannels="{ch}" audioRate="{rate}"/>'
    assets[k] = (aid, x); order.append(k); return aid

for b0, b1, kind, fname, mk in PLAN:
    f0, f1 = fr(b0), fr(b1); d = f1 - f0
    if mk: body.append(f'<marker start="{t(f0)}" duration="100/2400s" value={quoteattr(mk)}/>')
    if kind in ("gfx", "gap"): continue
    p = idx.get(fname)
    if not p:
        missing.append(fname)
        body.append(f'<marker start="{t(f0)}" duration="100/2400s" value={quoteattr("НЕ ЗНАЙДЕНО ФАЙЛ: "+fname)}/>')
        continue
    a = asset(p, kind, d); nm = quoteattr(os.path.splitext(fname)[0])
    if kind == "still":
        body.append(f'<video ref="{a}" lane="1" offset="{t(f0)}" name={nm} start="0s" duration="{t(d)}"/>')
    else:
        body.append(f'<asset-clip ref="{a}" lane="1" offset="{t(f0)}" name={nm} start="0s" duration="{t(d)}" audioRole="effects"/>')

prev_end = 0.0; rep = []
for n in range(1, 7):
    pat = re.compile(rf"^EP01_VO_UA_{n:02d}_ACT\d_.*\.wav$")
    p = next((idx[k] for k in sorted(idx) if pat.match(k)), None)
    if not p:
        missing.append(f"EP01_VO_UA_{n:02d}_ACT*.wav"); continue
    dur, ch, rate = info(p)
    sb = 0 if n == 1 else int(math.ceil(max(SLOT[n], prev_end + BAR_S) / BAR_S - 1e-9))
    prev_end = sb * BAR_S + dur
    rep.append((n, round(dur,2), sb, round(prev_end,2)))
    if sb != EXPECT[n]: warn.append(f"Д{n:02d}: старт на барі {sb}, у плані {EXPECT[n]}")
    a = asset(p, "audio", int(round(dur*FPS)), ch, rate)
    body.append(f'<asset-clip ref="{a}" lane="-1" offset="{t(fr(sb))}" name="VO_UA_{n:02d}" start="0s" duration="{t(int(math.floor(dur*FPS)))}" audioRole="dialogue"/>')
    body.append(f'<marker start="{t(fr(sb))}" duration="100/2400s" value="Д{n:02d} старт (бар {sb})"/>')

mp = idx.get(MUSIC)
if mp:
    md, mch, mr = info(mp); total_f = fr(TOTAL_BARS)
    a = asset(mp, "audio", int(round(md*FPS)), mch, mr)
    body.append(f'<asset-clip ref="{a}" lane="-2" offset="0s" name="MUS_01_Act1" start="0s" duration="{t(min(total_f,int(math.floor(md*FPS))))}" audioRole="music"/>')
else: missing.append(MUSIC)

total_f = fr(TOTAL_BARS)
res = "\n    ".join(assets[k][1] for k in order)
xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<fcpxml version="1.8">
  <resources>
    <format id="r1" name="FFVideoFormat3840x2160p24" frameDuration="100/2400s" width="3840" height="2160" colorSpace="1-1-1 (Rec. 709)"/>
    {res}
  </resources>
  <library>
    <event name="SEM_EP01">
      <project name="{TL}">
        <sequence format="r1" duration="{t(total_f)}" tcStart="0s" tcFormat="NDF" audioLayout="stereo" audioRate="48k">
          <spine>
            <gap name="Akt_I" offset="0s" start="0s" duration="{t(total_f)}">
              {chr(10).join("              "+x for x in body).strip()}
            </gap>
          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(xml)
print("FCPXML:", macpath(OUT))
print("Голос (дубль, с, старт-бар, кінець с):")
for r in rep: print("  ", r)
print("Ассетів:", len(assets), "| відсутні:", sorted(set(missing)) or "немає")
for w in warn: print("УВАГА:", w)
