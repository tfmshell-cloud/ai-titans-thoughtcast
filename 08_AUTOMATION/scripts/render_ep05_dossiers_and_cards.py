#!/usr/bin/env python3
"""
Renders EP05 (Yann LeCun) complete broadcast plates:
  - Ensures web preview & zoom MP4 for existing EP05_DOC_01 (LeNet-5 IEEE 1998)
  - 5 new 4K Documentary Dossiers (EP05_DOC_02..06) + 720p web JPEG & zoom MP4 + 10s masters
  - 8 4K Ukrainian Quote Cards (EP05_UA_CARD_01..08) + 24fps H.264 MP4 clips
  - 18 Ken Burns 4K motion clips (EP05_CLIP_STILL_*) from verified Wikimedia archives
Reuses shared 4K Chrome plate builder and Ken Burns ffmpeg helper from render_ep03_dossiers_and_cards.
"""
import subprocess
from pathlib import Path
from PIL import Image
from render_ukrainian_quote_cards import draw_quote_card
from render_ep03_dossiers_and_cards import build_dossier_html, render_4k_still_video

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"

DOSS_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
WEB_DOSS_IMG = ROOT / "07_DASHBOARD" / "assets" / "dossiers_preview"
WEB_DOSS_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "dossiers"
STILLS_4K_DIR = ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k"
YOUNG_LECUN_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_lecun"
SCRATCH_HTML = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/scratch/ep05_dossiers_html")

for d in [DOSS_DIR, WEB_DOSS_IMG, WEB_DOSS_VID, STILLS_4K_DIR, SCRATCH_HTML]:
    d.mkdir(parents=True, exist_ok=True)


DOSSIERS_SPEC = [
    {
        "id": "EP05_DOC_02",
        "raw_png": "EP05_DOC_02_ACT1_Paris_Electronics_ESIEE_Piaget_1974.png",
        "web_jpg": "ep05_doc_02_paris_esiee_piaget_1974.jpg",
        "master_mp4": "EP05_DOC_02_Paris_ESIEE_10s.mp4",
        "accent": "#F5B941",
        "stamp": "ORIGINS // 1960–1983",
        "kicker": "BIOGRAPHICAL DOSSIER // SOISY-SOUS-MONTMORENCY & ESIEE PARIS ARCHIVES (1974–1983)",
        "headline": "Paris Soldered Circuits, ESIEE Acid Etching & The Piaget vs. Chomsky Spark",
        "meta": [
            ("CHILDHOOD BENCH", "Born July 8, 1960 Near Paris • Father Georges Was an Aerospace Engineer"),
            ("FIRST SPARK (1975)", "Discovered Royaumont Abbey Debate Between Jean Piaget and Noam Chomsky"),
            ("ESIEE PARIS (1983)", "Diplome d'Ingenieur • Built DIY Microcomputer Boards in Ferric Chloride"),
            ("COGNITIVE BET", "Rejected Hard-Coded Grammar -> Chose Constructivist Self-Learning Vision"),
        ],
        "paragraphs": [
            "TAUGHT BY MATTER BEFORE CODE: Growing up around his father's gliders, aluminum tools, and vintage Tektronix oscilloscopes, teenage Yann learned first-hand that physical intelligence lives in geometry and perception—not static symbol tables.",
            "PIAGET OVER CHOMSKY: While classical AI tried to pre-program human knowledge like dictionary grammar, LeCun sided with Jean Piaget's insight that minds build internal models of the world directly through interaction.",
        ],
        "quote": "“Jean Piaget argued intelligence constructs itself incrementally through observation and physical interaction with the world—that single debate convinced me machines had to learn perception from scratch.”",
        "highlight_span": "intelligence constructs itself incrementally through observation",
        "footnote": "VERIFIED BIOGRAPHICAL RECORD // EP05 THOUGHTCAST // PARIS – ESIEE ARCHIVE (1960–1983)",
    },
    {
        "id": "EP05_DOC_03",
        "raw_png": "EP05_DOC_03_ACT2_Sorbonne_Backprop_Minsky_1987.png",
        "web_jpg": "ep05_doc_03_sorbonne_minsky_1987.jpg",
        "master_mp4": "EP05_DOC_03_Sorbonne_BellLabs_10s.mp4",
        "accent": "#38BDF8",
        "stamp": "PHD 1987 // HOLMDEL 1988",
        "kicker": "UNIVERSITE PIERRE ET MARIE CURIE (PARIS PHD 1987) -> AT&T BELL LABS HOLMDEL (1988)",
        "headline": "Pencil in a Paris Cellar: Re-Deriving Minsky (1969) & Modeling Cat Cortex",
        "meta": [
            ("SORBONNE PHD (1987)", "Supervised by Maurice Milgram • Independent Early Backpropagation Formulation"),
            ("TORONTO POSTDOC", "Invited by Geoffrey Hinton (1987) After Re-Checking Perceptrons With Pencil"),
            ("BELL LABS HOLMDEL", "Joined Larry Jackel's Adaptive Systems Dept (1988) in Saarinen Mirror Lab"),
            ("NEURAL INSPIRATION", "Translated Hubel & Wiesel Simple/Complex Cat V1 Cells Into Weight-Sharing"),
        ],
        "paragraphs": [
            "EXPOSING A 20-YEAR MYTH: Reading Marvin Minsky and Seymour Papert's 1969 book by lamplight, LeCun verified their parity impossibility proof held strictly for single layers—whereas multi-layer hierarchical filters could learn spatial invariance end-to-end.",
            "HUBEL & WIESEL IN SILICON: Combining weight-sharing kernels with spatial subsampling at Holmdel, New Jersey created Convolutional Neural Networks (LeNet-1), demonstrated live on a 486 PC with AT&T DSP32C chips in 1989.",
        ],
        "quote": "“I turned to Hubel and Wiesel's classic neuroscience work on visual cortex and asked: can we train convolutional filters end-to-end with backpropagation directly from raw pixels?”",
        "highlight_span": "train convolutional filters end-to-end with backpropagation",
        "footnote": "UPMC PARIS – TORONTO – BELL LABS HOLMDEL NJ (1985–1989) // VERIFIED DOSSIER // EP05",
    },
    {
        "id": "EP05_DOC_04",
        "raw_png": "EP05_DOC_04_ACT2_AT_T_Checks_DjVu_SVM_Wilderness.png",
        "web_jpg": "ep05_doc_04_checks_djvu_svm_1998.jpg",
        "master_mp4": "EP05_DOC_04_Checks_DjVu_10s.mp4",
        "accent": "#A855F7",
        "stamp": "20% US CHECKS // DJVU",
        "kicker": "COMMERCIAL DEPLOYMENT (1995) & 15-YEAR SVM WILDERNESS (1995–2012) // BELL LABS & NYU",
        "headline": "Reading 20% of US Bank Checks, Inventing DjVu & The 15-Year SVM Exile",
        "meta": [
            ("NCR ATM DEPLOYMENT", "LeNet & Graph Transformer Networks Read 10–20% of All US Bank Checks"),
            ("DJVU COMPRESSION", "Co-Created With Leon Bottou & Patrick Haffner (1996) for Scanned Books"),
            ("ACADEMIC EXILE", "SVM Kernel Era Saw NeurIPS & CVPR Reject Deep ConvNet Papers Repeatedly"),
            ("NYU COURANT (2003)", "Silver Professor Advancing Energy-Based Models Before GPUs Arrived"),
        ],
        "paragraphs": [
            "PROVEN AT NATIONAL SCALE BEFORE HYPE: Long before ImageNet existed, LeCun's AT&T Bell Labs recognition engine processed millions of handwritten bank checks daily across North American ATMs and Post Office sorting lines.",
            "SUPERSONIC JET WITHOUT A RUNWAY: Even after proving real-world utility, mainstream machine learning sidelined neural nets for fifteen years until fast CUDA GPUs unlocked millions of trainable parameters in 2012.",
        ],
        "quote": "“By the late 1990s the system I built at Bell Labs was reading something like 10 to 20 percent of all the checks in the US—and at that exact moment the research community abandoned neural nets.”",
        "highlight_span": "10 to 20 percent of all the checks in the US",
        "footnote": "AT&T LABS – INTERNET ARCHIVE DJVU – NYU COURANT (1995–2012) // VERIFIED DOSSIER // EP05",
    },
    {
        "id": "EP05_DOC_05",
        "raw_png": "EP05_DOC_05_ACT3_Meta_FAIR_PyTorch_LLaMA_Gutenberg.png",
        "web_jpg": "ep05_doc_05_fair_pytorch_llama.jpg",
        "master_mp4": "EP05_DOC_05_FAIR_OpenSource_10s.mp4",
        "accent": "#22C55E",
        "stamp": "OPEN AI // 2013–2025",
        "kicker": "FOUNDING DIRECTOR OF META FAIR (DEC 2013) // PYTORCH, ICLR OPENREVIEW & LLAMA WEIGHTS",
        "headline": "The 2013 Open-Science Covenant: FAIR, PyTorch & The Gutenberg Defense",
        "meta": [
            ("ZUCKERBERG PACT (2013)", "Conditioned Joining Facebook on Publishing Open Papers & Code Without Vetoes"),
            ("ICLR + OPENREVIEW", "Co-Founded ICLR (2013) With Bengio to Break Closed Peer-Review Gatekeepers"),
            ("PYTORCH ENGINE", "FAIR Open-Sourced Research Framework Now Powering Global Deep Learning"),
            ("GUTENBERG ANALOGY", "Defended Open-Weight LLaMA Against Regulatory Capture & Corporate Monopolies"),
        ],
        "paragraphs": [
            "BUILDING AN OPEN BELL LABS FOR AI: Joining New York's Facebook AI Research lab in December 2013, LeCun institutionalized rapid open publication—shaping PyTorch, self-supervised vision (DINO/I-JEPA), and open-weight foundation models.",
            "LIGHT AGAINST PROPRIETARY CASTLES: Comparing open AI weights to Johannes Gutenberg's movable type, he argued concentration of intelligence inside two closed APIs is far riskier than transparent global scientific scrutiny.",
        ],
        "quote": "“The printing press democratized knowledge when critics feared chaos—similarly, the world's AI platform must become open-source common infrastructure, never owned by a handful of closed corporations.”",
        "highlight_span": "open-source common infrastructure",
        "footnote": "META FAIR NYC & PARIS – LEX FRIDMAN #258 / #416 // VERIFIED OPEN-SCIENCE DOSSIER // EP05",
    },
    {
        "id": "EP05_DOC_06",
        "raw_png": "EP05_DOC_06_ACT4_Turing_2018_JEPA_World_Models_AMI_2026.png",
        "web_jpg": "ep05_doc_06_jepa_ami_labs_2026.jpg",
        "master_mp4": "EP05_DOC_06_JEPA_AMI_10s.mp4",
        "accent": "#F43F5E",
        "stamp": "JEPA // AMI LABS $1.03B",
        "kicker": "TURING AWARD (2018) -> AUTONOMOUS MACHINE INTELLIGENCE (2022) -> AMI LABS PARIS (2026)",
        "headline": "Beyond Autoregressive Tokens: JEPA World Models & AMI Labs ($1.03B Seed)",
        "meta": [
            ("TURING TRIAD (2018)", "Awarded With Geoffrey Hinton & Yoshua Bengio for Deep Learning Revolution"),
            ("DATA REALITY GAP", "4-Year-Old Sees ~16,000 Hours Vision (~10^14 Bits) vs. 10^13 Bytes LLM Text"),
            ("JEPA ARCHITECTURE", "Joint Embedding Predictive Architecture Forecasts Abstract State—Not Pixels"),
            ("AMI LABS (2025–2026)", "Left Meta to Co-Found Advanced Machine Intelligence in Paris ($1.03B Raise)"),
        ],
        "paragraphs": [
            "WHY YOUR HOUSE CAT BEATS GPT ON PHYSICS: Autoregressive token prediction scales exponentially without grounding—diverging over long horizons because text captures a thin shadow of continuous 3D physical reality.",
            "SAILING CLOSE-HAULED INTO THE NEXT ERA: Rejecting billion-dollar LLM conformity in 2025–2026, LeCun launched AMI Labs in Paris to build hierarchical JEPA World Models capable of causal planning and common sense.",
        ],
        "quote": "“We are not going to get to human-level intelligence by scaling up autoregressive LLMs. A house cat has an intuitive physical world model richer than any language chatbot ever trained.”",
        "highlight_span": "intuitive physical world model richer than any language chatbot",
        "footnote": "ETH ZURICH KEYNOTE / DAVOS 2026 / AMI LABS $1.03B ARCHIVE // EP05 FINALE",
    },
]

EP05_CARDS = [
    (
        "EP05_UA_CARD_01_Soldering_And_Human_Eye.png",
        "EP05_UA_CLIP_CARD_01_Soldering_Eye_10s.mp4",
        10.0,
        "Акт 1 // Паризькі передмістя 1974 • Інженерія й еволюція",
        "«Розум не народився з правил у зошиті — розум почався тієї секунди, коли у темному океані вперше відкрилося живе око».",
        "— Пролог // Світло, зір та паяльник батька",
        (245, 185, 65),
        60,
    ),
    (
        "EP05_UA_CARD_02_Piaget_Constructivism_Choice.png",
        "EP05_UA_CLIP_CARD_02_Piaget_Constructivism_10s.mp4",
        10.0,
        "Акт 1 // Інженерна школа ESIEE Paris • Дискусія 1975",
        "«Дитина не народжується з готовою таблицею синтаксису — мозок будує модель реальності власноруч, зіштовхуючись із законами фізики».",
        "— Ян Лекун // Жан Піаже проти Ноама Хомського",
        (56, 189, 248),
        58,
    ),
    (
        "EP05_UA_CARD_03_Minsky_Pencil_Proof.png",
        "EP05_UA_CLIP_CARD_03_Minsky_Pencil_10s.mp4",
        10.0,
        "Акт 1 // Нічний підвал у Парижі (PhD 1985–1987)",
        "«Мінський і Пейперт довели безсилля одного шару персептрона — та вся галузь на двадцять років заборонила собі дивитися глибше».",
        "— Ян Лекун // Сорбонна та перерахунок формул",
        (168, 85, 247),
        58,
    ),
    (
        "EP05_UA_CARD_04_LeNet_Hubel_Wiesel_Checks.png",
        "EP05_UA_CLIP_CARD_04_LeNet_Checks_10s.mp4",
        10.0,
        "Акт 2 // AT&T Bell Labs Холмдел (1988–1995)",
        "«Перенесена із зорової кори кота геометрія згорток у Bell Labs розпізнавала кожен п'ятий паперовий банківський чек Сполучених Штатів».",
        "— Ян Лекун // Про LeNet-5 та 20% чеків США",
        (56, 189, 248),
        58,
    ),
    (
        "EP05_UA_CARD_05_Supersonic_Jet_15_Years.png",
        "EP05_UA_CLIP_CARD_05_Supersonic_Exile_10s.mp4",
        10.0,
        "Акт 2 // Ера методу опорних векторів (1995–2012)",
        "«Побудувати згорткову мережу в епоху SVM — це зібрати надзвуковий винищувач за п'ятнадцять років до появи бетонних злітних смуг».",
        "— П'ятнадцять років у науковій пустелі // NYU",
        (100, 190, 255),
        58,
    ),
    (
        "EP05_UA_CARD_06_Gutenberg_Press_Open_AI.png",
        "EP05_UA_CLIP_CARD_06_Gutenberg_OpenAI_10s.mp4",
        10.0,
        "Акт 3 // Пакт Meta FAIR 2013 • PyTorch & LLaMA",
        "«Друкарський верстат Гутенберга не спалив Європу — він вирвав знання з рук монополістів. Відкритий код ШІ — це новий Гутенберг».",
        "— Ян Лекун // Захист відкритих ваг LLaMA",
        (34, 197, 94),
        58,
    ),
    (
        "EP05_UA_CARD_07_House_Cat_VS_LLMs.png",
        "EP05_UA_CLIP_CARD_07_Cat_VS_LLM_12s.mp4",
        12.0,
        "Акт 3–4 // Межі авторегресивних мовних моделей",
        "«Звичайний домашній кіт розуміє фізику простору краще за будь-який суперкомп'ютер LLM, бо дитина бачить 16 000 годин світу очима, а не читає токени».",
        "— Ян Лекун // ETH Zurich & Lex Fridman #416",
        (255, 90, 95),
        56,
    ),
    (
        "EP05_UA_CARD_08_Sailing_Close_Hauled_Finale.png",
        "EP05_UA_CLIP_CARD_08_Close_Hauled_Finale_12s.mp4",
        12.0,
        "Акт 4 // Світові моделі JEPA & AMI Labs Париж (2026)",
        "«Коли весь флот іде за попутним вітром хайпу, єретик ставить вітрило під гострим кутом бейдевінд — і першим досягає нового континенту».",
        "— Епілог // Ян Лекун: Єретик світла та світових моделей",
        (245, 185, 65),
        58,
    ),
]

PHOTO_STILL_CLIPS = [
    ("EP05_IMG_ARCH_01_Paris_1977_Opera_Youth_Era.jpg", "EP05_CLIP_STILL_Paris_1977_Opera_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_02_Tektronix_475A_Oscilloscope_1977.jpg", "EP05_CLIP_STILL_Tektronix_475A_1977_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_03_MOS_6502_Microprocessor_Die.jpg", "EP05_CLIP_STILL_MOS_6502_Die_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_04_ESIEE_Paris_Engineering_School.jpg", "EP05_CLIP_STILL_ESIEE_Paris_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_05_Sorbonne_Paris_PhD_Campus.jpg", "EP05_CLIP_STILL_Sorbonne_Paris_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_06_Marvin_Minsky_Perceptrons_Rival.jpg", "EP05_CLIP_STILL_Marvin_Minsky_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_07_Bell_Labs_Holmdel_Aerial_1987.jpg", "EP05_CLIP_STILL_Bell_Labs_1987_Aerial_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_08_Bell_Labs_Holmdel_Mirror_Building.jpg", "EP05_CLIP_STILL_Bell_Labs_Holmdel_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_09_Courant_Institute_NYU_Weaver_Hall.jpg", "EP05_CLIP_STILL_Courant_NYU_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_10_Yann_LeCun_Minnesota_CNN_Lecture.jpg", "EP05_CLIP_STILL_LeCun_Minnesota_CNN_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_11_Meta_Menlo_Park_HQ_One_Hacker_Way.jpg", "EP05_CLIP_STILL_Meta_Menlo_Park_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_12_Yann_LeCun_Data_Science_Keynote.jpg", "EP05_CLIP_STILL_LeCun_Data_Science_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_13_Yann_LeCun_Turing_2018_Portrait.jpg", "EP05_CLIP_STILL_LeCun_Turing_2018_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_14_Gutenberg_Printing_Press_Mainz.jpg", "EP05_CLIP_STILL_Gutenberg_Press_Mainz_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_15_Cat_Physics_Animal_Locomotion.jpg", "EP05_CLIP_STILL_Cat_Animal_Locomotion_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_16_Yann_LeCun_IP_Paris_2025_Portrait.jpg", "EP05_CLIP_STILL_LeCun_IP_Paris_2025_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_17_Yann_LeCun_Brussels_EU_Summit_2026.jpg", "EP05_CLIP_STILL_LeCun_EU_2026_6s.mp4", 6.0),
    ("EP05_IMG_ARCH_18_Sailing_Close_Hauled_Badewind.jpg", "EP05_CLIP_STILL_Sailing_Badewind_6s.mp4", 6.0),
]


def ensure_doc01_previews():
    raw_01 = DOSS_DIR / "EP05_DOC_01_ACT2_LeCun_LeNet5_IEEE_1998.png"
    web_01 = WEB_DOSS_IMG / "ep05_doc_01_lenet5_ieee_1998.jpg"
    vid_01 = WEB_DOSS_VID / "EP05_DOC_01.mp4"
    if raw_01.exists():
        if not web_01.exists():
            with Image.open(raw_01) as im:
                im.convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).save(web_01, "JPEG", quality=86, optimize=True)
        if not vid_01.exists():
            subprocess.run([
                FFMPEG, "-y", "-loop", "1", "-i", str(raw_01),
                "-vf", "scale=2560:1440,zoompan=z='min(zoom+0.0005,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1280x720:fps=24,format=yuv420p",
                "-t", "5", "-c:v", "libx264", "-preset", "fast", "-crf", "26", "-movflags", "+faststart",
                str(vid_01),
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"  [OK] EP05_DOC_01 web={web_01.name} web_mp4={vid_01.name}", flush=True)


def main():
    print("=== [0/3] Verifying EP05_DOC_01 Web Previews ===", flush=True)
    ensure_doc01_previews()

    print("=== [1/3] Rendering 5 EP05 4K Documentary Dossiers + Web Previews + Zoom Videos ===", flush=True)
    for spec in DOSSIERS_SPEC:
        html_p = SCRATCH_HTML / f"{spec['id']}.html"
        html_p.write_text(build_dossier_html(spec), encoding="utf-8")
        raw_png = DOSS_DIR / spec["raw_png"]
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--window-size=3840,2160", "--force-device-scale-factor=1",
            f"--screenshot={raw_png}", html_p.as_uri()
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        web_jpg = WEB_DOSS_IMG / spec["web_jpg"]
        with Image.open(raw_png) as im:
            im.convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS).save(web_jpg, "JPEG", quality=86, optimize=True)
        web_mp4 = WEB_DOSS_VID / f"{spec['id']}.mp4"
        master_mp4 = DOSS_DIR / spec["master_mp4"]
        subprocess.run([
            FFMPEG, "-y", "-loop", "1", "-i", str(raw_png),
            "-vf", "scale=2560:1440,zoompan=z='min(zoom+0.0005,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=120:s=1280x720:fps=24,format=yuv420p",
            "-t", "5", "-c:v", "libx264", "-preset", "fast", "-crf", "26", "-movflags", "+faststart",
            str(web_mp4),
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        render_4k_still_video(raw_png, master_mp4, 10.0, zoom_drift=0.05)
        print(f"  [OK] {spec['id']} png={raw_png.stat().st_size//1024}KB web_mp4={web_mp4.stat().st_size//1024}KB master={master_mp4.stat().st_size//1024}KB", flush=True)

    print("=== [2/3] Rendering 8 EP05 4K Ukrainian Quote Cards + Video Clips ===", flush=True)
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP05_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP05: YANN LECUN",
        ))
        mp4_path = STILLS_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)
        print(f"  [OK] {png_name} -> {mp4_name} ({mp4_path.stat().st_size//1024}KB)", flush=True)

    print("=== [3/3] Rendering Ken Burns 4K Archival Motion Clips for EP05 ===", flush=True)
    for src_name, clip_name, dur in PHOTO_STILL_CLIPS:
        src_p = YOUNG_LECUN_DIR / src_name
        if not src_p.exists():
            print(f"  [SKIP missing] {src_name}")
            continue
        dst_p = STILLS_4K_DIR / clip_name
        render_4k_still_video(src_p, dst_p, dur, zoom_drift=0.05)
        print(f"  [OK] {clip_name} ({dst_p.stat().st_size//1024}KB)", flush=True)


if __name__ == "__main__":
    main()
