#!/usr/bin/env python3
"""Таймкоди кожного слова в дублях озвучки EP01 (UA і EN) — локально, faster-whisper.
Запуск (окреме середовище): ~/.venvs/whisper/bin/python 08_AUTOMATION/vo_transcribe.py [UA|EN]
Результат: 08_AUTOMATION/vo_words/EP01_{LANG}_{NN}.json — [{"w": слово, "s": початок, "e": кінець}, ...]"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vo_align as V                     # noqa: E402  (тексти блоків і шляхи до WAV)
from faster_whisper import WhisperModel  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo_words")
os.makedirs(OUT, exist_ok=True)
langs = sys.argv[1:] or ["UA", "EN"]
# лише словник власних назв: довгий текст-підказка змушує модель «копіювати» його і ламає таймкоди
GLOSSARY = {"UA": "Альтман, Loopt, Y Combinator, OpenAI, Rosewood, Ілон Маск, Суцкевер, DeepMind, Гассабіс, ChatGPT, Microsoft, Наделла, Stargate, Helion.",
            "EN": "Altman, Loopt, Y Combinator, OpenAI, Rosewood, Elon Musk, Sutskever, DeepMind, ChatGPT, Microsoft, Nadella, Stargate, Helion."}
model = WhisperModel("small", device="cpu", compute_type="int8")
for lang in langs:
    d = V.WAV[lang]
    for n in range(1, 18):
        out = os.path.join(OUT, f"EP01_{lang}_{n:02d}.json")
        if os.path.exists(out):
            continue
        f = next(x for x in sorted(os.listdir(d)) if x.startswith(f"EP01_VO_{lang}_{n:02d}_") and x.endswith(".wav"))
        segs, info = model.transcribe(os.path.join(d, f), language="uk" if lang == "UA" else "en", word_timestamps=True,
                                      initial_prompt=GLOSSARY[lang], beam_size=5, vad_filter=False,
                                      condition_on_previous_text=False)
        words = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3)} for s in segs for w in s.words]
        json.dump(words, open(out, "w"), ensure_ascii=False)
        print(f"{lang} {n:02d}: {len(words)} слів, до {words[-1]['e'] if words else 0:.1f} с", flush=True)
