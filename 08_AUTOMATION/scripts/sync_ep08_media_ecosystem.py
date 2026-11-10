#!/usr/bin/env python3
"""
EP08 Fei-Fei Li — Media Ecosystem Sync:
- Registers all 6 4K Dossiers (EP08_DOC_01..06), 16 HD Archival Video Clips (EP08_VID_ARCH_01..16),
  18 Curated Wikimedia Archival Photos (EP08_IMG_ARCH_01..18), 4 2K Flow Keyframes, and 8 4K UA Quote Cards
  into 07_DASHBOARD/data/media_acquisition_pool.js (preserving notebooklm_overview & existing audio/vfx).
- Generates 05_RAW_FOOTAGE/EP08_MEDIA_CATALOG.json & 05_RAW_FOOTAGE/EP08_MEDIA_CATALOG.md.
- Syncs 08_METADATA/EP08_FEI_FEI_LI/manifest.json.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
POOL_JS = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"
FOOTAGE_DIR = ROOT / "05_RAW_FOOTAGE"
META_DIR = ROOT / "08_METADATA" / "EP08_FEI_FEI_LI"
META_DIR.mkdir(parents=True, exist_ok=True)

EP08_DOSSIERS = [
    {
        "id": "EP08_DOC_01",
        "ep": "08",
        "act": "ACT2",
        "timecode": "06:15–07:30",
        "title": "ImageNet: A Large-Scale Hierarchical Image Database",
        "source_label": "Princeton & Stanford Vision Lab • Deng, Dong, Socher, Li, Li & Fei-Fei Li (CVPR 2009)",
        "highlight": "Hypothesis proven against all orthodoxy: algorithms do not learn like a child in a dark room — evolution spent 540 million years since the Cambrian Explosion giving biological minds continuous visual data.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_01_ACT2_FeiFeiLi_ImageNet_CVPR_2009.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_01_feifeili_imagenet.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_01.mp4",
    },
    {
        "id": "EP08_DOC_02",
        "ep": "08",
        "act": "ACT1",
        "timecode": "00:25–03:30",
        "title": "Шлях із $20 у кишені та подвійне життя у пральні Ormont Cleaners (1992–1999)",
        "source_label": "Memoir «The Worlds I See» & Princeton University Physics Scholarship Archive",
        "highlight": "Between Monday and Friday I studied Einstein's relativity under gothic Princeton arches; Friday at 4 PM I boarded New Jersey Transit and ironed shirts until Sunday night.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_02_ACT1_chengdu_parsippany_ormont_cleaners_1992.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_02_ormont_double_life.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_02.mp4",
    },
    {
        "id": "EP08_DOC_03",
        "ep": "08",
        "act": "ACT1",
        "timecode": "03:30–05:30",
        "title": "Відмова Уолл-стріт і благословення матері: шлях до біології зору в Калтеху",
        "source_label": "Stanford SIEPR & Caltech Vision / Cognitive Neuroscience PhD (1999–2005)",
        "highlight": "We did not cross an ocean and endure the steam of this laundry so you could sell your mind to a Wall Street bank. Go to Caltech and discover how we see.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_03_ACT1_princeton_caltech_neuro_vision_2005.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_03_caltech_mother_blessing.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_03.mp4",
    },
    {
        "id": "EP08_DOC_04",
        "ep": "08",
        "act": "ACT2",
        "timecode": "07:15–11:30",
        "title": "Бунт ImageNet: 14 мільйонів картинок проти відмов NSF і Маямі (2006–2009)",
        "source_label": "WordNet 22,000 Categories & 48,940+ Amazon Mechanical Turk Workers (167 Countries)",
        "highlight": "You have been trying to cure the wrong disease for thirty years. No algorithm can learn in a dark room starved of real-world visual experience.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_04_ACT2_imagenet_14m_mturk_miami_boycott_2009.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_04_imagenet_mturk_2009.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_04.mp4",
    },
    {
        "id": "EP08_DOC_05",
        "ep": "08",
        "act": "ACT3",
        "timecode": "11:30–15:15",
        "title": "Тріумф AlexNet 2012 у пологовій палаті та народження Stanford HAI (2012–2019)",
        "source_label": "ILSVRC 2012 • Stanford SAIL & HAI Founding Manifesto • AI4ALL",
        "highlight": "Technology carries no independent values of its own. At the center of every frontier algorithm must always stand human dignity, care, and inclusion.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_05_ACT3_alexnet_2012_hospital_hai_dignity_2019.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_05_alexnet_stanford_hai.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_05.mp4",
    },
    {
        "id": "EP08_DOC_06",
        "ep": "08",
        "act": "ACT4",
        "timecode": "15:15–21:30",
        "title": "World Labs 2024: Просторовий інтелект (3D) та Полярна зірка мемуарів",
        "source_label": "TED 2024 Spatial Intelligence Keynote & World Labs Manifesto",
        "highlight": "If seeing gave birth to intelligence half a billion years ago, true spatial intelligence will allow machines to perceive, reason, and act gracefully in 3D worlds.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP08_DOC_06_ACT4_world_labs_spatial_intelligence_2024_northstar.png",
        "web_preview": "assets/dossiers_preview/ep08_doc_06_world_labs_spatial_2024.jpg",
        "video_preview": "assets/video_previews/dossiers/EP08_DOC_06.mp4",
    },
]

EP08_ARCHIVES = [
    ("ARCH #01", "Акт 2 (ImageNet • Сцена TED)", "07:05–07:13", "EP08_VID_ARCH_01_ACT2_24FPS_FeiFeiLi_ImageNet_Stage.mp4",
     "Виступ Фей-Фей Лі на сцені TED про народження ImageNet",
     "TED Official Archive (40riCqvRoMs)", "https://www.youtube.com/watch?v=40riCqvRoMs", "00:06:30-00:06:38",
     "Фей-Фей Лі розповідає історію створення ImageNet на тлі візуальної сфери з мільйонів фотографій."),
    ("ARCH #02", "Акт 1 (Нью-Джерсі • $20)", "00:25–01:15", "EP08_VID_ARCH_02_ACT1_24FPS_FeiFeiLi_Immigrant_20Dollars_Parsippany_Hoover.mp4",
     "Прибуття з батьками в Парсіппані з $20 у кишені у підлітковому віці",
     "Hoover Institution (hHlpUt7Cqg8)", "https://www.youtube.com/watch?v=hHlpUt7Cqg8", "00:04:28-00:05:03",
     "Спогади про перші дні в Америці без знання мови, родичів і грошей."),
    ("ARCH #03", "Акт 1 (Прінстон & Ейнштейн)", "01:30–02:30", "EP08_VID_ARCH_03_ACT1_24FPS_FeiFeiLi_Princeton_Einstein_Physics_Hoover.mp4",
     "Чому вона подалася в Прінстон заради Ейнштейна поміж підробітків",
     "Hoover Institution (hHlpUt7Cqg8)", "https://www.youtube.com/watch?v=hHlpUt7Cqg8", "00:06:57-00:07:36",
     "Розповідь про любов до фізики поміж роботи прибиральницею, касиркою та офіціанткою."),
    ("ARCH #04", "Акт 1 (Прінстон ↔ Пральня)", "02:30–03:30", "EP08_VID_ARCH_04_ACT1_24FPS_FeiFeiLi_Laundries_Princeton_UofT.mp4",
     "Подвійне життя між аудиторіями Прінстона та роботою в пральні",
     "University of Toronto (QWWgr2rN45o)", "https://www.youtube.com/watch?v=QWWgr2rN45o", "00:23:47-00:24:26",
     "Діалог із Джеффрі Хінтоном про бідність еміграції, роботу в пральнях і пристрасть до науки."),
    ("ARCH #05", "Акт 1 (Калтех PhD • Зір)", "04:00–05:10", "EP08_VID_ARCH_05_ACT1_24FPS_FeiFeiLi_Caltech_Vision_PhD_TED2015.mp4",
     "Аспірантура в Калтеху й 15 років розгадування 3D-геометрії зору",
     "TED 2015 (40riCqvRoMs)", "https://www.youtube.com/watch?v=40riCqvRoMs", "00:03:38-00:04:18",
     "Від лабораторії в Пасадені до розуміння об'єктів, дій та тривимірного простору."),
    ("ARCH #06", "Акт 2 (Кембрій • 540 млн років)", "05:30–06:30", "EP08_VID_ARCH_06_ACT2_24FPS_FeiFeiLi_Cambrian_Explosion_Trilobites_TED2024.mp4",
     "Кембрійський вибух і перше око трилобітів 540 мільйонів років тому",
     "TED 2024 (y8NtMZ7VGmU)", "https://www.youtube.com/watch?v=y8NtMZ7VGmU", "00:00:55-00:01:38",
     "Як світлочутливі клітини живих організмів миттєво змінили еволюцію інтелекту."),
    ("ARCH #07", "Акт 2 (50K краудворкерів)", "07:30–08:50", "EP08_VID_ARCH_07_ACT2_24FPS_FeiFeiLi_Mechanical_Turk_167Countries_TED2015.mp4",
     "Майже 50 000 працівників зі 167 країн в Amazon Mechanical Turk",
     "TED 2015 (40riCqvRoMs)", "https://www.youtube.com/watch?v=40riCqvRoMs", "00:07:18-00:07:56",
     "Проривне рішення масштабування розмітки мільярда сирих фотографій з усього світу."),
    ("ARCH #08", "Акт 2 (Знову відкрити пральню)", "09:15–10:30", "EP08_VID_ARCH_08_ACT2_24FPS_FeiFeiLi_DryCleaner_Fund_ImageNet_TED2015.mp4",
     "«Я казала студентам, що знову відкрию хімчистку заради ImageNet»",
     "TED 2015 (40riCqvRoMs)", "https://www.youtube.com/watch?v=40riCqvRoMs", "00:08:14-00:08:52",
     "Боротьба з відмовами NSF і пропозиціями «зайнятися чимось кориснішим для кар'єри»."),
    ("ARCH #09", "Акт 2 (15 мільйонів вікон)", "10:30–11:30", "EP08_VID_ARCH_09_ACT2_24FPS_FeiFeiLi_ImageNet_15M_BigData_TED2024.mp4",
     "Корпус ImageNet на 15 мільйонів фото і тріумф Data-Centric підходу",
     "TED 2024 (y8NtMZ7VGmU)", "https://www.youtube.com/watch?v=y8NtMZ7VGmU", "00:02:46-00:03:20",
     "Підсумок парадигми великих візуальних даних як палива для глибокого навчання."),
    ("ARCH #10", "Акт 3 (Хінтон & Лекун CNN)", "11:30–12:30", "EP08_VID_ARCH_10_ACT3_24FPS_FeiFeiLi_Convolutional_Net_Hinton_LeCun_TED2015.mp4",
     "Згорткова нейромережа Хінтона й Лекуна на базі ImageNet (2012)",
     "TED 2015 (40riCqvRoMs)", "https://www.youtube.com/watch?v=40riCqvRoMs", "00:09:56-00:10:34",
     "Момент зустрічі величезного масиву даних зі згортковою архітектурою мозку."),
    ("ARCH #11", "Акт 3 (Торонто • Хінтон і Лі)", "12:30–13:30", "EP08_VID_ARCH_11_ACT3_24FPS_FeiFeiLi_Hinton_AlexNet_Toronto_Dialogue.mp4",
     "Діалог із Джеффрі Хінтоном про 22 000 категорій ImageNet та AlexNet",
     "University of Toronto (QWWgr2rN45o)", "https://www.youtube.com/watch?v=QWWgr2rN45o", "00:11:25-00:12:15",
     "Обидва архітектори революції 2012 року згадують кризу алгоритмів до появи великих даних."),
    ("ARCH #12", "Акт 3 (Лікарня & Сенсори)", "13:30–14:40", "EP08_VID_ARCH_12_ACT3_24FPS_FeiFeiLi_Hospital_Smart_Sensors_Ambient_TED2024.mp4",
     "Амбієнтний ШІ у лікарнях Стенфорда: додаткова пара турботливих очей",
     "TED 2024 (y8NtMZ7VGmU)", "https://www.youtube.com/watch?v=y8NtMZ7VGmU", "00:11:34-00:12:14",
     "Інфрачервоні сенсори глибини запобігають падінням пацієнтів і допомагають медсестрам."),
    ("ARCH #13", "Акт 3 (Людська гідність)", "14:40–15:25", "EP08_VID_ARCH_13_ACT3_24FPS_FeiFeiLi_Human_Dignity_Agency_TimFerriss.mp4",
     "Гідність людини й право на майбутнє понад автоматизацією",
     "Tim Ferriss Show (z1g1kkA1M-8)", "https://www.youtube.com/watch?v=z1g1kkA1M-8", "00:41:50-00:42:26",
     "Етичне кредо Stanford HAI: ШІ має підсилювати гідність, а не відбирати суб'єктність."),
    ("ARCH #14", "Акт 4 (Просторовий ШІ • 3D)", "15:30–17:00", "EP08_VID_ARCH_14_ACT4_24FPS_FeiFeiLi_Spatial_Intelligence_3D_Space_TED2024.mp4",
     "Просторовий інтелект: коли машини бачать і діють у 3D-просторі й часі",
     "TED 2024 (y8NtMZ7VGmU)", "https://www.youtube.com/watch?v=y8NtMZ7VGmU", "00:05:32-00:06:08",
     "Ключовий перехід від пласких двовимірних пікселів до повної геометрії реального світу."),
    ("ARCH #15", "Акт 4 (World Labs • Цивілізація)", "17:00–19:00", "EP08_VID_ARCH_15_ACT4_24FPS_FeiFeiLi_World_Labs_Mission_TimFerriss.mp4",
     "Чому Фей-Фей Лі створила World Labs: технології для побудови цивілізацій",
     "Tim Ferriss Show (z1g1kkA1M-8)", "https://www.youtube.com/watch?v=z1g1kkA1M-8", "00:46:06-00:46:44",
     "Стратегічна візія тривимірних моделей світу для науки, дизайну та фізичної робототехніки."),
    ("ARCH #16", "Акт 4 (Голос іммігрантів • HAI)", "19:30–21:30", "EP08_VID_ARCH_16_ACT4_24FPS_FeiFeiLi_Young_Immigrants_Voice_StanfordHAI.mp4",
     "Для чого було написано «Світи, які я бачу» — голос жінок і дітей іммігрантів",
     "Stanford HAI (HiSK7nv-i94)", "https://www.youtube.com/watch?v=HiSK7nv-i94", "00:08:12-00:08:46",
     "Фінальне напуття молодим дослідникам усього світу: ваш нестандартний шлях має значення."),
]

EP08_PHOTOS = [
    ("EP08_PH_01", "ФОТО #01 (1976–1992 • Ченду)", "Історична вулиця Сичуань у Ченду — місто юності Фей-Фей Лі", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Huanglongxi_-_Flickr_-_xiquinhosilva.jpg", "ep08_img_arch_01_chengdu_sichuan_heritage_street.jpg", "Автентична сичуаньська архітектура провінції Ченду, де зростала майбутня вчена."),
    ("EP08_PH_02", "ФОТО #02 (Камера батька)", "Механічний 35-мм фотоапарат із оптикою — ремонт фотокамер її батька", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Vintage_Minolta_SR-T_101_35mm_SLR_Camera_with_MC_Rokkor,_PF_1-14,_f_%3D_58_Minolta_Lens,_Also_35mm_F2.8_and_135mm_F2.8_Lens_(9102234387).jpg", "ep08_img_arch_02_father_repaired_35mm_camera_lens.jpg", "Символ батьківського інженерного інтересу до оптики і фотокамер, які він лагодив в еміграції."),
    ("EP08_PH_03", "ФОТО #03 (1992 • Словник)", "Англо-китайський словник — нічні переклади підручників фізики", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Oxford_Advanced_Learner%27s_English-Chinese_Dictionary_7th_Edition.jpg", "ep08_img_arch_03_english_chinese_study_dictionary.jpg", "Двомовний словник, через який 16-річна школярка в Парсіппані перекладала кожне слово формул."),
    ("EP08_PH_04", "ФОТО #04 (Парсіппані • Ранок)", "Робота за дошкою прасування біля вікна — емігрантська витривалість", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Young_man_ironing_a_T_shirt,_Auckland_-_0964.jpg", "ep08_img_arch_04_immigrant_laundry_pressing_steam_silhouette.jpg", "Мовчазна праця біля праски та світло ранкового вікна, що викували залізний характер."),
    ("EP08_PH_05", "ФОТО #05 (Ormont Cleaners)", "Руки та важка гаряча праска на полотні — вихідні у хімчистці", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:A_Local_Taylor_ironing_cloth.jpg", "ep08_img_arch_05_ormont_cleaners_heavy_iron_press.jpg", "Щоп'ятниці о 16:00 студентка Прінстона міняла формули на важку ручну працю пральні."),
    ("EP08_PH_06", "ФОТО #06 (1995–1999 • Прінстон)", "Корпус Nassau Hall у Прінстоні в сутінках — стипендія й фізика", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Nassau_Hall_Princeton_Uni.JPG", "ep08_img_arch_06_princeton_nassau_hall_dusk_physics.jpg", "Кампус Прінстонського університету, де Лі вивчала квантову фізику й теорію відносності."),
    ("EP08_PH_07", "ФОТО #07 (1999 • Уолл-стріт)", "Нью-Йоркська фондова біржа — пропозиції банків, від яких вона відмовилася", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:New_York_Stock_Exchange_August_2017_02.jpg", "ep08_img_arch_07_wall_street_nyse_rejected_offers.jpg", "Велика зарплата Уолл-стріт могла б миттєво закрити борги пральні, але мати благословила доньку на науку."),
    ("EP08_PH_08", "ФОТО #08 (1999–2005 • Калтех)", "Інститут Бекмана у Калтеху (Пасадена) — PhD з нейробіології зору", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Beckman_Institute_at_Caltech.jpg", "ep08_img_arch_08_caltech_beckman_institute_pasadena.jpg", "Калтех, де під керівництвом Перони й Коха вона досліджувала природу зорового сприйняття людини."),
    ("EP08_PH_09", "ФОТО #09 (Кембрій • 540 млн)", "Скам'янілі трилобіти Кембрію — перші живі очі на планеті", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Agnostoid_trilobite_packstone_(Alum_Shale_Formation,_Upper_Cambrian;_southern_Sweden)_1.jpg", "ep08_img_arch_09_cambrian_trilobite_evolution_eyes.jpg", "Метафора Фей-Фей Лі про 540 мільйонів років оптичного досвіду біологічної еволюції."),
    ("EP08_PH_10", "ФОТО #10 (2006 • Загадка кота)", "Згорнутий кіт у тіні — класичний тест, на якому сліпли ручні алгоритми", "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Sleeping_cat_curled_up.JPG", "ep08_img_arch_10_sleeping_cat_computer_vision_challenge.jpg", "До появи великих даних комп'ютери не могли впізнати навіть кота, що згорнувся клубочком."),
    ("EP08_PH_11", "ФОТО #11 (Стенфорд • Gates CS)", "Будівля Gates Computer Science у Стенфорді — директорка Stanford AI Lab", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Gates_Computer_Science_Building_(2025)-L1007406.jpg", "ep08_img_arch_11_stanford_gates_cs_sail_building.jpg", "Осередок Stanford Vision Lab і SAIL, де дозріла ідея щорічного чемпіонату ImageNet."),
    ("EP08_PH_12", "ФОТО #12 (2012 • Крива ImageNet)", "Історичний графік падіння похибки ImageNet після прориву AlexNet 2012", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:ImageNet_error_rate_history.svg", "ep08_img_arch_12_imagenet_alexnet_error_rate_crash.jpg", "Документальна візуалізація драматичного зламу точності розпізнавання у 2012 році."),
    ("EP08_PH_13", "ФОТО #13 (2017–2018 • Google)", "Корпус №43 Googleplex — головна вчена ШІ у Google Cloud", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Googleplex_building_43.jpg", "ep08_img_arch_13_googleplex_cloud_ai_2017.jpg", "Період академічної відпустки в Google, коли вона переносила комп'ютерний зір в індустрію."),
    ("EP08_PH_14", "ФОТО #14 (Женева • 2017)", "Виступ Фей-Фей Лі на глобальному саміті ООН AI for Good (2017)", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Fei-Fei_Li_at_AI_for_Good_2017.jpg", "ep08_img_arch_14_feifei_li_ai_for_good_2017_keynote.jpg", "Офіційний портрет вченої на трибуні ITU щодо гуманістичного розвитку технологій."),
    ("EP08_PH_15", "ФОТО #15 (Stanford HAI)", "Круглий стіл Інституту людиноцентричного ШІ у Стенфорді (Stanford HAI)", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:HAI_Roundtable_on_AI_and_the_Economy.jpg", "ep08_img_arch_15_stanford_hai_roundtable_feifei_li.jpg", "Робоча дискусія за участю Фей-Фей Лі навколо етики, економіки та права людини у добу ШІ."),
    ("EP08_PH_16", "ФОТО #16 (Медицина милосердя)", "Палата інтенсивної терапії з пацієнткою — джерело медичних проєктів ШІ", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Patient_lying_in_bed_in_intensive_care_unit_of_hospital_with_apparatuses_and_hemodialysis_machine.jpg", "ep08_img_arch_16_hospital_bedside_ambient_healthcare_ai.jpg", "Після важкої хвороби матері Фей-Фей Лі спрямувала сенсори глибини на захист пацієнтів у лікарнях."),
    ("EP08_PH_17", "ФОТО #17 (Відзнака 2024)", "Експозиція глобальної гуманітарної нагороди ім. Джеймса Моргана — Др. Фей-Фей Лі", "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:The_Tech_for_Global_Good,_The_Tech_Interactive,_San_Jose,_California_01.jpg", "ep08_img_arch_17_feifei_li_global_humanitarian_award_2024.jpg", "Визнання в Кремнієвій долині у 2024 році за поєднання фундаментальної науки й людяності."),
    ("EP08_PH_18", "ФОТО #18 (World Labs • 3D LiDAR)", "Тривимірна LiDAR-реконструкція кварталу Сан-Франциско — Просторовий інтелект", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Ouster_OS1-64_lidar_point_cloud_of_intersection_of_Folsom_and_Dore_St,_San_Francisco.png", "ep08_img_arch_18_world_labs_3d_spatial_point_cloud.jpg", "Математика просторової геометрії та глибини 3D-світів, над якими працює World Labs."),
]

EP08_QUOTES_CARDS = [
    ("UA #01 (4K • 10с)", "00:00–00:35", "ep08_ua_clip_card_01_cambrian_eye_540m_10s", "Кембрійський вибух першого ока й народження зору машин"),
    ("UA #02 (4K • 10с)", "01:45–03:30", "ep08_ua_clip_card_02_ormont_double_life_10s", "Прінстон у будні й пара пральні Ormont Cleaners на вихідних"),
    ("UA #03 (4K • 10с)", "03:30–05:30", "ep08_ua_clip_card_03_mother_blessing_1999_10s", "Благословення матері: відмова від Уолл-стріт заради Калтеху"),
    ("UA #04 (4K • 10с)", "05:30–07:15", "ep08_ua_clip_card_04_dark_basement_data_10s", "Жоден алгоритм не оживе в темному підвалі без даних"),
    ("UA #05 (4K • 10с)", "07:15–11:30", "ep08_ua_clip_card_05_imagenet_14m_miami_10s", "50 000 людей і 14 мільйонів вікон ImageNet у світ (CVPR 2009)"),
    ("UA #06 (4K • 10с)", "11:30–13:30", "ep08_ua_clip_card_06_maternity_ward_alexnet_10s", "Пологова палата 2012: дзвінок про прорив AlexNet"),
    ("UA #07 (4K • 12с)", "13:30–15:15", "ep08_ua_clip_card_07_hai_human_dignity_12s", "Stanford HAI: у центрі кожного алгоритму — гідність людини"),
    ("UA #08 (4K • 12с)", "15:15–21:30", "ep08_ua_clip_card_08_spatial_north_star_finale_12s", "World Labs Spatial Intelligence (3D) & Полярна зірка"),
]

EP08_FLOW_KEYFRAMES = [
    ("KF #01 (2K)", "05:30–07:30", "Human Eye Merging With Data Streams (Оптична кора зустрічає 14 млн картинок)",
     "assets/flow_keyframes/ep08_flow_img_01_human_eye_data.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP08_FLOW_IMG_01_Human_Eye_Merging_With_Data_2K.jpg"),
    ("KF #02 (2K)", "15:15–17:00", "Silhouettes Morphing Into 3D Wireframe (Перехід із 2D-тіней у 3D-геометрію World Labs)",
     "assets/flow_keyframes/ep08_flow_img_02_silhouettes_wireframe.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP08_FLOW_IMG_02_Silhouettes_Morphing_Into_3D_Wireframe_2K.jpg"),
    ("KF #03 (2K)", "17:00–19:00", "Painter Holding Glowing Brush (Творче ремесло візуального світу людини й ШІ)",
     "assets/flow_keyframes/ep08_flow_img_03_painter_glowing_brush.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP08_FLOW_IMG_03_Painter_Holding_Glowing_Brush_2K.jpg"),
    ("KF #04 (2K)", "13:30–15:15", "Robotic Arms Weaving Golden Tapestry (Ніжна допомога амбієнтних машин людині)",
     "assets/flow_keyframes/ep08_flow_img_04_robotic_arms_tapestry.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP08_FLOW_IMG_04_Robotic_Arms_Weaving_Golden_Tapestry_2K.jpg"),
]


def main():
    raw_txt = POOL_JS.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    pool = json.loads(raw_txt[len(prefix):].rstrip(";\n "))
    ep8 = pool["08"]

    ep8["dossiers"] = EP08_DOSSIERS

    archives_list = []
    for code, act, tc, fn, title, src, url, sec, note in EP08_ARCHIVES:
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
    ep8["archives"] = archives_list

    photos_list = []
    for pid, code, title, src, url, fn, desc in EP08_PHOTOS:
        photos_list.append({
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_feifei/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        })
    ep8["archival_photos"] = photos_list

    gallery = []
    for code, tc, title, web_p, raw_p in EP08_FLOW_KEYFRAMES:
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
    for code, tc, slug, desc in EP08_QUOTES_CARDS:
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
    ep8["flow_gallery"] = gallery

    POOL_JS.write_text(prefix + json.dumps(pool, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"[OK] Updated {POOL_JS} EP08: dossiers={len(ep8['dossiers'])}, archives={len(ep8['archives'])}, photos={len(ep8['archival_photos'])}, gallery={len(ep8['flow_gallery'])}")

    catalog_json = {
        "episode": "EP08",
        "hero": "Fei-Fei Li",
        "dossiers_4k": EP08_DOSSIERS,
        "archives_1080p": archives_list,
        "archival_photos": photos_list,
        "flow_gallery": gallery,
    }
    (FOOTAGE_DIR / "EP08_MEDIA_CATALOG.json").write_text(json.dumps(catalog_json, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# EP08 — Фей-Фей Лі: Повний Каталог Медіа-Асетів",
        "",
        f"- **4K Досьє-плашки (`05_RAW_FOOTAGE/dossiers_press/`):** {len(EP08_DOSSIERS)}",
        f"- **HD Архівні відеокліпи 1080p24 (`05_RAW_FOOTAGE/archives/`):** {len(archives_list)}",
        f"- **Фотоархів Wikimedia Commons (`05_RAW_FOOTAGE/speaker_portraits/young_feifei/`):** {len(photos_list)}",
        f"- **2K Flow Ключові кадри & 4K UA Цитат-Картки:** {len(gallery)}",
        "",
        "## Архівні відеокліпи (16 HD)",
    ]
    for a in archives_list:
        md_lines.append(f"- `{a['code']}` [{a['tc']}] **{a['file']}** — {a['title']}")
    md_lines.append("\n## Фотоархів Wikimedia Commons (18)")
    for p in photos_list:
        md_lines.append(f"- `{p['code']}` **{p['id']}** — {p['title']} (`{p['raw_file']}`)")
    (FOOTAGE_DIR / "EP08_MEDIA_CATALOG.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print("[OK] Generated EP08_MEDIA_CATALOG.json & EP08_MEDIA_CATALOG.md")

    manifest = {
        "episode_id": "EP08",
        "hero": "Fei-Fei Li",
        "title": "Очі машин та пара пральні",
        "bpm": 92,
        "status": "MEDIA_AND_RESEARCH_SYNCED",
        "source_count": 16,
        "archival_video_count": len(archives_list),
        "archival_photo_count": len(photos_list),
        "dossier_4k_count": len(EP08_DOSSIERS),
        "ua_quote_card_count": len(EP08_QUOTES_CARDS),
        "verified_milestones": [
            "Childhood in Chengdu, Emigration to Parsippany NJ at Age 16 (1992)",
            "Double Life: Princeton Physics Scholarship & Working Weekends at Ormont Cleaners (1995-1999)",
            "PhD in Electrical Engineering / Neurobiology at Caltech (2005)",
            "The Rebellion of ImageNet: Crowdsourcing 14M Images on MTurk Against Grants Rejection (2006-2009)",
            "AlexNet Historic Breakthrough on ImageNet Benchmark (2012)",
            "Director of Stanford AI Lab (SAIL) & Chief Scientist of AI at Google Cloud (2013-2018)",
            "Co-Founding AI4ALL Non-Profit to Expand Underrepresented Access (2017)",
            "Founding Co-Director of the Stanford Institute for Human-Centered AI (HAI) (2019)",
            "Publication of Acclaimed Memoir 'The Worlds I See' (2023)",
            "Founding World Labs to Pioneer Spatial Intelligence ($230M+ Seed, 2024)",
        ],
    }
    (META_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("[OK] Initialized 08_METADATA/EP08_FEI_FEI_LI/manifest.json")


if __name__ == "__main__":
    main()
