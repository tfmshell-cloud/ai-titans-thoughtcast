#!/usr/bin/env python3
"""
EP01 «Сем Альтман: Анатомія експоненти» — Акти II–IV і повний епізод (режисерська версія Claude).

Наскрізні мотиви
  * «Розмита межа» з Акту I: анімація = внутрішній світ, фото/архів = реальність.
  * Рими: хлопчик за CRT (Акт I) повертається у фіналі на словах «поки система нарешті не оживе»;
    корпус Mac з холодного відкриття замикає епізод з клацанням реле CRT.
  * Матеріали інших епізодів працюють на сюжет Альтмана: угода Google–DeepMind (EP03), Суцкевер
    і розкол листопада 2023 (EP06), сервери NVIDIA DGX і NVLink (EP02), закони масштабу (EP07),
    сенат, Білий дім, саміт з безпеки ШІ, Уолл-стріт (EP07–EP09), енергія (EP10).

Запуск:
  python3 build_ep01_acts.py                 # мікси музики + FCPXML для II, III, IV і повного епізоду
  python3 build_ep01_acts.py --resolve       # + імпорт у SEM (старі версії цих таймлайнів замінюються)
  python3 build_ep01_acts.py --only II       # лише один акт
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ep01_engine as E                     # noqa: E402
import build_ep01_actI_claude_cut as A1     # noqa: E402

bar = E.bar
VO_DIR = "EP01_VO_UA_{:02d}_"


def vo_name(n):
    d = os.path.join(E.BASE, "03_AUDIO", "voiceover", "EP01_ALTMAN_UA_MASTER")
    return next(f for f in sorted(os.listdir(d)) if f.startswith(VO_DIR.format(n)) and f.endswith(".wav"))


def make_at(starts):
    def at(n, rel):
        return starts[n] + int(round(rel * E.FPS)) - 3
    return at


def vo_block(spec):
    """spec: {n: (такт, тривалість_с)} → (vo, starts)"""
    vo = {n: (vo_name(n), bar(b), secs) for n, (b, secs) in spec.items()}
    return vo, {n: v[1] for n, v in vo.items()}


def vo_markers(vo):
    return [(f0, "Blue", f"Д{n:02d}", name) for n, (name, f0, s) in vo.items()]


U = None  # місце для приміток

# =========================================================================== АКТ II
vo2, s2 = vo_block({7: (2, 48.85), 8: (22, 48.77), 9: (42, 45.56), 10: (61, 43.65)})
a = make_at(s2)
ACT2 = dict(
    name="Акт II", end_f=bar(81), vo=vo2,
    v1=[
        (0,          "EP01_CLIP_V1_16_ServerCold_8s.mp4", 0, None, "титр АКТ II"),
        (a(7, 0),     "EP01_V2_B2_01_TechCrunch_Disrupt_2014_10s.mp4", 0, None, "Д07 «У 2014 році…»"),
        (a(7, 5.08),  "EP01_VID_ARCH_05_ACT2_24FPS_Altman_Stanford_CS183B_Lecture.mp4", 2.0, None, "Д07 президент YC — справжня лекція 2014"),
        (a(7, 10.9),  "EP01_V2_B2_02_Stanford_2014_10s.mp4", 0, None, "Д07 «у джинсах і старих кросівках»"),
        (a(7, 16.32), "EP01_V1_B2_00_Startup_Engine_Matrix_14s.mp4", 0, None, "Д07 «штампувати мобільні додатки»"),
        (a(7, 21.46), "EP01_V1_B2_07_Corporate_Transmutation_15s.mp4", 0, None, "Д07 «розвертає штурвал велетенської машини»"),
        (a(7, 24.78), "ep01_flow_09_fusion_torus.mp4", 0, None, "Д07 YC Research, Helion — термоядерний синтез"),
        (a(7, 30.0),  "EP01_V1_B2_01_Retro_Cellular_14s.mp4", 0, None, "Д07 Retro Biosciences"),
        (a(7, 33.82), "ep08_clip_still_wall_street_nyse_6s.mp4", 0, None, "Д07 «роздратування традиційних фінансистів» (EP08)"),
        (a(7, 37.8),  "EP01_CLIP_STILL_TechCrunch_2014_10s.mp4", 2.0, None, "Д07 «знаменитий маніфест»"),
        (a(7, 40.54), "EP01_UA_CLIP_CARD_03_Exponential_Risk_15s.mp4", 0, None, "Д07 ЦИТАТА"),
        (a(8, 0),     "Photographic_strobe_inverting_image_81594c7e_1080p.mp4", 0, None, "Д08 «сліпа зона… мислять лінійно»"),
        (a(8, 5.28),  "EP01_V1_B3_02_Boardroom_Void_14s.mp4", 0, None, "Д08 «20% на рік — інвестор задоволений»"),
        (a(8, 10.34), "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4", 0, -14, "Д08 «обчислення не підкоряються лінійності»"),
        (a(8, 14.02), "EP02_CLIP_STILL_GF110_GTX580_Die_6s.mp4", 0, None, "Д08 «потужність чіпів подвоюється» (EP02)"),
        (a(8, 17.36), "Camera_zooms_out_from_microchip_9bc5eb71_1080p.mp4", 0, -14, "Д08 «у мільярд разів» — від чипа до планети"),
        (a(8, 22.4),  "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", 0, None, "Д08 вечеря в Rosewood"),
        (a(8, 27.5),  "Four_men_sitting_at_table_3911bdbc_1080p.mp4", 0, None, "Д08 «зводить разом…»"),
        (a(8, 31.0),  "EP06_VID_ARCH_07_ACT2_24FPS_Sutskever_OpenAI_Origins_NoPriors.mp4", 16.0, None, "Д08 Ілля Суцкевер (EP06)"),
        (a(8, 35.22), "EP06_SCI_01_Alcubierre_Warp_Drive_Metric.mp4", 0, None, "Д08 «тема — екзистенційна»"),
        (a(8, 37.56), "EP03_CLIP_STILL_DeepMind_KingsCross_6s.mp4", 0, None, "Д08 Google купив DeepMind (EP03)"),
        (a(8, 39.9),  "EP03_VID_ARCH_11_ACT2_24FPS_Google_650M_Deal_Military_Ethics.mp4", 11.0, None, "Д08 Деміс Гассабіс (EP03)"),
        (a(8, 42.25), "Camera_moving_through_server_aisle_48549a87_1080p.mp4", 0, -12, "Д08 «концентрація інтелекту… смертельно небезпечно»"),
        (a(9, 0),     "EP01_DOC_02_OpenAI_Introducing_12s.mp4", 0, None, "Д09 11 грудня 2015"),
        (a(9, 6.56),  "EP06_CLIP_STILL_OpenAI_Pioneer_Building_6s.mp4", 0, None, "Д09 некомерційна лабораторія (EP06)"),
        (a(9, 10.06), "EP01_V1_B2_06_Server_Matrix_Billions_15s.mp4", 0, None, "Д09 «1 мільярд доларів»"),
        (a(9, 13.92), "Fiber-optic_nodes_pulse_and_expand_da399bab_1080p.mp4", 0, -14, "Д09 «мета — AGI»"),
        (a(9, 20.44), "EP01_V1_NEW_01_Silhouette_Dorm_14s.mp4", 0, None, "Д09 «пошук наосліп»"),
        (a(9, 23.6),  "EP01_V1_B2_04_Robotic_Dexterity_15s.mp4", 0, None, "Д09 кубик Рубіка"),
        (a(9, 26.62), "EP01_V1_B2_03_Singularity_Threat_12s.mp4", 0, None, "Д09 Dota 2"),
        (a(9, 29.08), "EP01_V1_B2_05_Swarm_Gaming_RL_12s.mp4", 0, None, "Д09 «академія глузувала»"),
        (a(9, 31.4),  "EP03_CLIP_STILL_Royal_Society_London_6s.mp4", 0, None, "Д09 «піар-майданчик мільярдерів» (EP03)"),
        (a(9, 37.3),  "EP06_VID_ARCH_07_ACT2_24FPS_Sutskever_OpenAI_Origins_NoPriors.mp4", 21.0, None, "Д09 гіпотеза Суцкевера (EP06)"),
        (a(9, 43.46), "EP07_DOC_03_ACT2_scaling_laws_7orders_openai_2020.mp4", 0, None, "Д09 «Масштаб вирішує все» (EP07)"),
        (a(10, 0),    "EP02_VID_ARCH_15_ACT3_24FPS_NVIDIA_DGX_Server_Hallway_Pressroom.mp4", 0, None, "Д10 гіпотеза масштабування (EP02)"),
        (a(10, 5.56), "EP02_VID_ARCH_16_ACT3_24FPS_NVIDIA_NVLink_Fiber_Rack_Pressroom.mp4", 0, None, "Д10 «десятки мільйонів… чіпи» (EP02)"),
        (a(10, 8.8),  "EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4", 0, -16, "Д10 «електроенергія» (EP10)"),
        (a(10, 12.48), "Glass_shatters_into_voxel_bricks_6403835d_1080p.mp4", 0, -12, "Д10 «хід, який розколює індустрію»"),
        (a(10, 17.7), "EP01_V1_CREATIVE_07_Golden_Transistor_Dust_8s.mp4", 0, None, "Д10 capped-profit"),
        (a(10, 23.6), "Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4", 0, -14, "Д10 мільярд від Microsoft — лабораторія → рукостискання"),
        (a(10, 30.24), "EP01_V2_B2_04_TechCrunch_Disrupt_2019_OpenAI_CEO_10s.mp4", 0, None, "Д10 «критики кричали…»"),
        (a(10, 36.1), "EP01_UA_CLIP_CARD_04_Compute_Equations_18s.mp4", 0, None, "Д10 ЦИТАТА"),
    ],
    v3=[(10, "EP01_SUPER_10_Act_II_Title.png", 4.6),
        (a(7, 0.3), "EP01_SUPER_11_YC_2014.png", 3.6),
        (a(8, 22.6), "EP01_SUPER_12_Rosewood_2015.png", 3.6),
        (a(10, 12.7), "EP01_SUPER_13_SF_2019.png", 3.6)],
    sfx=[],
    music=[("EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension.wav", 0, 0, bar(81), 3.0)],
)
ACT2["markers"] = vo_markers(vo2)

# =========================================================================== АКТ III
vo3, s3 = vo_block({11: (2, 46.11), 12: (20, 50.29), 13: (40, 43.73), 14: (58, 54.44)})
a = make_at(s3)
ACT3 = dict(
    name="Акт III", end_f=bar(82), vo=vo3,
    v1=[
        (0,           "EP01_CLIP_STILL_Boardroom_Tense_9s.mp4", 0, None, "титр АКТ III"),
        (a(11, 0),     "Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4", 0, -12, "Д11 «інтерфейс під назвою ChatGPT» — камера пірнає в екран"),
        (a(11, 9.74),  "EP01_CLIP_STILL_ChatGPT_Genesis_7s.mp4", 0, None, "Д11 «жодних прес-конференцій»"),
        (a(11, 13.9),  "Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4", 0, -12, "Д11 мільйон → сто мільйонів"),
        (a(11, 20.42), "EP04_CLIP_STILL_AI_Benchmarks_Curve_6s.mp4", 0, None, "Д11 найшвидший запуск в історії (EP04)"),
        (a(11, 25.38), "Aerial_view_of_city_center_41b81743_1080p.mp4", 0, None, "Д11 «світ прокинувся в іншій реальності»"),
        (a(11, 28.42), "Walls_dissolving_into_textbook_v…_de18897e_1080p.mp4", 6.8, None, "Д11 студенти"),
        (a(11, 31.5),  "EP10_VID_ARCH_14_ACT4_24FPS_AndrewNg_Sequoia_Agentic_Workflows_GPT.mp4", 8.0, None, "Д11 програмісти — бенчмарк GPT (EP10)"),
        (a(11, 34.5),  "ep09_clip_still_bletchley_summit_6s.mp4", 0, None, "Д11 екстрені безпекові саміти (EP09)"),
        (a(11, 38.12), "ep07_clip_still_white_house_2023_6s.mp4", 0, None, "Д11 овальні кабінети (EP07)"),
        (a(11, 42.0),  "EP01_VID_ARCH_01_ACT3_24FPS_Altman_Senate_Oath_Closeup.mp4", 0, None, "Д11 слухання в Сенаті — справжній архів"),
        (a(12, 0),     "EP01_V1_B2_02_Rosewood_Boardroom_15s.mp4", 5.0, None, "Д12 ТИША. П'ятниця, 17 листопада"),
        (a(12, 7.24),  "Mouse_click_triggers_flash_42a0e76f_1080p.mp4", 0, -14, "Д12 відеодзвінок"),
        (a(12, 9.24),  "Photographic_strobe_inverting_image_81594c7e_1080p.mp4", 0, -10, "Д12 «на екрані —»"),
        (a(12, 11.16), "Four_men_sitting_at_table_3911bdbc_1080p.mp4", 4.5, None, "Д12 рада директорів — тепловізор"),
        (a(12, 15.24), "EP06_CLIP_STILL_Sutskever_TAU_2023_6s.mp4", 0, None, "Д12 Ілля Суцкевер (EP06)"),
        (a(12, 16.5),  "ep01_flow_07_boardroom_noir.mp4", 0, None, "Д12 «розмова триває кілька хвилин»"),
        (a(12, 20.08), "Photographic_strobe_inverting_image_81594c7e_1080p.mp4", 2.0, -10, "Д12 «без попереджень»"),
        (a(12, 24.58), "EP01_V1_B3_01_Chess_King_Falling_12s.mp4", 0, None, "Д12 «його звільнено» — король падає"),
        (a(12, 27.8),  "EP01_DOC_03_Board_Ouster_10s.mp4", 0, None, "Д12 прес-реліз і формулювання"),
        (a(12, 35.66), "ep08_clip_still_wall_street_nyse_6s.mp4", 0, None, "Д12 «підриває світові біржі»"),
        (a(12, 39.02), "EP01_V1_ASSOC_01_Lidar_City_Grid_8s.mp4", 0, None, "Д12 акції Microsoft падають"),
        (a(12, 42.2),  "ep01_flow_07_boardroom_noir_ua_alt.mp4", 5.0, None, "Д12 «індустрія застигає» — СИСТЕМУ ЗАБЛОКОВАНО"),
        (a(12, 44.54), "EP01_V1_NEW_03_Window_Rain_16s.mp4", 6.0, None, "Д12 «викинуто з компанії»"),
        (a(13, 0),     "Finger_slamming_clock_plunger_dd1a4152_1080p.mp4", 0, -10, "Д13 «сто двадцять годин»"),
        (a(13, 4.66),  "EP06_VID_ARCH_13_ACT3_24FPS_Sutskever_Superalignment_Safety_NoPriors.mp4", 2.0, None, "Д13 рада: «нехтує безпекою» (EP06)"),
        (a(13, 8.7),   "EP06_CLIP_STILL_AGI_Effigy_Bonfire_6s.mp4", 0, None, "Д13 страх AGI (EP06)"),
        (a(13, 12.74), "Holographic_game_data_streams_fl…_0aa820c5_1080p.mp4", 0, -14, "Д13 «співробітники — це вчені»"),
        (a(13, 18.74), "EP01_V1_B3_03_Two_Silhouettes_Nadella_12s.mp4", 0, None, "Д13 «природа лояльності»"),
        (a(13, 23.32), "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4", 1.3, -14, "Д13 Наделла: лабораторія з необмеженим бюджетом"),
        (a(13, 31.94), "Mouse_click_triggers_flash_42a0e76f_1080p.mp4", 2.3, -12, "Д13 гостьовий бейдж на шиї"),
        (a(13, 38.08), "EP01_CLIP_STILL_Guest_Badge_Desk_10s.mp4", 0, None, "Д13 «публікує фото»"),
        (a(13, 40.34), "EP01_UA_CLIP_CARD_05_Guest_Badge_8s.mp4", 0, None, "Д13 ЦИТАТА"),
        (a(14, 0),     "EP01_CLIP_STILL_Employees_Solidarity_9s.mp4", 0, None, "Д14 «понеділок, ранок»"),
        (a(14, 6.28),  "EP01_DOC_05_Employees_Letter_12s.mp4", 0, None, "Д14 730 із 770"),
        (a(14, 10.6),  "EP01_UA_CLIP_CARD_06_730_Employees_11s.mp4", 0, None, "Д14 ЦИТАТА ультиматуму"),
        (a(14, 17.6),  "EP01_DOC_04_Sutskever_Regret_10s.mp4", 0, None, "Д14 підпис Суцкевера"),
        (a(14, 21.3),  "EP06_DOC_05_Nov2023_Rift_10s.mp4", 0, None, "Д14 «глибоко шкодує» (EP06)"),
        (a(14, 25.0),  "EP01_V2_B3_01_Altman_ChatGPT_Launch_10s.mp4", 0, None, "Д14 повернення на посаду CEO"),
        (a(14, 30.4),  "EP01_V1_CREATIVE_03_Chess_Simulation_Grid_15s.mp4", 0, None, "Д14 стару раду розпущено"),
        (a(14, 32.94), "EP01_V1_B3_04_Golden_Grid_Stabilizing_15s.mp4", 0, None, "Д14 анатомія лідерства"),
        (a(14, 37.66), "Timber_dissolving_into_crystal_m…_ed88b1bf_1080p.mp4", 0, -16, "Д14 «не на інструкціях чи контрактах»"),
        (a(14, 44.02), "ep01_flow_08_golden_signatures.mp4", 0, None, "Д14 «спільна віра команди» — підписи"),
        (a(14, 51.8),  "EP01_V1_B3_CLOSER_GoldenGrid_340f.mp4", 0, None, "кінець Акту III"),
    ],
    v3=[(10, "EP01_SUPER_20_Act_III_Title.png", 4.6),
        (a(11, 0.2), "EP01_SUPER_21_ChatGPT_2022.png", 3.6),
        (a(12, 0.3), "EP01_SUPER_22_Friday_Nov17.png", 5.0),
        (a(13, 0.3), "EP01_SUPER_23_120_Hours.png", 3.8),
        (a(14, 25.2), "EP01_SUPER_24_Wednesday_Nov22.png", 4.0)],
    sfx=[],
    music=[("EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav", 0, 0, s3[12] - 20, 0.05),          # різкий обрив
           ("EP01_MUS_B3_PART1_08_00_to_10_00_120s.wav", 0, s3[13] - bar(1), bar(82), 3.0)],    # повернення ритму
)
ACT3["markers"] = vo_markers(vo3) + [(s3[12] - 20, "Red", "ТИША", "Різкий обрив музики: Д12 звучить без музики (за сценарієм)")]

# =========================================================================== АКТ IV
vo4, s4 = vo_block({15: (2, 48.20), 16: (21, 59.64), 17: (45, 26.44)})
a = make_at(s4)
F = E.FPS
ACT4 = dict(
    name="Акт IV", end_f=bar(67), vo=vo4,
    v1=[
        (0,           "EP01_V1_B4_CLOSER_DeepSpace_154f.mp4", 0, None, "титр АКТ IV"),
        (a(15, 0),     "EP01_V1_NEW_06_Cosmic_Dyson_12s.mp4", 0, None, "Д15 «далеко за межі софту»"),
        (a(15, 6.96),  "Electrical_spark_traveling_neuro…_362f1f95_1080p.mp4", 0, -16, "Д15 «інтелект — не абстрактна наука»"),
        (a(15, 12.02), "Plane_blade_transforming_into_ci…_97ad6a7c_1080p.mp4", 2.5, -14, "Д15 «інтелект став фізичним товаром» — дерево стає чипом"),
        (a(15, 14.72), "EP10_SCI_01_Tesla_Coil_Electric_Discharges.mp4", 4.0, -14, "Д15 тервати енергії (EP10)"),
        (a(15, 18.54), "EP02_CLIP_STILL_DGX_B200_HGX_6s.mp4", 0, None, "Д15 мільйони чіпів (EP02)"),
        (a(15, 21.12), "EP01_DOC_06_Stargate_100B_Report_10s.mp4", 0, None, "Д15 Stargate"),
        (a(15, 24.7),  "Camera_moving_through_server_aisle_48549a87_1080p.mp4", 5.5, -12, "Д15 кластери на сотні мільярдів"),
        (a(15, 28.38), "EP01_DOC_07_7_Trillion_Chip_Network_10s.mp4", 0, None, "Д15 переговори з виробниками чипів"),
        (a(15, 32.0),  "ep01_flow_09_fusion_torus.mp4", 3.0, None, "Д15 ядерна енергетика і синтез"),
        (a(15, 36.4),  "Finger_drawing_glowing_algorithm…_57eaed58_1080p.mp4", 2.0, -16, "Д15 термодинамічна формула"),
        (a(15, 41.22), "EP02_SCI_01_Nanobots_Graphene_Lattice_Assembly.mp4", 5.0, -14, "Д15 «вартість близька до нуля» (EP02)"),
        (a(15, 45.4),  "ep10_clip_still_earth_dawn_lights_finale_6s.mp4", 0, None, "Д15 дефіцит зникне (EP10)"),
        (a(16, 0),     "EP01_UA_CLIP_CARD_07_Three_Rules_12s.mp4", 0, None, "Д16 «який головний урок…»"),
        (a(16, 5.88),  "Teenage_boy_speaking_into_microp…_9259f8fe_1080p.mp4", 2.0, None, "ПРАВИЛО 1 — рима: підліток на сцені"),
        (a(16, 9.84),  "EP01_CLIP_STILL_Neural_Lattice_10s.mp4", 4.0, None, "Д16 «переконуватиме у пересічності» — рима: коридори"),
        (a(16, 15.38), "Boy_aging_into_tech_leader_cd380219_1080p.mp4", 2.5, -16, "Д16 «зробити ставку на свою ідею»"),
        (a(16, 21.38), "ep01_flow_02_crt_code.mp4", 0, None, "ПРАВИЛО 2 — проблеми як код"),
        (a(16, 24.82), "EP01_V1_CREATIVE_04_Mind_Radiating_Light_12s.mp4", 4.0, None, "Д16 образи, страхи — рима: тріснута порцеляна"),
        (a(16, 30.12), "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4", 4.0, -14, "Д16 «криза — це баг»"),
        (a(16, 35.5),  "ep01_flow_03_silicon_laser.mp4", 0, None, "Д16 «перепишіть алгоритм»"),
        (a(16, 40.52), "ep01_flow_04_exponential_line.mp4", 2.0, -12, "ПРАВИЛО 3 — обирайте експоненту"),
        (a(16, 43.32), "Finger_slamming_clock_plunger_dd1a4152_1080p.mp4", 4.5, -12, "Д16 «обмінюєте час на виживання»"),
        (a(16, 48.7),  "Fiber-optic_nodes_pulse_and_expand_da399bab_1080p.mp4", 0, -14, "Д16 складний відсоток"),
        (a(16, 56.0),  "Light_point_explodes_into_streaks_0827d703_1080p.mp4", 3.3, -14, "Д16 автономні інструменти — мережа світу"),
        (a(17, 0),     "EP01_CLIP_STILL_Young_Altman_Portrait_5s.mp4", 0, None, "Д17 «ніж здається з дитинства» — рима"),
        (a(17, 4.02),  "EP01_UA_CLIP_CARD_08_Plastic_Reality_10s.mp4", 0, None, "Д17 ЦИТАТА про правила"),
        (a(17, 9.68),  "Aircraft_climbing_into_stratosph…_081016cf_1080p.mp4", 0, -12, "Д17 «сміливість масштабних запитань»"),
        (a(17, 14.0),  "ElevenLabs_video_seedance-2-5_Intense_macro_r_2026-11-09T12_58_53.mp4", 0, -14, "Д17 «над кодом до четвертої ранку» — МОРФІНГ"),
        (a(17, 19.04), "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4", 0.6, -8, "Д17 «поки система не оживе» — CRT вмикається (рима Акту I)"),
        (a(17, 21.72), "Camera_zooms_out_from_microchip_9bc5eb71_1080p.mp4", 5.0, -14, "Д17 «майбутнє не настає само собою»"),
        (a(17, 24.18), "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4", 3.3, -8, "Д17 «створюють просто зараз» — світанок"),
        (int(148.0 * F), "EP01_V1_B2_10_Earth_Horizon_Finale_550f.mp4", 0, None, "ФІНАЛ: Земля"),
        (int(162.0 * F), "ep01_flow_01_mac_chassis.mp4", 2.0, None, "ФІНАЛ: корпус Mac — коло замкнулося"),
        (int(167.5 * F), "EP01_END_CARD.png", 0, None, "фінальна картка"),
    ],
    v3=[(10, "EP01_SUPER_30_Act_IV_Title.png", 4.6),
        (a(16, 5.9), "EP01_RULE_A_Belief.png", 9.0),
        (a(16, 21.5), "EP01_RULE_B_Code.png", 8.0),
        (a(16, 40.6), "EP01_RULE_C_Exponent.png", 8.0)],
    sfx=[(int(162.0 * F), "EP01_ARCH_AUDIO_Macintosh_1992_CRT_Scan.wav", 8.0, -6)],
    music=[("EP01_MUS_15_ACT4_92BPM_Future_Horizon_Finale.wav", 0, 0, bar(67), 6.0)],
)
ACT4["markers"] = vo_markers(vo4)


# =========================================================================== Акт I (з режисерської версії)
def act1():
    vo = {n: (f, A1.vo_f(n), s) for n, (f, b, s) in A1.VO.items()}
    v2 = [(f0, n, d or (A1.at(4, 0.0) - f0)) for f0, n, d in A1.V2]
    return dict(name="Акт I", end_f=A1.END_F, vo=vo,
                v1=[(f0, n, si, db, note) for f0, n, si, ln, db, note in A1.V1],
                v2=v2, v3=A1.V3, sfx=A1.SFX,
                music=[(A1.MUSIC_SRC, 0, 0, A1.END_F, 3.0)],
                markers=vo_markers(vo) + list(A1.MARKERS))


ACTS = {"I": (act1(), "EP01_ActI_UA_Claude_DirectorsCut"), "II": (ACT2, "EP01_ActII_UA_Claude"), "III": (ACT3, "EP01_ActIII_UA_Claude"), "IV": (ACT4, "EP01_ActIV_UA_Claude")}


def mix_path(key):
    return os.path.join(E.BASE, "03_AUDIO", "claude_mix", f"EP01_MUS_Act{key}_ducked_Claude.wav")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolve", action="store_true")
    ap.add_argument("--only", choices=["I", "II", "III", "IV", "FULL"])
    ap.add_argument("--skip-mix", action="store_true")
    a_ = ap.parse_args()
    idx = E.index_files()
    out_dir = os.path.join(E.BASE, "06_DAVINCI_PROJECTS")
    keys = [] if a_.only == "FULL" else ([a_.only] if a_.only else ["I", "II", "III", "IV"])
    for k in keys:
        act, tl = ACTS[k]
        print(f"{act['name']}: {len(act['v1'])} планів, {act['end_f'] / E.FPS:.1f} с")
        if not (a_.skip_mix and os.path.exists(mix_path(k))):
            E.mix_music(act, idx, mix_path(k))
        xml, probs, paths = E.build_fcpxml([(act, 0, mix_path(k))], idx, tl)
        p = os.path.join(out_dir, f"{tl}.fcpxml")
        open(p, "w", encoding="utf-8").write(xml)
        for pr in probs:
            print("  УВАГА:", pr)
        for row in E.build_fcpxml.report:
            print(f"    {row[3]:12} {str(row[2]):>6} dB  {row[1][:60]}")
        if a_.resolve:
            E.to_resolve(p, paths, tl, act["markers"], replace=True)
    if a_.only in (None, "FULL"):
        a1 = ACTS["I"][0]
        seq, off = [(a1, 0, mix_path("I"))], a1["end_f"]
        markers = list(a1["markers"])
        for k in ("II", "III", "IV"):
            act = ACTS[k][0]
            seq.append((act, off, mix_path(k)))
            markers += [(f + off, c, n, note) for f, c, n, note in act["markers"]]
            off += act["end_f"]
        tl = "EP01_FULL_UA_Claude_DirectorsCut"
        xml, probs, paths = E.build_fcpxml(seq, idx, tl)
        p = os.path.join(out_dir, f"{tl}.fcpxml")
        open(p, "w", encoding="utf-8").write(xml)
        print(f"Повний епізод: {int(off / E.FPS // 60)} хв {off / E.FPS % 60:.0f} с")
        for pr in probs:
            print("  УВАГА:", pr)
        if a_.resolve:
            E.to_resolve(p, paths, tl, markers, replace=True)


if __name__ == "__main__":
    main()
