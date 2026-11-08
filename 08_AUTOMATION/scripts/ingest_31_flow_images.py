#!/usr/bin/env python3
"""Ingest 31 new 2K Google Flow / Veo images from ~/Downloads into EP01, EP03, EP06, EP10."""
import os
import shutil
import json
from PIL import Image

ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
DL_DIR = "/Users/volodymyrkatasonov/Downloads"
RAW_DIR = os.path.join(ROOT, "05_RAW_FOOTAGE")
DASH_DIR = os.path.join(ROOT, "07_DASHBOARD")
PREVIEW_DIR = os.path.join(DASH_DIR, "assets", "flow_keyframes")
os.makedirs(PREVIEW_DIR, exist_ok=True)

# Specification of the 31 assets
ASSETS = [
    # === EP01: Sam Altman (13 items) ===
    {
        "ep": "01",
        "dl_file": "Light_threads_converging_into_core_0a9b575a_2K.jpg",
        "category": "primary",
        "shot_num": "08",
        "target_name": "EP01_FLOW_IMG_08_Golden_Signatures_Light_Threads_2K.jpg",
        "preview_name": "ep01_flow_kf_08_golden_signatures.jpg",
        "title": "Збіжність золотих світлових ниток в ядро енергії",
        "act": "ACT4",
        "timecode": "13:45–15:30",
        "prompt": "Particle physics simulation: thousands of glowing golden light threads converging from darkness into a single blinding core of energy, Octane render, 8k."
    },
    {
        "ep": "01",
        "dl_file": "Plasma_contained_in_fusion_reactor_b2a62691_2K.jpg",
        "category": "primary",
        "shot_num": "09",
        "target_name": "EP01_FLOW_IMG_09_Fusion_Torus_Plasma_2K.jpg",
        "preview_name": "ep01_flow_kf_09_fusion_torus.jpg",
        "title": "Магнітний термоядерний реактор торус (Helion Energy)",
        "act": "ACT4",
        "timecode": "15:30–17:00",
        "prompt": "Cinematic interior view of a magnetic fusion reactor torus, glowing violet and gold plasma contained by magnetic fields, hard sci-fi documentary realism, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Earth_illuminated_by_neural_netw…_c8db3389_2K.jpg",
        "category": "primary",
        "shot_num": "10",
        "target_name": "EP01_FLOW_IMG_10_Earth_Horizon_Neural_Grid_2K.jpg",
        "preview_name": "ep01_flow_kf_10_earth_horizon.jpg",
        "title": "Орбітальний відхід від Землі з сіткою нейромереж",
        "act": "ACT4",
        "timecode": "18:30–20:00",
        "prompt": "Slow majestic orbital camera pull-back from dark Earth night side illuminated by glowing golden neural network grids connecting cities, quiet cosmic awe, IMAX 8k."
    },
    {
        "ep": "01",
        "dl_file": "Smartphone_vibrating_on_table_743c34d9_2K.jpg",
        "category": "broll",
        "shot_num": "07B",
        "target_name": "EP01_FLOW_IMG_07B_Smartphone_Vibrating_Table_2K.jpg",
        "preview_name": "ep01_flow_broll_07b_phone_vibrating.jpg",
        "title": "Смартфон, що вібрує на столі ради директорів (Ніч перевороту)",
        "act": "ACT3",
        "timecode": "11:15–11:45",
        "prompt": "48fps poetic slow-motion insert of smartphone vibrating violently on dark conference table, screen glowing in low-key noir lighting, rain on window glass, 4k."
    },
    {
        "ep": "01",
        "dl_file": "CRT_computer_in_boardroom_3d9ac17f_2K.jpg",
        "category": "broll",
        "shot_num": "02E",
        "target_name": "EP01_FLOW_STUDY_02E_CRT_Computer_Boardroom_2K.jpg",
        "preview_name": "ep01_flow_broll_02e_crt_boardroom.jpg",
        "title": "Вінтажний CRT комп'ютер у темній залі засідань",
        "act": "ACT1/3",
        "timecode": "01:00–02:00",
        "prompt": "Juxtaposition study: glowing 1990s green CRT monitor sitting on polished black boardroom conference table in obsidian void, moody volumetric lighting, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Macintosh_computer_in_boardroom_6a4b9601_2K.jpg",
        "category": "broll",
        "shot_num": "01D",
        "target_name": "EP01_FLOW_STUDY_01D_Mac_Boardroom_StudyA_2K.jpg",
        "preview_name": "ep01_flow_broll_01d_mac_boardroom_a.jpg",
        "title": "Macintosh LC II у конференц-залі ради директорів (Ракурс A)",
        "act": "ACT1",
        "timecode": "00:45–01:15",
        "prompt": "Archival concept study: 1993 beige Apple Macintosh LC II on high-gloss obsidian executive boardroom table, dramatic rim lighting, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Macintosh_computer_in_boardroom_9ed801cb_2K.jpg",
        "category": "broll",
        "shot_num": "01E",
        "target_name": "EP01_FLOW_STUDY_01E_Mac_Boardroom_StudyB_2K.jpg",
        "preview_name": "ep01_flow_broll_01e_mac_boardroom_b.jpg",
        "title": "Macintosh LC II у конференц-залі ради директорів (Ракурс B)",
        "act": "ACT1",
        "timecode": "00:45–01:15",
        "prompt": "Archival concept study: side profile of vintage Macintosh LC II on minimalist dark table, soft amber backlight, cinematic depth of field, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Computer_in_boardroom_obsidian_void_d6e23985_2K.jpg",
        "category": "broll",
        "shot_num": "07C",
        "target_name": "EP01_FLOW_STUDY_07C_Computer_Boardroom_Void_2K.jpg",
        "preview_name": "ep01_flow_broll_07c_boardroom_void.jpg",
        "title": "Комп'ютерний термінал в обсидіановій порожнечі ради директорів",
        "act": "ACT3",
        "timecode": "11:45–12:30",
        "prompt": "Obsidian void concept: glowing retro-futuristic computing workstation in absolute black room, single pool of spotlight, cold thriller atmosphere, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Silhouette_against_illuminated_w…_f135a90b_2K.jpg",
        "category": "broll",
        "shot_num": "07D",
        "target_name": "EP01_FLOW_IMG_07D_Silhouette_Against_Window_2K.jpg",
        "preview_name": "ep01_flow_broll_07d_silhouette_window.jpg",
        "title": "Силует засновника біля панорамного вікна під час нічної грози",
        "act": "ACT3",
        "timecode": "12:15–13:00",
        "prompt": "Low-key silhouette of leader looking through rain-streaked floor-to-ceiling glass window over foggy San Francisco night skyline, moody reflections, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Silhouette_at_illuminated_comput…_7c9f2966_2K.jpg",
        "category": "broll",
        "shot_num": "02F",
        "target_name": "EP01_FLOW_IMG_02F_Silhouette_At_Computer_2K.jpg",
        "preview_name": "ep01_flow_broll_02f_silhouette_computer.jpg",
        "title": "Силует програміста за свіченням монітора",
        "act": "ACT1",
        "timecode": "01:15–02:00",
        "prompt": "Backlit silhouette of young coder seated before bright monitor screen in pitch black room, amber particles floating, 35mm grain, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Visual_study_of_vintage_hardware_290cf9b9_2K.jpg",
        "category": "broll",
        "shot_num": "01F",
        "target_name": "EP01_FLOW_STUDY_01F_Vintage_Hardware_Macro_2K.jpg",
        "preview_name": "ep01_flow_broll_01f_vintage_hardware.jpg",
        "title": "Макро-дослідження вінтажної материнської плати 1993 року",
        "act": "ACT1",
        "timecode": "02:00–02:30",
        "prompt": "Macro photography of vintage motherboard traces, capacitors, Motorola 68030 processor socket, warm tungsten rim lighting, 4k."
    },
    {
        "ep": "01",
        "dl_file": "Optical_visualization_of_symboli…_8dc6924a_2K.jpg",
        "category": "broll",
        "shot_num": "08B",
        "target_name": "EP01_FLOW_STUDY_08B_Optical_Symbolic_Filaments_2K.jpg",
        "preview_name": "ep01_flow_broll_08b_optical_filaments.jpg",
        "title": "Оптична візуалізація символічних ниток світла",
        "act": "ACT4",
        "timecode": "14:15–15:00",
        "prompt": "Photorealistic scientific optical visualization of glowing fiber-optic quantum filaments refracting through geometric crystal prisms, Octane render, 8k."
    },
    {
        "ep": "01",
        "dl_file": "Visual_study_of_architectural_el…_67027e7f_2K.jpg",
        "category": "broll",
        "shot_num": "06B",
        "target_name": "EP01_FLOW_STUDY_06B_Architectural_Monoliths_2K.jpg",
        "preview_name": "ep01_flow_broll_06b_arch_monoliths.jpg",
        "title": "Архітектурне дослідження серверних монолітів",
        "act": "ACT2",
        "timecode": "08:45–09:15",
        "prompt": "Architectural visual study of brutalist server monoliths, pristine glass reflections, volumetric fog, blue LED guidance lights, 4k."
    },

    # === EP03: Demis Hassabis (12 items) ===
    {
        "ep": "03",
        "dl_file": "Wooden_king_falling_onto_chessboard_fcd6f10e_2K.jpg",
        "category": "primary",
        "shot_num": "01",
        "target_name": "EP03_FLOW_IMG_01_Wooden_King_Falling_Chessboard_2K.jpg",
        "preview_name": "ep03_flow_kf_01_wooden_king.jpg",
        "title": "Дерев'яний шаховий король падає на дошку (Лондон 1980)",
        "act": "ACT1",
        "timecode": "00:00–00:15",
        "prompt": "Extreme macro cinematic shot of a wooden king chess piece casting a long sharp shadow across a glowing digital grid in a dark room, cinematic depth of field, 35mm Kodak film grain, 4k 24fps."
    },
    {
        "ep": "03",
        "dl_file": "Chess_knight_transforming_into_w…_c07848fb_2K.jpg",
        "category": "primary",
        "shot_num": "03",
        "target_name": "EP03_FLOW_IMG_03_Staunton_Chess_Knight_Macro_2K.jpg",
        "preview_name": "ep03_flow_kf_03_chess_knight.jpg",
        "title": "Шаховий кінь Стаунтона над турнірною дошкою",
        "act": "ACT1",
        "timecode": "01:15–01:45",
        "prompt": "Photorealistic scientific optical visualization of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Black_stone_on_goban_board_7a6eacc7_2K.jpg",
        "category": "primary",
        "shot_num": "07",
        "target_name": "EP03_FLOW_IMG_07_AlphaGo_Move_37_Goban_Stone_2K.jpg",
        "preview_name": "ep03_flow_kf_07_move37_goban.jpg",
        "title": "Чорний камінь AlphaGo Хід 37 на дошці гобан (Сеул 2016)",
        "act": "ACT3",
        "timecode": "10:30–12:00",
        "prompt": "Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, deep chiaroscuro shadows, Kodak 2383 D60 film print, 4k 24fps."
    },
    {
        "ep": "03",
        "dl_file": "Black_Go_stone_on_board_b8e13dbc_2K.jpg",
        "category": "broll",
        "shot_num": "07B",
        "target_name": "EP03_FLOW_BROLL_07B_Go_Stone_CloseA_2K.jpg",
        "preview_name": "ep03_flow_broll_07b_go_stone_a.jpg",
        "title": "Чорний камінь Го на сітці гобану (Макро-ракурс A)",
        "act": "ACT3",
        "timecode": "10:45–11:15",
        "prompt": "Macro close-up of obsidian slate Go stone on warm natural wood grid, delicate woodgrain texture, directional side light, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Black_Go_stone_on_board_ee9f6f4d_2K.jpg",
        "category": "broll",
        "shot_num": "07C",
        "target_name": "EP03_FLOW_BROLL_07C_Go_Stone_CloseB_2K.jpg",
        "preview_name": "ep03_flow_broll_07c_go_stone_b.jpg",
        "title": "Чорний камінь Го на сітці гобану (Макро-ракурс B)",
        "act": "ACT3",
        "timecode": "11:15–11:45",
        "prompt": "Low-angle cinematic macro of black Go stone reflecting soft amber rim light, shallow focus on the intersecting grid line, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Fingers_holding_Go_stone_68b95370_2K.jpg",
        "category": "broll",
        "shot_num": "07D",
        "target_name": "EP03_FLOW_BROLL_07D_Fingers_Holding_Go_Stone_2K.jpg",
        "preview_name": "ep03_flow_broll_07d_fingers_stone.jpg",
        "title": "Пальці гравця тримають камінь Го перед вирішальним ходом",
        "act": "ACT3",
        "timecode": "11:45–12:15",
        "prompt": "Tactile close-up of human player's index and middle fingers holding smooth slate Go stone, tension in hands, Seoul Four Seasons hotel ambient lighting, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Go_stone_landing_on_grid_1f1e7ee0_2K.jpg",
        "category": "broll",
        "shot_num": "07E",
        "target_name": "EP03_FLOW_BROLL_07E_Go_Stone_Landing_Grid_2K.jpg",
        "preview_name": "ep03_flow_broll_07e_stone_landing.jpg",
        "title": "Момент удару каменю Го об дерево гобану (Звук кліку)",
        "act": "ACT3",
        "timecode": "12:15–12:45",
        "prompt": "High-speed 120fps slow-motion capture of black Go stone landing crisply on wooden grid, microscopic dust displacement, acoustic tactile shock, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Grandmaster_resting_hands_on_tem…_edcb4f21_2K.jpg",
        "category": "broll",
        "shot_num": "07F",
        "target_name": "EP03_FLOW_BROLL_07F_Grandmaster_Lee_Sedol_Temples_2K.jpg",
        "preview_name": "ep03_flow_broll_07f_grandmaster.jpg",
        "title": "Гросмейстер Лі Седоль тримається за скроні після Ходу 37",
        "act": "ACT3",
        "timecode": "12:45–13:30",
        "prompt": "Cinematic medium close-up of Korean Go grandmaster sitting in deep contemplation with hands resting on temples, psychological shock of facing alien machine intuition, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Go_board_transforming_into_heatmap_c7fccade_2K.jpg",
        "category": "broll",
        "shot_num": "07G",
        "target_name": "EP03_FLOW_STUDY_07G_MCTS_Policy_Heatmap_2K.jpg",
        "preview_name": "ep03_flow_broll_07g_heatmap.jpg",
        "title": "Дошка Го трансформується у теплову карту ймовірностей (MCTS)",
        "act": "ACT3",
        "timecode": "13:30–14:15",
        "prompt": "Scientific CGI visualization: physical wooden goban grid melting into glowing cyan and magenta probabilistic heatmap of Monte Carlo Tree Search neural policy, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Go_board_in_cosmic_nebula_5f5e1d44_2K.jpg",
        "category": "broll",
        "shot_num": "07H",
        "target_name": "EP03_FLOW_STUDY_07H_Go_Board_Cosmic_Nebula_2K.jpg",
        "preview_name": "ep03_flow_broll_07h_cosmic_nebula.jpg",
        "title": "Дошка Го у космічній туманності (10^170 можливих ходів)",
        "act": "ACT3",
        "timecode": "14:15–15:00",
        "prompt": "Cosmic scale metaphor: luminous Go grid floating among star clusters and swirling interstellar dust clouds, symbolizing the infinite search space greater than atoms in universe, 8k."
    },
    {
        "ep": "03",
        "dl_file": "Chess_and_Go_boards_floating_3f541701_2K.jpg",
        "category": "broll",
        "shot_num": "01B",
        "target_name": "EP03_FLOW_STUDY_01B_Chess_Go_Boards_Floating_2K.jpg",
        "preview_name": "ep03_flow_broll_01b_floating_boards.jpg",
        "title": "Шахівниця та гобан ширяють у порожнечі (Синтез стратегій)",
        "act": "ACT1",
        "timecode": "00:45–01:15",
        "prompt": "Philosophical 3D study: traditional European chessboard and Asian Go board slowly revolving in zero gravity dark void, golden light filaments connecting the squares, 4k."
    },
    {
        "ep": "03",
        "dl_file": "Chess_piece_and_Go_stone_9ae731f8_2K.jpg",
        "category": "broll",
        "shot_num": "01C",
        "target_name": "EP03_FLOW_STUDY_01C_Chess_Piece_Go_Stone_2K.jpg",
        "preview_name": "ep03_flow_broll_01c_piece_stone.jpg",
        "title": "Символічна пара: Шаховий ферзь та камінь Го",
        "act": "ACT1",
        "timecode": "01:45–02:15",
        "prompt": "Minimalist macro composition of hand-carved boxwood chess queen standing adjacent to a matte black slate Go stone on dark obsidian mirror, pristine reflection, 4k."
    },

    # === EP06: Ilya Sutskever (4 items) ===
    {
        "ep": "06",
        "dl_file": "Visual_study_of_Jerusalem_limestone_70620dfe_2K.jpg",
        "category": "primary",
        "shot_num": "01",
        "target_name": "EP06_FLOW_IMG_01_Jerusalem_Limestone_Roots_2K.jpg",
        "preview_name": "ep06_flow_kf_01_jerusalem_limestone.jpg",
        "title": "Єрусалимський камінь та коріння дитинства Іллі",
        "act": "ACT1",
        "timecode": "00:00–01:30",
        "prompt": "Photorealistic scientific optical visualization of warm twilight falling across golden Jerusalem stone walls, ancient mathematical geometry, contemplative quiet, 4k 24fps."
    },
    {
        "ep": "06",
        "dl_file": "Student_knocking_on_professor's_…_932d8f75_2K.jpg",
        "category": "primary",
        "shot_num": "02",
        "target_name": "EP06_FLOW_IMG_02_Student_Knocking_Hinton_Door_2K.jpg",
        "preview_name": "ep06_flow_kf_02_knocking_door.jpg",
        "title": "Студент Ілля стукає у двері професора Джеффрі Хінтона (Торонто 2003)",
        "act": "ACT1",
        "timecode": "01:30–03:00",
        "prompt": "University of Toronto 2003: young student knocking on weathered oak office door of Professor Geoffrey Hinton, dim corridor light, academic atmosphere, destiny moment, 4k."
    },
    {
        "ep": "06",
        "dl_file": "Researcher_viewing_graphics_cards_eddd647e_2K.jpg",
        "category": "primary",
        "shot_num": "04",
        "target_name": "EP06_FLOW_IMG_04_Researcher_Viewing_GPUs_AlexNet_2K.jpg",
        "preview_name": "ep06_flow_kf_04_researcher_gpus.jpg",
        "title": "Дослідник спостерігає за GPU в лабораторії AlexNet (2012)",
        "act": "ACT2",
        "timecode": "04:30–06:00",
        "prompt": "Close-up of glowing matrix multiplication lines streaming across two hot graphics cards in a dark room in 2012, researcher silhouette watching screens, birth of deep learning, 4k."
    },
    {
        "ep": "06",
        "dl_file": "Vintage_computer_motherboard_tra…_1325590a_2K.jpg",
        "category": "broll",
        "shot_num": "04B",
        "target_name": "EP06_FLOW_STUDY_04B_Motherboard_Traces_GPU_2K.jpg",
        "preview_name": "ep06_flow_broll_04b_motherboard_traces.jpg",
        "title": "Доріжки материнської плати та PCIe шини графічних карт",
        "act": "ACT2",
        "timecode": "06:00–06:45",
        "prompt": "Top-down vertical birds-eye macro of circuit board PCIe bus tracks illuminating with cyan pulses, microscopic electronic copper architecture, 4k."
    },

    # === EP10: Andrew Ng (2 items) ===
    {
        "ep": "10",
        "dl_file": "Doctor_father_showing_medical_te…_32ef6366_2K.jpg",
        "category": "primary",
        "shot_num": "02",
        "target_name": "EP10_FLOW_IMG_02_Doctor_Father_Medical_Textbook_2K.jpg",
        "preview_name": "ep10_flow_kf_02_doctor_father.jpg",
        "title": "Батько-лікар показує юному Ендрю підручник з експертних систем (1984)",
        "act": "ACT1",
        "timecode": "00:25–01:45",
        "prompt": "1984 Hong Kong and Singapore montage: a doctor father showing his young son a medical textbook on expert systems, warm desk lamp illumination, nostalgic film texture, 4k."
    },
    {
        "ep": "10",
        "dl_file": "Father_showing_medical_textbook_…_ae1053d0_2K.jpg",
        "category": "broll",
        "shot_num": "02B",
        "target_name": "EP10_FLOW_BROLL_02B_Father_Son_Medical_Textbook_Close_2K.jpg",
        "preview_name": "ep10_flow_broll_02b_father_textbook_close.jpg",
        "title": "Батько та син вивчають схеми експертних систем (Близький ракурс)",
        "act": "ACT1",
        "timecode": "01:45–02:30",
        "prompt": "Intimate documentary close-up: hands of father and child turning thin printed paper pages with diagrams of artificial intelligence diagnostic trees, warm golden lighting, 4k."
    }
]

print(f"Starting ingestion of {len(ASSETS)} assets...")

# Ensure EP directories exist
EP_NAMES = {
    "01": "EP01_Altman",
    "03": "EP03_Hassabis",
    "06": "EP06_Sutskever",
    "10": "EP10_Ng"
}

for ep, folder in EP_NAMES.items():
    os.makedirs(os.path.join(RAW_DIR, "flow_images", folder, "01_primary_keyframes"), exist_ok=True)
    os.makedirs(os.path.join(RAW_DIR, "flow_images", folder, "02_broll_stills_and_studies"), exist_ok=True)

copied_count = 0
for item in ASSETS:
    ep = item["ep"]
    folder = EP_NAMES[ep]
    sub = "01_primary_keyframes" if item["category"] == "primary" else "02_broll_stills_and_studies"
    src = os.path.join(DL_DIR, item["dl_file"])
    dst = os.path.join(RAW_DIR, "flow_images", folder, sub, item["target_name"])
    
    if not os.path.exists(src):
        print(f"ERROR: missing {src}")
        continue
    
    # Copy high-res 2K file
    shutil.copy2(src, dst)
    sz_mb = os.path.getsize(dst) / 1024 / 1024
    
    # Generate web preview (resize max width 1280, quality 85%)
    preview_dst = os.path.join(PREVIEW_DIR, item["preview_name"])
    with Image.open(dst) as img:
        w, h = img.size
        target_w = 1280
        target_h = int(h * (target_w / w))
        thumb = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        thumb.save(preview_dst, "JPEG", quality=85, optimize=True)
    
    item["raw_path"] = os.path.relpath(dst, ROOT)
    item["web_preview"] = os.path.relpath(preview_dst, DASH_DIR)
    item["size_mb"] = round(sz_mb, 2)
    item["resolution"] = f"{w}x{h}"
    copied_count += 1
    print(f"[{copied_count:02d}/{len(ASSETS)}] Ingested {item['target_name']} ({sz_mb:.2f}MB, {w}x{h}) -> {item['preview_name']}")

print(f"\nSuccessfully ingested {copied_count} assets!")
