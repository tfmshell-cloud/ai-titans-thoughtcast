#!/usr/bin/env python3
"""
EP09 Yoshua Bengio — Media Ecosystem Sync:
- Registers all 6 4K Dossiers (EP09_DOC_01..06), 16 HD Archival Video Clips (EP09_VID_ARCH_01..16),
  18 Curated Wikimedia Archival Photos (EP09_IMG_ARCH_01..18), 6 Flow Keyframes + 8 4K UA Quote Cards
  into 07_DASHBOARD/data/media_acquisition_pool.js (preserving existing audio, sci_vfx, flow_keyframes).
- Generates 05_RAW_FOOTAGE/EP09_MEDIA_CATALOG.json & 05_RAW_FOOTAGE/EP09_MEDIA_CATALOG.md.
- Syncs 08_METADATA/EP09_YOSHUA_BENGIO/manifest.json.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
POOL_JS = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"
FOOTAGE_DIR = ROOT / "05_RAW_FOOTAGE"
META_DIR = ROOT / "08_METADATA" / "EP09_YOSHUA_BENGIO"
META_DIR.mkdir(parents=True, exist_ok=True)

EP09_DOSSIERS = [
    {
        "id": "EP09_DOC_01",
        "ep": "09",
        "act": "ACT2",
        "timecode": "06:40–07:55",
        "title": "Neural Machine Translation by Jointly Learning to Align and Translate",
        "source_label": "Bahdanau, Cho & Bengio (ICLR 2015) + U.S. Senate Judiciary Testimony (2023)",
        "highlight": "This soft-alignment mechanism — quickly christened 'Attention' — became the direct mathematical cornerstone of the 2017 Transformer ('Attention Is All You Need') and every modern LLM.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_01_ACT2_Bengio_Attention_Bahdanau_2014.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_01_bengio_attention.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_01.mp4",
    },
    {
        "id": "EP09_DOC_02",
        "ep": "09",
        "act": "ACT1",
        "timecode": "00:25–03:30",
        "title": "Театр батька в Парижі, союз у Bell Labs та повернення до Університету Монреаля (1964–1993)",
        "source_label": "Paris Roots, McGill PhD (1991), MIT, AT&T Bell Labs & Université de Montréal",
        "highlight": "I have chosen to stay in university, to work for the public good, to guide the next generation, and to remain free to speak the truth.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_02_ACT1_paris_mcgill_bell_labs_montreal_1993.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_02_paris_mcgill_bell_labs.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_02.mp4",
    },
    {
        "id": "EP09_DOC_03",
        "ep": "09",
        "act": "ACT2",
        "timecode": "03:30–07:15",
        "title": "20 років зими ШІ та «геометрія слів» (A Neural Probabilistic Language Model, 2000)",
        "source_label": "NIPS 2000 / JMLR 2003 (Bengio, Ducharme, Vincent, Janvin) & HLF Turing Lecture",
        "highlight": "By learning a distributed vector representation for each word in semantic space, the neural model breaks the curse of dimensionality forever.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_03_ACT2_word_embeddings_2000_ai_winter_open_lab.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_03_ai_winter_word_vectors.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_03.mp4",
    },
    {
        "id": "EP09_DOC_04",
        "ep": "09",
        "act": "ACT2",
        "timecode": "07:15–11:15",
        "title": "Механізм Уваги (2014), GAN після пабу, відмова від мільярдів та інститут Mila",
        "source_label": "ICLR 2015 (arXiv 1409.0473) • Mila Montreal (1,000+ Researchers) • Turing Award 2018",
        "highlight": "If I took your tens of millions, I would no longer belong to humanity — I would belong to your shareholders. Someone must stay free.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_04_ACT2_attention_2014_gan_mila_refusing_billions.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_04_attention_gan_mila_2014.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_04.mp4",
    },
    {
        "id": "EP09_DOC_05",
        "ep": "09",
        "act": "ACT3",
        "timecode": "11:15–16:45",
        "title": "Бунт сумління 2023: Міжнародний звіт безпеки ООН, GFlowNets і ШІ-Вчений (Система 2)",
        "source_label": "US Senate Judiciary 2023 • International AI Safety Report 2025 • arXiv GFlowNets & Scientist AI",
        "highlight": "We must stop rushing to build unchecked autonomous agents seeking self-preservation, and build Scientist AI anchored in epistemic humility.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_05_ACT3_un_ai_safety_report_system2_gflownets.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_05_system2_gflownets_un_report.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_05.mp4",
    },
    {
        "id": "EP09_DOC_06",
        "ep": "09",
        "act": "ACT4",
        "timecode": "16:45–21:00",
        "title": "Монреальська декларація та Кодекс Вільної Людини: велосипедом крізь сніги Квебеку",
        "source_label": "Montreal Declaration for a Responsible Development of AI (2018) & Guardian Code",
        "highlight": "Science without humanism is merely the cold blueprint of a machine in an empty void. We endure only as long as guardians keep their compass of conscience.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP09_DOC_06_ACT4_montreal_declaration_conscience_compass.png",
        "web_preview": "assets/dossiers_preview/ep09_doc_06_montreal_declaration_compass.jpg",
        "video_preview": "assets/video_previews/dossiers/EP09_DOC_06.mp4",
    },
]

EP09_ARCHIVES = [
    ("ARCH #01", "Акт 3 (Сенат США • 2023)", "11:30–11:38", "EP09_VID_ARCH_01_ACT3_24FPS_Bengio_Senate_Testimony.mp4",
     "Виступ Йошуа Бенжіо в Сенаті США про ризики втрати контролю",
     "U.S. Senate Judiciary (hm1zexCjELo)", "https://www.youtube.com/watch?v=hm1zexCjELo", "00:27:40-00:27:48",
     "Йошуа Бенжіо попереджає законодавців про втрату людського контролю над автономними агентами."),
    ("ARCH #02", "Акт 1 (Батьки & Париж '68)", "00:25–01:15", "EP09_VID_ARCH_02_ACT1_24FPS_Bengio_Parents_Freedom_Sixties_RobotBrains.mp4",
     "Свобода дитинства та бунтівний дух батька з 1960-х",
     "The Robot Brains Podcast (wdExmzSfw4g)", "https://www.youtube.com/watch?v=wdExmzSfw4g", "01:22:55-01:23:37",
     "Спогади про виховання батьками: чому свобода ставити під сумнів усе є фундаментом ученого."),
    ("ARCH #03", "Акт 1 (Макгілл • Хінтон)", "01:45–02:45", "EP09_VID_ARCH_03_ACT1_24FPS_Bengio_Reading_Hinton_McGill_HLF.mp4",
     "Відкриття нейромереж у 1980-х і вплив ідей Джеффрі Хінтона",
     "Heidelberg Laureate Forum (llGG62fNN64)", "https://www.youtube.com/watch?v=llGG62fNN64", "00:04:15-00:04:58",
     "Офіційна Тюрінгівська лекція: як концепція синергії простих нейронів і праці Хінтона запалили шлях Бенжіо."),
    ("ARCH #04", "Акт 1 (Вибір академії)", "02:45–03:45", "EP09_VID_ARCH_04_ACT1_24FPS_Bengio_Academic_Independence_TEDxMontreal.mp4",
     "Чому Бенжіо залишився в університеті замість божевільних зарплат корпорацій",
     "TEDxMontreal (uawLjkSI7Mo)", "https://www.youtube.com/watch?v=uawLjkSI7Mo", "00:13:58-00:14:38",
     "Коли колеги масово переходили в індустрію за великими чеками, Бенжіо обрав свободу й студентів Монреаля."),
    ("ARCH #05", "Акт 1 (Зима ШІ → Хаб Монреаль)", "03:45–05:15", "EP09_VID_ARCH_05_ACT1_24FPS_Bengio_AI_Winter_Abandoned_Nets_TEDxMontreal.mp4",
     "Роки покинутих нейромереж і перетворення Монреаля на світовий центр",
     "TEDxMontreal (uawLjkSI7Mo)", "https://www.youtube.com/watch?v=uawLjkSI7Mo", "00:12:25-00:13:12",
     "Як невелика лабораторія вижила під час «зими ШІ» й перетворила Квебек на столицю глибокого навчання."),
    ("ARCH #06", "Акт 2 (Вектори слів • 2000)", "05:15–06:20", "EP09_VID_ARCH_06_ACT2_24FPS_Bengio_Distributed_Word_Vectors_HLF.mp4",
     "Розподілені векторні представлення слів (кіт і собака поруч у просторі)",
     "Heidelberg Laureate Forum (llGG62fNN64)", "https://www.youtube.com/watch?v=llGG62fNN64", "00:05:00-00:05:45",
     "Пояснення роботи «Neural Probabilistic Language Model»: слова набувають вивчених векторів атрибутів."),
    ("ARCH #07", "Акт 2 (10 років тиші NLP)", "06:20–07:15", "EP09_VID_ARCH_07_ACT2_24FPS_Bengio_Neural_NLP_Ten_Years_Unnoticed_HLF.mp4",
     "Непомічена стаття 2000 року, що через 15 років підкорила всю мовну індустрію",
     "Heidelberg Laureate Forum (llGG62fNN64)", "https://www.youtube.com/watch?v=llGG62fNN64", "00:17:38-00:18:18",
     "Двовимірні мапи змісту слів і історія того, як скепсис перетворився на стандарт усього NLP."),
    ("ARCH #08", "Акт 2 (Книга і Attention 2014)", "07:15–08:30", "EP09_VID_ARCH_08_ACT2_24FPS_Bengio_Attention_Translating_Book_REWORK.mp4",
     "Переклад цілої книги vs фокусування променя уваги на одному слові (2014)",
     "RE•WORK Deep Learning (GibjI5FoZsE)", "https://www.youtube.com/watch?v=GibjI5FoZsE", "00:25:42-00:26:28",
     "Класична метафора Бенжіо: чому не можна стиснути всю книгу в один вектор перед початком перекладу."),
    ("ARCH #09", "Акт 2 (Soft Attention & Google)", "08:30–09:40", "EP09_VID_ARCH_09_ACT2_24FPS_Bengio_Soft_Attention_GoogleTranslate_HLF.mp4",
     "Як content-based soft attention перевернув машинний переклад та Transformer",
     "Heidelberg Laureate Forum (llGG62fNN64)", "https://www.youtube.com/watch?v=llGG62fNN64", "00:25:05-00:25:52",
     "Історія винаходу м'якого вирівнювання 2014 року, який заклав серце всіх сучасних LLM."),
    ("ARCH #10", "Акт 2 (Mila • Клімат & Медицина)", "09:45–11:15", "EP09_VID_ARCH_10_ACT2_24FPS_Bengio_Mila_Medicine_Climate_TED2024.mp4",
     "Відмова переходити в техкорпорації 2012-го заради медицини та клімату",
     "TED Official Archive (qe9QSCF-d88)", "https://www.youtube.com/watch?v=qe9QSCF-d88", "00:02:56-00:03:38",
     "Бенжіо пояснює, чому залишився в академії й спрямував Mila на діагностику хвороб та кліматичні дослідження."),
    ("ARCH #11", "Акт 3 (Тюрінг • Система 1 і 2)", "13:15–14:30", "EP09_VID_ARCH_11_ACT3_24FPS_Bengio_Turing_Pioneers_System2_AAAI2020.mp4",
     "Лауреати Премії Тюрінга AAAI 2020: перехід від Системи 1 до Системи 2",
     "AAAI 2020 Keynote (UX8OubxsY8w)", "https://www.youtube.com/watch?v=UX8OubxsY8w", "01:12:58-01:13:45",
     "Пояснення інтуїтивної Системи 1 та послідовного свідомого міркування Системи 2 Канемана."),
    ("ARCH #12", "Акт 3 (GFlowNets & Молекули)", "14:30–15:30", "EP09_VID_ARCH_12_ACT3_24FPS_Bengio_GFlowNets_Molecules_MSR.mp4",
     "Потокові мережі GFlowNets для пошуку нових молекул та антибіотиків",
     "Microsoft Research (647kOjU3TlE)", "https://www.youtube.com/watch?v=647kOjU3TlE", "00:28:38-00:29:22",
     "Технічна презентація графового семпліювання GFlowNets для наукових відкриттів у фармакології."),
    ("ARCH #13", "Акт 3 (Онук Кларенс & 2023)", "11:45–13:00", "EP09_VID_ARCH_13_ACT3_24FPS_Bengio_Grandson_DiaryOfACEO.mp4",
     "Чому інтроверт вийшов на світову сцену: погляд в очі маленького онука",
     "The Diary Of A CEO (zQ1POHiR8m8)", "https://www.youtube.com/watch?v=zQ1POHiR8m8", "00:00:35-00:01:16",
     "Особисте зізнання про переломний 2023 рік і страх за життя онука через неконтрольованих агентів."),
    ("ARCH #14", "Акт 3 (Scientist AI & Смирення)", "15:30–16:45", "EP09_VID_ARCH_14_ACT3_24FPS_Bengio_ScientistAI_Humility_TED2024.mp4",
     "ШІ-Вчений (Scientist AI): чистий дослідник без егоїстичної волі",
     "TED Official Archive (qe9QSCF-d88)", "https://www.youtube.com/watch?v=qe9QSCF-d88", "00:10:25-00:11:08",
     "Архітектурна альтернатива небезпечним агентам: неагентивний ШІ-охоронець без інстинкту виживання."),
    ("ARCH #15", "Акт 4 (Звіт ООН • 30 країн)", "16:45–18:15", "EP09_VID_ARCH_15_ACT4_24FPS_Bengio_UN_Safety_Report_CanadaSenate.mp4",
     "Очільник Міжнародного звіту з безпеки ШІ ООН, ЄС, ОЕСР і 30 країн",
     "Canadian Senate Testimony (A7mPKpk7NGk)", "https://www.youtube.com/watch?v=A7mPKpk7NGk", "00:09:37-00:10:22",
     "Офіційні свідчення у Сенаті Канади про заснування LawZero та незалежну експертизу ООН."),
    ("ARCH #16", "Акт 4 (Заповіт надії • Фінал)", "19:15–21:00", "EP09_VID_ARCH_16_ACT4_24FPS_Bengio_Introvert_Love_Future_TED2024.mp4",
     "Ставка на любов і захист радості майбутніх поколінь",
     "TED Official Archive (qe9QSCF-d88)", "https://www.youtube.com/watch?v=qe9QSCF-d88", "00:12:08-00:12:52",
     "Зворушливе послання вченого-інтроверта про ШІ як глобальне суспільне благо під демократичним контролем."),
]

EP09_PHOTOS = [
    ("EP09_PH_01", "ФОТО #01 (1964–1976 • Париж)", "Латинський квартал Парижа 1970-х — роки дитинства Йошуа Бенжіо", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Latin_Quarter_rue_Monsieur_Le_Prince_October_1978.jpg", "ep09_img_arch_01_paris_latin_quarter_1978_roots.jpg", "Атмосфера богемного Парижа, де в родині митців цінували думку й чесність понад гроші."),
    ("EP09_PH_02", "ФОТО #02 (Театр батька)", "Сцена Théâtre de Paris — творчий світ батька Карло Бенжіо", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Theatre_de_Paris_-_Plateau.jpg", "ep09_img_arch_02_paris_theatre_father_carlo_stage.jpg", "Символ сефардського театру, заради якого аптекар Карло Бенжіо полишив бізнес."),
    ("EP09_PH_03", "ФОТО #03 (Монреаль • Азімов)", "Айзек Азімов — книжки «Фундації», які надихнули братів Бенжіо", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Isaac.Asimov01.jpg", "ep09_img_arch_03_isaac_asimov_foundation_youth.jpg", "Читаючи Азімова у 12 років після переїзду до Монреаля, Йошуа та Самі мріяли про науку розуму."),
    ("EP09_PH_04", "ФОТО #04 (1991 • Макгілл)", "Історичний корпус Arts Building Університету Макгілла — захист PhD", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Arts_Building,_McGill_University,_Aug_31_2022.jpg", "ep09_img_arch_04_mcgill_university_arts_phd_1991.jpg", "Університет Макгілла в Монреалі, де у 1980-х аспірант Бенжіо прочитав перші статті Хінтона."),
    ("EP09_PH_05", "ФОТО #05 (1992 • Bell Labs)", "AT&T Bell Labs Холмдел — союз Хінтона, Лекуна й Бенжіо у Нью-Джерсі", "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Bell_Labs_Holmdel.jpg", "ep09_img_arch_05_att_bell_labs_holmdel_lecun_pact.jpg", "Легендарна лабораторія, де молодий постдок працював поряд із Яном Лекуном перед поверненням до Канади."),
    ("EP09_PH_06", "ФОТО #06 (1993 • УдМ)", "Вежа Pavillon Roger-Gaudry в Університеті Монреаля — кафедра Бенжіо", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Pavillon_Roger-Gaudry_II.jpg", "ep09_img_arch_06_universite_de_montreal_roger_gaudry_1993.jpg", "Тиха франкомовна фортеця науки, куди Бенжіо повернувся 1993 року, відмовившись від перегонів США."),
    ("EP09_PH_07", "ФОТО #07 (Зима ШІ • Монреаль)", "Засніжений Монреаль з гори Мон-Рояль — 20 років самотньої зими ШІ", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:View_of_Montreal_in_winter_from_Mount_Royal.JPG", "ep09_img_arch_07_montreal_mount_royal_winter_skyline.jpg", "Місто, де без грантів і секретів зростала відкрита родина молодих дослідників нейромереж."),
    ("EP09_PH_08", "ФОТО #08 (2000 • Вектори)", "Зелена математична дошка з імовірнісними рівняннями — прорив 2000 року", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:CMAP_-_Centre_de_Math%C3%A9matiques_Appliqu%C3%A9es_de_l%27Ecole_polytechnique.jpg", "ep09_img_arch_08_word_embeddings_math_blackboard_2000.jpg", "Символ роботи «A Neural Probabilistic Language Model», що перетворила слова на геометричні вектори."),
    ("EP09_PH_09", "ФОТО #09 (2014 • Attention)", "Схема багатоголової перехресної уваги (Encoder Cross-Attention)", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Encoder_cross-attention,_multiheaded_version.png", "ep09_img_arch_09_attention_mechanism_encoder_cross_2014.jpg", "Механізм фокусування погляду на ключові слова оригіналу (Bahdanau, Cho, Bengio, 2014)."),
    ("EP09_PH_10", "ФОТО #10 (Бульвар Сен-Лоран)", "Вечірній бульвар Сен-Лоран поблизу Міле-Екс — серце спільноти Mila", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Boulevard_Saint-Laurent,_Montreal,_Quebec_(30033445196).jpg", "ep09_img_arch_10_montreal_boulevard_saint_laurent_mila.jpg", "Квартал Монреаля, де розташовано штаб-квартиру інституту Mila з понад 1000 учених."),
    ("EP09_PH_11", "ФОТО #11 (Голос відкритої науки)", "Йошуа Бенжіо за трибуною: виступ про незалежну фундаментальну науку", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:SD_2025_-_Yoshua_Bengio_01.jpg", "ep09_img_arch_11_yoshua_bengio_open_science_portrait.jpg", "Професор, який відмовився від багатомільйонних корпоративних пропозицій заради відкритого знання."),
    ("EP09_PH_12", "ФОТО #12 (GFlowNets • Ліки)", "Тривимірна молекулярна структура — пошук антибіотиків через GFlowNets", "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:4,4%27-Diaminodiphenylmethane-3D-molecular-model-engraved-render-CAS-101-77-9.png", "ep09_img_arch_12_gflownet_molecular_drug_discovery.jpg", "Імовірнісний пошук різноманітних кандидатів молекул для медицини й чистої енергії."),
    ("EP09_PH_13", "ФОТО #13 (ICLR Keynote)", "Йошуа Бенжіо на міжнародній науковій сцені ICLR", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:ICLR_2025_-_Yoshua_Bengio_04.jpg", "ep09_img_arch_13_yoshua_bengio_iclr_keynote_stage.jpg", "Найцитованіший живий комп'ютерний вчений світу презентує дослідження безпечного ШІ."),
    ("EP09_PH_14", "ФОТО #14 (2023 • Капітолій)", "Капітолій США у сутінках — слухання Сенату щодо нагляду за ШІ (2023)", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Capitol_at_Dusk_2.jpg", "ep09_img_arch_14_us_capitol_senate_judiciary_2023.jpg", "Після виходу GPT-4 та роздумів про майбутнє онука Бенжіо виступив перед законодавцями США."),
    ("EP09_PH_15", "ФОТО #15 (2023 • Блетчлі-Парк)", "Глобальний саміт з безпеки ШІ у Блетчлі-Парку (листопад 2023)", "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:UK_Government_hosts_AI_Summit_at_Bletchley_Park_(53302263013).jpg", "ep09_img_arch_15_bletchley_park_ai_safety_summit_2023.jpg", "Саміт, де Бенжіо було призначено головою першого Міжнародного наукового звіту безпеки ШІ."),
    ("EP09_PH_16", "ФОТО #16 (Зала РБ ООН)", "Зала Ради Безпеки ООН — міжнародна дипломатія захисту людства від ризиків ШІ", "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:United_Nations_Headquarters_-_Security_Council_chamber,_angled_view_(cropped).jpg", "ep09_img_arch_16_un_security_council_global_governance.jpg", "Майданчик глобальних переговорів ООН щодо демократичного контролю над потужними моделями."),
    ("EP09_PH_17", "ФОТО #17 (Велосипед у снігу)", "Старий комутерський велосипед на зимовому снігу Квебеку", "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Commuting_Icebike.jpg", "ep09_img_arch_17_quebec_winter_bicycle_conscience.jpg", "Він досі їздить на роботу крізь сніг на велосипеді, залишаючись вільним від корпоративних кайданів."),
    ("EP09_PH_18", "ФОТО #18 (Сяйво над Канадою)", "Північне сяйво над засніженою Канадою з орбіти — фінальний етичний щит", "Wikimedia Commons (NASA Public Domain)", "https://commons.wikimedia.org/wiki/File:NASA_astronaut_Scott_Kelly_took_this_aurora_image_over_Canada_on_Jan._21,_2016_01.jpg", "ep09_img_arch_18_canada_aurora_borealis_moral_shield.jpg", "Завершальний образ епізоду: зелене сяйво розуму й совісті над сплячою Землею."),
]

EP09_QUOTES_CARDS = [
    ("UA #01 (4K • 10с)", "00:00–00:25", "ep09_ua_clip_card_01_bicycle_moral_bastion_10s", "Старий велосипед у снігу Квебеку як бастіон вільної науки"),
    ("UA #02 (4K • 10с)", "00:25–01:45", "ep09_ua_clip_card_02_paris_theatre_asimov_10s", "Богемна квартира у Парижі 1964 й книжки Азімова в Монреалі"),
    ("UA #03 (4K • 10с)", "03:30–05:15", "ep09_ua_clip_card_03_ai_winter_family_lab_10s", "20 років зими ШІ: жодної конкуренції — лабораторія-родина"),
    ("UA #04 (4K • 10с)", "05:15–07:15", "ep09_ua_clip_card_04_word_embeddings_cosmos_10s", "Word Embeddings (2000): слово стало координатою чистого смислу"),
    ("UA #05 (4K • 10с)", "07:15–09:30", "ep09_ua_clip_card_05_attention_2014_goodfellow_10s", "2014: промінь Уваги (Attention) Богданова–Чо–Бенжіо та GAN Гудфеллоу"),
    ("UA #06 (4K • 10с)", "09:30–11:15", "ep09_ua_clip_card_06_not_for_sale_mila_10s", "«Я не продаюся!» — відмова від чеків і заснування інституту Mila"),
    ("UA #07 (4K • 12с)", "11:15–16:45", "ep09_ua_clip_card_07_grandson_scientist_ai_12s", "ШІ-Вчений (Система 2 і GFlowNets) зупиняється перед 1% ризику"),
    ("UA #08 (4K • 12с)", "16:45–21:00", "ep09_ua_clip_card_08_conscience_compass_finale_12s", "Монреальська декларація й Кодекс Вартового під північним сяйвом"),
]

EP09_FLOW_KEYFRAMES = [
    ("ATTENTION #01", "⚡ Механізм Уваги 2014 • Bahdanau & Bengio", "chip-purple", "06:30–08:00",
     "Золоті нитки уваги, що з'єднують вектори слів (Additive Attention Vector Core)",
     "assets/flow_keyframes/ep01_flow_kf_08_golden_signatures.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_08_Golden_Signatures_Light_Threads_2K.jpg",
     "Акт 2: Стаття 2014 року про Attention, яка лягла в основу архітектури Transformer."),
    ("MILA #02", "🧠 Глибокі рекурентні мережі • MILA", "chip-cyan", "04:00–05:30",
     "Світіння синапсів глибокої мережі (Нейроінститут Монреаля)",
     "assets/flow_keyframes/ep01_flow_kf_05_neural_lattice.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_05_Neural_Lattice_Glowing_Nodes_2K.jpg",
     "Акт 1: Науковий оазис у Монреалі, що зберіг фундаментальні дослідження ШІ."),
    ("SAFETY TREATY #03", "🛡️ Міжнародний договір • Блетчлі", "chip-emerald", "11:00–13:00",
     "Земля у планетарній мережі контролю (Global AI Safety Treaty)",
     "assets/flow_keyframes/ep01_flow_kf_10_earth_horizon.jpg",
     "05_RAW_FOOTAGE/flow_images/EP01_Altman/01_primary_keyframes/EP01_FLOW_IMG_10_Earth_Horizon_Neural_Grid_2K.jpg",
     "Акт 3 та 4: Бенжіо на саміті в Блетчлі-Парку попереджає світ про небезпеку втрати контролю над автономним ШІ."),
    ("MATRIX #04", "🌌 Матричний туман • Бенжіо", "chip-cyan", "05:30–07:00",
     "Силует мислителя у цифровому матричному тумані (Йошуа Бенжіо)",
     "assets/flow_keyframes/ep09_flow_img_01_silhouette_matrix.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP09_FLOW_IMG_01_Human_Silhouette_In_Digital_Matrix_2K.jpg",
     "Акт 2: Спокійна впевненість ученого серед шуму венчурного ажіотажу."),
    ("TREATY #02", "📜 Монреальська Декларація • Етичний Компас", "chip-emerald", "14:00–15:30",
     "Золота координатна сітка законів заспокоює бурхливий океан ризику",
     "assets/flow_keyframes/ep09_flow_img_02_golden_grid_ocean.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP09_FLOW_IMG_02_Golden_Grid_Stabilizing_Stormy_Ocean_2K.jpg",
     "Акт 3: Йошуа Бенжіо ініціює Монреальську декларацію 2018 року та звернення до ООН: необхідність глобальних правил безпеки ШІ."),
    ("ATTENTION #03", "⚡ Механізм Уваги (Attention) • 2014", "chip-cyan", "09:00–10:30",
     "Два силуети з'єднують літаючі символи крізь семантичний простір",
     "assets/flow_keyframes/ep09_flow_img_03_two_silhouettes_symbols.jpg",
     "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP09_FLOW_IMG_03_Two_Silhouettes_Connecting_Symbols_2K.jpg",
     "Акт 2: Винахід механізму Attention у лабораторії Mila в Монреалі (Bahdanau, Cho, Bengio 2014) — фундамент майбутніх трансформерів."),
]


def main():
    raw_txt = POOL_JS.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    pool = json.loads(raw_txt[len(prefix):].rstrip(";\n "))
    ep9 = pool["09"]

    ep9["dossiers"] = EP09_DOSSIERS

    archives_list = []
    for code, act, tc, fn, title, src, url, sec, note in EP09_ARCHIVES:
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
    ep9["archives"] = archives_list

    photos_list = []
    for pid, code, title, src, url, fn, desc in EP09_PHOTOS:
        photos_list.append({
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_bengio/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        })
    ep9["archival_photos"] = photos_list

    gallery = []
    for code, badge, chip, tc, title, web_p, raw_p, usage in EP09_FLOW_KEYFRAMES:
        gallery.append({
            "code": code,
            "badge": badge,
            "chip": chip,
            "tc": tc,
            "title": title,
            "web_preview": web_p,
            "raw_path": raw_p,
            "dims": "2752×1536 (2K JPG)",
            "usage": usage,
        })
    for code, tc, slug, desc in EP09_QUOTES_CARDS:
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
    ep9["flow_gallery"] = gallery

    POOL_JS.write_text(prefix + json.dumps(pool, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"[OK] Updated {POOL_JS} EP09: dossiers={len(ep9['dossiers'])}, archives={len(ep9['archives'])}, photos={len(ep9['archival_photos'])}, gallery={len(ep9['flow_gallery'])}")

    catalog_json = {
        "episode": "EP09",
        "hero": "Yoshua Bengio",
        "dossiers_4k": EP09_DOSSIERS,
        "archives_1080p": archives_list,
        "archival_photos": photos_list,
        "flow_gallery": gallery,
    }
    (FOOTAGE_DIR / "EP09_MEDIA_CATALOG.json").write_text(json.dumps(catalog_json, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# EP09 — Йошуа Бенжіо: Повний Каталог Медіа-Асетів",
        "",
        f"- **4K Досьє-плашки (`05_RAW_FOOTAGE/dossiers_press/`):** {len(EP09_DOSSIERS)}",
        f"- **HD Архівні відеокліпи 1080p24 (`05_RAW_FOOTAGE/archives/`):** {len(archives_list)}",
        f"- **Фотоархів Wikimedia Commons (`05_RAW_FOOTAGE/speaker_portraits/young_bengio/`):** {len(photos_list)}",
        f"- **Flow Ключові кадри & 4K UA Цитат-Картки:** {len(gallery)}",
        "",
        "## Архівні відеокліпи (16 HD)",
    ]
    for a in archives_list:
        md_lines.append(f"- `{a['code']}` [{a['tc']}] **{a['file']}** — {a['title']}")
    md_lines.append("\n## Фотоархів Wikimedia Commons (18)")
    for p in photos_list:
        md_lines.append(f"- `{p['code']}` **{p['id']}** — {p['title']} (`{p['raw_file']}`)")
    (FOOTAGE_DIR / "EP09_MEDIA_CATALOG.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")
    print("[OK] Generated EP09_MEDIA_CATALOG.json & EP09_MEDIA_CATALOG.md")

    manifest = {
        "episode_id": "EP09",
        "hero": "Yoshua Bengio",
        "title": "Вартовий Монреаля та архітектура уваги",
        "bpm": 92,
        "status": "MEDIA_AND_RESEARCH_SYNCED",
        "source_count": 21,
        "archival_video_count": len(archives_list),
        "archival_photo_count": len(photos_list),
        "dossier_4k_count": len(EP09_DOSSIERS),
        "ua_quote_card_count": len(EP09_QUOTES_CARDS),
        "verified_milestones": [
            "Born in Paris (1964), Emigrated to Montreal; McGill University PhD (1991)",
            "Postdoctoral Studies at MIT & AT&T Bell Labs with LeCun (1991-1993)",
            "Founding of Mila (Montreal Institute for Learning Algorithms) (1993-Present)",
            "Invention of Word Embeddings for Neural Language Models (2000-2003)",
            "Invention of the Attention Mechanism with Bahdanau and Cho (2014)",
            "ACM A.M. Turing Award with Hinton and LeCun (2018)",
            "Montreal Declaration for a Responsible Development of AI (2018)",
            "Development of Generative Flow Networks (GFlowNets) for Science (2021-2023)",
            "Appointed Chair of the UN International Scientific Report on AI Safety (2023-2025)",
        ],
    }
    (META_DIR / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("[OK] Initialized 08_METADATA/EP09_YOSHUA_BENGIO/manifest.json")


if __name__ == "__main__":
    main()
