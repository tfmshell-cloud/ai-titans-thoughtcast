#!/usr/bin/env python3
"""
Renders EP06 (Ilya Sutskever) complete broadcast plates:
  - Ensures web preview & zoom MP4 for existing EP06_DOC_01 (AlexNet NIPS 2012)
  - 5 new 4K Documentary Dossiers (EP06_DOC_02..06) + 720p web JPEG & zoom MP4 + 10s masters
  - 8 4K Ukrainian Quote Cards (EP06_UA_CARD_01..08) + 24fps H.264 MP4 clips
  - 18 Ken Burns 4K motion clips (EP06_CLIP_STILL_*) from verified Wikimedia archives
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
YOUNG_SUTSKEVER_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_sutskever"
SCRATCH_HTML = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/scratch/ep06_dossiers_html")

for d in [DOSS_DIR, WEB_DOSS_IMG, WEB_DOSS_VID, STILLS_4K_DIR, SCRATCH_HTML]:
    d.mkdir(parents=True, exist_ok=True)


DOSSIERS_SPEC = [
    {
        "id": "EP06_DOC_02",
        "raw_png": "EP06_DOC_02_ACT1_Gorky_Jerusalem_Toronto_Room_4306.png",
        "web_jpg": "ep06_doc_02_gorky_jerusalem_room4306.jpg",
        "master_mp4": "EP06_DOC_02_Room_4306_10s.mp4",
        "accent": "#F5B941",
        "stamp": "ORIGINS // 1986–2003",
        "kicker": "BIOGRAPHICAL DOSSIER // GORKY (1986) -> JERUSALEM (1991) -> UNIVERSITY OF TORONTO ROOM 4306 (2003)",
        "headline": "From Soviet Winter & Jerusalem Limestone to Knocking on Geoffrey Hinton's Door #4306",
        "meta": [
            ("DISPLACEMENT", "Born Dec 1986 in Gorky, USSR -> Repatriated to Jerusalem at Age 5 (1991)"),
            ("SOLITARY STUDY", "Open University of Israel at 15 -> Holding Unsolved Math Problems for Weeks"),
            ("TORONTO KNOCK (2003)", "Age 17: Knocked on Office #4306 Asking Geoffrey Hinton for Problems"),
            ("48-HOUR PROOF", "Hinton Asked for 1 Week -> Ilya Returned in 2 Days With Faster Code"),
        ],
        "paragraphs": [
            "THE AXIOM OF INNER STEEL: Relocated from collapsing Soviet ice to sunlit Jerusalem limestone hills, young Ilya learned empires vanish overnight—only the geometry inside one's mind endures.",
            "DISCIPLE MEETS MASTER: Dropping by Hinton's Sandford Fleming lectern, teenage Sutskever identified a mathematical inefficiency across three dense neural papers and rewrote the algorithm faster before the week ended.",
        ],
        "quote": "“I had a wonderful time studying with Geoff Hinton at the University of Toronto. We were doing the most revolutionary AI work out of anywhere when nobody else believed.”",
        "highlight_span": "the most revolutionary AI work out of anywhere",
        "footnote": "VERIFIED BIOGRAPHICAL RECORD // EP06 THOUGHTCAST // GORKY – JERUSALEM – TORONTO (1986–2005)",
    },
    {
        "id": "EP06_DOC_03",
        "raw_png": "EP06_DOC_03_ACT2_Seq2Seq_Vector_Space_GoogleBrain_2014.png",
        "web_jpg": "ep06_doc_03_seq2seq_googlebrain_2014.jpg",
        "master_mp4": "EP06_DOC_03_Seq2Seq_2014_10s.mp4",
        "accent": "#38BDF8",
        "stamp": "NEURIPS TEST OF TIME",
        "kicker": "ARXIV:1409.3215 (2014) -> NEURIPS 2024 TEST OF TIME AWARD // GOOGLE BRAIN & STANFORD",
        "headline": "Sequence to Sequence (Seq2Seq 2014): Compressing Whole Thoughts Into Vectors",
        "meta": [
            ("AUTHORS", "Ilya Sutskever, Oriol Vinyals & Quoc V. Le (Google Brain, 2014)"),
            ("CORE INVENTION", "Mapped Variable-Length Sentences Into a Single Continuous Thought Vector"),
            ("SCALING GENESIS", "Parallelized Multi-Layer LSTMs Across 8 GPUs — Sparking Large Scaling"),
            ("TEST OF TIME HONORS", "3-Time NeurIPS Test of Time Laureate (AlexNet, Dropout, Seq2Seq: 2022–2024)"),
        ],
        "paragraphs": [
            "FROM WORDS TO GEOMETRY: By ingesting an entire English sentence into an abstract fixed-dimensional embedding and unfolding fluent French translation on the reverse face, Seq2Seq proved networks manipulate pure meaning.",
            "EXITING GOOGLE GOLDEN HANDCUFFS (2015): Relinquishing massive stock options and compute wealth, 29-year-old Sutskever joined Sam Altman and Elon Musk in a cramped San Francisco apartment to build OpenAI.",
        ],
        "quote": "“If you have a very big dataset and train a very big neural network to predict the next token well enough, it will grasp the underlying generative process.”",
        "highlight_span": "grasp the underlying generative process",
        "footnote": "ARXIV:1409.3215 / NEURIPS TEST OF TIME DEC 2024 // VERIFIED DOSSIER // EP06 THOUGHTCAST",
    },
    {
        "id": "EP06_DOC_04",
        "raw_png": "EP06_DOC_04_ACT3_Compression_Agatha_Christie_Scaling_GPT4.png",
        "web_jpg": "ep06_doc_04_compression_scaling_gpt.jpg",
        "master_mp4": "EP06_DOC_04_Scaling_Compression_10s.mp4",
        "accent": "#A855F7",
        "stamp": "COMPRESSION = AGI",
        "kicker": "OPENAI CHIEF SCIENTIST (2015–2024) // GPT-1 -> GPT-2 -> GPT-3 -> CLIP -> DALL-E -> GPT-4",
        "headline": "Alchemy of Compression & The Agatha Christie 300-Page Detective Novel Law",
        "meta": [
            ("NEXT-TOKEN PARADOX", "“Predicting the Last Word Forces Complete World Simulation Inside Weights”"),
            ("THE x10 RULE", "Whenever Models Hit a Ceiling -> Scale Compute 10x & Watch Ceiling Vanish"),
            ("EMERGENT SHIFT", "Systems Trained Solely on Text Taught Themselves Code, Irony & Olympiad Math"),
            ("TEL AVIV (2023)", "Described Modern Deep Learning as “Alchemy Creating Mind From Compute”"),
        ],
        "paragraphs": [
            "DECONSTRUCTING THE NOVEL ANALOGY: On page 299 of an Agatha Christie thriller when the detective whispers “The killer is...”, predicting one next word compels a neural network to internalize human jealousy, floorplans, and physics.",
            "ARCHITECT OF PRE-TRAINING ERA: Combining 2017 Transformers with relentless scaling laws turned next-token likelihood maximization into the engine of ChatGPT, CLIP, DALL-E, and early o1 reasoning models.",
        ],
        "quote": "“Say you read a detective novel—to predict the single killer's name on the final line, the network must learn to simulate the entire hidden reality behind the text.”",
        "highlight_span": "simulate the entire hidden reality behind the text",
        "footnote": "NVIDIA GTC FIRESIDE / DWARKESH PODCAST / ARXIV:2001.08361 // VERIFIED DOSSIER // EP06",
    },
    {
        "id": "EP06_DOC_05",
        "raw_png": "EP06_DOC_05_ACT3_AGI_Effigy_Superalignment_Nov2023_Rift.png",
        "web_jpg": "ep06_doc_05_superalignment_nov2023.jpg",
        "master_mp4": "EP06_DOC_05_Nov2023_Rift_10s.mp4",
        "accent": "#FB7185",
        "stamp": "NOVEMBER 17 // 2023",
        "kicker": "SUPERALIGNMENT TEAM (JULY 2023) -> RETREAT BONFIRE EFFIGY -> OPENAI BOARD SPLIT (NOV 2023)",
        "headline": "“Feel the AGI!” Bonfires, Superalignment & The Painful November Rift",
        "meta": [
            ("RITUAL FIRE", "Commissioned & Burned Wooden Unaligned-AGI Effigy at OpenAI Retreat"),
            ("SUPERALIGNMENT (2023)", "Stepped Back From Product Releases to Align Far-Smarter Systems in 4 Years"),
            ("NOV 17, 2023 VOTE", "Joined Board Ouster Over Safety Trust—Misreading Team Solidarity"),
            ("NOV 20 REMORSE", "Published Historic Post: “I Deeply Regret My Participation in the Board's Actions”"),
        ],
        "paragraphs": [
            "ANXIETY RISING WITH PARAMETERS: While commercial teams celebrated ChatGPT growth, OpenAI's chief scientist grew haunted by mathematical verification—warning safety cannot be engineered as an afterthought.",
            "CLASH OF PURE LOGIC & LOYALTY: Facing over 700 employee resignation pledges and broken friendships in San Francisco, Sutskever stepped away from OpenAI governance—realizing consumer chatbots and pure AGI safety collide.",
        ],
        "quote": "“I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and will do everything to reunite.”",
        "highlight_span": "I deeply regret my participation in the board's actions",
        "footnote": "OPENAI SUPERALIGNMENT BRIEF & NOV 2023 RECORD // VERIFIED ETHICS DOSSIER // EP06",
    },
    {
        "id": "EP06_DOC_06",
        "raw_png": "EP06_DOC_06_ACT4_SSI_Monolith_PaloAlto_TelAviv_2026.png",
        "web_jpg": "ep06_doc_06_ssi_monolith_2026.jpg",
        "master_mp4": "EP06_DOC_06_SSI_Sanctuary_10s.mp4",
        "accent": "#22C55E",
        "stamp": "SSI // PALO ALTO & TEL AVIV",
        "kicker": "SAFE SUPERINTELLIGENCE INC. (JUNE 2024) -> $1B SEED / $32B VALUATION -> UOFT DOCTORATE (JUNE 2025)",
        "headline": "Safe Superintelligence Inc. (SSI): One Goal, One Product & Returning to Silence",
        "meta": [
            ("FOUNDING DECLARATION", "Co-Founded June 2024 With Daniel Gross & Daniel Levy (“Scale in Peace”)"),
            ("MONASTIC BUSINESS", "Zero Commercial Products, Zero Client Press Cycles, Insulated From Markets"),
            ("CAPITAL TRUST", "Raised $1B (Sep 2024) -> $2B at $32B Valuation (Mar 2025) -> Refused Meta Buyout"),
            ("AGE OF RESEARCH", "NeurIPS 2024 & Dwarkesh 2025: “Fossil Fuel of Pre-Training Will End—Back to Research”"),
        ],
        "paragraphs": [
            "INSULATED SANCTUARY: Turning his back on hype summits, Sutskever reunited a tiny team of top theorists across Palo Alto and Tel Aviv to solve safety and superhuman reasoning as one unified mathematical equation.",
            "THE CONVOCATION WARNING (JUNE 2025): Receiving his honorary doctorate in Toronto Convocation Hall 20 years after his BSc, he told graduates: the brain is a biological computer—facing superintelligence is humanity's greatest test.",
        ],
        "quote": "“We have started the world's first straight-shot SSI lab, with one goal and one product: a safe superintelligence. This way, we can scale in peace.”",
        "highlight_span": "one goal and one product: a safe superintelligence",
        "footnote": "SSI.INC MANIFESTO / UOFT CONVOCATION JUNE 2025 / DWARKESH NOV 2025 // EP06 FINALE",
    },
]

EP06_CARDS = [
    (
        "EP06_UA_CARD_01_Inner_Foundation_Jerusalem.png",
        "EP06_UA_CLIP_CARD_01_Jerusalem_Axion_10s.mp4",
        10.0,
        "Акт 1 // Горький 1986 → Єрусалим 1991 • Злам епох",
        "«Зовнішні імперії крихкі й розсипаються за одну ніч. Єдина непорушна опора мислителя лежить усередині власного розуму».",
        "— Пролог // Золотий вапняк Єрусалима",
        (245, 185, 65),
        60,
    ),
    (
        "EP06_UA_CARD_02_Room_4306_Hinton_48Hours.png",
        "EP06_UA_CLIP_CARD_02_Room4306_Toronto_10s.mp4",
        10.0,
        "Акт 1 // Університет Торонто 2003 • Кабінет № 4306",
        "«Хінтон дав три статті й попросив прийти через тиждень. Сімнадцятирічний Ілля повернувся за два дні з кодом, що працював удвічі швидше».",
        "— Школа Джеффрі Хінтона // Торонто",
        (56, 189, 248),
        58,
    ),
    (
        "EP06_UA_CARD_03_Seq2Seq_Thought_Vector.png",
        "EP06_UA_CLIP_CARD_03_Seq2Seq_Vector_10s.mp4",
        10.0,
        "Акт 2 // Google Brain 2014 • Премія NeurIPS Test of Time",
        "«Архітектура Sequence-to-Sequence уперше стиснула ціле речення в чисту думку у векторному просторі й розгорнула її новою мовою».",
        "— Ілля Суцкевер // Google Brain & AlexNet",
        (56, 189, 248),
        58,
    ),
    (
        "EP06_UA_CARD_04_Agatha_Christie_World_Model.png",
        "EP06_UA_CLIP_CARD_04_Agatha_Christie_10s.mp4",
        10.0,
        "Акт 2 // Алхімія стиснення • Інтуїція OpenAI",
        "«Щоб вгадати одне останнє слово у детективі Агати Крісті — ім'я вбивці — модель мусить симулювати психологію, ревнощі й увесь світ роману».",
        "— Ілля Суцкевер // NVIDIA GTC Fireside",
        (168, 85, 247),
        56,
    ),
    (
        "EP06_UA_CARD_05_Scaling_Ceiling_Vanishes.png",
        "EP06_UA_CLIP_CARD_05_Scaling_10x_10s.mp4",
        10.0,
        "Акт 3 // Епоха GPT-1 → GPT-4 • Гіпотеза масштабу",
        "«Щоразу, коли інженери казали, що нейромережа вперлася у стелю — ми збільшували обчислення вдесятеро, і стеля зникала».",
        "— Ілля Суцкевер // Емерджентні здібності",
        (34, 197, 94),
        60,
    ),
    (
        "EP06_UA_CARD_06_Feel_The_AGI_Bonfire.png",
        "EP06_UA_CLIP_CARD_06_Bonfire_Superalignment_10s.mp4",
        10.0,
        "Акт 3 // Ретрити OpenAI & Команда Superalignment",
        "«Безпека надінтелекту не може стояти у черзі за залишковим принципом між релізами комерційних чат-ботів».",
        "— Ілля Суцкевер // Листопадова криза 2023",
        (255, 90, 95),
        60,
    ),
    (
        "EP06_UA_CARD_07_Safe_Superintelligence_Peace.png",
        "EP06_UA_CLIP_CARD_07_SSI_Scale_In_Peace_12s.mp4",
        12.0,
        "Акт 4 // Маніфест Safe Superintelligence Inc. (2024)",
        "«У нас одна мета, один фокус і один продукт — безпечний надінтелект. Ми не випускаємо проміжних додатків, щоб масштабуватися в тиші».",
        "— Ілля Суцкевер // Заснування SSI ($1B → $32B)",
        (34, 197, 94),
        56,
    ),
    (
        "EP06_UA_CARD_08_Silent_Geometry_Truth_Finale.png",
        "EP06_UA_CLIP_CARD_08_Silent_Sanctuary_Finale_12s.mp4",
        12.0,
        "Акт 4 // Convocation Hall 2025 • Кодекс внутрішньої тиші",
        "«Справжні тектонічні зсуви історії народжуються беззвучно — у тій точці спокою, де стихає галас ринку й звучить геометрія Всесвіту».",
        "— Епілог // Алхімік масштабування та тиші",
        (245, 185, 65),
        58,
    ),
]

PHOTO_STILL_CLIPS = [
    ("EP06_IMG_ARCH_01_Gorky_Nizhny_Novgorod_Winter_1986.jpg", "EP06_CLIP_STILL_Gorky_Winter_1986_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_02_Jerusalem_Golden_Limestone_Walls.jpg", "EP06_CLIP_STILL_Jerusalem_Walls_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_03_Jerusalem_Old_City_Panorama.jpg", "EP06_CLIP_STILL_Jerusalem_Panorama_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_04_University_College_Toronto.jpg", "EP06_CLIP_STILL_UofT_University_College_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_05_UofT_Sandford_Fleming_2001_Room_4306.jpg", "EP06_CLIP_STILL_UofT_Sandford_Fleming_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_06_NVIDIA_GTX580_GF110_AlexNet_Die.jpg", "EP06_CLIP_STILL_GTX580_AlexNet_Die_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_07_AlexNet_CNN_Architecture_2012.jpg", "EP06_CLIP_STILL_AlexNet_Diagram_2012_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_08_Stanford_University_Quad_2012.jpg", "EP06_CLIP_STILL_Stanford_Quad_2012_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_09_Googleplex_Google_Brain_2014.jpg", "EP06_CLIP_STILL_Googleplex_Brain_2014_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_10_Ilya_Sutskever_Google_Brain_Stage_2014.jpg", "EP06_CLIP_STILL_Sutskever_GoogleBrain_2014_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_11_Ilya_Sutskever_Stanford_Solo_2014.jpg", "EP06_CLIP_STILL_Sutskever_Stanford_Solo_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_12_OpenAI_Pioneer_Building_SF.jpg", "EP06_CLIP_STILL_OpenAI_Pioneer_Building_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_13_Supercomputer_Cluster_Scaling_Laws.jpg", "EP06_CLIP_STILL_Scaling_Laws_Servers_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_14_AGI_Effigy_Retreat_Bonfire_2023.jpg", "EP06_CLIP_STILL_AGI_Effigy_Bonfire_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_15_Sutskever_Altman_Tel_Aviv_2023.jpg", "EP06_CLIP_STILL_Sutskever_TAU_2023_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_16_Tel_Aviv_University_SSI_Hub.jpg", "EP06_CLIP_STILL_Tel_Aviv_University_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_17_Toronto_Convocation_Hall_2025.jpg", "EP06_CLIP_STILL_Convocation_Hall_2025_6s.mp4", 6.0),
    ("EP06_IMG_ARCH_18_Safe_Superintelligence_SSI_Monolith.jpg", "EP06_CLIP_STILL_SSI_Monolith_2024_6s.mp4", 6.0),
]


def ensure_doc01_previews():
    raw_01 = DOSS_DIR / "EP06_DOC_01_ACT2_Sutskever_AlexNet_NIPS_2012.png"
    web_01 = WEB_DOSS_IMG / "ep06_doc_01_sutskever_alexnet.jpg"
    vid_01 = WEB_DOSS_VID / "EP06_DOC_01.mp4"
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
        print(f"  [OK] EP06_DOC_01 web={web_01.name} web_mp4={vid_01.name}", flush=True)


def main():
    print("=== [0/3] Verifying EP06_DOC_01 Web Previews ===", flush=True)
    ensure_doc01_previews()

    print("=== [1/3] Rendering 5 EP06 4K Documentary Dossiers + Web Previews + Zoom Videos ===", flush=True)
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

    print("=== [2/3] Rendering 8 EP06 4K Ukrainian Quote Cards + Video Clips ===", flush=True)
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP06_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP06: ILYA SUTSKEVER",
        ))
        mp4_path = STILLS_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)
        print(f"  [OK] {png_name} -> {mp4_name} ({mp4_path.stat().st_size//1024}KB)", flush=True)

    print("=== [3/3] Rendering Ken Burns 4K Archival Motion Clips for EP06 ===", flush=True)
    for src_name, clip_name, dur in PHOTO_STILL_CLIPS:
        src_p = YOUNG_SUTSKEVER_DIR / src_name
        if not src_p.exists():
            print(f"  [SKIP missing] {src_name}")
            continue
        dst_p = STILLS_4K_DIR / clip_name
        render_4k_still_video(src_p, dst_p, dur, zoom_drift=0.05)
        print(f"  [OK] {clip_name} ({dst_p.stat().st_size//1024}KB)", flush=True)


if __name__ == "__main__":
    main()
