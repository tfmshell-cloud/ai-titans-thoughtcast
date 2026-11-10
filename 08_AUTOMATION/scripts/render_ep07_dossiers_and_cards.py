#!/usr/bin/env python3
"""
Render EP07 Dario Amodei 4K documentary assets:
- 5 new 4K Dossier plates (EP07_DOC_02..06) + web JPG/MP4 previews (+ ensure DOC_01 previews)
- 8 Ukrainian 4K animated quote cards + PNG stills + 720p JPG / 480p MP4 web previews
- 18 Ken Burns 4K archival clips from 05_RAW_FOOTAGE/speaker_portraits/young_amodei/
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
YOUNG_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_amodei"
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
        "id": "EP07_DOC_02",
        "raw_png": "EP07_DOC_02_ACT1_sf_leather_princeton_retina_2011.png",
        "master_mp4": "EP07_DOC_02_ACT1_sf_leather_princeton_retina_2011.mp4",
        "web_jpg": "ep07_doc_02_princeton_retina.jpg",
        "accent": "#fbbf24",
        "kicker": "EP07 // ACT I: MISSION SF ➔ STANFORD ➔ PRINCETON BIOPHYSICS (1983–2011)",
        "stamp": "HERTZ FELLOW • PHD 2011",
        "headline": "Тусканська шкіра, втрата 2006 року та нейрофізика сітківки",
        "meta": [
            ("РОДИНА & УТРАТА", "Ріккардо Амодей (майстер шкіри), втрата 2006"),
            ("STANFORD PHYSICS (2006)", "BS in Physics — перехід із Caltech до Стенфорда"),
            ("PRINCETON PHD (2011)", "Network-Scale Electrophysiology of Neural Circuits"),
            ("БІОЛОГІЧНИЙ ІМПЕРАТИВ", "Розшифрування кодів сітківки заради перемоги над хворобами"),
        ],
        "paragraphs": [
            "Народжений 1983 року в Сан-Франциско в родині тосканського ремісника шкіри, Даріо Амодей пережив раптову хворобу й смерть батька у 2006 році — якраз у рік випуску зі Стенфорда.",
            "У Принстонському університеті він присвятив п'ять років експериментам із мультиелектродними матрицями на живій сітківці ссавців, вивчаючи, як групи нейронів кодують світло у статистично впорядкований сигнал.",
        ],
        "quote": "“Before trying to align silicon intelligence, I spent five years listening to living neurons inside the retina fire across multi-electrode arrays.”",
        "highlight_span": "living neurons inside the retina",
        "footnote": "ARCHIVE: PRINCETON UNIVERSITY PHD 2011 // STANFORD & OPENALEX BIOPHYSICS",
    },
    {
        "id": "EP07_DOC_03",
        "raw_png": "EP07_DOC_03_ACT2_scaling_laws_7orders_openai_2020.png",
        "master_mp4": "EP07_DOC_03_ACT2_scaling_laws_7orders_openai_2020.mp4",
        "web_jpg": "ep07_doc_03_scaling_laws_2020.jpg",
        "accent": "#38bdf8",
        "kicker": "EP07 // ACT II: BAIDU ➔ GOOGLE BRAIN ➔ OPENAI VP OF RESEARCH (2014–2020)",
        "stamp": "arXiv:2001.08361",
        "headline": "Закони масштабу (2020): Пряма лінія крізь сім порядків",
        "meta": [
            ("BAIDU & GOOGLE BRAIN", "Deep Speech 2 (2014) ➔ Concrete Problems in AI Safety (2016)"),
            ("OPENAI VP RESEARCH", "Кураторство GPT-2 та GPT-3 й формування RLHF-підходу"),
            ("ЗАКОН L(N, D, C)", "Точні степеневі криві втрат на 7 порядках обчислень"),
            ("ЗРУШЕННЯ ПАРАДИГМИ", "Глибоке навчання перетворюється на статистичну фізику розуму"),
        ],
        "paragraphs": [
            "Робота Каплана, МакКендліша та Амодея (січень 2020) показала, що втрата крос-ентропії мовних моделей падає не випадковими стрибками, а ідеально прямою лінією на логарифмічній шкалі впродовж семи порядків величини.",
            "Це відкриття дало Амодею математичну впевненість, що системи рівня AGI стануть реальністю у найближчі роки — і безпеку доведеться будувати до появи надпотужного інтелекту.",
        ],
        "quote": "“Intelligence obeys smooth empirical power laws: scale compute, dataset size, and parameters in harmony, and loss drops along a straight line across seven orders of magnitude.”",
        "highlight_span": "straight line across seven orders of magnitude",
        "footnote": "ARCHIVE: KAPLAN, MCCANDLISH, AMODEI ET AL. // OPENAI SCALING LAWS (2020)",
    },
    {
        "id": "EP07_DOC_04",
        "raw_png": "EP07_DOC_04_ACT2_silent_exit_anthropic_shannon_2021.png",
        "master_mp4": "EP07_DOC_04_ACT2_silent_exit_anthropic_shannon_2021.mp4",
        "web_jpg": "ep07_doc_04_anthropic_pbc_2021.jpg",
        "accent": "#a78bfa",
        "kicker": "EP07 // ACT II: SILENT EXODUS & ANTHROPIC PBC INCORPORATION (2020–2021)",
        "stamp": "CLAUDE SHANNON // PBC",
        "headline": "Тихий вихід сімох дослідників 2020: Народження Anthropic PBC",
        "meta": [
            ("ГРУДЕНЬ 2020", "Тихий вихід Даріо, Даніели Амодей і команди безпеки з OpenAI"),
            ("СІЧЕНЬ 2021", "Заснування Anthropic як Public Benefit Corporation (PBC)"),
            ("LONG-TERM BENEFIT TRUST", "Незалежна рада опіки з правом захисту місії понад прибутком"),
            ("ІМ'Я КЛОДА ШЕННОНА", "Назва моделі Claude як омаж творцю теорії інформації"),
        ],
        "paragraphs": [
            "Наприкінці 2020 року Даріо та його сестра Даніела Амодей разом із групою провідних інженерів залишили OpenAI без пресових скандалів через незгоду з темпами комерційних перегонів.",
            "Нову лабораторію зареєстрували як Public Benefit Corporation (PBC), щоб закласти безпеку в статут компанії, а власне сімейство моделей назвали Claude — на честь батька теорії інформації Клода Шеннона.",
        ],
        "quote": "“We didn't leave OpenAI to start a war in the headlines. We left so that racing for capability could never silently silence safety research.”",
        "highlight_span": "never silently silence safety research",
        "footnote": "ARCHIVE: ANTHROPIC PBC CHARTER // 500 HOWARD ST, SAN FRANCISCO (2021)",
    },
    {
        "id": "EP07_DOC_05",
        "raw_png": "EP07_DOC_05_ACT3_constitutional_ai_mech_interp_2024.png",
        "master_mp4": "EP07_DOC_05_ACT3_constitutional_ai_mech_interp_2024.mp4",
        "web_jpg": "ep07_doc_05_cai_interp_2024.jpg",
        "accent": "#34d399",
        "kicker": "EP07 // ACT III: RLAIF PRISM & TRANSFORMER CIRCUITS ATLAS (2022–2024)",
        "stamp": "SCALING MONOSEMANTICITY",
        "headline": "Конституційний ШІ та «МРТ» усередині чорної скриньки Claude 3",
        "meta": [
            ("CONSTITUTIONAL AI (2022)", "arXiv:2212.08073 — самокритика моделі через відкриті принципи"),
            ("МЕХАНІСТИЧНИЙ МІКРОСКОП", "Спільно з Крісом Ола — декомпозиція матриць Claude 3 Sonnet"),
            ("МІЛЬЙОНИ ОЗНАК", "Травень 2024: виділення інтерпретованих концептів із суперпозиції"),
            ("GOLDEN GATE CLAUDE", "Пряма локалізація та керування абстрактними концептами всередині ШІ"),
        ],
        "paragraphs": [
            "Конституційний ШІ (RLAIF) замінив сотні тисяч непрозорих людських заборон на прозорий перелік етичних принципів, із яким модель сама звіряє власні відповіді у циклі самокритики.",
            "У травні 2024 року команда Transformer Circuits вперше застосувала розріджені автоенкодери до великої продакшн-моделі Claude 3 Sonnet, перетворивши «чорну скриньку» на прозорий атлас нейробіології машин.",
        ],
        "quote": "“Mechanistic interpretability is building a microscope into the neurobiology of silicon minds — illuminating circuits for deception, sycophancy, and empathy before deployment.”",
        "highlight_span": "microscope into the neurobiology of silicon minds",
        "footnote": "ARCHIVE: arXiv:2212.08073 & TRANSFORMER-CIRCUITS.PUB (MAY 2024)",
    },
    {
        "id": "EP07_DOC_06",
        "raw_png": "EP07_DOC_06_ACT4_asl_biosecurity_machines_loving_grace.png",
        "master_mp4": "EP07_DOC_06_ACT4_asl_biosecurity_machines_loving_grace.mp4",
        "web_jpg": "ep07_doc_06_asl_loving_grace_2025.jpg",
        "accent": "#f43f5e",
        "kicker": "EP07 // ACT IV: SENATE CBRN TESTIMONY & MACHINES OF LOVING GRACE (2023–2026)",
        "stamp": "ASL-4 // +10X BIOLOGY",
        "headline": "Протоколи зупинки ASL-1..4 та «стиснене XXI століття»",
        "meta": [
            ("СЕНАТ США (25.07.2023)", "Свідчення про ризики біологічної зброї та потребу тестування"),
            ("ПОРОГИ ASL-1..ASL-4", "Захисні рівні за взірцем біолабораторій BSL-1..4 з правом стопу"),
            ("МАНІФЕСТ (10.2024)", "Machines of Loving Grace — 15,000 слів про гуманістичний ШІ"),
            ("МЕДИЧНИЙ ГОРИЗОНТ", "Стиснення 50–100 років біопрогресу в 5–10 років без хвороб"),
        ],
        "paragraphs": [
            "Політика відповідального масштабування (RSP) прирівняла сильні нейромережі до небезпечних біопатогенів: при наближенні до порогу автономного синтезу загроз (ASL-3/ASL-4) лабораторія зобов'язана зупинити навчання.",
            "А в жовтневому маніфесті «Машини благодаті» Даріо Амодей повертається до втрати свого батька 2006 року: справжня мета безпечного ШІ — подолати більшість інфекцій і вдвічі зменшити смертність від раку.",
        ],
        "quote": "“We can compress a century of biological and medical progress into five to ten years — eliminating most infectious diseases and cutting cancer deaths in half.”",
        "highlight_span": "compress a century of biological and medical progress",
        "footnote": "ARCHIVE: US SENATE JUDICIARY 2023 // MACHINES OF LOVING GRACE (OCT 2024)",
    },
]

EP07_CARDS = [
    ("ep07_ua_clip_card_01_leather_and_illness_10s.png", "ep07_ua_clip_card_01_leather_and_illness_10s.mp4", 10.0,
     "АКТ I • САН-ФРАНЦИСКО 1983–2006",
     "«СВІТ ТРИМАЄТЬСЯ НА РЕМЕСЛІ,\nТОЧНОСТІ Й КРИХКОМУ ТІЛІ»",
     "— Даріо Амодей (про батька Ріккардо і втрату 2006 року)", (251, 191, 36), 54),
    ("ep07_ua_clip_card_02_princeton_retina_2011_10s.png", "ep07_ua_clip_card_02_princeton_retina_2011_10s.mp4", 10.0,
     "АКТ I • ПРИНСТОН • БІОФІЗИКА (2011)",
     "«СІТКІВКА ОКА — ЦЕ ЖИВИЙ\nБІОЛОГІЧНИЙ КОМП'ЮТЕР»",
     "— Мультиелектродна електрофізіологія нейронних контурів зору", (56, 189, 248), 54),
    ("ep07_ua_clip_card_03_scaling_laws_line_10s.png", "ep07_ua_clip_card_03_scaling_laws_line_10s.mp4", 10.0,
     "АКТ II • ЗАКОНИ МАСШТАБУ (2020)",
     "«ІНТЕЛЕКТ ВИЯВИВСЯ ПРЯМОЮ\nЧЕРЕЗ СІМ ПОРЯДКІВ ВЕЛИЧИНИ»",
     "— Kaplan, McCandlish & Amodei (arXiv:2001.08361)", (56, 189, 248), 52),
    ("ep07_ua_clip_card_04_silent_exodus_anthropic_10s.png", "ep07_ua_clip_card_04_silent_exodus_anthropic_10s.mp4", 10.0,
     "АКТ II • ТИХИЙ ВИХІД 2020–2021",
     "«КОЛИ ПЕРЕГОНИ ВТРАЧАЮТЬ\nГАЛЬМА — ІДИ ТА БУДУЙ НАНОВО»",
     "— Заснування Anthropic PBC та спадок Клода Шеннона", (167, 139, 250), 52),
    ("ep07_ua_clip_card_05_claude_shannon_prism_10s.png", "ep07_ua_clip_card_05_claude_shannon_prism_10s.mp4", 10.0,
     "АКТ III • КОНСТИТУЦІЙНИЙ ШІ (RLAIF)",
     "«КОНСТИТУЦІЯ ШІ — ЦЕ ПРОЗОРА\nПРИЗМА, А НЕ СЛІПА ЦЕНЗУРА»",
     "— Самокритика моделі проти відкритого кодексу принципів", (52, 211, 153), 52),
    ("ep07_ua_clip_card_06_mech_interp_microscope_10s.png", "ep07_ua_clip_card_06_mech_interp_microscope_10s.mp4", 10.0,
     "АКТ III • МІКРОСКОП Claude 3 (2024)",
     "«ІНТЕРПРЕТОВАНІСТЬ — ЦЕ МРТ\nУСЕРЕДИНІ ЧОРНОЇ СКРИНЬКИ»",
     "— Scaling Monosemanticity & Golden Gate Claude (травень 2024)", (52, 211, 153), 52),
    ("ep07_ua_clip_card_07_asl_biosecurity_vow_12s.png", "ep07_ua_clip_card_07_asl_biosecurity_vow_12s.mp4", 12.0,
     "АКТ IV • ПРОТОКОЛИ ASL-1..ASL-4",
     "«НА ПОРОЗІ БІОЗАГРОЗИ ASL-4\nМИ ЗУПИНИМО НАВЧАННЯ МОДЕЛІ»",
     "— Свідчення Даріо Амодея у Сенаті США (25.07.2023)", (244, 63, 94), 52),
    ("ep07_ua_clip_card_08_loving_grace_finale_12s.png", "ep07_ua_clip_card_08_loving_grace_finale_12s.mp4", 12.0,
     "ЕПІЛОГ • «МАШИНИ БЛАГОДАТІ» (2024)",
     "«МИ СТИСНЕМО СТОЛІТТЯ БІОЛОГІЇ\nУ ДЕСЯТЬ РОКІВ ЗЦІЛЕННЯ»",
     "— Есе «Machines of Loving Grace» (жовтень 2024)", (251, 191, 36), 54),
]

PHOTO_STILL_CLIPS = [
    ("ep07_img_arch_01_san_francisco_victorian_childhood_era.jpg", "ep07_clip_still_sf_mission_era_6s.mp4", 6.0),
    ("ep07_img_arch_02_tuscan_leather_working_tools.jpg", "ep07_clip_still_tuscan_leather_tools_6s.mp4", 6.0),
    ("ep07_img_arch_03_stanford_university_physics_quad.jpg", "ep07_clip_still_stanford_quad_6s.mp4", 6.0),
    ("ep07_img_arch_04_princeton_carl_icahn_biophysics_lab.jpg", "ep07_clip_still_princeton_icahn_6s.mp4", 6.0),
    ("ep07_img_arch_05_princeton_jadwin_hall_physics.jpg", "ep07_clip_still_princeton_jadwin_6s.mp4", 6.0),
    ("ep07_img_arch_06_retinal_ganglion_neurons_microscopy.jpg", "ep07_clip_still_retinal_ganglion_6s.mp4", 6.0),
    ("ep07_img_arch_07_baidu_headquarters_shangdi.jpg", "ep07_clip_still_baidu_shangdi_6s.mp4", 6.0),
    ("ep07_img_arch_08_googleplex_building43_brain_era.jpg", "ep07_clip_still_googleplex43_6s.mp4", 6.0),
    ("ep07_img_arch_09_openai_pioneer_building_sf.jpg", "ep07_clip_still_openai_pioneer_6s.mp4", 6.0),
    ("ep07_img_arch_10_google_tpu_v3_scaling_laws_pod.jpg", "ep07_clip_still_tpu_v3_scaling_6s.mp4", 6.0),
    ("ep07_img_arch_11_claude_shannon_information_theory.jpg", "ep07_clip_still_claude_shannon_6s.mp4", 6.0),
    ("ep07_img_arch_12_anthropic_howard_street_sf_hq.jpg", "ep07_clip_still_anthropic_howard_6s.mp4", 6.0),
    ("ep07_img_arch_13_white_house_ai_ceo_summit_2023.jpg", "ep07_clip_still_white_house_2023_6s.mp4", 6.0),
    ("ep07_img_arch_14_downing_street_pm_ai_developers_2023.jpg", "ep07_clip_still_downing_street_2023_6s.mp4", 6.0),
    ("ep07_img_arch_15_dario_amodei_techcrunch_disrupt_2023_portrait.jpg", "ep07_clip_still_amodei_disrupt_2023_6s.mp4", 6.0),
    ("ep07_img_arch_16_dario_amodei_tokyo_ai_diplomacy_2025.jpg", "ep07_clip_still_amodei_tokyo_2025_6s.mp4", 6.0),
    ("ep07_img_arch_17_bsl4_containment_asl_protocol.jpg", "ep07_clip_still_bsl4_containment_6s.mp4", 6.0),
    ("ep07_img_arch_18_cancer_dna_fluorescence_loving_grace.jpg", "ep07_clip_still_cancer_fluorescence_6s.mp4", 6.0),
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
    print("=== [1/3] Rendering 5 EP07 4K Documentary Dossiers + Web Previews + Master MP4 ===", flush=True)
    doc1 = DOSSIER_DIR / "EP07_DOC_01_ACT3_Amodei_Constitutional_AI_2022.png"
    if doc1.exists() and not (WEB_DOS_VID / "EP07_DOC_01.mp4").exists():
        make_web_jpg_and_mp4(doc1, WEB_DOS_PREVIEW / "ep07_doc_01_amodei_cai.jpg", WEB_DOS_VID / "EP07_DOC_01.mp4", 5.0)

    for spec in DOSSIERS_SPEC:
        html_p = SCRATCH_HTML / f"{spec['id']}.html"
        html_p.write_text(build_dossier_html(spec), encoding="utf-8")
        raw_png = DOSSIER_DIR / spec["raw_png"]
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--window-size=3840,2160", "--force-device-scale-factor=1",
            f"--screenshot={raw_png}", html_p.as_uri(),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        web_jpg = WEB_DOS_PREVIEW / spec["web_jpg"]
        web_mp4 = WEB_DOS_VID / f"{spec['id']}.mp4"
        make_web_jpg_and_mp4(raw_png, web_jpg, web_mp4, dur=5.0)

        master_mp4 = DOSSIER_DIR / spec["master_mp4"]
        render_4k_still_video(raw_png, master_mp4, 10.0, zoom_drift=0.05)
        print(f"  [OK] {spec['id']} png={raw_png.stat().st_size//1024}KB master={master_mp4.stat().st_size//1024}KB", flush=True)


def render_cards():
    print("\n=== [2/3] Rendering 8 EP07 4K Ukrainian Quote Cards + Web Previews ===", flush=True)
    rendered_pngs = []
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP07_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP07: DARIO AMODEI",
        ))
        rendered_pngs.append(png_path)
        mp4_path = OUT_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)

        stem = Path(mp4_name).stem
        make_web_jpg_and_mp4(png_path, WEB_CARD_PREVIEW / f"{stem}.jpg", WEB_CARD_VID / mp4_name, dur=5.0)
        print(f"  [OK] {mp4_name} ({dur}s • {mp4_path.stat().st_size//1024}KB)", flush=True)
    return rendered_pngs


def render_photo_stills():
    print("\n=== [3/3] Rendering 18 Ken Burns 4K Archival Motion Clips for EP07 ===", flush=True)
    for img_name, mp4_name, dur in PHOTO_STILL_CLIPS:
        src = YOUNG_DIR / img_name
        dst = OUT_4K_DIR / mp4_name
        assert src.exists(), f"Missing {src}"
        render_4k_still_video(src, dst, dur, zoom_drift=0.05)
        print(f"  [OK] {mp4_name} ({dst.stat().st_size//1024}KB)", flush=True)


def render_contact_sheet(card_pngs):
    plates = [DOSSIER_DIR / "EP07_DOC_01_ACT3_Amodei_Constitutional_AI_2022.png"] + [DOSSIER_DIR / d["raw_png"] for d in DOSSIERS_SPEC] + card_pngs
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
    out = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/ep07_dossiers_and_cards_sheet.jpg")
    sheet.save(out, "JPEG", quality=90)
    print("\nSaved dossiers/cards sheet:", out)


if __name__ == "__main__":
    render_dossiers()
    cards = render_cards()
    render_photo_stills()
    render_contact_sheet(cards)
    print("=== EP07 4K ASSETS RENDERING COMPLETE ===")
