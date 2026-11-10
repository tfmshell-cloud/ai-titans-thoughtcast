#!/usr/bin/env python3
"""
EP10 Andrew Ng — Media Ecosystem Sync:
- Registers all 6 4K Dossiers (EP10_DOC_01..06), 16 HD Archival Video Clips (EP10_VID_ARCH_01..16),
  18 Curated Wikimedia Archival Photos (EP10_IMG_ARCH_01..18), 9 Flow Keyframes + 8 4K UA Quote Cards
  into 07_DASHBOARD/data/media_acquisition_pool.js (preserving existing portrait, audio, sci_vfx).
- Generates 05_RAW_FOOTAGE/EP10_MEDIA_CATALOG.json & 05_RAW_FOOTAGE/EP10_MEDIA_CATALOG.md.
- Initializes 08_METADATA/EP10_ANDREW_NG/manifest.json.
"""
import json
import urllib.parse
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
POOL_JS = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"
FOOTAGE_DIR = ROOT / "05_RAW_FOOTAGE"
META_DIR = ROOT / "08_METADATA" / "EP10_ANDREW_NG"
META_DIR.mkdir(parents=True, exist_ok=True)

EP10_DOSSIERS = [
    {
        "id": "EP10_DOC_01",
        "ep": "10",
        "act": "ACT2",
        "timecode": "06:20–07:40",
        "title": "Democratizing Deep Learning: From 16,000 Cores to 8 Million Builders",
        "source_label": "ml-class.org Enrollment Log (104,000 Students) & Google Brain 16,000-Core Cluster",
        "highlight": "“Just as electricity transformed almost everything 100 years ago, today I actually have a hard time thinking of an industry that I don't think AI will transform in the next several years.”",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_01_ACT2_AndrewNg_GoogleBrain_Coursera_2011.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_01_andrewng_coursera.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_01.mp4",
    },
    {
        "id": "EP10_DOC_02",
        "ep": "10",
        "act": "ACT1",
        "timecode": "00:25–05:15",
        "title": "Гонконг і Сінгапур 1984: код батька-лікаря, Raffles BASIC та перевернутий вертоліт RL",
        "source_label": "Hong Kong & Raffles Institution Archive • Carnegie Mellon, MIT, UC Berkeley & Stanford Helicopter (arXiv 1105.0010)",
        "highlight": "Aerodynamics of an inverted helicopter are too complex to program by hand — you teach it through apprenticeship and reinforcement learning.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_02_ACT1_hong_kong_singapore_raffles_basic_1984.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_02_singapore_helicopter_rl.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_02.mp4",
    },
    {
        "id": "EP10_DOC_03",
        "ep": "10",
        "act": "ACT2",
        "timecode": "05:15–10:45",
        "title": "Google X і Джефф Дін: 16 000 ядер CPU і «нейрон кота» на першій шпальті NYT (2012)",
        "source_label": "ICML 2012 / arXiv 1112.6209 (Le, Dean, Ng — 1B Parameters, 10M YouTube Frames) & NYT 2012",
        "highlight": "Without anyone ever telling the network what a cat was, a high-level neuron spontaneously learned to recognize feline faces from raw unlabeled YouTube video.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_03_ACT2_google_brain_16000_cores_cat_neuron_2012.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_03_google_brain_16k_cat.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_03.mp4",
    },
    {
        "id": "EP10_DOC_04",
        "ep": "10",
        "act": "ACT3",
        "timecode": "10:45–14:30",
        "title": "Вебкамера в Пало-Альто: 104 000 студентів, Coursera, DeepLearning.AI та Baidu (1,300 людей)",
        "source_label": "Stanford ml-class.org (2011) • Coursera Founding (Koller & Ng, 2012) • Baidu SVAIL / Deep Speech",
        "highlight": "It would have taken 250 years teaching Stanford classrooms to reach 100,000 students — online democratization reached them in one semester.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_04_ACT3_cs229_webcam_104k_coursera_baidu_2014.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_04_coursera_104k_students.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_04.mp4",
    },
    {
        "id": "EP10_DOC_05",
        "ep": "10",
        "act": "ACT3",
        "timecode": "14:30–18:00",
        "title": "«ШІ — це нова електрика» та революція Data-Centric AI (50 чистих фото замість мільярда шуму)",
        "source_label": "AI Frontiers / Stanford MS&E Manifesto (2017) & Landing AI Data-Centric Steel Defect Case (2021)",
        "highlight": "You can build an extraordinary factory inspection model with just 50 carefully curated examples — fix the data, not just the model code.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_05_ACT3_ai_is_the_new_electricity_data_centric_2021.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_05_new_electricity_data_centric.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_05.mp4",
    },
    {
        "id": "EP10_DOC_06",
        "ep": "10",
        "act": "ACT4",
        "timecode": "18:00–21:30",
        "title": "Захист відкритого коду, Agentic Workflows і Фінал Сезону: десять рядків на світанку",
        "source_label": "Sequoia AI Ascent & LangChain Interrupt (2024–2025) • 4 Agentic Patterns & Season 1 Finale",
        "highlight": "GPT-3.5 wrapped in an iterative Agentic Workflow outperforms zero-shot GPT-4. Any builder worldwide can start with ten lines of code at dawn.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP10_DOC_06_ACT4_open_source_gutenberg_agentic_workflows_finale.png",
        "web_preview": "assets/dossiers_preview/ep10_doc_06_agentic_workflows_finale.jpg",
        "video_preview": "assets/video_previews/dossiers/EP10_DOC_06.mp4",
    },
]

EP10_ARCHIVES = [
    ("ARCH #01", "Акт 2 (Stanford CS229 • 2018)", "05:30–05:38", "EP10_VID_ARCH_01_ACT2_24FPS_AndrewNg_Stanford_CS229_Chalkboard.mp4",
     "Стенфордська лекція Ендрю Ина (CS229 Machine Learning)",
     "Stanford Online — CS229 (jGwO_UgTS7I)", "https://www.youtube.com/watch?v=jGwO_UgTS7I", "00:01:40-00:01:48",
     "Ендрю Ин біля класичної стенфордської дошки відкриває курс, з якого виросло ціле покоління інженерів ШІ."),
    ("ARCH #02", "Акт 1 (CS229 • Класика 2008)", "01:45–02:35", "EP10_VID_ARCH_02_ACT1_24FPS_AndrewNg_Stanford_CS229_2008_Classic.mp4",
     "Історична лекція CS229 (2008): завдання, які неможливо запрограмувати вручну",
     "Stanford CS229 Archive (UzxYlbK2c7E)", "https://www.youtube.com/watch?v=UzxYlbK2c7E", "00:02:08-00:02:50",
     "Ранній запис лекцій Стенфорду, що згодом став основою першого масового онлайн-курсу."),
    ("ARCH #03", "Акт 1 (Вертоліт RL • Стенфорд)", "03:30–04:30", "EP10_VID_ARCH_03_ACT1_24FPS_AndrewNg_Autonomous_Helicopter_RL.mp4",
     "Автономний трюковий вертоліт навчається перевернутого польоту через RL",
     "Stanford Robotics Archive (M-QUkgk3HyE)", "https://www.youtube.com/watch?v=M-QUkgk3HyE", "00:00:22-00:01:06",
     "Реальні кадри перевернутих петель вертольота, який спостерігав за пілотом-експертом через навчання з підкріпленням."),
    ("ARCH #04", "Акт 1 (Робототехніка 2011)", "04:30–05:15", "EP10_VID_ARCH_04_ACT1_24FPS_AndrewNg_Robotics_Aerodynamics_Stanford.mp4",
     "Чому аеродинаміку неможливо закодувати вручну — дайте комп'ютеру вчитися самому",
     "Stanford Lecture 2011 (AY4ajbu_G3k)", "https://www.youtube.com/watch?v=AY4ajbu_G3k", "00:03:20-00:04:08",
     "Пояснення принципу: замість мільйона правил if-else алгоритм сам опановує фізику польоту."),
    ("ARCH #05", "Акт 2 (Google Brain • Витоки)", "05:45–07:00", "EP10_VID_ARCH_05_ACT2_24FPS_AndrewNg_Google_Brain_Team_Origin.mp4",
     "Як команда Google Brain трансформувала Google у AI-компанію",
     "Stanford CS229 2018 (jGwO_UgTS7I)", "https://www.youtube.com/watch?v=jGwO_UgTS7I", "00:07:48-00:08:30",
     "Ендрю Ин згадує заснування підрозділу Google Brain 2011 року разом із Джеффом Діном."),
    ("ARCH #06", "Акт 2 (Baidu & 1,300 вчених)", "07:00–08:30", "EP10_VID_ARCH_06_ACT2_24FPS_AndrewNg_Baidu_1300_AI_Team_SVOD.mp4",
     "Google Brain і керівництво 1,300 дослідниками ШІ в Baidu Research",
     "SVOD Silicon Valley (PS9MELl8vLQ)", "https://www.youtube.com/watch?v=PS9MELl8vLQ", "00:02:15-00:02:58",
     "Масштабування глибокого навчання у Кремнієвій долині та Пекіні: від мовлення до комп'ютерного зору."),
    ("ARCH #07", "Акт 2 (Від котів до рентгенів)", "08:30–10:45", "EP10_VID_ARCH_07_ACT2_24FPS_AndrewNg_Cats_Xrays_Transfer_Learning.mp4",
     "Від розпізнавання котів на YouTube до медичних рентген-знімків",
     "Startup Grind Keynote (fgbBtnCvcDI)", "https://www.youtube.com/watch?v=fgbBtnCvcDI", "00:08:25-00:09:10",
     "Як трансферне навчання перетворило «експеримент із котом на 16 000 ядер» на порятунок пацієнтів."),
    ("ARCH #08", "Акт 2 (Коллер & Ин • 100K)", "10:45–12:15", "EP10_VID_ARCH_08_ACT2_24FPS_AndrewNg_EDUKWEST_Koller_Coursera_100K.mp4",
     "Ендрю Ин і Дафна Коллер: 100 000 студентів на перших курсах та народження Coursera",
     "EDUKWEST Interview (e-NoK9jOuEE)", "https://www.youtube.com/watch?v=e-NoK9jOuEE", "00:01:00-00:01:46",
     "Архівне інтерв'ю 2012 року засновників Coursera про миттєвий планетарний вибух онлайн-освіти."),
    ("ARCH #09", "Акт 3 (Масштаб Coursera)", "12:15–14:00", "EP10_VID_ARCH_09_ACT3_24FPS_AndrewNg_Coursera_Tens_of_Thousands.mp4",
     "Як масштабувати університетську освіту на сотні тисяч учнів одночасно",
     "EDUKWEST Interview (e-NoK9jOuEE)", "https://www.youtube.com/watch?v=e-NoK9jOuEE", "00:04:50-00:05:35",
     "Чому вебкамера та інтерактивні завдання змінили доступ до вищої освіти для всього світу."),
    ("ARCH #10", "Акт 3 (Нова електрика • 2017)", "14:30–15:45", "EP10_VID_ARCH_10_ACT3_24FPS_AndrewNg_AI_Is_The_New_Electricity_2017.mp4",
     "Маніфест «ШІ — це нова електрика»: трансформація кожної індустрії",
     "AI Frontiers 2017 (JsGPh-HOqjY)", "https://www.youtube.com/watch?v=JsGPh-HOqjY", "00:02:51-00:03:38",
     "Знаменита історична аналогія Ендрю Ина між електрифікацією ХХ століття та сучасним ШІ."),
    ("ARCH #11", "Акт 3 (Сталеві рулони • Data)", "16:15–17:15", "EP10_VID_ARCH_11_ACT3_24FPS_AndrewNg_Steel_Defects_Data_Centric_AI.mp4",
     "39 типів дефектів на сталевому заводі: чому Big Data не працює на виробництві",
     "DeepLearning.AI (06-AZXmwHjo)", "https://www.youtube.com/watch?v=06-AZXmwHjo", "00:02:23-00:03:08",
     "Програмне підняття точності з 76.2% до 90%+ завдяки очищенню даних замість гонитви за архітектурами."),
    ("ARCH #12", "Акт 3 (50 чистих знімків)", "17:15–18:00", "EP10_VID_ARCH_12_ACT3_24FPS_AndrewNg_Databricks_Fifty_Good_Images.mp4",
     "Досить усього 50 якісних зображень, якщо дані відібрано з любов'ю",
     "Databricks Keynote (avoijDORAlc)", "https://www.youtube.com/watch?v=avoijDORAlc", "00:07:12-00:07:56",
     "Квінтесенція Data-Centric AI: якість та узгодженість розмітки перемагають мільйони сміттєвих даних."),
    ("ARCH #13", "Акт 3 (Формула зростання)", "13:30–14:30", "EP10_VID_ARCH_13_ACT3_24FPS_AndrewNg_OReilly_Read_Papers_Replicate.mp4",
     "Секретна формула кар'єри в ШІ: читай статті й відтворюй результати",
     "O'Reilly AI Conference (mQ29kb_jZYI)", "https://www.youtube.com/watch?v=mQ29kb_jZYI", "00:18:45-00:19:30",
     "Порада Вчителя Світу молодим інженерам: фундамент онлайн-курсів + реплікація досліджень."),
    ("ARCH #14", "Акт 4 (Agentic Workflows)", "18:00–19:00", "EP10_VID_ARCH_14_ACT4_24FPS_AndrewNg_Sequoia_Agentic_Workflows_GPT.mp4",
     "GPT-3.5 у циклі Agentic Workflow перемагає моноліт GPT-4 (Sequoia AI Ascent)",
     "Sequoia Capital (sal78ACtGTc)", "https://www.youtube.com/watch?v=sal78ACtGTc", "00:02:45-00:03:28",
     "Культова демонстрація того, як ітеративна рефлексія маленької моделі перевершує єдиний промпт гіганта."),
    ("ARCH #15", "Акт 4 (Захист Open Source)", "19:00–19:45", "EP10_VID_ARCH_15_ACT4_24FPS_AndrewNg_LangChain_Protect_Open_Source.mp4",
     "Захист відкритих ваг і відкритого коду від регуляторних монополій",
     "LangChain Interrupt (OaRhpwz_TGM)", "https://www.youtube.com/watch?v=OaRhpwz_TGM", "00:25:55-00:26:40",
     "Чому відкриті моделі — це сучасний верстат Гутенберга, який не можна зачиняти на замок."),
    ("ARCH #16", "Акт 4 (Час творити • Фінал)", "19:45–21:30", "EP10_VID_ARCH_16_ACT4_24FPS_AndrewNg_Snowflake_Great_Time_To_Be_Builder.mp4",
     "«Найкращий час в історії, щоб бути творцем»: послання наприкінці Сезону 1",
     "Snowflake BUILD (KrRD7r7y7NY)", "https://www.youtube.com/watch?v=KrRD7r7y7NY", "00:25:38-00:26:22",
     "Заключний заклик до розробників у всьому світі перетворювати ідеї на реальні системи."),
]

RAW_WM_TITLES = [
    ("EP10_PH_01", "ФОТО #01 (1976–1984 • Гонконг)", "Історична бухта Вікторія в Гонконзі — роки дитинства в родині лікаря Рональда Ина", "Wikimedia Commons (Public Domain)", "File:Historical Hong Kong- Junk in Victoria Harbour.jpg", "ep10_img_arch_01_hong_kong_childhood_era.jpg", "Мальовничий Гонконг, де батько-гематолог надихнув маленького Ендрю на першу медичну програму."),
    ("EP10_PH_02", "ФОТО #02 (1988 • Raffles, Сінгапур)", "Вежа з годинником легендарної школи Raffles Institution у Сінгапурі", "Wikimedia Commons (CC BY-SA 4.0)", "File:Raffles Institution Clocktower.jpg", "ep10_img_arch_02_raffles_institution_singapore.jpg", "Школа в Сінгапурі, де підліток Ендрю вивчав алгоритми та передруковував код із журналів."),
    ("EP10_PH_03", "ФОТО #03 (Перший Apple II • BASIC)", "Комп'ютер Apple II 1977 року — перші рядки коду BASIC без жодної зайвої коми", "Wikimedia Commons (CC BY 2.0)", "File:Apple II, 1977, Computer History Museum.jpg", "ep10_img_arch_03_apple_ii_basic_coding_youth.jpg", "Символ шкільних експериментів із BASIC: перехід від паперових роздруківок до живої логіки."),
    ("EP10_PH_04", "ФОТО #04 (1997 • Carnegie Mellon)", "Панорама Університету Карнегі-Меллона — потрійний бакалавр за 3 роки", "Wikimedia Commons (CC BY-SA 3.0)", "File:Carnegie Mellon University as seen from the Cathedral of Learning.jpg", "ep10_img_arch_04_carnegie_mellon_bs_era.jpg", "Піттсбург, де Ендрю Ин закінчив Carnegie Mellon одразу за трьома напрямами й очолив клас."),
    ("EP10_PH_05", "ФОТО #05 (1998 • MIT Killian Court)", "Академічний двір Killian Court у MIT — магістерське дослідження навчання", "Wikimedia Commons (CC BY-SA 4.0)", "File:MIT Killian Court.jpg", "ep10_img_arch_05_mit_killian_court_ms_era.jpg", "Массачусетський технологічний інститут, де формувався його підхід до нейромереж та статистики."),
    ("EP10_PH_06", "ФОТО #06 (2002 • UC Berkeley)", "Вежа Sather Tower в Каліфорнійському університеті Берклі (PhD під керівництвом Джордана)", "Wikimedia Commons (CC BY 2.0)", "File:Sather Tower - UC Berkeley (15862067865).jpg", "ep10_img_arch_06_uc_berkeley_sather_tower_phd.jpg", "Захист докторської дисертації у Берклі (2002) з навчання з підкріпленням та робототехніки."),
    ("EP10_PH_07", "ФОТО #07 (2002+ • Stanford Quad)", "Головний кампус Стенфордського університету з вежі Гувера — лабораторія CS229", "Wikimedia Commons (CC BY-SA 3.0)", "File:Stanford University from Hoover Tower May 2011 004.jpg", "ep10_img_arch_07_stanford_university_professor_quad.jpg", "Академічний дім Ендрю Ина: курси машинного навчання та Стенфордська лабораторія ШІ (SAIL)."),
    ("EP10_PH_08", "ФОТО #08 (Автономний вертоліт RL)", "Перевернутий політ радіокерованого вертольота — ілюстрація експериментів Stanford", "Wikimedia Commons (CC BY-SA 3.0)", "File:Radio Controlled Model Helicopter Upside Down over Chengkungling Ground 20121006.jpg", "ep10_img_arch_08_inverted_rc_helicopter_rl_flight.jpg", "Трюковий політ догори дригом, який навчили виконувати автономно через Apprenticeship Learning."),
    ("EP10_PH_09", "ФОТО #09 (2011 • Googleplex)", "Кампус Googleplex у Маунтін-В'ю — народження таємного проєкту Google Brain", "Wikimedia Commons (CC BY-SA 3.0)", "File:Outside Googleplex in Mountain View, California.jpg", "ep10_img_arch_09_googleplex_mountain_view_google_brain.jpg", "Штаб-квартира Google, де разом із Джеффом Діном розпочалася ера індустріального Deep Learning."),
    ("EP10_PH_10", "ФОТО #10 (2012 • Нейрон Кота)", "Мордочка смугастого кота — обличчя з чистої статистики 16 000 серверних ядер", "Wikimedia Commons (CC BY-SA 3.0)", "File:Tabby face.jpg", "ep10_img_arch_10_google_brain_cat_neuron_2012.jpg", "Символ легендарної статті ICML 2012 та сенсації New York Times про самостійне прозріння мережі."),
    ("EP10_PH_11", "ФОТО #11 (Coursera HQ)", "381 E. Evelyn Avenue у Маунтін-В'ю — перша штаб-квартира Coursera", "Wikimedia Commons (CC BY-SA 4.0)", "File:381 E. Evelyn Avenue.jpg", "ep10_img_arch_11_coursera_mountain_view_hq.jpg", "Дім платформи, яка перетворила один курс CS229 (104 000 студентів) на світовий університет."),
    ("EP10_PH_12", "ФОТО #12 (2012 • Запуск Coursera)", "Зустріч партнерів Coursera у роки глобальної освітньої революції", "Wikimedia Commons (CC BY-SA 2.0)", "File:Coursera à la rencontre de son 1er partenaire français (15380450114).jpg", "ep10_img_arch_12_coursera_global_launch_era.jpg", "Демократизація елітної освіти Стенфорду для учнів у Києві, Лагосі, Бангалорі та всьому світі."),
    ("EP10_PH_13", "ФОТО #13 (2014 • Baidu Шанді)", "Штаб-квартира Baidu в пекінському Шанді — керівництво 1,300 дослідниками ШІ", "Wikimedia Commons (CC BY-SA 4.0)", "File:Baidu headquarters at Shangdi (20220509111808).jpg", "ep10_img_arch_13_baidu_shangdi_chief_scientist_hq.jpg", "У 2014–2017 роках Ендрю Ин очолив Baidu AI Group, створивши Deep Speech та масштабне розпізнавання мовлення."),
    ("EP10_PH_14", "ФОТО #14 (WSJ Keynote Stage)", "Ендрю Ин у фірмовій блакитній сорочці на сцені WSJ D.Live", "Wikimedia Commons (CC BY 2.0)", "File:Andrew Ng WSJ.jpg", "ep10_img_arch_14_andrew_ng_wsj_ai_electricity_keynote.jpg", "Образ спокійного Просвітителя технологічної епохи, який пояснює бізнесу нову електрику."),
    ("EP10_PH_15", "ФОТО #15 (Нитка Нової Електрики)", "Світна нитка розжарення у темряві — символ маніфесту «ШІ — це нова електрика»", "Wikimedia Commons (CC0)", "File:Low-key photograph of light bulb, Straume, Norway julesvernex2.jpg", "ep10_img_arch_15_ai_is_the_new_electricity_bulb.jpg", "Метафора трансформування кожної базової галузі людства за аналогією з електрифікацією 100 років тому."),
    ("EP10_PH_16", "ФОТО #16 (Landing AI • Заводи)", "Прецизійна оптична інспекція промислових деталей (комп'ютерний зір Data-Centric AI)", "Wikimedia Commons (CC BY-SA 4.0)", "File:Walter Helitronic Vision IMG 0005.jpg", "ep10_img_arch_16_landing_ai_precision_factory_vision.jpg", "Індустріальний фокус Landing AI: 50 чистих знімків сталі й таблеток замість хаотичних гігабайтів."),
    ("EP10_PH_17", "ФОТО #17 (Лампа Едісона • Світло)", "Класична лампа Едісона — міст від винайдення електрики до доступу знань для всіх", "Wikimedia Commons (CC BY-SA 3.0)", "File:Light Bulb 3.jpg", "ep10_img_arch_17_edison_grid_new_electricity_glow.jpg", "Щоб електрика освітила кожну оселю, знадобилася інфраструктура — те саме робить відкритий код ШІ."),
    ("EP10_PH_18", "ФОТО #18 (Світанок на Землі • МКС)", "Світанок над нічними вогнями континентів із борту МКС — фінал 10-серійного Сезону", "Wikimedia Commons (NASA Public Domain)", "File:Before the Dawn in America’s Heartland (1507747 - ISS075-E-226709).jpg", "ep10_img_arch_18_earth_dawn_global_builders_finale.jpg", "Заключний кадр всього Сезону: мільйони вогнів людських вікон назустріч світанку творення."),
]

EP10_FLOW_KEYFRAMES = [
    ("KF #02 (2K)", "🖼️ 2K Кадр готовий", "chip-cyan", "00:25–01:45",
     "Doctor Father Medical Textbook (Батько-лікар показує підручник)",
     "assets/flow_keyframes/ep10_flow_kf_02_doctor_father.jpg",
     "05_RAW_FOOTAGE/flow_images/EP10_Ng/01_primary_keyframes/EP10_FLOW_IMG_02_Doctor_Father_Medical_Textbook_2K.jpg",
     "2752×1536 (2K JPG)", None),
    ("B-ROLL #02B (2K)", "🎬 B-Roll Кадр", "chip-amber", "01:45–02:30",
     "Father & Son Medical AI Textbook (Батько та син вивчають схеми)",
     "assets/flow_keyframes/ep10_flow_broll_02b_father_textbook_close.jpg",
     "05_RAW_FOOTAGE/flow_images/EP10_Ng/02_broll_stills_and_studies/EP10_FLOW_BROLL_02B_Father_Son_Medical_Textbook_Close_2K.jpg",
     "2752×1536 (2K JPG)", None),
    ("GOOGLE BRAIN #03", "🐱 16 000 Ядер • Розпізнавання котів", "chip-amber", "06:00–07:30",
     "Суперкомп'ютерні сервери Google Brain у крижаній залі (16,000 Cores Cat Neuron)",
     "assets/flow_keyframes/ep01_flow_kf_06_server_monolith.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_06_Supercomputer_Servers_Cold_Hall_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 2: 2011 рік — заснування Google Brain разом із Джеффом Діном і відкриття нейрона, що впізнає котів без вчителя."),
    ("COURSERA #04", "🎓 Нова Електрика • Мільйони учнів", "chip-emerald", "10:30–12:30",
     "Планета, охоплена сяйвом знань (Coursera & DeepLearning.AI Education Grid)",
     "assets/flow_keyframes/ep01_flow_kf_10_earth_horizon.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_10_Earth_Horizon_Neural_Grid_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 3 та 4: Навчання понад 8 мільйонів студентів: «ШІ — це нова електрика»."),
    ("CHILDHOOD #05", "💻 Сінгапур 1980-ті • Перший код", "chip-cyan", "02:00–03:30",
     "Хлопчик перед вінтажним комп'ютером у темній кімнаті",
     "assets/flow_keyframes/ep01_flow_broll_02d_boy_crt_room.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/02_broll_stills_and_studies/EP01_FLOW_IMG_02D_Boy_At_Vintage_CRT_1993_Room.jpg",
     "1920×1080 (1080p JPG)", "Акт 1: Дитинство в Сінгапурі та Гонконзі, батько вчить писати перші алгоритми сортування."),
    ("SMART CITY #06", "🏙️ Розумне місто • AI for Everyone", "chip-emerald", "09:00–10:30",
     "Голографічна карта трансформується у сяюче розумне місто",
     "assets/flow_keyframes/ep10_flow_img_03_map_city.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP10_FLOW_IMG_03_Holographic_Map_Morphing_City_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 3: Практичне застосування ШІ в охороні здоров'я, транспорті та освіті міст майбутнього."),
    ("SINGAPORE #04", "🏙️ Код Сінгапуру • Раффлз", "chip-cyan", "02:00–03:30",
     "Хмарочос пронизує вертикальний дощ двійкового коду над затокою",
     "assets/flow_keyframes/ep10_flow_img_04_skyscraper_binary_rain.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP10_FLOW_IMG_04_Skyscraper_Piercing_Binary_Rain_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 1: Юність Ендрю Ина в Сінгапурі: перші рядки коду на касетному комп'ютері серед тропічних дощів та хмарочосів Raffles Place."),
    ("GRID #05", "⚡ Нова Електрика • Світова Інфраструктура", "chip-amber", "17:30–19:00",
     "Будівлі мегаполіса перетворюються на кремнієві інтегральні плати",
     "assets/flow_keyframes/ep10_flow_img_05_metropolis_silicon.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP10_FLOW_IMG_05_Metropolis_Transforming_Into_Silicon_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 4: Знаменитий маніфест Ендрю Ина: «ШІ — це нова електрика», що докорінно трансформує міста, транспорт, лікарні та школи."),
    ("PLANET #06", "🌍 Coursera • Знання для 8 Мільярдів", "chip-emerald", "13:00–14:30",
     "Золоті імпульси знань поширюються тектонічними контурами Землі",
     "assets/flow_keyframes/ep10_flow_img_06_energy_pulses_earth.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP10_FLOW_IMG_06_Energy_Pulses_Flowing_Through_Earth_2K.jpg",
     "2752×1536 (2K JPG)", "Акт 3: Створення платформи Coursera: 100 000 студентів на першому онлайн-курсі машинного навчання та доступ до знань для кожного куточка планети."),
]

EP10_QUOTES_CARDS = [
    ("UA #01 (4K • 10с)", "00:00–00:25", "ep10_ua_clip_card_01_prometheus_blue_shirt_10s", "Прометей у блакитній сорочці, що приніс вогонь у кожну оселю"),
    ("UA #02 (4K • 10с)", "00:25–02:15", "ep10_ua_clip_card_02_singapore_basic_doctor_10s", "Діагноз на перфострічці: Гонконг і передрук BASIC у Сінгапурі"),
    ("UA #03 (4K • 10с)", "02:15–05:15", "ep10_ua_clip_card_03_inverted_helicopter_scale_10s", "Вертоліт догори дригом — навчання з підкріпленням у Стенфорді"),
    ("UA #04 (4K • 10с)", "05:15–10:45", "ep10_ua_clip_card_04_google_brain_cat_ghost_10s", "16 000 ядер Google X і «нейрон кота» на першій шпальті NYT"),
    ("UA #05 (4K • 10с)", "10:45–14:30", "ep10_ua_clip_card_05_cs229_webcam_104k_10s", "Дешева вебкамера в Пало-Альто й 104 000 учнів Coursera"),
    ("UA #06 (4K • 10с)", "14:30–16:15", "ep10_ua_clip_card_06_ai_new_electricity_10s", "«ШІ — це нова електрика»: провідник для фермера, лікаря й заводу"),
    ("UA #07 (4K • 12с)", "16:15–19:45", "ep10_ua_clip_card_07_data_centric_agentic_12s", "50 чистих знімків сталі & Agentic Workflows перемагають моноліти"),
    ("UA #08 (4K • 12с)", "19:45–21:30", "ep10_ua_clip_card_08_ten_lines_dawn_finale_12s", "Фінал Сезону: десять рядків коду на світанку — світло в кожному домі"),
]


def main():
    raw_txt = POOL_JS.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    pool = json.loads(raw_txt[len(prefix):].rstrip(";\n "))
    ep10 = pool["10"]

    ep10["dossiers"] = EP10_DOSSIERS

    archives_list = []
    for code, act, tc, fn, title, src, url, sec, note in EP10_ARCHIVES:
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
    ep10["archives"] = archives_list

    photos_list = []
    for pid, code, title, src, wm_title, fn, desc in RAW_WM_TITLES:
        photos_list.append({
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(wm_title, safe=":"),
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_andrew/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        })
    ep10["archival_photos"] = photos_list

    gallery = []
    for code, badge, chip, tc, title, web_p, raw_p, dims, usage in EP10_FLOW_KEYFRAMES:
        item = {
            "code": code,
            "badge": badge,
            "chip": chip,
            "tc": tc,
            "title": title,
            "web_preview": web_p,
            "raw_path": raw_p,
            "dims": dims,
        }
        if usage:
            item["usage"] = usage
        gallery.append(item)
    for code, tc, slug, desc in EP10_QUOTES_CARDS:
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
    ep10["flow_gallery"] = gallery

    POOL_JS.write_text(prefix + json.dumps(pool, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"[OK] Updated {POOL_JS} EP10: dossiers={len(ep10['dossiers'])}, archives={len(ep10['archives'])}, photos={len(ep10['archival_photos'])}, gallery={len(ep10['flow_gallery'])}")

    catalog_json = {
        "episode": "EP10",
        "hero": "Andrew Ng",
        "dossiers_4k": EP10_DOSSIERS,
        "archives_1080p": archives_list,
        "archival_photos": photos_list,
        "flow_gallery": gallery,
    }
    (FOOTAGE_DIR / "EP10_MEDIA_CATALOG.json").write_text(json.dumps(catalog_json, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# EP10 — Ендрю Ин: Повний Каталог Медіа-Асетів",
        "",
        f"- **4K Досьє-плашки (`05_RAW_FOOTAGE/dossiers_press/`):** {len(EP10_DOSSIERS)}",
        f"- **HD Архівні відеокліпи 1080p24 (`05_RAW_FOOTAGE/archives/`):** {len(archives_list)}",
        f"- **Фотоархів Wikimedia Commons (`05_RAW_FOOTAGE/speaker_portraits/young_andrew/`):** {len(photos_list)}",
        f"- **Flow Ключові кадри & 4K UA Цитат-Картки:** {len(gallery)}",
        "",
        "## Архівні відеокліпи (16 HD)",
    ]
    for a in archives_list:
        md_lines.append(f"- `{a['code']}` [{a['tc']}] **{a['file']}** — {a['title']}")
    md_lines.append("\n## Фотоархів Wikimedia Commons (18)")
    for p in photos_list:
        md_lines.append(f"- `{p['code']}` **{p['id']}** — {p['title']} (`{p['raw_file']}`)")
    (FOOTAGE_DIR / "EP10_MEDIA_CATALOG.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print("[OK] Generated EP10_MEDIA_CATALOG.json & EP10_MEDIA_CATALOG.md")

    manifest = {
        "episode_id": "EP10",
        "hero": "Andrew Ng",
        "title": "Вчитель світу та нова електрика",
        "bpm": 92,
        "status": "MEDIA_AND_RESEARCH_SYNCED",
        "source_count": 21,
        "archival_video_count": len(archives_list),
        "archival_photo_count": len(photos_list),
        "dossier_4k_count": len(EP10_DOSSIERS),
        "ua_quote_card_count": len(EP10_QUOTES_CARDS),
        "verified_milestones": [
            "Born in London (1976), Raised in Hong Kong & Singapore (Raffles Institution)",
            "Triple Major B.S. at Carnegie Mellon (1997), M.S. at MIT (1998), PhD at UC Berkeley (2002)",
            "Stanford Professor & Autonomous Helicopter Reinforcement Learning (2002-2011)",
            "Co-Founder of Google Brain & 16,000-Core Cat Neuron Breakthrough (2011-2012)",
            "Stanford CS229 Online (104,000+ Students) & Co-Founder of Coursera with Daphne Koller (2012)",
            "Chief Scientist at Baidu Research (2014-2017) & Deep Speech Scaling",
            "Founder of DeepLearning.AI, Landing AI & AI Fund (2017-Present)",
            "AI is the New Electricity & Data-Centric AI Paradigm (2017-2021)",
            "Champion of Agentic Workflows & Open-Weight AI Democratization (2024-2026)",
        ],
    }
    (META_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("[OK] Initialized 08_METADATA/EP10_ANDREW_NG/manifest.json")


if __name__ == "__main__":
    main()
