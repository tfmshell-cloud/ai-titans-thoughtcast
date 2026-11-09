#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.append("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/08_AUTOMATION/scripts")
from generate_50_scenes_hassabis import SCENES

MD_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/01_RESEARCH/demis_hassabis/50_BIOGRAPHICAL_SCENES_VISUALIZATION.md"

def get_chapter(n):
    if n <= 10:
        return "АКТ 1: КОРІННЯ, БОГЕМА ТА ПЕРШІ КЛІТИНКИ (1976–1984)"
    elif n <= 20:
        return "АКТ 2: 8-БІТНЕ ОДРОВЕННЯ ТА ШАХОВИЙ ВУНДЕРКІНД (1984–1990)"
    elif n <= 26:
        return "АКТ 3: BULLFROG, THEME PARK ТА ПЕРШІ СИМУЛЯЦІЇ (1991–1994)"
    elif n <= 30:
        return "АКТ 4: КЕМБРИДЖ, DOUBLE FIRST ТА ELIXIR STUDIOS (1994–1998)"
    elif n <= 36:
        return "АКТ 5: ВТЕЧА В НЕЙРОНАУКУ ТА СВЯТИЙ ГРААЛЬ УЯВИ (2005–2009)"
    elif n <= 40:
        return "АКТ 6: НАРОДЖЕННЯ ЛАБОРАТОРІЇ ТА ПРОРИВ В ATARI (2010–2014)"
    elif n <= 44:
        return "АКТ 7: СЕУЛ, ХІД 37 ТА СЛЬОЗА ЧЕМПІОНА (2016–2017)"
    else:
        return "АКТ 8: КРОК ДРУГИЙ — ВІД ІГОР ДО БІОЛОГІЇ, ТА НАЙВИЩА НАГОРОДА (2018–2024+)"

lines = []
lines.append("# 50 Біографічних Сюжетів & Кінематографічних Тріад: Деміс Гассабіс (Епізод 03)")
lines.append("> **100% Policy-Safe (Zero Moderation Blocks) • Google Flow & Veo 2 Master Prompts**\n")
lines.append("Цей документ містить вичерпний режисерський каталог 50 ключових сцен із життя героя — від дитячої колиски у північному Лондоні та теслярської майстерні батька до розгадки 50-річного Святого Грааля біології та найвищої світової наукової нагороди 2024 року.\n")
lines.append("Кожна сцена реалізована за стандартом **Синергетичної 3-Промпт Тріади**:")
lines.append("1. **Prompt 1 (Start Frame A — 16:9):** Художній опис стартового візуального якоря.")
lines.append("2. **Prompt 2 (Flow Action Morph — 24fps):** Безперервна дія / оптична трансформація від кадру А до кадру Б.")
lines.append("3. **Prompt 3 (End Frame B — 16:9):** Фотореалістичний цільовий кадр, де рух зупиняється.")
lines.append("4. **DaVinci Resolve 19 Recipe:** Професійний колірний та Fusion пайплайн.")
lines.append("5. **Fairlight SFX Cue:** Саунд-дизайн та звуковий ландшафт.\n")
lines.append("---\n")

current_chap = None
for s in SCENES:
    n = int(s["num"])
    chap = get_chapter(n)
    if chap != current_chap:
        current_chap = chap
        lines.append(f"\n## 🏛️ {current_chap}\n")

    lines.append(f"### Сюжет #{s['num']}: {s['title']}")
    lines.append(f"- **Хронологія & Локація:** `{s['period']}`")
    lines.append(f"- **Драматичний наратив / Історичний факт:** {s['narrative']}")
    lines.append(f"- **Філософський символ / Сенс:** {s['symbol']}\n")
    lines.append("#### 🎬 Кінематографічна Тріада для Google Flow / Veo 2 / Midjourney\n")
    
    lines.append("**Prompt 1: Стартове зображення (Start Frame A — 16:9)**")
    lines.append("```text")
    lines.append(s["p1_start"])
    lines.append("```\n")

    lines.append("**Prompt 2: Трансформація / Дія (Flow Action Morph — 24fps)**")
    lines.append("```text")
    lines.append(s["p2_flow"])
    lines.append("```\n")

    lines.append("**Prompt 3: Фінальне зображення (End Frame B — 16:9)**")
    lines.append("```text")
    lines.append(s["p3_end"])
    lines.append("```\n")

    lines.append(f"**DaVinci Resolve 19 Колор / Fusion рецепт:** {s['davinci_recipe']}")
    lines.append(f"**Fairlight Саунд-дизайн (SFX):** {s['sfx_cue']}\n")
    lines.append("---\n")

with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Rendered Markdown to {MD_PATH} ({len(lines)} lines, {os.path.getsize(MD_PATH)} bytes)")
