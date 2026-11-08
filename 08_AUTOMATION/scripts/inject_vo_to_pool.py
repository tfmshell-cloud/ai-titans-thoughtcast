import json, re

pool_path = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/data/media_acquisition_pool.js"
manifest_path = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/03_AUDIO/voiceover/EP01_ALTMAN/SEGMENTS_MANIFEST_EN.json"

with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open(pool_path, "r", encoding="utf-8") as f:
    content = f.read()

vo_items = []
for item in manifest:
    num_val = item['num']
    n_str = f"{num_val:02d}"
    base = item['target_wav'].replace('.wav', '')
    dur_val = item.get('duration_sec', 0)
    dur_str = f"{dur_val:.1f}s"
    vo_items.append({
        'num': n_str,
        'tc': item['tc'],
        'duration': dur_str,
        'title': base.split('_', 5)[-1].replace('_', ' '),
        'voice': 'Adam - Radio Announcer (ElevenLabs v4)',
        'wav_master': '03_AUDIO/voiceover/EP01_ALTMAN/' + base + '.wav',
        'mp3_master': '03_AUDIO/voiceover/EP01_ALTMAN/' + base + '.mp3',
        'web_preview': 'assets/audio_previews/vo/' + base + '.mp3',
        'davinci_track': 'A1 (VO EN 115 WPM • Broadcast 48k/24b WAV)',
        'words': item.get('words', 0)
    })

vo_json = json.dumps(vo_items, indent=6, ensure_ascii=False)

pattern = r'("01":\s*\{[\s\S]*?)("audio":\s*\[)'
replacement = r'\1"voiceover": ' + vo_json + ',\n    \\2'

new_content = re.sub(pattern, replacement, content, count=1)

with open(pool_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected 17 voiceover entries into media_acquisition_pool.js!")
