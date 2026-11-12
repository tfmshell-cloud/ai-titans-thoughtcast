#!/usr/bin/env python3
"""
Перевірка озвучки EP01: чи всі дублі на місці, чи не обрізані, чи немає
довгих провалів тиші та чи співпадає звук із текстом.

Потрібно: Python 3.9+, ffmpeg та ffprobe у PATH.
Для порівняння зі сценарієм (необов'язково): pip install faster-whisper

Приклад:
  python3 verify_ep01_audio.py \
      --ua-dir "/шлях/EP01_ALTMAN_UA_MASTER" \
      --en-dir "/шлях/EP01_ALTMAN" \
      --txt-dir "/шлях/UA_text_takes" \
      --whisper --out ep01_audio_report.csv
"""
import argparse, csv, difflib, glob, json, os, re, subprocess, sys

TAKES = range(1, 18)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def find(folder, lang, n, ext):
    if not folder:
        return None
    hits = sorted(glob.glob(os.path.join(folder, f"EP01_VO_{lang}_{n:02d}_*.{ext}")))
    return hits[0] if hits else None


def probe(path):
    r = run(["ffprobe", "-v", "error", "-show_entries",
             "stream=codec_name,sample_rate,channels:format=duration",
             "-of", "json", path])
    if r.returncode != 0:
        return None
    j = json.loads(r.stdout or "{}")
    st = (j.get("streams") or [{}])[0]
    return {
        "duration": float(j.get("format", {}).get("duration", 0) or 0),
        "sample_rate": int(st.get("sample_rate", 0) or 0),
        "channels": int(st.get("channels", 0) or 0),
        "codec": st.get("codec_name", ""),
    }


def silences(path, noise="-45dB", min_dur=0.7):
    """Повертає список (початок, кінець) тиші та загальну тривалість."""
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path,
             "-af", f"silencedetect=noise={noise}:d={min_dur}", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    out = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else None
        out.append((s, e))
    return out


def loudness(path):
    r = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path,
             "-af", "volumedetect", "-f", "null", "-"])
    mx = re.search(r"max_volume: (-?[0-9.]+) dB", r.stderr)
    mean = re.search(r"mean_volume: (-?[0-9.]+) dB", r.stderr)
    return (float(mx.group(1)) if mx else None, float(mean.group(1)) if mean else None)


def norm(t):
    t = t.lower().replace("’", "'")
    t = re.sub(r"[^\w\s']", " ", t, flags=re.UNICODE)
    return re.sub(r"\s+", " ", t).strip()


def transcribe(model, path, lang):
    segs, _ = model.transcribe(path, language=lang, vad_filter=False)
    return " ".join(s.text for s in segs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ua-dir", required=True)
    ap.add_argument("--en-dir")
    ap.add_argument("--txt-dir", help="папка з українськими .txt (EP01_VO_UA_NN_*.txt)")
    ap.add_argument("--whisper", action="store_true", help="порівняти звук зі сценарієм")
    ap.add_argument("--whisper-model", default="medium")
    ap.add_argument("--out", default="ep01_audio_report.csv")
    a = ap.parse_args()

    model = None
    if a.whisper:
        try:
            from faster_whisper import WhisperModel
            model = WhisperModel(a.whisper_model, compute_type="int8")
        except Exception as e:
            print("Whisper недоступний:", e, file=sys.stderr)

    rows = []
    for n in TAKES:
        flags = []
        ua_wav, ua_mp3 = find(a.ua_dir, "UA", n, "wav"), find(a.ua_dir, "UA", n, "mp3")
        en_wav = find(a.en_dir, "EN", n, "wav")
        if not ua_wav:
            flags.append("НЕМАЄ UA WAV")
        if not ua_mp3:
            flags.append("НЕМАЄ UA MP3")
        if a.en_dir and not en_wav:
            flags.append("НЕМАЄ EN WAV")

        ua = probe(ua_wav) if ua_wav else None
        mp3 = probe(ua_mp3) if ua_mp3 else None
        en = probe(en_wav) if en_wav else None
        if ua_wav and not ua:
            flags.append("UA WAV НЕ ЧИТАЄТЬСЯ")

        d_ua = ua["duration"] if ua else None
        d_mp3 = mp3["duration"] if mp3 else None
        d_en = en["duration"] if en else None

        if d_ua and d_mp3 and abs(d_ua - d_mp3) > 0.3:
            flags.append(f"WAV і MP3 різняться на {abs(d_ua - d_mp3):.2f} с")
        if d_ua and d_en and not (0.9 <= d_ua / d_en <= 1.35):
            flags.append(f"UA/EN = {d_ua / d_en:.2f} (незвично)")
        if ua and (ua["sample_rate"] != 48000 or ua["channels"] != 1):
            flags.append(f"формат {ua['sample_rate']} Гц, {ua['channels']} кан.")

        lead = trail = None
        inner = 0
        mx = mean = None
        if ua_wav and ua:
            sil = silences(ua_wav)
            if sil and sil[0][0] < 0.05:
                lead = (sil[0][1] or 0) - sil[0][0]
            if sil and sil[-1][1] is None:
                trail = d_ua - sil[-1][0]
            inner = sum(1 for s, e in sil
                        if s > 0.05 and e is not None and (e - s) >= 1.5)
            if lead and lead > 1.0:
                flags.append(f"тиша на початку {lead:.1f} с")
            if trail and trail > 1.5:
                flags.append(f"тиша в кінці {trail:.1f} с")
            if inner:
                flags.append(f"{inner} пауз(и) довше 1,5 с всередині")
            mx, mean = loudness(ua_wav)
            if mx is not None and mx >= -0.1:
                flags.append("можливе кліпування (пік 0 дБ)")
            if mean is not None and mean < -35:
                flags.append(f"дуже тихо (середня {mean} дБ)")

        match = None
        txt = find(a.txt_dir, "UA", n, "txt")
        if model and ua_wav and txt:
            heard = norm(transcribe(model, ua_wav, "uk"))
            with open(txt, encoding="utf-8") as f:
                want = norm(f.read())
            match = difflib.SequenceMatcher(None, heard, want).ratio()
            if match < 0.85:
                flags.append(f"звук не збігається зі сценарієм ({match:.0%})")
        elif a.txt_dir and not txt:
            flags.append("НЕМАЄ тексту .txt")

        rows.append({
            "take": n,
            "ua_wav": os.path.basename(ua_wav) if ua_wav else "",
            "ua_sec": round(d_ua, 2) if d_ua else "",
            "mp3_sec": round(d_mp3, 2) if d_mp3 else "",
            "en_sec": round(d_en, 2) if d_en else "",
            "ua_over_en": round(d_ua / d_en, 2) if d_ua and d_en else "",
            "lead_silence": round(lead, 2) if lead else "",
            "trail_silence": round(trail, 2) if trail else "",
            "inner_pauses_1.5s": inner,
            "peak_db": mx if mx is not None else "",
            "mean_db": mean if mean is not None else "",
            "script_match": round(match, 3) if match is not None else "",
            "flags": "; ".join(flags) if flags else "OK",
        })

    with open(a.out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"{'№':>2} {'UA, с':>7} {'EN, с':>7}  стан")
    for r in rows:
        print(f"{r['take']:>2} {str(r['ua_sec']):>7} {str(r['en_sec']):>7}  {r['flags']}")
    print(f"\nЗвіт збережено: {a.out}")
    total = sum(r["ua_sec"] for r in rows if r["ua_sec"] != "")
    print(f"Разом UA: {total / 60:.2f} хв")


if __name__ == "__main__":
    main()
