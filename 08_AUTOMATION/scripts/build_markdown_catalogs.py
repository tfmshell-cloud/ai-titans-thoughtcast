#!/usr/bin/env python3
"""Generate clean markdown catalogs for EP01, EP03, EP06, EP10 and Master Registry."""
import os
import json

RAW_DIR = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/05_RAW_FOOTAGE"
DATA_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/data/media_acquisition_pool.js"

raw = open(DATA_PATH, "r", encoding="utf-8").read()
prefix = "window.MEDIA_ACQUISITION_POOL = "
data = json.loads(raw[len(prefix):].rstrip(";\n "))

EPISODES = [
    ("01", "EP01", "Сем Альтман", "Анатомія експоненти"),
    ("03", "EP03", "Деміс Гассабіс", "Гросмейстер біологічного коду"),
    ("06", "EP06", "Ілля Суцкевер", "Алхімік масштабування та тиші"),
    ("10", "EP10", "Ендрю Ин", "Вчитель світу та нова електрика")
]

for ep_key, ep_code, titan, title in EPISODES:
    ep_data = data.get(ep_key, {})
    q = ep_data.get("flow_queue", [])
    g = ep_data.get("flow_gallery", [])
    
    md_lines = [
        f"# {ep_code} — {titan} | Реєстр Медіаконтенту Google Flow & 2K Keyframes",
        "",
        f"> **Тема епізоду:** «{title}» (21:30 хв)",
        f"> **Пріоритетна черга:** {len(q)} базових сцен. **Галерея концепт-кадрів та B-roll:** {len(g)} асетів.",
        "",
        "## 1. Пріоритетна Черга Google Flow / Veo (10 базових сцен)",
        "",
        "| № | Статус | Таймкод | Назва сцени | Файл / Кадр | Технічні характеристики |",
        "| :-: | :-: | :-: | :--- | :--- | :--- |"
    ]
    for item in q:
        status_badge = "🟢 Відео готове" if item["status"] == "video_ready" else ("🔵 2K Кадр готовий" if item["status"] == "image_ready" else "⏳ У розробці")
        target_f = item.get("raw_video_path") or item.get("raw_image_path") or item.get("file", "")
        tc = item.get("tc", "")
        t = item.get("title", "")
        sp = item.get("specs", "")
        md_lines.append(f"| **{item['num']}** | {status_badge} | `{tc}` | **{t}** | `{target_f}` | {sp} |")
        
    md_lines.extend([
        "",
        f"## 2. Галерея 2K Концепт-Кадрів та Кінокадрів B-Roll ({len(g)} асетів)",
        "",
        "| Код | Бейдж | Таймкод | Назва асету | Локальний шлях | Роздільна здатність |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])
    for item in g:
        c = item.get("code", "")
        b = item.get("badge", "")
        tc = item.get("tc", "")
        t = item.get("title", "")
        rp = item.get("raw_path", "")
        dims = item.get("dims", "")
        md_lines.append(f"| **{c}** | {b} | `{tc}` | {t} | `{rp}` | {dims} |")
        
    out_md = os.path.join(RAW_DIR, f"{ep_code}_MEDIA_CATALOG.md")
    with open(out_md, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md_lines) + "\n")
    print(f"Generated {out_md}")

# Master Registry
master_lines = [
    "# SEASON 1 — MASTER MEDIA ACQUISITION REGISTRY",
    "",
    "Повний центральний звіт про стан візуальних асетів (Google Flow 4K/HD Video, 2K Keyframes, 4K Dossiers) у виробничому середовищі **«Cinematic Thoughtcast: AI Titans»**.",
    "",
    "## Зведена Таблиця Першого Сезону",
    "",
    "| Епізод | Герой | Відео Готові | 2K Кадри Готові | B-Roll & Студії | Всього Асетів | Статус Екосистеми |",
    "| :---: | :--- | :-: | :-: | :-: | :-: | :--- |",
    "| **EP01** | Сем Альтман | **4** (1080p/720p) | **6** (10/10 черга) | 21 кадри | **31 асетів** | 🚀 Черга заповнена на 100% |",
    "| **EP02** | Дженсен Хуанг | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP03** | Деміс Гассабіс | 0 | **3** (#01, #03, #07) | 9 кадрів | **12 асетів** | ♟️ Шахи, AlphaGo, 2K кадри |",
    "| **EP04** | Джеффрі Хінтон | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP05** | Ян Лекун | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP06** | Ілля Суцкевер | 0 | **3** (#01, #02, #04) | 1 кадр | **4 асети** | 🏛️ Єрусалим, Хінтон, AlexNet |",
    "| **EP07** | Даріо Амодей | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP08** | Фей-Фей Лі | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP09** | Йошуа Бенжіо | 0 | 0 | 0 | 0 | ⏳ У черзі генерації |",
    "| **EP10** | Ендрю Ин | 0 | **1** (#02) | 1 кадр | **2 асети** | 📚 Батько-лікар, 1984 |",
    "| **РАЗОМ** | **10 Титанів** | **4 відео** | **13 ключових 2K** | **32 B-Roll/Study** | **49 асетів** | 🎬 Виробничий спринт триває |"
]

master_path = os.path.join(RAW_DIR, "SEASON1_MEDIA_MASTER_REGISTRY.md")
with open(master_path, "w", encoding="utf-8") as fh:
    fh.write("\n".join(master_lines) + "\n")
print(f"Generated {master_path}")
