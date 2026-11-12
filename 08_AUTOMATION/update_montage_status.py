#!/usr/bin/env python3
"""
Записує стан монтажу в дашборд: 07_DASHBOARD/data/montage_status.js (window.MONTAGE_STATUS).
Дані беруться прямо з шот-листів (build_ep01_acts.py), тож дашборд завжди відповідає монтажу.
Запуск: python3 08_AUTOMATION/update_montage_status.py
"""
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_ep01_acts as B  # noqa: E402
import ep01_engine as E      # noqa: E402

BASE = E.BASE
OUT = os.path.join(BASE, "07_DASHBOARD", "data", "montage_status.js")


def mmss(frames):
    s = frames / E.FPS
    return f"{int(s // 60)}:{int(round(s % 60)):02d}"


IDX = None


def source_episode(name):
    """Номер епізоду, з якого походить кліп (за префіксом імені або папкою)."""
    global IDX
    m = re.match(r"(?i)ep(\d\d)_", name)
    if m:
        return m.group(1)
    IDX = IDX or E.index_files()
    path = E.find(IDX, name) or ""
    if "ep02_demis_hassabis" in path:      # папка генерацій для Хассабіса (епізод 03)
        return "03"
    return "01"


def main():
    titles = {"I": "Походження та кремнієвий щит", "II": "Код експоненти та народження OpenAI",
              "III": "Землетрус і п'ять днів бунту", "IV": "Кодекс будівничого та горизонт AGI"}
    acts, start, cross = [], 0, {}
    for key in ("I", "II", "III", "IV"):
        act, tl = B.ACTS[key]
        names = [r[1] for r in act["v1"]]
        for n in names:
            ep = source_episode(n)
            if ep != "01":
                cross.setdefault(ep, set()).add(n)
        acts.append({
            "act": key, "title": titles[key], "timeline": tl,
            "start": mmss(start), "duration": mmss(act["end_f"]),
            "shots": len(act["v1"]), "dubs": sorted(act["vo"].keys()),
            "music": ", ".join(m[0].replace(".wav", "") for m in act["music"]),
            "markers": [m[3] for m in act.get("markers", []) if m[1] in ("Green", "Red")],
        })
        start += act["end_f"]
    status = {
        "01": {
            "updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "headline": "Режисерська версія «Розмита межа» зібрана повністю",
            "concept": ("Альтман пише, що Mac «розмив лінію між внутрішнім світом і зовнішньою реальністю». "
                        "Внутрішній світ показано анімацією, реальний — фото й архівом; кожен поворотний момент героя — "
                        "морфінг анімації в реальність. Фінал римується з початком: CRT хлопчика вмикається знову, "
                        "корпус Mac із клацанням реле замикає епізод."),
            "project": "SEM (DaVinci Resolve Studio)",
            "full_timeline": "EP01_FULL_UA_Claude_DirectorsCut",
            "en_timeline": "EP01_FULL_EN_Claude_DirectorsCut",
            "en_duration": "12:39",
            "total_duration": mmss(start),
            "total_shots": sum(a["shots"] for a in acts),
            "acts": acts,
            "audio": [
                "Голос: −20 dBFS, 17 дублів вирівняно (розкид < 1 dB)",
                "Музика Suno: −22 dBFS у паузах, −32 під голосом (на 12 dB нижче диктора), автоматичний даккінг",
                "Живий звук кліпів і SFX: нормалізовано за виміряною гучністю, −36 під голосом / −28 у паузах",
                "Акт III: повна тиша на звільненні (Д12) за сценарієм, повернення ритму на «120 годинах»",
                "Пік −2 dBFS; для YouTube у Deliver увімкнути нормалізацію до −14 LUFS",
                "Ембієнт-мости між актами (8 с педу) замість провалів тиші",
            ],
            "cross_episode": {ep: sorted(v) for ep, v in sorted(cross.items())},
            "scripts": ["08_AUTOMATION/build_ep01_actI_claude_cut.py", "08_AUTOMATION/build_ep01_acts.py", "08_AUTOMATION/build_ep01_en.py", "08_AUTOMATION/make_ep01_en_graphics.py",
                        "08_AUTOMATION/ep01_engine.py", "08_AUTOMATION/make_ep01_actI_graphics.py",
                        "08_AUTOMATION/make_ep01_green_dot_card.py", "08_AUTOMATION/update_montage_status.py"],
            "fixes": [
                "Битий кадр 1:40 (JPEG з розширенням .png) замінено відновленим 4K-кліпом із повільним наїздом",
                "Сцена в соборі (1:22): новий 4K-кліп «крихітна постать у соборі»",
                "Наплави між дублями й актами, поява з чорного та фінальне затемнення",
                "Титри: плавна поява й зникнення (наплав 8 кадрів) — перевірено рендером",
                "Звук: повний рендер без провалів тиші на стиках актів, пік −2 dBFS",
                "Синхрон української версії звірено з планом до кадру після перезапуску Resolve (17 дублів, 165 планів)",
                "Відновлено 4 наплави, що раніше випадали в жорсткі склейки (5:47, 10:52, 13:00, 13:31)",
                "Англійська версія EP01_FULL_EN (12:39): англійський голос, титри й картки, свій мікс музики; бін 00_EP01_MASTER_UA_EN",
            ],
            "next": [
                "Прослухати мікс наживо (особливо Акт III і фінал) — обидві версії, UA і EN",
                "Deliver: нормалізація гучності −14 LUFS для YouTube",
                "Хронометраж 13:58 замість 20:30 за сценарієм — визначається довжиною озвучки",
            ],
        }
    }
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Згенеровано 08_AUTOMATION/update_montage_status.py — не редагувати вручну\n")
        f.write("window.MONTAGE_STATUS = " + json.dumps(status, ensure_ascii=False, indent=2) + ";\n")
    print(f"✓ {os.path.relpath(OUT, BASE)}: EP01 {status['01']['total_duration']}, "
          f"{status['01']['total_shots']} планів, матеріали з {len(cross)} інших епізодів")


if __name__ == "__main__":
    main()
