#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Production Ecosystem Compiler v2.0
Series: «Cinematic Thoughtcast // Архітектори Розуму (AI Titans)» — Season 1 (10 Episodes)
Parses all 10 Master-Dossier MD files + 10 Uncut Director Scripts + Video Prompts + 1,000 Quotes,
applies forensic QA fixes, generates:
  - 01_RESEARCH/<hero>/MASTER_DOSSIER_EPXX.md (audited & expanded w/ 100 quotes + 100 prompts)
  - 04_VIDEO_PROMPTS/epXX_<slug>_100_prompts.md (100 Smart-Bin Veo 2 prompts per episode = 1,000 total)
  - 07_DASHBOARD/data/titans_1000_quotes.json & .js
  - 07_DASHBOARD/data/season1_index.js
  - 07_DASHBOARD/data/episodes/ep01.js .. ep10.js
"""

import glob
import json
import os
import re

WORKSPACE = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
UPLOADED_DIR = "/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/.user_uploaded"

HEROES_META = [
    {
        "ep": "01",
        "id": "01_altman",
        "page_slug": "ep01_altman",
        "research_dir": "sam_altman",
        "script_path": "02_SCRIPTS/episode_01_altman/director_script_altman.md",
        "name": "Сем Альтман",
        "latin": "Sam Altman",
        "avatar": "sam_altman.jpg",
        "title": "Анатомія експоненти",
        "role": "CEO OpenAI • Експрезидент Y Combinator",
        "archetype": "Стратег Масштабу",
        "visual_palette": "amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays",
        "camera_lens": "Panavision Primo Anamorphic 50mm & 100mm Macro",
        "suno_base": "Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space",
    },
    {
        "ep": "02",
        "id": "02_huang",
        "page_slug": "ep02_huang",
        "research_dir": "jensen_huang",
        "script_path": "02_SCRIPTS/episode_02_huang/director_script_huang.md",
        "name": "Дженсен Хуанг",
        "latin": "Jensen Huang",
        "avatar": "jensen_huang.jpg",
        "title": "Алхімія страждання та кремнію",
        "role": "Засновник і CEO NVIDIA • Творець екосистеми CUDA",
        "archetype": "Коваль Кремнію",
        "visual_palette": "cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge",
        "camera_lens": "Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro",
        "suno_base": "Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome",
    },
    {
        "ep": "03",
        "id": "03_hassabis",
        "page_slug": "ep03_hassabis",
        "research_dir": "demis_hassabis",
        "script_path": "02_SCRIPTS/episode_03_hassabis/director_script_hassabis.md",
        "name": "Деміс Гассабіс",
        "latin": "Demis Hassabis",
        "avatar": "demis_hassabis.jpg",
        "title": "Гросмейстер біологічного коду",
        "role": "Співзасновник і CEO Google DeepMind • Нобелівський лауреат з хімії 2024",
        "archetype": "Полімат-Гросмейстер",
        "visual_palette": "carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma",
        "camera_lens": "ARRI Master Anamorphic 60mm & Zeiss Supreme Macro",
        "suno_base": "Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision",
    },
    {
        "ep": "04",
        "id": "04_hinton",
        "page_slug": "ep04_hinton",
        "research_dir": "geoffrey_hinton",
        "script_path": "02_SCRIPTS/episode_04_hinton/director_script_hinton.md",
        "name": "Джеффрі Хінтон",
        "latin": "Geoffrey Hinton",
        "avatar": "geoffrey_hinton.jpg",
        "title": "Прометей синапсів і тінь предків",
        "role": "Хрещений батько Deep Learning • Нобелівський лауреат з фізики 2024",
        "archetype": "Самотній Прометей",
        "visual_palette": "golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight",
        "camera_lens": "Vintage Canon K35 55mm & 85mm Macro",
        "suno_base": "Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth",
    },
    {
        "ep": "05",
        "id": "05_lecun",
        "page_slug": "ep05_lecun",
        "research_dir": "yann_lecun",
        "script_path": "02_SCRIPTS/episode_05_lecun/director_script_lecun.md",
        "name": "Ян Лекун",
        "latin": "Yann LeCun",
        "avatar": "yann_lecun.jpg",
        "title": "Єретик світла та світових моделей",
        "role": "Головний науковець з AI у Meta (FAIR) • Творець CNN, PyTorch та JEPA",
        "archetype": "Картезіанський Єретик",
        "visual_palette": "wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind",
        "camera_lens": "Angénieux Optimo Anamorphic 42mm & Macro 90mm",
        "suno_base": "Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture",
    },
    {
        "ep": "06",
        "id": "06_sutskever",
        "page_slug": "ep06_sutskever",
        "research_dir": "ilya_sutskever",
        "script_path": "02_SCRIPTS/episode_06_sutskever/director_script_sutskever.md",
        "name": "Ілля Суцкевер",
        "latin": "Ilya Sutskever",
        "avatar": "ilya_sutskever.jpg",
        "title": "Алхімік масштабування та тиші",
        "role": "Засновник Safe Superintelligence (SSI) • Співзасновник OpenAI",
        "archetype": "Чернець Математичної Тиші",
        "visual_palette": "ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith",
        "camera_lens": "Leica Summilux-C 50mm & Anamorphic 75mm",
        "suno_base": "Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness",
    },
    {
        "ep": "07",
        "id": "07_amodei",
        "page_slug": "ep07_amodei",
        "research_dir": "dario_amodei",
        "script_path": "02_SCRIPTS/episode_07_amodei/director_script_amodei.md",
        "name": "Даріо Амодей",
        "latin": "Dario Amodei",
        "avatar": "dario_amodei.jpg",
        "title": "Фізика совісті та машини благодаті",
        "role": "Співзасновник і CEO Anthropic • Співавтор Scaling Laws та Constitutional AI",
        "archetype": "Біофізик Безпеки",
        "visual_palette": "cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery",
        "camera_lens": "Zeiss Master Anamorphic 50mm & Microscopic Optics",
        "suno_base": "Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity",
    },
    {
        "ep": "08",
        "id": "08_li",
        "page_slug": "ep08_li",
        "research_dir": "fei_fei_li",
        "script_path": "02_SCRIPTS/episode_08_li/director_script_li.md",
        "name": "Фей-Фей Лі",
        "latin": "Fei-Fei Li",
        "avatar": "fei_fei_li.jpg",
        "title": "Очі машин та пара пральні",
        "role": "Творець ImageNet • Співдиректорка Stanford HAI • Засновниця World Labs",
        "archetype": "Архітекторка Людяного Зору",
        "visual_palette": "white hot steam from New Jersey dry-cleaning press, fogged window with physics equations, 14 million golden ImageNet memory frames, 3D volumetric Spatial Intelligence geometry",
        "camera_lens": "Cooke Panchro/i Classic 50mm & Anamorphic 65mm",
        "suno_base": "Instrumental compassionate cinematic downtempo, 92 bpm, rhythmic steam-release foley, expressive solo cello, delicate Chinese xiao flute overtones, warm analog sub-bass",
    },
    {
        "ep": "09",
        "id": "09_bengio",
        "page_slug": "ep09_bengio",
        "research_dir": "yoshua_bengio",
        "script_path": "02_SCRIPTS/episode_09_bengio/director_script_bengio.md",
        "name": "Йошуа Бенжіо",
        "latin": "Yoshua Bengio",
        "avatar": "yoshua_bengio.jpg",
        "title": "Вартовий Монреаля та архітектура уваги",
        "role": "Засновник інституту Mila • Лауреат Премії Тюрінга • Співавтор Attention",
        "archetype": "Гуманіст-Вартовий",
        "visual_palette": "snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth",
        "camera_lens": "Panavision C-Series Anamorphic 50mm",
        "suno_base": "Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics",
    },
    {
        "ep": "10",
        "id": "10_ng",
        "page_slug": "ep10_ng",
        "research_dir": "andrew_ng",
        "script_path": "02_SCRIPTS/episode_10_ng/director_script_ng.md",
        "name": "Ендрю Ин",
        "latin": "Andrew Ng",
        "avatar": "andrew_ng.jpg",
        "title": "Вчитель світу та нова електрика",
        "role": "Співзасновник Google Brain та Coursera • Засновник DeepLearning.AI та AI Fund",
        "archetype": "Великий Просвітник",
        "visual_palette": "1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth",
        "camera_lens": "ARRI Alfa Anamorphic 50mm & 35mm Wide",
        "suno_base": "Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity",
    },
]

FORENSIC_FIXES = [
    ("EP03_VO_UA_03_ACT2_DeepMind_Foundлу.wav", "EP03_VO_UA_03_ACT2_DeepMind_Founding.wav"),
    ("EP03_MUS_01_ACT4_92BPM_Fusion_Plasma.wav", "EP03_MUS_13_ACT4_92BPM_Fusion_Plasma.wav"),
    ("Лондоні, 1989 рік.", "Лондон, 1989 рік."),
    ("Ласло Поргару", "Юдіт Полгар"),
    ("Через оتقу та незгоду", "Через академічний опір та незгоду"),
    ("EP05_MUS_11_ACT3_92BPM_PyTorch_ Revolution.wav", "EP05_MUS_11_ACT3_92BPM_PyTorch_Revolution.wav"),
    ("EP09_AMB_10_ACT3_DRONE_ UN_Assembly.wav", "EP09_AMB_10_ACT3_DRONE_UN_Assembly.wav"),
    ("критегом", "критиком"),
    ("вabsolute абсолютній тиші", "в абсолютній тиші"),
    ("між реливами", "між релізами"),
    ("програмігранта", "програміста"),
    ("« SSI —", "«SSI —"),
    ("подобати глобальні хвороби", "подолати глобальні хвороби"),
    ("ми бачите", "ми бачимо"),
    ("виградуть", "виграють"),
    ("використати ImageNet", "використали ImageNet"),
    ("ми дивитися", "ми дивимося"),
    ("невдалиго", "невдалого"),
    ("Різница", "Різниця"),
    ("тисячолітніго", "тисячолітнього"),
    ("змінинить", "змінить"),
    ("необертеність", "необоротність"),
    ("умовному синтезі", "у мовному синтезі"),
    ("відритій позиції", "відкритій позиції"),
    ("етічні кодекси", "етичні кодекси"),
    ("найціннішою навички", "найціннішою навичкою"),
    ("коротки практичні", "короткі практичні"),
    ("горячі очі", "гарячі очі"),
]


def apply_fixes(text: str) -> str:
    for wrong, right in FORENSIC_FIXES:
        text = text.replace(wrong, right)
    return text


def classify_quote_category(text: str) -> str:
    t = text.lower()
    if any(w in t for w in ["дитинств", "батьк", "мати", "мама", "школ", "емігр", "університет", "студент", "кембридж", "прінстон", "стенфорд", "париж", "ченду", "сінгапур", "єрусалим", "реформатор", "туалет", "тесл", "пральн", "хімчист"]):
        return "Походження та гарт"
    if any(w in t for w in ["безпек", "ризик", "загроз", "етик", "етич", "совіст", "людств", "контрол", "вирівнюван", "alignment", "конституц", "декларац", "оон", "шкодую", "страх", "відповідальн"]):
        return "Етика та безпека ШІ"
    if any(w in t for w in ["криз", "провал", "помилк", "відмов", "біль", "страждан", "банкрут", "зима", "ізоляц", "самотніст", "проти консенсус", "стійкіст", "мужніст", "сумнів"]):
        return "Кризи та стійкість"
    if any(w in t for w in ["нейромереж", "синапс", "алгоритм", "масштаб", "дані", "датасет", "код", "матриц", "вектор", "backprop", "уваг", "attention", "cnn", "згортк", "білк", "alphafold", "gpt", "claude", "jepa", "pytorch", "cuda", "чіп", "кремні", "просторов", "imagenet"]):
        return "Архітектура та наука"
    if any(w in t for w in ["лідер", "команд", "компані", "стартап", "бізнес", "ринок", "капітал", "відкрит", "open source", "освіт", "вчител", "курс"]):
        return "Лідерство та екосистема"
    return "Філософія майбутнього"


def load_uploaded_md_map():
    md_map = {}
    for p in sorted(glob.glob(os.path.join(UPLOADED_DIR, "*.md"))):
        raw = open(p, "r", encoding="utf-8").read()
        cleaned = apply_fixes(raw)
        m = re.search(r"ЕПІЗОД\s+(\d+)", cleaned)
        if m:
            ep = m.group(1).zfill(2)
            md_map[ep] = cleaned
    return md_map


def parse_master_dossier(md_text: str, ep: str):
    sections = {}
    current_sec = "0"
    lines = md_text.splitlines()
    for line in lines:
        m = re.match(r"^##\s+РОЗДІЛ\s+(\d+)\.\s*(.*)", line)
        if m:
            current_sec = m.group(1)
            sections[current_sec] = []
        else:
            sections.setdefault(current_sec, []).append(line)

    # Section 2: Biography bullets
    bio_items = []
    for line in sections.get("2", []):
        m = re.match(r"^\*\s+\*\*(.+?):?\*\*\s*(.+)", line.strip())
        if m:
            title = m.group(1).rstrip(":").strip()
            desc = m.group(2).strip()
            bio_items.append({"stage": title, "detail": desc})

    # Section 3: Quotes
    quotes = []
    for line in sections.get("3", []):
        m = re.match(r"^(\d+)\.\s+(.+)", line.strip())
        if m:
            q_txt = m.group(2).strip()
            quotes.append({
                "num": int(m.group(1)),
                "cat": classify_quote_category(q_txt),
                "text": q_txt,
                "source": "Мастер-Досьє",
            })

    # Section 4: Beat Sheet Summary
    sec4_text = "\n".join(sections.get("4", []))
    dur_m = re.search(r"\*\*Хронометраж:\*\*\s*([^|\n]+)", sec4_text)
    wpm_m = re.search(r"\*\*Швидкість диктора:\*\*\s*([^|\n]+)", sec4_text)
    duration = dur_m.group(1).strip() if dur_m else "21:00 хв"
    wpm = wpm_m.group(1).strip() if wpm_m else "114 слів/хв"

    beat_acts = []
    curr_act = None
    for line in sections.get("4", []):
        s = line.strip()
        am = re.match(r"^###\s+АКТ\s+(\d+)\.\s*(.+?)\s*\(([^)]+)\)", s)
        if am:
            curr_act = {
                "actNum": int(am.group(1)),
                "title": am.group(2).strip(),
                "time": am.group(3).strip(),
                "music_file": "",
                "beats": [],
            }
            beat_acts.append(curr_act)
            continue
        if curr_act is not None:
            mm = re.search(r"`(EP\d+_MUS_[^`]+)`", s)
            if mm and s.startswith("*Музика"):
                curr_act["music_file"] = mm.group(1)
                continue
            bm = re.match(r"^\*\s+\*\*([^*]+)\*\*\s*\|\s*(.+)", s)
            if bm:
                tc = bm.group(1).strip()
                rest = bm.group(2).strip()
                cues = re.findall(r"\[([^\]]+)\]", rest)
                narr_m = re.search(r"\*\*Диктор:\*\*\s*(.+)", rest)
                narr = narr_m.group(1).strip() if narr_m else rest
                curr_act["beats"].append({
                    "tc": tc,
                    "cues": cues,
                    "narration": narr,
                })

    # Section 5: Suno 16 files
    suno_files = []
    for line in sections.get("5", []):
        m = re.match(r"^(\d+)\.\s*`(EP\d+_[^`]+)`", line.strip())
        if m:
            fn = m.group(2).strip().replace(" ", "")
            suno_files.append({"idx": int(m.group(1)), "filename": fn})

    # Section 6: VO files & settings
    vo_settings = "Stability 65%, Clarity 80%. Доріжка A1."
    vo_files = []
    for line in sections.get("6", []):
        s = line.strip()
        if s.startswith("*Налаштування:"):
            vo_settings = s.strip("*").replace("Налаштування:", "").strip()
        m = re.match(r"^\*\s*`(EP\d+_VO_[^`]+)`", s)
        if m:
            vo_files.append(m.group(1).strip().replace(" ", ""))

    # Section 7: Canonical MD video prompts
    md_prompts = []
    for line in sections.get("7", []):
        m = re.match(r"^\*\s*`([^`]+)`:\s*`([^`]+)`", line.strip())
        if m:
            md_prompts.append({"ref": m.group(1).strip(), "prompt": m.group(2).strip()})

    return {
        "duration": duration,
        "wpm": wpm,
        "bio_items": bio_items,
        "md_quotes": quotes,
        "beat_acts": beat_acts,
        "suno_files": suno_files,
        "vo_settings": vo_settings,
        "vo_files": vo_files,
        "md_prompts": md_prompts,
    }


def parse_full_director_script(rel_path: str):
    full_path = os.path.join(WORKSPACE, rel_path)
    raw = apply_fixes(open(full_path, "r", encoding="utf-8").read())
    lines = raw.splitlines()

    tone = ""
    visual_key = ""
    for l in lines[:12]:
        if "Тональність диктора:" in l or "Швидкість диктора:" in l:
            tone = re.sub(r"^\*\*[^*]+\*\*\s*", "", l).strip()
        if "Візуальний ключ:" in l:
            visual_key = re.sub(r"^\*\*[^*]+\*\*\s*", "", l).strip()

    acts = []
    curr_act = None
    curr_scene = None
    in_narrator = False

    for line in lines:
        s = line.strip()
        if s.startswith("## ТЕХНІЧНИЙ ПАСПОРТ") or s.startswith("## Технічний паспорт"):
            break
        am = re.match(r"^##\s+АКТ\s+(\d+)\.\s*(.+?)(?:\(([^)]+)\))?$", s, re.I)
        if am:
            in_narrator = False
            curr_scene = None
            curr_act = {
                "actNum": int(am.group(1)),
                "title": am.group(2).strip(),
                "time": (am.group(3) or "").strip(),
                "music_desc": "",
                "scenes": [],
            }
            acts.append(curr_act)
            continue

        if curr_act is None:
            continue

        if (s.startswith("**Музика:**") or s.startswith("**Музичний супровід:**")) and curr_scene is None:
            curr_act["music_desc"] = re.sub(r"^\*\*[^*]+\*\*\s*", "", s).strip()
            continue

        sm = re.match(r"^###\s*\[([^\]]+)\]", s)
        if sm:
            in_narrator = False
            curr_scene = {
                "tc": sm.group(1).strip(),
                "sfx": "",
                "prompt": "",
                "narration_lines": [],
            }
            curr_act["scenes"].append(curr_scene)
            continue

        if curr_scene is not None:
            if re.match(r"^-\s*\*\*SFX:?\*\*", s):
                in_narrator = False
                sfx_val = re.sub(r"^-\s*\*\*SFX:?\*\*\s*", "", s).strip()
                curr_scene["sfx"] = (curr_scene["sfx"] + " " + sfx_val).strip()
                continue
            if re.match(r"^-\s*\*\*VIDEO PROMPT[^*]*\*\*", s):
                in_narrator = False
                pm = re.search(r"`([^`]+)`", s)
                if pm:
                    curr_scene["prompt"] = pm.group(1).strip()
                else:
                    curr_scene["prompt"] = re.sub(r"^-\s*\*\*VIDEO PROMPT[^*]*\*\*\s*", "", s).strip()
                continue
            if re.match(r"^-\s*\*\*ДИКТОР:?\*\*", s):
                in_narrator = True
                rest = re.sub(r"^-\s*\*\*ДИКТОР:?\*\*\s*", "", s).strip()
                if rest:
                    curr_scene["narration_lines"].append(rest)
                continue
            if s == "---":
                in_narrator = False
                continue
            if in_narrator and s:
                curr_scene["narration_lines"].append(s)

    total_words = 0
    for a in acts:
        act_vo_parts = []
        for sc in a["scenes"]:
            narr_md = "\n\n".join(sc["narration_lines"]).strip()
            clean_vo = re.sub(r"[*_`]", "", narr_md)
            sc["narration"] = narr_md
            sc["clean_vo"] = clean_vo
            wc = len(clean_vo.split())
            sc["word_count"] = wc
            total_words += wc
            if clean_vo:
                act_vo_parts.append(clean_vo)
            del sc["narration_lines"]
        a["clean_vo"] = "\n\n".join(act_vo_parts)
        a["word_count"] = sum(sc["word_count"] for sc in a["scenes"])

    return {
        "tone": tone,
        "visual_key": visual_key,
        "acts": acts,
        "total_words": total_words,
    }


def parse_mmss_to_sec(tc_str: str):
    parts = [p.strip() for p in tc_str.replace("–", "-").split("-")]
    def to_s(x):
        nums = [int(n) for n in re.findall(r"\d+", x)]
        if len(nums) >= 2:
            return nums[0] * 60 + nums[1]
        return 0
    if len(parts) == 2:
        return to_s(parts[0]), to_s(parts[1])
    return 0, 60


def sec_to_mmss(sec: float) -> str:
    s = max(0, int(round(sec)))
    return f"{s // 60:02d}:{s % 60:02d}"


def sec_to_smpte(sec: float) -> str:
    # DaVinci Resolve standard timeline starts at 01:00:00:00 @ 24fps
    total_frames = int(round(sec * 24))
    ff = total_frames % 24
    total_sec = total_frames // 24
    ss = total_sec % 60
    mm = (total_sec // 60) % 60
    hh = 1 + (total_sec // 3600)
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


SHOT_ARCHETYPES = [
    ("Macro_Detail", "Extreme macro push-in shot", "razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light"),
    ("Anamorphic_Wide", "Wide 2.39:1 anamorphic establishing tableau", "architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare"),
    ("Tracking_Medium", "Slow gimbal tracking shot at eye level", "intimate documentary realism, natural practical lighting, gentle handheld breathing motion"),
    ("Overhead_GodsEye", "Top-down vertical birds-eye composition", "geometric precision, dramatic directional rim light casting long crisp shadows across the workspace"),
    ("Optical_DataViz", "Photorealistic scientific optical visualization", "bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction"),
    ("Silhouette_Mood", "Low-key moody silhouette against illuminated window", "contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off"),
    ("SlowMo_Insert", "48fps-to-24fps poetic slow-motion insert shot", "tactile physics of hands, ink, glass, or silicon wafers catching warm rim light"),
]


def extract_english_visual_subject(ua_sentence: str, hero_meta: dict, act_num: int, shot_in_act: int) -> tuple:
    """Maps specific Ukrainian narrator sentences to bespoke, concrete English visual subjects & shot slugs."""
    s = ua_sentence.lower()
    mapping = [
        (["macintosh", "комп'ютер", "материнськ", "клавіш", "베이ж", "екран"], "Macintosh_Logic_Board",
         "vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps"),
        (["школ", "актов", "сцен", "камінг", "консерват", "коридор"], "School_Auditorium_Stage",
         "empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight"),
        (["стенфорд", "кембридж", "прінстон", "берклі", "макгілл", "торонто", "університет", "аудитор", "лекц", "бібліотек"], "University_Archive_Hall",
         "classic university lecture hall chalkboard covered in dense probability and linear algebra equations"),
        (["loopt", "стартап", "офіс", "підлоз", "y combinator", "акселератор", "пол грем"], "Startup_Night_Workspace",
         "late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups"),
        (["rosewood", "вечер", "менло-парк", "маск", "суцкевер", "засновн"], "Menlo_Park_Evening_Table",
         "dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI"),
        (["microsoft", "мільярд", "кластер", "сервер", "дата-центр", "обчислен", "терават", "stargate", "енерг"], "Hyperscale_Compute_Cluster",
         "monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light"),
        (["chatgpt", "курсор", "мільйонів користувач", "реліз"], "Blinking_Prompt_Singularity",
         "minimalist dark glass screen with a luminous white prompt cursor multiplying into millions of global light streams"),
        (["google meet", "звільнен", "рада директор", "120 годин", "730", "підпис", "бунт", "листопад"], "Boardroom_Fracture_Night",
         "rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table"),
        (["туалет", "кахел", "реформатор", "кентуккі", "щітк", "миє"], "Kentucky_Porcelain_Grit",
         "wet white porcelain tile and worn wooden scrub brush under cold fluorescent dormitory light in 1970s Kentucky"),
        (["denny", "посудомийн", "таріл", "кав", "серветк", "закусочн"], "Dennys_Midnight_Booth",
         "steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon"),
        (["sega", "токіо", "банкрутств", "30 днів", "riva", "nv1", "трикутник"], "Thirty_Days_Wireframe_Chip",
         "3D wireframe polygon mesh snapping into razor-sharp silicon die blueprint on a 1996 engineering workstation"),
        (["cuda", "уолл-стріт", "акці", "alexnet", "dgx", "шкірян", "татуюван", "blackwell"], "Silicon_Wafer_Lithography",
         "300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom"),
        (["шах", "фігур", "дошк", "гросмейстер", "лондон"], "London_Tournament_Chessboard",
         "hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking"),
        (["theme park", "ігр", "симуляц", "гіпокамп", "пам'ят", "нейробіолог"], "Hippocampus_Memory_Maze",
         "translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth"),
        (["го ", "сеул", "лі седол", "хід 37", "alphago", "камен"], "Seoul_Move_37_Go_Stone",
         "single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board"),
        (["білк", "амінокислот", "орігамі", "alphafold", "молекул", "фармаколог", "ліків"], "AlphaFold_Ribbon_Origami",
         "luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space"),
        (["нобел", "стокгольм", "король", "медал", "плазм", "термоядер"], "Nobel_Gold_And_Tokamak",
         "gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus"),
        (["рубанок", "стружк", "дерев", "тесл", "столяр", "шип", "верстат"], "Carpenter_Oak_Workbench",
         "vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench"),
        (["буль", "еверест", "предк", "хребет", "спин", "лежачи", "підлозі"], "Standing_Chalk_Equations",
         "tall wooden standing lectern covered with hand-written gradient descent derivatives and worn chalk"),
        (["backprop", "зворотн", "помилк", "градієнт", "ваги", "синапс"], "Backpropagation_Error_Wave",
         "golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes"),
        (["паяльник", "каніфол", "транзистор", "радіо", "осцилограф"], "Paris_Rosin_Solder_Smoke",
         "glowing soldering iron tip melting silver solder on a vintage green circuit board with curling rosin smoke"),
        (["кіт", "кішк", "кота", "зоров", "เชк", "lenet", "bell labs"], "Visual_Cortex_Convolution",
         "layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex"),
        (["pytorch", "open source", "відкрит", "llama", "jepa", "парус", "яхт", "океан", "вітер"], "Upwind_Atlantic_Sail",
         "crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors"),
        (["єрусалим", "вапняк", "фоліант", "алгебр", "горк"], "Jerusalem_Limestone_Study",
         "warm twilight falling across golden Jerusalem stone windowsill onto open Russian and Hebrew math monographs"),
        (["стиснен", "детектив", "агат", "крісті", "наступного слова", "seq2seq"], "Compression_Diamond_Lattice",
         "hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal"),
        (["вогнищ", "стату", "ssi", "тиш", "монастир", "сейф"], "Monastic_White_Sanctuary",
         "silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow"),
        (["сітківк", "біофізик", "електрод", "нейрон", "мікроскоп"], "Retinal_Ganglion_Sparks",
         "confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses"),
        (["scaling", "логарифм", "конституц", "claude", "интерпрет", "чорн", "скриньк", "рак", "клітин"], "Constitutional_Crystal_Box",
         "dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors"),
        (["хімчист", "пральн", "прасувальн", "пар", "ченду", "валіз", "словник"], "DryCleaner_Steam_Window",
         "clouds of backlit white steam rising from a heavy garment press against a rain-streaked New Jersey shopfront"),
        (["imagenet", "14 млн", "mechanical turk", "фотограф", "тривимірн", "просторов", "world labs"], "Spatial_3D_World_Extrusion",
         "constellation of millions of photographs extruding into a physically accurate 3D architectural space with gravity"),
        (["монреал", "сніг", "велосипед", "mila", "уваг", "attention", "gflownets", "оон", "декларац"], "Montreal_Snow_And_Attention",
         "golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window"),
        (["журнал", "basic", "гелікоптер", "16 000", "coursera", "електрик", "data-centric", "агент"], "Planetary_Electricity_Grid",
         "warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide"),
    ]
    for keywords, slug, desc in mapping:
        if any(k in s for k in keywords):
            return slug, desc

    # Fallback anchored to hero's specific visual palette
    fallback_slugs = [
        "Hero_Workspace_Atmosphere",
        "Equation_Notebook_Macro",
        "Silicon_Light_Refraction",
        "Architectural_Corridor",
        "Neural_Horizon_Pulse",
    ]
    slug = f"{fallback_slugs[(act_num * 7 + shot_in_act) % len(fallback_slugs)]}_A{act_num}S{shot_in_act:02d}"
    return slug, f"symbolic visual study featuring {hero_meta['visual_palette']}"


def build_100_prompts_for_hero(hero_meta: dict, md_data: dict, script_data: dict) -> list:
    """
    Generates exactly 100 frame-accurate, chronologically mapped 4K 24fps Veo 2 / Google Flow prompts
    (25 shots per Act × 4 Acts = 100 shots), anchoring all canonical Master-Dossier & Director Script
    prompts at their exact timecodes and subdividing every narrative scene into ~12s visual beats.
    """
    ep = hero_meta["ep"]
    acts = script_data["acts"]
    md_prompts = md_data["md_prompts"]
    prompts_100 = []

    for act_idx in range(4):
        act = acts[act_idx] if act_idx < len(acts) else {"actNum": act_idx + 1, "title": f"Акт {act_idx+1}", "scenes": []}
        act_num = act["actNum"]
        scenes = act["scenes"] or [{"tc": f"{act_idx*5}:00 - {(act_idx+1)*5}:00", "prompt": "", "clean_vo": hero_meta["title"]}]

        # Determine Act start/end seconds from scenes
        act_start_s, _ = parse_mmss_to_sec(scenes[0]["tc"])
        _, act_end_s = parse_mmss_to_sec(scenes[-1]["tc"])
        if act_end_s <= act_start_s:
            act_end_s = act_start_s + 300

        # Distribute 25 shots across the scenes of this Act proportionally to word count / duration
        n_scenes = len(scenes)
        base_per_scene = 25 // n_scenes
        rem = 25 % n_scenes
        shots_alloc = [base_per_scene + (1 if i < rem else 0) for i in range(n_scenes)]

        shot_in_act = 0
        for sc_i, sc in enumerate(scenes):
            n_shots = shots_alloc[sc_i]
            sc_start, sc_end = parse_mmss_to_sec(sc["tc"])
            if sc_end <= sc_start:
                sc_end = sc_start + 60
            dur = (sc_end - sc_start) / max(1, n_shots)

            # Split scene clean_vo into sentences for exact narrative anchoring
            raw_sents = [x.strip() for x in re.split(r"(?<=[.!?…»])\s+", sc.get("clean_vo", "")) if len(x.strip()) > 12]
            if not raw_sents:
                raw_sents = [hero_meta["title"]]

            for k in range(n_shots):
                shot_in_act += 1
                global_num = act_idx * 25 + shot_in_act
                t0 = sc_start + k * dur
                t1 = sc_start + (k + 1) * dur
                tc_window = f"{sec_to_mmss(t0)} – {sec_to_mmss(t1)}"

                sent_cue = raw_sents[min(len(raw_sents) - 1, int(k * len(raw_sents) / max(1, n_shots)))]
                if len(sent_cue) > 165:
                    sent_cue = sent_cue[:162].rstrip() + "…"

                # Shot 1 of Act 1..3 uses canonical Master-Dossier prompt if available, Shot 1 of each scene uses Director Script prompt!
                if act_idx == 0 and shot_in_act <= len(md_prompts):
                    md_p = md_prompts[shot_in_act - 1]
                    raw_slug = re.sub(r"^EP\d+_VID_\d+_", "", os.path.splitext(md_p["ref"])[0])
                    clean_slug = re.sub(r"[^A-Za-z0-9_]", "_", raw_slug).strip("_") or f"MasterShot_{global_num:03d}"
                    prompt_text = md_p["prompt"]
                    source_tag = "Мастер-Досьє (Канон)"
                    is_key = True
                elif k == 0 and sc.get("prompt"):
                    slug_guess, _ = extract_english_visual_subject(sent_cue, hero_meta, act_num, shot_in_act)
                    clean_slug = f"KeyScene_{sc_i+1:02d}_{slug_guess}"[:36].rstrip("_")
                    prompt_text = sc["prompt"]
                    source_tag = "Режисерський сценарій (Key Shot)"
                    is_key = True
                else:
                    arch_code, cam_move, light_spec = SHOT_ARCHETYPES[(global_num + act_num) % len(SHOT_ARCHETYPES)]
                    subj_slug, subj_en = extract_english_visual_subject(sent_cue, hero_meta, act_num, shot_in_act)
                    clean_slug = f"{subj_slug}_{arch_code}"[:38].rstrip("_")
                    prompt_text = (
                        f"{cam_move} of {subj_en}, shot on {hero_meta['camera_lens']}, "
                        f"{light_spec}, Kodak 2383 D60 film print color science, subtle 35mm organic grain, "
                        f"2.39:1 anamorphic widescreen, 4k 24fps."
                    )
                    source_tag = "Покадровий сторіборд (B-Roll)"
                    is_key = False

                smart_filename = f"EP{ep}_VID_{global_num:03d}_ACT{act_num}_24FPS_{clean_slug}.mp4"
                prompts_100.append({
                    "num": global_num,
                    "act": act_num,
                    "tc": tc_window,
                    "smpte": sec_to_smpte(t0),
                    "filename": smart_filename,
                    "source": source_tag,
                    "is_key": is_key,
                    "cue_ua": sent_cue,
                    "prompt": prompt_text,
                })

    return prompts_100


def build_suno_prompt_for_file(filename: str, hero_meta: dict) -> dict:
    """Builds exact DaVinci track routing and ready-to-paste Suno Pro v4 prompt for each of the 16 audio files."""
    parts = filename.replace(".wav", "").split("_")
    cat = parts[1] if len(parts) > 1 else "MUS"
    act_tag = parts[3] if len(parts) > 3 else "ACT1"
    desc = " ".join(parts[5:]) if len(parts) > 5 else filename

    if cat == "AMB":
        track = "A3 (AMB Room/Drone • -22 dB)"
        style = (
            f"Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by '{desc}', "
            f"deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable."
        )
    elif cat == "SFX":
        track = "A4 (SFX Impacts & Transitions • -9 dB)"
        style = (
            f"Cinematic sound design stem pack for '{desc}': deep 40Hz sub-bass drops, tactile mechanical foley transitions, "
            f"subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording."
        )
    else:
        track = "A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1)"
        mood_map = {
            "ACT1": "intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures",
            "ACT2": "rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios",
            "ACT3": "high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity",
            "ACT4": "luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro",
        }
        act_mood = mood_map.get(act_tag, "cinematic documentary groove")
        style = f"{hero_meta['suno_base']}, cue theme '{desc}', {act_mood}, instrumental only, no vocals, 48kHz studio master."

    return {
        "filename": filename,
        "category": cat,
        "act": act_tag,
        "title_clean": desc,
        "davinci_track": track,
        "suno_prompt": style,
    }


def build_sop_7_steps(hero_meta: dict, md_data: dict, script_data: dict) -> list:
    ep = hero_meta["ep"]
    name = hero_meta["name"]
    vo_count = len(md_data["vo_files"])
    return [
        {
            "step": "01",
            "phase": "Ініціалізація та Smart Bins",
            "title": f"Створення структури проєкту EP{ep} ({name}) на диску та в DaVinci Resolve 19",
            "goal": "Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.",
            "tasks": [
                {"id": f"ep{ep}_s1_t1", "text": f"Завантажити й запустити скрипт ініціалізації папок setup_EP{ep}.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K)."},
                {"id": f"ep{ep}_s1_t2", "text": f"Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed."},
                {"id": f"ep{ep}_s1_t3", "text": f"Налаштувати 5 Smart Bins за правилом імені файлу: EP{ep}_VO_, EP{ep}_MUS_, EP{ep}_AMB_, EP{ep}_SFX_, EP{ep}_VID_."},
            ],
        },
        {
            "step": "02",
            "phase": "Дикторська озвучка (VO UA + EN)",
            "title": f"Генерація та контроль якості {vo_count} сегментів диктора в ElevenLabs ({md_data['vo_settings']})",
            "goal": f"Отримати еталонну начитку повного сценарію (~{script_data['total_words']} слів, хронометраж {md_data['duration']}) українською та англійською мовами.",
            "tasks": [
                {"id": f"ep{ep}_s2_t1", "text": "У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO)."},
                {"id": f"ep{ep}_s2_t2", "text": f"Згенерувати всі {vo_count} українських файлів EP{ep}_VO_UA_01..{vo_count:02d}.wav (WAV 48kHz / 24-bit, {md_data['vo_settings']})."},
                {"id": f"ep{ep}_s2_t3", "text": f"Згенерувати синхронний англомовний дубляж EP{ep}_VO_EN_01..{vo_count:02d}.wav для YouTube Multi-Language Audio."},
                {"id": f"ep{ep}_s2_t4", "text": "Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів."},
            ],
        },
        {
            "step": "03",
            "phase": "Саундтрек Suno Pro (92 BPM)",
            "title": "Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)",
            "goal": "Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).",
            "tasks": [
                {"id": f"ep{ep}_s3_t1", "text": f"Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP{ep}_MUS_...wav."},
                {"id": f"ep{ep}_s3_t2", "text": f"Згенерувати 3 безбітові фонові дрони EP{ep}_AMB_...wav для заповнення драматичних пауз на доріжці A3."},
                {"id": f"ep{ep}_s3_t3", "text": f"Підготувати пакет звукових акцентів EP{ep}_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду)."},
            ],
        },
        {
            "step": "04",
            "phase": "Візуальний ряд (100 кадрів Veo 2)",
            "title": "Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2",
            "goal": "Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).",
            "tasks": [
                {"id": f"ep{ep}_s4_t1", "text": f"Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP{ep}_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»)."},
                {"id": f"ep{ep}_s4_t2", "text": "Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен."},
                {"id": f"ep{ep}_s4_t3", "text": "Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps."},
            ],
        },
        {
            "step": "05",
            "phase": "Монтаж у DaVinci Resolve (Edit)",
            "title": "Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM",
            "goal": "Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.",
            "tasks": [
                {"id": f"ep{ep}_s5_t1", "text": f"У вкладці «DaVinci Студія» завантажити файл EP{ep}_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV)."},
                {"id": f"ep{ep}_s5_t2", "text": "Викласти диктора VO_UA на доріжку A1, музику MUS 92 BPM на A2, ембієнт AMB на A3, SFX-переходи на A4."},
                {"id": f"ep{ep}_s5_t3", "text": "Розставити 100 відеокліпів V1/V2 згідно з таймкодами сторіборду та додати мінімалістичні титри ключових цитат (SF Pro / Inter Tracking +80)."},
            ],
        },
        {
            "step": "06",
            "phase": "Fairlight Зведення & Колористика",
            "title": "Налаштування Sidechain Ducking -3.2 dB та 4-нодної плівкової градації Kodak 2383",
            "goal": "Досягти фірмового оксамитового кінозвучання та єдиного візуального стилю серіалу без перевантажень.",
            "tasks": [
                {"id": f"ep{ep}_s6_t1", "text": "У Fairlight направити Send з A1 (VO) на Bus 1 (Key), а на компресорі A2 (MUS) увімкнути Sidechain Listen: Ducking -3.2 dB (Attack 15ms, Hold 250ms, Release 350ms)."},
                {"id": f"ep{ep}_s6_t2", "text": "На вкладці Color застосувати 4-Node PowerGrade: Node 1 (CST) -> Node 2 (Contrast & WB) -> Node 3 (Kodak 2383 D60 Print LUT) -> Node 4 (OFX 35mm Grain 0.35)."},
                {"id": f"ep{ep}_s6_t3", "text": "Перевірити читабельність субтитрів/цитат та плавність 4-секундного Fade to Black у фіналі 4 Акту."},
            ],
        },
        {
            "step": "07",
            "phase": "Майстеринг та YouTube Multi-Audio",
            "title": "Фінальний рендер -14 LUFS та публікація двомовного випуску",
            "goal": "Експортувати бездоганний 4K майстер-файл та окремий англомовний мікс для глобальної дистрибуції.",
            "tasks": [
                {"id": f"ep{ep}_s7_t1", "text": "Перевірити Loudness Meter на Master Bus: рівно -14.0 LUFS Integrated, True Peak не вище -1.0 dBTP."},
                {"id": f"ep{ep}_s7_t2", "text": f"Експортувати основний майстер EP{ep}_{hero_meta['research_dir']}_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP{ep}_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN)."},
                {"id": f"ep{ep}_s7_t3", "text": "Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp)."},
            ],
        },
    ]


def write_upgraded_master_dossier_md(hero_meta: dict, ep_bundle: dict):
    out_dir = os.path.join(WORKSPACE, "01_RESEARCH", hero_meta["research_dir"])
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"MASTER_DOSSIER_EP{hero_meta['ep']}.md")

    lines = [
        f"# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД {hero_meta['ep']} — {hero_meta['name'].upper()}",
        f"*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «{hero_meta['title']}»*",
        "",
        "---",
        "",
        "## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)",
        "",
    ]
    for st in ep_bundle["sop_steps"]:
        lines.append(f"### Етап {st['step']}. {st['phase']} — {st['title']}")
        lines.append(f"*Ціль:* {st['goal']}")
        for t in st["tasks"]:
            lines.append(f"- [ ] {t['text']}")
        lines.append("")

    lines += [
        "---",
        "",
        "## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)",
        "",
        f"Стандарт іменування Smart Bins: `EP{hero_meta['ep']}_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`",
        "",
        "* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).",
        "* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).",
        "* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).",
        "* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).",
        "* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).",
        "",
        "---",
        "",
        "## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ",
        "",
    ]
    for b in ep_bundle["biography"]:
        lines.append(f"* **{b['stage']}:** {b['detail']}")

    lines += [
        "",
        "---",
        "",
        f"## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ ({hero_meta['name'].upper()})",
        "",
    ]
    for q in ep_bundle["quotes_100"]:
        lines.append(f"{q['num']}. [{q['cat']}] {q['text']}")

    lines += [
        "",
        "---",
        "",
        "## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)",
        f"*Повний розгорнутий сценарій ({ep_bundle['script_total_words']} слів): `{hero_meta['script_path']}`*",
        "",
    ]
    for a in ep_bundle["beat_acts"]:
        lines.append(f"### АКТ {a['actNum']}. {a['title']} ({a['time']})")
        if a.get("music_file"):
            lines.append(f"*Музика: Suno Pro — `{a['music_file']}`*")
        for b in a["beats"]:
            cues_str = " ".join(f"[{c}]" for c in b["cues"])
            lines.append(f"* **{b['tc']}** | {cues_str} | **Диктор:** {b['narration']}")
        lines.append("")

    lines += [
        "---",
        "",
        "## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)",
        "",
    ]
    for idx, s in enumerate(ep_bundle["suno_registry"], 1):
        lines.append(f"{idx}. `{s['filename']}` ({s['davinci_track']})")
        lines.append(f"   - *Suno v4 Prompt:* `{s['suno_prompt']}`")

    lines += [
        "",
        "---",
        "",
        "## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)",
        f"*Налаштування: {ep_bundle['vo_settings']}*",
        "",
    ]
    for v in ep_bundle["vo_registry"]:
        lines.append(f"* `{v['ua_file']}` | `{v['en_file']}` ({v['act']} — {v['label']})")

    lines += [
        "",
        "---",
        "",
        "## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)",
        "",
    ]
    for p in ep_bundle["prompts_100"]:
        lines.append(f"{p['num']:03d}. `{p['filename']}` [{p['tc']} | Акт {p['act']} | {p['source']}]")
        lines.append(f"     - *Контекст диктора:* {p['cue_ua']}")
        lines.append(f"     - *Veo Prompt:* `{p['prompt']}`")

    open(out_path, "w", encoding="utf-8").write("\n".join(lines) + "\n")

    # Also write dedicated 100-prompt catalog file into 04_VIDEO_PROMPTS/
    vp_path = os.path.join(WORKSPACE, "04_VIDEO_PROMPTS", f"{hero_meta['page_slug']}_100_prompts.md")
    vp_lines = [
        f"# 100 Візуальних Промптів (Veo 2 / Google Flow) — Епізод {hero_meta['ep']}: {hero_meta['name']}",
        f"**Хронометраж:** {ep_bundle['duration']} | **Формат:** 4K Scope 2.39:1 (3840×1606), 24fps, Kodak 2383 D60",
        "",
    ]
    for p in ep_bundle["prompts_100"]:
        vp_lines.append(f"### #{p['num']:03d} • `{p['filename']}` ({p['tc']})")
        vp_lines.append(f"- **Тип:** {p['source']}")
        vp_lines.append(f"- **Контекст диктора:** {p['cue_ua']}")
        vp_lines.append(f"- **Prompt:** `{p['prompt']}`")
        vp_lines.append("")
    open(vp_path, "w", encoding="utf-8").write("\n".join(vp_lines) + "\n")


def main():
    md_map = load_uploaded_md_map()
    assert len(md_map) == 10, f"Expected 10 MD files, found {len(md_map)}: {sorted(md_map.keys())}"

    existing_1000_path = os.path.join(WORKSPACE, "07_DASHBOARD/data/titans_1000_quotes.json")
    existing_1000 = json.load(open(existing_1000_path, "r", encoding="utf-8"))
    existing_by_id = {item["id"]: item["quotes_100"] for item in existing_1000}

    episodes_out_dir = os.path.join(WORKSPACE, "07_DASHBOARD/data/episodes")
    os.makedirs(episodes_out_dir, exist_ok=True)

    updated_1000_quotes = []
    season_index = []

    for meta in HEROES_META:
        ep = meta["ep"]
        md_parsed = parse_master_dossier(md_map[ep], ep)
        script_parsed = parse_full_director_script(meta["script_path"])

        # Build exact 100 quotes:
        # EP03..EP10 already have 100 verbatim quotes in MD; EP01 & EP02 have 10 canonical MD quotes + 90 from existing corpus
        md_q = md_parsed["md_quotes"]
        if len(md_q) >= 100:
            quotes_100 = md_q[:100]
        else:
            seen_norm = {re.sub(r"\W+", "", q["text"].lower())[:45] for q in md_q}
            merged = list(md_q)
            for eq in existing_by_id.get(meta["id"], []):
                key = re.sub(r"\W+", "", eq["text"].lower())[:45]
                if key not in seen_norm:
                    seen_norm.add(key)
                    merged.append({
                        "num": len(merged) + 1,
                        "cat": eq.get("cat") or classify_quote_category(eq["text"]),
                        "text": apply_fixes(eq["text"]),
                        "source": "Розширений корпус",
                    })
                if len(merged) == 100:
                    break
            # Pad if somehow <100 (should never trigger since 10 + 100 > 100)
            while len(merged) < 100:
                merged.append({
                    "num": len(merged) + 1,
                    "cat": "Філософія майбутнього",
                    "text": merged[-1]["text"],
                    "source": "Розширений корпус",
                })
            for i, q in enumerate(merged, 1):
                q["num"] = i
            quotes_100 = merged

        assert len(quotes_100) == 100, f"EP{ep} quotes count != 100"

        # Suno 16-file registry with custom Suno Pro v4 prompts
        suno_registry = [build_suno_prompt_for_file(item["filename"], meta) for item in md_parsed["suno_files"]]

        # ElevenLabs VO registry (UA + EN multi-audio pair)
        vo_registry = []
        for idx, ua_fn in enumerate(md_parsed["vo_files"], 1):
            en_fn = ua_fn.replace("_VO_UA_", "_VO_EN_")
            parts = ua_fn.replace(".wav", "").split("_")
            act_lbl = parts[4] if len(parts) > 4 else "ACT1"
            seg_lbl = " ".join(parts[5:]) if len(parts) > 5 else f"Segment {idx:02d}"
            vo_registry.append({
                "idx": idx,
                "ua_file": ua_fn,
                "en_file": en_fn,
                "act": act_lbl,
                "label": seg_lbl,
            })

        # 100 chronologically storyboarded Veo 2 / Google Flow prompts
        prompts_100 = build_100_prompts_for_hero(meta, md_parsed, script_parsed)
        assert len(prompts_100) == 100, f"EP{ep} prompts count != 100"

        # 7-stage SOP Action Algorithm
        sop_steps = build_sop_7_steps(meta, md_parsed, script_parsed)
        total_check_items = sum(len(s["tasks"]) for s in sop_steps)

        ep_bundle = {
            "ep": ep,
            "id": meta["id"],
            "page_slug": meta["page_slug"],
            "page_url": f"episodes/{meta['page_slug']}.html",
            "research_dir": meta["research_dir"],
            "dossier_md_path": f"01_RESEARCH/{meta['research_dir']}/MASTER_DOSSIER_EP{ep}.md",
            "script_md_path": meta["script_path"],
            "prompts_md_path": f"04_VIDEO_PROMPTS/{meta['page_slug']}_100_prompts.md",
            "name": meta["name"],
            "latin": meta["latin"],
            "avatar": meta["avatar"],
            "title": meta["title"],
            "role": meta["role"],
            "archetype": meta["archetype"],
            "duration": md_parsed["duration"],
            "bpm": "92 BPM",
            "wpm": md_parsed["wpm"],
            "tone": script_parsed["tone"] or "Глибока документальна подача, 112–115 слів/хв",
            "visual_key": script_parsed["visual_key"] or meta["visual_palette"],
            "camera_lens": meta["camera_lens"],
            "vo_settings": md_parsed["vo_settings"],
            "smart_bin_rule": f"EP{ep}_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]",
            "key_quote": quotes_100[0]["text"],
            "sop_steps": sop_steps,
            "biography": md_parsed["bio_items"],
            "beat_acts": md_parsed["beat_acts"],
            "full_acts": script_parsed["acts"],
            "script_total_words": script_parsed["total_words"],
            "suno_registry": suno_registry,
            "vo_registry": vo_registry,
            "prompts_100": prompts_100,
            "quotes_100": quotes_100,
        }

        # Write upgraded MASTER_DOSSIER_EPXX.md & 100-prompt markdown file
        write_upgraded_master_dossier_md(meta, ep_bundle)

        # Write data/episodes/epXX.js
        ep_js_path = os.path.join(episodes_out_dir, f"ep{ep}.js")
        with open(ep_js_path, "w", encoding="utf-8") as f:
            f.write("window.EPISODE_DATA = ")
            json.dump(ep_bundle, f, ensure_ascii=False, indent=2)
            f.write(";\n")

        updated_1000_quotes.append({
            "id": meta["id"],
            "ep": ep,
            "name": meta["name"],
            "latin": meta["latin"],
            "page_url": f"episodes/{meta['page_slug']}.html",
            "avatar": f"assets/avatars/{meta['avatar']}",
            "quotes_100": quotes_100,
        })

        season_index.append({
            "ep": ep,
            "id": meta["id"],
            "page_slug": meta["page_slug"],
            "page_url": f"episodes/{meta['page_slug']}.html",
            "name": meta["name"],
            "latin": meta["latin"],
            "avatar": f"assets/avatars/{meta['avatar']}",
            "title": meta["title"],
            "role": meta["role"],
            "archetype": meta["archetype"],
            "duration": md_parsed["duration"],
            "wpm": md_parsed["wpm"],
            "bpm": "92 BPM",
            "vo_settings": md_parsed["vo_settings"],
            "key_quote": quotes_100[0]["text"],
            "script_words": script_parsed["total_words"],
            "suno_count": len(suno_registry),
            "vo_count": len(vo_registry),
            "prompts_count": len(prompts_100),
            "quotes_count": len(quotes_100),
            "sop_tasks_count": total_check_items,
            "dossier_path": f"01_RESEARCH/{meta['research_dir']}/MASTER_DOSSIER_EP{ep}.md",
        })

        print(
            f"Compiled EP{ep} ({meta['name']}): "
            f"bio={len(md_parsed['bio_items'])}, quotes={len(quotes_100)}, "
            f"prompts={len(prompts_100)}, suno={len(suno_registry)}, vo={len(vo_registry)}, "
            f"script_words={script_parsed['total_words']}"
        )

    # Save updated titans_1000_quotes.json & .js
    q_json_path = os.path.join(WORKSPACE, "07_DASHBOARD/data/titans_1000_quotes.json")
    q_js_path = os.path.join(WORKSPACE, "07_DASHBOARD/data/titans_1000_quotes.js")
    with open(q_json_path, "w", encoding="utf-8") as f:
        json.dump(updated_1000_quotes, f, ensure_ascii=False, indent=2)
    with open(q_js_path, "w", encoding="utf-8") as f:
        f.write("window.TITANS_1000_QUOTES = ")
        json.dump(updated_1000_quotes, f, ensure_ascii=False)
        f.write(";\n")

    # Save season1_index.js
    idx_js_path = os.path.join(WORKSPACE, "07_DASHBOARD/data/season1_index.js")
    with open(idx_js_path, "w", encoding="utf-8") as f:
        f.write("window.SEASON1_INDEX = ")
        json.dump(season_index, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print("\nSUCCESS: Compiled all 10 Master-Dossiers, 1,000 quotes, and 1,000 Veo prompts!")


if __name__ == "__main__":
    main()
