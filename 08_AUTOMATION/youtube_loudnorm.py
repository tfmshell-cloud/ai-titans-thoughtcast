#!/usr/bin/env python3
"""Нормалізація гучності мастера для YouTube: −14 LUFS інтегровано, справжній пік ≤ −1 dBTP.
Два проходи ffmpeg loudnorm; відео копіюється без перекодування, звук — AAC 320 кбіт/с 48 кГц.
    python3 08_AUTOMATION/youtube_loudnorm.py 10_MASTERS/AI_Titans_EP01_Sam_Altman_UA_4K.mp4
→ 10_MASTERS/AI_Titans_EP01_Sam_Altman_UA_4K_YouTube.mp4"""
import json
import os
import re
import subprocess
import sys

FF = os.path.expanduser("~/Library/Python/3.9/bin/ffmpeg")
TARGET = "I=-14:TP=-1.0:LRA=11"


def measure(path, extra=""):
    r = subprocess.run([FF, "-hide_banner", "-i", path, "-vn", "-af", f"loudnorm={TARGET}{extra}:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    return json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r, re.S).group(0))


def main(src):
    m = measure(src)
    print(f"до:    {float(m['input_i']):6.1f} LUFS, пік {float(m['input_tp']):5.1f} dBTP, LRA {float(m['input_lra']):4.1f}")
    out = src.replace(".mp4", "_YouTube.mp4")
    af = (f"loudnorm={TARGET}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.run([FF, "-loglevel", "error", "-y", "-i", src, "-map", "0:v:0", "-map", "0:a:0", "-c:v", "copy",
                    "-af", af, "-ar", "48000", "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", out], check=True)
    m2 = measure(out)
    print(f"після: {float(m2['input_i']):6.1f} LUFS, пік {float(m2['input_tp']):5.1f} dBTP → {out}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
