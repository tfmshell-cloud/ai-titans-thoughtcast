#!/usr/bin/env python3
"""
AI Titans Thoughtcast — ElevenLabs Voiceover Batch Generator / Auditor for EP01 (Sam Altman)
Usage:
  # Check status of VO files:
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --status

  # Generate all segments via API (requires ELEVENLABS_API_KEY env var):
  export ELEVENLABS_API_KEY="sk_..."
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --voice-id <VOICE_ID>

  # Generate single segment:
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --seg 1 --voice-id <VOICE_ID>
"""

import os, sys, json, argparse, urllib.request, urllib.error

PROJECT_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
TEXTS_DIR = os.path.join(PROJECT_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN/source_texts")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN")
MANIFEST_FILE = os.path.join(OUTPUT_DIR, "SEGMENTS_MANIFEST.json")

def load_manifest():
    if not os.path.exists(MANIFEST_FILE):
        print(f"Error: Manifest not found at {MANIFEST_FILE}")
        sys.exit(1)
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def check_status(manifest):
    print("=" * 80)
    print("🎙️ EPISODE 01: ELEVENLABS VOICEOVER STATUS AUDIT (17 SCENES)")
    print("=" * 80)
    ready_count = 0
    missing_count = 0
    total_words = 0

    for item in manifest:
        num = item["num"]
        wav_name = item["target_wav"]
        wav_path = os.path.join(OUTPUT_DIR, wav_name)
        txt_path = os.path.join(TEXTS_DIR, item["file_txt"])
        
        words = item.get("words", 0)
        total_words += words
        
        exists = os.path.exists(wav_path)
        if exists:
            size_kb = os.path.getsize(wav_path) / 1024
            status_str = f"🟢 READY ({size_kb:.1f} KB)"
            ready_count += 1
        else:
            status_str = "⏳ PENDING"
            missing_count += 1

        print(f"[{num:02d}] {item['tc']:<18} | {words:>3} w | {status_str:<16} | {wav_name}")

    print("-" * 80)
    pct = (ready_count / len(manifest)) * 100 if manifest else 0
    print(f"TOTAL: {ready_count}/{len(manifest)} clips ready ({pct:.1f}%) • Total script words: {total_words}")
    print(f"Source texts directory: {TEXTS_DIR}")
    print(f"Destination WAV directory: {OUTPUT_DIR}")
    print("=" * 80)
    return ready_count, missing_count

def generate_segment(item, api_key, voice_id):
    num = item["num"]
    txt_path = os.path.join(TEXTS_DIR, item["file_txt"])
    wav_path = os.path.join(OUTPUT_DIR, item["target_wav"])

    if not os.path.exists(txt_path):
        print(f"Error: Text file not found: {txt_path}")
        return False

    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    print(f"\n[Take {num:02d}] Generating: {item['target_wav']} ({len(text.split())} words)...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.58,
            "similarity_boost": 0.82,
            "style": 0.05,
            "use_speaker_boost": True
        }
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }
    )

    try:
        with urllib.request.urlopen(req) as response:
            audio_data = response.read()
            with open(wav_path, "wb") as out_f:
                out_f.write(audio_data)
            print(f"✓ Saved successfully: {wav_path} ({len(audio_data) / 1024:.1f} KB)")
            return True
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8")
        print(f"✗ ElevenLabs API Error ({e.code}): {error_msg}")
        return False
    except Exception as e:
        print(f"✗ Network/Request error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="ElevenLabs VO Batch Manager")
    parser.add_argument("--status", action="store_true", help="Check status of VO WAV files")
    parser.add_argument("--voice-id", type=str, help="ElevenLabs Voice ID")
    parser.add_argument("--seg", type=int, help="Single segment number (1-17)")
    args = parser.parse_args()

    manifest = load_manifest()

    if args.status or (not args.voice_id and not args.seg):
        check_status(manifest)
        return

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("Error: ELEVENLABS_API_KEY environment variable is not set.")
        print("Please export ELEVENLABS_API_KEY='your_key' or generate clips via ElevenLabs web app.")
        sys.exit(1)

    if args.seg:
        target = next((item for item in manifest if item["num"] == args.seg), None)
        if not target:
            print(f"Segment {args.seg} not found in manifest.")
            sys.exit(1)
        generate_segment(target, api_key, args.voice_id)
    else:
        for item in manifest:
            wav_path = os.path.join(OUTPUT_DIR, item["target_wav"])
            if os.path.exists(wav_path):
                print(f"Skipping Take {item['num']:02d} (already exists)")
                continue
            success = generate_segment(item, api_key, args.voice_id)
            if not success:
                print("Stopping batch on failure.")
                break

if __name__ == "__main__":
    main()
