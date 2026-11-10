#!/usr/bin/env python3
"""
Synchronizes EP04 (Geoffrey Hinton) curated global archives across:
  - 07_DASHBOARD/data/media_acquisition_pool.js (dossiers, archives, archival_photos)
  - 05_RAW_FOOTAGE/EP04_MEDIA_CATALOG.json & EP04_MEDIA_CATALOG.md
Verifies every single file path exists on disk before saving.
"""
import json
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
MP_PATH = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"

DOSSIERS_EP04 = [
    {
        "id": "EP04_DOC_01",
        "ep": "04",
        "act": "ACT2",
        "timecode": "06:30–07:45",
        "title": "Learning representations by back-propagating errors (Nature 1986)",
        "source_label": "doi:10.1038/323533a0 — Rumelhart, Hinton & Williams (1986)",
        "highlight": "“We describe a new learning procedure, back-propagation, for networks of neurone-like units. The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector and the desired output vector.”",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_01_ACT2_Hinton_Backprop_Nature_1986.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_01_hinton_backprop.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_01.mp4",
    },
    {
        "id": "EP04_DOC_02",
        "ep": "04",
        "act": "ACT1",
        "timecode": "00:25–05:30",
        "title": "Тінь предків (Буль і Еверест) та лондонська столярна майстерня (1947–1978)",
        "source_label": "Bristol — Cambridge — London Carpentry Workshop — University of Edinburgh PhD",
        "highlight": "Descendant of George Boole & Sir George Everest; dropped Cambridge philosophy to spend a year planing oak cabinets — discovering physical matter never lies.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_02_ACT1_Bristol_Lineage_Boole_Everest_1947.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_02_boole_everest_lineage.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_02.mp4",
    },
    {
        "id": "EP04_DOC_03",
        "ep": "04",
        "act": "ACT2",
        "timecode": "07:45–11:00",
        "title": "Boltzmann Machines (Cognitive Science 1985): Статистична фізика в нейромережах",
        "source_label": "Cognitive Science 9(1), 147–169 (1985) • Ackley, Hinton & Sejnowski (Nobel 2024 Basis)",
        "highlight": "Refused Pentagon defense grants and moved to Toronto with severe spinal disc injury — connecting Boltzmann thermodynamics to generative neural nets.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_03_ACT2_Ackley_Hinton_Sejnowski_Boltzmann_1985.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_03_boltzmann_machine_1985.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_03.mp4",
    },
    {
        "id": "EP04_DOC_04",
        "ep": "04",
        "act": "ACT3",
        "timecode": "11:00–12:45",
        "title": "AlexNet (NIPS 2012) & Таємний аукціон DNNresearch на озері Тахо ($44M)",
        "source_label": "NIPS 2012 (Krizhevsky, Sutskever & Hinton) • Dual GTX 580 • ImageNet 26.2% → 15.3%",
        "highlight": "Shattered ImageNet error by 10.9 percentage points overnight, ending three decades of ridicule and triggering an hourly Google vs. Microsoft vs. Baidu bidding war.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_04_ACT3_AlexNet_ImageNet_NIPS_2012.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_04_alexnet_nips_2012.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_04.mp4",
    },
    {
        "id": "EP04_DOC_05",
        "ep": "04",
        "act": "ACT3",
        "timecode": "12:45–16:45",
        "title": "Премія Тюрінга (2018) та історична відставка з Google (травень 2023)",
        "source_label": "ACM A.M. Turing Award 2018 -> CBS 60 Minutes & BBC Resignation Statement (2023)",
        "highlight": "Human speech transfers ~10 bits/sec while 10,000 immortal AI copies share trillions of weights instantaneously — leading Hinton to leave Google and warn humanity.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_05_ACT3_Turing_2018_And_Google_Resignation_2023.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_05_google_exit_2023.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_05.mp4",
    },
    {
        "id": "EP04_DOC_06",
        "ep": "04",
        "act": "ACT4",
        "timecode": "16:45–22:00",
        "title": "Нобелівська премія з фізики 2024: Сповідь у Стокгольмі перед королями",
        "source_label": "Kungl. Vetenskapsakademien (Stockholm, Dec 10, 2024) • Hopfield & Hinton",
        "highlight": "“For foundational discoveries & inventions enabling machine learning with artificial neural networks” — standing at the Stockholm lectern in spinal pain to call for urgent AI safety governance.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP04_DOC_06_ACT4_Nobel_Physics_2024_Stockholm_Citation.png",
        "web_preview": "assets/dossiers_preview/ep04_doc_06_nobel_physics_2024.jpg",
        "video_preview": "assets/video_previews/dossiers/EP04_DOC_06.mp4",
    },
]

ARCHIVES_EP04 = [
    {
        "code": "ARCH #01",
        "act": "Акт 4 (Стокгольм)",
        "timecode": "17:10–17:18",
        "tc": "17:10–17:18",
        "file": "EP04_VID_ARCH_01_ACT4_24FPS_Hinton_Nobel_Warning_2024.mp4",
        "mp4_file": "EP04_VID_ARCH_01_ACT4_24FPS_Hinton_Nobel_Warning_2024.mp4",
        "title": "Нобелівське попередження Джеффрі Хінтона у Стокгольмі (2024)",
        "source": "Nobel Prize Official Banquet Speech (Dec 2024)",
        "url": "https://www.youtube.com/watch?v=-f5WQAk3dYo",
        "section": "00:00:35-00:00:43",
        "note": "Промова Джеффрі Хінтона у Стокгольмі про майбутнє надрозумних цифрових систем.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_01_ACT4_24FPS_Hinton_Nobel_Warning_2024.mp4",
    },
    {
        "code": "ARCH #02",
        "act": "Акт 1 (Родовід)",
        "timecode": "00:25–01:40",
        "tc": "00:25–01:40",
        "file": "EP04_VID_ARCH_02_ACT1_24FPS_Hinton_Ancestry_Boole_Everest.mp4",
        "mp4_file": "EP04_VID_ARCH_02_ACT1_24FPS_Hinton_Ancestry_Boole_Everest.mp4",
        "title": "Джеффрі Хінтон про прадіда Джорджа Буля та сера Джорджа Евереста",
        "source": "The Diary Of A CEO Archive (YouTube giT0ytynSqg)",
        "url": "https://www.youtube.com/watch?v=giT0ytynSqg",
        "section": "01:19:53-01:20:24",
        "note": "Сімейне дерево геніїв: засновник булевої логіки 0/1 та топограф вершини світу.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_02_ACT1_24FPS_Hinton_Ancestry_Boole_Everest.mp4",
    },
    {
        "code": "ARCH #03",
        "act": "Акт 1 (Лос-Аламос)",
        "timecode": "01:00–01:40",
        "tc": "01:00–01:40",
        "file": "EP04_VID_ARCH_03_ACT1_24FPS_Hinton_Joan_Los_Alamos_Cousin.mp4",
        "mp4_file": "EP04_VID_ARCH_03_ACT1_24FPS_Hinton_Joan_Los_Alamos_Cousin.mp4",
        "title": "Кузина Джоан Хінтон — фізик-ядерниця проєкту Оппенгеймера у Лос-Аламосі",
        "source": "The Diary Of A CEO Archive (YouTube giT0ytynSqg)",
        "url": "https://www.youtube.com/watch?v=giT0ytynSqg",
        "section": "01:20:39-01:21:05",
        "note": "Паралель моральної відповідальності фізиків атомної бомби і творців AGI.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_03_ACT1_24FPS_Hinton_Joan_Los_Alamos_Cousin.mp4",
    },
    {
        "code": "ARCH #04",
        "act": "Акт 2 (Зима ШІ)",
        "timecode": "05:30–07:00",
        "tc": "05:30–07:00",
        "file": "EP04_VID_ARCH_04_ACT2_24FPS_Hinton_Second_AI_Winter_Turing.mp4",
        "mp4_file": "EP04_VID_ARCH_04_ACT2_24FPS_Hinton_Second_AI_Winter_Turing.mp4",
        "title": "Хроніка ACM: льодовиковий період нейромереж 1987–2000-х",
        "source": "Association for Computing Machinery (ACM Turing 2018)",
        "url": "https://www.youtube.com/watch?v=HzilDIhWhrE",
        "section": "00:01:44-00:02:16",
        "note": "Як Хінтон, Бенжіо та Лекун десятиліттями пливли проти консенсусу індустрії.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_04_ACT2_24FPS_Hinton_Second_AI_Winter_Turing.mp4",
    },
    {
        "code": "ARCH #05",
        "act": "Акт 2 (Машини Больцмана)",
        "timecode": "07:00–08:15",
        "tc": "07:00–08:15",
        "file": "EP04_VID_ARCH_05_ACT2_24FPS_Hinton_Boltzmann_Machine_Nobel_Lecture.mp4",
        "mp4_file": "EP04_VID_ARCH_05_ACT2_24FPS_Hinton_Boltzmann_Machine_Nobel_Lecture.mp4",
        "title": "Нобелівська лекція з фізики: як машини Больцмана описують мислення",
        "source": "Nobel Prize Official Channel (Stockholm, Dec 8, 2024)",
        "url": "https://www.youtube.com/watch?v=XDE9DjpcSdI",
        "section": "00:01:46-00:02:14",
        "note": "Пояснення двійкових стохастичних нейронів і фізичних функцій енергії на сцені.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_05_ACT2_24FPS_Hinton_Boltzmann_Machine_Nobel_Lecture.mp4",
    },
    {
        "code": "ARCH #06",
        "act": "Акт 2 (Backprop)",
        "timecode": "08:15–08:45",
        "tc": "08:15–08:45",
        "file": "EP04_VID_ARCH_06_ACT2_24FPS_Hinton_Backpropagation_Nobel_Lecture.mp4",
        "mp4_file": "EP04_VID_ARCH_06_ACT2_24FPS_Hinton_Backpropagation_Nobel_Lecture.mp4",
        "title": "Нобелівська лекція: формула зворотного поширення помилки (Backpropagation)",
        "source": "Nobel Prize Official Channel (YouTube XDE9DjpcSdI)",
        "url": "https://www.youtube.com/watch?v=XDE9DjpcSdI",
        "section": "00:20:15-00:20:39",
        "note": "Фундаментальна роль зворотного поширення похідних у навчанні всіх сучасних моделей.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_06_ACT2_24FPS_Hinton_Backpropagation_Nobel_Lecture.mp4",
    },
    {
        "code": "ARCH #07",
        "act": "Акт 2 (1980-ті)",
        "timecode": "08:45–10:15",
        "tc": "08:45–10:15",
        "file": "EP04_VID_ARCH_07_ACT2_24FPS_Hinton_Sejnowski_1980s_Neuroscience.mp4",
        "mp4_file": "EP04_VID_ARCH_07_ACT2_24FPS_Hinton_Sejnowski_1980s_Neuroscience.mp4",
        "title": "Нобелівське інтерв'ю 2024: про роботу з Террі Сейновським у 1980-х",
        "source": "Nobel Prize Official Interview (YouTube 66WiF8fXL0k)",
        "url": "https://www.youtube.com/watch?v=66WiF8fXL0k",
        "section": "00:16:45-00:17:10",
        "note": "Історія створення алгоритму машини Больцмана на стику нейробіології й термодинаміки.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_07_ACT2_24FPS_Hinton_Sejnowski_1980s_Neuroscience.mp4",
    },
    {
        "code": "ARCH #08",
        "act": "Акт 3 (AlexNet GPU)",
        "timecode": "11:00–12:00",
        "tc": "11:00–12:00",
        "file": "EP04_VID_ARCH_08_ACT3_24FPS_Hinton_Two_Students_GPUs_Turing.mp4",
        "mp4_file": "EP04_VID_ARCH_08_ACT3_24FPS_Hinton_Two_Students_GPUs_Turing.mp4",
        "title": "Лекція Тюрінга: два ігрові GPU та двоє одержимих аспірантів Торонто",
        "source": "ACM Turing Award Lecture (YouTube VsnQf7exv5I)",
        "url": "https://www.youtube.com/watch?v=VsnQf7exv5I",
        "section": "00:27:12-00:27:36",
        "note": "Як Алекс Крижевський та Ілля Суцкевер запустили AlexNet на відеокартах NVIDIA.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_08_ACT3_24FPS_Hinton_Two_Students_GPUs_Turing.mp4",
    },
    {
        "code": "ARCH #09",
        "act": "Акт 3 ($44M Тахо)",
        "timecode": "12:00–12:45",
        "tc": "12:00–12:45",
        "file": "EP04_VID_ARCH_09_ACT3_24FPS_Hinton_AlexNet_DNNresearch_Auction.mp4",
        "mp4_file": "EP04_VID_ARCH_09_ACT3_24FPS_Hinton_AlexNet_DNNresearch_Auction.mp4",
        "title": "Аукціон компанії DNNresearch: торги гігантів за трьох науковців без продукту",
        "source": "The Diary Of A CEO Archive (YouTube giT0ytynSqg)",
        "url": "https://www.youtube.com/watch?v=giT0ytynSqg",
        "section": "01:11:51-01:12:28",
        "note": "Історія створення DNNresearch у 65 років разом із Суцкевером і Крижевським.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_09_ACT3_24FPS_Hinton_AlexNet_DNNresearch_Auction.mp4",
    },
    {
        "code": "ARCH #10",
        "act": "Акт 3 (Тюрінг 2018)",
        "timecode": "12:45–13:30",
        "tc": "12:45–13:30",
        "file": "EP04_VID_ARCH_10_ACT3_24FPS_Hinton_Turing_2018_Three_Fathers.mp4",
        "mp4_file": "EP04_VID_ARCH_10_ACT3_24FPS_Hinton_Turing_2018_Three_Fathers.mp4",
        "title": "Тріо Хрещених батьків ШІ: Хінтон, Бенжіо та Лекун отримують Премію Тюрінга",
        "source": "Association for Computing Machinery (ACM Turing 2018)",
        "url": "https://www.youtube.com/watch?v=HzilDIhWhrE",
        "section": "00:04:50-00:05:14",
        "note": "Офіційна церемонія визнання революції глибокого навчання 2018 року.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_10_ACT3_24FPS_Hinton_Turing_2018_Three_Fathers.mp4",
    },
    {
        "code": "ARCH #11",
        "act": "Акт 3 (Відставка з Google)",
        "timecode": "14:45–15:30",
        "tc": "14:45–15:30",
        "file": "EP04_VID_ARCH_11_ACT3_24FPS_Hinton_Leaving_Google_Speak_Freely.mp4",
        "mp4_file": "EP04_VID_ARCH_11_ACT3_24FPS_Hinton_Leaving_Google_Speak_Freely.mp4",
        "title": "Чому Хінтон пішов із Google у квітні 2023: право говорити без цензури",
        "source": "The Diary Of A CEO Archive (YouTube giT0ytynSqg)",
        "url": "https://www.youtube.com/watch?v=giT0ytynSqg",
        "section": "01:15:02-01:15:24",
        "note": "Пряма відповідь про свободу слова та моральний обов'язок застерегти світ.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_11_ACT3_24FPS_Hinton_Leaving_Google_Speak_Freely.mp4",
    },
    {
        "code": "ARCH #12",
        "act": "Акт 3 (BBC 2023)",
        "timecode": "15:30–16:00",
        "tc": "15:30–16:00",
        "file": "EP04_VID_ARCH_12_ACT3_24FPS_Hinton_BBC_Regret_Warning_2023.mp4",
        "mp4_file": "EP04_VID_ARCH_12_ACT3_24FPS_Hinton_BBC_Regret_Warning_2023.mp4",
        "title": "Екстрений випуск BBC News (2023): «Хрещений батько ШІ» залишає Google",
        "source": "BBC News Official (YouTube DsBGaHywRhs)",
        "url": "https://www.youtube.com/watch?v=DsBGaHywRhs",
        "section": "00:00:02-00:00:28",
        "note": "Момент, коли відставка 75-річного вченого сколихнула перші шпальти світових медіа.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_12_ACT3_24FPS_Hinton_BBC_Regret_Warning_2023.mp4",
    },
    {
        "code": "ARCH #13",
        "act": "Акт 3 (Трильйони біт/с)",
        "timecode": "14:45–16:15",
        "tc": "14:45–16:15",
        "file": "EP04_VID_ARCH_13_ACT3_24FPS_Hinton_Digital_Weights_Trillions_Bits.mp4",
        "mp4_file": "EP04_VID_ARCH_13_ACT3_24FPS_Hinton_Digital_Weights_Trillions_Bits.mp4",
        "title": "10 біт/с людської мови проти трильйонів біт/с цифрових копій нейромережі",
        "source": "The Diary Of A CEO Archive (YouTube giT0ytynSqg)",
        "url": "https://www.youtube.com/watch?v=giT0ytynSqg",
        "section": "00:57:41-00:58:14",
        "note": "Математичне пояснення того, чому цифровий інтелект безсмертний у передачі досвіду.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_13_ACT3_24FPS_Hinton_Digital_Weights_Trillions_Bits.mp4",
    },
    {
        "code": "ARCH #14",
        "act": "Акт 3 (CBS 60 Minutes)",
        "timecode": "16:00–16:45",
        "tc": "16:00–16:45",
        "file": "EP04_VID_ARCH_14_ACT3_24FPS_Hinton_60Minutes_Species_Control.mp4",
        "mp4_file": "EP04_VID_ARCH_14_ACT3_24FPS_Hinton_60Minutes_Species_Control.mp4",
        "title": "Скотт Пеллі на CBS 60 Minutes: «Вони можуть перехопити контроль у людства»",
        "source": "CBS 60 Minutes Archive (YouTube QH6QqjIwv68)",
        "url": "https://www.youtube.com/watch?v=QH6QqjIwv68",
        "section": "00:11:50-00:12:28",
        "note": "Легендарний діалог про експерименти безпеки та паралель із Робертом Оппенгеймером.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_14_ACT3_24FPS_Hinton_60Minutes_Species_Control.mp4",
    },
    {
        "code": "ARCH #15",
        "act": "Акт 4 (Пресконференція Торонто)",
        "timecode": "16:45–17:10",
        "tc": "16:45–17:10",
        "file": "EP04_VID_ARCH_15_ACT4_24FPS_Hinton_UofT_Students_Nobel_Presser.mp4",
        "mp4_file": "EP04_VID_ARCH_15_ACT4_24FPS_Hinton_UofT_Students_Nobel_Presser.mp4",
        "title": "Пресконференція в Університеті Торонто: вдячність учням (Ілля Суцкевер)",
        "source": "University of Toronto Official (YouTube H7DgMFqrON0)",
        "url": "https://www.youtube.com/watch?v=H7DgMFqrON0",
        "section": "00:03:16-00:03:40",
        "note": "Зворушлива й дотепна промова після оголошення Нобелівської премії з фізики 2024.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_15_ACT4_24FPS_Hinton_UofT_Students_Nobel_Presser.mp4",
    },
    {
        "code": "ARCH #16",
        "act": "Акт 4 (Золота зала Стокгольма)",
        "timecode": "17:20–18:15",
        "tc": "17:20–18:15",
        "file": "EP04_VID_ARCH_16_ACT4_24FPS_Hinton_Banquet_Existential_Threat.mp4",
        "mp4_file": "EP04_VID_ARCH_16_ACT4_24FPS_Hinton_Banquet_Existential_Threat.mp4",
        "title": "Золота зала Стокгольма (10 грудня 2024): екзистенційне попередження королям",
        "source": "Nobel Prize Official Channel (YouTube -f5WQAk3dYo)",
        "url": "https://www.youtube.com/watch?v=-f5WQAk3dYo",
        "section": "00:02:26-00:02:52",
        "note": "Кульмінація виступу лауреата Нобелівської премії перед світовими лідерами.",
        "video_preview": "assets/video_previews/archives/EP04_VID_ARCH_16_ACT4_24FPS_Hinton_Banquet_Existential_Threat.mp4",
    },
]

ARCHIVAL_PHOTOS_EP04 = [
    ("EP04_PH_01", "ФОТО #01 (1847–1864)", "Джордж Буль — прапрадід Джеффрі Хінтона, творець булевої логіки 0 і 1",
     "Wikimedia Commons (Public Domain)", "https://commons.wikimedia.org/wiki/File:Portrait_of_Boole.jpg",
     "EP04_IMG_ARCH_01_George_Boole_Logician_Ancestor.jpg",
     "Вікторіанський гравійований портрет видатного математика, під тінню якого виріс молодий Джеффрі Хінтон."),
    ("EP04_PH_02", "ФОТО #02 (Гімалаї • Еверест)", "Північний схил вершини світу, названої іменем родича сера Джорджа Евереста",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:20110810_North_Face_of_Everest_Tibet_China_Panoramic.jpg",
     "EP04_IMG_ARCH_02_Mount_Everest_Peak_Survey_Lineage.jpg",
     "Спадщина родини Еверестів-Булів: прабабуся Мері Еверест-Буль була племінницею легендарного геодезиста."),
    ("EP04_PH_03", "ФОТО #03 (1967–1970)", "King's College, Кембридж — бунт юного Хінтона проти фізики й філософії",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Cambridge_-_King%27s_College,_founded_in_1441_-_Front_Court_-_View_SSE_on_Wilkins%27_Building_1828_%26_Gibbs%27_Building_1724.jpg",
     "EP04_IMG_ARCH_03_Kings_College_Cambridge_Front_Court.jpg",
     "Парадний двір коледжу у Кембриджі, звідки студент Хінтон пішов шукати чесність фізичної праці."),
    ("EP04_PH_04", "ФОТО #04 (1970–1972)", "Столярний рубанок і дерев'яна стружка — лондонський рік теслярства",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Germany_Plane-with-wood-shavings-and-carpenters-pencil-01.jpg",
     "EP04_IMG_ARCH_04_London_Carpentry_Hand_Plane_Oak.jpg",
     "«Дерево не обдуриш красивою цитатою чи дипломом — матерія чесна»."),
    ("EP04_PH_05", "ФОТО #05 (1972–1978)", "Единбурзький університет (Informatics Forum) — захист PhD про нейромережі",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Informatics_Forum_University_of_Edinburgh.JPG",
     "EP04_IMG_ARCH_05_University_of_Edinburgh_Informatics_Forum.jpg",
     "Академічна домівка, де молодий докторант відстоював нейронні мережі всупереч «Зимі ШІ»."),
    ("EP04_PH_06", "ФОТО #06 (1982–1987)", "Університет Карнегі-Меллона (CMU Hamerschlag Hall) — робота над Boltzmann Machines",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Carnegie_Mellon_Hamerschlag_Hall_and_Scott_Hall.jpg",
     "EP04_IMG_ARCH_06_CMU_Hamerschlag_Hall_Pittsburgh.jpg",
     "Кампус у Піттсбурзі, з якого Хінтон поїхав у Канаду, відмовившись брати військові гроші Пентагону."),
    ("EP04_PH_07", "ФОТО #07 (1987–2000-ті)", "Зимовий корпус Sandford Fleming Університету Торонто",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Sandford_Fleming_Building_2011_Toronto.jpg",
     "EP04_IMG_ARCH_07_University_of_Toronto_Sandford_Fleming.jpg",
     "Сніжний кампус Університету Торонто, де Хінтон стоячи та лежачи на підлозі пережив 25 років наукового вигнання."),
    ("EP04_PH_08", "ФОТО #08 (Торонто)", "Bahen Centre for Information Technology — центр прориву глибокого навчання (CIFAR)",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Bahen_Front_View.jpg",
     "EP04_IMG_ARCH_08_University_of_Toronto_Bahen_Centre.jpg",
     "Корпус інформатики Торонто, у стінах якого народжувалися дослідження AlexNet і RBM."),
    ("EP04_PH_09", "ФОТО #09 (Університет Торонто)", "Історична ротонда Convocation Hall — головна сцена канадської науки",
     "Wikimedia Commons (CC0 Public Domain)", "https://commons.wikimedia.org/wiki/File:Convocation_Hall,_University_of_Toronto_Northeastern_entrance.jpg",
     "EP04_IMG_ARCH_09_University_of_Toronto_Convocation_Hall.jpg",
     "Університет Торонто, що став оплотом світового відродження нейромереж."),
    ("EP04_PH_10", "ФОТО #10 (Торонто • Сцена)", "Виступ Джеффрі Хінтона про революцію нейромереж (Collision Conference)",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Collision_2024_-_PO2_5304_(53801813022).jpg",
     "EP04_IMG_ARCH_10_Geoffrey_Hinton_Toronto_Tech_Stage.jpg",
     "Професор-емерит Університету Торонто перед багатотисячною аудиторією у Канаді."),
    ("EP04_PH_11", "ФОТО #11 (Грудень 2012)", "Stateline, Озеро Тахо — місце готельного аукціону DNNresearch на $44M",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:South_Lake_Tahoe_(CA,_USA),_Blick_nach_Stateline_--_2022_--_162945.jpg",
     "EP04_IMG_ARCH_11_Lake_Tahoe_DNNresearch_Auction_2012.jpg",
     "Готельні гори на межі Каліфорнії та Невади, де Google виграв торги за Хінтона, Суцкевера і Крижевського."),
    ("EP04_PH_12", "ФОТО #12 (2018 • Тюрінг)", "Троє Хрещених батьків ШІ разом: Йошуа Бенжіо, Джеффрі Хінтон, Ян Лекун",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Deep_Thinkers_on_Deep_Learning.jpg",
     "EP04_IMG_ARCH_12_Three_Godfathers_Deep_Learning_Turing_2018.jpg",
     "Рідкісний груповий кадр трьох архітекторів сучасного Deep Learning, лауреатів Премії Тюрінга 2018."),
    ("EP04_PH_13", "ФОТО #13 (1998–2024)", "Історичний графік прориву точності ШІ на бенчмарках після AlexNet 2012",
     "Wikimedia Commons (OGL 3 Open Govt License)", "https://commons.wikimedia.org/wiki/File:Performance_of_AI_models_on_various_benchmarks_from_1998_to_2024.png",
     "EP04_IMG_ARCH_13_AI_Benchmarks_1998_2024_Exponential.jpg",
     "Наукова діаграма вертикального стрибка комп'ютерного зору й мови після впровадження Backprop + GPU."),
    ("EP04_PH_14", "ФОТО #14 (Червень 2023)", "Перший публічний виступ після відставки з Google — попередження світу на Collision",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Collision_2023_-_Centre_Stage_RCZ_1307.jpg",
     "EP04_IMG_ARCH_14_Geoffrey_Hinton_Collision_2023_Stage.jpg",
     "Червень 2023 року: вільний від корпоративних рамок учений попереджає про цифрові ризики."),
    ("EP04_PH_15", "ФОТО #15 (2024 • Торонто)", "Великий емоційний портрет Джеффрі Хінтона у софітах сцени",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Collision_2024_-_VR5_3157_(53803195889).jpg",
     "EP04_IMG_ARCH_15_Geoffrey_Hinton_Collision_2024_Toronto.jpg",
     "«Усе життя я думав, що нейромережі — карикатура на мозок. Тепер бачу, що вони обганяють еволюцію»."),
    ("EP04_PH_16", "ФОТО #16 (8 грудня 2024)", "Нобелівська лекція Джеффрі Хінтона у Стокгольмі про машини Больцмана",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Geoffrey_Hinton_at_the_2024_Nobel_Lectures.jpg",
     "EP04_IMG_ARCH_16_Hinton_Nobel_Physics_Lectures_2024_Stockholm.jpg",
     "Офіційна лекція Нобелівського лауреата з фізики 2024 у Шведській королівській академії наук."),
    ("EP04_PH_17", "ФОТО #17 (Грудень 2024)", "Джон Гопфілд і Джеффрі Хінтон — два Нобелівські лауреати з фізики 2024",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:John_J._Hopfield_and_Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics.jpg",
     "EP04_IMG_ARCH_17_Hopfield_Hinton_2024_Nobel_Laureates.jpg",
     "Символічний дует фізиків-першопрохідців, чиї моделі 1982–1985 років заклали еру ШІ."),
    ("EP04_PH_18", "ФОТО #18 (Грудень 2024)", "Джеффрі Хінтон на пресконференції Нобелівського тижня в Стокгольмі",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Geoffrey_Hinton_at_2024_Nobel_Prize_Conference_8.jpg",
     "EP04_IMG_ARCH_18_Hinton_2024_Nobel_Prize_Conference.jpg",
     "Спокійний і чесний погляд ученого, який розсіяв тінь предків і залишив совість вищою за славу."),
]


def verify_paths():
    missing = []
    for d in DOSSIERS_EP04:
        if not (ROOT / d["raw_4k_png"]).exists():
            missing.append(d["raw_4k_png"])
        for k in ["web_preview", "video_preview"]:
            if not (ROOT / "07_DASHBOARD" / d[k]).exists():
                missing.append("07_DASHBOARD/" + d[k])
    for a in ARCHIVES_EP04:
        if not (ROOT / "05_RAW_FOOTAGE" / "archives" / a["mp4_file"]).exists():
            missing.append("05_RAW_FOOTAGE/archives/" + a["mp4_file"])
        if not (ROOT / "07_DASHBOARD" / a["video_preview"]).exists():
            missing.append("07_DASHBOARD/" + a["video_preview"])
    for item in ARCHIVAL_PHOTOS_EP04:
        fn = item[5]
        if not (ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_hinton" / fn).exists():
            missing.append("young_hinton/" + fn)
        if not (ROOT / "07_DASHBOARD" / "assets" / "archival_photos" / fn).exists():
            missing.append("archival_photos/" + fn)
    if missing:
        raise RuntimeError("Missing verified files:\n  " + "\n  ".join(missing))


def main():
    verify_paths()
    raw = MP_PATH.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    mp = json.loads(raw[len(prefix):].rstrip(";\n "))

    ep04 = mp["04"]
    ep04["dossiers"] = DOSSIERS_EP04
    ep04["archives"] = ARCHIVES_EP04
    ep04["archival_photos"] = [
        {
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_hinton/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        }
        for (pid, code, title, src, url, fn, desc) in ARCHIVAL_PHOTOS_EP04
    ]

    MP_PATH.write_text(prefix + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

    ua_cards = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP04_*.png"))
    still_clips = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k").glob("EP04_*.mp4"))
    cat_json = {
        "episode": "EP04 — Geoffrey Hinton",
        "updated_at": "2026-11-10",
        "summary": {
            "archival_broll_mp4": len(ARCHIVES_EP04),
            "archival_photos": len(ARCHIVAL_PHOTOS_EP04),
            "uhd_4k_dossiers": len(DOSSIERS_EP04),
            "ukrainian_4k_quote_cards": len(ua_cards),
            "ken_burns_and_card_4k_mp4": len(still_clips),
        },
        "dossiers": DOSSIERS_EP04,
        "archives": ARCHIVES_EP04,
        "archival_photos": ep04["archival_photos"],
        "ukrainian_4k_quote_cards": ua_cards,
        "rendered_cinematic_stills_4k": still_clips,
    }
    (ROOT / "05_RAW_FOOTAGE" / "EP04_MEDIA_CATALOG.json").write_text(json.dumps(cat_json, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP04 (Джеффрі Хінтон)",
        "",
        f"- **📼 Реальні архівні відеокліпи B-Roll (`05_RAW_FOOTAGE/archives/`):** {len(ARCHIVES_EP04)}",
        f"- **📸 Історичні фото та наукові артефакти (`05_RAW_FOOTAGE/speaker_portraits/young_hinton/`):** {len(ARCHIVAL_PHOTOS_EP04)}",
        f"- **🗂️ 4K Документальні досьє-пластини (`05_RAW_FOOTAGE/dossiers_press/`):** {len(DOSSIERS_EP04)}",
        f"- **🇺🇦 4K Українські цитат-картки (`ukrainian_quote_cards/`):** {len(ua_cards)}",
        f"- **🎞️ Ken Burns 4K відеокліпи зі стілів і карток (`rendered_cinematic_stills_4k/`):** {len(still_clips)}",
        "",
        "## 📼 Архівні відеокліпи (`EP04_VID_ARCH_01..16`)",
        "",
        "| Код | Таймкод EP04 | Файл | Джерело |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for a in ARCHIVES_EP04:
        md.append(f"| **{a['code']}** | `{a['timecode']}` | `{a['mp4_file']}` | {a['source']} |")
    md += ["", "## 📸 Хронологічні архівні фото (`EP04_IMG_ARCH_*`)", "", "| Код | Файл | Ліцензія / Джерело |", "| :--- | :--- | :--- |"]
    for p in ep04["archival_photos"]:
        md.append(f"| **{p['code']}** | `{p['raw_file'].split('/')[-1]}` | [{p['source']}]({p['url']}) |")
    (ROOT / "05_RAW_FOOTAGE" / "EP04_MEDIA_CATALOG.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"[✓] EP04 synced: {len(DOSSIERS_EP04)} dossiers, {len(ARCHIVES_EP04)} archival videos, {len(ARCHIVAL_PHOTOS_EP04)} archival photos, {len(ua_cards)} UA cards, {len(still_clips)} 4K motion clips!")


if __name__ == "__main__":
    main()
