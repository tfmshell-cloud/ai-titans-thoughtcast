#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/08_AUTOMATION/scripts')
from generate_cinematic_innovations_ep02_html import INNOVATIONS

md_lines = [
    '# 20 Кінематографічних Тріад (Google Flow / Veo 2) — Епізод 02: Дженсен Хуанг',
    '**Серіал:** «Архітектори Розуму» // Cinematic Thoughtcast',
    '**Герой:** Дженсен Хуанг (Jensen Huang) — «Алхімія страждання та кремнію»',
    '**Стандарт:** 3-Промптна Тріада (Start Image A -> Google Flow Action -> End Image B)',
    '**Статус безпеки:** 100% Policy-Safe (Всі чутливі імена, бренди та документи замінено на кінематографічні контекстні архетипи)',
    '',
    '---',
    ''
]

for item in INNOVATIONS:
    md_lines.append(f"## #{item['num']}. {item['name_ua']} / {item['name_en']}")
    md_lines.append(f"**Таймкод:** `{item['tc']}` | **Акт:** {item['act']} | **Категорія:** {item['cat_label']}")
    md_lines.append(f"> «{item['tagline']}»")
    md_lines.append('')
    md_lines.append(f"**Концепція:** {item['concept']}")
    md_lines.append(f"**Психологія сприйняття:** {item['why_it_works']}")
    md_lines.append('')
    md_lines.append('### 🎯 Тріада для генерації:')
    md_lines.append('1. **ПРОМПТ 1: Start Image (Кадр А):**')
    md_lines.append(f"   ```text\n   {item['p1_start']}\n   ```")
    md_lines.append('2. **ПРОМПТ 2: Video Morph Action (Рух у Google Flow):**')
    md_lines.append(f"   ```text\n   {item['p2_flow']}\n   ```")
    md_lines.append('3. **ПРОМПТ 3: End Image (Кадр В - Фінал):**')
    md_lines.append(f"   ```text\n   {item['p3_end']}\n   ```")
    md_lines.append('')
    md_lines.append(f"- **✂️ DaVinci Resolve 19:** {item['davinci_recipe']}")
    md_lines.append(f"- **🔊 Fairlight SFX:** {item['sfx_cue']}")
    md_lines.append('')
    md_lines.append('---')
    md_lines.append('')

out_path = '/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/04_VIDEO_PROMPTS/ep02_huang_20_triads.md'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
print(f"Generated {out_path} ({len(md_lines)} lines)")
