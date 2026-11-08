#!/usr/bin/env python3
"""
AI Titans Thoughtcast — ElevenLabs Voiceover Batch Manager for EP01 (Sam Altman)
Supports English (EN) and Ukrainian (UA) master narration.

Usage:
  # Check status:
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --status --lang en
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --status --lang ua

  # Generate all segments via API (requires ELEVENLABS_API_KEY env var):
  export ELEVENLABS_API_KEY="sk_..."
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --lang en --voice-id <VOICE_ID>

  # Generate single segment:
  python3 08_AUTOMATION/scripts/generate_elevenlabs_vo_ep01.py --lang en --seg 1 --voice-id <VOICE_ID>
"""

import os, sys, json, argparse, urllib.request, urllib.error

PROJECT_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
VO_BASE_DIR = os.path.join(PROJECT_ROOT, "03_AUDIO/voiceover/EP01_ALTMAN")

def get_paths(lang):
    if lang.lower() == "en":
        texts_dir = os.path.join(VO_BASE_DIR, "source_texts_en")
        manifest_file = os.path.join(VO_BASE_DIR, "SEGMENTS_MANIFEST_EN.json")
        wav_prefix = "EP01_VO_EN_"
        default_model = "eleven_turbo_v2_5" # or eleven_multilingual_v2
    else:
        texts_dir = os.path.join(VO_BASE_DIR, "source_texts")
        manifest_file = os.path.join(VO_BASE_DIR, "SEGMENTS_MANIFEST.json")
        wav_prefix = "EP01_VO_UA_"
        default_model = "eleven_multilingual_v2"
    return texts_dir, manifest_file, wav_prefix, default_model

def load_manifest(manifest_file):
    if not os.path.exists(manifest_file):
        print(f"Error: Manifest not found at {manifest_file}")
        sys.exit(1)
    with open(manifest_file, "r", encoding="utf-8") as f:
        return json.load(f)

def check_status(manifest, texts_dir, lang):
    print("=" * 85)
    print(f"🎙️ EPISODE 01: ELEVENLABS VOICEOVER STATUS [{lang.upper()}] (17 CALIBRATED SCENES)")
    print("=" * 85)
    ready_count = 0
    missing_count = 0
    total_words = 0

    for item in manifest:
        num = item["num"]
        wav_name = item["target_wav"]
        wav_path = os.path.join(VO_BASE_DIR, wav_name)
        txt_path = os.path.join(texts_dir, item["file_txt"])
        
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

    print("-" * 85)
    pct = (ready_count / len(manifest)) * 100 if manifest else 0
    print(f"TOTAL: {ready_count}/{len(manifest)} clips ready ({pct:.1f}%) • Total words: {total_words}")
    print(f"Source texts directory: {texts_dir}")
    print(f"Destination WAV directory: {VO_BASE_DIR}")
    print("=" * 85)
    return ready_count, missing_count

def generate_segment(item, texts_dir, api_key, voice_id, model_id):
    num = item["num"]
    txt_path = os.path.join(texts_dir, item["file_txt"])
    wav_path = os.path.join(VO_BASE_DIR, item["target_wav"])

    if not os.path.exists(txt_path):
        print(f"Error: Text file not found: {txt_path}")
        return False

    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    print(f"\n[Take {num:02d}] Generating: {item['target_wav']} ({len(text.split())} words)...")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    payload = {
        "text": text,
        "model_id": model_id,
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
    parser.add_argument("--lang", type=str, default="en", choices=["en", "ua"], help="Language: 'en' (default) or 'ua'")
    parser.add_argument("--status", action="store_true", help="Check status of VO WAV files")
    parser.add_argument("--voice-id", type=str, help="ElevenLabs Voice ID (e.g. 21m00Tcm4TlvDq8ikWAM for Rachel, JBFqnCBsd6RMkjVDRZzb for George)")
    parser.add_argument("--model-id", type=str, default="eleven_multilingual_v2", help="ElevenLabs Model ID")
    parser.add_argument("--seg", type=int, help="Single segment number (1-17)")
    args = parser.parse_args()

    texts_dir, manifest_file, wav_prefix, default_model = get_paths(args.lang)
    manifest = load_manifest(manifest_file)
    model_id = args.model_id or default_model

    if args.status or (not args.voice_id and not args.seg):
        check_status(manifest, texts_dir, args.lang)
        return

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("Error: ELEVENLABS_API_KEY environment variable is not set.")
        print("Please export ELEVENLABS_API_KEY='your_key' or copy texts from:")
        print(texts_dir)
        sys.exit(1)

    if args.seg:
        target = next((item for item in manifest if item["num"] == args.seg), None)
        if not target:
            print(f"Segment {args.seg} not found in manifest.")
            sys.exit(1)
        generate_segment(target, texts_dir, api_key, args.voice_id, model_id)
    else:
        for item in manifest:
            wav_path = os.path.join(VO_BASE_DIR, item["target_wav"])
            if os.path.exists(wav_path):
                print(f"Skipping Take {item['num']:02d} (already exists)")
                continue
            success = generate_segment(item, texts_dir, api_key, args.voice_id, model_id)
            if not success:
                print("Stopping batch on failure.")
                break

if __name__ == "__main__":
    main()
