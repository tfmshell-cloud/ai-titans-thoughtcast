#!/usr/bin/env python3
"""
Render EP09 Yoshua Bengio 4K documentary assets:
- 5 new 4K Dossier plates (EP09_DOC_02..06) + web JPG/MP4 previews (+ verify DOC_01)
- 8 Ukrainian 4K animated quote cards + PNG stills + 720p JPG / 480p MP4 web previews
- 18 Ken Burns 4K archival clips from 05_RAW_FOOTAGE/speaker_portraits/young_bengio/
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
YOUNG_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_bengio"
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
        "id": "EP09_DOC_02",
        "raw_png": "EP09_DOC_02_ACT1_paris_mcgill_bell_labs_montreal_1993.png",
        "master_mp4": "EP09_DOC_02_ACT1_paris_mcgill_bell_labs_montreal_1993.mp4",
        "web_jpg": "ep09_doc_02_paris_mcgill_bell_labs.jpg",
        "accent": "#38bdf8",
        "kicker": "EP09 // ACT I: PARIS 1964 -> MCGILL PHD 1991 -> BELL LABS -> MONTRÉAL (1964–1993)",
        "stamp": "NO SELLOUT // MONTRÉAL",
        "headline": "Театр батька в Парижі, союз у Bell Labs та повернення до Університету Монреаля",
        "meta": [
            ("ПАРИЖ 1964 • СЕФАРДСЬКЕ КОРІННЯ", "Батько Карло (аптекар → драматург) і мати Селія (художниця й активістка)"),
            ("МОНРЕАЛЬ • КНИГИ АЗІМОВА", "Переїзд у 12 років; брат Самі; захоплення «Фундацією» Айзека Азімова"),
            ("MCGILL PHD 1991 • MIT • BELL LABS", "Союз бунтарів-нейробіологів: Хінтон, Лекун та Бенжіо у Нью-Джерсі"),
            ("ВИБІР 1993 РОКУ", "Відмова від американських перегонів — повернення у тихий франкомовний УдМ"),
        ],
        "paragraphs": [
            "У богемній паризькій квартирі мірилом успіху були не гроші, а глибина думки й захист слабких. У Монреалі брати Йошуа та Самі Бенжіо шукали відповідь на питання: як із простих правил народжується розум.",
            "Після дисертації в Макгіллі та досліджень у MIT і AT&T Bell Labs поряд із Яном Лекуном Бенжіо обрав незалежність рідного Монреаля.",
        ],
        "quote": "“I have chosen to stay in university, to work for the public good, to guide the next generation, and to remain free to speak the truth.”",
        "highlight_span": "remain free to speak the truth",
        "footnote": "ARCHIVE: UNIVERSITÉ DE MONTRÉAL & MCGILL BIOGRAPHICAL CHRONICLE (1964–1993)",
    },
    {
        "id": "EP09_DOC_03",
        "raw_png": "EP09_DOC_03_ACT2_word_embeddings_2000_ai_winter_open_lab.png",
        "master_mp4": "EP09_DOC_03_ACT2_word_embeddings_2000_ai_winter_open_lab.mp4",
        "web_jpg": "ep09_doc_03_ai_winter_word_vectors.jpg",
        "accent": "#fbbf24",
        "kicker": "EP09 // ACT II: 20-YEAR AI WINTER -> NEURAL PROBABILISTIC LANGUAGE MODEL (2000–2003)",
        "stamp": "WORD EMBEDDINGS 2000",
        "headline": "20 років зими ШІ та «геометрія слів»: як слово стало координатою смислу",
        "meta": [
            ("ЛАБОРАТОРІЯ БЕЗ ТАЄМНИЦЬ", "Під час «зими ШІ» учні ділилися кодом і нотатками за одним дерев'яним столом"),
            ("ПРОКЛЯТТЯ РОЗМІРНОСТІ", "Класичні n-грами не бачили подібності між словами «кіт» і «собака»"),
            ("НЕЙРОННА МОВНА МОДЕЛЬ (2000)", "Bengio, Ducharme, Vincent, Janvin — розподілені вектори слів у космосі"),
            ("ТИХА РЕВОЛЮЦІЯ NLP", "Проігнорована в 2000-му стаття через 15 років стала фундаментом усіх LLM"),
        ],
        "paragraphs": [
            "Коли фінансування нейромереж в Америці згасло, скромна підвальна група в Монреалі вистояла на ентузіазмі й братній взаємодопомозі без корпоративної конкуренції.",
            "У роботі «A Neural Probabilistic Language Model» (NIPS 2000 / JMLR 2003) Бенжіо перетворив дискретні символи на неперервні геометричні вектори — пращури сучасного word embedding.",
        ],
        "quote": "“By learning a distributed vector representation for each word in semantic space, the neural model breaks the curse of dimensionality forever.”",
        "highlight_span": "distributed vector representation",
        "footnote": "ARCHIVE: NIPS 2000 / JMLR 2003 // HLF TURING AWARD LECTURE",
    },
    {
        "id": "EP09_DOC_04",
        "raw_png": "EP09_DOC_04_ACT2_attention_2014_gan_mila_refusing_billions.png",
        "master_mp4": "EP09_DOC_04_ACT2_attention_2014_gan_mila_refusing_billions.mp4",
        "web_jpg": "ep09_doc_04_attention_gan_mila_2014.jpg",
        "accent": "#a78bfa",
        "kicker": "EP09 // ACT II: ATTENTION MECHANISM (2014) -> MILA 1,000 RESEARCHERS -> TURING 2018",
        "stamp": "MILA & ATTENTION 2014",
        "headline": "Механізм Уваги (2014), GAN після пабу, відмова від мільярдів та інститут Mila",
        "meta": [
            ("БОГДАНОВ • ЧО • БЕНЖІО (2014)", "Soft Alignment долає «вузьке горло» перекладу — прямий предок Transformer"),
            ("ЯН ГУДФЕЛЛОУ (GAN 2014)", "Народження генеративно-змагальних мереж у монреальській лабораторії Бенжіо"),
            ("ВІДМОВА «Я НЕ ПРОДАЮСЯ»", "Корпоративні чеки на десятки мільйонів відхилено заради свободи совісті"),
            ("ІНСТИТУТ MILA • ТЮРІНГ 2018", "1000+ вільних дослідників (клімат, антибіотики); Нобель інформатики 2018"),
        ],
        "paragraphs": [
            "Рекурентні мережі намагалися стиснути цілу книгу в один вузький вектор. Разом із Дмитром Богдановим та Кюнхьоном Чо Бенжіо навчив модель «повертати погляд назад» — фокусуючи промені Attention на потрібних словах.",
            "Замість переїзду до корпорацій він збудував у кварталі Міле-Екс найбільший незалежний інститут ШІ планети — Mila.",
        ],
        "quote": "“If I took your tens of millions, I would no longer belong to humanity — I would belong to your shareholders. Someone must stay free.”",
        "highlight_span": "no longer belong to humanity",
        "footnote": "ARCHIVE: ICLR 2015 (ARXIV 1409.0473) // MILA MONTRÉAL // ACM TURING 2018",
    },
    {
        "id": "EP09_DOC_05",
        "raw_png": "EP09_DOC_05_ACT3_un_ai_safety_report_system2_gflownets.png",
        "master_mp4": "EP09_DOC_05_ACT3_un_ai_safety_report_system2_gflownets.mp4",
        "web_jpg": "ep09_doc_05_system2_gflownets_un_report.jpg",
        "accent": "#f43f5e",
        "kicker": "EP09 // ACT III: GPT-4 & GRANDSON -> UN AI SAFETY REPORT -> SYSTEM 2 & SCIENTIST AI",
        "stamp": "UN SAFETY // SYSTEM 2",
        "headline": "Бунт сумління 2023: Міжнародний звіт безпеки ООН, GFlowNets і ШІ-Вчений",
        "meta": [
            ("ВЕСНА 2023 • ОЧІ ОНУКА", "Поява GPT-4 і тривога за майбутнє онука: звернення в Сенаті США та ООН"),
            ("ЗВІТ БЕЗПЕКИ (30+ КРАЇН)", "Голова першого International Scientific Report on Advanced AI Safety"),
            ("СИСТЕМА 1 VS СИСТЕМА 2", "Заміна галюцинаційного потоку асоціацій на причинне міркування Канемана"),
            ("GFLOWNETS & SCIENTIST AI", "Пошук ліків без егоїстичної волі самозбереження та з математичним смиренням"),
        ],
        "paragraphs": [
            "Через відсутність корпоративних конфліктів інтересів уряди 30+ країн та ООН обрали саме Бенжіо головою незалежного Міжнародного наукового звіту про екзистенційні ризики передового ШІ.",
            "Математична відповідь Монреаля — GFlowNets та «ШІ-Вчений» (Scientist AI): система без власної агенції, що зважує невизначеність і зупиняється перед ризиком.",
        ],
        "quote": "“We must stop rushing to build unchecked autonomous agents seeking self-preservation, and build Scientist AI anchored in epistemic humility.”",
        "highlight_span": "epistemic humility",
        "footnote": "ARCHIVE: US SENATE JUDICIARY 2023 // INTERNATIONAL AI SAFETY REPORT 2025 // GFLOWNETS",
    },
    {
        "id": "EP09_DOC_06",
        "raw_png": "EP09_DOC_06_ACT4_montreal_declaration_conscience_compass.png",
        "master_mp4": "EP09_DOC_06_ACT4_montreal_declaration_conscience_compass.mp4",
        "web_jpg": "ep09_doc_06_montreal_declaration_compass.jpg",
        "accent": "#34d399",
        "kicker": "EP09 // ACT IV: MONTREAL DECLARATION (2018) -> GUARDIAN CODE ON SNOWY ROADS",
        "stamp": "MONTREAL DECLARATION",
        "headline": "Монреальська декларація та Кодекс Вільної Людини: велосипедом крізь сніги Квебеку",
        "meta": [
            ("ДЕКЛАРАЦІЯ ВІДПОВІДАЛЬНОСТІ", "Заборона на автономне позбавлення життя й приховування машинної природи"),
            ("ПЕРШИЙ ВЧЕНиЙ ГОЛОВНИЙ", "Найцитованіший науковець на Google Scholar їздить на старому велосипеді"),
            ("ТРИ ЗАПОВІДІ БЕНЖІО", "1. Бережіть незалежність • 2. Керуйте Attention • 3. Живіть за Системою 2"),
            ("ГОЛОВНА ТЕЗА ФІНАЛУ", "Наука без гуманізму — лише холодне креслення машини в порожнечі"),
        ],
        "paragraphs": [
            "Ще у 2018 році Бенжіо об'єднав філософів, лікарів, громадян і програмістів Монреаля, викарбувавши демократичний етичний щит задовго до світових самітів безпеки.",
            "Дорогою додому крізь зимовий сніг Квебеку лауреат Тюрінга залишається вірним урокам батька з паризької квартири: чиста совість дорожча за всі опціони світу.",
        ],
        "quote": "“Science without humanism is merely the cold blueprint of a machine in an empty void. We endure only as long as guardians keep their compass of conscience.”",
        "highlight_span": "compass of conscience",
        "footnote": "ARCHIVE: MONTRÉAL DECLARATION FOR RESPONSIBLE AI (2018) // EP09 FINALE",
    },
]

# Fix accidental lowercase character in bullet title above before rendering
DOSSIERS_SPEC[4]["meta"][1] = ("ПЕРШИЙ ВЧЕНИЙ ГОЛОВНИЙ", "Найцитованіший науковець на Google Scholar їздить на старому велосипеді")

EP09_CARDS = [
    ("ep09_ua_clip_card_01_bicycle_moral_bastion_10s.png", "ep09_ua_clip_card_01_bicycle_moral_bastion_10s.mp4", 10.0,
     "АКТ I • ВСТУП • КВЕБЕЦЬКИЙ СНІГ",
     "«ХТОСЬ ІЗ НАС ПОВИНЕН ЗАЛИШИТИСЯ ВІЛЬНИМ,\nЩОБ ЗБЕРЕГТИ ОСТАННІЙ БАСТІОН НАУКИ»",
     "— Йошуа Бенжіо: старий велосипед проти мільйонних опціонів", (56, 189, 248), 52),
    ("ep09_ua_clip_card_02_paris_theatre_asimov_10s.png", "ep09_ua_clip_card_02_paris_theatre_asimov_10s.mp4", 10.0,
     "АКТ I • ПАРИЖ 1964 → МОНРЕАЛЬ",
     "«У ЇХНЬОМУ ДОМІ МІРИЛОМ УСПІХУ БУЛА\nГЛИБИНА ДУМКИ І ТЕ, ЧИ ЗАХИЩАЄШ СЛАБКИХ»",
     "— Родина Карло й Селії Бенжіо, читання «Фундації» Азімова", (251, 191, 36), 52),
    ("ep09_ua_clip_card_03_ai_winter_family_lab_10s.png", "ep09_ua_clip_card_03_ai_winter_family_lab_10s.mp4", 10.0,
     "АКТ I • 20 РОКІВ ЗИМИ ШІ (1993–2012)",
     "«ЖОДНОЇ БОРОТЬБИ МІЖ УЧНЯМИ, ЖОДНИХ ТАЄМНИЦЬ —\nУСІ ДІЛЯТЬСЯ ІДЕЯМИ З УСІМА, ЯК РОДИНА»",
     "— Франкомовний Університет Монреаля як фортеця відкритої науки", (52, 211, 153), 50),
    ("ep09_ua_clip_card_04_word_embeddings_cosmos_10s.png", "ep09_ua_clip_card_04_word_embeddings_cosmos_10s.mp4", 10.0,
     "АКТ II • WORD EMBEDDINGS (2000)",
     "«СЛОВО ПЕРЕСТАЛО БУТИ МЕРТВОЮ ФІШКОЮ —\nСЛОВО СТАЛО КООРДИНАТОЮ ЧИСТОГО СМИСЛУ»",
     "— Neural Probabilistic Language Model: подолання прокляття розмірності", (56, 189, 248), 52),
    ("ep09_ua_clip_card_05_attention_2014_goodfellow_10s.png", "ep09_ua_clip_card_05_attention_2014_goodfellow_10s.mp4", 10.0,
     "АКТ II • ATTENTION (2014) & GAN",
     "«ЛЮДИНА ПОСТІЙНО ПОВЕРТАЄ ПОГЛЯД НАЗАД —\nТАК НАРОДИВСЯ МЕХАНІЗМ УВАГИ (ATTENTION)»",
     "— Богданов, Чо й Бенжіо (2014) — фундамент усіх сучасних Transformer-ів", (167, 139, 250), 50),
    ("ep09_ua_clip_card_06_not_for_sale_mila_10s.png", "ep09_ua_clip_card_06_not_for_sale_mila_10s.mp4", 10.0,
     "АКТ II • ІНСТИТУТ MILA • ВІДМОВА",
     "«ДЯКУЮ, АЛЕ Я НЕ ПРОДАЮСЯ. ХТОСЬ МАЄ\nМАТИ ПРАВО СКАЗАТИ ПРАВДУ АКЦІОНЕРАМ»",
     "— Заснування Mila (1000+ вільних учених: клімат, ліки, права людини)", (251, 191, 36), 52),
    ("ep09_ua_clip_card_07_grandson_scientist_ai_12s.png", "ep09_ua_clip_card_07_grandson_scientist_ai_12s.mp4", 12.0,
     "АКТ III • ЗВІТ ООН & SCIENTIST AI",
     "«ШІ-ВЧЕНИЙ (СИСТЕМА 2 І GFLOWNETS) ТОЧНО ЗНАЄ\nМЕЖУ НЕЗНАННЯ І ЗУПИНЯЄТЬСЯ ПЕРЕД РИЗИКОМ»",
     "— Бунт сумління після GPT-4 заради майбутнього онука", (244, 63, 94), 50),
    ("ep09_ua_clip_card_08_conscience_compass_finale_12s.png", "ep09_ua_clip_card_08_conscience_compass_finale_12s.mp4", 12.0,
     "АКТ IV • МОНРЕАЛЬСЬКА ДЕКЛАРАЦІЯ",
     "«НАУКА БЕЗ ГУМАНІЗМУ — ХОЛОДНЕ КРЕСЛЕННЯ;\nМИ ВСТОЇМО, ДОКИ Є ВАРТОВІ СОВІСТІ»",
     "— Фінальний кодекс Йошуа Бенжіо під північним сяйвом Квебеку", (52, 211, 153), 52),
]

PHOTO_STILL_CLIPS = [
    ("ep09_img_arch_01_paris_latin_quarter_1978_roots.jpg", "ep09_clip_still_paris_latin_quarter_6s.mp4", 6.0),
    ("ep09_img_arch_02_paris_theatre_father_carlo_stage.jpg", "ep09_clip_still_paris_theatre_carlo_6s.mp4", 6.0),
    ("ep09_img_arch_03_isaac_asimov_foundation_youth.jpg", "ep09_clip_still_isaac_asimov_books_6s.mp4", 6.0),
    ("ep09_img_arch_04_mcgill_university_arts_phd_1991.jpg", "ep09_clip_still_mcgill_arts_phd_6s.mp4", 6.0),
    ("ep09_img_arch_05_att_bell_labs_holmdel_lecun_pact.jpg", "ep09_clip_still_bell_labs_holmdel_6s.mp4", 6.0),
    ("ep09_img_arch_06_universite_de_montreal_roger_gaudry_1993.jpg", "ep09_clip_still_udem_roger_gaudry_6s.mp4", 6.0),
    ("ep09_img_arch_07_montreal_mount_royal_winter_skyline.jpg", "ep09_clip_still_montreal_winter_skyline_6s.mp4", 6.0),
    ("ep09_img_arch_08_word_embeddings_math_blackboard_2000.jpg", "ep09_clip_still_word_embeddings_board_6s.mp4", 6.0),
    ("ep09_img_arch_09_attention_mechanism_encoder_cross_2014.jpg", "ep09_clip_still_attention_mechanism_6s.mp4", 6.0),
    ("ep09_img_arch_10_montreal_boulevard_saint_laurent_mila.jpg", "ep09_clip_still_saint_laurent_mila_6s.mp4", 6.0),
    ("ep09_img_arch_11_yoshua_bengio_open_science_portrait.jpg", "ep09_clip_still_bengio_open_science_6s.mp4", 6.0),
    ("ep09_img_arch_12_gflownet_molecular_drug_discovery.jpg", "ep09_clip_still_gflownet_molecules_6s.mp4", 6.0),
    ("ep09_img_arch_13_yoshua_bengio_iclr_keynote_stage.jpg", "ep09_clip_still_bengio_iclr_stage_6s.mp4", 6.0),
    ("ep09_img_arch_14_us_capitol_senate_judiciary_2023.jpg", "ep09_clip_still_us_capitol_senate_6s.mp4", 6.0),
    ("ep09_img_arch_15_bletchley_park_ai_safety_summit_2023.jpg", "ep09_clip_still_bletchley_summit_6s.mp4", 6.0),
    ("ep09_img_arch_16_un_security_council_global_governance.jpg", "ep09_clip_still_un_security_council_6s.mp4", 6.0),
    ("ep09_img_arch_17_quebec_winter_bicycle_conscience.jpg", "ep09_clip_still_winter_bicycle_quebec_6s.mp4", 6.0),
    ("ep09_img_arch_18_canada_aurora_borealis_moral_shield.jpg", "ep09_clip_still_canada_aurora_finale_6s.mp4", 6.0),
]


def render_dossiers():
    print("=== [1/3] Rendering 5 EP09 4K Documentary Dossiers + Web Previews + Master MP4 ===", flush=True)
    doc1 = DOSSIER_DIR / "EP09_DOC_01_ACT2_Bengio_Attention_Bahdanau_2014.png"
    if doc1.exists() and (not (WEB_DOS_VID / "EP09_DOC_01.mp4").exists() or not (WEB_DOS_PREVIEW / "ep09_doc_01_bengio_attention.jpg").exists()):
        make_web_jpg_and_mp4(doc1, WEB_DOS_PREVIEW / "ep09_doc_01_bengio_attention.jpg", WEB_DOS_VID / "EP09_DOC_01.mp4", 5.0)

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
    print("\n=== [2/3] Rendering 8 EP09 4K Ukrainian Quote Cards + Web Previews ===", flush=True)
    rendered_pngs = []
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP09_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP09: YOSHUA BENGIO",
        ))
        rendered_pngs.append(png_path)
        mp4_path = OUT_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)

        stem = Path(mp4_name).stem
        make_web_jpg_and_mp4(png_path, WEB_CARD_PREVIEW / f"{stem}.jpg", WEB_CARD_VID / mp4_name, dur=5.0)
        print(f"  [OK] {mp4_name} ({dur}s • {mp4_path.stat().st_size//1024}KB)", flush=True)
    return rendered_pngs


def render_photo_stills():
    print("\n=== [3/3] Rendering 18 Ken Burns 4K Archival Motion Clips for EP09 ===", flush=True)
    for img_name, mp4_name, dur in PHOTO_STILL_CLIPS:
        src = YOUNG_DIR / img_name
        out_mp4 = OUT_4K_DIR / mp4_name
        assert src.exists(), f"Missing {src}"
        render_4k_still_video(src, out_mp4, dur, zoom_drift=0.05)
        print(f"  [OK] {out_mp4.name} ({out_mp4.stat().st_size//1024}KB)", flush=True)


def render_contact_sheet(card_pngs):
    plates = [DOSSIER_DIR / "EP09_DOC_01_ACT2_Bengio_Attention_Bahdanau_2014.png"] + [DOSSIER_DIR / d["raw_png"] for d in DOSSIERS_SPEC] + card_pngs
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
    out = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/ep09_dossiers_and_cards_sheet.jpg")
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
    print("=== EP09 4K ASSETS RENDERING COMPLETE ===")
