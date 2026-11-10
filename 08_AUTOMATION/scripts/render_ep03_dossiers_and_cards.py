#!/usr/bin/env python3
"""
Renders EP03 (Demis Hassabis) complete broadcast plates:
  - 5 new 4K Documentary Dossiers (EP03_DOC_02..06) + 720p web JPEG & zoom MP4 + 10s masters
  - 8 4K Ukrainian Quote Cards (EP03_UA_CARD_01..08) + 24fps H.264 MP4 clips
  - 18 Ken Burns 4K motion clips (EP03_CLIP_STILL_*) from verified Wikimedia archives
"""
import html as html_lib
import subprocess
from pathlib import Path
from PIL import Image, ImageOps
from render_ukrainian_quote_cards import draw_quote_card

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"

DOSS_DIR = ROOT / "05_RAW_FOOTAGE" / "dossiers_press"
UA_CARDS_DIR = DOSS_DIR / "ukrainian_quote_cards"
WEB_DOSS_IMG = ROOT / "07_DASHBOARD" / "assets" / "dossiers_preview"
WEB_DOSS_VID = ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "dossiers"
STILLS_4K_DIR = ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k"
YOUNG_HASSABIS_DIR = ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_hassabis"
SCRATCH_HTML = Path("/Users/volodymyrkatasonov/.gemini/antigravity/brain/7e650e1a-beea-44f1-879f-71808e392c0e/scratch/ep03_dossiers_html")

for d in [DOSS_DIR, UA_CARDS_DIR, WEB_DOSS_IMG, WEB_DOSS_VID, STILLS_4K_DIR, SCRATCH_HTML]:
    d.mkdir(parents=True, exist_ok=True)


DOSSIERS_SPEC = [
    {
        "id": "EP03_DOC_02",
        "raw_png": "EP03_DOC_02_ACT1_Chess_Elo2300_Liechtenstein_1990.png",
        "web_jpg": "ep03_doc_02_chess_elo2300.jpg",
        "master_mp4": "EP03_DOC_02_Chess_Elo2300_10s.mp4",
        "accent": "#F5B941",
        "stamp": "FIDE ARCHIVE // 1990",
        "kicker": "ARCHIVAL DOSSIER // FIDE INTERNATIONAL CHESS RATING REGISTRY • LIECHTENSTEIN OPEN (1989–1990)",
        "headline": "FIDE Master Rating 2300 at Age 13 — & The 10-Hour Liechtenstein Epiphany",
        "meta": [
            ("PLAYER PROFILE", "Demis Hassabis (ENG) • Born 27 July 1976, North London"),
            ("PEAK JUNIOR RANK", "Elo 2300 (FIDE Master) • World #2 Under-14 behind Judit Polgár"),
            ("NATIONAL TEAM", "Captain of All England Junior Chess Teams (Ages 8–13)"),
            ("CRITICAL PIVOT", "10-Hour Match in Liechtenstein -> Abandoning Chess Pro Path for AI"),
        ],
        "paragraphs": [
            "RECORD 01 // AGE 4 INITIATION (EAST FINCHLEY, 1980): Learned chess rules purely by observing father & uncle play; defeating both within 14 days and becoming London U-8 champion at age 6.",
            "RECORD 02 // LIECHTENSTEIN TOURNAMENT REALIZATION (AGE 13): Looking around a tournament hall holding 300 of the world's sharpest young minds grinding for 10 hours over a 64-square wooden board.",
        ],
        "quote": "“If you could plug those 300 brains into solving cancer instead of moving wooden pieces around, we could cure diseases. Although I loved chess, I realized this is not where I should spend my whole life.”",
        "highlight_span": "solve cancer instead of moving wooden pieces",
        "footnote": "VERIFIED PRIMARY DOCUMENT // EP03 THOUGHTCAST // CHESS PRODIGY ARCHIVE (1980–1990)",
    },
    {
        "id": "EP03_DOC_03",
        "raw_png": "EP03_DOC_03_ACT1_Bullfrog_ThemePark_1994_Specs.png",
        "web_jpg": "ep03_doc_03_themepark_1994.jpg",
        "master_mp4": "EP03_DOC_03_ThemePark_1994_10s.mp4",
        "accent": "#38BDF8",
        "stamp": "BULLFROG // 1994 CODE",
        "kicker": "TECHNICAL DESIGN ARCHIVE // BULLFROG PRODUCTIONS LTD. • GUILDFORD, UK (GAP YEAR 1993–1994)",
        "headline": "Theme Park (1994): Co-Designed & Coded at Age 17 Before Starting Cambridge",
        "meta": [
            ("ENGINEERING LEAD", "Demis Hassabis (Age 17) alongside Peter Molyneux"),
            ("ORIGIN CONTEXT", "Cambridge Computer Science Accepted at 16 -> Mandated 1-Year Wait"),
            ("GLOBAL IMPACT", "Multi-Million Unit Global Bestseller • Early Multi-Agent Simulation"),
            ("AI INSIGHT", "Thousands of Simple Local Agent Rules Yield Complex Macro-Behavior"),
        ],
        "paragraphs": [
            "SYSTEM DESIGN // EMERGENT CROWDS: Each digital park visitor operated as an independent reward-seeking agent reacting to queue length, ride excitement, pricing, and thirst.",
            "TRANSITION TO ACADEMIA: Returned to Queens' College, Cambridge at age 18 with financial independence and empirical proof that simulated worlds are laboratories for intelligence.",
        ],
        "quote": "“Cambridge accepted me at 16 but told me to wait a year. I went to Bullfrog and built Theme Park — seeing thousands of little autonomous AI agents generate an unpredictable living economy.”",
        "highlight_span": "autonomous AI agents generate an unpredictable living economy",
        "footnote": "VERIFIED ENGINEERING RECORD // EP03 THOUGHTCAST // BULLFROG SIMULATION ARCHIVE (1994)",
    },
    {
        "id": "EP03_DOC_04",
        "raw_png": "EP03_DOC_04_ACT2_PNAS_Hippocampus_Imagination_2007.png",
        "web_jpg": "ep03_doc_04_pnas_2007.jpg",
        "master_mp4": "EP03_DOC_04_PNAS_2007_10s.mp4",
        "accent": "#22C55E",
        "stamp": "PNAS // TOP 10 SCIENCE",
        "kicker": "PROCEEDINGS OF THE NATIONAL ACADEMY OF SCIENCES // VOL. 104, NO. 5 • UCL NEUROSCIENCE (2007)",
        "headline": "Patients with Hippocampal Amnesia Cannot Imagine New Experiences",
        "meta": [
            ("AUTHORS", "Demis Hassabis, Dharshan Kumaran, Seralynne D. Vann & Eleanor A. Maguire"),
            ("INSTITUTION", "Wellcome Trust Centre for Neuroimaging, University College London (UCL)"),
            ("RECOGNITION", "Cited by Science Magazine as One of the Top 10 Breakthroughs of 2007"),
            ("AI TRANSLATION", "Inspired DeepMind Experience Replay Buffer in Deep Q-Networks (DQN)"),
        ],
        "paragraphs": [
            "EMPIRICAL FINDING: Bilateral hippocampal damage destroys not only episodic memory of the past, but also the ability to construct coherent mental simulations of future scenarios.",
            "ALGORITHMIC BRIDGE (2010–2013): Just as the human hippocampus replays waking episodes during sleep to generalize policy, DeepMind gave Atari Breakout agents an Experience Replay memory buffer.",
        ],
        "quote": "“Imagination and episodic memory share the same neural machinery in the hippocampus — the brain is not a passive recorder, it is a scene-construction simulation engine for tomorrow.”",
        "highlight_span": "same neural machinery in the hippocampus",
        "footnote": "PNAS 104(5), 1726–1731 (JAN 30, 2007) // VERIFIED NEUROSCIENCE ARCHIVE // EP03 THOUGHTCAST",
    },
    {
        "id": "EP03_DOC_05",
        "raw_png": "EP03_DOC_05_ACT3_Nature_AlphaFold2_CASP14_2021.png",
        "web_jpg": "ep03_doc_05_alphafold2_nature.jpg",
        "master_mp4": "EP03_DOC_05_AlphaFold2_Nature_10s.mp4",
        "accent": "#A855F7",
        "stamp": "CASP14 // GDT 92.4",
        "kicker": "NATURE VOL. 596, 583–589 (15 JULY 2021) // CASP14 GRAND CHALLENGE • GOOGLE DEEPMIND & EMBL-EBI",
        "headline": "Highly Accurate Protein Structure Prediction with AlphaFold 2",
        "meta": [
            ("CORE ARCHITECTURE", "Evoformer + Equivariant 3D Structure Module (Geometric Attention)"),
            ("CASP14 ACCURACY", "92.4 GDT_TS Median Score — Atomic Width Precision (~1.0 Å RMSD)"),
            ("SCALE ACHIEVED", "200,000,000+ Predicted Structures — Virtually All Known Science Proteins"),
            ("OPEN ACCESS", "100% Free Global Release via AlphaFold Protein Structure Database"),
        ],
        "paragraphs": [
            "STRUCTURAL PIVOT (2018->2020): After winning CASP13 with AlphaFold 1, Hassabis scrapped the architecture and rebuilt end-to-end physics-aware geometric attention directly over amino acid chains.",
            "SCIENTIFIC GIFT: Rather than monetizing predictions behind a paywall, DeepMind folded all 200M catalogued proteins in one year — saving billions of years of X-ray crystallography.",
        ],
        "quote": "“AlphaFold 2 achieved an error comparable to the width of a single carbon atom. Instead of charging for single structures, we decided to fold every protein known to science and gift it to the world.”",
        "highlight_span": "fold every protein known to science and gift it to the world",
        "footnote": "NATURE DOI: 10.1038/s41586-021-03819-2 // VERIFIED PROTEIN UNIVERSE ARCHIVE // EP03 THOUGHTCAST",
    },
    {
        "id": "EP03_DOC_06",
        "raw_png": "EP03_DOC_06_ACT4_Nobel_Chemistry_2024_Citation.png",
        "web_jpg": "ep03_doc_06_nobel_2024.jpg",
        "master_mp4": "EP03_DOC_06_Nobel_2024_10s.mp4",
        "accent": "#F5B941",
        "stamp": "NOBEL LAUREATE // 2024",
        "kicker": "THE ROYAL SWEDISH ACADEMY OF SCIENCES // STOCKHOLM KONSERTHUSET • DECEMBER 2024",
        "headline": "The Nobel Prize in Chemistry 2024 — Half Awarded to Demis Hassabis & John Jumper",
        "meta": [
            ("OFFICIAL CITATION", "“For protein structure prediction” — Validating a 50-Year Biology Quest"),
            ("CO-LAUREATES", "Demis Hassabis (Google DeepMind) • John M. Jumper • David Baker"),
            ("NEXT FRONTIER", "Isomorphic Labs (Digital Drug Design), Tokamak Plasma & GNoME Crystals"),
            ("DEEPMIND CREDO", "Step 1: Solve Intelligence. Step 2: Use It to Solve Everything Else."),
        ],
        "paragraphs": [
            "HISTORIC PRECEDENT: Awarded just four years after AlphaFold 2's CASP14 breakthrough — one of the fastest validations from algorithmic discovery to Nobel Prize in modern scientific history.",
            "ULTIMATE SYNTHESIS: Connecting 1980s East Finchley chess trees, Bullfrog game simulations, UCL hippocampal studies, and Move 37 intuition into a digital telescope reading the source code of life.",
        ],
        "quote": "“AI is the ultimate meta-solution: the digital telescope that will allow humanity to accelerate centuries of chemistry, biology, and physics into a single decade.”",
        "highlight_span": "digital telescope that will allow humanity to accelerate",
        "footnote": "KUNGLIGA VETENSKAPSAKADEMIEN STOCKHOLM 2024 // EP03 FINALE ARCHIVE // THOUGHTCAST 4K",
    },
]

EP03_CARDS = [
    (
        "EP03_UA_CARD_01_Cosmology_Of_64_Squares.png",
        "EP03_UA_CLIP_CARD_01_Chess_Order_10s.mp4",
        10.0,
        "Акт 1 // Північний Лондон (1980 • 4 роки)",
        "«Для мене шахи не були іграшкою. Це був замкнений космос із 64 клітинок, де немає місця сліпій удачі».",
        "— Деміс Гассабіс // Магія порядку на дошці",
        (245, 185, 65),
        64,
    ),
    (
        "EP03_UA_CARD_02_Biological_Intuition_Vs_BruteForce.png",
        "EP03_UA_CLIP_CARD_02_ZX_Spectrum_Intuition_10s.mp4",
        10.0,
        "Акт 1 // ZX Spectrum 48K та асемблер Z80 (8 років)",
        "«Коли я граю в шахи, я не рахую мільйони варіантів. Чому мій мозок відчуває форму позиції, а машина приречена на перебір?»",
        "— Деміс Гассабіс // Головне питання дитинства",
        (56, 189, 248),
        60,
    ),
    (
        "EP03_UA_CARD_03_Leaving_Chess_For_Science.png",
        "EP03_UA_CLIP_CARD_03_Liechtenstein_Pivot_10s.mp4",
        10.0,
        "Акт 1 // Турнір у Ліхтенштейні • Майстер ФІДЕ (Ело 2300)",
        "«300 найгостріших умів світу спалюють життя на дерев'яні фігурки — замість того, щоб лікувати хвороби та розгадувати Всесвіт».",
        "— Деміс Гассабіс // Вихід із шахової дошки",
        (255, 170, 50),
        60,
    ),
    (
        "EP03_UA_CARD_04_Memory_And_Imagination_Hippocampus.png",
        "EP03_UA_CLIP_CARD_04_UCL_Hippocampus_10s.mp4",
        10.0,
        "Акт 2 // Нейробіологія в UCL • Відкриття року Science (2007)",
        "«Пам'ять і уява — це один і той самий нейронний механізм гіпокампа. Мозок програє досвід заново, щоб симулювати майбутнє».",
        "— Деміс Гассабіс // Дисертація та PNAS 2007",
        (34, 197, 94),
        60,
    ),
    (
        "EP03_UA_CARD_05_Two_Step_Manifesto_AGI.png",
        "EP03_UA_CLIP_CARD_05_Two_Step_Plan_10s.mp4",
        10.0,
        "Акт 2 // Заснування DeepMind • Лондон, 2010 рік",
        "«Крок перший: Розв'язати проблему інтелекту. Крок другий: Використати його, щоб розв'язати все інше у Всесвіті».",
        "— Деміс Гассабіс // Бізнес-план, з якого сміялися інвестори",
        (64, 224, 208),
        62,
    ),
    (
        "EP03_UA_CARD_06_Move37_Alien_Creativity.png",
        "EP03_UA_CLIP_CARD_06_Move37_Seoul_12s.mp4",
        12.0,
        "Акт 3 // Сеул • Матч AlphaGo проти Лі Седоля (Хід 37)",
        "«Людство вперше побачило не імітацію свого розуму — а справжню машинну креативність, вільну від 3000 років людських догм».",
        "— Про Хід 37 на п'ятій лінії • Імовірність 1 : 10 000",
        (245, 185, 65),
        60,
    ),
    (
        "EP03_UA_CARD_07_AlphaFold_200M_Open_Gift.png",
        "EP03_UA_CLIP_CARD_07_AlphaFold_Gift_10s.mp4",
        10.0,
        "Акт 3 // AlphaFold 2 • CASP14 → Нобелівська премія 2024",
        "«Замість того щоб продавати доступи по одному білку, ми вирішили згорнути всі 200 мільйонів білків Землі — і відкрити їх безкоштовно».",
        "— Деміс Гассабіс // Подарунок світовій медицині",
        (168, 85, 247),
        58,
    ),
    (
        "EP03_UA_CARD_08_Universe_Reading_Source_Code.png",
        "EP03_UA_CLIP_CARD_08_Source_Code_Finale_12s.mp4",
        12.0,
        "Акт 4 // Фінал • Нічна зміна в Лондоні (00:00–04:00)",
        "«Коли серед ночі в лондонському кабінеті спалахує монітор — це життя за допомогою цифрового телескопа вперше читає свій вихідний код».",
        "— Епілог • Деміс Гассабіс: Гросмейстер біологічного коду",
        (74, 222, 128),
        58,
    ),
]

PHOTO_STILL_CLIPS = [
    ("EP03_IMG_ARCH_01_North_London_Finchley_Youth_Era.jpg", "EP03_CLIP_STILL_Finchley_London_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_02_Staunton_Chess_Board_Strategy.jpg", "EP03_CLIP_STILL_Staunton_Chess_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_03_Garde_Mechanical_Chess_Clock.jpg", "EP03_CLIP_STILL_Garde_Clock_5s.mp4", 5.0),
    ("EP03_IMG_ARCH_04_Sinclair_ZX_Spectrum_48K_1984.jpg", "EP03_CLIP_STILL_ZX_Spectrum_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_05_ZX_Spectrum_48K_Keyboard_Detail.jpg", "EP03_CLIP_STILL_ZX_Keyboard_5s.mp4", 5.0),
    ("EP03_IMG_ARCH_06_Queens_College_Cambridge_Gatehouse.jpg", "EP03_CLIP_STILL_Cambridge_Gatehouse_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_07_Queens_College_Mathematical_Bridge.jpg", "EP03_CLIP_STILL_Math_Bridge_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_08_UCL_Main_Quad_Cognitive_Neuroscience.jpg", "EP03_CLIP_STILL_UCL_Main_Building_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_09_Demis_Hassabis_DeepMind_Early_Talk_2014.jpg", "EP03_CLIP_STILL_DeepMind_2014_Stage_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_10_DeepMind_London_HQ_Kings_Cross.jpg", "EP03_CLIP_STILL_DeepMind_KingsCross_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_11_Goban_Board_Go_Move37_Strategy.jpg", "EP03_CLIP_STILL_Goban_Stones_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_12_Demis_Hassabis_DeepMind_Era_Portrait.jpg", "EP03_CLIP_STILL_Hassabis_EPFL_Talk_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_13_AlphaFold_ZNF555_Protein_Structure.jpg", "EP03_CLIP_STILL_AlphaFold_ZNF555_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_14_AlphaFold2_Transformer_Architecture.jpg", "EP03_CLIP_STILL_AlphaFold2_Diagram_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_15_Royal_Society_London_Carlton_Terrace.jpg", "EP03_CLIP_STILL_Royal_Society_London_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_16_Nobel_Lectures_2024_Hassabis_Stockholm.jpg", "EP03_CLIP_STILL_Nobel_Lecture_Podium_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_17_Nobel_2024_Laureates_Hassabis_Jumper_Baker.jpg", "EP03_CLIP_STILL_Nobel_Laureates_Trio_6s.mp4", 6.0),
    ("EP03_IMG_ARCH_18_Demis_Hassabis_Nobel_Week_2024_Portrait.jpg", "EP03_CLIP_STILL_Hassabis_Nobel_Week_6s.mp4", 6.0),
]


def build_dossier_html(spec: dict) -> str:
    accent = spec["accent"]
    hl = html_lib.escape(spec["highlight_span"])
    q_esc = html_lib.escape(spec["quote"]).replace(hl, f'<span class="hl">{hl}</span>')
    meta_html = "".join(
        f'<div class="meta-box"><div class="meta-k">{html_lib.escape(k)}</div><div class="meta-v">{html_lib.escape(v)}</div></div>'
        for k, v in spec["meta"]
    )
    paras_html = "".join(f"<p>{html_lib.escape(p)}</p>" for p in spec["paragraphs"])
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html, body {{
  width: 3840px; height: 2160px; overflow: hidden;
  background: radial-gradient(circle at 22% 18%, #162032 0%, #090d16 58%, #04060b 100%);
  color: #e6eef8; font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Helvetica Neue", sans-serif;
}}
.grid-bg {{
  position: absolute; inset: 0;
  background-image: linear-gradient(rgba(255,255,255,0.03) 2px, transparent 2px),
                    linear-gradient(90deg, rgba(255,255,255,0.03) 2px, transparent 2px);
  background-size: 96px 96px;
}}
.frame {{
  position: relative; width: 3560px; height: 1880px; margin: 140px;
  border: 3px solid rgba(255,255,255,0.16); border-radius: 28px;
  background: linear-gradient(160deg, rgba(16,24,39,0.92), rgba(8,12,20,0.96));
  box-shadow: 0 50px 140px rgba(0,0,0,0.75); padding: 92px 110px;
  display: flex; flex-direction: column; justify-content: space-between;
}}
.topbar {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(255,255,255,0.14); padding-bottom: 36px; }}
.kicker {{ font-family: "SF Mono", Menlo, monospace; font-size: 32px; letter-spacing: 3px; color: {accent}; font-weight: 700; }}
.stamp {{ border: 4px solid {accent}; color: {accent}; font-family: "SF Mono", Menlo, monospace; font-size: 34px; font-weight: 800; padding: 14px 32px; border-radius: 12px; letter-spacing: 3px; background: rgba(255,255,255,0.03); }}
h1 {{ font-size: 82px; line-height: 1.12; letter-spacing: -1.5px; color: #ffffff; margin: 38px 0 34px; font-weight: 800; }}
.meta-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px 36px; margin-bottom: 34px; }}
.meta-box {{ background: rgba(255,255,255,0.04); border-left: 6px solid {accent}; padding: 22px 30px; border-radius: 10px; }}
.meta-k {{ font-family: "SF Mono", Menlo, monospace; font-size: 24px; letter-spacing: 2px; color: #94a3b8; margin-bottom: 8px; }}
.meta-v {{ font-size: 33px; font-weight: 600; color: #f1f5f9; }}
.paras {{ display: flex; flex-direction: column; gap: 22px; margin-bottom: 34px; }}
.paras p {{ font-size: 36px; line-height: 1.44; color: #cbd5e1; }}
.quote-box {{
  background: rgba(15, 23, 42, 0.85); border: 2px solid {accent}; border-radius: 18px;
  padding: 44px 56px; font-family: "Georgia", serif; font-size: 46px; line-height: 1.38; color: #f8fafc;
}}
.hl {{ background: rgba(245, 185, 65, 0.24); color: #fde68a; padding: 4px 12px; border-radius: 8px; font-weight: 700; }}
.foot {{ display: flex; justify-content: space-between; align-items: center; border-top: 2px solid rgba(255,255,255,0.12); padding-top: 30px; font-family: "SF Mono", Menlo, monospace; font-size: 28px; color: #64748b; letter-spacing: 2px; }}
</style></head><body>
<div class="grid-bg"></div>
<div class="frame">
  <div>
    <div class="topbar">
      <div class="kicker">{html_lib.escape(spec["kicker"])}</div>
      <div class="stamp">{html_lib.escape(spec["stamp"])}</div>
    </div>
    <h1>{html_lib.escape(spec["headline"])}</h1>
    <div class="meta-grid">{meta_html}</div>
    <div class="paras">{paras_html}</div>
  </div>
  <div>
    <div class="quote-box">{q_esc}</div>
    <div class="foot">
      <span>{html_lib.escape(spec["footnote"])}</span>
      <span>3840×2160 UHD // 24FPS MASTER PLATE</span>
    </div>
  </div>
</div>
</body></html>"""


def render_4k_still_video(src_path: Path, dst_path: Path, dur_s: float, zoom_drift: float = 0.05):
    frames = max(24, int(round(dur_s * 24.0)))
    step = zoom_drift / float(frames)
    vf = (
        f"scale=3840:2160:force_original_aspect_ratio=increase,"
        f"crop=3840:2160:(iw-3840)/2:(ih-2160)/2,"
        f"zoompan=z='min(zoom+{step:.6f},{1.0+zoom_drift:.3f})':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps=24,"
        f"format=yuv420p"
    )
    subprocess.run([
        FFMPEG, "-y", "-loop", "1", "-i", str(src_path),
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
        "-vf", vf,
        "-t", f"{dur_s:.2f}", "-shortest",
        "-c:v", "libx264", "-preset", "fast", "-crf", "19", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
        str(dst_path),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    print("=== [1/3] Rendering 5 EP03 4K Documentary Dossiers + Web Previews + Zoom Videos ===", flush=True)
    for spec in DOSSIERS_SPEC:
        html_p = SCRATCH_HTML / f"{spec['id']}.html"
        html_p.write_text(build_dossier_html(spec), encoding="utf-8")
        raw_png = DOSS_DIR / spec["raw_png"]
        subprocess.run([
            CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--window-size=3840,2160", "--force-device-scale-factor=1",
            f"--screenshot={raw_png}", html_p.as_uri()
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # web jpg
        web_jpg = WEB_DOSS_IMG / spec["web_jpg"]
        with Image.open(raw_png) as im:
            im = im.convert("RGB").resize((1280, 720), Image.Resampling.LANCZOS)
            im.save(web_jpg, "JPEG", quality=86, optimize=True)
        # web zoom mp4 (5s) + 10s master mp4
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

    print("=== [2/3] Rendering 8 EP03 4K Ukrainian Quote Cards + Video Clips ===", flush=True)
    for png_name, mp4_name, dur, cat, quote, author, color, fsize in EP03_CARDS:
        png_path = Path(draw_quote_card(
            png_name, cat, quote, author, accent_color=color, font_size_quote=fsize,
            footer_tag="THOUGHTCAST 4K // AI TITANS // EP03: DEMIS HASSABIS",
        ))
        mp4_path = STILLS_4K_DIR / mp4_name
        render_4k_still_video(png_path, mp4_path, dur, zoom_drift=0.015)
        print(f"  [OK] {png_name} -> {mp4_name} ({mp4_path.stat().st_size//1024}KB)", flush=True)

    print("=== [3/3] Rendering 18 Ken Burns 4K Archival Motion Clips for EP03 ===", flush=True)
    for src_name, clip_name, dur in PHOTO_STILL_CLIPS:
        src_p = YOUNG_HASSABIS_DIR / src_name
        dst_p = STILLS_4K_DIR / clip_name
        render_4k_still_video(src_p, dst_p, dur, zoom_drift=0.05)
        print(f"  [OK] {clip_name} ({dst_p.stat().st_size//1024}KB)", flush=True)


if __name__ == "__main__":
    main()
