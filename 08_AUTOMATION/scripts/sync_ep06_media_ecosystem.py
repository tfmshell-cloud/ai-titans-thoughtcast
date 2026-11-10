#!/usr/bin/env python3
"""
Synchronizes EP06 (Ilya Sutskever) curated global archives across:
  - 07_DASHBOARD/data/media_acquisition_pool.js (dossiers, archives, archival_photos)
  - 05_RAW_FOOTAGE/EP06_MEDIA_CATALOG.json & EP06_MEDIA_CATALOG.md
Verifies every single file path exists on disk before saving.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
MP_PATH = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"

DOSSIERS_EP06 = [
    {
        "id": "EP06_DOC_01",
        "ep": "06",
        "act": "ACT2",
        "timecode": "03:30–05:15",
        "title": "ImageNet Classification with Deep Convolutional Neural Networks (AlexNet)",
        "source_label": "Advances in Neural Information Processing Systems (NIPS 2012) • Krizhevsky, Sutskever & Hinton",
        "highlight": "Using two dual GPU GTX 580s in Geoffrey Hinton's Toronto lab, AlexNet shattered ImageNet error from 26.2% down to 15.3%, detonating the global Deep Learning Big Bang.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_01_ACT2_Sutskever_AlexNet_NIPS_2012.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_01_sutskever_alexnet.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_01.mp4",
    },
    {
        "id": "EP06_DOC_02",
        "ep": "06",
        "act": "ACT1",
        "timecode": "00:25–03:30",
        "title": "Горький (1986) → Єрусалим (1991) → Торонто: стукіт у двері Хінтона №4306",
        "source_label": "Gorky USSR — Open University of Israel (Age 15) — UofT Sandford Fleming Room 4306 (2003)",
        "highlight": "Asked Geoffrey Hinton for papers at age 17 with a 1-week deadline — returned in 48 hours with mathematically optimized, faster-running neural code.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_02_ACT1_Gorky_Jerusalem_Toronto_Room_4306.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_02_gorky_jerusalem_room4306.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_02.mp4",
    },
    {
        "id": "EP06_DOC_03",
        "ep": "06",
        "act": "ACT2",
        "timecode": "04:15–06:45",
        "title": "Sequence to Sequence (Seq2Seq 2014): Стиснення цілого речення у вектор думки",
        "source_label": "arXiv:1409.3215 • Google Brain (Sutskever, Vinyals & Le) • NeurIPS 2024 Test of Time",
        "highlight": "Encoded variable-length sentences into continuous latent vectors across multi-GPU LSTMs before Sutskever left Google stock options to co-found OpenAI in a San Francisco flat.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_03_ACT2_Seq2Seq_Vector_Space_GoogleBrain_2014.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_03_seq2seq_googlebrain_2014.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_03.mp4",
    },
    {
        "id": "EP06_DOC_04",
        "ep": "06",
        "act": "ACT3",
        "timecode": "06:45–11:15",
        "title": "Алхімія стиснення, детектив Агати Крісті та емерджентний стрибок GPT-1 → GPT-4",
        "source_label": "OpenAI Scaling Hypothesis (arXiv:2001.08361) • NVIDIA GTC Fireside • Tel Aviv 2023",
        "highlight": "Demonstrated that predicting the single final word of a 300-page mystery novel forces a massive Transformer to internalize human psychology, causality, and world physics.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_04_ACT3_Compression_Agatha_Christie_Scaling_GPT4.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_04_compression_scaling_gpt.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_04.mp4",
    },
    {
        "id": "EP06_DOC_05",
        "ep": "06",
        "act": "ACT3",
        "timecode": "11:15–15:00",
        "title": "Багаття «Відчуйте AGI!», Superalignment та болісний розкол 17 листопада 2023",
        "source_label": "OpenAI Superalignment (July 2023) — Retreat Bonfire — Nov 17 Board Vote & Nov 20 Post",
        "highlight": "Burned an unaligned-AGI wooden effigy at company retreats and spearheaded Superalignment before the Nov 2023 board rupture taught him pure safety collides with consumer product pressure.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_05_ACT3_AGI_Effigy_Superalignment_Nov2023_Rift.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_05_superalignment_nov2023.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_05.mp4",
    },
    {
        "id": "EP06_DOC_06",
        "ep": "06",
        "act": "ACT4",
        "timecode": "15:00–21:45",
        "title": "Safe Superintelligence Inc. (SSI): $1B → $32B в абсолютній тиші та промова в Торонто (2025)",
        "source_label": "SSI.inc Manifesto (Palo Alto & Tel Aviv, June 2024) • UofT Convocation June 2025 • Dwarkesh 2025",
        "highlight": "Launched a pure-research sanctuary with zero interim apps (“Scale in Peace”), growing to a $32B valuation while pioneering post-pretraining superintelligence research.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP06_DOC_06_ACT4_SSI_Monolith_PaloAlto_TelAviv_2026.png",
        "web_preview": "assets/dossiers_preview/ep06_doc_06_ssi_monolith_2026.jpg",
        "video_preview": "assets/video_previews/dossiers/EP06_DOC_06.mp4",
    },
]

ARCHIVES_EP06 = [
    ("ARCH #01", "Акт 2 (Берклі • Саймонс)", "03:50–04:10", "EP06_VID_ARCH_01_ACT2_24FPS_Sutskever_Simons_Lecture.mp4",
     "Лекція в Інституті Саймонса: математика узагальнення та стиснення в глибоких мережах",
     "Simons Institute UC Berkeley (YouTube AKMuA_TVz3A)", "https://www.youtube.com/watch?v=AKMuA_TVz3A", "00:03:10-00:03:18",
     "Класичний академічний виступ Іллі Суцкевера біля дошки про природу генералізації."),
    ("ARCH #02", "Акт 1 (Convocation Hall 2025)", "01:45–02:15", "EP06_VID_ARCH_02_ACT1_24FPS_Sutskever_UofT_Convocation_Return_2025.mp4",
     "Повернення через 20 років у залу Університету Торонто (вручення почесного докторату)",
     "University of Toronto Official (YouTube zuZ2zaotrJs)", "https://www.youtube.com/watch?v=zuZ2zaotrJs", "00:00:24-00:00:52",
     "Ілля Суцкевер згадує день отримання диплома бакалавра рівно два десятиліття тому в тій самій залі."),
    ("ARCH #03", "Акт 1 (Учень Хінтона • Торонто)", "02:15–03:30", "EP06_VID_ARCH_03_ACT1_24FPS_Sutskever_Studying_With_Hinton_UofT.mp4",
     "Навчання у Джеффрі Хінтона: «Те, що Хінтон був у Торонто — головне везіння мого життя»",
     "University of Toronto Official (YouTube zuZ2zaotrJs)", "https://www.youtube.com/watch?v=zuZ2zaotrJs", "00:01:08-00:01:36",
     "Особисте свідчення Суцкевера про роки аспірантури в лабораторії майбутнього нобелівського лауреата."),
    ("ARCH #04", "Акт 1 (До 2012 • Перед AlexNet)", "03:30–04:15", "EP06_VID_ARCH_04_ACT1_24FPS_Sutskever_Pre_AlexNet_2012_NoPriors.mp4",
     "Епоха до AlexNet 2012: коли в глибокому навчанні «ще нічого не працювало»",
     "No Priors Ep. 39 (YouTube Ft0gTO2K85A)", "https://www.youtube.com/watch?v=Ft0gTO2K85A", "00:00:36-00:01:04",
     "Згадка про перші кроки в Торонто всупереч науковому скепсису галузі."),
    ("ARCH #05", "Акт 1 (2012 • AlexNet & NVIDIA)", "04:15–05:15", "EP06_VID_ARCH_05_ACT1_24FPS_Sutskever_Jensen_Huang_AlexNet_GTC.mp4",
     "Діалог із Дженсеном Хуангом про Big Bang 2012 року — створення AlexNet із Крижевським",
     "NVIDIA GTC Fireside Chat 2023 (YouTube I6qQinoY9WM)", "https://www.youtube.com/watch?v=I6qQinoY9WM", "00:04:55-00:05:25",
     "Двоє архітекторів революції ШІ згадують момент, коли GPU перевернули комп'ютерний зір."),
    ("ARCH #06", "Акт 2 (Seq2Seq • NeurIPS 2024)", "04:30–05:15", "EP06_VID_ARCH_06_ACT2_24FPS_Sutskever_Seq2Seq_Scaling_NeurIPS2024.mp4",
     "Промова NeurIPS 2024 Test of Time: Seq2Seq 2014 і народження гіпотези масштабування",
     "NeurIPS 2024 Lecture (YouTube WQQdd6qGxNs)", "https://www.youtube.com/watch?v=WQQdd6qGxNs", "00:05:36-00:06:06",
     "Десять років по тому Суцкевер пояснює, як паралелізація Seq2Seq відкрила дорогу великим моделям."),
    ("ARCH #07", "Акт 2 (2015 • Старт OpenAI)", "05:15–06:45", "EP06_VID_ARCH_07_ACT2_24FPS_Sutskever_OpenAI_Origins_NoPriors.mp4",
     "Народження OpenAI у 2015 році: відмова від комфорту Google заради місії AGI",
     "No Priors Ep. 39 (YouTube Ft0gTO2K85A)", "https://www.youtube.com/watch?v=Ft0gTO2K85A", "00:06:48-00:07:18",
     "Розповідь головного науковця OpenAI про ранні принципи й мету нової лабораторії."),
    ("ARCH #08", "Акт 2 (Стиснення = Інтелект)", "06:45–07:45", "EP06_VID_ARCH_08_ACT2_24FPS_Sutskever_Compression_Learning_GTC.mp4",
     "Навчання без нагляду через стиснення: фундаментальна теорема Суцкевера",
     "NVIDIA GTC Fireside Chat 2023 (YouTube I6qQinoY9WM)", "https://www.youtube.com/watch?v=I6qQinoY9WM", "00:12:28-00:12:56",
     "Чому стиснення даних природно створює внутрішнє розуміння законів світу."),
    ("ARCH #09", "Акт 3 (Детектив Агати Крісті)", "07:45–08:45", "EP06_VID_ARCH_09_ACT3_24FPS_Sutskever_Detective_Novel_Metaphor_GTC.mp4",
     "Детективний роман на 300 сторінок: чому вгадати ім'я вбивці означає симулювати світ",
     "NVIDIA GTC Fireside Chat 2023 (YouTube I6qQinoY9WM)", "https://www.youtube.com/watch?v=I6qQinoY9WM", "00:28:16-00:28:50",
     "Першоджерельний фрагмент, на якому побудований ключовий драматургічний образ 2-го Акту."),
    ("ARCH #10", "Акт 3 (Тель-Авів • Алхімія ШІ)", "08:45–09:45", "EP06_VID_ARCH_10_ACT3_24FPS_Sutskever_Deep_Learning_Alchemy_TAU2023.mp4",
     "Виступ у Тель-Авіві 2023: «Deep learning is a process of alchemy» (алхімія обчислень)",
     "Tel Aviv University June 2023 (YouTube xjDn-kFfpGU)", "https://www.youtube.com/watch?v=xjDn-kFfpGU", "00:03:24-00:03:54",
     "Ілля Суцкевер називає глибоке навчання сучасною науковою алхімією перетворення сирого кремнію на розум."),
    ("ARCH #11", "Акт 3 (Прогноз наступного токена)", "09:45–10:30", "EP06_VID_ARCH_11_ACT3_24FPS_Sutskever_Next_Token_Dwarkesh2023.mp4",
     "«Я заперечую твердження, ніби прогноз наступного токена не може перевершити людину»",
     "Dwarkesh Patel Interview 2023 (YouTube Yf1o0TQzry8)", "https://www.youtube.com/watch?v=Yf1o0TQzry8", "00:00:24-00:00:54",
     "Пряма теоретична полеміка проти скептиків можливостей авторегресивних мовних моделей."),
    ("ARCH #12", "Акт 3 (Емерджентні здібності GPT)", "10:30–11:15", "EP06_VID_ARCH_12_ACT3_24FPS_Sutskever_GPT_Emergent_Behaviors_NoPriors.mp4",
     "Як при 10x зростанні масштабів у моделях GPT раптом прокидалися нові якісні здібності",
     "No Priors Ep. 39 (YouTube Ft0gTO2K85A)", "https://www.youtube.com/watch?v=Ft0gTO2K85A", "00:13:52-00:14:22",
     "Момент переходу кількості параметрів і даних у несподіване системне мислення."),
    ("ARCH #13", "Акт 3 (Superalignment 2023)", "11:15–13:00", "EP06_VID_ARCH_13_ACT3_24FPS_Sutskever_Superalignment_Safety_NoPriors.mp4",
     "Місія Superalignment: створити математичний захист раніше за виникнення надінтелекту",
     "No Priors Ep. 39 (YouTube Ft0gTO2K85A)", "https://www.youtube.com/watch?v=Ft0gTO2K85A", "00:35:10-00:35:40",
     "Поворот фокуса Суцкевера влітку 2023 року на вирівнювання систем, сильніших за людство."),
    ("ARCH #14", "Акт 4 (Кінець епохи Pre-Training)", "15:00–16:45", "EP06_VID_ARCH_14_ACT4_24FPS_Sutskever_End_Of_Pretraining_NeurIPS2024.mp4",
     "NeurIPS 2024: «Епоха попереднього навчання неминуче закінчиться — викопне паливо даних обмежене»",
     "NeurIPS 2024 Test of Time (YouTube WQQdd6qGxNs)", "https://www.youtube.com/watch?v=WQQdd6qGxNs", "00:08:18-00:08:50",
     "Знакова заява Суцкевера про межу інтернет-корпусів та перехід до нової архітектурної парадигми."),
    ("ARCH #15", "Акт 4 (Dwarkesh 2025 • SSI)", "16:45–18:15", "EP06_VID_ARCH_15_ACT4_24FPS_Sutskever_Age_Of_Research_SSI_Dwarkesh2025.mp4",
     "Safe Superintelligence (SSI): перехід від гонитви масштабів до чистої «Епохи досліджень»",
     "Dwarkesh Patel 2025 (YouTube aR20FWCCjAs)", "https://www.youtube.com/watch?v=aR20FWCCjAs", "00:21:16-00:21:46",
     "Фундаментальне інтерв'ю про філософію роботи SSI в ізоляції від ринкового шуму."),
    ("ARCH #16", "Акт 4 (Фінал • Торонто 2025)", "20:15–21:45", "EP06_VID_ARCH_16_ACT4_24FPS_Sutskever_Brain_Biological_Computer_UofT2025.mp4",
     "Фінал: «Людський мозок — це біологічний комп'ютер... ШІ стане найбільшим викликом людства»",
     "UofT Honorary Degree 2025 (YouTube zuZ2zaotrJs)", "https://www.youtube.com/watch?v=zuZ2zaotrJs", "00:06:14-00:06:44",
     "Урочисте звернення 2025 року до нового покоління вчених у Торонто."),
]

ARCHIVAL_PHOTOS_EP06 = [
    ("EP06_PH_01", "ФОТО #01 (1986 • Горький)", "Зима у Нижньому Новгороді (Горький) — снігові простори перших 5 років життя Суцкевера",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Nizhny_Novgorod._Winter_view_to_Kanavino_bridge.jpg",
     "EP06_IMG_ARCH_01_Gorky_Nizhny_Novgorod_Winter_1986.jpg", "ep06_arch_01_gorky_winter.jpg",
     "Зимовий краєвид Волги та засніженого мосту, що нагадує холодну радянську епоху до еміграції 1991 року."),
    ("EP06_PH_02", "ФОТО #02 (1991–2001 • Єрусалим)", "Старовинні кам'яні мури Єрусалима у вечірньому золотому світлі",
     "Wikimedia Commons (CC BY 2.5)", "https://commons.wikimedia.org/wiki/File:PikiWiki_Israel_35499_Old_City_Walls_Jerusalem.jpg",
     "EP06_IMG_ARCH_02_Jerusalem_Golden_Limestone_Walls.jpg", "ep06_arch_02_jerusalem_walls.jpg",
     "Місто, де підліток Ілля у 15 років вступив до Відкритого університету Ізраїлю й загартував концентрацію."),
    ("EP06_PH_03", "ФОТО #03 (Панорама Єрусалима)", "Панорама біблійних пагорбів і золотого вапняку Єрусалима",
     "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:Jerusalem_Dome_of_the_rock_BW_14.JPG",
     "EP06_IMG_ARCH_03_Jerusalem_Old_City_Panorama.jpg", "ep06_arch_03_jerusalem_panorama.jpg",
     "Візуальний ключ 1-го Акту: «Зовнішній світ мінливий, єдиний фундамент усередині власного розуму»."),
    ("EP06_PH_04", "ФОТО #04 (2002 • Торонто)", "University College, Університет Торонто — коледж Іллі Суцкевера",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:University_College,_University_of_Toronto.jpg",
     "EP06_IMG_ARCH_04_University_College_Toronto.jpg", "ep06_arch_04_uoft_college.jpg",
     "Коледж 1859 року, куди Суцкевер вступив 16-річним юнаком одразу після переїзду родини до Канади."),
    ("EP06_PH_05", "ФОТО #05 (2003 • Кабінет №4306)", "Корпус Sandford Fleming (фото 2001 року) — будівля факультету CS та кабінету Хінтона №4306",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Sanford_Fleming_Building,_UofT_(2001)_(50945698932).jpg",
     "EP06_IMG_ARCH_05_UofT_Sandford_Fleming_2001_Room_4306.jpg", "ep06_arch_05_sandford_fleming.jpg",
     "Історичний знімок епохи, коли 17-річний Суцкевер постукав у двері професора Джеффрі Хінтона."),
    ("EP06_PH_06", "ФОТО #06 (2012 • Кристал GTX 580)", "Макрознімок кремнієвого кристала NVIDIA Fermi GF110 (GeForce GTX 580) — рушій AlexNet",
     "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:NVIDIA@40nm@Fermi@GF110@GeForce_GTX_580@UA10B338_1041A1_N2Y540.000_GF110-375-A1_DSC06447_(28114556341).jpg",
     "EP06_IMG_ARCH_06_NVIDIA_GTX580_GF110_AlexNet_Die.jpg", "ep06_arch_06_gtx580_die.jpg",
     "Автентичний кристал 40 нм відеокарти, на парі яких Суцкевер і Крижевський навчили нейромережу AlexNet."),
    ("EP06_PH_07", "ФОТО #07 (2012 • Схема AlexNet)", "Архітектурна блок-схема двопотокової згорткової мережі AlexNet",
     "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:AlexNet_architecture.png",
     "EP06_IMG_ARCH_07_AlexNet_CNN_Architecture_2012.jpg", "ep06_arch_07_alexnet_diagram.jpg",
     "Наочна візуалізація поділу мережі на два паралельні GPU-шляхи для перемоги на ImageNet 2012."),
    ("EP06_PH_08", "ФОТО #08 (2012 • Стенфорд)", "Головний кампус Стенфордського університету — постдокторантура в лабораторії Ендрю Ина",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Stanford_University_from_Hoover_Tower_May_2011_001.jpg",
     "EP06_IMG_ARCH_08_Stanford_University_Quad_2012.jpg", "ep06_arch_08_stanford_quad.jpg",
     "Каліфорнійський науковий центр, куди Суцкевер прибув у 2012 році перед злетом DNNresearch."),
    ("EP06_PH_09", "ФОТО #09 (2013–2015 • Google)", "Googleplex у Маунтін-В'ю — місце створення Sequence-to-Sequence (Seq2Seq)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Outside_Googleplex_in_Mountain_View,_California.jpg",
     "EP06_IMG_ARCH_09_Googleplex_Google_Brain_2014.jpg", "ep06_arch_09_googleplex.jpg",
     "Корпоративна фортеця Google Brain, від мільйонних опціонів якої Суцкевер відмовився заради OpenAI."),
    ("EP06_PH_10", "ФОТО #10 (2014 • Google Brain)", "Молодий Ілля Суцкевер на панелі Nervana & Google Brain (2014)",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Democratizing_Deep_Learning_with_Nervana_and_Google_Brain_(15105407149).jpg",
     "EP06_IMG_ARCH_10_Ilya_Sutskever_Google_Brain_Stage_2014.jpg", "ep06_arch_10_google_brain_2014.jpg",
     "Документальний кадр із титром «Ilya Sutskever — Research Scientist, Google Brain» у рік публікації Seq2Seq."),
    ("EP06_PH_11", "ФОТО #11 (2014 • Стенфорд)", "Сольний портрет молодого Іллі Суцкевера на конференції 2014 року",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Democratizing_Deep_Learning_with_Nervana_and_Google_Brain_(15105407149)_(cropped).jpg",
     "EP06_IMG_ARCH_11_Ilya_Sutskever_Stanford_Solo_2014.jpg", "ep06_arch_11_stanford_solo_2014.jpg",
     "Зосереджений дослідник у простій футболці — образ 28-річного вченого на порозі заснування OpenAI."),
    ("EP06_PH_12", "ФОТО #12 (2015–2023 • OpenAI)", "Pioneer Building у районі Mission (Сан-Франциско) — перша штаб-квартира OpenAI",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Pioneer_Building,_San_Francisco_(2019)_-1.jpg",
     "EP06_IMG_ARCH_12_OpenAI_Pioneer_Building_SF.jpg", "ep06_arch_12_openai_pioneer.jpg",
     "Скромна цегляно-скляна будівля, у якій народилися GPT-1, GPT-2, GPT-3, GPT-4 та ChatGPT."),
    ("EP06_PH_13", "ФОТО #13 (Кластер масштабу)", "Стійка високопродуктивного суперкомп'ютерного кластера (NERSC) — фізична база Scaling Laws",
     "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Rear_of_rack_at_NERSC_data_center_-_closeup.jpg",
     "EP06_IMG_ARCH_13_Supercomputer_Cluster_Scaling_Laws.jpg", "ep06_arch_13_datacenter_servers.jpg",
     "Оптичні магістралі й вузли прискорювачів, де кількість обчислень трансформується в емерджентний інтелект."),
    ("EP06_PH_14", "ФОТО #14 (Ретрит OpenAI)", "Нічне багаття в темряві — символ ритуального спалення неконтрольованої статуї AGI",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Closeup_of_raging_flames_in_a_large_bonfire._-_Flickr_-_shixart1985.jpg",
     "EP06_IMG_ARCH_14_AGI_Effigy_Retreat_Bonfire_2023.jpg", "ep06_arch_14_agi_bonfire_night.jpg",
     "Емоційний символ третього акту про екзистенційну тривогу на ретритах OpenAI («Feel the AGI!»)."),
    ("EP06_PH_15", "ФОТО #15 (2023 • Тель-Авів)", "Ілля Суцкевер та Сем Альтман на сцені Тель-Авівського університету (червень 2023)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Ilya_Sutskever_and_Sam_Altman_in_TAU.jpg",
     "EP06_IMG_ARCH_15_Sutskever_Altman_Tel_Aviv_2023.jpg", "ep06_arch_15_tau_2023.jpg",
     "Останнє спільне світове турне двох співзасновників OpenAI за 5 місяців до листопадової кризи."),
    ("EP06_PH_16", "ФОТО #16 (2024 • Тель-Авів SSI)", "Кампус Тель-Авівського університету — один із двох наукових полюсів Safe Superintelligence",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Tel_Aviv_University_1.jpg",
     "EP06_IMG_ARCH_16_Tel_Aviv_University_SSI_Hub.jpg", "ep06_arch_16_tel_aviv_campus.jpg",
     "Повернення науковця до Ізраїлю при заснуванні дослідницької лабораторії SSI між Пало-Альто й Тель-Авівом."),
    ("EP06_PH_17", "ФОТО #17 (2025 • Торонто)", "Convocation Hall Університету Торонто — місце вручення почесного докторату 6 червня 2025",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:CN_Tower_and_Convocation_Hall_of_the_University_of_Toronto_(March_2019).jpg",
     "EP06_IMG_ARCH_17_Toronto_Convocation_Hall_2025.jpg", "ep06_arch_17_convocation_hall.jpg",
     "Кругла зала, де через 20 років після бакалаврату Суцкевер попередив світ про виклик надінтелекту."),
    ("EP06_PH_18", "ФОТО #18 (2024–2026 • SSI)", "Мінімалістичний моноліт логотипу Safe Superintelligence Inc. (SSI)",
     "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:Safe_Superintelligence_Inc._logo.jpg",
     "EP06_IMG_ARCH_18_Safe_Superintelligence_SSI_Monolith.jpg", "ep06_arch_18_ssi_logo_2024.jpg",
     "Офіційна емблема компанії без комерційних релізів, побудованої виключно навколо однієї мети — безпечного AGI."),
]


def verify_paths():
    missing = []
    for d in DOSSIERS_EP06:
        if not (ROOT / d["raw_4k_png"]).exists():
            missing.append(d["raw_4k_png"])
        for k in ("web_preview", "video_preview"):
            if not (ROOT / "07_DASHBOARD" / d[k]).exists():
                missing.append("07_DASHBOARD/" + d[k])
    for row in ARCHIVES_EP06:
        mp4_file = row[3]
        if not (ROOT / "05_RAW_FOOTAGE" / "archives" / mp4_file).exists():
            missing.append("05_RAW_FOOTAGE/archives/" + mp4_file)
        if not (ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "archives" / mp4_file).exists():
            missing.append("07_DASHBOARD/assets/video_previews/archives/" + mp4_file)
    for row in ARCHIVAL_PHOTOS_EP06:
        raw_fn, web_fn = row[5], row[6]
        if not (ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_sutskever" / raw_fn).exists():
            missing.append("young_sutskever/" + raw_fn)
        if not (ROOT / "07_DASHBOARD" / "assets" / "archival_photos" / web_fn).exists():
            missing.append("archival_photos/" + web_fn)
    if missing:
        raise RuntimeError("Missing verified files:\n  " + "\n  ".join(missing))


def main():
    verify_paths()
    raw = MP_PATH.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    mp = json.loads(raw[len(prefix):].rstrip(";\n "))

    ep06 = mp["06"]
    ep06["dossiers"] = DOSSIERS_EP06
    ep06["archives"] = [
        {
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
        }
        for (code, act, tc, fn, title, src, url, sec, note) in ARCHIVES_EP06
    ]
    ep06["archival_photos"] = [
        {
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_sutskever/{raw_fn}",
            "web_preview": f"assets/archival_photos/{web_fn}",
            "desc": desc,
        }
        for (pid, code, title, src, url, raw_fn, web_fn, desc) in ARCHIVAL_PHOTOS_EP06
    ]

    existing_fg = [g for g in ep06.get("flow_gallery", []) if not str(g.get("code", "")).startswith("UA CARD")]
    for idx_c, card_p in enumerate(sorted((ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP06_UA_CARD_*.png")), 1):
        prev_rel = f"assets/cards_preview/{card_p.stem.lower()}.jpg"
        if (ROOT / "07_DASHBOARD" / prev_rel).exists():
            existing_fg.append({
                "code": f"UA CARD #{idx_c:02d}",
                "badge": "🇺🇦 4K Цитат-Картка",
                "tc": f"Акт {(idx_c - 1) // 2 + 1}",
                "title": card_p.stem.replace("EP06_UA_CARD_", "Картка ").replace("_", " "),
                "dims": "3840×2160 4K",
                "chip": "chip-emerald",
                "web_preview": prev_rel,
                "raw_path": f"05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/{card_p.name}",
            })
    ep06["flow_gallery"] = existing_fg

    MP_PATH.write_text(prefix + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

    ua_cards = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP06_*.png"))
    still_clips = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k").glob("EP06_*.mp4"))
    cat_json = {
        "episode": "EP06 — Ilya Sutskever",
        "updated_at": "2026-11-10",
        "summary": {
            "archival_broll_mp4": len(ARCHIVES_EP06),
            "archival_photos": len(ARCHIVAL_PHOTOS_EP06),
            "uhd_4k_dossiers": len(DOSSIERS_EP06),
            "ukrainian_4k_quote_cards": len(ua_cards),
            "ken_burns_and_card_4k_mp4": len(still_clips),
        },
        "dossiers": DOSSIERS_EP06,
        "archives": ep06["archives"],
        "archival_photos": ep06["archival_photos"],
        "ukrainian_4k_quote_cards": ua_cards,
        "rendered_cinematic_stills_4k": still_clips,
    }
    (ROOT / "05_RAW_FOOTAGE" / "EP06_MEDIA_CATALOG.json").write_text(json.dumps(cat_json, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP06 (Ілля Суцкевер)",
        "",
        f"- **📼 Реальні архівні відеокліпи B-Roll (`05_RAW_FOOTAGE/archives/`):** {len(ARCHIVES_EP06)}",
        f"- **📸 Історичні фото та наукові артефакти (`05_RAW_FOOTAGE/speaker_portraits/young_sutskever/`):** {len(ARCHIVAL_PHOTOS_EP06)}",
        f"- **🗂️ 4K Документальні досьє-пластини (`05_RAW_FOOTAGE/dossiers_press/`):** {len(DOSSIERS_EP06)}",
        f"- **🇺🇦 4K Українські цитат-картки (`ukrainian_quote_cards/`):** {len(ua_cards)}",
        f"- **🎞️ Ken Burns 4K відеокліпи зі стілів і карток (`rendered_cinematic_stills_4k/`):** {len(still_clips)}",
        "",
        "## 📼 Архівні відеокліпи (`EP06_VID_ARCH_01..16`)",
        "",
        "| Код | Таймкод EP06 | Файл | Джерело |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for a in ep06["archives"]:
        md.append(f"| **{a['code']}** | `{a['timecode']}` | `{a['mp4_file']}` | {a['source']} |")
    md += ["", "## 📸 Хронологічні архівні фото (`EP06_IMG_ARCH_*`)", "", "| Код | Файл | Ліцензія / Джерело |", "| :--- | :--- | :--- |"]
    for p in ep06["archival_photos"]:
        md.append(f"| **{p['code']}** | `{p['raw_file'].split('/')[-1]}` | [{p['source']}]({p['url']}) |")
    (ROOT / "05_RAW_FOOTAGE" / "EP06_MEDIA_CATALOG.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"[✓] EP06 synced: {len(DOSSIERS_EP06)} dossiers, {len(ARCHIVES_EP06)} archival videos, {len(ARCHIVAL_PHOTOS_EP06)} archival photos, {len(ua_cards)} UA cards, {len(still_clips)} 4K motion clips!")


if __name__ == "__main__":
    main()
