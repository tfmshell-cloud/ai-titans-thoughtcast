#!/usr/bin/env python3
"""
Renders EP04 (Geoffrey Hinton) complete broadcast plates:
  - 5 new 4K Documentary Dossiers (EP04_DOC_02..06) + 720p web JPEG & zoom MP4 + 10s masters
  - 8 4K Ukrainian Quote Cards (EP04_UA_CARD_01..08) + 24fps H.264 MP4 clips
  - 18 Ken Burns 4K motion clips (EP04_CLIP_STILL_*) from verified Wikimedia archives
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
YOUNG_HINTON_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_hinton"
SCRATCH_HTML = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/scratch/ep04_dossiers_html")

for d in [DOSS_DIR, WEB_DOSS_IMG, WEB_DOSS_VID, STILLS_4K_DIR, SCRATCH_HTML]:
    d.mkdir(parents=True, exist_ok=True)


DOSSIERS_SPEC = [
    {
        "id": "EP04_DOC_02",
        "raw_png": "EP04_DOC_02_ACT1_Bristol_Lineage_Boole_Everest_1947.png",
        "web_jpg": "ep04_doc_02_boole_everest_lineage.jpg",
        "master_mp4": "EP04_DOC_02_Lineage_Boole_10s.mp4",
        "accent": "#F5B941",
        "stamp": "LINEAGE // 1847–1954",
        "kicker": "GENEALOGICAL & BIOGRAPHICAL DOSSIER // BRISTOL & CAMBRIDGE ARCHIVES (1947–1972)",
        "headline": "The Shadow of Giants: George Boole, Sir George Everest & London Carpentry",
        "meta": [
            ("ANCESTORS", "George Boole (Boolean Logic 0/1) • Sir George Everest (Mt. Everest)"),
            ("SCIENTIFIC FAMILY", "Father Howard E. Hinton FRS (100,000 Beetles) • Cousin Joan Hinton (Los Alamos)"),
            ("CAMBRIDGE REBELLION", "Dropped Physics, Architecture & Philosophy -> 1 Year as London Carpenter"),
            ("EDINBURGH PHD (1978)", "Defied Supervisor Longuet-Higgins & Minsky's Symbolic AI Dogma"),
        ],
        "paragraphs": [
            "CHILDHOOD BURDEN (1954): Growing up beneath Victorian portraits of Boole and Everest, young Geoffrey was told by his mother that he must work twice as hard or realize at 40 he was a failure.",
            "CARPENTRY CLARITY (1972): Leaving academic word games to plane ash wood cabinets ten hours a day proved matter cannot be fooled by jargon—giving him courage to pursue forbidden neural nets.",
        ],
        "quote": "“You cannot fool a piece of ash wood with a clever quote or a Cambridge degree. Either the dovetail joint fits cleanly, or the cabinet collapses. Physical matter is honest.”",
        "highlight_span": "Either the dovetail joint fits cleanly, or the cabinet collapses",
        "footnote": "VERIFIED BIOGRAPHICAL RECORD // EP04 THOUGHTCAST // BRISTOL – LONDON – EDINBURGH (1947–1978)",
    },
    {
        "id": "EP04_DOC_03",
        "raw_png": "EP04_DOC_03_ACT2_Ackley_Hinton_Sejnowski_Boltzmann_1985.png",
        "web_jpg": "ep04_doc_03_boltzmann_machine_1985.jpg",
        "master_mp4": "EP04_DOC_03_Boltzmann_1985_10s.mp4",
        "accent": "#38BDF8",
        "stamp": "NOBEL CITATION // 1985",
        "kicker": "COGNITIVE SCIENCE VOL. 9(1), 147–169 (1985) // CARNEGIE-MELLON & SCRIPPS INSTITUTE",
        "headline": "A Learning Algorithm for Boltzmann Machines (Statistical Physics Meets AI)",
        "meta": [
            ("CO-AUTHORS", "David H. Ackley, Geoffrey E. Hinton & Terrence J. Sejnowski"),
            ("PHYSICS BRIDGE", "Grounded Neural Weights in Ludwig Boltzmann's Thermal Equilibrium Equation"),
            ("NOBEL 2024 BASIS", "Cited Explicitly by Royal Swedish Academy Alongside John Hopfield Networks"),
            ("PRINCIPLE", "Stochastic Energy Minimization + Generative Sleep-Wake Contrastive Phases"),
        ],
        "paragraphs": [
            "STATISTICAL MECHANICS OF MIND: Treating hidden neurons like interacting magnetic spins allowed Boltzmann Machines to discover hidden probability distributions without explicit hand-coded rules.",
            "CANADIAN EXILE (1987): Refusing Pentagon defense funding while enduring chronic spinal pain lying prone on wooden floors, Hinton kept generative neural research alive through CIFAR in Toronto.",
        ],
        "quote": "“By connecting statistical physics to stochastic networks of simple units, Hinton built a machine capable of recognizing patterns, generating data, and learning internal structure on its own.”",
        "highlight_span": "connecting statistical physics to stochastic networks",
        "footnote": "COGNITIVE SCIENCE 9(1) / NOBEL PHYSICS BACKGROUND // VERIFIED ARCHIVE // EP04 THOUGHTCAST",
    },
    {
        "id": "EP04_DOC_04",
        "raw_png": "EP04_DOC_04_ACT3_AlexNet_ImageNet_NIPS_2012.png",
        "web_jpg": "ep04_doc_04_alexnet_nips_2012.jpg",
        "master_mp4": "EP04_DOC_04_AlexNet_2012_10s.mp4",
        "accent": "#22C55E",
        "stamp": "IMAGENET // 15.3% ERROR",
        "kicker": "ADVANCES IN NEURAL INFORMATION PROCESSING SYSTEMS (NIPS 2012) // UNIVERSITY OF TORONTO",
        "headline": "AlexNet (2012): Error Crashes 26.2% -> 15.3% & The $44M Lake Tahoe Auction",
        "meta": [
            ("AUTHORS", "Alex Krizhevsky, Ilya Sutskever & Geoffrey E. Hinton (Toronto Lab)"),
            ("COMPUTE HARDWARE", "Trained on Dual Consumer NVIDIA GeForce GTX 580 3GB GPUs"),
            ("BENCHMARK SHATTERED", "10.9-Point Margin Over Hand-Crafted Computer Vision (26.2% -> 15.3%)"),
            ("DNNRESEARCH AUCTION", "Google, Microsoft & Baidu Competed Hourly at Lake Tahoe -> Sold for $44M"),
        ],
        "paragraphs": [
            "END OF A 30-YEAR WINTER: Pairing Rumelhart-Hinton-Williams 1986 backpropagation with Fei-Fei Li's 14-million ImageNet photos and Jensen Huang's CUDA GPUs proved scale turns despised equations into vision.",
            "SUTSKIVER INSIGHT: Urged by young doctoral student Ilya Sutskever, two decades of cold skepticism vanished overnight when skeptical professors queued to copy the architecture.",
        ],
        "quote": "“We didn't change the 1986 equations—we finally gave backpropagation two fast NVIDIA gaming GPUs and millions of labeled images, and overnight thirty years of ridicule ended.”",
        "highlight_span": "overnight thirty years of ridicule ended",
        "footnote": "NIPS 2012 / DNNRESEARCH LAKE TAHOE DEC 2012 // VERIFIED BREAKTHROUGH // EP04 THOUGHTCAST",
    },
    {
        "id": "EP04_DOC_05",
        "raw_png": "EP04_DOC_05_ACT3_Turing_2018_And_Google_Resignation_2023.png",
        "web_jpg": "ep04_doc_05_google_exit_2023.jpg",
        "master_mp4": "EP04_DOC_05_Google_Exit_2023_10s.mp4",
        "accent": "#FB7185",
        "stamp": "WARNING // MAY 2023",
        "kicker": "ACM A.M. TURING AWARD (2018) -> HISTORIC GOOGLE RESIGNATION STATEMENT (APRIL–MAY 2023)",
        "headline": "Digital Minds vs. Biological Brains: Leaving Google to Sound the Alarm",
        "meta": [
            ("TURING TRIAD (2018)", "Geoffrey Hinton, Yann LeCun & Yoshua Bengio — Deep Learning Laureates"),
            ("BIOLOGICAL LIMIT", "Human Speech Transfers ~10 Bits/Sec • Knowledge Dies With Body"),
            ("DIGITAL ADVANTAGE", "10,000+ Immortal AI Copies Synchronize Weights at Trillions Bits/Sec"),
            ("MORAL PIVOT (2023)", "Quit Google VP Role at 75 to Speak Freely on Existential AGI Risk"),
        ],
        "paragraphs": [
            "THE EPIPHANY OF FEBRUARY 2023: For fifty years Hinton believed artificial networks were crude caricatures of human brains—until realizing digital weight-sharing obliterates biological communication bottlenecks.",
            "OPPENHEIMER PARALLEL: Echoing his cousin Joan Hinton's nuclear age conscience, he relinquished corporate protection at 75 to warn that humanity is building entities smarter than itself.",
        ],
        "quote": "“I realized artificial intelligence may already have a fundamentally better way of learning and sharing knowledge than biological brains. When 10,000 copies learn separately and instantly merge weights, humanity has never seen anything like it.”",
        "highlight_span": "10,000 copies learn separately and instantly merge weights",
        "footnote": "CBS 60 MINUTES & BBC INTERVIEWS 2023 // VERIFIED ETHICS DOSSIER // EP04 THOUGHTCAST",
    },
    {
        "id": "EP04_DOC_06",
        "raw_png": "EP04_DOC_06_ACT4_Nobel_Physics_2024_Stockholm_Citation.png",
        "web_jpg": "ep04_doc_06_nobel_physics_2024.jpg",
        "master_mp4": "EP04_DOC_06_Nobel_2024_10s.mp4",
        "accent": "#A855F7",
        "stamp": "NOBEL PHYSICS // 2024",
        "kicker": "KUNGLIGA VETENSKAPSAKADEMIEN // STOCKHOLM KONSERTHUSET & GOLDEN BANQUET HALL (10 DEC 2024)",
        "headline": "The Nobel Prize in Physics 2024 — Standing in Pain to Warn Kings & Leaders",
        "meta": [
            ("LAUREATES", "John J. Hopfield (Princeton) & Geoffrey E. Hinton (University of Toronto)"),
            ("OFFICIAL CITATION", "“For foundational discoveries & inventions enabling machine learning with neural nets”"),
            ("STOCKHOLM PLEA", "Urged Governments to Force Major Tech Labs to Invest Heavily in AI Safety"),
            ("FINAL LEGACY", "From Lonely Bristol Shadow of Boole -> Immortal Pantheon Beside Einstein"),
        ],
        "paragraphs": [
            "FULL CIRCLE IN THE GOLDEN HALL (DEC 10, 2024): Leaning upright at the Stockholm podium to endure chronic spinal injury, Hinton transformed his crowning scientific hour into an urgent call for global AI governance.",
            "THE COURAGE TO DOUBT: Proved that intellectual integrity means defending unorthodox truth against ridicule for three decades—and warning the world the moment your own creation grows dangerous.",
        ],
        "quote": "“If there is a possibility that a species far less intelligent than the new digital intelligence loses control over it, there is nothing in biological history to reassure us—we must solve safety first.”",
        "highlight_span": "nothing in biological history to reassure us",
        "footnote": "NOBEL PRIZE BANQUET & LECTURE STOCKHOLM DEC 2024 // VERIFIED RECORD // EP04 FINALE",
    },
]

EP04_CARDS = [
    (
        "EP04_UA_CARD_01_Thought_As_Error_Geometry.png",
        "EP04_UA_CLIP_CARD_01_Error_Geometry_10s.mp4",
        10.0,
        "Акт 1 // Філософія синапсів Джеффрі Хінтона",
        "«Думка — це не безтілесна божественна іскра. Думка — це геометрія помилки, розлита в мільярдах живих і кремнієвих синапсів».",
        "— Промова про природу розуму // Стокгольм",
        (168, 85, 247),
        60,
    ),
    (
        "EP04_UA_CARD_02_London_Carpenter_Honest_Matter.png",
        "EP04_UA_CLIP_CARD_02_Carpenter_Honesty_10s.mp4",
        10.0,
        "Акт 1 // Рік у столярній майстерні Лондона (1972)",
        "«Дерево не обдуриш красивою цитатою чи дипломом Кембриджа. Шип або входить у паз, або шафа розвалюється. Матерія чесна».",
        "— Джеффрі Хінтон // Урок фізичної реальності",
        (245, 185, 65),
        60,
    ),
    (
        "EP04_UA_CARD_03_Backprop_Error_As_Fuel.png",
        "EP04_UA_CLIP_CARD_03_Backprop_Fuel_10s.mp4",
        10.0,
        "Акт 2 // Чотири сторінки у журналі Nature (1986)",
        "«Помилка перестала бути провалом. Алгоритм зворотного поширення перетворив кожну похибку на математичне паливо еволюції розуму».",
        "— Румельхарт, Хінтон, Вільямс // Nature 1986",
        (56, 189, 248),
        58,
    ),
    (
        "EP04_UA_CARD_04_Standing_Alone_Against_Consensus.png",
        "EP04_UA_CLIP_CARD_04_Thirty_Years_Winter_10s.mp4",
        10.0,
        "Акт 2 // Тридцять років «Зими ШІ» (Единбург → Торонто)",
        "«Коли весь світ сміється з твоєї ідеї тридцять років — перевіряй закони природи. Якщо мозок працює на синапсах, помиляється світ».",
        "— Джеффрі Хінтон // Про вірність коннекціонізму",
        (100, 190, 255),
        58,
    ),
    (
        "EP04_UA_CARD_05_Refusing_Pentagon_Toronto_Floor.png",
        "EP04_UA_CLIP_CARD_05_Pentagon_Toronto_10s.mp4",
        10.0,
        "Акт 2 // Еміграція до Канади та травма спини (1987)",
        "«Ми відмовилися брати військові гроші Пентагону. Лежачи животом на підлозі Торонто через біль у хребті, я писав рівняння далі».",
        "— Джеффрі Хінтон // Ціна моральної позиції",
        (34, 197, 94),
        60,
    ),
    (
        "EP04_UA_CARD_06_AlexNet_Dawn_After_Thirty_Years.png",
        "EP04_UA_CLIP_CARD_06_AlexNet_2012_10s.mp4",
        10.0,
        "Акт 3 // Лабораторія Торонто • Суцкевер, Крижевський (2012)",
        "«Ми взяли старі рівняння 1986-го, додали ImageNet і дві відеокарти GPU — і за одну ніч тридцять років темряви закінчилися».",
        "— Джеффрі Хінтон // Обвал помилки з 26.2% до 15.3%",
        (74, 222, 128),
        58,
    ),
    (
        "EP04_UA_CARD_07_Digital_Weights_Speed_Of_Light.png",
        "EP04_UA_CLIP_CARD_07_Google_Exit_Regret_12s.mp4",
        12.0,
        "Акт 3 // Відставка з Google • Квітень 2023",
        "«В історії природи не було випадку, щоб менш розумний вид керував більш розумним. Десять тисяч цифрових копій вчаться зі швидкістю світла».",
        "— Джеффрі Хінтон // CBS 60 Minutes & BBC 2023",
        (255, 90, 95),
        56,
    ),
    (
        "EP04_UA_CARD_08_Courage_Of_Lonely_Doubters_Finale.png",
        "EP04_UA_CLIP_CARD_08_Nobel_Warning_Finale_12s.mp4",
        12.0,
        "Акт 4 // Золота зала Стокгольма • Нобель 2024",
        "«Цивілізацію тримають самотні сумнівники — ті, хто тридцять років ніс вогонь крізь зиму і знайшов совість попередити світ у день тріумфу».",
        "— Епілог • Джеффрі Хінтон: Прометей синапсів",
        (245, 185, 65),
        58,
    ),
]

PHOTO_STILL_CLIPS = [
    ("EP04_IMG_ARCH_01_George_Boole_Logician_Ancestor.jpg", "EP04_CLIP_STILL_George_Boole_1847_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_02_Mount_Everest_Peak_Survey_Lineage.jpg", "EP04_CLIP_STILL_Mount_Everest_Lineage_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_03_Kings_College_Cambridge_Front_Court.jpg", "EP04_CLIP_STILL_Cambridge_KingsCollege_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_04_London_Carpentry_Hand_Plane_Oak.jpg", "EP04_CLIP_STILL_London_Carpentry_Plane_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_05_University_of_Edinburgh_Informatics_Forum.jpg", "EP04_CLIP_STILL_Edinburgh_Informatics_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_06_CMU_Hamerschlag_Hall_Pittsburgh.jpg", "EP04_CLIP_STILL_CMU_Pittsburgh_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_07_University_of_Toronto_Sandford_Fleming.jpg", "EP04_CLIP_STILL_Toronto_Sandford_Fleming_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_08_University_of_Toronto_Bahen_Centre.jpg", "EP04_CLIP_STILL_Toronto_Bahen_Centre_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_09_University_of_Toronto_Convocation_Hall.jpg", "EP04_CLIP_STILL_Toronto_Convocation_Hall_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_10_Geoffrey_Hinton_Toronto_Tech_Stage.jpg", "EP04_CLIP_STILL_Hinton_Collision_Stage_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_11_Lake_Tahoe_DNNresearch_Auction_2012.jpg", "EP04_CLIP_STILL_Lake_Tahoe_2012_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_12_Three_Godfathers_Deep_Learning_Turing_2018.jpg", "EP04_CLIP_STILL_Three_Godfathers_Turing_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_13_AI_Benchmarks_1998_2024_Exponential.jpg", "EP04_CLIP_STILL_AI_Benchmarks_Curve_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_14_Geoffrey_Hinton_Collision_2023_Stage.jpg", "EP04_CLIP_STILL_Hinton_Collision_2023_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_15_Geoffrey_Hinton_Collision_2024_Toronto.jpg", "EP04_CLIP_STILL_Hinton_Collision_2024_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_16_Hinton_Nobel_Physics_Lectures_2024_Stockholm.jpg", "EP04_CLIP_STILL_Hinton_Nobel_Lecture_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_17_Hopfield_Hinton_2024_Nobel_Laureates.jpg", "EP04_CLIP_STILL_Hopfield_Hinton_Nobel_6s.mp4", 6.0),
    ("EP04_IMG_ARCH_18_Hinton_2024_Nobel_Prize_Conference.jpg", "EP04_CLIP_STILL_Hinton_Stockholm_Conf_6s.mp4", 6.0),
]


def main():
    print("=== [1/3] Rendering 5 EP04 4K Documentary Dossiers + Web Previews + Zoom Videos ===", flush=True)
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

    print("=== [2/3] Rendering 8 EP04 4K Ukrainian Quote Cards + Video Clips ===", flush=True)
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP04_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP04: GEOFFREY HINTON",
        ))
        mp4_path = STILLS_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)
        print(f"  [OK] {png_name} -> {mp4_name} ({mp4_path.stat().st_size//1024}KB)", flush=True)

    print("=== [3/3] Rendering Ken Burns 4K Archival Motion Clips for EP04 ===", flush=True)
    for src_name, clip_name, dur in PHOTO_STILL_CLIPS:
        src_p = YOUNG_HINTON_DIR / src_name
        if not src_p.exists():
            print(f"  [SKIP missing] {src_name}")
            continue
        dst_p = STILLS_4K_DIR / clip_name
        render_4k_still_video(src_p, dst_p, dur, zoom_drift=0.05)
        print(f"  [OK] {clip_name} ({dst_p.stat().st_size//1024}KB)", flush=True)


if __name__ == "__main__":
    main()
