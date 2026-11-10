#!/usr/bin/env python3
"""
Render EP08 Fei-Fei Li 4K documentary assets:
- 5 new 4K Dossier plates (EP08_DOC_02..06) + web JPG/MP4 previews (+ ensure DOC_01 previews)
- 8 Ukrainian 4K animated quote cards + PNG stills + 720p JPG / 480p MP4 web previews
- 18 Ken Burns 4K archival clips from 05_RAW_FOOTAGE/speaker_portraits/young_feifei/
- Contact sheet of all 14 rendered 4K plates (6 dossiers + 8 quote cards)
"""
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

from render_ukrainian_quote_cards import draw_quote_card
from render_ep03_dossiers_and_cards import build_dossier_html, render_4k_still_video

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
DOSSIER_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
YOUNG_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_feifei"
OUT_4K_DIR = ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k"
SCRATCH_HTML = ROOT / "08_AUTOMATION" / "scratch"

WEB_DOS_PREVIEW = ROOT / "07_DASHBOARD" / "assets" / "dossiers_preview"
WEB_DOS_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "dossiers"
WEB_CARD_PREVIEW = ROOT / "07_DASHBOARD" / "assets" / "cards_preview"
WEB_CARD_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "cards"

for d in (DOSSIER_DIR, OUT_4K_DIR, SCRATCH_HTML, WEB_DOS_PREVIEW, WEB_DOS_VID, WEB_CARD_PREVIEW, WEB_CARD_VID):
    d.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"

DOSSIERS_SPEC = [
    {
        "id": "EP08_DOC_02",
        "raw_png": "EP08_DOC_02_ACT1_chengdu_parsippany_ormont_cleaners_1992.png",
        "master_mp4": "EP08_DOC_02_ACT1_chengdu_parsippany_ormont_cleaners_1992.mp4",
        "web_jpg": "ep08_doc_02_ormont_double_life.jpg",
        "accent": "#fbbf24",
        "kicker": "EP08 // ACT I: CHENGDU -> PARSIPPANY NJ -> ORMONT CLEANERS (1992–1999)",
        "stamp": "$20 TO PRINCETON",
        "headline": "Шлях із $20 у кишені та подвійне життя у пральні Ormont Cleaners",
        "meta": [
            ("ЕМІГРАЦІЯ 1992", "З Ченду (Сичуань) до Нью-Джерсі у 16 років; чищення часнику по $2/год"),
            ("МІСТЕР САБАРСЕЛЛА", "Вчитель математики допоміг отримати майже повну стипендію у Прінстоні"),
            ("ПОНЕДІЛОК – П'ЯТНИЦЯ", "Фізичний корпус Прінстона: квантова механіка й відносна фізика"),
            ("ВИХІДНІ У ПРАЛЬНІ", "П'ятниця 16:00 -> недільна ніч біля прасувального преса Ormont Cleaners"),
        ],
        "paragraphs": [
            "Без знання англійської мови та з $20 родина інженерів із Китаю впала на соціальне дно: мати стояла за касою, батько лагодив старі камери, а Фей-Фей спала по чотири години, переводячи підручники словником.",
            "Щоб утримувати сім'ю й лікувати хворе серце матері, вони купили в борг збиткову хімчистку — чотири роки студентка Прінстона поєднувала вищу фізику з парою прасувального преса.",
        ],
        "quote": "“Between Monday and Friday I studied Einstein's relativity under gothic Princeton arches; Friday at 4 PM I boarded New Jersey Transit and ironed shirts until Sunday night.”",
        "highlight_span": "ironed shirts until Sunday night",
        "footnote": "ARCHIVE: THE WORLDS I SEE (2023) // PRINCETON UNIVERSITY ARCHIVE",
    },
    {
        "id": "EP08_DOC_03",
        "raw_png": "EP08_DOC_03_ACT1_princeton_caltech_neuro_vision_2005.png",
        "master_mp4": "EP08_DOC_03_ACT1_princeton_caltech_neuro_vision_2005.mp4",
        "web_jpg": "ep08_doc_03_caltech_mother_blessing.jpg",
        "accent": "#38bdf8",
        "kicker": "EP08 // ACT I: WALL STREET REFUSAL -> CALTECH NEUROSCIENCE PHD (1999–2005)",
        "stamp": "CALTECH PHD 2005",
        "headline": "Відмова Уолл-стріт і благословення матері: шлях до біології зору в Калтеху",
        "meta": [
            ("ДИПЛОМ З ВІДЗНАКОЮ (1999)", "Princeton BS in Physics — пропозиції інвестбанків Уолл-стріт"),
            ("РІШЕННЯ МАТЕРІ", "«Ми терпіли цю пральню не щоб ти продала мрію банкам. Іди в науку!»"),
            ("ДОКТОРАНТУРА КАЛТЕХ", "П'єтро Перона й Крістоф Кох — нейрофізика миттєвого розпізнавання сцен"),
            ("КЛЮЧОВА ЗАГАДКА", "Чому трирічна дитина бачить світ, а найпотужніші алгоритми — сліпі?"),
        ],
        "paragraphs": [
            "Велика зарплата інвестбанків могла миттєво закрити всі борги родини після Прінстона, але важкохвора мати взяла доньку за руки й наказала не зраджувати наукове покликання.",
            "У Калтеху під керівництвом П'єтро Перони та Крістофа Коха Фей-Фей Лі поєднала комп'ютерні науки з експериментальною нейробіологією зорової кори людини.",
        ],
        "quote": "“We did not cross an ocean and endure the steam of this laundry so you could sell your mind to a Wall Street bank. Go to Caltech and discover how we see.”",
        "highlight_span": "discover how we see",
        "footnote": "ARCHIVE: STANFORD SIEPR & CALTECH VISION LAB (1999–2005)",
    },
    {
        "id": "EP08_DOC_04",
        "raw_png": "EP08_DOC_04_ACT2_imagenet_14m_mturk_miami_boycott_2009.png",
        "master_mp4": "EP08_DOC_04_ACT2_imagenet_14m_mturk_miami_boycott_2009.mp4",
        "web_jpg": "ep08_doc_04_imagenet_mturk_2009.jpg",
        "accent": "#34d399",
        "kicker": "EP08 // ACT II: DATA-CENTRIC REBELLION -> WORDNET & 14M IMAGES (2006–2009)",
        "stamp": "14,197,122 IMAGES",
        "headline": "Бунт ImageNet: 14 мільйонів картинок проти відмов у грантах і скепсису",
        "meta": [
            ("АНАЛОГІЯ З КЕМБРІЄМ", "540 млн років тому око запустило Кембрійський вибух живих форм"),
            ("МЕХАНІЗМ AMAZON MTURK", "48 940+ краудворкерів зі 167 країн розмітили 22 000 категорій WordNet"),
            ("БОЙКОТ СНОБІВ", "NSF відхиляв гранти як «беззмістовне збирання картинок без новизни»"),
            ("МАЯМІ CVPR 2009", "Презентація ImageNet на паперовому стенді в кутку біля туалетів"),
        ],
        "paragraphs": [
            "Три десятиліття дослідники писали крихкі формули вусів кота чи коліс велосипеда, тренуючи моделі на тисячах знімків. Лі показала: алгоритм у темному підвалі ніколи не прозріє без досвіду, співмірного із зором дитини.",
            "Замість 19 років ручної праці аспірантів команда відкрила Amazon Mechanical Turk — але навіть готовий корпус на 14 мільйонів фотографій у 2009 році зустріли глухим неприйняттям на головній конференції.",
        ],
        "quote": "“You have been trying to cure the wrong disease for thirty years. No algorithm can learn in a dark room starved of real-world visual experience.”",
        "highlight_span": "cure the wrong disease for thirty years",
        "footnote": "ARCHIVE: CVPR 2009 MIAMI // DENG, DONG, SOCHER, LI, LI & FEI-FEI LI",
    },
    {
        "id": "EP08_DOC_05",
        "raw_png": "EP08_DOC_05_ACT3_alexnet_2012_hospital_hai_dignity_2019.png",
        "master_mp4": "EP08_DOC_05_ACT3_alexnet_2012_hospital_hai_dignity_2019.mp4",
        "web_jpg": "ep08_doc_05_alexnet_stanford_hai.jpg",
        "accent": "#a78bfa",
        "kicker": "EP08 // ACT III: ILSVRC 2012 BREAKTHROUGH -> STANFORD HAI & HEALTHCARE (2012–2019)",
        "stamp": "HUMAN-CENTERED AI",
        "headline": "Тріумф AlexNet 2012 у пологовій палаті та народження Stanford HAI",
        "meta": [
            ("ЖОВТЕНЬ 2012 • ФЛОРИДА", "Дзвінок студента у пологову палату: AlexNet Хінтона зламав бар'єр 15.3%"),
            ("STANFORD SAIL & GOOGLE", "Директорка Stanford AI Lab (2013) & Chief Scientist Google Cloud AI"),
            ("STANFORD HAI (2019)", "Інститут людиноцентричного ШІ + освітня фундація AI4ALL (2017)"),
            ("МЕДИЦИНА МИЛОСЕРДЯ", "Інфрачервоний моніторинг у лікарнях без фіксації облич пацієнтів"),
        ],
        "paragraphs": [
            "Коли жоден грантодавець не оцінив ImageNet, Лі заснувала щорічний чемпіонат ILSVRC. У 2012 році, тримаючи новонародженого сина Лео на руках, вона почула новину, що змінила світову історію обчислень.",
            "А після ночей біля лікарняного ліжка матері професорка повернула фокус технологій на гідність пацієнтів і лікарів — довівши, що в кожному алгоритмі першочерговою має залишатися людина.",
        ],
        "quote": "“Technology carries no independent values of its own. At the center of every frontier algorithm must always stand human dignity, care, and inclusion.”",
        "highlight_span": "always stand human dignity",
        "footnote": "ARCHIVE: ILSVRC 2012 // STANFORD HAI (2019) & NATURE AMBIENT INTELLIGENCE",
    },
    {
        "id": "EP08_DOC_06",
        "raw_png": "EP08_DOC_06_ACT4_world_labs_spatial_intelligence_2024_northstar.png",
        "master_mp4": "EP08_DOC_06_ACT4_world_labs_spatial_intelligence_2024_northstar.mp4",
        "web_jpg": "ep08_doc_06_world_labs_spatial_2024.jpg",
        "accent": "#f43f5e",
        "kicker": "EP08 // ACT IV: WORLD LABS 3D SPATIAL INTELLIGENCE & THE NORTH STAR (2024–2026)",
        "stamp": "SPATIAL INTELLIGENCE",
        "headline": "World Labs (2024): вихід із пласких пікселів у 3D-фізику та Полярна зірка",
        "meta": [
            ("WORLD LABS ($230M+)", "Стартап із Justin Johnson & Christoph Lassner для моделювання 3D-світів"),
            ("ПРОСТОРОВИЙ РОЗУМ", "Навчання ШІ геометрії, маси, гравітації, руху й причинності об'єктів"),
            ("МЕМУАРИ «THE WORLDS I SEE»", "Кодекс незламності та погляд дитини на запітнілому вікні пральні"),
            ("ТРИ ОПОРИ ХАРАКТЕРУ", "Броня важкого старту • Праця там, де заважає снобізм • Полярна зірка"),
        ],
        "paragraphs": [
            "Генеративні мовні моделі досі живуть у пласкому світі двовимірних токенів і не відчувають фізичного опору матерії. World Labs будує Large World Models (LWMs), які мислять об'ємом, простором і дією.",
            "Через 30 років після дешевої пральні в Парсіппані докторка Лі формулює головний урок титанів: найбільші наукові скарби лежать там, де інші не хочуть забруднити руки.",
        ],
        "quote": "“If seeing gave birth to intelligence half a billion years ago, then true spatial intelligence will allow machines to perceive, reason, and act gracefully in our three-dimensional world.”",
        "highlight_span": "perceive, reason, and act gracefully",
        "footnote": "ARCHIVE: TED 2024 // WORLD LABS MANIFESTO & THE WORLDS I SEE",
    },
]

EP08_CARDS = [
    ("ep08_ua_clip_card_01_cambrian_eye_540m_10s.png", "ep08_ua_clip_card_01_cambrian_eye_540m_10s.mp4", 10.0,
     "АКТ I • 540 МЛН РОКІВ ТОМУ",
     "«КЕМБРІЙСЬКИЙ ВИБУХ ПОЧАВСЯ З ПЕРШОЇ\nСВІТЛОЧУТЛИВОЇ ПЛЯМИ ЖИВОГО ОКА»",
     "— Фей-Фей Лі (TED 2015 — про народження біологічного зору)", (251, 191, 36), 54),
    ("ep08_ua_clip_card_02_ormont_double_life_10s.png", "ep08_ua_clip_card_02_ormont_double_life_10s.mp4", 10.0,
     "АКТ I • ПРІНСТОН ↔ ПРАЛЬНЯ (1995–1999)",
     "«ПОНЕДІЛОК–П'ЯТНИЦЯ — КВАНТОВА ФІЗИКА;\nВИХІДНІ — ПАРА ORMONT CLEANERS»",
     "— Подвійне життя студентки з $20 на старті в Нью-Джерсі", (251, 191, 36), 52),
    ("ep08_ua_clip_card_03_mother_blessing_1999_10s.png", "ep08_ua_clip_card_03_mother_blessing_1999_10s.mp4", 10.0,
     "АКТ I • БЛАГОСЛОВЕННЯ МАТЕРІ (1999)",
     "«МИ ТЕРПІЛИ ЦЮ ПРАЛЬНЮ НЕ ЩОБ ТИ ПРОДАЛА\nМРІЮ БАНКАМ. ТВОЯ ГОЛОВА НАЛЕЖИТЬ НАУЦІ»",
     "— Відмова від мільйонів Уолл-стріт заради Калтеху", (56, 189, 248), 50),
    ("ep08_ua_clip_card_04_dark_basement_data_10s.png", "ep08_ua_clip_card_04_dark_basement_data_10s.mp4", 10.0,
     "АКТ II • ДІАГНОЗ 2006 РОКУ",
     "«ЖОДЕН АЛГОРИТМ НЕ ОЖИВЕ В ТЕМНОМУ\nПІДВАЛІ БЕЗ РЕАЛЬНОГО СВІТУ ДАНИХ»",
     "— Data-Centric революція проти 30 років сліпоти формул", (52, 211, 153), 52),
    ("ep08_ua_clip_card_05_imagenet_14m_miami_10s.png", "ep08_ua_clip_card_05_imagenet_14m_miami_10s.mp4", 10.0,
     "АКТ II • IMAGENET • CVPR 2009",
     "«П'ЯТДЕСЯТ ТИСЯЧ ЛЮДЕЙ ІЗ 167 КРАЇН ЗІБРАЛИ\n14 МІЛЬЙОНІВ ВІКОН У ВИДИМИЙ СВІТ»",
     "— Бунт проти відмов NSF і стенд біля туалетів у Маямі", (52, 211, 153), 52),
    ("ep08_ua_clip_card_06_maternity_ward_alexnet_10s.png", "ep08_ua_clip_card_06_maternity_ward_alexnet_10s.mp4", 10.0,
     "АКТ III • ПОЛОГОВА ПАЛАТА (ЖОВТЕНЬ 2012)",
     "«ТРИМАЮЧИ СИНА НА ГРУДЯХ, ВОНА ПОЧУЛА:\nALEXNET РОЗТРОЩИВ БАР'ЄР IMAGENET»",
     "— Мить початку Кембрійського вибуху глибокого навчання", (167, 139, 250), 52),
    ("ep08_ua_clip_card_07_hai_human_dignity_12s.png", "ep08_ua_clip_card_07_hai_human_dignity_12s.mp4", 12.0,
     "АКТ III • STANFORD HAI & ЛІКАРНЯ МАТЕРІ",
     "«У ЦЕНТРІ КОЖНОГО АЛГОРИТМУ ЗАВЖДИ\nМАЄ СТОЯТИ ГІДНІСТЬ ЖИВОЇ ЛЮДИНИ»",
     "— Маніфест Stanford HAI та інфрачервоний ШІ-охоронець лікарень", (167, 139, 250), 52),
    ("ep08_ua_clip_card_08_spatial_north_star_finale_12s.png", "ep08_ua_clip_card_08_spatial_north_star_finale_12s.mp4", 12.0,
     "ЕПІЛОГ • WORLD LABS & ПОЛЯРНА ЗІРКА",
     "«НАЙБІЛЬШИЙ СКАРБ ЛЕЖИТЬ ТАМ, ДЕ СНОБІЗМ\nЗАВАЖАЄ ІНШИМ ЗАБРУДНИТИ РУКИ»",
     "— World Labs Spatial Intelligence (3D) & «Світи, які я бачу»", (244, 63, 94), 52),
]

PHOTO_STILL_CLIPS = [
    ("ep08_img_arch_01_chengdu_sichuan_heritage_street.jpg", "ep08_clip_still_chengdu_heritage_6s.mp4", 6.0),
    ("ep08_img_arch_02_father_repaired_35mm_camera_lens.jpg", "ep08_clip_still_father_camera_lens_6s.mp4", 6.0),
    ("ep08_img_arch_03_english_chinese_study_dictionary.jpg", "ep08_clip_still_english_chinese_dict_6s.mp4", 6.0),
    ("ep08_img_arch_04_immigrant_laundry_pressing_steam_silhouette.jpg", "ep08_clip_still_laundry_silhouette_6s.mp4", 6.0),
    ("ep08_img_arch_05_ormont_cleaners_heavy_iron_press.jpg", "ep08_clip_still_ormont_iron_press_6s.mp4", 6.0),
    ("ep08_img_arch_06_princeton_nassau_hall_dusk_physics.jpg", "ep08_clip_still_princeton_nassau_6s.mp4", 6.0),
    ("ep08_img_arch_07_wall_street_nyse_rejected_offers.jpg", "ep08_clip_still_wall_street_nyse_6s.mp4", 6.0),
    ("ep08_img_arch_08_caltech_beckman_institute_pasadena.jpg", "ep08_clip_still_caltech_beckman_6s.mp4", 6.0),
    ("ep08_img_arch_09_cambrian_trilobite_evolution_eyes.jpg", "ep08_clip_still_cambrian_trilobite_6s.mp4", 6.0),
    ("ep08_img_arch_10_sleeping_cat_computer_vision_challenge.jpg", "ep08_clip_still_sleeping_cat_vision_6s.mp4", 6.0),
    ("ep08_img_arch_11_stanford_gates_cs_sail_building.jpg", "ep08_clip_still_stanford_gates_cs_6s.mp4", 6.0),
    ("ep08_img_arch_12_imagenet_alexnet_error_rate_crash.jpg", "ep08_clip_still_imagenet_curve_6s.mp4", 6.0),
    ("ep08_img_arch_13_googleplex_cloud_ai_2017.jpg", "ep08_clip_still_googleplex_cloud_2017_6s.mp4", 6.0),
    ("ep08_img_arch_14_feifei_li_ai_for_good_2017_keynote.jpg", "ep08_clip_still_feifei_aiforgood_2017_6s.mp4", 6.0),
    ("ep08_img_arch_15_stanford_hai_roundtable_feifei_li.jpg", "ep08_clip_still_stanford_hai_roundtable_6s.mp4", 6.0),
    ("ep08_img_arch_16_hospital_bedside_ambient_healthcare_ai.jpg", "ep08_clip_still_hospital_bedside_6s.mp4", 6.0),
    ("ep08_img_arch_17_feifei_li_global_humanitarian_award_2024.jpg", "ep08_clip_still_humanitarian_award_2024_6s.mp4", 6.0),
    ("ep08_img_arch_18_world_labs_3d_spatial_point_cloud.jpg", "ep08_clip_still_world_labs_3d_lidar_6s.mp4", 6.0),
]


def make_web_jpg_and_mp4(src_img: Path, out_jpg: Path, out_mp4: Path, dur: float = 5.0):
    with Image.open(src_img) as im:
        im = im.convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS)
        im.save(out_jpg, "JPEG", quality=86, optimize=True)
    frames = max(24, int(round(dur * 24.0)))
    subprocess.run([
        FFMPEG, "-y", "-v", "error", "-loop", "1", "-i", str(src_img),
        "-vf", f"scale=2560:1440,zoompan=z='min(zoom+0.0005,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1280x720:fps=24,format=yuv420p",
        "-t", f"{dur:.1f}", "-c:v", "libx264", "-preset", "fast", "-crf", "26", "-movflags", "+faststart",
        str(out_mp4),
    ], check=True)


def render_dossiers():
    print("=== [1/3] Rendering 5 EP08 4K Documentary Dossiers + Web Previews + Master MP4 ===", flush=True)
    doc1 = DOSSIER_DIR / "EP08_DOC_01_ACT2_FeiFeiLi_ImageNet_CVPR_2009.png"
    if doc1.exists() and not (WEB_DOS_VID / "EP08_DOC_01.mp4").exists():
        make_web_jpg_and_mp4(doc1, WEB_DOS_PREVIEW / "ep08_doc_01_feifeili_imagenet.jpg", WEB_DOS_VID / "EP08_DOC_01.mp4", 5.0)

    for spec in DOSSIERS_SPEC:
        html_p = SCRATCH_HTML / f"{spec['id']}.html"
        html_p.write_text(build_dossier_html(spec), encoding="utf-8")
        raw_png = DOSSIER_DIR / spec["raw_png"]
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--window-size=3840,2160", "--force-device-scale-factor=1",
            f"--screenshot={raw_png}", html_p.as_uri(),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        make_web_jpg_and_mp4(raw_png, WEB_DOS_PREVIEW / spec["web_jpg"], WEB_DOS_VID / f"{spec['id']}.mp4", dur=5.0)
        master_mp4 = DOSSIER_DIR / spec["master_mp4"]
        render_4k_still_video(raw_png, master_mp4, 10.0, zoom_drift=0.05)
        print(f"  [OK] {spec['id']} png={raw_png.stat().st_size//1024}KB master={master_mp4.stat().st_size//1024}KB", flush=True)


def render_cards():
    print("\n=== [2/3] Rendering 8 EP08 4K Ukrainian Quote Cards + Web Previews ===", flush=True)
    rendered_pngs = []
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP08_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP08: FEI-FEI LI",
        ))
        rendered_pngs.append(png_path)
        mp4_path = OUT_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)

        stem = Path(mp4_name).stem
        make_web_jpg_and_mp4(png_path, WEB_CARD_PREVIEW / f"{stem}.jpg", WEB_CARD_VID / mp4_name, dur=5.0)
        print(f"  [OK] {mp4_name} ({dur}s • {mp4_path.stat().st_size//1024}KB)", flush=True)
    return rendered_pngs


def render_photo_stills():
    print("\n=== [3/3] Rendering 18 Ken Burns 4K Archival Motion Clips for EP08 ===", flush=True)
    for img_name, mp4_name, dur in PHOTO_STILL_CLIPS:
        src = YOUNG_DIR / img_name
        out_mp4 = OUT_4K_DIR / mp4_name
        assert src.exists(), f"Missing {src}"
        render_4k_still_video(src, out_mp4, dur, zoom_drift=0.05)
        print(f"  [OK] {out_mp4.name} ({out_mp4.stat().st_size//1024}KB)", flush=True)


def render_contact_sheet(card_pngs):
    plates = [DOSSIER_DIR / "EP08_DOC_01_ACT2_FeiFeiLi_ImageNet_CVPR_2009.png"] + [DOSSIER_DIR / d["raw_png"] for d in DOSSIERS_SPEC] + card_pngs
    cols = 4
    rows = (len(plates) + cols - 1) // cols
    tw, th = 480, 290
    sheet = Image.new("RGB", (cols * tw, rows * th), (10, 15, 28))
    draw = ImageDraw.Draw(sheet)
    for idx, p in enumerate(plates):
        if not p.exists():
            continue
        r, c = divmod(idx, cols)
        im = Image.open(p).convert("RGB")
        im.thumbnail((tw - 14, th - 36))
        sheet.paste(im, (c * tw + (tw - im.width) // 2, r * th + 6))
        draw.text((c * tw + 10, r * th + th - 24), p.name[:44], fill=(248, 250, 252))
    out = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/ep08_dossiers_and_cards_sheet.jpg")
    sheet.save(out, "JPEG", quality=90)
    print("\nSaved dossiers/cards sheet:", out)


if __name__ == "__main__":
    render_dossiers()
    cards = render_cards()
    render_photo_stills()
    render_contact_sheet(cards)
    print("=== EP08 4K ASSETS RENDERING COMPLETE ===")
