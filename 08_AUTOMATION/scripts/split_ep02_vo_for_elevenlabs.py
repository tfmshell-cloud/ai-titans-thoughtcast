#!/usr/bin/env python3
"""Розрізає EP02_VO_UA_ELEVENLABS_MASTER.txt на окремі дублі для ElevenLabs.

Вихід: 03_AUDIO/voiceover/EP02_HUANG/
  source_texts/EP02_VO_UA_NN_ACTx_....txt  — по одному файлу на дубль (вставляти в ElevenLabs)
  SEGMENTS_MANIFEST.json                    — список дублів (той самий формат, що й EP01)
  EP02_VO_UA_ALL_TAKES.txt                  — усі дублі одним файлом для копіювання з телефона
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "02_SCRIPTS/episode_02_huang/EP02_VO_UA_ELEVENLABS_MASTER.txt")
OUT = os.path.join(ROOT, "03_AUDIO/voiceover/EP02_HUANG")
TXT = os.path.join(OUT, "source_texts")

SLUGS = [
    "Sterile_Legends_Kentucky_Floor", "Oneida_Reformatory_1972", "Pact_With_Dorm_Leader",
    "Toilets_Humility_Quote", "Dennys_Dishwasher", "NVIDIA_Founding_Dennys_1993",
    "NV1_Fatal_Mistake", "Sega_Honesty_Gambit", "RIVA128_Thirty_Days",
    "GeForce256_CUDA_Bet", "CUDA_Decade_Zero_Market", "AlexNet_2012_DGX1",
    "No_Office_Flat_Leadership", "Three_Rules_Of_Pain", "Tattoo_Thirty_Days_Outro",
]
ACT_STARTS = [(0, 1), (315, 2), (645, 3), (975, 4)]  # секунди початку актів 1–4


def secs(tc):
    m, s = tc.split(":")
    return int(m) * 60 + int(s)


def act_for(start):
    act = 1
    for st, a in ACT_STARTS:
        if start >= st:
            act = a
    return act


def clean(body):
    t = body.replace("\\n", "\n")
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)          # **жирний** -> текст
    t = re.sub(r"\*(«.+?»[.!?]?)\*", r"\1", t, flags=re.S)  # *«цитата»* -> «цитата»
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


raw = open(SRC, encoding="utf-8").read()
blocks = re.findall(r"^\[(\d+:\d\d) - (\d+:\d\d)\] \((\d+) слів\)\n(.+?)(?=\n\[\d+:\d\d - |\Z)", raw, re.S | re.M)
assert len(blocks) == len(SLUGS), f"знайдено {len(blocks)} блоків, очікувалось {len(SLUGS)}"

os.makedirs(TXT, exist_ok=True)
manifest, combined = [], []
for i, ((a, b, w, body), slug) in enumerate(zip(blocks, SLUGS), 1):
    text = clean(body)
    sa, sb = secs(a), secs(b)
    base = f"EP02_VO_UA_{i:02d}_ACT{act_for(sa)}_{sa//60:02d}_{sa%60:02d}_{sb//60:02d}_{sb%60:02d}_{slug}"
    with open(os.path.join(TXT, base + ".txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    words = len(text.split())
    manifest.append({"num": i, "tc": f"[{a} - {b}] ({w} слів)", "file_txt": base + ".txt",
                     "target_wav": base + ".wav", "target_mp3": base + ".mp3",
                     "words": words, "sample": text[:60] + "..."})
    combined.append(f"===== ДУБЛЬ {i:02d} · [{a} - {b}] · {words} слів · файл: {base}.mp3 =====\n\n{text}\n")

with open(os.path.join(OUT, "SEGMENTS_MANIFEST.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

header = """EP02 · ДЖЕНСЕН ХУАНГ · УКРАЇНСЬКА ОЗВУЧКА ДЛЯ ELEVENLABS
Модель: Eleven Multilingual v2 · той самий голос, що в EP01
Налаштування (як у майстер-скрипті): Speed 0.86 · Stability 55% · Similarity (Clarity) 85% · Style 5% · Speaker boost ON
Темп: ~115 слів/хв, музика 92 BPM (такт 2.61 с)
Порядок: копіюєте текст одного дубля → генеруєте → завантажуєте й називаєте файл, як указано в заголовку дубля.
"""
with open(os.path.join(OUT, "EP02_VO_UA_ALL_TAKES.txt"), "w", encoding="utf-8") as f:
    f.write(header + "\n" + "\n".join(combined))

print(f"{len(manifest)} дублів, {sum(m['words'] for m in manifest)} слів -> {OUT}")
