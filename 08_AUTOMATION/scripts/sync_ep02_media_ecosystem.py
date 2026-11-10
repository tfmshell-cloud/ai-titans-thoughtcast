#!/usr/bin/env python3
"""
Synchronizes EP02 (Jensen Huang) curated global archives across:
  - 07_DASHBOARD/data/media_acquisition_pool.js (dossiers, archives, archival_photos)
  - 05_RAW_FOOTAGE/EP02_MEDIA_CATALOG.json & EP02_MEDIA_CATALOG.md
Verifies every single file path exists on disk before saving.
"""
import json
import os
import subprocess
import re
from pathlib import Path

ROOT = Path("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast")
FFMPEG = "/Users/volodymyrkatasonov/Library/Python/3.9/bin/ffmpeg"
MP_PATH = ROOT / "07_DASHBOARD" / "data" / "media_acquisition_pool.js"

DOSSIERS_EP02 = [
    {
        "id": "EP02_DOC_01",
        "ep": "02",
        "act": "ACT3",
        "timecode": "10:20–11:40",
        "title": "NVIDIA Corporation: «30 днів до банкрутства» та ставка $500M на CUDA",
        "source_label": "NVIDIA Corp. S-1 Risk Factors & G80 Unified CUDA Architecture Directive (1997 / 2006)",
        "highlight": "“Our company is thirty days from going out of business.” — Followed in 2006 by embedding CUDA compute silicon into every GeForce GPU at $500M annual R&D cost while Wall Street cut share price by 70%.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_01_ACT2_NVIDIA_RIVA128_SEC_1999_IPO.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_01_nvidia_cuda.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_01.mp4",
    },
    {
        "id": "EP02_DOC_02",
        "ep": "02",
        "act": "ACT2",
        "timecode": "05:15–06:05",
        "title": "Кабінка #1 у Denny's на Берріесса-роуд: Хартія заснування NVIDIA (1993)",
        "source_label": "2484 Berryessa Rd, San Jose CA • Jensen Huang, Chris Malachowsky & Curtis Priem (April 1993)",
        "highlight": "“We didn't have a clue how to write a business plan. Don Valentine of Sequoia Capital invested $1.4M purely on our former CEO's word that we were builders who refused to lose.”",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_02_ACT2_Dennys_Founding_Charter_1993.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_02_dennys_1993.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_02.mp4",
    },
    {
        "id": "EP02_DOC_03",
        "ep": "02",
        "act": "ACT2",
        "timecode": "06:30–09:30",
        "title": "Провал NV1, звільнення 60% штату та рятівний чек Sega на $5M (1997)",
        "source_label": "NVIDIA – SEGA Contract Renegotiation • Shoichiro Irimajiri $5M Equity Lifeline",
        "highlight": "Huang flew to Tokyo to tell Sega CEO Shoichiro Irimajiri the truth: NVIDIA must walk away from its broken Sega console chip — yet asked Sega to convert the remaining $5M milestone payment into equity so NVIDIA could survive 6 months.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_03_ACT2_Sega_NV2_Rescue_Memorandum_1997.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_03_sega_rescue_1997.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_03.mp4",
    },
    {
        "id": "EP02_DOC_04",
        "ep": "02",
        "act": "ACT2",
        "timecode": "09:30–11:18",
        "title": "RIVA 128 та народження першого у світі GPU — GeForce 256 (1997–1999)",
        "source_label": "TSMC First-Silicon Success & NASDAQ: NVDA IPO (Jan 22, 1999)",
        "highlight": "On October 11, 1999, NVIDIA unveiled GeForce 256 (NV10) with integrated hardware Transform & Lighting — coining the industry category 'GPU' (Graphics Processing Unit) with 17 million transistors on 220nm silicon.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_04_ACT2_RIVA128_GeForce256_First_GPU_1999.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_04_riva_geforce_1999.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_04.mp4",
    },
    {
        "id": "EP02_DOC_05",
        "ep": "02",
        "act": "ACT3",
        "timecode": "13:45–15:25",
        "title": "Прорив AlexNet 2012 на двох ігрових GTX 580: виправдання ставки CUDA",
        "source_label": "University of Toronto • Krizhevsky, Sutskever & Hinton • ImageNet ILSVRC-2012",
        "highlight": "Trained directly on CUDA kernels in Alex Krizhevsky's bedroom, AlexNet shattered the ImageNet Top-5 error benchmark (15.3% vs. 26.2%), triggering Huang's company-wide pivot: NVIDIA goes 100% all-in on Deep Learning.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_05_ACT3_AlexNet_GTX580_Turning_Point_2012.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_05_alexnet_gtx580_2012.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_05.mp4",
    },
    {
        "id": "EP02_DOC_06",
        "ep": "02",
        "act": "ACT3",
        "timecode": "15:25–16:15",
        "title": "Серпень 2016: Особиста доставка першого суперкомп'ютера DGX-1 команді OpenAI",
        "source_label": "San Francisco Hand-Delivery • 8× Pascal P100 • Inscribed Chassis for Elon Musk & OpenAI",
        "highlight": "Handwritten Marker Inscription on OpenAI's Chassis: “To Elon & the OpenAI team — To the future of computing & humanity. I give you the world's first DGX-1.” — Jensen Huang, 2016.",
        "raw_4k_png": "05_RAW_FOOTAGE/dossiers_press/EP02_DOC_06_ACT3_DGX1_OpenAI_Delivery_2016.png",
        "web_preview": "assets/dossiers_preview/ep02_doc_06_dgx1_openai_2016.jpg",
        "video_preview": "assets/video_previews/dossiers/EP02_DOC_06.mp4",
    },
]

ARCHIVES_EP02 = [
    {
        "code": "ARCH #01",
        "act": "Акт 3 (GTC Blackwell)",
        "timecode": "15:40–16:00",
        "tc": "15:40–16:00",
        "title": "Вихід Дженсена Хуанга у шкіряній куртці на сцену арени GTC",
        "source": "NVIDIA Official GTC Keynote Press Stream (YouTube _waPvOwL9Z8)",
        "url": "https://www.youtube.com/watch?v=_waPvOwL9Z8",
        "section": "00:14:20-00:14:28",
        "mp4_file": "EP02_VID_ARCH_01_ACT3_24FPS_Huang_GTC_Stage_Walk.mp4",
        "file": "EP02_VID_ARCH_01_ACT3_24FPS_Huang_GTC_Stage_Walk.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_01_ACT3_24FPS_Huang_GTC_Stage_Walk.mp4",
        "specs": "1920×1080 • 24 fps • 8.0s • H.264 • Головна сцена GTC",
        "davinci_usage": "Вступ або фінал індустріального тріумфу: фірмова хода Хуанга на сцені перед розробниками.",
        "note": "Фірмова хода Дженсена Хуанга у шкіряній куртці на сцені арени GTC.",
        "verified_speaker": "Jensen Huang (NVIDIA GTC)",
    },
    {
        "code": "ARCH #02",
        "act": "Акт 3 (Blackwell Wafer)",
        "timecode": "15:50–16:15",
        "tc": "15:50–16:15",
        "title": "Презентація кремнієвої пластини та суперчіпа Blackwell B200",
        "source": "NVIDIA Official GTC Keynote Press Stream (YouTube _waPvOwL9Z8)",
        "url": "https://www.youtube.com/watch?v=_waPvOwL9Z8",
        "section": "00:46:10-00:46:18",
        "mp4_file": "EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4",
        "file": "EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_02_ACT3_24FPS_Huang_Blackwell_Wafer_Reveal.mp4",
        "specs": "1920×1080 • 24 fps • 8.0s • H.264 • Тунель серверного ядра GTC",
        "davinci_usage": "Акт 3–4: сучасна масштабна архітектура ШІ-фабрик NVIDIA.",
        "note": "Демонстрація дзеркальної кремнієвої пластини та суперчіпа Blackwell.",
        "verified_speaker": "Jensen Huang (Blackwell Reveal)",
    },
    {
        "code": "ARCH #03",
        "act": "Акт 1 (Кентуккі 1972)",
        "timecode": "01:36–02:15",
        "tc": "01:36–02:15",
        "title": "«У 9 років у Oneida (Кентуккі) я мав мити всі туалети» — інтерв'ю Stripe",
        "source": "Stripe Sessions 2024 Conversation with Jensen Huang (YouTube 8Pfa8kPjUio)",
        "url": "https://www.youtube.com/watch?v=8Pfa8kPjUio",
        "section": "00:09:44-00:10:00",
        "mp4_file": "EP02_VID_ARCH_03_ACT1_24FPS_Huang_Oneida_Bathrooms_Age9.mp4",
        "file": "EP02_VID_ARCH_03_ACT1_24FPS_Huang_Oneida_Bathrooms_Age9.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_03_ACT1_24FPS_Huang_Oneida_Bathrooms_Age9.mp4",
        "specs": "1920×1080 • 24 fps • 16.0s • H.264 • Чистий звук",
        "davinci_usage": "Акт 1: пряма мова Дженсена про приїзд до США та щоденне прибирання інтернату.",
        "note": "Хуанг згадує інститут Oneida Baptist у Кентуккі та свою першу роботу у 9 років.",
        "verified_speaker": "Jensen Huang (Stripe 2024)",
    },
    {
        "code": "ARCH #04",
        "act": "Акт 1 (Stanford GSB)",
        "timecode": "02:15–03:30",
        "tc": "02:15–03:30",
        "title": "«Для мене немає низької праці — я вимив більше туалетів, ніж усі ви»",
        "source": "Stanford Graduate School of Business 2024 (YouTube lXLBTBBil2U)",
        "url": "https://www.youtube.com/watch?v=lXLBTBBil2U",
        "section": "00:30:27-00:30:43",
        "mp4_file": "EP02_VID_ARCH_04_ACT1_24FPS_Huang_Dennys_Dishwasher_NoTaskBeneath.mp4",
        "file": "EP02_VID_ARCH_04_ACT1_24FPS_Huang_Dennys_Dishwasher_NoTaskBeneath.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_04_ACT1_24FPS_Huang_Dennys_Dishwasher_NoTaskBeneath.mp4",
        "specs": "1920×1080 • 24 fps • 16.0s • H.264 • Дві камери, Stanford",
        "davinci_usage": "Пряма синхронізація з рядком сценарію «Пів століття потому на сцені Стенфорду: немає низької праці».",
        "note": "Цитата зі Стенфордської школи бізнесу: «To me, no task is beneath me... I've cleaned more toilets than all of you combined».",
        "verified_speaker": "Jensen Huang (Stanford GSB 2024)",
    },
    {
        "code": "ARCH #05",
        "act": "Акт 1–2 (60 Minutes • Denny's)",
        "timecode": "04:40–05:15",
        "tc": "04:40–05:15",
        "title": "Повернення у забігайлівку Denny's на Berryessa Rd та горнятко Denny's (60 Minutes)",
        "source": "CBS 60 Minutes (29.04.2024, YouTube DpQQi2scsHo)",
        "url": "https://www.youtube.com/watch?v=DpQQi2scsHo",
        "section": "00:07:49-00:08:09",
        "mp4_file": "EP02_VID_ARCH_05_ACT1_24FPS_Huang_Dennys_Booth_Founding_60Min.mp4",
        "file": "EP02_VID_ARCH_05_ACT1_24FPS_Huang_Dennys_Booth_Founding_60Min.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_05_ACT1_24FPS_Huang_Dennys_Booth_Founding_60Min.mp4",
        "specs": "1920×1080 • 24 fps • 20.0s • H.264 • Аероплан кампуса -> інтер'єр Denny's",
        "davinci_usage": "Акт 1/2 перехід: аероплан штаб-квартири Endeavor переходить у двері Denny's та горнятко кави.",
        "note": "Унікальні кадри CBS 60 Minutes: Хуанг повертається до свого першого місця роботи та кабінки заснування NVIDIA.",
        "verified_speaker": "Jensen Huang & Bill Whitaker (CBS 60 Minutes)",
    },
    {
        "code": "ARCH #06",
        "act": "Акт 2 (1993 • Меморіальна табличка)",
        "timecode": "05:15–05:38",
        "tc": "05:15–05:38",
        "title": "Табличка в кабінці Denny's («$2 Trillion Company») + рідкісне фото молодого Хуанга 1990-х",
        "source": "CBS 60 Minutes (29.04.2024, YouTube DpQQi2scsHo)",
        "url": "https://www.youtube.com/watch?v=DpQQi2scsHo",
        "section": "00:08:21-00:08:36",
        "mp4_file": "EP02_VID_ARCH_06_ACT1_24FPS_Huang_Dennys_Booth_Inside_60Min.mp4",
        "file": "EP02_VID_ARCH_06_ACT1_24FPS_Huang_Dennys_Booth_Inside_60Min.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_06_ACT1_24FPS_Huang_Dennys_Booth_Inside_60Min.mp4",
        "specs": "1920×1080 • 24 fps • 15.0s • H.264 • Вінтажні 3D-ігри -> табличка -> фото молодого Хуанга",
        "davinci_usage": "Акт 2 старт: автентичне архівне фото молодого інженера Хуанга поруч із табличкою кабінки #1.",
        "note": "Рідкісні кадри ретро-графіки 1990-х, меморіальної таблички Denny's та молодого Дженсена.",
        "verified_speaker": "Jensen Huang (1990s Archival Footage)",
    },
    {
        "code": "ARCH #07",
        "act": "Акт 2 (Oregon State 2009)",
        "timecode": "06:30–07:05",
        "tc": "06:30–07:05",
        "title": "Молодий Джен-Сун Хуанг у 2009 році на випуску Oregon State University: «Ми провалилися»",
        "source": "Oregon State University Commencement 2009 (YouTube lMW5v7wK7zo)",
        "url": "https://www.youtube.com/watch?v=lMW5v7wK7zo",
        "section": "00:02:40-00:02:56",
        "mp4_file": "EP02_VID_ARCH_07_ACT2_24FPS_Huang_2009_OSU_We_Failed.mp4",
        "file": "EP02_VID_ARCH_07_ACT2_24FPS_Huang_2009_OSU_We_Failed.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_07_ACT2_24FPS_Huang_2009_OSU_We_Failed.mp4",
        "specs": "640×480 (ориг. 2009) • 24 fps • 16.0s • H.264 • Рідкісний запис OSU 2009",
        "davinci_usage": "Акт 2: розповідь про провал першого чипа NV1 в оригінальному голосі й образі Хуанга 2009 року.",
        "note": "Унікальний ранній виступ 46-річного Хуанга в рідному університеті в Орегоні про технічну поразку NV1.",
        "verified_speaker": "Jen-Hsun Huang (OSU 2009)",
    },
    {
        "code": "ARCH #08",
        "act": "Акт 2 (Sega $5M • NTU 2023)",
        "timecode": "08:25–09:30",
        "tc": "08:25–09:30",
        "title": "Історія дзвінка в Токіо до CEO Sega Сьоїтіро Ірімадзірі: «Знайдіть іншого, але врятуйте нас»",
        "source": "National Taiwan University Commencement 2023 (YouTube TOXp-Yk_Gsk)",
        "url": "https://www.youtube.com/watch?v=TOXp-Yk_Gsk",
        "section": "00:11:46-00:12:04",
        "mp4_file": "EP02_VID_ARCH_08_ACT2_24FPS_Huang_Sega_Lifeline_NTU2023.mp4",
        "file": "EP02_VID_ARCH_08_ACT2_24FPS_Huang_Sega_Lifeline_NTU2023.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_08_ACT2_24FPS_Huang_Sega_Lifeline_NTU2023.mp4",
        "specs": "1920×1080 • 24 fps • 18.0s • H.264 • Тайбей, NTU 2023",
        "davinci_usage": "Акт 2 кульмінація: чесність на межі банкрутства перед Сьоїтіро Ірімадзірі.",
        "note": "Виступ в університеті Тайваню про фатальну несумісність NV2 з Direct3D та рятівний контракт Sega.",
        "verified_speaker": "Jensen Huang (NTU 2023)",
    },
    {
        "code": "ARCH #09",
        "act": "Акт 3 (CUDA 2006)",
        "timecode": "11:18–13:45",
        "tc": "11:18–13:45",
        "title": "«Ми винайшли CUDA та додали її у кожен чип» — про ринок із нулем мільярдів",
        "source": "Stripe Sessions 2024 Conversation (YouTube 8Pfa8kPjUio)",
        "url": "https://www.youtube.com/watch?v=8Pfa8kPjUio",
        "section": "00:28:00-00:28:18",
        "mp4_file": "EP02_VID_ARCH_09_ACT2_24FPS_Huang_Invented_CUDA_Stripe2024.mp4",
        "file": "EP02_VID_ARCH_09_ACT2_24FPS_Huang_Invented_CUDA_Stripe2024.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_09_ACT2_24FPS_Huang_Invented_CUDA_Stripe2024.mp4",
        "specs": "1920×1080 • 24 fps • 18.0s • H.264 • Великий план пояснення архітектури",
        "davinci_usage": "Акт 3: як NVIDIA пожертвувала маржею заради створення універсального ринку CUDA.",
        "note": "Детальне пояснення задуму CUDA за 6 років до AlexNet.",
        "verified_speaker": "Jensen Huang (Stripe 2024)",
    },
    {
        "code": "ARCH #10",
        "act": "Акт 3 (GTC 2016 • DGX-1)",
        "timecode": "15:25–16:15",
        "tc": "15:25–16:15",
        "title": "Офіційна прем'єра першого ШІ-суперкомп'ютера NVIDIA DGX-1 на GTC 2016",
        "source": "NVIDIA Official GTC 2016 Keynote Part 7 (YouTube 1ayGJDO6PKU)",
        "url": "https://www.youtube.com/watch?v=1ayGJDO6PKU",
        "section": "00:01:26-00:01:44",
        "mp4_file": "EP02_VID_ARCH_10_ACT3_24FPS_Huang_GTC2016_DGX1_Reveal.mp4",
        "file": "EP02_VID_ARCH_10_ACT3_24FPS_Huang_GTC2016_DGX1_Reveal.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_10_ACT3_24FPS_Huang_GTC2016_DGX1_Reveal.mp4",
        "specs": "1280×720 • 24 fps • 18.0s • H.264 • Золото-чорний рендер DGX-1 на сцені GTC 2016",
        "davinci_usage": "Акт 3: візуал легендарної коробки DGX-1 перед розповіддю про доставку в OpenAI.",
        "note": "Офіційний анонс 2-петафлопсного суперкомп'ютера DGX-1 («World's First Deep Learning Supercomputer»).",
        "verified_speaker": "NVIDIA GTC 2016 Keynote",
    },
    {
        "code": "ARCH #11",
        "act": "Акт 4 (Stanford SIEPR 2024)",
        "timecode": "17:45–18:20",
        "tc": "17:45–18:20",
        "title": "Культова промова у Стенфорді: «Я бажаю вам великих порцій болю та страждань»",
        "source": "Stanford SIEPR Economic Summit (March 2024, YouTube cEg8cOx7UZk)",
        "url": "https://www.youtube.com/watch?v=cEg8cOx7UZk",
        "section": "00:37:58-00:38:22",
        "mp4_file": "EP02_VID_ARCH_11_ACT4_24FPS_Huang_Stanford_Pain_And_Suffering.mp4",
        "file": "EP02_VID_ARCH_11_ACT4_24FPS_Huang_Stanford_Pain_And_Suffering.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_11_ACT4_24FPS_Huang_Stanford_Pain_And_Suffering.mp4",
        "specs": "1920×1080 • 24 fps • 24.0s • H.264 • Чистий кіноплан SIEPR",
        "davinci_usage": "Акт 4 Правило #1: повна емоційна цитата Хуанга про характер і страждання.",
        "note": "Справжній запис легендарної фрази: «Greatness comes from character... I wish upon you ample doses of pain and suffering».",
        "verified_speaker": "Jensen Huang (Stanford SIEPR 2024)",
    },
    {
        "code": "ARCH #12",
        "act": "Акт 4 (Фінал • NTU 2023)",
        "timecode": "20:05–21:00",
        "tc": "20:05–21:00",
        "title": "Фінальний заклик Дженсена Хуанга у Тайбеї: «Біжіть, не йдіть! (Run, don't walk)»",
        "source": "National Taiwan University Commencement 2023 (YouTube TOXp-Yk_Gsk)",
        "url": "https://www.youtube.com/watch?v=TOXp-Yk_Gsk",
        "section": "00:21:08-00:21:24",
        "mp4_file": "EP02_VID_ARCH_12_ACT4_24FPS_Huang_NTU2023_Run_Dont_Walk.mp4",
        "file": "EP02_VID_ARCH_12_ACT4_24FPS_Huang_NTU2023_Run_Dont_Walk.mp4",
        "web_preview": "assets/video_previews/archives/EP02_VID_ARCH_12_ACT4_24FPS_Huang_NTU2023_Run_Dont_Walk.mp4",
        "specs": "1920×1080 • 24 fps • 16.0s • H.264 • Повний зал випускників",
        "davinci_usage": "Фінальна кульмінація всього епізоду перед заключними титрами.",
        "note": "Знамените фінальне послання: «Whatever it is, run after it like we did. Run, don't walk».",
        "verified_speaker": "Jensen Huang (NTU 2023)",
    },
]

ARCHIVAL_PHOTOS_EP02 = [
    ("EP02_IMG_ARCH_01", "PHOTO #01", "Тайвань 1970-х (Тамсуй): епоха дитинства перед еміграцією у 9 років",
     "Wikimedia Commons (CC BY-SA 3.0)", "https://commons.wikimedia.org/wiki/File:Tamsui_in_1970.jpg",
     "EP02_IMG_ARCH_01_Taiwan_Tamsui_1970_Childhood_Era.jpg",
     "Чорно-білий документальний знімок узбережжя Тайваню близько 1970 року — візуальний контекст дитинства Дженсена Хуанга до перельоту в США."),
    ("EP02_IMG_ARCH_02", "PHOTO #02", "Oneida Baptist Institute (Кентуккі): територія трудового інтернату",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Calf_igloos_at_OBI,_Kentucky,_USA.jpg",
     "EP02_IMG_ARCH_02_Oneida_Kentucky_Dorm_Farm_Campus.jpg",
     "Кампус-ферма інституту Oneida Baptist у глушині штату Кентуккі, де дев'ятирічний Дженсен мив туалети та вчився виживати серед важких підлітків."),
    ("EP02_IMG_ARCH_03", "PHOTO #03", "Школа Aloha High School в Орегоні (Випуск 1981)",
     "Wikimedia Commons (Public domain)", "https://commons.wikimedia.org/wiki/File:Aloha_High_School.JPG",
     "EP02_IMG_ARCH_03_Aloha_High_School_Oregon_1981.jpg",
     "Американська школа Aloha High School у передмісті Портленда, яку Хуанг закінчив у 1981 році, паралельно працюючи мийником посуду та виграючи національні турніри з настільного тенісу."),
    ("EP02_IMG_ARCH_04", "PHOTO #04", "Кампус Oregon State University (Корвалліс, Орегон)",
     "Wikimedia Commons (No restrictions)", "https://commons.wikimedia.org/wiki/File:Aerial_view_of_Oregon_State_University_campus_(6443595921).jpg",
     "EP02_IMG_ARCH_04_Oregon_State_University_Campus_1984.jpg",
     "Історичний аерофотознімок університету штату Орегон, де Дженсен вивчав електротехніку (випуск 1984) і зустрів свою майбутню дружину Лорі Міллс."),
    ("EP02_IMG_ARCH_05", "PHOTO #05", "Реальний Denny's на 2484 Berryessa Rd у Сан-Хосе — колиска NVIDIA (1993)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:2484_Berryessa_Road.jpg",
     "EP02_IMG_ARCH_05_Dennys_2484_Berryessa_San_Jose_1993.jpg",
     "Саме ця забігайлівка Denny's у Східному Сан-Хосе, де 1993 року Дженсен Хуанг, Кріс Малаховскі та Кертіс Прім у кутовій кабінці придумали NVIDIA."),
    ("EP02_IMG_ARCH_06", "PHOTO #06", "Кристал першого чипа NVIDIA NV1 (1995, 500nm)",
     "Wikimedia Commons (CC0)", "https://commons.wikimedia.org/wiki/File:NVIDIA@500nm@Fixed-pipeline@NV1@STG2000X_B_A22CI9601_MALTA_DSCx15_polysilicon@5x.jpg",
     "EP02_IMG_ARCH_06_NVIDIA_NV1_500nm_Silicon_Die_1995.jpg",
     "Реальна мікрофотографія полікремнію першого чипа NVIDIA NV1 із квадратичним текстуруванням, який ледь не довів компанію до банкрутства."),
    ("EP02_IMG_ARCH_07", "PHOTO #07", "Рятівний графічний процесор NVIDIA RIVA 128 (NV3, 1997)",
     "Wikimedia Commons (Public domain)", "https://commons.wikimedia.org/wiki/File:RIVA_128_NV_GPU.jpg",
     "EP02_IMG_ARCH_07_NVIDIA_RIVA_128_Chip_1997.jpg",
     "Чип RIVA 128 — єдиний постріл за $5 млн від Sega, спроєктований у симуляторі IKOS, що заробив із першої секунди та розійшовся тиражем у 1 млн штук."),
    ("EP02_IMG_ARCH_08", "PHOTO #08", "Моріс Чанг — засновник TSMC і стратегічний союзник Хуанга",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Morris_Chang_2021APEC.jpg",
     "EP02_IMG_ARCH_08_Morris_Chang_TSMC_Founder.jpg",
     "Легендарний засновник тайванської ливарні TSMC Моріс Чанг, який повірив молодому Дженсену Хуангу у 1990-х і забезпечив виробництво всіх чипів NVIDIA."),
    ("EP02_IMG_ARCH_09", "PHOTO #09", "NVIDIA GeForce 256 (NV10, 1999) — перший у світі GPU",
     "Wikimedia Commons (Public domain)", "https://commons.wikimedia.org/wiki/File:VisionTek_GeForce_256.jpg",
     "EP02_IMG_ARCH_09_NVIDIA_GeForce_256_Worlds_First_GPU_1999.jpg",
     "Плата VisionTek на базі GeForce 256 — відеокарта 1999 року, для якої NVIDIA винайшла сам термін Graphics Processing Unit (GPU)."),
    ("EP02_IMG_ARCH_10", "PHOTO #10", "Відеокарта EVGA GeForce GTX 580 — залізо прориву AlexNet (2012)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:EVGAGeforceGTX580.jpg",
     "EP02_IMG_ARCH_10B_EVGA_GeForce_GTX_580_Card_2012.jpg",
     "Дві саме такі споживчі відеокарти GeForce GTX 580 (3 ГБ) дозволили Крижевському, Суцкеверу та Хінтону перемогти в ImageNet 2012 і запалити бум глибокого навчання."),
    ("EP02_IMG_ARCH_11", "PHOTO #11", "Іризуючий кристал Fermi GF110 (GeForce GTX 580 • 40nm)",
     "Wikimedia Commons (CC0)", "https://commons.wikimedia.org/wiki/File:NVIDIA@40nm@Fermi@GF110@GeForce_GTX_580@UA10B338_1041A1_N2Y540.000_GF110-375-A1_DSC06913_(28114553671).jpg",
     "EP02_IMG_ARCH_10_EVGA_GeForce_GTX_580_AlexNet_2012.jpg",
     "Макрозйомка кремнієвого кристала Fermi GF110 — серця GTX 580, у яке Хуанг вшив блоки CUDA попри падіння акцій."),
    ("EP02_IMG_ARCH_12", "PHOTO #12", "Інженерний центр Джен-Сун Хуанга у Стенфордському університеті",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Jen-Hsun_Huang_Engineering_Center_in_2016.jpg",
     "EP02_IMG_ARCH_11_JenHsun_Huang_Engineering_Center_Stanford.jpg",
     "Будівля школи інженерії Стенфорда імені Джен-Сун Хуанга (магістра 1992 року), де він читав свої культові лекції студентам."),
    ("EP02_IMG_ARCH_13", "PHOTO #13", "Ранній портрет Дженсена Хуанга епохи становлення CUDA",
     "Wikimedia Commons (CC BY-SA 2.0)", "https://commons.wikimedia.org/wiki/File:Jen-Hsun_Huang_Headshot_(15313247387).jpg",
     "EP02_IMG_ARCH_12_Huang_Early_Leather_Jacket_2014_Portrait.jpg",
     "Ранній студійний портрет Дженсена Хуанга у темно-синьому поло без шкіряної куртки (архів 2014)."),
    ("EP02_IMG_ARCH_14", "PHOTO #14", "Дженсен Хуанг на сцені GTC поруч із слайдом 1995 року",
     "Wikimedia Commons (CC BY 2.0)", "https://commons.wikimedia.org/wiki/File:Jensen_Huang_at_GTC_Japan_20161005.jpg",
     "EP02_IMG_ARCH_13_Jensen_Huang_GTC_Keynote_2016.jpg",
     "Презентація 2016 року: Хуанг у шкіряній куртці розповідає історію NVIDIA від заснування 1993–1995 років до революції ШІ."),
    ("EP02_IMG_ARCH_15", "PHOTO #15", "Компактний суперкомп'ютер NVIDIA DGX Spark (золотисте шасі)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Nvidia_DGX_front_view_dllu.jpg",
     "EP02_IMG_ARCH_14_NVIDIA_DGX_Supercomputer_Front.jpg",
     "Сучасний нащадок лінійки DGX-1 — настільний AI-суперкомп'ютер у характерному матово-золотому індустріальному корпусі."),
    ("EP02_IMG_ARCH_16", "PHOTO #16", "Серверний блок NVIDIA DGX B200 / HGX (8× Blackwell GPU)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Nvidia_DGX-B200-HGX.jpg",
     "EP02_IMG_ARCH_15_NVIDIA_DGX_B200_HGX_System.jpg",
     "Відкрита обчислювальна платформа DGX B200 / HGX — фізичний двигун сучасних трильйонних фабрик штучного інтелекту."),
    ("EP02_IMG_ARCH_17", "PHOTO #17", "Штаб-квартира NVIDIA Endeavor у Санта-Кларі (зовнішня панорама)",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:NVIDIA_Headquarters.jpg",
     "EP02_IMG_ARCH_16_NVIDIA_Endeavor_HQ_Santa_Clara.jpg",
     "Футуристичний трикутний кампус NVIDIA Endeavor у Силіконовій долині — за кілька хвилин їзди від забігайлівки Denny's."),
    ("EP02_IMG_ARCH_18", "PHOTO #18", "Алея входу до NVIDIA Endeavor на урочистому відкритті",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Nvdia_Endeavor_Grand_Opening_entry.jpg",
     "EP02_IMG_ARCH_16B_NVIDIA_Endeavor_Grand_Opening_Lobby.jpg",
     "Архітектура без закритих кабінетів — Дженсен Хуанг працює у спільних залах поруч із 55 прямими керівниками."),
    ("EP02_IMG_ARCH_19", "PHOTO #19", "Дженсен Хуанг серед студентів Стенфорда після виступу",
     "Wikimedia Commons (CC BY-SA 4.0)", "https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_024.jpg",
     "EP02_IMG_ARCH_17_Jensen_Huang_Stanford_Keynote_Portrait.jpg",
     "Живий кадр спілкування Хуанга з молодими інженерами Стенфорда — фінальний людяний штрих після лекції."),
]


def verify_paths():
    missing = []
    for d in DOSSIERS_EP02:
        for k in ["raw_4k_png"]:
            if not (ROOT / d[k]).exists(): missing.append(d[k])
        for k in ["web_preview", "video_preview"]:
            if not (ROOT / "07_DASHBOARD" / d[k]).exists(): missing.append("07_DASHBOARD/" + d[k])
    for a in ARCHIVES_EP02:
        if not (ROOT / "05_RAW_FOOTAGE" / "archives" / a["mp4_file"]).exists(): missing.append("05_RAW_FOOTAGE/archives/" + a["mp4_file"])
        if not (ROOT / "07_DASHBOARD" / a["web_preview"]).exists(): missing.append("07_DASHBOARD/" + a["web_preview"])
    for item in ARCHIVAL_PHOTOS_EP02:
        fn = item[5]
        if not (ROOT / "05_RAW_FOOTAGE" / "speaker_portraits" / "young_huang" / fn).exists():
            missing.append("young_huang/" + fn)
        if not (ROOT / "07_DASHBOARD" / "assets" / "archival_photos" / fn).exists():
            missing.append("archival_photos/" + fn)
    if missing:
        raise RuntimeError("Missing verified files:\n  " + "\n  ".join(missing))


def main():
    verify_paths()
    raw = MP_PATH.read_text(encoding="utf-8")
    prefix = "window.MEDIA_ACQUISITION_POOL = "
    mp = json.loads(raw[len(prefix):].rstrip(";\n "))

    ep02 = mp["02"]
    ep02["dossiers"] = DOSSIERS_EP02
    ep02["archives"] = ARCHIVES_EP02
    ep02["archival_photos"] = [
        {
            "id": pid,
            "code": code,
            "title": title,
            "source": src,
            "url": url,
            "raw_file": f"05_RAW_FOOTAGE/speaker_portraits/young_huang/{fn}",
            "web_preview": f"assets/archival_photos/{fn}",
            "desc": desc,
        }
        for (pid, code, title, src, url, fn, desc) in ARCHIVAL_PHOTOS_EP02
    ]

    out_js = prefix + json.dumps(mp, ensure_ascii=False, indent=2) + ";\n"
    MP_PATH.write_text(out_js, encoding="utf-8")

    # Write EP02_MEDIA_CATALOG.json & .md mirroring EP01
    ua_cards = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "dossiers_press" / "ukrainian_quote_cards").glob("EP02_*.png"))
    still_clips = sorted(p.name for p in (ROOT / "05_RAW_FOOTAGE" / "rendered_cinematic_stills_4k").glob("EP02_*.mp4"))
    cat_json = {
        "episode": "EP02 — Jensen Huang",
        "updated_at": "2026-11-10",
        "summary": {
            "archival_broll_mp4": len(ARCHIVES_EP02),
            "archival_photos": len(ARCHIVAL_PHOTOS_EP02),
            "uhd_4k_dossiers": len(DOSSIERS_EP02),
            "ukrainian_4k_quote_cards": len(ua_cards),
            "ken_burns_and_card_4k_mp4": len(still_clips),
        },
        "dossiers": DOSSIERS_EP02,
        "archives": ARCHIVES_EP02,
        "archival_photos": ep02["archival_photos"],
        "ukrainian_4k_quote_cards": ua_cards,
        "rendered_cinematic_stills_4k": still_clips,
    }
    (ROOT / "05_RAW_FOOTAGE" / "EP02_MEDIA_CATALOG.json").write_text(json.dumps(cat_json, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# 🎬 МАЙСТЕР-КАТАЛОГ МЕДІАКОНТЕНТУ EP02 (Дженсен Хуанг)",
        "",
        f"- **📼 Реальні архівні відеокліпи B-Roll (`05_RAW_FOOTAGE/archives/`):** {len(ARCHIVES_EP02)}",
        f"- **📸 Історичні фото та апаратні артефакти (`05_RAW_FOOTAGE/speaker_portraits/young_huang/`):** {len(ARCHIVAL_PHOTOS_EP02)}",
        f"- **🗂️ 4K Документальні досьє-пластини (`05_RAW_FOOTAGE/dossiers_press/`):** {len(DOSSIERS_EP02)}",
        f"- **🇺🇦 4K Українські цитат-картки (`ukrainian_quote_cards/`):** {len(ua_cards)}",
        f"- **🎞️ Ken Burns 4K відеокліпи зі стілів і карток (`rendered_cinematic_stills_4k/`):** {len(still_clips)}",
        "",
        "## 📼 Архівні відеокліпи (`EP02_VID_ARCH_01..12`)",
        "",
        "| Код | Таймкод EP02 | Файл | Джерело |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for a in ARCHIVES_EP02:
        md.append(f"| **{a['code']}** | `{a['timecode']}` | `{a['mp4_file']}` | {a['source']} |")
    md += ["", "## 📸 Хронологічні архівні фото (`EP02_IMG_ARCH_*`)", "", "| Код | Файл | Ліцензія / Джерело |", "| :--- | :--- | :--- |"]
    for p in ep02["archival_photos"]:
        md.append(f"| **{p['code']}** | `{p['raw_file'].split('/')[-1]}` | [{p['source']}]({p['url']}) |")
    (ROOT / "05_RAW_FOOTAGE" / "EP02_MEDIA_CATALOG.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"[✓] EP02 synced: {len(DOSSIERS_EP02)} dossiers, {len(ARCHIVES_EP02)} archival videos, {len(ARCHIVAL_PHOTOS_EP02)} archival photos, {len(ua_cards)} UA cards, {len(still_clips)} 4K motion clips!")


if __name__ == "__main__":
    main()
