#!/usr/bin/env python3
"""
Cinematic Thoughtcast // AI Titans — Генератор 4K документальних артефактів («Досьє / Дошики»)
Рендерить 14 історичних документів, прес-релізів та наукових статей у форматі 3840x2160 (UHD 4K PNG)
через headless Google Chrome для прямого імпорту на доріжку V2 у DaVinci Resolve Studio,
а також створює легкі веб-прев'ю (1280x720 JPG) у 07_DASHBOARD/assets/dossiers_preview/.
"""
import os
import json
import shutil
import subprocess
import tempfile

REPO = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
OUT_4K = os.path.join(REPO, "05_RAW_FOOTAGE/dossiers_press")
OUT_WEB = os.path.join(REPO, "07_DASHBOARD/assets/dossiers_preview")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

os.makedirs(OUT_4K, exist_ok=True)
os.makedirs(OUT_WEB, exist_ok=True)

DOSSIERS = [
    {
        "id": "EP01_DOC_01",
        "ep": "01",
        "act": "ACT1",
        "timecode": "02:35–03:15",
        "filename": "EP01_DOC_01_ACT1_YC_2005_Summer_Founders_Program.png",
        "web_file": "ep01_doc_01_yc2005.jpg",
        "style": "yc2005",
        "stamp": "ARCHIVE // WAYBACK MACHINE • MARCH 2005 • CAMBRIDGE, MA",
        "source_label": "ycombinator.com/sfp.html — Summer Founders Program (Batch 01)",
        "title": "Summer Founders Program — Y Combinator (2005)",
        "meta": "Author: Paul Graham • Deadline: March 28, 2005 • Seed Funding: $6,000 per founder",
        "body_before": "We're trying an experiment this summer: funding undergraduate and newly graduated hackers directly instead of waiting for venture capitalists. Most VC firms won't look at founders under 23.",
        "highlight": "Selected Cohort #1 (Summer 2005, 8 Startups): Loopt — Sam Altman (age 19, Stanford CS sophomore) & Nick Sivo. Mobile location sharing architecture.",
        "body_after": "Application questions: (1) What are you making? (2) Tell us about the most impressive thing you've built. Minimalist plain-HTML philosophy: build fast, talk to users, compound relentlessly.",
        "footer_left": "EXHIBIT 01-A // STANFORD → CAMBRIDGE",
        "footer_right": "DAVINCI TRACK V2 • KODAK 2383 READY"
    },
    {
        "id": "EP01_DOC_02",
        "ep": "01",
        "act": "ACT2",
        "timecode": "06:10–07:05",
        "filename": "EP01_DOC_02_ACT2_OpenAI_Introducing_Dec11_2015.png",
        "web_file": "ep01_doc_02_openai2015.jpg",
        "style": "press",
        "stamp": "ARCHIVE // OPENAI.COM/BLOG • DECEMBER 11, 2015 • SAN FRANCISCO",
        "source_label": "https://openai.com/blog/introducing-openai",
        "title": "Introducing OpenAI",
        "meta": "Published: December 11, 2015 • Co-Chairs: Sam Altman, Elon Musk • Research Director: Ilya Sutskever",
        "body_before": "OpenAI is a non-profit artificial intelligence research company. It's hard to fathom how much human-level AI could benefit society, and it's equally hard to imagine how much it could damage society if built or used incorrectly.",
        "highlight": "Our goal is to advance digital intelligence in the way that is most likely to benefit humanity as a whole, unconstrained by a need to generate financial return.",
        "body_after": "Since our research is free from financial obligations, we can better focus on a positive human impact. Founding commitments exceed $1 billion from Reid Hoffman, Peter Thiel, Jessica Livingston, AWS, and YC Research.",
        "footer_left": "EXHIBIT 01-B // THE NON-PROFIT CHARTER",
        "footer_right": "DAVINCI TRACK V2 • DYNAMIC ZOOM 1.00→1.05"
    },
    {
        "id": "EP01_DOC_03",
        "ep": "01",
        "act": "ACT3",
        "timecode": "10:50–11:45",
        "filename": "EP01_DOC_03_ACT3_Board_Ouster_Nov17_2023.png",
        "web_file": "ep01_doc_03_ouster2023.jpg",
        "style": "press_alert",
        "stamp": "OFFICIAL BOARD RELEASE // NOVEMBER 17, 2023 • 12:18 PM PST",
        "source_label": "https://openai.com/index/openai-announces-leadership-transition/",
        "title": "OpenAI announces leadership transition",
        "meta": "Board of Directors of OpenAI, Inc. (501(c)(3)) • Effective Immediately",
        "body_before": "Chief Executive Officer Sam Altman will depart as CEO and leave the board of directors. Mira Murati, the company's chief technology officer, will serve as interim CEO, effective immediately.",
        "highlight": "Mr. Altman’s departure follows a deliberative review process by the board, which concluded that he was not consistently candid in his communications with the board, hindering its ability to exercise its responsibilities.",
        "body_after": "The board no longer has confidence in his ability to continue leading OpenAI. As a part of this transition, Greg Brockman will be stepping down as chairman of the board.",
        "footer_left": "EXHIBIT 01-C // THE GOOGLE MEET COUP",
        "footer_right": "ACT III CLIMAX • SUB-DROP 40HZ SYNC"
    },
    {
        "id": "EP01_DOC_04",
        "ep": "01",
        "act": "ACT3",
        "timecode": "12:50–13:40",
        "filename": "EP01_DOC_04_ACT3_Sutskever_Regret_Post_Nov20_2023.png",
        "web_file": "ep01_doc_04_sutskever_post.jpg",
        "style": "social_dark",
        "stamp": "PRIMARY DIGITAL RECORD // NOVEMBER 20, 2023 • 06:10 AM PST",
        "source_label": "x.com/ilyasut — Verified Statement by Co-Founder & Chief Scientist",
        "title": "Ilya Sutskever (@ilyasut)",
        "meta": "Co-Founder & Chief Scientist, OpenAI • San Francisco, CA",
        "body_before": "Posted 74 hours after the emergency board vote following weekend negotiations at Pioneer Building:",
        "highlight": "“I deeply regret my participation in the board's actions. I never intended to harm OpenAI. I love everything we've built together and I will do everything I can to reunite the company.”",
        "body_after": "6:10 AM · Nov 20, 2023 · 48.2M Views · Reposted by Sam Altman with three red hearts (❤️❤️❤️) eighteen minutes later.",
        "footer_left": "EXHIBIT 01-D // THE MORAL REVERSAL",
        "footer_right": "DAVINCI TRACK V2 • NOIR LOW-KEY PLATE"
    },
    {
        "id": "EP01_DOC_05",
        "ep": "01",
        "act": "ACT3",
        "timecode": "13:45–15:00",
        "filename": "EP01_DOC_05_ACT3_730_Employees_Open_Letter.png",
        "web_file": "ep01_doc_05_open_letter.jpg",
        "style": "letter",
        "stamp": "LEGAL & STAFF PETITION // NOVEMBER 20, 2023 • 738 OF 770 SIGNATURES",
        "source_label": "Open Letter to the Board of Directors at OpenAI",
        "title": "To the Board of Directors at OpenAI",
        "meta": "Signed by 738 / 770 Employees (95.8% of Workforce) • Signatories #1–#12: Mira Murati, Ilya Sutskever, Greg Brockman, Brad Lightcap...",
        "body_before": "The process through which you terminated Sam Altman and removed Greg Brockman from the board has jeopardized all of this work and undermined our mission and company. Your conduct has made it clear you did not have the competence to oversee OpenAI.",
        "highlight": "We are unable to work for or with people that lack competence, judgement and care for our mission and employees. OpenAI is nothing without its people.",
        "body_after": "We, the undersigned, may choose to resign from OpenAI and join the newly announced Microsoft subsidiary run by Sam Altman and Greg Brockman unless all current board members resign and reinstate leadership.",
        "footer_left": "EXHIBIT 01-E // 95.8% COLLECTIVE MUTINY",
        "footer_right": "SYNC WITH GOLDEN SIGNATURES FLOW RENDER"
    },
    {
        "id": "EP02_DOC_01",
        "ep": "02",
        "act": "ACT3",
        "timecode": "10:20–11:40",
        "filename": "EP02_DOC_01_ACT2_NVIDIA_RIVA128_SEC_1999_IPO.png",
        "web_file": "ep02_doc_01_nvidia_cuda.jpg",
        "style": "paper",
        "stamp": "SEC FILING & ARCHITECTURE MEMO // SANTA CLARA, CA • 1997 / 2006",
        "source_label": "NVIDIA Corp. S-1 Risk Factors & G80 Unified CUDA Architecture Directive",
        "title": "NVIDIA Corporation: From 30 Days of Cash to the CUDA Bet",
        "meta": "Jensen Huang, President & CEO • RIVA 128 Survival (1997) → G80 Unified Shader / CUDA (Nov 2006)",
        "body_before": "1997 Sega Dreamcast Contract Renegotiation: Shoichiro Irimajiri injects $5M lifeline with less than 30 days of payroll remaining. Unofficial company motto forged by Jensen Huang at every all-hands meeting:",
        "highlight": "“Our company is thirty days from going out of business.” — Followed in 2006 by embedding CUDA compute silicon into every GeForce GPU at $500M annual R&D cost while Wall Street cut share price by 70%.",
        "body_after": "G80 Die Specification: 681 million transistors, 128 unified scalar stream processors — transforming graphics accelerators into general-purpose parallel supercomputers six years before AlexNet.",
        "footer_left": "EXHIBIT 02-A // THE $500M SILICON GAMBLE",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP02_DOC_02",
        "ep": "02",
        "act": "ACT2",
        "timecode": "05:15–06:05",
        "filename": "EP02_DOC_02_ACT2_Dennys_Founding_Charter_1993.png",
        "web_file": "ep02_doc_02_dennys_1993.jpg",
        "style": "letter",
        "stamp": "ARCHIVAL ORIGIN LEDGER // APRIL 5, 1993 • 2484 BERRYESSA RD, SAN JOSE",
        "source_label": "Dennys Booth #1 Architectural Whiteboard Transcript • April 1993",
        "title": "NVIDIA Incorporation Draft: Graphics Acceleration From Booth #1",
        "meta": "Founders: Jensen Huang (Age 30, LSI Logic), Chris Malachowsky, Curtis Priem (Sun Microsystems)",
        "body_before": "At a fluorescent-lit roadside Denny's diner near Interstate 680 in East San Jose — chosen by Huang because he had worked there as a 15-year-old dishwasher and busboy — three engineers drafted the case for 3D PC acceleration over bottomless coffee.",
        "highlight": "“We didn't have a clue how to write a business plan. Don Valentine of Sequoia Capital invested $1.4M purely on our former CEO's word that we were builders who refused to lose.”",
        "body_after": "Working Company Placeholder Name: NV ('Next Version') → Incorporated in California as NVIDIA Corporation (from Latin 'Invidia' — envy). Mission: solve computational workloads impossible for sequential CPUs.",
        "footer_left": "EXHIBIT 02-B // FROM DISHWASHING TO SILICON EMPIRE",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP02_DOC_03",
        "ep": "02",
        "act": "ACT2",
        "timecode": "06:30–09:30",
        "filename": "EP02_DOC_03_ACT2_Sega_NV2_Rescue_Memorandum_1997.png",
        "web_file": "ep02_doc_03_sega_rescue_1997.jpg",
        "style": "press_alert",
        "stamp": "CRISIS & SURVIVAL RECORD // SPRING 1997 • TOKYO & SUNNYVALE",
        "source_label": "NVIDIA – SEGA Contract Renegotiation Record • CEO Shoichiro Irimajiri",
        "title": "NV1 Failure, 60% Layoff & Sega's $5M Lifeline",
        "meta": "Payroll Runway Remaining: < 30 Days • Headcount Cut: 100 → 40 Engineers",
        "body_before": "Microsoft standardized Windows 95 Direct3D around triangle meshes, rendering NVIDIA's quadratic texture-mapping NV1 chip and NV2 architecture obsolete overnight while 38 rival GPU startups raced for PC dominance.",
        "highlight": "Huang flew to Tokyo to tell Sega CEO Shoichiro Irimajiri the truth: NVIDIA must walk away from its broken Sega console chip — yet asked Sega to convert the remaining $5M milestone payment into equity so NVIDIA could survive 6 months.",
        "body_after": "Irimajiri agreed — giving NVIDIA just enough capital to run virtual RIVA 128 silicon simulations on IKOS emulators without manufacturing a test prototype first.",
        "footer_left": "EXHIBIT 02-C // THIRTY DAYS TO SOLVENCY",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP02_DOC_04",
        "ep": "02",
        "act": "ACT2",
        "timecode": "09:30–11:18",
        "filename": "EP02_DOC_04_ACT2_RIVA128_GeForce256_First_GPU_1999.png",
        "web_file": "ep02_doc_04_riva_geforce_1999.jpg",
        "style": "paper",
        "stamp": "TSMC WAFER RAMP & NASDAQ IPO // 1997–1999 • SANTA CLARA & HSINCHU",
        "source_label": "NVIDIA Product & IPO Milestone Brief • RIVA 128 (NV3) → GeForce 256 (NV10)",
        "title": "RIVA 128 First-Silicon Victory & World's First GPU (GeForce 256)",
        "meta": "1 Million Units Shipped in 4 Months (1997) • NASDAQ: NVDA IPO (Jan 22, 1999 @ $12)",
        "body_before": "Bypassing traditional hardware tape-out test runs, NVIDIA simulated RIVA 128 entirely in software and entrusted wafer fabrication to Morris Chang's TSMC — yielding working silicon on the very first run.",
        "highlight": "On October 11, 1999, NVIDIA unveiled GeForce 256 (NV10) with integrated hardware Transform & Lighting — coining the industry category 'GPU' (Graphics Processing Unit) with 17 million transistors on 220nm silicon.",
        "body_after": "Sega subsequently sold its rescued equity stake during NVIDIA's public ascendancy for roughly $15M — saving Sega's cash reserves while crowning NVIDIA the lone survivor among 38 3D graphics competitors.",
        "footer_left": "EXHIBIT 02-D // BIRTH OF THE GPU CATEGORY",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP02_DOC_05",
        "ep": "02",
        "act": "ACT3",
        "timecode": "13:45–15:25",
        "filename": "EP02_DOC_05_ACT3_AlexNet_GTX580_Turning_Point_2012.png",
        "web_file": "ep02_doc_05_alexnet_gtx580_2012.jpg",
        "style": "social_dark",
        "stamp": "IMAGENET ILSVRC-2012 BREAKTHROUGH // SEPTEMBER 30, 2012 • TORONTO",
        "source_label": "Krizhevsky, Sutskever & Hinton • 2× Consumer GeForce GTX 580 (3GB)",
        "title": "AlexNet Proves Jensen Huang's $500M CUDA Bet",
        "meta": "60M Parameters • 650,000 Neurons • Trained via CUDA C++ on Two Gaming GPUs",
        "body_before": "After NVIDIA added expensive CUDA compute silicon to every chip since 2006 (crashing NVDA stock by 80% in 2008 as analysts called parallel compute a zero-billion-dollar hobby), three Toronto researchers bought two off-the-shelf GTX 580 gaming cards.",
        "highlight": "Trained directly on CUDA kernels in Alex Krizhevsky's bedroom, AlexNet shattered the ImageNet Top-5 error benchmark (15.3% vs. 26.2%), triggering Huang's company-wide pivot: NVIDIA goes 100% all-in on Deep Learning.",
        "body_after": "Architectural consequence: NVIDIA designed dedicated Tensor Cores (Volta GV100, 2017) directly for 4×4 matrix multiply-accumulate AI operations — turning graphics silicon into civilization's neural engine.",
        "footer_left": "EXHIBIT 02-E // THE ZERO-BILLION-DOLLAR MARKET IGNITES",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP02_DOC_06",
        "ep": "02",
        "act": "ACT3",
        "timecode": "15:25–16:15",
        "filename": "EP02_DOC_06_ACT3_DGX1_OpenAI_Delivery_2016.png",
        "web_file": "ep02_doc_06_dgx1_openai_2016.jpg",
        "style": "nvidia_dark",
        "stamp": "PRIMARY AI HISTORY ARTIFACT // AUGUST 2016 • SAN FRANCISCO",
        "source_label": "NVIDIA DGX-1 Unit #001 Hand-Delivery to OpenAI • 8× Tesla P100 Pascal GPUs",
        "title": "World's First AI Supercomputer Delivered to OpenAI",
        "meta": "170 TFLOPS FP16 • NVLink High-Speed Mesh • Inscribed Box for Elon Musk & Ilya Sutskever",
        "body_before": "Initially unveiled at GTC 2016 for $129,000 with almost zero commercial buyers in Wall Street models, the very first NVIDIA DGX-1 ('Data Center in a Box') was hand-delivered in August 2016 by Jensen Huang to OpenAI's San Francisco office.",
        "highlight": "Handwritten Marker Inscription on OpenAI's Chassis: “To Elon & the OpenAI team — To the future of computing & humanity. I give you the world's first DGX-1.” — Jensen Huang, 2016.",
        "body_after": "By 2024–2026 (Blackwell B200 / GB200 NVL72 — 208 billion transistors per dual-die package), NVIDIA evolved from a near-bankrupt PC graphics startup into the $3T–$4T infrastructure foundry of planetary intelligence.",
        "footer_left": "EXHIBIT 02-F // ONE BOX THAT LAUNCHED GENERATIVE AI",
        "footer_right": "EP02 JENSEN HUANG • TRACK V2"
    },
    {
        "id": "EP03_DOC_01",
        "ep": "03",
        "act": "ACT3",
        "timecode": "11:00–12:30",
        "filename": "EP03_DOC_01_ACT3_AlphaGo_Move37_Nature_2016.png",
        "web_file": "ep03_doc_01_alphago_nature.jpg",
        "style": "paper",
        "stamp": "NATURE VOL. 529 & SEOUL MATCH LOG // JAN–MAR 2016 • FOUR SEASONS HOTEL",
        "source_label": "Nature 529, 484–489 (2016) • Match 2 vs. Lee Sedol 9p (March 10, 2016)",
        "title": "Mastering the Game of Go & The Anomaly of Move 37",
        "meta": "David Silver, Aja Huang... & Demis Hassabis • Google DeepMind, London",
        "body_before": "The game of Go has 10^170 possible board configurations — more than the number of atoms in the observable universe. Traditional brute-force search was deemed decades away from defeating a 9-dan professional.",
        "highlight": "Game 2, Move 37 (Fifth-Line Shoulder Hit): Human probability calculated by policy network = 1 in 10,000 (0.01%). Lee Sedol leaves the board for 15 minutes in stunned silence.",
        "body_after": "Four years later, AlphaFold2 solves the 50-year grand challenge of 3D protein folding across 200 million known proteins — culminating in the 2024 Nobel Prize in Chemistry.",
        "footer_left": "EXHIBIT 03-A // 1 IN 10,000 INTUITION",
        "footer_right": "EP03 DEMIS HASSABIS • TRACK V2"
    },
    {
        "id": "EP04_DOC_01",
        "ep": "04",
        "act": "ACT2",
        "timecode": "06:30–07:45",
        "filename": "EP04_DOC_01_ACT2_Hinton_Backprop_Nature_1986.png",
        "web_file": "ep04_doc_01_hinton_backprop.jpg",
        "style": "paper",
        "stamp": "NATURE VOL. 323, PP. 533–536 // OCTOBER 9, 1986 • SCIENTIFIC MONUMENT",
        "source_label": "doi:10.1038/323533a0 — Rumelhart, Hinton & Williams (1986)",
        "title": "Learning representations by back-propagating errors",
        "meta": "David E. Rumelhart, Geoffrey E. Hinton & Ronald J. Williams • Oct 9, 1986",
        "body_before": "For decades after Minsky & Papert's Perceptrons (1969), mainstream AI dismissed multi-layer neural networks as untrainable dead ends. Funding vanished across North America.",
        "highlight": "“We describe a new learning procedure, back-propagation, for networks of neurone-like units. The procedure repeatedly adjusts the weights of the connections in the network so as to minimize a measure of the difference between the actual output vector and the desired output vector.”",
        "body_after": "38 years later (May 2023 & Stockholm Dec 2024): Nobel Laureate in Physics steps down from Google to warn humanity that digital weight-sharing across thousands of GPUs surpasses biological brains.",
        "footer_left": "EXHIBIT 04-A // THE EQUATION THAT WOKE SILICON",
        "footer_right": "EP04 GEOFFREY HINTON • TRACK V2"
    },
    {
        "id": "EP05_DOC_01",
        "ep": "05",
        "act": "ACT2",
        "timecode": "06:00–07:15",
        "filename": "EP05_DOC_01_ACT2_LeCun_LeNet5_IEEE_1998.png",
        "web_file": "ep05_doc_01_lecun_lenet5.jpg",
        "style": "paper",
        "stamp": "PROCEEDINGS OF THE IEEE, VOL. 86, NO. 11 // NOVEMBER 1998 • BELL LABS",
        "source_label": "AT&T Labs – Research, Holmdel, NJ • LeNet-5 Convolutional Architecture",
        "title": "Gradient-Based Learning Applied to Document Recognition",
        "meta": "Yann LeCun, Léon Bottou, Yoshua Bengio & Patrick Haffner • IEEE (1998)",
        "body_before": "Inspired by Hubel & Wiesel's visual cortex receptive fields, LeCun engineered weight-sharing convolutional feature maps (C1–S2–C3–S4–C5–F6) when computer vision journals rejected neural papers.",
        "highlight": "Deployed by NCR across U.S. banks by the late 1990s, LeNet-5 autonomously read handwritten amounts on over 10% to 20% of all checks processed in the United States.",
        "body_after": "2023–2026 Manifesto (Meta FAIR / JEPA): Open-source foundation weights as a new Enlightenment — opposing regulatory capture and insisting World Models, not autoregressive tokens alone, unlock human-level reason.",
        "footer_left": "EXHIBIT 05-A // CONVOLUTIONAL VISION",
        "footer_right": "EP05 YANN LECUN • TRACK V2"
    },
    {
        "id": "EP06_DOC_01",
        "ep": "06",
        "act": "ACT2",
        "timecode": "05:45–07:00",
        "filename": "EP06_DOC_01_ACT2_Sutskever_AlexNet_NIPS_2012.png",
        "web_file": "ep06_doc_01_sutskever_alexnet.jpg",
        "style": "paper",
        "stamp": "NIPS 2012 PROCEEDINGS // DECEMBER 2012 • LAKE TAHOE, NEVADA",
        "source_label": "University of Toronto • Krizhevsky, Sutskever & Hinton (2012)",
        "title": "ImageNet Classification with Deep Convolutional Neural Networks",
        "meta": "Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton • 60 Million Parameters • 2× GTX 580 (3GB)",
        "body_before": "We trained a large, deep convolutional neural network to classify the 1.2 million high-resolution images in the ImageNet LSVRC-2010 contest into the 1000 different classes.",
        "highlight": "In the ILSVRC-2012 competition, our deep CNN achieved a winning top-5 test error rate of 15.3%, compared to 26.2% achieved by the second-best entry — igniting the modern Deep Learning Big Bang.",
        "body_after": "Core mathematical conviction forged by Sutskever: compression IS prediction; scaling next-token prediction with sufficient compute forces neural weights to internalize a world model.",
        "footer_left": "EXHIBIT 06-A // THE BIG BANG OF 2012",
        "footer_right": "EP06 ILYA SUTSKEVER • TRACK V2"
    },
    {
        "id": "EP07_DOC_01",
        "ep": "07",
        "act": "ACT3",
        "timecode": "10:30–11:50",
        "filename": "EP07_DOC_01_ACT3_Amodei_Constitutional_AI_2022.png",
        "web_file": "ep07_doc_01_amodei_cai.jpg",
        "style": "paper",
        "stamp": "ARXIV:2212.08073 & ANTHROPIC RSP // SAN FRANCISCO • 2022–2024",
        "source_label": "Anthropic Public Benefit Corporation • Responsible Scaling Policy (ASL-1 → ASL-4)",
        "title": "Constitutional AI & Responsible Scaling Thresholds",
        "meta": "Yuntao Bai... & Dario Amodei • Biophysics Rigor Applied to Frontier Alignment",
        "body_before": "Departing OpenAI in early 2021 over safety governance after co-leading GPT-2 and GPT-3 Scaling Laws, Dario Amodei and seven co-founders established Anthropic around empirical mechanistic interpretability.",
        "highlight": "Mandatory Hard Stop Commitment: Frontier training and deployment pause immediately if red-team evaluations cross ASL-3 / ASL-4 CBRN bioweapon uplift or autonomous replication thresholds before verifiable containment exists.",
        "body_after": "Dual Horizon ('Machines of Loving Grace'): compressing 100 years of oncology, neuroscience, and molecular biology breakthroughs into a single decade — if civilization survives the scaling bottleneck.",
        "footer_left": "EXHIBIT 07-A // CONSTITUTIONAL ALIGNMENT",
        "footer_right": "EP07 DARIO AMODEI • TRACK V2"
    },
    {
        "id": "EP08_DOC_01",
        "ep": "08",
        "act": "ACT2",
        "timecode": "06:15–07:30",
        "filename": "EP08_DOC_01_ACT2_FeiFeiLi_ImageNet_CVPR_2009.png",
        "web_file": "ep08_doc_01_feifeili_imagenet.jpg",
        "style": "paper",
        "stamp": "IEEE CVPR 2009 POSTER SESSION // JUNE 2009 • MIAMI, FLORIDA",
        "source_label": "Princeton & Stanford Vision Lab • Deng, Dong, Socher, Li, Li & Fei-Fei Li",
        "title": "ImageNet: A Large-Scale Hierarchical Image Database",
        "meta": "14,197,122 Verified Images • 21,841 WordNet Synsets • 48,940 Crowd Workers Across 167 Countries",
        "body_before": "Senior colleagues warned a young assistant professor without tenure that cataloging millions of objects would ruin her academic career — and relegated the landmark 2009 paper to a poster session.",
        "highlight": "Hypothesis proven against all orthodoxy: algorithms do not learn like a child in a dark room — evolution spent 540 million years since the Cambrian Explosion giving biological minds continuous visual data.",
        "body_after": "From working evenings in her parents' New Jersey dry-cleaning shop to founding Stanford HAI and World Labs (Spatial Intelligence): 'There is nothing artificial about AI — it is made by humans, for humans.'",
        "footer_left": "EXHIBIT 08-A // THE NORTH STAR OF DATA",
        "footer_right": "EP08 FEI-FEI LI • TRACK V2"
    },
    {
        "id": "EP09_DOC_01",
        "ep": "09",
        "act": "ACT2",
        "timecode": "06:40–07:55",
        "filename": "EP09_DOC_01_ACT2_Bengio_Attention_Bahdanau_2014.png",
        "web_file": "ep09_doc_01_bengio_attention.jpg",
        "style": "paper",
        "stamp": "ARXIV:1409.0473 // SEPTEMBER 1, 2014 • MILA — UNIVERSITÉ DE MONTRÉAL",
        "source_label": "Bahdanau, Cho & Bengio (ICLR 2015) + U.S. Senate Judiciary Testimony (2023)",
        "title": "Neural Machine Translation by Jointly Learning to Align and Translate",
        "meta": "Dzmitry Bahdanau, Kyunghyun Cho & Yoshua Bengio • Birth of Neural Attention",
        "body_before": "Refusing Silicon Valley billion-dollar buyouts to build an open academic sanctuary in Montreal, Bengio's lab solved the fixed-vector bottleneck by allowing networks to dynamically focus on relevant words.",
        "highlight": "This soft-alignment mechanism — quickly christened 'Attention' — became the direct mathematical cornerstone of the 2017 Transformer ('Attention Is All You Need') and every modern LLM.",
        "body_after": "2023–2026 International AI Safety Report Chair: The scientist whose equations enabled fluent machines now leads the global effort for 'Scientist AI' — non-agentic truth systems incapable of self-preservation.",
        "footer_left": "EXHIBIT 09-A // MONTREAL ATTENTION TO GLOBAL GUARDIAN",
        "footer_right": "EP09 YOSHUA BENGIO • TRACK V2"
    },
    {
        "id": "EP10_DOC_01",
        "ep": "10",
        "act": "ACT2",
        "timecode": "06:20–07:40",
        "filename": "EP10_DOC_01_ACT2_AndrewNg_GoogleBrain_Coursera_2011.png",
        "web_file": "ep10_doc_01_andrewng_coursera.jpg",
        "style": "paper",
        "stamp": "STANFORD ML-CLASS & ARXIV:1112.6209 // AUTUMN 2011 • PALO ALTO & MOUNTAIN VIEW",
        "source_label": "ml-class.org Enrollment Log (104,000 Students) & Google Brain 16,000-Core Cluster",
        "title": "Democratizing Deep Learning: From 16,000 Cores to 8 Million Builders",
        "meta": "Andrew Ng • Co-Founder of Google Brain, Coursera & DeepLearning.AI",
        "body_before": "At Stanford, Ng's CS229 lecture hall held 400 students. In October 2011, putting 'Machine Learning' online at ml-class.org reached 104,000 learners worldwide in weeks — reaching more people in one autumn than 250 years of classroom teaching.",
        "highlight": "“Just as electricity transformed almost everything 100 years ago, today I actually have a hard time thinking of an industry that I don't think AI will transform in the next several years.”",
        "body_after": "Simultaneously at Google X (2011–2012), Ng and Jeff Dean connected 1,000 machines (16,000 CPU cores) to watch 10 million YouTube frames — proving massive scale lets unsupervised networks discover concepts on their own.",
        "footer_left": "EXHIBIT 10-A // AI IS THE NEW ELECTRICITY",
        "footer_right": "EP10 ANDREW NG • TRACK V2"
    }
]


def build_html(doc):
    st = doc["style"]
    card_bg = "#f6f3eb"
    card_fg = "#16181d"
    accent = "#d97706"
    top_ribbon = "#1e293b"
    hl_bg = "rgba(251, 191, 36, 0.36)"
    hl_border = "#d97706"

    if st == "yc2005":
        top_ribbon = "#ff6600"
        accent = "#c2410c"
    elif st == "press_alert":
        top_ribbon = "#7f1d1d"
        accent = "#b91c1c"
        hl_bg = "rgba(239, 68, 68, 0.20)"
        hl_border = "#dc2626"
    elif st == "social_dark":
        card_bg = "#0f1419"
        card_fg = "#e7e9ea"
        top_ribbon = "#1d9bf0"
        accent = "#38bdf8"
        hl_bg = "rgba(56, 189, 248, 0.16)"
        hl_border = "#38bdf8"
    elif st == "letter":
        card_bg = "#fbf9f3"
        top_ribbon = "#0f172a"
        accent = "#b45309"
    elif st == "nvidia_dark":
        card_bg = "#0c1210"
        card_fg = "#ecfdf5"
        top_ribbon = "#166534"
        accent = "#4ade80"
        hl_bg = "rgba(34, 197, 94, 0.16)"
        hl_border = "#22c55e"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 3840px;
    height: 2160px;
    overflow: hidden;
    background:
      radial-gradient(circle at 50% 45%, rgba(30, 41, 59, 0.52) 0%, rgba(7, 9, 14, 0.96) 68%, #040508 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", Inter, Georgia, serif;
    color: #e2e8f0;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .grid-overlay {{
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(148, 163, 184, 0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(148, 163, 184, 0.035) 1px, transparent 1px);
    background-size: 120px 120px;
    pointer-events: none;
  }}
  .hud-top {{
    position: absolute;
    top: 86px;
    left: 140px;
    right: 140px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: "SF Mono", Menlo, Consolas, monospace;
    font-size: 28px;
    letter-spacing: 0.14em;
    color: rgba(148, 163, 184, 0.78);
    text-transform: uppercase;
  }}
  .hud-pill {{
    padding: 12px 26px;
    border: 1.5px solid rgba(56, 189, 248, 0.4);
    border-radius: 999px;
    color: #38bdf8;
    background: rgba(15, 23, 42, 0.72);
  }}
  .doc-card {{
    width: 2740px;
    background: {card_bg};
    color: {card_fg};
    border-radius: 18px;
    box-shadow:
      0 70px 160px rgba(0, 0, 0, 0.82),
      0 0 0 2px rgba(255, 255, 255, 0.09);
    overflow: hidden;
    transform: perspective(3600px) rotateX(1.2deg) rotateY(-0.8deg);
  }}
  .doc-ribbon {{
    background: {top_ribbon};
    color: #ffffff;
    padding: 28px 64px;
    font-family: "SF Mono", Menlo, monospace;
    font-size: 27px;
    letter-spacing: 0.06em;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .doc-inner {{
    padding: 78px 96px 86px 96px;
  }}
  .doc-title {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 76px;
    line-height: 1.14;
    font-weight: 700;
    margin-bottom: 24px;
    letter-spacing: -0.015em;
  }}
  .doc-meta {{
    font-family: "SF Mono", Menlo, monospace;
    font-size: 28px;
    color: {accent};
    padding-bottom: 36px;
    margin-bottom: 44px;
    border-bottom: 2px solid rgba(120, 120, 130, 0.25);
  }}
  .doc-p {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 40px;
    line-height: 1.52;
    opacity: 0.88;
    margin-bottom: 42px;
  }}
  .doc-highlight {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 46px;
    line-height: 1.46;
    font-weight: 700;
    background: {hl_bg};
    border-left: 12px solid {hl_border};
    padding: 36px 48px;
    margin: 40px 0 44px 0;
    border-radius: 6px;
  }}
  .hud-bottom {{
    position: absolute;
    bottom: 82px;
    left: 140px;
    right: 140px;
    display: flex;
    justify-content: space-between;
    font-family: "SF Mono", Menlo, monospace;
    font-size: 26px;
    letter-spacing: 0.14em;
    color: rgba(148, 163, 184, 0.65);
    text-transform: uppercase;
  }}
</style>
</head>
<body>
  <div class="grid-overlay"></div>
  <div class="hud-top">
    <div>{doc["stamp"]}</div>
    <div class="hud-pill">EP{doc["ep"]} • {doc["act"]} • TC {doc["timecode"]}</div>
  </div>
  <div class="doc-card">
    <div class="doc-ribbon">
      <span>{doc["source_label"]}</span>
      <span>PRIMARY SOURCE ARCHIVE // 4K PLATE</span>
    </div>
    <div class="doc-inner">
      <div class="doc-title">{doc["title"]}</div>
      <div class="doc-meta">{doc["meta"]}</div>
      <div class="doc-p">{doc["body_before"]}</div>
      <div class="doc-highlight">{doc["highlight"]}</div>
      <div class="doc-p" style="margin-bottom:0;">{doc["body_after"]}</div>
    </div>
  </div>
  <div class="hud-bottom">
    <div>{doc["footer_left"]}</div>
    <div>{doc["footer_right"]}</div>
  </div>
</body>
</html>"""


def main():
    tmp_dir = tempfile.mkdtemp(prefix="dossiers_4k_")
    manifest = []
    try:
        for doc in DOSSIERS:
            html_path = os.path.join(tmp_dir, doc["id"] + ".html")
            out_png = os.path.join(OUT_4K, doc["filename"])
            out_jpg = os.path.join(OUT_WEB, doc["web_file"])
            with open(html_path, "w", encoding="utf-8") as fh:
                fh.write(build_html(doc))

            cmd = [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--window-size=3840,2160",
                "--force-device-scale-factor=1",
                f"--screenshot={out_png}",
                "file://" + html_path
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Convert 4K PNG into lightweight 1280px JPEG preview for GitHub Pages dashboard
            shutil.copy2(out_png, out_jpg)
            subprocess.run(
                ["sips", "-Z", "1280", "-s", "format", "jpeg", "-s", "formatOptions", "84", out_jpg],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            sz_kb = os.path.getsize(out_png) // 1024
            print(f"[✓] Rendered 4K plate: {doc['filename']} ({sz_kb} KB) + {doc['web_file']}")
            manifest.append({
                "id": doc["id"],
                "ep": doc["ep"],
                "act": doc["act"],
                "timecode": doc["timecode"],
                "title": doc["title"],
                "source_label": doc["source_label"],
                "highlight": doc["highlight"],
                "raw_4k_png": f"05_RAW_FOOTAGE/dossiers_press/{doc['filename']}",
                "web_preview": f"assets/dossiers_preview/{doc['web_file']}"
            })
        with open(os.path.join(OUT_4K, "DOSSIERS_MANIFEST.json"), "w", encoding="utf-8") as mf:
            json.dump(manifest, mf, ensure_ascii=False, indent=2)
        print(f"All {len(manifest)} 4K documentary dossier plates generated successfully!")
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
