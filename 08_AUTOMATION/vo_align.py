#!/usr/bin/env python3
"""Карта часу озвучки: коли саме диктор вимовляє кожну фразу блоку.

Речення тексту ElevenLabs (02_SCRIPTS/...ELEVENLABS_MASTER.txt) зіставляються з відрізками мовлення,
розділеними паузами у WAV (динамічне програмування за часткою символів), всередині речення —
лінійно за символами. Точність ~0,2–0,4 с, цього достатньо, щоб склейка влучала в слово.

    phrase_time(n, "сто двадцять годин") → секунди від початку блоку n (або None)
"""
import array
import audioop
import math
import os
import re
import wave
from functools import lru_cache

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT = {"UA": os.path.join(BASE, "02_SCRIPTS", "episode_01_altman", "EP01_VO_UA_ELEVENLABS_MASTER.txt"),
       "EN": os.path.join(BASE, "02_SCRIPTS", "episode_01_altman", "EP01_VO_EN_ELEVENLABS_MASTER.txt")}
WAV = {"UA": os.path.join(BASE, "03_AUDIO", "voiceover", "EP01_ALTMAN_UA_MASTER"),
       "EN": os.path.join(BASE, "03_AUDIO", "voiceover", "EP01_ALTMAN")}


def norm(s):
    s = s.lower().replace("’", "'").replace("ʼ", "'")
    return re.sub(r"[^0-9a-zа-яіїєґ'\s]", " ", s)


@lru_cache(None)
def blocks(lang):
    raw = open(TXT[lang], encoding="utf-8").read()
    parts = re.split(r"^\[\d+:\d+ - \d+:\d+\].*$", raw, flags=re.M)[1:]
    out = []
    for p in parts:
        t = p.replace("\\n", "\n")
        t = re.sub(r"\*+", "", t)
        out.append(re.sub(r"\s+", " ", t).strip())
    return out


@lru_cache(None)
def speech(lang, n):
    d = WAV[lang]
    f = next(x for x in sorted(os.listdir(d)) if x.startswith(f"EP01_VO_{lang}_{n:02d}_") and x.endswith(".wav"))
    w = wave.open(os.path.join(d, f))
    sr, ch, sw = w.getframerate(), w.getnchannels(), w.getsampwidth()
    raw = w.readframes(w.getnframes())
    if sw != 2:
        raw = audioop.lin2lin(raw, sw, 2)
    if ch == 2:
        raw = audioop.tomono(raw, 2, 0.5, 0.5)
    hop = int(sr * 0.01)
    env = [audioop.rms(raw[i:i + hop * 2], 2) for i in range(0, len(raw), hop * 2)]
    peak = sorted(env)[int(len(env) * 0.95)] or 1
    thr = peak * 10 ** (-30 / 20)
    voiced = [v > thr for v in env]
    segs, i = [], 0
    while i < len(voiced):              # відрізки мовлення; паузи < 0,22 с не розривають
        if voiced[i]:
            j = i
            while j < len(voiced):
                k = j
                while k < len(voiced) and not voiced[k]:
                    k += 1
                if k - j >= 22 or k == len(voiced):
                    break
                j = k + 1 if k > j else j + 1
                while j < len(voiced) and voiced[j]:
                    j += 1
            segs.append((i / 100, j / 100))
            i = j
        else:
            i += 1
    return segs, len(env) / 100


@lru_cache(None)
def charmap(lang, n):
    """[(індекс_символу, секунда)]: частини тексту (між розділовими знаками) ↔ відрізки мовлення.
    ДП дозволяє і «частина на кілька відрізків», і «кілька частин на один відрізок»."""
    text = blocks(lang)[n - 1]
    cut = sorted({0} | {m.end() for m in re.finditer(r"[.!?…:;,—–»]\s+", text)} | {len(text)})
    parts = [(a, b) for a, b in zip(cut, cut[1:]) if b > a]
    lens = [max(1, len(norm(text[a:b]).replace(" ", ""))) for a, b in parts]
    segs, total = speech(lang, n)
    P, K = len(parts), len(segs)
    if K == 0:
        return [(0, 0.0)]
    rate = sum(b - a for a, b in segs) / sum(lens)             # с на символ
    INF = 1e18
    dp = [[INF] * (K + 1) for _ in range(P + 1)]
    bk = [[None] * (K + 1) for _ in range(P + 1)]
    dp[0][0] = 0.0
    for i in range(P + 1):
        for j in range(K + 1):
            if dp[i][j] >= INF:
                continue
            for pi in range(1, 5):                                # pi частин
                for sj in range(1, 5):                            # sj відрізків
                    if i + pi > P or j + sj > K or (pi > 1 and sj > 1):
                        continue
                    exp = sum(lens[i:i + pi]) * rate
                    dur = segs[j + sj - 1][1] - segs[j][0]
                    gaps = sum(segs[q + 1][0] - segs[q][1] for q in range(j, j + sj - 1))
                    c = dp[i][j] + (dur - gaps - exp) ** 2 / (exp + 0.5) + 0.15 * (pi - 1) + 0.05 * (sj - 1)
                    if c < dp[i + pi][j + sj]:
                        dp[i + pi][j + sj], bk[i + pi][j + sj] = c, (i, j)
    i, j, groups = P, K, []
    while i > 0 and j > 0 and bk[i][j]:
        pi, pj = bk[i][j]
        groups.append((pi, i, pj, j))
        i, j = pi, pj
    groups.reverse()
    pts = []
    for i0, i1, j0, j1 in groups:
        a, b = parts[i0][0], parts[i1 - 1][1]
        st, en = segs[j0][0], segs[j1 - 1][1]
        if i1 - i0 > 1:                                           # кілька частин в одному відрізку — за символами
            L = sum(lens[i0:i1])
            acc = 0
            for q in range(i0, i1):
                pts.append((parts[q][0], round(st + (en - st) * acc / L, 2)))
                acc += lens[q]
            pts.append((b, en))
        else:
            pts.append((a, st))
            pts.append((b, en))
    return pts


def phrase_time(n, phrase, lang="UA", strict=False):
    text = blocks(lang)[n - 1]
    nt, ph = norm(text), norm(phrase).split()
    if not ph:
        return None
    if strict:                                  # лише точний збіг усієї фрази (позиція — початок фрази)
        m = re.search(r"(?<![0-9a-zа-яіїєґ'])" + r"\s+".join(map(re.escape, ph)), nt)
        if not m:
            return None
        pos = m.start()
        pts = charmap(lang, n)
        for (c0, t0), (c1, t1) in zip(pts, pts[1:]):
            if c0 <= pos <= c1 and c1 > c0:
                return round(t0 + (pos - c0) / (c1 - c0) * (t1 - t0), 2)
        return pts[-1][1]
    key = " ".join(ph[:3])
    pos = nt.find(key)
    if pos < 0 and len(ph) >= 2:
        pos = nt.find(" ".join(ph[:2]))
    if pos < 0:
        pos = nt.find(ph[0]) if len(ph[0]) > 5 else -1
    if pos < 0:
        return None
    pts = charmap(lang, n)
    for (c0, t0), (c1, t1) in zip(pts, pts[1:]):
        if c0 <= pos <= c1 and c1 > c0:
            return round(t0 + (pos - c0) / (c1 - c0) * (t1 - t0), 2)
    return pts[-1][1]


if __name__ == "__main__":
    for n in (8, 12):
        segs, tot = speech("UA", n)
        print(n, f"{tot:.1f}с", len(segs), "відрізків", charmap("UA", n)[:6])
