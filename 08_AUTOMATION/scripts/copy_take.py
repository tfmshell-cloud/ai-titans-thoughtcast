#!/usr/bin/env python3
"""
Quick Take Copier & Finder Opener for AI Titans Thoughtcast
Usage:
  python3 08_AUTOMATION/scripts/copy_take.py 1       # Copies English Take 1 to clipboard & opens in Finder
  python3 08_AUTOMATION/scripts/copy_take.py 1 --ua  # Copies Ukrainian Take 1 to clipboard & opens in Finder
  python3 08_AUTOMATION/scripts/copy_take.py 2       # Copies Take 2, etc.
"""

import sys, os, subprocess, json

PROJECT_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
VO_DIR = os.path.join(PROJECT_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 08_AUTOMATION/scripts/copy_take.py <take_number_1_to_17> [--ua]")
        sys.exit(1)

    take_num = int(sys.argv[1])
    is_ua = "--ua" in sys.argv

    manifest_file = os.path.join(VO_DIR, "SEGMENTS_MANIFEST.json" if is_ua else "SEGMENTS_MANIFEST_EN.json")
    texts_dir = os.path.join(VO_DIR, "source_texts" if is_ua else "source_texts_en")

    with open(manifest_file, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    target = next((item for item in manifest if item["num"] == take_num), None)
    if not target:
        print(f"Error: Take {take_num} not found (available: 1..{len(manifest)})")
        sys.exit(1)

    txt_path = os.path.join(texts_dir, target["file_txt"])
    with open(txt_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # 1. Copy to macOS Clipboard using pbcopy
    process = subprocess.Popen("pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE)
    process.communicate(content.encode("utf-8"))

    # 2. Reveal in Finder
    subprocess.run(["open", "-R", txt_path])

    lang_tag = "UA" if is_ua else "EN"
    print("=" * 75)
    print(f"📋 COPIED TO CLIPBOARD ({lang_tag}) -> TAKE {take_num:02d}: {target['file_txt']}")
    print(f"⏱️ Timecode: {target['tc']} ({target['words']} words)")
    print(f"📁 Revealed in Finder: {txt_path}")
    print(f"🎯 Target WAV Name: {target['target_wav']}")
    print("-" * 75)
    print(content)
    print("=" * 75)
    print("👉 Now switch to ElevenLabs in your browser and press Cmd + V (Paste)!")

if __name__ == "__main__":
    main()
