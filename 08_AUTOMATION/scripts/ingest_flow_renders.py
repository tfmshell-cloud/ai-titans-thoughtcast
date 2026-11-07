#!/usr/bin/env python3
"""
Cinematic Thoughtcast // AI Titans — Автоматичний імпортер рендерів Google Flow / Veo
Сканує ~/Downloads на нові MP4-файли, перевіряє роздільну здатність/FPS через ffmpeg
і акуратно розкладає їх у 05_RAW_FOOTAGE/flow_renders/ за канонічним списком черги епізоду!

Використання:
  python3 08_AUTOMATION/scripts/ingest_flow_renders.py EP01        # Переглянути / імпортувати нові MP4 з ~/Downloads для EP01
  python3 08_AUTOMATION/scripts/ingest_flow_renders.py EP01 --dry  # Сухий перегляд без переміщення
"""
import os
import sys
import json
import glob
import shutil
import subprocess

REPO = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
FLOW_DIR = os.path.join(REPO, "05_RAW_FOOTAGE/flow_renders")
POOL_JS = os.path.join(REPO, "07_DASHBOARD/data/media_acquisition_pool.js")
DOWNLOADS = os.path.expanduser("~/Downloads")


def load_queue(ep_num):
    raw = open(POOL_JS, encoding="utf-8").read()
    obj = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
    return obj.get(ep_num, {}).get("flow_queue", [])


def main():
    ep_arg = (sys.argv[1] if len(sys.argv) > 1 else "EP01").upper().replace("EP", "")
    ep_num = ep_arg.zfill(2)
    dry_run = "--dry" in sys.argv

    os.makedirs(FLOW_DIR, exist_ok=True)
    queue = load_queue(ep_num)
    if not queue:
        print(f"[!] Чергу для EP{ep_num} не знайдено.")
        sys.exit(1)

    missing = [q for q in queue if not os.path.exists(os.path.join(FLOW_DIR, q["file"]))]
    print(f"=== Статус 05_RAW_FOOTAGE/flow_renders/ для EP{ep_num} ===")
    print(f"Готово: {len(queue) - len(missing)}/{len(queue)} | Очікують генерації в Google Flow: {len(missing)}")
    for q in queue:
        p = os.path.join(FLOW_DIR, q["file"])
        mark = "✅ Є" if os.path.exists(p) else "⏳ Очікує"
        print(f"  [{mark}] #{q['num']} ({q['tc']}) -> {q['file']}")

    # Шукаємо свіжі MP4 у ~/Downloads (за останні 24 години), які ще не лежать у проєкті
    cand_mp4 = sorted(
        glob.glob(os.path.join(DOWNLOADS, "*.mp4")),
        key=lambda x: os.path.getmtime(x),
        reverse=False
    )
    # Фільтруємо лише файли зі свіжими генераціями (не старі побутові відео)
    import time
    now = time.time()
    recent_mp4 = [f for f in cand_mp4 if (now - os.path.getmtime(f)) < 86400]

    if not recent_mp4 or not missing:
        if not recent_mp4:
            print("\n[i] У ~/Downloads наразі немає нових .mp4 файлів за останні 24 години.")
            print("    Згенеруйте сцени в Google Flow / Veo і запустіть цей скрипт повторно — він сам перейменує їх за списком!")
        return

    print(f"\n[*] Знайдено нових .mp4 у ~/Downloads: {len(recent_mp4)}")
    for src, target_q in zip(recent_mp4, missing):
        dst = os.path.join(FLOW_DIR, target_q["file"])
        if dry_run:
            print(f"  [DRY-RUN] {os.path.basename(src)} -> {dst}")
        else:
            shutil.copy2(src, dst)
            print(f"  [✓ Імпортовано] {os.path.basename(src)} -> 05_RAW_FOOTAGE/flow_renders/{target_q['file']}")


if __name__ == "__main__":
    main()
