#!/usr/bin/env python3
"""
Synchronizes EP03 (Demis Hassabis) curated global archives across:
  - 07_DASHBOARD/data/media_acquisition_pool.js (dossiers, archives, archival_photos)
  - 05_RAW_FOOTAGE/EP03_MEDIA_CATALOG.json & EP03_MEDIA_CATALOG.md
Verifies every single file path exists on disk before saving.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
MP_PATH = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"

DOSSIERS_EP03 = [
    {
        "id": "EP03_DOC_01",
        "ep": "03",
        "act": "ACT3",
        "timecode": "11:00–12:30",
        "title": "Nature 2016: Аномалія Ходу 37 та перемога AlphaGo над Лі Седолем",
        "source_label": "Nature 529, 484–489 (2016) • Match 2 vs. Lee Sedol 9p (March 10, 2016)",
        "highlight": "Game 2, Move 37 (Fifth-Line Shoulder Hit): Human probability calculated by policy network = 1 in 10,000 (0.01%). Lee Sedol leaves the board for 15 minutes in stunned silence.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_01_ACT3_AlphaGo_Move37_Nature_2016.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_01_alphago_nature.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_01.mp4",
    },
    {
        "id": "EP03_DOC_02",
        "ep": "03",
        "act": "ACT1",
        "timecode": "02:45–04:00",
        "title": "FIDE Ело 2300 у 13 років та 10-годинне прозріння у Ліхтенштейні (1990)",
        "source_label": "FIDE International Chess Rating Registry • London — Liechtenstein Open (1989–1990)",
        "highlight": "World #2 Under-14 behind Judit Polgár: looking around 300 sharp minds spending life on 64 squares and choosing instead to solve intelligence & cure disease.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_02_ACT1_Chess_Elo2300_Liechtenstein_1990.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_02_chess_elo2300.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_02.mp4",
    },
    {
        "id": "EP03_DOC_03",
        "ep": "03",
        "act": "ACT1",
        "timecode": "04:00–05:15",
        "title": "Bullfrog Theme Park (1994): Код 17-річного архітектора симуляцій",
        "source_label": "Bullfrog Productions Ltd. (Guildford) • Cambridge-Mandated Gap Year Project (1993–1994)",
        "highlight": "Accepted to Cambridge at 16, asked to wait 1 year -> co-designed & wrote AI core of Theme Park, proving simple local rules spawn living economic ecosystems.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_03_ACT1_Bullfrog_ThemePark_1994_Specs.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_03_themepark_1994.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_03.mp4",
    },
    {
        "id": "EP03_DOC_04",
        "ep": "03",
        "act": "ACT2",
        "timecode": "05:15–06:45",
        "title": "PNAS 2007 (UCL): Пацієнти з амнезією гіпокампа не здатні уявляти майбутнє",
        "source_label": "PNAS Vol. 104(5), 1726–1731 (Jan 2007) • Science Magazine Top 10 Breakthrough",
        "highlight": "Hassabis, Kumaran, Vann & Maguire proved memory & imagination share one hippocampal simulation engine — inspiring DeepMind's Experience Replay in DQN.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_04_ACT2_PNAS_Hippocampus_Imagination_2007.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_04_pnas_2007.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_04.mp4",
    },
    {
        "id": "EP03_DOC_05",
        "ep": "03",
        "act": "ACT3",
        "timecode": "14:15–16:45",
        "title": "Nature 2021 (CASP14): AlphaFold 2 та 200 мільйонів відкритих білків",
        "source_label": "Nature Vol. 596, 583–589 (15 July 2021) • Google DeepMind & EMBL-EBI Open DB",
        "highlight": "92.4 GDT_TS (~1.0 Å atomic accuracy) shattering biology's 50-year protein folding grand challenge; 200M+ structures gifted freely to humanity.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_05_ACT3_Nature_AlphaFold2_CASP14_2021.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_05_alphafold2_nature.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_05.mp4",
    },
    {
        "id": "EP03_DOC_06",
        "ep": "03",
        "act": "ACT4",
        "timecode": "16:45–21:30",
        "title": "Нобелівська премія з хімії 2024: Цифровий телескоп для вихідного коду життя",
        "source_label": "Kungl. Vetenskapsakademien (Stockholm, Dec 2024) • Demis Hassabis & John Jumper",
        "highlight": "“For protein structure prediction” — completing DeepMind's Step 2 mission statement and ushering in Isomorphic Labs digital biology.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP03_DOC_06_ACT4_Nobel_Chemistry_2024_Citation.png",
        "web_preview": "assets/dossiers_preview/ep03_doc_06_nobel_2024.jpg",
        "video_preview": "assets/video_previews/dossiers/EP03_DOC_06.mp4",
    },
]

ARCHIVES_EP03 = [
    {
        "code": "ARCH #01",
        "act": "Акт 4 (Стокгольм)",
        "timecode": "16:15–16:45",
        "tc": "16:15–16:45",
        "file": "EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024.mp4",
        "mp4_file": "EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024.mp4",
        "title": "Нобелівська лекція Деміса Гассабіса у Стокгольмі (2024)",
        "source": "Nobel Prize Official Channel (Stockholm, Dec 2024)",
        "url": "https://www.youtube.com/watch?v=YtPaZsasmNA",
        "section": "00:02:15-00:02:23",
        "note": "Деміс Гассабіс на трибуні Нобелівської лекції з хімії за AlphaFold.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_01_ACT4_24FPS_Hassabis_Nobel_Lecture_2024.mp4",
    },
    {
        "code": "ARCH #02",
        "act": "Акт 3 (Сеул • Хід 37)",
        "timecode": "11:00–11:45",
        "tc": "11:00–11:45",
        "file": "EP03_VID_ARCH_02_ACT3_24FPS_AlphaGo_Seoul_Move37_Reaction.mp4",
        "mp4_file": "EP03_VID_ARCH_02_ACT3_24FPS_AlphaGo_Seoul_Move37_Reaction.mp4",
        "title": "Реакція в Сеулі на легендарний Хід 37 (AlphaGo vs Lee Sedol)",
        "source": "Google DeepMind Official — AlphaGo Documentary",
        "url": "https://www.youtube.com/watch?v=WXuK6gekU1Y",
        "section": "00:51:20-00:51:28",
        "note": "Шок Лі Седоля та коментаторів у Сеулі після Ходу 37 на п'ятій лінії.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_02_ACT3_24FPS_AlphaGo_Seoul_Move37_Reaction.mp4",
    },
    {
        "code": "ARCH #03",
        "act": "Акт 1 (Шахи у 4 роки)",
        "timecode": "00:25–01:15",
        "tc": "00:25–01:15",
        "file": "EP03_VID_ARCH_03_ACT1_24FPS_Hassabis_Chess_Age4_WSJ.mp4",
        "mp4_file": "EP03_VID_ARCH_03_ACT1_24FPS_Hassabis_Chess_Age4_WSJ.mp4",
        "title": "Спогад Гассабіса: як у 4 роки переграв батька і дядька в шахи (WSJ)",
        "source": "Wall Street Journal Interview (YouTube Ea6ajW5hcCY)",
        "url": "https://www.youtube.com/watch?v=Ea6ajW5hcCY",
        "section": "00:00:36-00:00:52",
        "note": "«Вони підіграли мені жартома — але за два тижні я вже обігрував обох і очолив юнацькі збірні Англії».",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_03_ACT1_24FPS_Hassabis_Chess_Age4_WSJ.mp4",
    },
    {
        "code": "ARCH #04",
        "act": "Акт 1 (Дитячі турніри)",
        "timecode": "01:30–02:15",
        "tc": "01:30–02:15",
        "file": "EP03_VID_ARCH_04_ACT1_24FPS_Hassabis_Childhood_Chess_ThinkingGame.mp4",
        "mp4_file": "EP03_VID_ARCH_04_ACT1_24FPS_Hassabis_Childhood_Chess_ThinkingGame.mp4",
        "title": "Архівна хроніка дитинства: юний Деміс на турнірі Англія–США",
        "source": "Google DeepMind Official — The Thinking Game (d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:22:50-00:23:18",
        "note": "Реальна телехроніка 1980-х із богемної родини в Північному Лондоні й перемог на шахових дошках.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_04_ACT1_24FPS_Hassabis_Childhood_Chess_ThinkingGame.mp4",
    },
    {
        "code": "ARCH #05",
        "act": "Акт 1 (Гра за дошкою)",
        "timecode": "02:15–02:45",
        "tc": "02:15–02:45",
        "file": "EP03_VID_ARCH_05_ACT1_24FPS_Hassabis_Playing_Chess_Board.mp4",
        "mp4_file": "EP03_VID_ARCH_05_ACT1_24FPS_Hassabis_Playing_Chess_Board.mp4",
        "title": "Жива партія Деміса Гассабіса за шаховою дошкою (з Лексом Фрідманом)",
        "source": "Lex Fridman Chess Session (YouTube UbkB-vhjhHA)",
        "url": "https://www.youtube.com/watch?v=UbkB-vhjhHA",
        "section": "00:01:25-00:01:45",
        "note": "Фірмова концентрація та рухи рук шахового майстра над 64 клітинками.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_05_ACT1_24FPS_Hassabis_Playing_Chess_Board.mp4",
    },
    {
        "code": "ARCH #06",
        "act": "Акт 1 (Ліхтенштейн)",
        "timecode": "02:45–04:00",
        "tc": "02:45–04:00",
        "file": "EP03_VID_ARCH_06_ACT1_24FPS_Hassabis_Leaving_Chess_Realization.mp4",
        "mp4_file": "EP03_VID_ARCH_06_ACT1_24FPS_Hassabis_Leaving_Chess_Realization.mp4",
        "title": "Прозріння в 13 років: «Якщо скерувати ці 300 умів на лікування раку»",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:26:20-00:26:39",
        "note": "Момент рішення залишити професійну шахову кар'єру заради фундаментальної науки та ШІ.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_06_ACT1_24FPS_Hassabis_Leaving_Chess_Realization.mp4",
    },
    {
        "code": "ARCH #07",
        "act": "Акт 1 (Bullfrog 1994)",
        "timecode": "04:00–05:15",
        "tc": "04:00–05:15",
        "file": "EP03_VID_ARCH_07_ACT1_24FPS_Hassabis_Bullfrog_ThemePark_GapYear.mp4",
        "mp4_file": "EP03_VID_ARCH_07_ACT1_24FPS_Hassabis_Bullfrog_ThemePark_GapYear.mp4",
        "title": "Gap Year у 17 років: студія Bullfrog, Пітер Моліньє та культова Theme Park",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:39:17-00:39:44",
        "note": "Кембридж визнав його геній, але попросив почекати рік — і юнак написав культовий симулятор.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_07_ACT1_24FPS_Hassabis_Bullfrog_ThemePark_GapYear.mp4",
    },
    {
        "code": "ARCH #08",
        "act": "Акт 2 (Нейробіологія UCL)",
        "timecode": "05:15–06:45",
        "tc": "05:15–06:45",
        "file": "EP03_VID_ARCH_08_ACT2_24FPS_Hassabis_Neuroscience_Brain_Goal.mp4",
        "mp4_file": "EP03_VID_ARCH_08_ACT2_24FPS_Hassabis_Neuroscience_Brain_Goal.mp4",
        "title": "Чому Гассабіс пішов у когнітивну нейронауку досліджувати людський мозок",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:03:20-00:03:38",
        "note": "Єдиний працюючий прототип загального інтелекту у Всесвіті — біологічний гіпокамп.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_08_ACT2_24FPS_Hassabis_Neuroscience_Brain_Goal.mp4",
    },
    {
        "code": "ARCH #09",
        "act": "Акт 2 (DeepMind 2010)",
        "timecode": "06:45–08:15",
        "tc": "06:45–08:15",
        "file": "EP03_VID_ARCH_09_ACT2_24FPS_DeepMind_Solve_Intelligence_Plan.mp4",
        "mp4_file": "EP03_VID_ARCH_09_ACT2_24FPS_DeepMind_Solve_Intelligence_Plan.mp4",
        "title": "Бізнес-план 2010: «Крок 1 — Розв'язати інтелект, Крок 2 — Усе інше» (Stanford GSB)",
        "source": "Stanford Graduate School of Business (YouTube DsewHeVbL-0)",
        "url": "https://www.youtube.com/watch?v=DsewHeVbL-0",
        "section": "00:09:12-00:09:30",
        "note": "Спогад про венчурних інвесторів Лондона 2010 року, які не вірили у словосполучення AGI.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_09_ACT2_24FPS_DeepMind_Solve_Intelligence_Plan.mp4",
    },
    {
        "code": "ARCH #10",
        "act": "Акт 2 (Atari DQN)",
        "timecode": "08:15–09:00",
        "tc": "08:15–09:00",
        "file": "EP03_VID_ARCH_10_ACT2_24FPS_DeepMind_Atari_Breakout_Tunnel.mp4",
        "mp4_file": "EP03_VID_ARCH_10_ACT2_24FPS_DeepMind_Atari_Breakout_Tunnel.mp4",
        "title": "Прорив Atari Breakout: алгоритм сам відкриває тунель за стіною цеглин",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:11:36-00:11:58",
        "note": "Демонстрація глибокого навчання з підкріпленням (Deep Q-Network + Experience Replay).",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_10_ACT2_24FPS_DeepMind_Atari_Breakout_Tunnel.mp4",
    },
    {
        "code": "ARCH #11",
        "act": "Акт 2 (Етика Google $650M)",
        "timecode": "09:00–09:40",
        "tc": "09:00–09:40",
        "file": "EP03_VID_ARCH_11_ACT2_24FPS_Google_650M_Deal_Military_Ethics.mp4",
        "mp4_file": "EP03_VID_ARCH_11_ACT2_24FPS_Google_650M_Deal_Military_Ethics.mp4",
        "title": "Етичний ультиматум в угоді з Google (2014): заборона військового застосування",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "00:35:52-00:36:18",
        "note": "Обов'язкова умова продажу DeepMind Ларрі Пейджу — створення незалежної етичної ради.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_11_ACT2_24FPS_Google_650M_Deal_Military_Ethics.mp4",
    },
    {
        "code": "ARCH #12",
        "act": "Акт 3 (Сеул • Аналіз)",
        "timecode": "10:30–11:15",
        "tc": "10:30–11:15",
        "file": "EP03_VID_ARCH_12_ACT3_24FPS_AlphaGo_Move37_Fifth_Line_Shock.mp4",
        "mp4_file": "EP03_VID_ARCH_12_ACT3_24FPS_AlphaGo_Move37_Fifth_Line_Shock.mp4",
        "title": "Камінь на 5-й лінії: «Жодна людина у світі так би не зіграла» (AlphaGo)",
        "source": "Google DeepMind Official — AlphaGo Documentary (WXuK6gekU1Y)",
        "url": "https://www.youtube.com/watch?v=WXuK6gekU1Y",
        "section": "00:50:00-00:50:25",
        "note": "Пряма реакція гросмейстерів Го на порушення тисячолітньої канонічної геометрії гри.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_12_ACT3_24FPS_AlphaGo_Move37_Fifth_Line_Shock.mp4",
    },
    {
        "code": "ARCH #13",
        "act": "Акт 3 (200M білків)",
        "timecode": "14:45–15:45",
        "tc": "14:45–15:45",
        "file": "EP03_VID_ARCH_13_ACT3_24FPS_AlphaFold_200M_Proteins_Open_Data.mp4",
        "mp4_file": "EP03_VID_ARCH_13_ACT3_24FPS_AlphaFold_200M_Proteins_Open_Data.mp4",
        "title": "Рішення подарувати людству 200 мільйонів білкових структур безкоштовно",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "01:15:12-01:15:36",
        "note": "«Згорнімо абсолютно всі відомі науці білки на Землі та викладімо у відкритий доступ для кожного біолога».",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_13_ACT3_24FPS_AlphaFold_200M_Proteins_Open_Data.mp4",
    },
    {
        "code": "ARCH #14",
        "act": "Акт 3 (CBS 60 Minutes)",
        "timecode": "15:45–16:15",
        "tc": "15:45–16:15",
        "file": "EP03_VID_ARCH_14_ACT3_24FPS_AlphaFold_Protein_Fold_60Minutes.mp4",
        "mp4_file": "EP03_VID_ARCH_14_ACT3_24FPS_AlphaFold_Protein_Fold_60Minutes.mp4",
        "title": "Репортаж CBS 60 Minutes: від менше ніж 1% до 200M структур за один рік",
        "source": "CBS 60 Minutes — Google DeepMind London (YouTube 1XF-NG_35NE)",
        "url": "https://www.youtube.com/watch?v=1XF-NG_35NE",
        "section": "00:10:05-00:10:42",
        "note": "Лондонська студія DeepMind, тривимірна візуалізація білків та прискорення відкриття ліків.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_14_ACT3_24FPS_AlphaFold_Protein_Fold_60Minutes.mp4",
    },
    {
        "code": "ARCH #15",
        "act": "Акт 4 (CASP14 Лекція)",
        "timecode": "14:15–14:45",
        "tc": "14:15–14:45",
        "file": "EP03_VID_ARCH_15_ACT4_24FPS_Nobel_Lecture_CASP14_Atomic_Accuracy.mp4",
        "mp4_file": "EP03_VID_ARCH_15_ACT4_24FPS_Nobel_Lecture_CASP14_Atomic_Accuracy.mp4",
        "title": "Нобелівська лекція 2024: стрибок AlphaFold 1 → AlphaFold 2 до ширини атома",
        "source": "Nobel Prize Official Channel (Stockholm, YouTube YtPaZsasmNA)",
        "url": "https://www.youtube.com/watch?v=YtPaZsasmNA",
        "section": "00:14:20-00:14:46",
        "note": "Демонстрація на сцені Стокгольма графіка історичного прориву CASP13–CASP14.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_15_ACT4_24FPS_Nobel_Lecture_CASP14_Atomic_Accuracy.mp4",
    },
    {
        "code": "ARCH #16",
        "act": "Акт 4 (Фінал AGI)",
        "timecode": "17:30–18:15",
        "tc": "17:30–18:15",
        "file": "EP03_VID_ARCH_16_ACT4_24FPS_Hassabis_AGI_Horizon_Life_Moment.mp4",
        "mp4_file": "EP03_VID_ARCH_16_ACT4_24FPS_Hassabis_AGI_Horizon_Life_Moment.mp4",
        "title": "Фінальне одкровення Гассабіса: «AGI на горизонті — це мить, заради якої я жив»",
        "source": "The Thinking Game Documentary (YouTube d95J8yzvjbQ)",
        "url": "https://www.youtube.com/watch?v=d95J8yzvjbQ",
        "section": "01:19:50-01:20:16",
        "note": "Відповідальність за покоління майбутнього та підсумок шляху від шахової дошки до телескопа науки.",
        "video_preview": "assets/video_previews/archives/EP03_VID_ARCH_16_ACT4_24FPS_Hassabis_AGI_Horizon_Life_Moment.mp4",
    },
]

ARCHIVAL_PHOTOS_EP03 = [
    ("EP03_PH_01", "ФОТО #01 (1976–1980)", "Північний Лондон • East Finchley High Road (дитинство Деміса)",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:East_Finchley_High_Road_geograph-2988922-by-Ben-Brooksbank.jpg",
     "EP03_IMG_ARCH_01_North_London_Finchley_Youth_Era.jpg",
     "Архівна вулиця East Finchley у Північному Лондоні — середовище юності сина кіпрського митця та сінгапурської матері."),
    ("EP03_PH_02", "ФОТО #02 (1980)", "Турнірна дерев'яна шахівниця Staunton — космос із 64 клітинок",
     "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Chess_game_Staunton_No._6_perfil_view_8.jpg",
     "EP03_IMG_ARCH_02_Staunton_Chess_Board_Strategy.jpg",
     "Острів абсолютного порядку, з якого у 4 роки почалося формування математичного дерева рішень Гассабіса."),
    ("EP03_PH_03", "ФОТО #03 (1984–1990)", "Механічний шаховий годинник Garde юніорських турнірів ФІДЕ",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Garde-chess-clock.jpg",
     "EP03_IMG_ARCH_03_Garde_Mechanical_Chess_Clock.jpg",
     "Класичний механічний таймер міжнародних юніорських турнірів, де Гассабіс здобув рейтинг Ело 2300."),
    ("EP03_PH_04", "ФОТО #04 (1984)", "Перший мікрокомп'ютер Sinclair ZX Spectrum 48K (куплений за шахові призові)",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Sinclair_ZX_Spectrum_48k_(7160141482).jpg",
     "EP03_IMG_ARCH_04_Sinclair_ZX_Spectrum_48K_1984.jpg",
     "Легендарний 8-бітний домашній комп'ютер, що породив перше порівняння біологічної інтуїції та кремнієвого перебору."),
    ("EP03_PH_05", "ФОТО #05 (1985)", "Гумова клавіатура ZX Spectrum 48K та перші ігрові програми на Z80",
     "Wikimedia Commons (CC BY-SA 2.5)", "https://commons.wikimedia.org/wiki/File:ZXSpectrum48k.jpg",
     "EP03_IMG_ARCH_05_ZX_Spectrum_48K_Keyboard_Detail.jpg",
     "Машинна платформа перших експериментів 8-річного програміста зі створенням штучного гравця в реверсі."),
    ("EP03_PH_06", "ФОТО #06 (1994–1997)", "Історична брама Queens' College, Кембридж — Double First з інформатики",
     "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:Cambridge_Queens%27_Gatehouse.JPG",
     "EP03_IMG_ARCH_06_Queens_College_Cambridge_Gatehouse.jpg",
     "Коледж Кембриджського університету, який ухвалив рішення прийняти геніального 16-річного студента."),
    ("EP03_PH_07", "ФОТО #07 (1995–1997)", "Математичний міст над річкою Кем у Queens' College",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Queens%27_College_-_Mathematical_Bridge.jpg",
     "EP03_IMG_ARCH_07_Queens_College_Mathematical_Bridge.jpg",
     "Символ геометричної інженерії та університетських років перед заснуванням Elixir Studios."),
    ("EP03_PH_08", "ФОТО #08 (2005–2009)", "Університетський коледж Лондона (UCL) — PhD з когнітивної нейробіології",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:UCL_Main_Building_-_UCL_Illuminated.jpg",
     "EP03_IMG_ARCH_08_UCL_Main_Quad_Cognitive_Neuroscience.jpg",
     "Альма-матер дослідження пацієнтів з амнезією гіпокампа (PNAS 2007), що відкрило зв'язок пам'яті та уяви."),
    ("EP03_PH_09", "ФОТО #09 (2014)", "Виступ Деміса Гассабіса на старті епохи DeepMind поруч зі Space Invaders (Atari DQN)",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:PhotonQ-Demis_Hassabis_on_Artificial_Playful_Intelligence_(15366514658)_(2).jpg",
     "EP03_IMG_ARCH_09_Demis_Hassabis_DeepMind_Early_Talk_2014.jpg",
     "Автентичний ранній кадр із доповіді «Artificial Playful Intelligence» на тлі піксельної гри Atari."),
    ("EP03_PH_10", "ФОТО #10 (Лондон)", "Штаб-квартира Google DeepMind на 6 Pancras Square (King's Cross, Лондон)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Google-Deep_Mind_headquarters_in_London,_6_Pancras_Square.jpg",
     "EP03_IMG_ARCH_10_DeepMind_London_HQ_Kings_Cross.jpg",
     "Серце європейської науки про штучний інтелект у Лондоні, де об'єдналися команди AlphaGo та AlphaFold."),
    ("EP03_PH_11", "ФОТО #11 (2016)", "Традиційний дерев'яний гобан із базальтовими каменями Го",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Go_--_2021_--_6732.jpg",
     "EP03_IMG_ARCH_11_Goban_Board_Go_Move37_Strategy.jpg",
     "10^170 комбінацій на перетинах ліній — арена, де у березні 2016 року AlphaGo зіграла легендарний Хід 37."),
    ("EP03_PH_12", "ФОТО #12 (2014–2016)", "Деміс Гассабіс за трибуною EPFL у роки тріумфу DeepMind",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Demis_Hassabis.jpg",
     "EP03_IMG_ARCH_12_Demis_Hassabis_DeepMind_Era_Portrait.jpg",
     "Лекція співзасновника DeepMind про архітектуру загального інтелекту та фундаментальні ігри."),
    ("EP03_PH_13", "ФОТО #13 (2020–2022)", "3D-модель згортання білка ZNF555 з бази AlphaFold",
     "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:AlphaFold_ZNF555_Protein_Structure.png",
     "EP03_IMG_ARCH_13_AlphaFold_ZNF555_Protein_Structure.jpg",
     "Точна тривимірна геометрія білкових спіралей, передбачена системою штучного інтелекту DeepMind."),
    ("EP03_PH_14", "ФОТО #14 (2021 • Nature)", "Архітектура Evoformer у системі AlphaFold 2 та графік перемоги на CASP14",
     "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:AlphaFold_2.png",
     "EP03_IMG_ARCH_14_AlphaFold2_Transformer_Architecture.jpg",
     "Наукова діаграма революції 92.4 GDT_TS, що зробила можливим відкриття 200M білкових структур."),
    ("EP03_PH_15", "ФОТО #15 (2018)", "Королівське наукове товариство Великої Британії (6-9 Carlton House Terrace, Лондон)",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:The_Royal_Society_(geograph_5899669).jpg",
     "EP03_IMG_ARCH_15_Royal_Society_London_Carlton_Terrace.jpg",
     "Історичний осідок британської науки (Royal Society FRS), членом якого Деміса Гассабіса обрали у 2018 році."),
    ("EP03_PH_16", "ФОТО #16 (Грудень 2024)", "Нобелівська лекція Деміса Гассабіса в Шведській королівській академії наук",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Demis_Hassabis_at_the_2024_Nobel_Lectures_2.jpg",
     "EP03_IMG_ARCH_16_Nobel_Lectures_2024_Hassabis_Stockholm.jpg",
     "Історичний виступ у Стокгольмі (Kungl. Vetenskapsakademien) на тему прискорення наукових відкриттів через ШІ."),
    ("EP03_PH_17", "ФОТО #17 (Грудень 2024)", "Лауреати Нобелівської премії з хімії 2024: Девід Бейкер, Деміс Гассабіс, Джон Джампер",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:David_Baker,_Demis_Hassabis,_and_John_Jumper_at_2024_Nobel_Prize_Conference.jpg",
     "EP03_IMG_ARCH_17_Nobel_2024_Laureates_Hassabis_Jumper_Baker.jpg",
     "Три архітектори цифрової революції в біохімії та дизайні білків на пресконференції в Стокгольмі."),
    ("EP03_PH_18", "ФОТО #18 (Грудень 2024)", "Деміс Гассабіс під час Нобелівського тижня в Стокгольмі (крупний портрет)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Demis_Hassabis_at_2024_Nobel_Week_2.jpg",
     "EP03_IMG_ARCH_18_Demis_Hassabis_Nobel_Week_2024_Portrait.jpg",
     "Фінальний живий кадр Нобелівського лауреата — синтез інтелекту шахіста, нейробіолога й першовідкривача."),
]


def verify_paths():
    missing = []
    for d in DOSSIERS_EP03:
        if not (ROOT / d["raw_4k_png"]).exists():
            missing.append(d["raw_4k_png"])
        for k in ["web_preview", "video_preview"]:
            if not (ROOT / "07_DASHBOARD" / d[k]).exists():
                missing.append("07_DASHBOARD/" + d[k])
    for a in ARCHIVES_EP03:
        if not (ROOT / "05_RAW_FOOTAGE" / "archives" / a["mp4_file"]).exists():
            missing.append("05_RAW_FOOTAGE/archives/" + a["mp4_file"])
        if not (ROOT / "07_DASHBOARD" / a["video_preview"]).exists():
            missing.append("07_DASHBOARD/" + a["video_preview"])
    for item in ARCHIVAL_PHOTOS_EP03:
        fn = item[5]
        if not (ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_hassabis" / fn).exists():
            missing.append("young_hassabis/" + fn)
        if not (ROOT / "07_DASHBOARD" / "assets" / "archival_photos" / fn).exists():
            missing.append("archival_photos/" + fn)
    if missing:
        raise RuntimeError("Missing verified files:\n  " + "\n  ".join(missing))


def main():
    verify_paths()
    raw = MP_PATH.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    mp = json.loads(raw[len(prefix):].rstrip(";\n "))

    ep03 = mp["03"]
    ep03["dossiers"] = DOSSIERS_EP03
    ep03["archives"] = ARCHIVES_EP03
    ep03["archival_photos"] = [
        {
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_hassabis/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        }
        for (pid, code, title, src, url, fn, desc) in ARCHIVAL_PHOTOS_EP03
    ]

    MP_PATH.write_text(prefix + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

    ua_cards = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP03_*.png"))
    still_clips = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k").glob("EP03_*.mp4"))
    cat_json = {
        "episode": "EP03 — Demis Hassabis",
        "updated_at": "2026-11-10",
        "summary": {
            "archival_broll_mp4": len(ARCHIVES_EP03),
            "archival_photos": len(ARCHIVAL_PHOTOS_EP03),
            "uhd_4k_dossiers": len(DOSSIERS_EP03),
            "ukrainian_4k_quote_cards": len(ua_cards),
            "ken_burns_and_card_4k_mp4": len(still_clips),
        },
        "dossiers": DOSSIERS_EP03,
        "archives": ARCHIVES_EP03,
        "archival_photos": ep03["archival_photos"],
        "ukrainian_4k_quote_cards": ua_cards,
        "rendered_cinematic_stills_4k": still_clips,
    }
    (ROOT / "05_RAW_FOOTAGE" / "EP03_MEDIA_CATALOG.json").write_text(json.dumps(cat_json, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP03 (Деміс Гассабіс)",
        "",
        f"- **📼 Реальні архівні відеокліпи B-Roll (`05_RAW_FOOTAGE/archives/`):** {len(ARCHIVES_EP03)}",
        f"- **📸 Історичні фото та наукові артефакти (`05_RAW_FOOTAGE/speaker_portraits/young_hassabis/`):** {len(ARCHIVAL_PHOTOS_EP03)}",
        f"- **🗂️ 4K Документальні досьє-пластини (`05_RAW_FOOTAGE/dossiers_press/`):** {len(DOSSIERS_EP03)}",
        f"- **🇺🇦 4K Українські цитат-картки (`ukrainian_quote_cards/`):** {len(ua_cards)}",
        f"- **🎞️ Ken Burns 4K відеокліпи зі стілів і карток (`rendered_cinematic_stills_4k/`):** {len(still_clips)}",
        "",
        "## 📼 Архівні відеокліпи (`EP03_VID_ARCH_01..16`)",
        "",
        "| Код | Таймкод EP03 | Файл | Джерело |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for a in ARCHIVES_EP03:
        md.append(f"| **{a['code']}** | `{a['timecode']}` | `{a['mp4_file']}` | {a['source']} |")
    md += ["", "## 📸 Хронологічні архівні фото (`EP03_IMG_ARCH_*`)", "", "| Код | Файл | Ліцензія / Джерело |", "| :--- | :--- | :--- |"]
    for p in ep03["archival_photos"]:
        md.append(f"| **{p['code']}** | `{p['raw_file'].split('/')[-1]}` | [{p['source']}]({p['url']}) |")
    (ROOT / "05_RAW_FOOTAGE" / "EP03_MEDIA_CATALOG.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"[✓] EP03 synced: {len(DOSSIERS_EP03)} dossiers, {len(ARCHIVES_EP03)} archival videos, {len(ARCHIVAL_PHOTOS_EP03)} archival photos, {len(ua_cards)} UA cards, {len(still_clips)} 4K motion clips!")


if __name__ == "__main__":
    main()
