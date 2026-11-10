#!/usr/bin/env python3
"""
EP07 Dario Amodei — Media Ecosystem Sync:
- Registers all 6 4K Dossiers (EP07_DOC_01..06), 16 HD Archival Video Clips (EP07_VID_ARCH_01..16),
  18 Curated Wikimedia Archival Photos (EP07_IMG_ARCH_01..18), 5 2K Flow Keyframes, and 8 4K UA Quote Cards
  into 07_DASHBOARD/data/media_acquisition_pool.js.
- Generates 05_RAW_FOOTAGE/EP07_MEDIA_CATALOG.json & 05_RAW_FOOTAGE/EP07_MEDIA_CATALOG.md.
- Syncs 08_METADATA/EP07_DARIO_AMODEI/manifest.json with rich milestone & media telemetry.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
POOL_JS = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"
FOOTAGE_DIR = ROOT / "05_RAW_FOOTAGE"
META_DIR = ROOT / "08_METADATA" / "EP07_DARIO_AMODEI"
META_DIR.mkdir(parents=True, exist_ok=True)

EP07_DOSSIERS = [
    {
        "id": "EP07_DOC_01",
        "ep": "07",
        "act": "ACT3",
        "timecode": "10:30–11:50",
        "title": "Constitutional AI & Responsible Scaling Thresholds",
        "source_label": "Anthropic Public Benefit Corporation • Responsible Scaling Policy (ASL-1 → ASL-4)",
        "highlight": "Mandatory Hard Stop Commitment: Frontier training and deployment pause immediately if red-team evaluations cross ASL-3 / ASL-4 CBRN bioweapon uplift or autonomous replication thresholds before verifiable containment exists.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_01_ACT3_Amodei_Constitutional_AI_2022.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_01_amodei_cai.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_01.mp4",
    },
    {
        "id": "EP07_DOC_02",
        "ep": "07",
        "act": "ACT1",
        "timecode": "00:25–02:45",
        "title": "Шкіра батька, втрата 2006 року та біофізика сітківки (Принстон 2011)",
        "source_label": "Stanford BS Physics (2006) • Princeton PhD Biophysics Dissertation (2011)",
        "highlight": "Before trying to align silicon intelligence, I spent five years listening to living neurons inside the retina fire across multi-electrode arrays.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_02_ACT1_sf_leather_princeton_retina_2011.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_02_princeton_retina.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_02.mp4",
    },
    {
        "id": "EP07_DOC_03",
        "ep": "07",
        "act": "ACT2",
        "timecode": "04:15–06:30",
        "title": "Закони масштабу (2020): Пряма лінія крізь 7 порядків L(N, D, C)",
        "source_label": "Kaplan, McCandlish & Amodei et al. • Scaling Laws for Neural Language Models (arXiv:2001.08361)",
        "highlight": "Intelligence obeys smooth empirical power laws: scale compute, dataset size, and parameters in harmony, and loss drops along a straight line across seven orders of magnitude.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_03_ACT2_scaling_laws_7orders_openai_2020.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_03_scaling_laws_2020.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_03.mp4",
    },
    {
        "id": "EP07_DOC_04",
        "ep": "07",
        "act": "ACT2",
        "timecode": "06:30–09:15",
        "title": "Тихий вихід сімох дослідників 2020: Anthropic PBC та Клод Шеннон",
        "source_label": "Anthropic Public Benefit Corporation Charter & Long-Term Benefit Trust (2021)",
        "highlight": "We left so that racing for capability could never silently silence safety research — incorporating safety into the company charter and naming Claude after Claude Shannon.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_04_ACT2_silent_exit_anthropic_shannon_2021.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_04_anthropic_pbc_2021.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_04.mp4",
    },
    {
        "id": "EP07_DOC_05",
        "ep": "07",
        "act": "ACT3",
        "timecode": "10:15–14:30",
        "title": "Конституційний ШІ (RLAIF) & Механістична інтерпретованість (травень 2024)",
        "source_label": "arXiv:2212.08073 & Transformer Circuits: Scaling Monosemanticity in Claude 3 Sonnet",
        "highlight": "Mechanistic interpretability builds a microscope into the neurobiology of silicon minds — illuminating features inside Claude 3 Sonnet before deployment.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_05_ACT3_constitutional_ai_mech_interp_2024.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_05_cai_interp_2024.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_05.mp4",
    },
    {
        "id": "EP07_DOC_06",
        "ep": "07",
        "act": "ACT4",
        "timecode": "16:00–21:15",
        "title": "Протоколи зупинки ASL-1..4 та маніфест «Машини благодаті» (10.2024)",
        "source_label": "US Senate Judiciary Hearing (25.07.2023) & Essay «Machines of Loving Grace»",
        "highlight": "Compress a century of biological and medical progress into 5–10 years — eliminating infectious diseases and cutting cancer deaths in half.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP07_DOC_06_ACT4_asl_biosecurity_machines_loving_grace.png",
        "web_preview": "assets/dossiers_preview/ep07_doc_06_asl_loving_grace_2025.jpg",
        "video_preview": "assets/video_previews/dossiers/EP07_DOC_06.mp4",
    },
]

EP07_ARCHIVES = [
    ("ARCH #01", "Акт 3 (Сенат США • 2023)", "11:05–11:13", "EP07_VID_ARCH_01_ACT3_24FPS_Amodei_Senate_Biosecurity_Hearing.mp4",
     "Свідчення Даріо Амодея у Сенаті США щодо біобезпеки ШІ",
     "US Senate Judiciary Hearing (yBgvqGrJ3g8)", "https://www.youtube.com/watch?v=yBgvqGrJ3g8", "00:36:15-00:36:23",
     "Даріо Амодей свідчить у Сенаті США про ризики біологічних загроз та обов'язкові тести перед релізом."),
    ("ARCH #02", "Акт 1 (Принстон • Біофізика)", "01:40–02:10", "EP07_VID_ARCH_02_ACT1_24FPS_Amodei_Biophysics_Physics_Path_Lex452.mp4",
     "Шлях від бакалаврату фізики до біофізики нейромереж та 1/f-шуму",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "00:08:58-00:09:26",
     "Даріо Амодей згадує власну кар'єру фізика й біофізика в аспірантурі та зв'язок фізичних розподілів зі ШІ."),
    ("ARCH #03", "Акт 1 (Baidu 2014 • Deep Speech)", "02:50–03:20", "EP07_VID_ARCH_03_ACT1_24FPS_Amodei_Baidu_DeepSpeech_Scaling_Lex452.mp4",
     "Вхід у світ ШІ в команді Baidu з Ендрю Ином наприкінці 2014 року",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "00:03:25-00:03:54",
     "Спогад про перші системи розпізнавання мовлення і ранні скептичні суперечки про брак алгоритмів."),
    ("ARCH #04", "Акт 2 (OpenAI VP • Суцкевер)", "04:00–04:45", "EP07_VID_ARCH_04_ACT2_24FPS_Amodei_Ilya_Models_Want_Learn_LexClip.mp4",
     "Роки на посаді VP Research OpenAI: дзен-коан Суцкевера про масштабування",
     "Lex Fridman Clips (FzkCLR378fE)", "https://www.youtube.com/watch?v=FzkCLR378fE", "00:00:13-00:00:46",
     "Амодей згадує роботу поряд з Іллею Суцкевером та фразу «The models just want to learn»."),
    ("ARCH #05", "Акт 2 (Закони масштабу)", "04:50–05:35", "EP07_VID_ARCH_05_ACT2_24FPS_Amodei_Scaling_Power_Laws_Dwarkesh2024.mp4",
     "Чому степеневі закони фізики пояснюють передбачуваність зростання ШІ",
     "Dwarkesh Patel 2024 (Nlkk3glap_U)", "https://www.youtube.com/watch?v=Nlkk3glap_U", "00:01:36-00:02:14",
     "Амодей пояснює, як кожен логарифмічний порядок величини обчислень відкриває нові кореляції у даних."),
    ("ARCH #06", "Акт 2 (GPT-2 -> GPT-3)", "05:35–06:20", "EP07_VID_ARCH_06_ACT2_24FPS_Amodei_Scaling_Smoothness_GPT3_Dwarkesh2024.mp4",
     "Плавність степеневої прямої та перехід від GPT-2 до появи вміння кодити",
     "Dwarkesh Patel 2024 (Nlkk3glap_U)", "https://www.youtube.com/watch?v=Nlkk3glap_U", "00:03:38-00:04:12",
     "Порівняння передбачуваності середніх кліматичних кривих і раптового прориву конкретних здібностей."),
    ("ARCH #07", "Акт 2 (Вихід з OpenAI 2020)", "06:40–07:25", "EP07_VID_ARCH_07_ACT2_24FPS_Amodei_Why_Left_OpenAI_Vision_LexClip.mp4",
     "Чому Даріо Амодей та команда безпеки тихо пішли з OpenAI",
     "Lex Fridman Clips (FzkCLR378fE)", "https://www.youtube.com/watch?v=FzkCLR378fE", "00:03:26-00:04:06",
     "Пряме спростування чуток про Microsoft і пояснення рішення створити власний чесний експеримент."),
    ("ARCH #08", "Акт 2 (Anthropic PBC • Візія)", "07:25–08:20", "EP07_VID_ARCH_08_ACT2_24FPS_Amodei_Race_To_The_Top_Anthropic_LexClip.mp4",
     "«Перегони вгору» замість гонитви на дно — принцип впливу через продукт",
     "Lex Fridman Clips (FzkCLR378fE)", "https://www.youtube.com/watch?v=FzkCLR378fE", "00:06:00-00:06:34",
     "Амодей формулює стратегію Anthropic: змусити всю індустрію копіювати високі стандарти безпеки."),
    ("ARCH #09", "Акт 2 (Співзасновники Anthropic)", "08:20–09:10", "EP07_VID_ARCH_09_ACT2_24FPS_Amodei_Cofounders_GPT2_Safety_BuildingAnthropic.mp4",
     "Співзасновники про «згусток дослідників», які стояли за GPT-2, Scaling і GPT-3",
     "Anthropic Official (om2lIWXLLN4)", "https://www.youtube.com/watch?v=om2lIWXLLN4", "00:02:06-00:02:40",
     "Розмова співзасновників про поєднання величезних обчислень і науки безпеки з першого дня."),
    ("ARCH #10", "Акт 3 (Народження CAI)", "10:15–11:05", "EP07_VID_ARCH_10_ACT3_24FPS_Amodei_Constitutional_AI_Origin_BuildingAnthropic.mp4",
     "Як на старті Anthropic народилася ідея написати Конституцію для Claude",
     "Anthropic Official (om2lIWXLLN4)", "https://www.youtube.com/watch?v=om2lIWXLLN4", "00:06:00-00:06:32",
     "Живий спогад про ранню ідею Джареда Каплана керувати поведінкою LLM через відкриту Конституцію."),
    ("ARCH #11", "Акт 3 (RLAIF Принципи)", "11:15–12:10", "EP07_VID_ARCH_11_ACT3_24FPS_Amodei_Constitutional_AI_Principles_Lex452.mp4",
     "Конституційний ШІ як прозорий кодекс принципів і самонавчання",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "01:53:40-01:54:18",
     "Даріо Амодей особисто пояснює Конституційний ШІ як цикл самокритики та інтерпретованості."),
    ("ARCH #12", "Акт 3 (Мікроскоп Кріса Ола)", "12:15–13:15", "EP07_VID_ARCH_12_ACT3_24FPS_Amodei_ChrisOlah_Mech_Interp_Lex452.mp4",
     "Кріс Ола і чотирирічна ставка на механістичну інтерпретованість без комерції",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "00:21:25-00:22:02",
     "Історія підтримки фундаментальних досліджень нейробіології ШІ всередині Anthropic."),
    ("ARCH #13", "Акт 4 (Пороги ASL-1..4)", "14:40–15:30", "EP07_VID_ARCH_13_ACT4_24FPS_Amodei_ASL_Levels_Cofounders_BuildingAnthropic.mp4",
     "Політика відповідального масштабування (RSP): рівні тривоги ASL-2 та ASL-3",
     "Anthropic Official (om2lIWXLLN4)", "https://www.youtube.com/watch?v=om2lIWXLLN4", "00:29:28-00:29:54",
     "Про переведення безпеки з вузького технократичного жаргону в прозору систему порогів компанії."),
    ("ARCH #14", "Акт 4 (Сенат 2023 • Свідчення)", "15:30–16:40", "EP07_VID_ARCH_14_ACT4_24FPS_Amodei_Senate_Testimony_Human_Level_Risks.mp4",
     "Вступна промова Даріо Амодея у Сенаті США про Anthropic PBC і CAI",
     "US Senate Judiciary (yBgvqGrJ3g8)", "https://www.youtube.com/watch?v=yBgvqGrJ3g8", "00:19:02-00:19:38",
     "Амодей представляє сенаторам Конституційний ШІ, red teaming та інтерпретованість моделей."),
    ("ARCH #15", "Акт 4 (Ризики CBRN)", "16:45–17:55", "EP07_VID_ARCH_15_ACT4_24FPS_Amodei_Catastrophic_CBRN_Risks_Lex452.mp4",
     "Головний пріоритет захисту: недопущення зловживань у кібер- та біозброї",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "00:55:48-00:56:20",
     "Детальна позиція Амодея про те, чому запобігання ризикам CBRN важливіше за ринкові перегони."),
    ("ARCH #16", "Акт 4 (Машини благодаті • Рак)", "18:30–20:30", "EP07_VID_ARCH_16_ACT4_24FPS_Amodei_Cancer_DNA_Microscopes_Biology_Lex452.mp4",
     "Три мільярди пар ДНК, рак і «нові мікроскопи» для прискорення біології",
     "Lex Fridman #452 (ugvHCXCOmm4)", "https://www.youtube.com/watch?v=ugvHCXCOmm4", "02:23:12-02:23:48",
     "Філософія «Machines of Loving Grace»: надінтелект як універсальний мікроскоп для медицини."),
]

EP07_PHOTOS = [
    ("EP07_PH_01", "ФОТО #01 (1983 • Сан-Франциско)", "Вікторіанські квартали Сан-Франциско — місто народження Даріо Амодея (1983)", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Painted_Ladies_San_Francisco_January_2013_panorama_2.jpg", "ep07_img_arch_01_san_francisco_victorian_childhood_era.jpg", "Панорама класичних вікторіанських будинків Сан-Франциско, де в 1983 році в районі Мішн народився Даріо Амодей."),
    ("EP07_PH_02", "ФОТО #02 (Спадщина батька)", "Тосканські інструменти ремісника шкіри — майстерність батька Ріккардо Амодея", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Leather_working_tools_(DSC08329).jpg", "ep07_img_arch_02_tuscan_leather_working_tools.jpg", "Традиційні шкіряні ножі, шило та молоток на дубовому столі — символ ремісничої точності італійського батька Даріо."),
    ("EP07_PH_03", "ФОТО #03 (2006 • Стенфорд)", "Головний квад Стенфордського університету — бакалавр фізики (2006)", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Stanford_University_Main_Quad_May_2011_001.jpg", "ep07_img_arch_03_stanford_university_physics_quad.jpg", "Пісковикові аркади й вежа Гувера у Стенфорді, де Амодей завершив бакалаврат із фізики в рік утрати батька."),
    ("EP07_PH_04", "ФОТО #04 (2006–2011 • Принстон)", "Лабораторія Карла Айкана (Принстон) — центр інтегративної біофізики та нейрогеноміки", "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Carl_Icahn_Laboratory_-_Princeton_University_-_Princeton,_NJ_-_DSC00952.jpg", "ep07_img_arch_04_princeton_carl_icahn_biophysics_lab.jpg", "Дослідницький кампус Принстонського університету епохи докторської роботи Амодея на стику фізики та біології мозку."),
    ("EP07_PH_05", "ФОТО #05 (2011 • Jadwin Hall)", "Фізичний корпус Jadwin Hall у Принстоні (PhD з електрофізіології, 2011)", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Jadwin_Hall_At_Princeton_University_2024_011.jpg", "ep07_img_arch_05_princeton_jadwin_hall_physics.jpg", "Академічний осередок фізичного департаменту Принстона, де Амодей захистив дисертацію як стипендіат Hertz Fellowship."),
    ("EP07_PH_06", "ФОТО #06 (Сітківка • 50x RGC)", "Мікроскопія гангліозних нейронів сітківки ока — об'єкт дисертації Амодея", "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:50x_RGC_axotomy_1_day.png", "ep07_img_arch_06_retinal_ganglion_neurons_microscopy.jpg", "Радіальна мережа аксонів живих нейронів сітківки під мікроскопом 50x — природний біокомп'ютер."),
    ("EP07_PH_07", "ФОТО #07 (2014–2015 • Baidu)", "Штаб-квартира Baidu — лабораторія глибокого навчання (Deep Speech 2)", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Baidu_headquarters_at_Shangdi_(20220509111808).jpg", "ep07_img_arch_07_baidu_headquarters_shangdi.jpg", "Перша індустріальна AI-лабораторія в кар'єрі Амодея поряд з Ендрю Ином у 2014–2015 роках."),
    ("EP07_PH_08", "ФОТО #08 (2015–2016 • Google)", "Корпус №43 Googleplex у Маунтін-В'ю — ера Google Brain та безпекового напряму", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Googleplex_building_43.jpg", "ep07_img_arch_08_googleplex_building43_brain_era.jpg", "Роки у Google Brain, де Даріо Амодей став співавтором основоположної статті «Concrete Problems in AI Safety»."),
    ("EP07_PH_09", "ФОТО #09 (2016–2020 • OpenAI)", "Pioneer Building у Сан-Франциско — штаб раннього OpenAI (VP of Research)", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Pioneer_Building,_San_Francisco_(2019)_-1.jpg", "ep07_img_arch_09_openai_pioneer_building_sf.jpg", "Будівля в районі Мішн у Сан-Франциско, де Амодей керував науковим напрямом GPT-2, GPT-3 та RLHF."),
    ("EP07_PH_10", "ФОТО #10 (2020 • Масштаб)", "Рідинно-охолоджувана плата прискорювачів Google TPU v3 — апаратний рушій Scaling Laws", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Tensor_Processing_Unit_3.0.jpg", "ep07_img_arch_10_google_tpu_v3_scaling_laws_pod.jpg", "Кристали та мідне охолодження спеціалізованих чипів, що втілили відкриття законів масштабу."),
    ("EP07_PH_11", "ФОТО #11 (Клод Шеннон)", "Архівний портрет Клода Шеннона — натхнення для імені моделі Claude", "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:C.E._Shannon._Tekniska_museet_43069.jpg", "ep07_img_arch_11_claude_shannon_information_theory.jpg", "Засновник теорії інформації та автор ентропії Шеннона, на честь якого Anthropic назвала своє сімейство моделей."),
    ("EP07_PH_12", "ФОТО #12 (Anthropic HQ SF)", "Хмарочос на 500 Howard Street у Сан-Франциско — штаб-квартира Anthropic PBC", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Slack_offices,_Howard_Street,_San_Francisco_(viewed_from_the_south-west,_January_2020).jpg", "ep07_img_arch_12_anthropic_howard_street_sf_hq.jpg", "Офісний центр у серці SoMa, куди переїхала команда дослідників безпеки Anthropic."),
    ("EP07_PH_13", "ФОТО #13 (Білий дім • 2023)", "Історичний саміт керівників ШІ у Білому домі (4 травня 2023)", "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:V20230504LJ-0199-2.jpg", "ep07_img_arch_13_white_house_ai_ceo_summit_2023.jpg", "Даріо Амодей за круглим столом Білого дому поруч із віцепрезиденткою Гарріс, Семом Альтманом і Сатьєю Наделлою."),
    ("EP07_PH_14", "ФОТО #14 (Даунінг-стріт 10)", "Переговори з прем'єром Британії Ріші Сунаком (Даунінг-стріт, травень 2023)", "Wikimedia Commons (OGL / UK Govt)", "https://commons.wikimedia.org/wiki/File:The_Prime_Minister_meets_with_AI_developers_-_52923262063.jpg", "ep07_img_arch_14_downing_street_pm_ai_developers_2023.jpg", "Даріо Амодей, Деміс Гассабіс і Сем Альтман у Лондоні напередодні заснування перших інститутів безпеки ШІ."),
    ("EP07_PH_15", "ФОТО #15 (Disrupt 2023)", "Ключовий виступ Даріо Амодея на TechCrunch Disrupt 2023 (Сан-Франциско)", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Dario_Amodei_at_TechCrunch_Disrupt_2023_01.jpg", "ep07_img_arch_15_dario_amodei_techcrunch_disrupt_2023_portrait.jpg", "Портрет CEO Anthropic під час пояснення балансу між Конституційним ШІ та відповідальною конкуренцією."),
    ("EP07_PH_16", "ФОТО #16 (Токіо • 2025)", "Міжнародний саміт ШІ-дипломатії у Токіо з Даріо Амодеєм (2025)", "Wikimedia Commons (CC BY 4.0 / Japan Govt)", "https://commons.wikimedia.org/wiki/File:Sanae_Takaichi_and_Dario_Amodei_in_2025_(1).jpg", "ep07_img_arch_16_dario_amodei_tokyo_ai_diplomacy_2025.jpg", "Урядові перемовини в Японії щодо глобальної інфраструктури та відповідальних стандартів frontier-моделей."),
    ("EP07_PH_17", "ФОТО #17 (Біозахист BSL-4)", "Протоколи ізоляції біолабораторій BSL-4 — інженерний взірець рівнів ASL Anthropic", "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:BSL-4_Data-_Hands-On_Training_(3213)_(17977531191).jpg", "ep07_img_arch_17_bsl4_containment_asl_protocol.jpg", "Фізична модель чотирирівневого біозахисту, що лягла в основу Responsible Scaling Policy (ASL-1..ASL-4)."),
    ("EP07_PH_18", "ФОТО #18 («Машини благодаті»)", "Флуоресцентна мікроскопія ДНК онкоклітин — перемога над хворобами у XXI столітті", "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:Fluorescence_microscopy_of_the_DNA_of_the_oral_cancer_cells.jpg", "ep07_img_arch_18_cancer_dna_fluorescence_loving_grace.jpg", "Ядра клітин у флуоресцентному світлі — метафора гуманістичного маніфесту «Machines of Loving Grace»."),
]

EP07_QUOTES_CARDS = [
    ("UA #01 (4K • 10с)", "00:55–01:25", "ep07_ua_clip_card_01_leather_and_illness_10s", "Ремесло батька й крихке тіло людини (Сан-Франциско 1983–2006)"),
    ("UA #02 (4K • 10с)", "01:45–02:35", "ep07_ua_clip_card_02_princeton_retina_2011_10s", "Сітківка ока як живий біологічний комп'ютер (Принстон 2011)"),
    ("UA #03 (4K • 10с)", "04:45–05:45", "ep07_ua_clip_card_03_scaling_laws_line_10s", "Пряма лінія інтелекту через 7 порядків (Закони масштабу 2020)"),
    ("UA #04 (4K • 10с)", "06:45–08:15", "ep07_ua_clip_card_04_silent_exodus_anthropic_10s", "Коли перегони втрачають гальма — тихий вихід і створення Anthropic PBC"),
    ("UA #05 (4K • 10с)", "10:15–11:10", "ep07_ua_clip_card_05_claude_shannon_prism_10s", "Конституційний ШІ як прозора призма принципів (Клод Шеннон)"),
    ("UA #06 (4K • 10с)", "12:15–13:30", "ep07_ua_clip_card_06_mech_interp_microscope_10s", "Механістична інтерпретованість — МРТ усередині чорної скриньки (2024)"),
    ("UA #07 (4K • 12с)", "15:10–16:40", "ep07_ua_clip_card_07_asl_biosecurity_vow_12s", "Якщо модель сягне порогу ASL-4 — ми зупинимо навчання (Сенат 2023)"),
    ("UA #08 (4K • 12с)", "18:45–21:00", "ep07_ua_clip_card_08_loving_grace_finale_12s", "Стиснути століття біології в десять років зцілення («Машини благодаті»)"),
]

EP07_FLOW_KEYFRAMES = [
    ("KF #01 (2K)", "00:55–01:40", "Human Dissolving Into Golden Biological Equations (ДНК і нейрофізика сітківки)",
     "assets/flow_keyframes/ep07_flow_img_01_human_equations.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP07_FLOW_IMG_01_Human_Dissolving_Into_Equations_2K.jpg"),
    ("KF #02 (2K)", "05:00–06:10", "Human & Golden Power-Law Equations Alignment (Симетрія законів масштабу та совісті)",
     "assets/flow_keyframes/ep07_flow_img_02_golden_equations.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP07_FLOW_IMG_02_Human_Golden_Equations_Alignment_2K.jpg"),
    ("KF #03 (2K)", "17:45–19:00", "Nanobots Repairing Human Cell (Точкова клітинна терапія — «Машини благодаті»)",
     "assets/flow_keyframes/ep07_flow_img_03_nanobots_repairing_cell.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP07_FLOW_IMG_03_Nanobots_Repairing_Human_Cell_2K.jpg"),
    ("KF #04 (2K)", "10:15–11:15", "Hands Cupping Levitating Liquid Mirror (Крихкий баланс етичної Конституції)",
     "assets/flow_keyframes/ep07_flow_img_04_hands_levitating_liquid.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP07_FLOW_IMG_04_Hands_Cupping_Levitating_Liquid_Mirror_2K.jpg"),
    ("KF #05 (2K)", "13:15–14:30", "Finger Touching Glowing AI Core (Дотик до прозорого серця Claude 3)",
     "assets/flow_keyframes/ep07_flow_img_05_finger_touching_ai_core.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP07_FLOW_IMG_05_Finger_Touching_Glowing_AI_Core_2K.jpg"),
]


def main():
    raw_txt = POOL_JS.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    pool = json.loads(raw_txt[len(prefix):].rstrip(";\n "))
    ep7 = pool["07"]

    ep7["dossiers"] = EP07_DOSSIERS

    archives_list = []
    for code, act, tc, fn, title, src, url, sec, note in EP07_ARCHIVES:
        archives_list.append({
            "code": code,
            "act": act,
            "timecode": tc,
            "tc": tc,
            "file": fn,
            "mp4_file": fn,
            "title": title,
            "source": src,
            "url": url,
            "section": sec,
            "note": note,
            "video_preview": f"assets/video_previews/archives/{fn}",
        })
    ep7["archives"] = archives_list

    photos_list = []
    for pid, code, title, src, url, fn, desc in EP07_PHOTOS:
        photos_list.append({
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_amodei/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        })
    ep7["archival_photos"] = photos_list

    gallery = []
    for code, tc, title, web_p, raw_p in EP07_FLOW_KEYFRAMES:
        gallery.append({
            "code": code,
            "badge": "🖼️ 2K Кадр готовий",
            "chip": "chip-cyan",
            "tc": tc,
            "title": title,
            "web_preview": web_p,
            "raw_path": raw_p,
            "dims": "2752×1536 (2K JPG)",
        })
    for code, tc, slug, desc in EP07_QUOTES_CARDS:
        gallery.append({
            "code": code,
            "badge": "🎬 4K Цитат-Картка",
            "chip": "chip-amber",
            "tc": tc,
            "title": desc,
            "web_preview": f"assets/cards_preview/{slug}.jpg",
            "video_preview": f"assets/video_previews/cards/{slug}.mp4",
            "raw_path": f"05_RAW_FOOTAGE/rendered_cinematic_stills_4k/{slug}.mp4",
            "dims": "3840×2160 (4K MP4)",
        })
    ep7["flow_gallery"] = gallery

    POOL_JS.write_text(prefix + json.dumps(pool, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"[OK] Updated {POOL_JS} EP07: dossiers={len(ep7['dossiers'])}, archives={len(ep7['archives'])}, photos={len(ep7['archival_photos'])}, gallery={len(ep7['flow_gallery'])}")

    # Write EP07_MEDIA_CATALOG.json & .md
    catalog_json = {
        "episode": "EP07",
        "hero": "Dario Amodei",
        "dossiers_4k": EP07_DOSSIERS,
        "archives_1080p": archives_list,
        "archival_photos": photos_list,
        "flow_gallery": gallery,
    }
    (FOOTAGE_DIR / "EP07_MEDIA_CATALOG.json").write_text(json.dumps(catalog_json, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# EP07 — Даріо Амодей: Повний Каталог Медіа-Асетів",
        "",
        f"- **4K Досьє-плашки (`05_RAW_FOOTAGE/dossiers_press/`):** {len(EP07_DOSSIERS)}",
        f"- **HD Архівні відеокліпи 1080p24 (`05_RAW_FOOTAGE/archives/`):** {len(archives_list)}",
        f"- **Фотоархів Wikimedia Commons (`05_RAW_FOOTAGE/speaker_portraits/young_amodei/`):** {len(photos_list)}",
        f"- **2K Flow Ключові кадри & 4K UA Цитат-Картки:** {len(gallery)}",
        "",
        "## Архівні відеокліпи (16 HD)",
    ]
    for a in archives_list:
        md_lines.append(f"- `{a['code']}` [{a['tc']}] **{a['file']}** — {a['title']}")
    md_lines.append("\n## Фотоархів Wikimedia Commons (18)")
    for p in photos_list:
        md_lines.append(f"- `{p['code']}` **{p['id']}** — {p['title']} (`{p['raw_file']}`)")
    (FOOTAGE_DIR / "EP07_MEDIA_CATALOG.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print("[OK] Generated EP07_MEDIA_CATALOG.json & EP07_MEDIA_CATALOG.md")

    # Manifest base file (build_vault_inventory_and_triads.py will enrich/preserve)
    manifest = {
        "episode_id": "EP07",
        "hero": "Dario Amodei",
        "title": "Фізика совісті та машини благодаті",
        "bpm": 92,
        "status": "MEDIA_AND_RESEARCH_SYNCED",
        "source_count": 15,
        "archival_video_count": len(archives_list),
        "archival_photo_count": len(photos_list),
        "dossier_4k_count": len(EP07_DOSSIERS),
        "ua_quote_card_count": len(EP07_QUOTES_CARDS),
        "verified_milestones": [
            "Stanford Physics BS (2006) & Princeton Biophysics PhD on Retinal Electrophysiology (2011)",
            "Baidu Deep Speech 2 & Google Brain Concrete Problems in AI Safety (2014–2016)",
            "OpenAI VP of Research: Heading Safety, RLHF, GPT-2 & GPT-3 Scaling Oversight (2016–2020)",
            "Empirical Scaling Laws for Neural Language Models arXiv:2001.08361 (2020)",
            "Silent Departure from OpenAI with Daniela Amodei & Senior Staff (Late 2020)",
            "Founding of Anthropic as a Public Benefit Corporation (PBC) (2021)",
            "Constitutional AI (RLAIF) & Scaling Monosemanticity Mechanistic Interpretability (2022–2024)",
            "US Senate Judiciary Biosecurity Hearing & Responsible Scaling Policy ASL-1..4 (2023)",
            "Publication of 'Machines of Loving Grace' Visionary Manifesto (October 2024)",
        ],
    }
    (META_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("[OK] Initialized 08_METADATA/EP07_DARIO_AMODEI/manifest.json")


if __name__ == "__main__":
    main()
