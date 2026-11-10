#!/usr/bin/env python3
"""
Render EP10 Andrew Ng 4K documentary assets:
- 5 new 4K Dossier plates (EP10_DOC_02..06) + web JPG/MP4 previews (+ verify DOC_01)
- 8 Ukrainian 4K animated quote cards + PNG stills + 720p JPG / 480p MP4 web previews
- 18 Ken Burns 4K archival clips from 05_RAW_FOOTAGE/speaker_portraits/young_andrew/
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
from render_ep08_dossiers_and_cards import make_web_jpg_and_mp4

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
DOSSIER_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
YOUNG_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_andrew"
OUT_4K_DIR = ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k"
SCRATCH_HTML = ROOT / "08_AUTOMATION" / "scratch"

WEB_DOS_PREVIEW = ROOT / "07_DASHBOARD" / "assets" / "dossiers_preview"
WEB_DOS_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "dossiers"
WEB_CARD_PREVIEW = ROOT / "07_DASHBOARD" / "assets" / "cards_preview"
WEB_CARD_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "cards"

for d in (DOSSIER_DIR, OUT_4K_DIR, SCRATCH_HTML, WEB_DOS_PREVIEW, WEB_DOS_VID, WEB_CARD_PREVIEW, WEB_CARD_VID):
    d.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DOSSIERS_SPEC = [
    {
        "id": "EP10_DOC_02",
        "raw_png": "EP10_DOC_02_ACT1_hong_kong_singapore_raffles_basic_1984.png",
        "master_mp4": "EP10_DOC_02_ACT1_hong_kong_singapore_raffles_basic_1984.mp4",
        "web_jpg": "ep10_doc_02_singapore_helicopter_rl.jpg",
        "accent": "#38bdf8",
        "kicker": "EP10 // ACT I: HONG KONG & RAFFLES SINGAPORE -> CMU -> STANFORD HELICOPTERS (1984–2008)",
        "stamp": "RAFFLES TO STANFORD",
        "headline": "Журнали BASIC у Сінгапурі та перевернутий автономний гелікоптер у Стенфорді",
        "meta": [
            ("РОДИНА • БАТЬКО-ГЕМАТОЛОГ", "Рональд Ин писав діагностичні дерева для легень; син вивчав логіку умов"),
            ("RAFFLES INSTITUTION", "Передруковував лістинги BASIC з журналів — кожна кома навчала точності"),
            ("CMU • MIT • UC BERKELEY PHD", "Потрійний диплом CMU, магістратура MIT, PhD у Майкла Джордана (2002)"),
            ("ПРОЄКТ STAIR & ГЕЛІКОПТЕР", "Навчання з підкріпленням (RL): інвертований політ за метр над травою"),
        ],
        "paragraphs": [
            "У бібліотеці Сінгапуру десятирічний Ендрю мріяв про день, коли машини навчатимуться самі й звільнять людей від рутини. У 26 років він став наймолодшим професором Стенфорду.",
            "Навчивши нестабільний гелікоптер виконувати вищий пілотаж догори дриґом через RL і запустивши проєкт STAIR із молодим Семом Альтманом, Ин зрозумів: вирішальний прорив дасть масштаб мозку.",
        ],
        "quote": "“Growing up in Singapore reading printed BASIC code magazines, I dreamed of the day machines could learn autonomously to free humanity from drudgery.”",
        "highlight_span": "learn autonomously",
        "footnote": "ARCHIVE: STANFORD AUTONOMOUS HELICOPTER LAB & STAIR (2002–2008)",
    },
    {
        "id": "EP10_DOC_03",
        "raw_png": "EP10_DOC_03_ACT2_google_brain_16000_cores_cat_neuron_2012.png",
        "master_mp4": "EP10_DOC_03_ACT2_google_brain_16000_cores_cat_neuron_2012.mp4",
        "web_jpg": "ep10_doc_03_google_brain_16k_cat.jpg",
        "accent": "#fbbf24",
        "kicker": "EP10 // ACT II: GOOGLE X & JEFF DEAN -> 16,000 CPU CORES -> THE CAT NEURON (2011–2012)",
        "stamp": "16,000 CORES // CAT",
        "headline": "Шістнадцять тисяч ядер Google Brain: машина, що сама відкрила обличчя кота",
        "meta": [
            ("GOOGLE X • 2011 РІК", "Союз Ендрю Ина та Джеффа Діна — заснування лабораторії Google Brain"),
            ("1,000 СЕРВЕРІВ (16 000 ЯДЕР)", "Без спеціалізованих GPU — єдиний гігантський мозок на мільярд параметрів"),
            ("10 МІЛЬЙОНІВ КАДРІВ YOUTUBE", "Сім діб абсолютно неконтрольованого навчання без жодної мітки"),
            ("ПЕРША ШПАЛЬТА NYT (2012)", "Нейрон у верхньому шарі сам реконструював обличчя кота зі статистики"),
        ],
        "paragraphs": [
            "Переконавшись після розмов із Хінтоном та Суцкевером у силі глибокого масштабу, Ин і Дін підключили новонароджений кластер до випадкового потоку YouTube, не підказуючи жодного слова.",
            "Поява «нейрона кота» довела всьому світові: достатньо велика нейронна мережа здатна видобувати фундаментальні поняття реальності самостійно.",
        ],
        "quote": "“Google Brain proved that the unlabeled physical world is overflowing with latent structure, and a deep network of sufficient scale can discover meaning by itself.”",
        "highlight_span": "discover meaning by itself",
        "footnote": "ARCHIVE: LE, RANZATO, MONGA, DEVIN, CHEN, CORRADO, DEAN & NG (ICML 2012)",
    },
    {
        "id": "EP10_DOC_04",
        "raw_png": "EP10_DOC_04_ACT3_cs229_webcam_104k_coursera_baidu_2014.png",
        "master_mp4": "EP10_DOC_04_ACT3_cs229_webcam_104k_coursera_baidu_2014.mp4",
        "web_jpg": "ep10_doc_04_coursera_104k_students.jpg",
        "accent": "#34d399",
        "kicker": "EP10 // ACT III: STANFORD WEBCAM -> 104,000 STUDENTS -> COURSERA & BAIDU (2011–2017)",
        "stamp": "104,000 STUDENTS",
        "headline": "Вебкамера у Пало-Альто: як один курс перетворив 250 років аудиторії на одне літо",
        "meta": [
            ("АУДИТОРІЯ VS ПЛАНЕТА", "400 місць у Стенфорді проти мільйонів талантів у Києві, Лагосі, Індії"),
            ("104 000 СЛУХАЧІВ (2011)", "Одне літо з маркером і планшетом = чверть тисячоліття очних лекцій"),
            ("COURSERA & DEEPLEARNING.AI", "Засновано з Дафною Коллер; 8+ мільйонів студентів у світі"),
            ("BAIDU SVAIL (2014–2017)", "Керівництво 1,300 дослідниками: Deep Speech і прориви в голосі та авто"),
        ],
        "paragraphs": [
            "У момент золотого полювання корпорацій Ин не замкнувся за парканом секретності — він увімкнув вебкамеру в спальні й пояснив складну математику простою людською мовою.",
            "Слова «Не хвилюйтеся, якщо ви не одразу розумієте цю формулу» відчинили двері у нову технологічну епоху для цілого покоління інженерів світу.",
        ],
        "quote": "“I never cared about building an exclusive club of geniuses — I wanted to take the elite wall around Stanford down and put modern AI tools into millions of hands.”",
        "highlight_span": "into millions of hands",
        "footnote": "ARCHIVE: STANFORD CS229 // COURSERA ARCHIVE // DEEPLEARNING.AI",
    },
    {
        "id": "EP10_DOC_05",
        "raw_png": "EP10_DOC_05_ACT3_ai_is_the_new_electricity_data_centric_2021.png",
        "master_mp4": "EP10_DOC_05_ACT3_ai_is_the_new_electricity_data_centric_2021.mp4",
        "web_jpg": "ep10_doc_05_new_electricity_data_centric.jpg",
        "accent": "#f43f5e",
        "kicker": "EP10 // ACT III–IV: AI IS THE NEW ELECTRICITY -> DATA-CENTRIC AI & LANDING AI (2017–2023)",
        "stamp": "THE NEW ELECTRICITY",
        "headline": "ШІ — нова електрика і маніфест Data-Centric AI: чиста крапля проти океану шуму",
        "meta": [
            ("МАНІФЕСТ «НОВА ЕЛЕКТРИКА»", "Як 100 років тому електрика змінила заводи й ферми, так ШІ змінює все"),
            ("ПРОБЛЕМА РЕАЛЬНИХ ЗАВОДІВ", "У цеху чи клініці немає мільярда фото — є лише 50 дефектних деталей"),
            ("ПОВОРОТ DATA-CENTRIC AI", "Зафіксувати код моделі та ретельно вичистити якість самих даних"),
            ("LANDING AI & AI FUND (2018+)", "Венчурна студія практичних застосувань у медицині, агро й індустрії"),
        ],
        "paragraphs": [
            "Поки медіа сперечалися про сценарії апокаліпсису, «головний електрик» епохи шукав, як протягнути надійний кабель ШІ в лікарню, на ферму та сталеливарний завод.",
            "Проголосивши рух Data-Centric AI, Ендрю Ин навчив індустрію: п'ятдесят бездоганно маркованих прикладів на виробництві сильніші за гігабайти брудного коду.",
        ],
        "quote": "“AI is the new electricity. Stop endlessly tweaking your neural network code — hold the model fixed and engineer your dataset with loving care.”",
        "highlight_span": "engineer your dataset with loving care",
        "footnote": "ARCHIVE: STANFORD GSB // DATA-CENTRIC AI & LANDING AI (2017–2023)",
    },
    {
        "id": "EP10_DOC_06",
        "raw_png": "EP10_DOC_06_ACT4_open_source_gutenberg_agentic_workflows_finale.png",
        "master_mp4": "EP10_DOC_06_ACT4_open_source_gutenberg_agentic_workflows_finale.mp4",
        "web_jpg": "ep10_doc_06_agentic_workflows_finale.jpg",
        "accent": "#a78bfa",
        "kicker": "EP10 // ACT IV: OPEN-SOURCE GUTENBERG -> AGENTIC WORKFLOWS -> SEASON 1 FINALE (2024–2026)",
        "stamp": "BUILD EVERY DAY",
        "headline": "Верстат Гутенберга, Agentic Workflows та фінал Сезону 1: десять рядків на світанку",
        "meta": [
            ("ЗАХИСТ ВІДКРИТОГО КОДУ", "Заборонити відкриті ваги моделей — це спалити друкарський верстат Гутенберга"),
            ("AGENTIC WORKFLOWS (2024)", "Мала відкрита модель у циклі саморефлексії перемагає монолітний промпт"),
            ("ФІНАЛ 10 ТИТАНІВ СЕЗОНУ 1", "Ендрю Ин замикає коло: прометеїв вогонь знань роздано в кожен дім"),
            ("КОДЕКС ЩОДЕННОГО ТВОРЦЯ", "Одна стаття + десять рядків коду на світанку цеглинка за цеглинкою"),
        ],
        "paragraphs": [
            "Разом із Яном Лекуном скромний професор у блакитній сорочці захистив право інженерів на відкриті моделі й довів силу ітеративної рефлексії в Agentic Workflows.",
            "Революція завершується не в секретних дата-центрах, а на світанку, коли звичайна людина без страху відкриває чистий файл і будує своє майбутнє власноруч.",
        ],
        "quote": "“Don't ask whether AI will replace you. Read one paper and write ten lines of code every dawn — brick by brick, until light fills every home on Earth.”",
        "highlight_span": "until light fills every home on Earth",
        "footnote": "ARCHIVE: SEQUOIA AI ASCENT 2024 // AI TITANS SEASON 1 FINALE",
    },
]

EP10_CARDS = [
    ("ep10_ua_clip_card_01_prometheus_blue_shirt_10s.png", "ep10_ua_clip_card_01_prometheus_blue_shirt_10s.mp4", 10.0,
     "АКТ I • ПРОЛОГ • ПРОМЕТЕЇВ ВОГОНЬ",
     "«ВІН ВІДЧИНИВ ВОРОТА СТЕНФОРДУ І РОЗДАВ\nВОГОНЬ ШІ ВОСЬМИ МІЛЬЙОНАМ ЛЮДЕЙ СВІТУ»",
     "— Професор у простій блакитній сорочці, що демократизував епоху", (56, 189, 248), 52),
    ("ep10_ua_clip_card_02_singapore_basic_doctor_10s.png", "ep10_ua_clip_card_02_singapore_basic_doctor_10s.mp4", 10.0,
     "АКТ I • ГОНКОНГ & RAFFLES СІНГАПУР",
     "«КОЖНА ПРОПУЩЕНА КОМА ЛАМАЛА ПРОГРАМУ —\nТАК ГАРТУВАЛАСЯ ХІРУРГІЧНА ТОЧНІСТЬ КОДУ»",
     "— Лістинги BASIC у бібліотеці Сінгапуру й медичний приклад батька", (56, 189, 248), 50),
    ("ep10_ua_clip_card_03_inverted_helicopter_scale_10s.png", "ep10_ua_clip_card_03_inverted_helicopter_scale_10s.mp4", 10.0,
     "АКТ I • СТЕНФОРД • RL ПІЛОТАЖ",
     "«АВТОНОМНИЙ ГЕЛІКОПТЕР ЗАВИСАЄ ГВИНТОМ УНИЗ:\nВУЗЬКЕ МІСЦЕ ШІ ЛЕЖИТЬ У МАСШТАБІ МОЗКУ»",
     "— Наймолодший професор Стенфорду та уроки проєкту STAIR", (251, 191, 36), 50),
    ("ep10_ua_clip_card_04_google_brain_cat_ghost_10s.png", "ep10_ua_clip_card_04_google_brain_cat_ghost_10s.mp4", 10.0,
     "АКТ II • GOOGLE BRAIN (2011–2012)",
     "«ШІСТНАДЦЯТЬ ТИСЯЧ ЯДЕР ДИВИЛИСЯ YOUTUBE —\nІ ЗІ СТАТИСТИКИ ПРОСТУПИВ ПРИВИД КОТА»",
     "— Ендрю Ин & Джефф Дін: перше відкриття поняття світу без вчителя", (251, 191, 36), 50),
    ("ep10_ua_clip_card_05_cs229_webcam_104k_10s.png", "ep10_ua_clip_card_05_cs229_webcam_104k_10s.mp4", 10.0,
     "АКТ III • COURSERA & CS229 (2011)",
     "«ВЕБКАМЕРА ЗА ОДНЕ ЛІТО НАВЧИЛА 104 000 ОСІБ —\nЯК ЗА ДВІСТІ П'ЯТДЕСЯТ РОКІВ У СТЕНФОРДІ»",
     "— «Не хвилюйтеся, якщо матрична похідна спершу здається складною»", (52, 211, 153), 50),
    ("ep10_ua_clip_card_06_ai_new_electricity_10s.png", "ep10_ua_clip_card_06_ai_new_electricity_10s.mp4", 10.0,
     "АКТ III • STANFORD GSB & BAIDU",
     "«ШТУЧНИЙ ІНТЕЛЕКТ — ЦЕ НОВА ЕЛЕКТРИКА,\nЩО ПЕРЕТВОРЮЄ КОЖНУ ГАЛУЗЬ ЦИВІЛІЗАЦІЇ»",
     "— Дати практичний рубильник лікарю, фермеру, вчителю й інженеру", (244, 63, 94), 52),
    ("ep10_ua_clip_card_07_data_centric_agentic_12s.png", "ep10_ua_clip_card_07_data_centric_agentic_12s.mp4", 12.0,
     "АКТ IV • DATA-CENTRIC & AGENTIC LOOPS",
     "«ЗАФІКСУЙТЕ МОДЕЛЬ І ВИЧИСТІТЬ ДАНІ —\nЧИСТА КРАПЛЯ ІСТИНИ СИЛЬНІША ЗА ОКЕАН ШУМУ»",
     "— Маніфест Data-Centric AI та цикл рефлексії Agentic Workflows", (167, 139, 250), 50),
    ("ep10_ua_clip_card_08_ten_lines_dawn_finale_12s.png", "ep10_ua_clip_card_08_ten_lines_dawn_finale_12s.mp4", 12.0,
     "ФІНАЛ СЕЗОНУ 1 • ЗАПОВІТ ЕНДРЮ ИНА",
     "«ПИШІТЬ ПО ДЕСЯТЬ РЯДКІВ КОДУ ЩОДНЯ —\nПОКИ В КОЖНОМУ ДОМІ НЕ СПАЛАХНЕ СВІТЛО»",
     "— Завершення циклу «Архітектори Розуму»: майбутнє збирають власноруч", (52, 211, 153), 52),
]

PHOTO_STILL_CLIPS = [
    ("ep10_img_arch_01_hong_kong_childhood_era.jpg", "ep10_clip_still_hong_kong_harbour_6s.mp4", 6.0),
    ("ep10_img_arch_02_raffles_institution_singapore.jpg", "ep10_clip_still_raffles_singapore_6s.mp4", 6.0),
    ("ep10_img_arch_03_apple_ii_basic_coding_youth.jpg", "ep10_clip_still_apple_ii_basic_6s.mp4", 6.0),
    ("ep10_img_arch_04_carnegie_mellon_bs_era.jpg", "ep10_clip_still_carnegie_mellon_6s.mp4", 6.0),
    ("ep10_img_arch_05_mit_killian_court_ms_era.jpg", "ep10_clip_still_mit_killian_court_6s.mp4", 6.0),
    ("ep10_img_arch_06_uc_berkeley_sather_tower_phd.jpg", "ep10_clip_still_uc_berkeley_sather_6s.mp4", 6.0),
    ("ep10_img_arch_07_stanford_university_professor_quad.jpg", "ep10_clip_still_stanford_quad_6s.mp4", 6.0),
    ("ep10_img_arch_08_inverted_rc_helicopter_rl_flight.jpg", "ep10_clip_still_inverted_helicopter_rl_6s.mp4", 6.0),
    ("ep10_img_arch_09_googleplex_mountain_view_google_brain.jpg", "ep10_clip_still_googleplex_google_brain_6s.mp4", 6.0),
    ("ep10_img_arch_10_google_brain_cat_neuron_2012.jpg", "ep10_clip_still_cat_neuron_2012_6s.mp4", 6.0),
    ("ep10_img_arch_11_coursera_mountain_view_hq.jpg", "ep10_clip_still_coursera_hq_6s.mp4", 6.0),
    ("ep10_img_arch_12_coursera_global_launch_era.jpg", "ep10_clip_still_coursera_launch_team_6s.mp4", 6.0),
    ("ep10_img_arch_13_baidu_shangdi_chief_scientist_hq.jpg", "ep10_clip_still_baidu_shangdi_hq_6s.mp4", 6.0),
    ("ep10_img_arch_14_andrew_ng_wsj_ai_electricity_keynote.jpg", "ep10_clip_still_andrew_ng_wsj_stage_6s.mp4", 6.0),
    ("ep10_img_arch_15_ai_is_the_new_electricity_bulb.jpg", "ep10_clip_still_new_electricity_filament_6s.mp4", 6.0),
    ("ep10_img_arch_16_landing_ai_precision_factory_vision.jpg", "ep10_clip_still_landing_ai_factory_6s.mp4", 6.0),
    ("ep10_img_arch_17_edison_grid_new_electricity_glow.jpg", "ep10_clip_still_edison_bulb_glow_6s.mp4", 6.0),
    ("ep10_img_arch_18_earth_dawn_global_builders_finale.jpg", "ep10_clip_still_earth_dawn_lights_finale_6s.mp4", 6.0),
]


def render_dossiers():
    print("=== [1/3] Rendering 5 EP10 4K Documentary Dossiers + Web Previews + Master MP4 ===", flush=True)
    doc1 = DOSSIER_DIR / "EP10_DOC_01_ACT2_AndrewNg_GoogleBrain_Coursera_2011.png"
    if doc1.exists() and (not (WEB_DOS_VID / "EP10_DOC_01.mp4").exists() or not (WEB_DOS_PREVIEW / "ep10_doc_01_andrewng_coursera.jpg").exists()):
        make_web_jpg_and_mp4(doc1, WEB_DOS_PREVIEW / "ep10_doc_01_andrewng_coursera.jpg", WEB_DOS_VID / "EP10_DOC_01.mp4", 5.0)

    for spec in DOSSIERS_SPEC:
        html_p = SCRATCH_HTML / f"{spec['id']}.html"
        html_p.write_text(build_dossier_html(spec), encoding="utf-8")
        raw_png = DOSSIER_DIR / spec["raw_png"]
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--window-size=3840,2160", "--force-device-scale-factor=1",
            f"--screenshot={raw_png}", html_p.as_uri(),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        html_p.unlink(missing_ok=True)

        make_web_jpg_and_mp4(raw_png, WEB_DOS_PREVIEW / spec["web_jpg"], WEB_DOS_VID / f"{spec['id']}.mp4", dur=5.0)
        master_mp4 = DOSSIER_DIR / spec["master_mp4"]
        render_4k_still_video(raw_png, master_mp4, 10.0, zoom_drift=0.05)
        print(f"  [OK] {spec['id']} png={raw_png.stat().st_size//1024}KB master={master_mp4.stat().st_size//1024}KB", flush=True)


def render_cards():
    print("\n=== [2/3] Rendering 8 EP10 4K Ukrainian Quote Cards + Web Previews ===", flush=True)
    rendered_pngs = []
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP10_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP10: ANDREW NG",
        ))
        rendered_pngs.append(png_path)
        mp4_path = OUT_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)

        stem = Path(mp4_name).stem
        make_web_jpg_and_mp4(png_path, WEB_CARD_PREVIEW / f"{stem}.jpg", WEB_CARD_VID / mp4_name, dur=5.0)
        print(f"  [OK] {mp4_name} ({dur}s • {mp4_path.stat().st_size//1024}KB)", flush=True)
    return rendered_pngs


def render_photo_stills():
    print("\n=== [3/3] Rendering 18 Ken Burns 4K Archival Motion Clips for EP10 ===", flush=True)
    for img_name, mp4_name, dur in PHOTO_STILL_CLIPS:
        src = YOUNG_DIR / img_name
        out_mp4 = OUT_4K_DIR / mp4_name
        assert src.exists(), f"Missing {src}"
        render_4k_still_video(src, out_mp4, dur, zoom_drift=0.05)
        print(f"  [OK] {out_mp4.name} ({out_mp4.stat().st_size//1024}KB)", flush=True)


def render_contact_sheet(card_pngs):
    plates = [DOSSIER_DIR / "EP10_DOC_01_ACT2_AndrewNg_GoogleBrain_Coursera_2011.png"] + [DOSSIER_DIR / d["raw_png"] for d in DOSSIERS_SPEC] + card_pngs
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
    out = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/ep10_dossiers_and_cards_sheet.jpg")
    sheet.save(out, "JPEG", quality=90)
    print("\nSaved dossiers/cards sheet:", out)


if __name__ == "__main__":
    render_dossiers()
    cards = render_cards()
    render_photo_stills()
    render_contact_sheet(cards)
    try:
        SCRATCH_HTML.rmdir()
    except OSError:
        pass
    print("=== EP10 4K ASSETS RENDERING COMPLETE ===")
