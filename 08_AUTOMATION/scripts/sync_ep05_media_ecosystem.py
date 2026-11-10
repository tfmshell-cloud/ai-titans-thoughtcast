#!/usr/bin/env python3
"""
Synchronizes EP05 (Yann LeCun) curated global archives across:
  - 07_DASHBOARD/data/media_acquisition_pool.js (dossiers, archives, archival_photos)
  - 05_RAW_FOOTAGE/EP05_MEDIA_CATALOG.json & EP05_MEDIA_CATALOG.md
Verifies every single file path exists on disk before saving.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
MP_PATH = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"

DOSSIERS_EP05 = [
    {
        "id": "EP05_DOC_01",
        "ep": "05",
        "act": "ACT2",
        "timecode": "06:00–07:15",
        "title": "Gradient-Based Learning Applied to Document Recognition (LeNet-5)",
        "source_label": "Proceedings of the IEEE, Nov 1998 • LeCun, Bottou, Bengio & Haffner (Bell Labs)",
        "highlight": "Deployed by NCR across U.S. banks by the late 1990s, LeNet-5 autonomously read handwritten amounts on over 10% to 20% of all checks processed in the United States.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_01_ACT2_LeCun_LeNet5_IEEE_1998.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_01_lecun_lenet5.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_01.mp4",
    },
    {
        "id": "EP05_DOC_02",
        "ep": "05",
        "act": "ACT1",
        "timecode": "00:25–03:35",
        "title": "Паризька майстерня, ESIEE (1983) та дебати Піаже проти Хомського",
        "source_label": "Soisy-sous-Montmorency (1960) — ESIEE Paris (1983) — Royaumont Piaget/Chomsky",
        "highlight": "Born to an aerospace engineer in 1960; etched double-sided circuit boards at ESIEE and sided with Jean Piaget's constructivism against hard-coded symbolic grammar.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_02_ACT1_Paris_Electronics_ESIEE_Piaget_1974.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_02_paris_esiee_piaget_1974.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_02.mp4",
    },
    {
        "id": "EP05_DOC_03",
        "ep": "05",
        "act": "ACT2",
        "timecode": "03:35–07:25",
        "title": "PhD у Сорбонні (1987) та Bell Labs Холмдел (1988): Спростування Мінського й кора кота",
        "source_label": "UPMC Paris (1987) -> U of T Postdoc Hinton -> AT&T Bell Labs Holmdel NJ (1988–1989)",
        "highlight": "Re-derived Minsky & Papert's 1969 Perceptron limits in a Paris cellar, proposed early backprop, and translated Hubel & Wiesel's visual cortex into LeNet-1.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_03_ACT2_Sorbonne_Backprop_Minsky_1987.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_03_sorbonne_minsky_1987.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_03.mp4",
    },
    {
        "id": "EP05_DOC_04",
        "ep": "05",
        "act": "ACT2",
        "timecode": "07:25–10:15",
        "title": "20% банківських чеків США, винахід DjVu (1996) і 15 років вигнання в епоху SVM",
        "source_label": "NCR ATMs (10–20% US Checks) • DjVu (Internet Archive) • NYU Courant Silver Prof (2003)",
        "highlight": "Even while LeNet read up to 20% of US checks and DjVu compressed digital libraries, NeurIPS/CVPR sidelined neural nets for 15 years during the SVM kernel craze.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_04_ACT2_AT_T_Checks_DjVu_SVM_Wilderness.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_04_checks_djvu_svm_1998.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_04.mp4",
    },
    {
        "id": "EP05_DOC_05",
        "ep": "05",
        "act": "ACT3",
        "timecode": "10:45–15:10",
        "title": "Пакт Meta FAIR (2013), PyTorch і LLaMA: Захист відкритого ШІ як верстат Гутенберга",
        "source_label": "Meta FAIR Founding Covenant (Dec 9, 2013) • PyTorch • ICLR OpenReview • LLaMA Open Weights",
        "highlight": "Insisted on unrestricted open publication to launch FAIR, co-founded ICLR OpenReview, stewarded PyTorch, and equated open-weight LLaMA to Gutenberg's press.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_05_ACT3_Meta_FAIR_PyTorch_LLaMA_Gutenberg.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_05_fair_pytorch_llama.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_05.mp4",
    },
    {
        "id": "EP05_DOC_06",
        "ep": "05",
        "act": "ACT4",
        "timecode": "15:10–21:00",
        "title": "Премія Тюрінга (2018), світові моделі JEPA та старт AMI Labs у Парижі ($1.03B, 2026)",
        "source_label": "ACM Turing Award (2018) • ETH Zurich JEPA • Advanced Machine Intelligence (AMI Labs $1.03B)",
        "highlight": "Showed 16,000 hours of infant vision beats text tokens, proposed Joint Embedding Predictive Architecture (JEPA), and launched AMI Labs ($1.03B Seed, March 2026).",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP05_DOC_06_ACT4_Turing_2018_JEPA_World_Models_AMI_2026.png",
        "web_preview": "assets/dossiers_preview/ep05_doc_06_jepa_ami_labs_2026.jpg",
        "video_preview": "assets/video_previews/dossiers/EP05_DOC_06.mp4",
    },
]

ARCHIVES_EP05 = [
    ("ARCH #01", "Акт 2 (Bell Labs 1989)", "06:15–06:23", "EP05_VID_ARCH_01_ACT2_24FPS_LeCun_BellLabs_1989_Digits.mp4",
     "Bell Labs (1989): Ян Лекун та перша згорткова мережа LeNet-1 на ПК 486 + DSP32C",
     "Yann LeCun Official Archive (YouTube FwFduRA_L6Q)", "https://www.youtube.com/watch?v=FwFduRA_L6Q", "00:00:12-00:00:20",
     "Історичний запис розпізнавання рукописних цифр у реальному часі в Холмделі, Нью-Джерсі."),
    ("ARCH #02", "Акт 1 (Париж • Філософія)", "01:15–03:35", "EP05_VID_ARCH_02_ACT1_24FPS_LeCun_Chomsky_Piaget_Debate_ETH.mp4",
     "Вплив Жана Піаже: чому інтелект народжується з фізичної взаємодії, а не правил Хомського",
     "ETH Zurich World Models Lecture (YouTube 72Xj8k5WQX4)", "https://www.youtube.com/watch?v=72Xj8k5WQX4", "00:02:55-00:03:20",
     "Ян Лекун пояснює, як дебати Піаже й Хомського наприкінці 1970-х сформували його конструктивістський підхід."),
    ("ARCH #03", "Акт 1 (Ніч із Мінським)", "04:05–05:15", "EP05_VID_ARCH_03_ACT1_24FPS_Hinton_LeCun_Minsky_Perceptrons_Turing.mp4",
     "Персептрони Розенблатта і роковий міф книги Мінського та Пейперта (1969)",
     "ACM A.M. Turing Award 2018 Lecture (YouTube VsnQf7exv5I)", "https://www.youtube.com/watch?v=VsnQf7exv5I", "00:14:38-00:15:02",
     "Академічна хроніка про те, як висновок Мінського про 1 шар зупинив фінансування нейромереж на два десятиліття."),
    ("ARCH #04", "Акт 2 (1989 Відновлене HD)", "05:35–06:15", "EP05_VID_ARCH_04_ACT2_24FPS_LeCun_1989_ConvNet_Restored.mp4",
     "Відновлена HD-хроніка демо LeNet-1 (1989): неперервна сегментація рукописних чисел",
     "Yann LeCun Official Restored Archive (YouTube H0oEr40YhrQ)", "https://www.youtube.com/watch?v=H0oEr40YhrQ", "00:00:25-00:00:58",
     "Відновлена версія культового ролика AT&T Bell Labs із робочим розпізнаванням цифр у русі."),
    ("ARCH #05", "Акт 2 (Холмдел • Архів)", "06:15–06:50", "EP05_VID_ARCH_05_ACT2_24FPS_LeCun_Young_Bell_Labs_Holmdel_Photo.mp4",
     "Молодий Ян Лекун у Bell Labs (1989): архівне фото зі старим телефоном лабораторії у Холмделі",
     "ACM Turing Award Lecture (YouTube VsnQf7exv5I)", "https://www.youtube.com/watch?v=VsnQf7exv5I", "00:46:26-00:46:48",
     "Рідкісний кадр із виступу на Премії Тюрінга: Лекун показує себе 29-річним за робочим столом Bell Labs."),
    ("ARCH #06", "Акт 2 (Зорова кора кота)", "06:50–07:25", "EP05_VID_ARCH_06_ACT2_24FPS_LeCun_Hubel_Wiesel_Visual_Cortex.mp4",
     "Нейробіологія Хьюбела та Візеля (1960-ті): як прості й складні клітини кори кота стали CNN",
     "ACM Turing Award Lecture (YouTube VsnQf7exv5I)", "https://www.youtube.com/watch?v=VsnQf7exv5I", "00:44:32-00:45:00",
     "Пряме пояснення першовідкривача, як нейрофізіологія зорової кори дала принцип поділу ваг згортки."),
    ("ARCH #07", "Акт 2 (20% чеків США)", "07:25–08:45", "EP05_VID_ARCH_07_ACT2_24FPS_LeCun_20_Percent_US_Checks_Turing.mp4",
     "Тріумф без хайпу: побудована в Bell Labs система читала 10–20% усіх банківських чеків у США",
     "ACM Turing Award Lecture (YouTube VsnQf7exv5I)", "https://www.youtube.com/watch?v=VsnQf7exv5I", "00:43:28-00:43:54",
     "Власне свідчення Лекуна на Премії Тюрінга про національний масштаб розпізнавання чеків."),
    ("ARCH #08", "Акт 2 (Зима ШІ & SVM)", "08:45–10:15", "EP05_VID_ARCH_08_ACT2_24FPS_LeCun_Neural_Net_Winter_SVM_Sequel.mp4",
     "«Темні віки» нейромереж (1995–2008): 15 років наукової пустелі в епоху SVM",
     "Turing Award Sequel Lecture (YouTube psl1wY2V-L0)", "https://www.youtube.com/watch?v=psl1wY2V-L0", "00:04:16-00:04:44",
     "Чому конференції масово відхиляли статті про нейромережі навіть після комерційного успіху LeNet."),
    ("ARCH #09", "Акт 2 (DSP32C продакшн)", "09:30–10:15", "EP05_VID_ARCH_09_ACT2_24FPS_LeCun_Bell_Labs_DSP_Compiler_Lex36.mp4",
     "Власний компілятор для сигнальних процесорів DSP і бойовий код розпізнавання у Bell Labs",
     "Lex Fridman Podcast #36 (YouTube SGSOCuByo24)", "https://www.youtube.com/watch?v=SGSOCuByo24", "00:28:10-00:28:36",
     "Інженерні деталі впровадження LeNet на залізі AT&T 1990-х років."),
    ("ARCH #10", "Акт 3 (Meta FAIR & PyTorch)", "10:45–12:15", "EP05_VID_ARCH_10_ACT3_24FPS_LeCun_FAIR_PyTorch_Open_Source_Lex258.mp4",
     "Народження Meta FAIR (2013) та відкриті наукові інструменти на кшталт PyTorch",
     "Lex Fridman Podcast #258 (YouTube SGzMElJ11Cc)", "https://www.youtube.com/watch?v=SGzMElJ11Cc", "01:51:10-01:51:38",
     "Про принцип відкритої науки в FAIR, який перетворив PyTorch на стандарт світових досліджень ШІ."),
    ("ARCH #11", "Акт 3 (Верстат Гутенберга)", "12:15–13:15", "EP05_VID_ARCH_11_ACT3_24FPS_LeCun_Gutenberg_Printing_Press_Lex258.mp4",
     "Друкарський верстат Гутенберга проти цензури знань — захист відкритого ШІ (LLaMA)",
     "Lex Fridman Podcast #258 (YouTube SGzMElJ11Cc)", "https://www.youtube.com/watch?v=SGzMElJ11Cc", "02:02:48-02:03:14",
     "Філософський маніфест Лекуна про те, чому штучний інтелект не можна замикати в пропрієтарних вежах."),
    ("ARCH #12", "Акт 3 (Домашній кіт vs LLM)", "13:30–15:10", "EP05_VID_ARCH_12_ACT3_24FPS_LeCun_House_Cat_Common_Sense_Lex258.mp4",
     "Чому ваш домашній кіт має більше здорового глузду й фізичної інтуїції, ніж будь-яка LLM",
     "Lex Fridman Podcast #258 (YouTube SGzMElJ11Cc)", "https://www.youtube.com/watch?v=SGzMElJ11Cc", "00:21:30-00:21:58",
     "Культова теза Яна Лекуна про неможливість побудувати фізичний розум виключно з тексту."),
    ("ARCH #13", "Акт 3 (Глухий кут токенів)", "15:10–16:15", "EP05_VID_ARCH_13_ACT3_24FPS_LeCun_No_AGI_By_Scaling_LLMs.mp4",
     "«Ми не досягнемо людського інтелекту простим масштабуванням LLM» — пряма полеміка",
     "Big Technology Interview (YouTube 4__gg83s_Do)", "https://www.youtube.com/watch?v=4__gg83s_Do", "00:00:00-00:00:26",
     "Прямий ультиматум авторегресивній парадигмі: тексту недостатньо для планування в реальному світі."),
    ("ARCH #14", "Акт 4 (Архітектура JEPA)", "16:15–17:45", "EP05_VID_ARCH_14_ACT4_24FPS_LeCun_JEPA_Architecture_ETH_Zurich.mp4",
     "Як працює JEPA (Joint Embedding Predictive Architecture): прогноз у просторі сенсів, а не пікселів",
     "ETH Zurich World Models Lecture (YouTube 72Xj8k5WQX4)", "https://www.youtube.com/watch?v=72Xj8k5WQX4", "00:25:14-00:25:48",
     "Детальне пояснення головної альтернативи генеративним трансформерам у лекції ETH Zurich."),
    ("ARCH #15", "Акт 4 (16 000 годин зору)", "17:45–19:15", "EP05_VID_ARCH_15_ACT4_24FPS_LeCun_Baby_3D_Intuitive_Physics_ETH.mp4",
     "Як немовля осягає тривимірну фізику світу за перші місяці зорового спостереження",
     "ETH Zurich World Models Lecture (YouTube 72Xj8k5WQX4)", "https://www.youtube.com/watch?v=72Xj8k5WQX4", "00:06:24-00:06:52",
     "Наукове порівняння пропускної здатності людського ока проти текстового тренування ШІ."),
    ("ARCH #16", "Акт 4 (Давос 2026 • AMI Labs)", "19:15–21:00", "EP05_VID_ARCH_16_ACT4_24FPS_LeCun_Davos_2026_Embodied_AI.mp4",
     "AI House Davos 2026: Втілений фізичний ШІ та курс проти течії хайпу (епоха AMI Labs)",
     "AI House Davos 2026 (YouTube pJyoqapCRZE)", "https://www.youtube.com/watch?v=pJyoqapCRZE", "00:04:46-00:05:14",
     "Виступ у Давосі 2026 про перехід до світових моделей та самокерованого фізичного інтелекту."),
]

ARCHIVAL_PHOTOS_EP05 = [
    ("EP05_PH_01", "ФОТО #01 (1977 • Париж)", "Паризькі вулиці кінця 1970-х — середовище юності Яна Лекуна у Франції",
     "Wikimedia Commons (GFDL 1.2)", "https://commons.wikimedia.org/wiki/File:Paris-Opera-1977-7a.jpg",
     "EP05_IMG_ARCH_01_Paris_1977_Opera_Youth_Era.jpg", "ep05_arch_01_paris_1977.jpg",
     "Атмосфера Парижа 1977 року — доба транзисторів, мопедів і студентського пошуку юного інженера."),
    ("EP05_PH_02", "ФОТО #02 (1977 • Осцилограф)", "Аналоговий осцилограф Tektronix 475A — інструмент радіоелектронної майстерні 1970-х",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Tektronix_Oscilloscope_475A.jpg",
     "EP05_IMG_ARCH_02_Tektronix_475A_Oscilloscope_1977.jpg", "ep05_arch_02_tektronix_1977.jpg",
     "Характерний прилад покоління інженерів-конструкторів, із якого починалося розуміння сигналів і заліза."),
    ("EP05_PH_03", "ФОТО #03 (1975–1980 • 6502)", "Топологія кремнієвого кристала 8-бітного мікропроцесора MOS 6502",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:BreakNES_MOS_6502.jpg",
     "EP05_IMG_ARCH_03_MOS_6502_Microprocessor_Die.jpg", "ep05_arch_03_mos_6502_die.jpg",
     "Кристал легендарного процесора епохи перших саморобних комп'ютерів і паяння плат у Парижі."),
    ("EP05_PH_04", "ФОТО #04 (1983 • ESIEE)", "Кампус інженерної школи ESIEE Paris, де Лекун здобув диплом інженера 1983 року",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:ESIEE_Paris_1.jpg",
     "EP05_IMG_ARCH_04_ESIEE_Paris_Engineering_School.jpg", "ep05_arch_04_esiee_paris.jpg",
     "Стіни школи електроніки та інформатики, де Лекун травив плати в кислоті й відкрив для себе персептрони."),
    ("EP05_PH_05", "ФОТО #05 (1987 • Сорбонна)", "Паризька альма-матер Сорбонна / UPMC — захист дисертації зі зворотного поширення (1987)",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Sorbonne_University_%40_Paris_%2823899763722%29.jpg",
     "EP05_IMG_ARCH_05_Sorbonne_Paris_PhD_Campus.jpg", "ep05_arch_05_sorbonne_paris.jpg",
     "Історичний паризький університетський квартал, де молодий аспірант самостійно вивів ранній backprop."),
    ("EP05_PH_06", "ФОТО #06 (Мінський • 1969)", "Марвін Мінський — автор книги «Персептрони», чию теорему Лекун перевірив і подолав",
     "Wikimedia Commons (CC BY 3.0)", "https://commons.wikimedia.org/wiki/File:Marvin_Minsky_at_OLPC.jpg",
     "EP05_IMG_ARCH_06_Marvin_Minsky_Perceptrons_Rival.jpg", "ep05_arch_06_marvin_minsky.jpg",
     "Провідний ідеолог символьного ШІ з MIT, помилкові узагальнення якого гальмували нейромережі на 20 років."),
    ("EP05_PH_07", "ФОТО #07 (1987 • Холмдел)", "Аерофотознімок Bell Labs Holmdel (USGS, 1987) — за рік до приходу Лекуна",
     "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:Bell_Labs_Holmdel,_1987,_USGS_(1VFKQC0020097).tif",
     "EP05_IMG_ARCH_07_Bell_Labs_Holmdel_Aerial_1987.jpg", "ep05_arch_07_bell_labs_1987.jpg",
     "Автентичний супутниково-аерофотознімок кампусу Bell Labs 1987 року, схожий на гігантську схему."),
    ("EP05_PH_08", "ФОТО #08 (1988–1995 • LeNet)", "Дзеркальний корпус Bell Labs Holmdel у Нью-Джерсі — батьківщина згорткових мереж",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Bell_Labs_Holmdel.jpg",
     "EP05_IMG_ARCH_08_Bell_Labs_Holmdel_Mirror_Building.jpg", "ep05_arch_08_bell_labs_holmdel.jpg",
     "Знакова скляна цитадель Ееро Саарінена, де відділ Ларрі Джекела прийняв молодого француза і породив LeNet."),
    ("EP05_PH_09", "ФОТО #09 (2003 • NYU)", "Warren Weaver Hall — Інститут математичних наук Куранта в Нью-Йоркському університеті",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Courant_Institute_of_Mathematical_Sciences_%2848072654781%29.jpg",
     "EP05_IMG_ARCH_09_Courant_Institute_NYU_Weaver_Hall.jpg", "ep05_arch_09_courant_nyu.jpg",
     "Фортеця Яна Лекуна у Нижньому Мангеттені в роки ізоляції, де розвивалися енергетичні моделі ШІ."),
    ("EP05_PH_10", "ФОТО #10 (Лекція CNN)", "Рідкісний кадр: Ян Лекун пояснює слайд NIPS 1989 про згорткові шари та пулінг",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Yann_LeCun_at_the_University_of_Minnesota.jpg",
     "EP05_IMG_ARCH_10_Yann_LeCun_Minnesota_CNN_Lecture.jpg", "ep05_arch_10_lecun_minnesota.jpg",
     "Архівний виступ професора NYU на дошці зі схемою 1989 року — жива історія комп'ютерного зору."),
    ("EP05_PH_11", "ФОТО #11 (2013 • FAIR)", "В'їзд до кампусу 1 Hacker Way (Менло-Парк) — епоха створення Meta FAIR",
     "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Facebook_Headquarters_1_Hacker_Way_Menlo_Park.jpg",
     "EP05_IMG_ARCH_11_Meta_Menlo_Park_HQ_One_Hacker_Way.jpg", "ep05_arch_11_meta_menlo_park.jpg",
     "Штаб-квартира корпорації, з керівництвом якої Лекун підписав пакт про 100% відкриту науку."),
    ("EP05_PH_12", "ФОТО #12 (2017 • Сцена)", "Виступ Яна Лекуна в Парижі (Data Science Summer School, École Polytechnique)",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Yann_LeCun_(41208595340).jpg",
     "EP05_IMG_ARCH_12_Yann_LeCun_Data_Science_Keynote.jpg", "ep05_arch_12_lecun_keynote.jpg",
     "Французько-американський науковець перед молодим поколінням дослідників машинного навчання."),
    ("EP05_PH_13", "ФОТО #13 (2018 • Тюрінг)", "Портрет Яна Лекуна 2018 року — року здобуття Премії Тюрінга",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Yann_LeCun_-_2018_(cropped).jpg",
     "EP05_IMG_ARCH_13_Yann_LeCun_Turing_2018_Portrait.jpg", "ep05_arch_13_turing_2018.jpg",
     "Кадр лауреата «Нобелівської премії комп'ютерних наук» у рік світового визнання глибокого навчання."),
    ("EP05_PH_14", "ФОТО #14 (Гутенберг)", "Історичний друкарський верстат у музеї Гутенберга (Майнц) — метафора відкритого коду",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Gutenberg%27s_vintage_hand_printing_press_in_the_Gutenberg_Museum,_Mainz,_Germany_(48988298351).jpg",
     "EP05_IMG_ARCH_14_Gutenberg_Printing_Press_Mainz.jpg", "ep05_arch_14_gutenberg_press.jpg",
     "Головна історична аналогія Лекуна: як книгодрукування, відкриті моделі на кшталт LLaMA звільняють знання."),
    ("EP05_PH_15", "ФОТО #15 (Фізика кота)", "Хронофотографія стрибка кота («Animal Locomotion») — зразок інтуїтивної фізики світу",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Animal-Locomotion-Photo-Cat-and-dog-jumping-735x1000.jpg",
     "EP05_IMG_ARCH_15_Cat_Physics_Animal_Locomotion.jpg", "ep05_arch_15_cat_locomotion.jpg",
     "Наукова фазова послідовність руху, що ілюструє тезу Лекуна: кіт прогнозує простір без текстових токенів."),
    ("EP05_PH_16", "ФОТО #16 (2025 • Париж)", "Великий план: Ян Лекун на саміті «AI, Science and Society» в École Polytechnique (2025)",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Conf%C3%A9rence_IP_Paris_%22AI,_Science_and_Society%22_%C3%A0_l%27Ecole_polytechnique_(54320377276).jpg",
     "EP05_IMG_ARCH_16_Yann_LeCun_IP_Paris_2025_Portrait.jpg", "ep05_arch_16_ip_paris_2025.jpg",
     "Портрет творця JEPA у розквіті кампанії проти сліпої віри у масштабування мовних моделей."),
    ("EP05_PH_17", "ФОТО #17 (2026 • ЄС)", "Зустріч Яна Лекуна з віцепрезиденткою Єврокомісії Хенною Вірккунен (Брюссель, 2026)",
     "Wikimedia Commons (CC BY 4.0)", "https://commons.wikimedia.org/wiki/File:Meeting_between_Yann_LeCun_%26_Henna_Virkkunen,_Executive_Vice-President_of_the_EC_-_2026.jpg",
     "EP05_IMG_ARCH_17_Yann_LeCun_Brussels_EU_Summit_2026.jpg", "ep05_arch_17_eu_summit_2026.jpg",
     "Європейська дипломатія відкритого ШІ та повернення Лекуна до Парижа з проєктом AMI Labs ($1.03B)."),
    ("EP05_PH_18", "ФОТО #18 (Бейдевінд)", "Вітрильник курсом бейдевінд — рух під гострим кутом проти вітру і хвилі",
     "Wikimedia Commons (CC BY 3.0)", "https://commons.wikimedia.org/wiki/File:Close_Hauled_(138379585).jpeg",
     "EP05_IMG_ARCH_18_Sailing_Close_Hauled_Badewind.jpg", "ep05_arch_18_sailing_badewind.jpg",
     "Фінальна візуальна метафора: йти супроти панівного хайпу до справжніх світових моделей реальності."),
]


def verify_paths():
    missing = []
    for d in DOSSIERS_EP05:
        if not (ROOT / d["raw_4k_png"]).exists():
            missing.append(d["raw_4k_png"])
        for k in ("web_preview", "video_preview"):
            if not (ROOT / "07_DASHBOARD" / d[k]).exists():
                missing.append("07_DASHBOARD/" + d[k])
    for row in ARCHIVES_EP05:
        mp4_file = row[3]
        if not (ROOT / "05_RAW_FOOTAGE" / "archives" / mp4_file).exists():
            missing.append("05_RAW_FOOTAGE/archives/" + mp4_file)
        if not (ROOT / "07_DASHBOARD" / "assets" / "video_previews" / "archives" / mp4_file).exists():
            missing.append("07_DASHBOARD/assets/video_previews/archives/" + mp4_file)
    for row in ARCHIVAL_PHOTOS_EP05:
        raw_fn, web_fn = row[5], row[6]
        if not (ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_lecun" / raw_fn).exists():
            missing.append("young_lecun/" + raw_fn)
        if not (ROOT / "07_DASHBOARD" / "assets" / "archival_photos" / web_fn).exists():
            missing.append("archival_photos/" + web_fn)
    if missing:
        raise RuntimeError("Missing verified files:\n  " + "\n  ".join(missing))


def main():
    verify_paths()
    raw = MP_PATH.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    mp = json.loads(raw[len(prefix):].rstrip(";\n "))

    ep05 = mp["05"]
    ep05["dossiers"] = DOSSIERS_EP05
    ep05["archives"] = [
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
        for (code, act, tc, fn, title, src, url, sec, note) in ARCHIVES_EP05
    ]
    ep05["archival_photos"] = [
        {
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_lecun/{raw_fn}",
            "web_preview": f"assets/archival_photos/{web_fn}",
            "desc": desc,
        }
        for (pid, code, title, src, url, raw_fn, web_fn, desc) in ARCHIVAL_PHOTOS_EP05
    ]

    ua_card_files = sorted((ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP05_UA_CARD_*.png"))
    native_flow_ep05 = [
        ("CONV #01", "FLOW 2K • Школа Електроніки", "01:40–02:20", "Діодний мозок і мідні доріжки сигналу",
         "1920×1080 2K", "chip-cyan", "assets/flow_keyframes/ep05_flow_img_01_nerve_laser_b.jpg",
         "05_RAW_FOOTAGE/flow_images/BATCH3_GAMING_CHESS_GO_SCIENCE/EP05_FLOW_IMG_01_Biological_Synapse_Vs_Digital_Laser_2K.jpg"),
        ("NAVIGATOR #02", "FLOW 2K • Океан & Світові Моделі", "17:00–18:30", "Кібернетичний штурман крізь шторм даних",
         "1920×1080 2K", "chip-amber", "assets/flow_keyframes/ep05_flow_img_02_cybernetic_ship_navigator.jpg",
         "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP05_FLOW_IMG_02_Cybernetic_Torso_Conducting_Ship_2K.jpg"),
        ("JEPA #03", "FLOW 2K • Сенсорне сприйняття світу", "15:10–16:40", "Блакитний лазер крізь живу структуру листка",
         "1920×1080 2K", "chip-purple", "assets/flow_keyframes/ep05_flow_img_03_cyan_laser_leaf.jpg",
         "05_RAW_FOOTAGE/flow_images/BATCH4_COSMIC_SCALE_BIOLOGY_HARDWARE/EP05_FLOW_IMG_03_Cyan_Laser_Pulsing_Through_Leaf_2K.jpg"),
    ]
    gallery_ep05 = [
        {
            "code": code,
            "badge": badge,
            "tc": tc,
            "title": title,
            "dims": dims,
            "chip": chip,
            "web_preview": prev,
            "raw_path": rawp,
        }
        for (code, badge, tc, title, dims, chip, prev, rawp) in native_flow_ep05
        if (ROOT / rawp).exists() and (ROOT / "07_DASHBOARD" / prev).exists()
    ]
    for idx_c, card_p in enumerate(ua_card_files, 1):
        prev_rel = f"assets/cards_preview/{card_p.stem.lower()}.jpg"
        if (ROOT / "07_DASHBOARD" / prev_rel).exists():
            gallery_ep05.append({
                "code": f"UA CARD #{idx_c:02d}",
                "badge": "🇺🇦 4K Цитат-Картка",
                "tc": f"Акт {(idx_c - 1) // 2 + 1}",
                "title": card_p.stem.replace("EP05_UA_CARD_", "Картка ").replace("_", " "),
                "dims": "3840×2160 4K",
                "chip": "chip-emerald",
                "web_preview": prev_rel,
                "raw_path": f"05_RAW_FOOTAGE/dossiers_press/ukrainian_quote_cards/{card_p.name}",
            })
    ep05["flow_gallery"] = gallery_ep05

    MP_PATH.write_text(prefix + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

    ua_cards = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP05_*.png"))
    still_clips = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k").glob("EP05_*.mp4"))
    cat_json = {
        "episode": "EP05 — Yann LeCun",
        "updated_at": "2026-11-10",
        "summary": {
            "archival_broll_mp4": len(ARCHIVES_EP05),
            "archival_photos": len(ARCHIVAL_PHOTOS_EP05),
            "uhd_4k_dossiers": len(DOSSIERS_EP05),
            "ukrainian_4k_quote_cards": len(ua_cards),
            "ken_burns_and_card_4k_mp4": len(still_clips),
        },
        "dossiers": DOSSIERS_EP05,
        "archives": ep05["archives"],
        "archival_photos": ep05["archival_photos"],
        "ukrainian_4k_quote_cards": ua_cards,
        "rendered_cinematic_stills_4k": still_clips,
    }
    (ROOT / "05_RAW_FOOTAGE" / "EP05_MEDIA_CATALOG.json").write_text(json.dumps(cat_json, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP05 (Ян Лекун)",
        "",
        f"- **📼 Реальні архівні відеокліпи B-Roll (`05_RAW_FOOTAGE/archives/`):** {len(ARCHIVES_EP05)}",
        f"- **📸 Історичні фото та наукові артефакти (`05_RAW_FOOTAGE/speaker_portraits/young_lecun/`):** {len(ARCHIVAL_PHOTOS_EP05)}",
        f"- **🗂️ 4K Документальні досьє-пластини (`05_RAW_FOOTAGE/dossiers_press/`):** {len(DOSSIERS_EP05)}",
        f"- **🇺🇦 4K Українські цитат-картки (`ukrainian_quote_cards/`):** {len(ua_cards)}",
        f"- **🎞️ Ken Burns 4K відеокліпи зі стілів і карток (`rendered_cinematic_stills_4k/`):** {len(still_clips)}",
        "",
        "## 📼 Архівні відеокліпи (`EP05_VID_ARCH_01..16`)",
        "",
        "| Код | Таймкод EP05 | Файл | Джерело |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for a in ep05["archives"]:
        md.append(f"| **{a['code']}** | `{a['timecode']}` | `{a['mp4_file']}` | {a['source']} |")
    md += ["", "## 📸 Хронологічні архівні фото (`EP05_IMG_ARCH_*`)", "", "| Код | Файл | Ліцензія / Джерело |", "| :--- | :--- | :--- |"]
    for p in ep05["archival_photos"]:
        md.append(f"| **{p['code']}** | `{p['raw_file'].split('/')[-1]}` | [{p['source']}]({p['url']}) |")
    (ROOT / "05_RAW_FOOTAGE" / "EP05_MEDIA_CATALOG.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"[✓] EP05 synced: {len(DOSSIERS_EP05)} dossiers, {len(ARCHIVES_EP05)} archival videos, {len(ARCHIVAL_PHOTOS_EP05)} archival photos, {len(ua_cards)} UA cards, {len(still_clips)} 4K motion clips!")


if __name__ == "__main__":
    main()
