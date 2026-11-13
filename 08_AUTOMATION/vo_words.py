#!/usr/bin/env python3
"""Точний час кожного слова сценарію за розпізнаванням Whisper (08_AUTOMATION/vo_words/*.json).

Слова тексту ElevenLabs вирівнюються з розпізнаними (difflib за нормалізованими словами + схожість
префіксів), невпізнані слова отримують час інтерполяцією між сусідами.
    word_time(n, "сто двадцять годин", "UA") → секунда початку фрази в дублі n
"""
import difflib
import json
import os
import re
from functools import lru_cache

import vo_align as V

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo_words")


def toks(s):
    s = V.norm(s.replace("-", " ").replace("—", " "))
    return [t for t in s.split() if t]


def stem(t):
    return t[:5]                          # грубий стемінг: відмінки/закінчення не заважають збігу


@lru_cache(None)
def script_times(lang, n):
    """[(слово_сценарію, позиція_символу, секунда)] для блоку n."""
    text = V.blocks(lang)[n - 1]
    nt = V.norm(text.replace("-", " ").replace("—", " "))
    words = [(m.group(0), m.start()) for m in re.finditer(r"\S+", nt)]
    rec = json.load(open(os.path.join(DIR, f"EP01_{lang}_{n:02d}.json")))
    rt = []
    for r in rec:
        for t in toks(r["w"]):
            rt.append((t, r["s"]))
    a = [stem(w) for w, _ in words]
    b = [stem(t) for t, _ in rt]
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    times = [None] * len(words)
    for i, j, k in sm.get_matching_blocks():
        for q in range(k):
            times[i + q] = rt[j + q][1]
    # інтерполяція для невпізнаних
    known = [i for i, t in enumerate(times) if t is not None]
    for i in range(len(times)):
        if times[i] is None:
            lo = max([k for k in known if k < i], default=None)
            hi = min([k for k in known if k > i], default=None)
            if lo is not None and hi is not None:
                times[i] = times[lo] + (times[hi] - times[lo]) * (i - lo) / (hi - lo)
            elif lo is not None:
                times[i] = times[lo] + 0.35 * (i - lo)
            elif hi is not None:
                times[i] = max(0.0, times[hi] - 0.35 * (hi - i))
            else:
                times[i] = 0.0
    matched = len(known) / max(1, len(words))
    return [(w, c, round(t, 3)) for (w, c), t in zip(words, times)], matched


def word_time(n, phrase, lang="UA"):
    """Початок фрази (точний збіг слів сценарію); None, якщо фрази немає в тексті."""
    ph = toks(phrase)
    st, _ = script_times(lang, n)
    ws = [w for w, _, _ in st]
    for i in range(len(ws) - len(ph) + 1):
        if ws[i:i + len(ph)] == ph:
            return st[i][2]
    return None


def coverage(lang):
    return {n: round(script_times(lang, n)[1], 2) for n in range(1, 18)}
