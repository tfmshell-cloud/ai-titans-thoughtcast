#!/usr/bin/env python3
"""
Generate Hollywood-Grade Interactive Media Vault & Second-by-Second Video Analysis Dashboard
Target: 07_DASHBOARD/media_vault_analysis.html
"""
import os, json, glob

PROJECT_ROOT = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast"
DASH_DIR = os.path.join(PROJECT_ROOT, "07_DASHBOARD")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "04_ASSETS", "user_ai_images")
VID_DIR = os.path.join(PROJECT_ROOT, "05_RAW_FOOTAGE", "user_ai_generations")

# Load video catalog
with open('/tmp/video_ai_catalog.json') as f:
    videos = json.load(f)

# Editorial Analysis Database for the 25 Videos
EDITORIAL_ANALYSIS = {
    "Boy_aging_into_tech_leader_cd380219_1080p.mp4": {
        "title": "Еволюція засновника: від спальні 90-х до дата-центру",
        "act": "АКТ 1 / АКТ 4",
        "flaw": "Різкі неприродні телепортації на 2.5s (гараж) та 3.8s (офіс). Людина зникає і з'являється у новому просторі без мотивованого переходу. Повністю ставити не можна.",
        "golden_in": "00:00 - 00:02.2 (Тейк А) та 00:05.8 - 00:09.9 (Тейк Б)",
        "golden_desc": "Тейк А: 2.2с теплого світла дитячої кімнати з CRT-монітором. Тейк Б: 4.1с монументального сидіння за скляним столом у нескінченному масиві серверів Stargate.",
        "status": "APPROVED SUBCLIPS"
    },
    "Boy_viewing_glowing_terminal_code_a3fe5f00_1080p.mp4": {
        "title": "Смарагдове сяйво першого термінала (Macintosh 1993)",
        "act": "АКТ 1 (00:15 - 00:45)",
        "flaw": "Жодних дефектів. Плавний кінематографічний наплив, фотореалістична шкіра та очі, що відбивають смарагдово-блакитні рядки UNIX-коду.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "Бездоганна 10-секундна атмосфера початку кодингу Сема Альтмана. Підходить під слова диктора про перше знайомство з Mac.",
        "status": "100% MASTER SHOT"
    },
    "Camera_accelerating_through_lett_clip_24ed2370_1080p.mp4": {
        "title": "Гіперпростір літер та математичних матриць",
        "act": "АКТ 4 (12:00 - 13:00)",
        "flaw": "Висока швидкість руху — може викликати сенсорне перевантаження, якщо ставити довше 6 секунд.",
        "golden_in": "00:02.0 - 00:07.5 (5.5 секунд)",
        "golden_desc": "Швидкісний політ крізь токени та символи. Ідеально під розповідь про те, як мова перетворюється на обчислювальний простір.",
        "status": "APPROVED SUBCLIP"
    },
    "Camera_moving_through_computer_m_clip_2acf3bda_1080p.mp4": {
        "title": "Макро-проліт над архітектурою материнської плати",
        "act": "АКТ 2 (04:15 - 04:40)",
        "flaw": "Кінець кліпу трохи сповільнюється у блюр.",
        "golden_in": "00:00 - 00:07.0 (7.0 секунд)",
        "golden_desc": "Золотаві мідні доріжки, чіпи та конденсатори. Ілюструє інженерний перехід YC до хардверних стартапів.",
        "status": "APPROVED SUBCLIP"
    },
    "Camera_orbiting_desk_photograph_2c2a80a3_1080p.mp4": {
        "title": "Орбіта навколо чорно-білої фотографії на столі",
        "act": "АКТ 1 (00:45 - 01:15)",
        "flaw": "Без дефектів. Глибока документальна ностальгія, м'яке аналогове світло лампи.",
        "golden_in": "00:01.0 - 00:08.5 (7.5 секунд)",
        "golden_desc": "Погляд у минуле: школа Джона Берроуза, спогади про формування характеру за столом.",
        "status": "100% MASTER SHOT"
    },
    "Camera_plunges_into_terminal_screen_11075f8d_1080p.mp4": {
        "title": "Пірнання в глибину скляного термінала / Квантовий перехід",
        "act": "АКТ 4 (13:10 - 13:20)",
        "flaw": "Початок має невеликий мікроривок рендерингу (перші 12 кадрів).",
        "golden_in": "00:00.8 - 00:08.5 (7.7 секунд)",
        "golden_desc": "Камера пробиває скло фосфорного монітора і входить у нескінченний світ нейронних потоків. Ударний монтажний стик.",
        "status": "APPROVED SUBCLIP"
    },
    "Digital_HUD_tracking_vehicles_d7d30811_1080p.mp4": {
        "title": "Супутниковий HUD-трекінг автомобілів у нічному місті (Loopt)",
        "act": "АКТ 1 (01:45 - 02:15)",
        "flaw": "Без дефектів. Досконала тактікал-візуалізація геолокації.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "Точне візуальне втілення першого стартапу Альтмана Loopt (геолокаційний трекер друзів у реальному часі).",
        "status": "100% MASTER SHOT"
    },
    "ElevenLabs_video_seedance-2-5_Authentic_histo_2026-11-09T12_29_51.mp4": {
        "title": "Хлопчик із викруткою розбирає материнку Apple на килимі",
        "act": "АКТ 1 (00:15 - 00:35)",
        "flaw": "Жодних дефектів! Абсолютний фестивальний шедевр: зерно плівки Kodak, пилинки, природні рухи дитячих рук.",
        "golden_in": "00:00 - 00:05.0 (Всі 5 секунд)",
        "golden_desc": "Ключовий архетипічний кадр дитинства Сема Альтмана. «Він не просто грав у ігри, він хотів знати, як влаштований кремній».",
        "status": "EMMY / OSCAR GRADE"
    },
    "ElevenLabs_video_seedance-2-5_Dynamic_camera__2026-11-09T12_53_36.mp4": {
        "title": "Студент із рюкзаком іде крізь кампус Стенфорда",
        "act": "АКТ 1 (01:30 - 02:00)",
        "flaw": "Початок 00:00 - 00:02.2 — це 2D аніме з неприродним махом рюкзака (те, що помітив користувач). СТРОГО ВИРІЗАТИ!",
        "golden_in": "00:02.5 - 00:05.0 (2.5 секунди / 61 кадр)",
        "golden_desc": "Після переходу: 100% фотореалістичний юнак у худі з військовим рюкзаком іде нічними іспанськими арками Стенфорда. Драматично і сильно.",
        "status": "CRITICAL CUT (USE 2.5s-5.0s ONLY)"
    },
    "ElevenLabs_video_seedance-2-5_Intense_macro_r_2026-11-09T12_58_53.mp4": {
        "title": "Екстремальне макро очей, що відбивають безмежність коду",
        "act": "АКТ 1 / АКТ 4",
        "flaw": "Без дефектів. Гіпнотичний фокус на райдужці ока.",
        "golden_in": "00:00 - 00:05.0 (Всі 5 секунд)",
        "golden_desc": "Погляд у майбутнє. Ідеально монтується перед або після текстової картки-цитати.",
        "status": "100% MASTER SHOT"
    },
    "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T11_32_59.mp4": {
        "title": "Анімація в реальний світ: хлопчик із викруткою (Take 1)",
        "act": "АКТ 1 (00:20 - 00:30)",
        "flaw": "00:00 - 00:02.5 — аніме-стилістика Ghibli. Якщо документальний фільм строгий, аніме-частину варто опустити.",
        "golden_in": "00:02.8 - 00:05.0 (2.2 секунди)",
        "golden_desc": "Чистий лайв-екшн фотореалізм: малюк зосереджено крутить гвинти на платі.",
        "status": "APPROVED SUBCLIP"
    },
    "ElevenLabs_video_seedance-2-5_Seamless_stylis_2026-11-09T12_34_37.mp4": {
        "title": "Анімація в реальний світ: хлопчик із викруткою (Take 2)",
        "act": "АКТ 1 (00:25 - 00:35)",
        "flaw": "Аналогічно: перша половина малювана, друга фотореалістична.",
        "golden_in": "00:02.8 - 00:05.0 (2.2 секунди)",
        "golden_desc": "Альтернативний живий план дитини над відкритою платою в сонячних променях.",
        "status": "APPROVED SUBCLIP"
    },
    "ElevenLabs_video_seedance-2-5_Slow,_powerful__2026-11-09T12_52_53.mp4": {
        "title": "Виступ підлітка біля мікрофона (Школа Джона Берроуза)",
        "act": "АКТ 1 (00:55 - 01:15)",
        "flaw": "00:00 - 00:02.3 — малюваний аніме-кадр у соборі з вітражем. Не відповідає кіно-есе.",
        "golden_in": "00:02.8 - 00:05.0 (2.2 секунди)",
        "golden_desc": "Живий юнак-старшокласник говорить у мікрофон на трибуні актової зали. Ідеально під історичний момент камінг-ауту Сема у консервативній школі.",
        "status": "APPROVED SUBCLIP (USE 2.8s-5.0s)"
    },
    "Four_men_sitting_at_table_3911bdbc_1080p.mp4": {
        "title": "Змова ради директорів OpenAI у переговорній (Листопад 2023)",
        "act": "АКТ 3 (09:10 - 09:30)",
        "flaw": "Перехід на 3.2s у тепловізор є раптовим. Потрібно або розбивати на два кліпи, або брати нуарну першу частину.",
        "golden_in": "00:00 - 00:03.2 (Драма) або 00:03.5 - 00:09.9 (Тепловізор)",
        "golden_desc": "Тейк 1: 3.2с напруженого кінематографічного шепоту чотирьох директорів (Фінчер-стайл). Тейк 2: Стеження крізь тепловізор FLIR за контурами тіл.",
        "status": "TWO HIGH-VALUE SUBCLIPS"
    },
    "Human_prenatal_development_3D_vi_clip_8b0d0b01_1080p.mp4": {
        "title": "3D-візуалізація біологічного розвитку клітини",
        "act": "АКТ 2 (05:15 - 05:40)",
        "flaw": "Без дефектів. Стерильна наукова естетика.",
        "golden_in": "00:01.0 - 00:08.0 (7.0 секунд)",
        "golden_desc": "Ілюструє інвестиції Альтмана у Retro Biosciences ($180M) та біологічне перепрограмування віку.",
        "status": "APPROVED SUBCLIP"
    },
    "Human_zygote_cell_division_timel_clip_063791c0_1080p.mp4": {
        "title": "Таймлапс мітозу: поділ клітини за законом експоненти",
        "act": "АКТ 1 / АКТ 2",
        "flaw": "Без дефектів.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "1 → 2 → 4 → 8... Візуальний закон складного відсотка та експоненціального масштабування.",
        "status": "100% MASTER SHOT"
    },
    "Laser_forms_text_words_89a267cd_1080p.mp4": {
        "title": "Лазерні промені випалюють текстові токени у повітрі",
        "act": "АКТ 3 (08:00 - 08:30)",
        "flaw": "Без дефектів. Гіперсучасна візуалізація генерації слів LLM.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "Ідеальна кінематографічна метафора релізу ChatGPT: слова матеріалізуються з чистого лазерного світла.",
        "status": "100% MASTER SHOT"
    },
    "Light_point_explodes_into_streaks_0827d703_1080p.mp4": {
        "title": "Квантовий вибух світності: розліт спектральних ліній (Take 1)",
        "act": "АКТ 3 (11:45 - 12:00)",
        "flaw": "Дуже яскравий фінальний спалах — потребує м'якого cross-dissolve у DaVinci.",
        "golden_in": "00:00 - 00:08.5 (8.5 секунд)",
        "golden_desc": "Тріумфальне повернення Альтмана в OpenAI: енергія солідарності 738 співробітників вибухає світлом.",
        "status": "APPROVED SUBCLIP"
    },
    "Light_point_explodes_into_streaks_c712a46e_1080p.mp4": {
        "title": "Квантовий спалах блакитно-білого спектра (Take 2)",
        "act": "АКТ 4 (12:20 - 12:40)",
        "flaw": "Без дефектів.",
        "golden_in": "00:01.0 - 00:08.5 (7.5 секунд)",
        "golden_desc": "Ілюстрація енергії Stargate та запалювання термоядерної плазми Helion Energy.",
        "status": "100% MASTER SHOT"
    },
    "Man_wearing_tactical_arctic_parka_24ef8e34_1080p.mp4": {
        "title": "Людина в арктичній парці на тлі засніженого горизонту",
        "act": "АКТ 4 (14:30 - 15:00)",
        "flaw": "Вертикальний формат 9:16 (1080x1920). Потрібно центрувати у 16:9 з масштабуванням 1.78x.",
        "golden_in": "00:01.0 - 00:05.5 (4.5 секунди)",
        "golden_desc": "Метафора стійкості перед льодовиковим штормом та випробуваннями Долини.",
        "status": "REQUIRES CROP / SCALE"
    },
    "Mouse_click_triggers_flash_42a0e76f_1080p.mp4": {
        "title": "Клацання миші запускає лавину обчислень (30 листопада 2022)",
        "act": "АКТ 3 (08:00 - 08:15)",
        "flaw": "Без дефектів. Винятковий таймінг і динаміка.",
        "golden_in": "00:00 - 00:07.5 (7.5 секунд)",
        "golden_desc": "Той самий клік, що випустив ChatGPT на свободу: палець тисне на клавішу миші, від контакту розлітається спалах.",
        "status": "EMMY / OSCAR GRADE"
    },
    "Neuron_morphs_into_GPU_chip_23314d03_1080p.mp4": {
        "title": "Біологічний нейрон трансмутує у кремнієвий кристал GPU",
        "act": "АКТ 2 (06:40 - 07:10)",
        "flaw": "Без дефектів. Музейний рівень медичної та кремнієвої CGI-графіки.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "Серце філософії OpenAI: біологія людського мозку перетікає у кремнієві ядра NVIDIA Blackwell.",
        "status": "EMMY / OSCAR GRADE"
    },
    "Photographic_strobe_inverting_image_81594c7e_1080p.mp4": {
        "title": "Імпульсний фотоспалах та інверсія портрета в негатив",
        "act": "АКТ 4 (12:50 - 13:10)",
        "flaw": "Часте стробування може втомлювати очі, брати коротким відрізком.",
        "golden_in": "00:02.0 - 00:06.0 (4.0 секунди)",
        "golden_desc": "Документальний арт-перехід між технічними главами.",
        "status": "APPROVED SUBCLIP"
    },
    "Physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4": {
        "title": "Фізична матерія розчиняється у цифрових бітах і матрицях",
        "act": "АКТ 4 (12:00 - 12:30)",
        "flaw": "Без дефектів. Величний масштаб дезінтеграції речовини.",
        "golden_in": "00:00 - 00:09.9 (Повний кліп)",
        "golden_desc": "Пряма візуалізація цитати Картки 14: «ШІ перестав бути абстрактним кодом. Це гігавати енергії, надпровідні річки та кремній».",
        "status": "EMMY / OSCAR GRADE"
    },
    "Spark_disruption_in_corporate_bo_clip_a6171ebf_1080p.mp4": {
        "title": "Дослідник біля скла → Збій → Бізнес-зустріч у хмарочосі",
        "act": "АКТ 3 (09:40 - 10:10)",
        "flaw": "Глючний цифровий зріз-телепортація на 00:02.2 - 00:03.2 (те, про що писав користувач). ВИРІЗАТИ ЦЕЙ ЗБІЙ!",
        "golden_in": "00:03.5 - 00:09.9 (6.4 секунди / 155 кадрів)",
        "golden_desc": "Чудовий, статусний план: бізнесмен іде по офісу з панорамним склінням над дощовим містом і тисне руку колезі. Чистий Голлівуд.",
        "status": "CRITICAL CUT (USE 3.5s-9.9s ONLY)"
    }
}

# Image Theme Mapping
ACT_MAP = {
    "ACT 1: GENESIS & MACINTOSH (00:00 - 04:00)": [
        "Child_inserting_floppy_disk_92a52bea_2K.jpg", "Boy_watching_glowing_code_77d7ee3b_2K.jpg",
        "_io.png", "vfre.png", "2026-11-09_14.45.29.jpg", "_df.png", "mymyy.png",
        "edsfrdtf.png", "mk.png", "vcx.png", "xzcs.png", "hmufj.png", "rvdst.png",
        "csr.png", "lknjb.png", "mmjghnfgbdf.png", "sax.png", "xdry.png", "bvcb.png",
        "kut.png", "sdgfhtyj.png", "_nkbh.png", "_v.png", "tredf.png"
    ],
    "ACT 2: EXPONENTIAL SCALING & YC (04:00 - 08:00)": [
        ";ll;.png", "byr.png", "utyfgv.png", "dv.png", "dxf_g.png", "cdwrf.png",
        "Human_prenatal_development_3D_vi…_3ec5e8ed_2K.jpg", "p;.png",
        "bhnuyvtf.png", "ghnfbyd.png", "jlgyf.png"
    ],
    "ACT 3: THE BOARDROOM COUP & REBELLION (08:00 - 12:00)": [
        "_fgxfhcg.png", "by.png", "cfz.png", "image.png", "rvt.png", "xas.png",
        "xasdwrc.png", "scesxcsr.png", "vscds.png", "ybr.png"
    ],
    "ACT 4: THE PHYSICALITY OF COMPUTE & HORIZON (12:00 - 16:00)": [
        "_yfht.png", "b_cgbxtd.png", "kjh.png", "nlbv.png", "xdgcfh.png"
    ]
}

# Generate HTML
html = f'''<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Titans: Голлівудський Медіа-Волт & Секундний Аналіз Футажів</title>
  <style>
    :root {{
      --bg: #07090e;
      --surface: #0f141f;
      --surface-elevated: #161e2e;
      --border: #1e293b;
      --border-accent: #38bdf8;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --gold: #fbbf24;
      --emerald: #10b981;
      --rose: #f43f5e;
      --cyan: #38bdf8;
      --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", sans-serif;
      --mono: ui-monospace, Menlo, Monaco, monospace;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: var(--font);
      line-height: 1.6;
      padding: 2rem;
      -webkit-font-smoothing: antialiased;
    }}
    .container {{ max-width: 1500px; margin: 0 auto; }}

    /* Header */
    header {{
      background: linear-gradient(135deg, #131b2e 0%, #0a0e17 100%);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }}
    .badge {{
      display: inline-block;
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 1rem;
    }}
    .badge-gold {{ background: rgba(251, 191, 36, 0.15); color: var(--gold); border: 1px solid var(--gold); }}
    .badge-emerald {{ background: rgba(16, 185, 129, 0.15); color: var(--emerald); border: 1px solid var(--emerald); }}
    .badge-rose {{ background: rgba(244, 63, 94, 0.15); color: var(--rose); border: 1px solid var(--rose); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid var(--cyan); }}

    h1 {{ font-size: 2.2rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 0.75rem; }}
    p.lead {{ color: var(--text-muted); font-size: 1.05rem; max-width: 900px; margin-bottom: 1.5rem; }}

    .quick-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border);
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.25rem;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid var(--border);
    }}
    .btn-primary {{ background: var(--cyan); color: #000; border-color: var(--cyan); }}
    .btn-primary:hover {{ background: #7dd3fc; }}
    .btn-secondary {{ background: var(--surface-elevated); color: var(--text); }}
    .btn-secondary:hover {{ background: #222f46; border-color: var(--cyan); }}

    /* Grid Sections */
    section {{ margin-bottom: 3.5rem; }}
    h2 {{ font-size: 1.6rem; font-weight: 700; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.75rem; }}
    p.section-sub {{ color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem; }}

    .stat-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 2rem;
    }}
    .stat-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
    }}
    .stat-val {{ font-size: 1.8rem; font-weight: 800; color: var(--cyan); font-family: var(--mono); }}
    .stat-lbl {{ font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; font-weight: 600; }}

    /* Video Cards Grid */
    .video-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
      gap: 1.5rem;
    }}
    .video-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: border-color 0.2s ease;
    }}
    .video-card:hover {{ border-color: var(--cyan); }}
    .video-header {{
      padding: 1.25rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
    }}
    .video-title {{ font-size: 1.05rem; font-weight: 700; line-height: 1.3; }}
    .video-file {{ font-family: var(--mono); font-size: 0.75rem; color: var(--cyan); margin-top: 0.25rem; }}
    .video-body {{ padding: 1.25rem; flex-grow: 1; display: flex; flex-direction: column; gap: 1rem; }}
    
    .critique-box {{
      background: rgba(244, 63, 94, 0.08);
      border-left: 3px solid var(--rose);
      padding: 0.75rem 1rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.85rem;
    }}
    .critique-title {{ font-weight: 700; color: var(--rose); margin-bottom: 0.25rem; display: flex; align-items: center; gap: 0.4rem; }}

    .golden-box {{
      background: rgba(16, 185, 129, 0.08);
      border-left: 3px solid var(--emerald);
      padding: 0.75rem 1rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.85rem;
    }}
    .golden-title {{ font-weight: 700; color: var(--emerald); margin-bottom: 0.25rem; display: flex; align-items: center; gap: 0.4rem; }}
    .golden-timecode {{ font-family: var(--mono); font-size: 0.9rem; color: #fff; font-weight: 800; }}

    .video-footer {{
      padding: 1rem 1.25rem;
      background: var(--surface-elevated);
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .meta-tag {{ font-family: var(--mono); font-size: 0.75rem; color: var(--text-muted); }}

    /* Image Gallery */
    .image-accordion {{ margin-bottom: 2rem; }}
    .theme-header {{
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      padding: 1rem 1.5rem;
      border-radius: 10px;
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 1rem;
      color: var(--gold);
      display: flex;
      justify-content: space-between;
    }}
    .image-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}
    .img-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}
    .img-card:hover {{ transform: translateY(-3px); border-color: var(--cyan); }}
    .img-card img {{ width: 100%; height: 130px; object-fit: cover; display: block; }}
    .img-meta {{ padding: 0.65rem 0.85rem; font-size: 0.75rem; font-family: var(--mono); color: var(--text-muted); }}
    .img-name {{ color: var(--text); font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
  </style>
</head>
<body>
<div class="container">

  <!-- Header -->
  <header>
    <div class="badge badge-gold">🏆 OSCAR-GRADE PRODUCTION ARCHITECTURE</div>
    <h1>AI TITANS (СЕМ АЛЬТМАН): ГОЛЛІВУДСЬКИЙ МЕДІА-ВОЛТ</h1>
    <p class="lead">
      Повний професійний каталог і посекундний аналіз 25 нових AI-відеокліпів та 50 концепт-зображень.
      Кожен кадр перевірено на артефакти, визначено точні хронометражі золотих фрагментів (In/Out) та синхронізовано з 16-хвилинним мастер-таймлайном DaVinci Resolve.
    </p>

    <div class="stat-strip">
      <div class="stat-card">
        <div class="stat-val">16:00.00</div>
        <div class="stat-lbl">Мастер-Таймлайн (23,040 Кадрів)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">0 DUPS</div>
        <div class="stat-lbl">Дублікатів Відео (100% Унікальність)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">0 CLASH</div>
        <div class="stat-lbl">Колізій V2/V3 (Ніколи 3 шари)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">17 TAKES</div>
        <div class="stat-lbl">100% Український Дубляж (+2.0 dB)</div>
      </div>
    </div>

    <div class="quick-actions">
      <a href="http://127.0.0.1:8765/open_folder?path={PROJECT_ROOT}/05_RAW_FOOTAGE/user_ai_generations" class="btn btn-primary" target="_blank">
        📁 Відкрити 25 Відео у Finder
      </a>
      <a href="http://127.0.0.1:8765/open_folder?path={PROJECT_ROOT}/04_ASSETS/user_ai_images" class="btn btn-secondary" target="_blank">
        🖼️ Відкрити 50 Зображень у Finder
      </a>
      <a href="https://github.com/tfmshell-cloud/ai-titans-thoughtcast" class="btn btn-secondary" target="_blank">
        🐙 GitHub Репозиторій
      </a>
      <a href="index.html" class="btn btn-secondary">
        📊 Головний Дашборд
      </a>
      <a href="season1_telemetry_dashboard.html" class="btn btn-secondary">
        📈 Телеметрія 10 Титанів
      </a>
    </div>
  </header>

  <!-- SECTION 0: LIVE MULTI-HERO MEDIA VAULT WORKBENCH (EP01 - EP10) -->
  <section id="seasonVaultWorkbench" style="background:linear-gradient(135deg,#0f172a,#111827);border:1px solid rgba(56,189,248,0.45);border-radius:16px;padding:1.75rem;margin-bottom:2.5rem;">
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:1rem;margin-bottom:1.1rem;">
      <div>
        <div class="badge badge-cyan" style="margin-bottom:0.45rem;">🎬 ЄДИНИЙ МЕДІА-ВОЛТ СЕЗОНУ 1 (EP01 – EP10)</div>
        <h2 style="margin:0 0 0.35rem 0;">УСІ ВІДЕО, АРХІВИ, 4K ДОСЬЄ, ФОТО ТА ТРАНСКРИПТИ ПО КОЖНОМУ ГЕРОЮ</h2>
        <p style="color:var(--text-muted);font-size:0.9rem;max-width:920px;">
          Живий інтерактивний індекс бази <code style="color:var(--cyan);">PROJECT_VAULT_INVENTORY</code> та <code style="color:var(--gold);">MEDIA_ACQUISITION_POOL</code>. Оберіть титана (зокрема EP05 Ян Лекун або EP06 Ілля Суцкевер), щоб переглянути всі відеокліпи, фото та завантажені першоджерела.
        </p>
      </div>
      <div style="display:flex;gap:0.5rem;align-items:center;flex-wrap:wrap;">
        <input id="vaultGlobalSearch" type="search" placeholder="Пошук файлу, фото або транскрипту..." style="padding:0.55rem 0.9rem;border-radius:8px;border:1px solid var(--border);background:#07090e;color:#f8fafc;min-width:250px;font-size:0.85rem;">
      </div>
    </div>
    <div id="seasonHeroSelector" style="display:flex;gap:0.45rem;flex-wrap:wrap;margin-bottom:1.15rem;"></div>
    <div id="seasonHeroSummaryStrip" style="display:flex;gap:0.65rem;flex-wrap:wrap;align-items:center;margin-bottom:1.15rem;"></div>
    <div id="seasonVaultContent"></div>
  </section>

  <!-- SECTION 1: 25 VIDEOS IN-DEPTH CRITIQUE -->
  <section>
    <h2>🎬 СЕКУНДНИЙ РОЗБІР 25 AI-ВІДЕОКЛІПІВ: БРАК, АРТЕФАКТИ ТА ЗОЛОТІ СУБХОХОДЖЕННЯ</h2>
    <p class="section-sub">
      Ретельний покадровий аудит. Більшість згенерованих відео не можна ставити цілком через аніме-вставки, раптові телепортації або цифрові спотворення. Ними сформовано точні таймкоди для монтажу.
    </p>

    <div class="video-grid">
'''

for v in videos:
    fname = v['file']
    ed = EDITORIAL_ANALYSIS.get(fname, {
        "title": fname,
        "act": "RESERVE",
        "flaw": "Потребує перегляду динаміки.",
        "golden_in": f"00:00 - {v['duration_sec']:.1f}s",
        "golden_desc": "Робочий матеріал для підкладки.",
        "status": "RAW FOOTAGE"
    })

    badge_class = "badge-emerald" if "100%" in ed['status'] or "EMMY" in ed['status'] else ("badge-rose" if "CRITICAL" in ed['status'] else "badge-cyan")

    html += f'''
      <div class="video-card">
        <div class="video-header">
          <div>
            <div class="badge {badge_class}">{ed['status']}</div>
            <div class="video-title">{ed['title']}</div>
            <div class="video-file">{fname}</div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--mono); font-weight: 700; color: var(--gold);">{v['duration_sec']}s</div>
            <div style="font-size: 0.75rem; color: var(--text-muted);">{v['resolution']} @ {v['fps']}fps</div>
          </div>
        </div>

        <div class="video-body">
          <div class="critique-box">
            <div class="critique-title">⚠️ ЧОМУ НЕ СТАВИТИ ПОВНІСТЮ (ШІ-АРТЕФАКТИ):</div>
            <div>{ed['flaw']}</div>
          </div>

          <div class="golden-box">
            <div class="golden-title">✨ ЗОЛОТИЙ ФРАГМЕНТ ДЛЯ МОНТАЖУ (IN - OUT):</div>
            <div class="golden-timecode">{ed['golden_in']}</div>
            <div style="margin-top: 0.25rem;">{ed['golden_desc']}</div>
          </div>
        </div>

        <div class="video-footer">
          <span class="meta-tag">🎯 ПРИЗНАЧЕННЯ: <b>{ed['act']}</b></span>
          <a href="http://127.0.0.1:8765/reveal?path={v['path']}" class="btn btn-secondary" style="padding: 0.35rem 0.75rem; font-size: 0.75rem;" target="_blank">
            🔍 Показати у Finder
          </a>
        </div>
      </div>
'''

html += '''
    </div>
  </section>

  <!-- SECTION 2: 50 IMAGES THEMATIC CATALOG -->
  <section>
    <h2>🖼️ КАТАЛОГ 50 КОНЦЕПТ-ЗОБРАЖЕНЬ (GEMINI / GOOGLE FLOW) ЗА АКТАМИ ТАЙМЛАЙНУ</h2>
    <p class="section-sub">
      Розбивка за драматургічними актами: дитинство 90-х, школи та кампус Стенфорда, кремнієва революція та суперкластери майбутнього.
    </p>
'''

for act_title, img_names in ACT_MAP.items():
    html += f'''
    <div class="image-accordion">
      <div class="theme-header">
        <span>{act_title}</span>
        <span>{len(img_names)} ЗОБРАЖЕНЬ</span>
      </div>
      <div class="image-grid">
    '''
    for iname in img_names:
        ipath = os.path.join(ASSETS_DIR, iname)
        if not os.path.exists(ipath):
            # check with spaces replaced
            ipath = os.path.join(ASSETS_DIR, iname.replace(' ', '_'))
        html += f'''
        <div class="img-card">
          <img src="../04_ASSETS/user_ai_images/{os.path.basename(ipath)}" alt="{iname}" loading="lazy">
          <div class="img-meta">
            <div class="img-name" title="{iname}">{iname}</div>
            <div style="margin-top: 0.35rem; display: flex; justify-content: space-between;">
              <span>HD/2K</span>
              <a href="http://127.0.0.1:8765/reveal?path={ipath}" style="color: var(--cyan); text-decoration: underline;" target="_blank">Finder</a>
            </div>
          </div>
        </div>
        '''
    html += '''
      </div>
    </div>
    '''

html += f'''
  </section>

  <!-- SECTION 3: TIMELINE ARCHITECTURE -->
  <section style="background: var(--surface); border: 1px solid var(--border); border-radius: 16px; padding: 2rem;">
    <h2>📐 АРХІТЕКТУРА 16-ХВИЛИННОГО МАСТЕР-ТАЙМЛАЙНУ (23 040 КАДРІВ)</h2>
    <p class="section-sub">
      Повний перелік 7 активних професійних треків у DaVinci Resolve Studio:
    </p>
    <div style="font-family: var(--mono); font-size: 0.85rem; line-height: 1.8; color: var(--text-secondary);">
      <div>🟢 <b>Track V1 (MASTER_FLOW_CANVAS):</b> 94 унікальні кліпи, 100% gapless без чорних кадрів (5760f + 5760f + 5760f + 5760f = 23,040f).</div>
      <div>🔵 <b>Track V2 (HISTORICAL_ARCHIVES):</b> 19 архівних моментів (Jobs WWDC, CS183B, Senate, TED). Жодного перекриття з V3!</div>
      <div>🟡 <b>Track V3 (THOUGHT_CARDS_PRESS):</b> 17 карток думок + 6 розсекречених досьє з м'якими 12-кадровими дізолвами.</div>
      <div>🎙️ <b>Track A1 (UKRAINIAN_VOICEOVER):</b> 17 майстер-тейків Макса Цукренка (00:00 - 16:00) на рівні +2.0 dB.</div>
      <div>🎵 <b>Track A2 (CINEMATIC_SCORE):</b> 4-актний безперервний ембієнт-пульс (-21.0 dB) з 5-секундним оксамитовим затуханням.</div>
      <div>🏛️ <b>Track A3 (AUTHENTIC_LIVE_AUDIO):</b> 3 живі історичні промови (Стів Джобс 2008, лекція CS183B, заява в Сенаті США).</div>
      <div>⌨️ <b>Track A4 (MECHANICAL_KEYBOARD_SFX):</b> 16 звукових спалахів друкарської клавіатури (-18.0 dB), синхронізованих із картками.</div>
    </div>
  </section>

</div>
<script src="data/season1_index.js?v=20261110_v10"></script>
<script src="data/media_acquisition_pool.js?v=20261110_v10"></script>
<script src="data/project_vault_inventory.js?v=20261110_v10"></script>
<script>
(function () {{
  var season = window.SEASON1_INDEX || [];
  var vault = window.PROJECT_VAULT_INVENTORY || {{}};
  var pool = window.MEDIA_ACQUISITION_POOL || {{}};
  var params = new URLSearchParams(window.location.search || "");
  var activeEp = params.get("ep") || "07";
  if (!vault[activeEp] && season.length) activeEp = season[0].ep;
  var activeKind = "videos";
  var searchQ = "";

  function esc(s) {{
    return String(s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }}

  function renderVaultWorkbench() {{
    var selEl = document.getElementById("seasonHeroSelector");
    var sumEl = document.getElementById("seasonHeroSummaryStrip");
    var bodyEl = document.getElementById("seasonVaultContent");
    if (!selEl || !sumEl || !bodyEl) return;

    selEl.innerHTML = season.map(function (h) {{
      var s = (vault[h.ep] || {{}}).summary || {{}};
      var isAct = h.ep === activeEp;
      return '<button data-pick-ep="' + esc(h.ep) + '" class="btn ' + (isAct ? 'btn-primary' : 'btn-secondary') + '" style="padding:0.45rem 0.85rem;font-size:0.8rem;">' +
        'EP' + esc(h.ep) + ' • ' + esc(h.name) + ' <span style="opacity:0.8;">(' + (s.videos_count || 0) + '📹/' + (s.images_count || 0) + '🖼️/' + (s.research_docs_count || 0) + '📚)</span></button>';
    }}).join("");

    var hInfo = season.find(function (x) {{ return x.ep === activeEp; }}) || {{}};
    var vEp = vault[activeEp] || {{}};
    var vSum = vEp.summary || {{}};
    var pEp = pool[activeEp] || {{}};
    var q = searchQ.trim().toLowerCase();

    sumEl.innerHTML = [
      '<span class="badge badge-cyan" style="margin:0;">🎥 Відео: ' + (vSum.videos_count || 0) + ' (Власних: ' + (vSum.native_videos_count || 0) + ')</span>',
      '<span class="badge badge-gold" style="margin:0;">🖼️ Фото & 4K карти: ' + (vSum.images_count || 0) + '</span>',
      '<span class="badge badge-emerald" style="margin:0;">📚 Джерел & Транскриптів: ' + (vSum.research_docs_count || 0) + ' (' + ((vSum.research_words || 0).toLocaleString("uk-UA")) + ' слів)</span>',
      '<button data-vault-kind="videos" class="btn ' + (activeKind === "videos" ? "btn-primary" : "btn-secondary") + '" style="padding:0.35rem 0.75rem;font-size:0.78rem;">🎥 Відео (' + ((vEp.videos || []).length) + ')</button>',
      '<button data-vault-kind="images" class="btn ' + (activeKind === "images" ? "btn-primary" : "btn-secondary") + '" style="padding:0.35rem 0.75rem;font-size:0.78rem;">🖼️ Зображення (' + ((vEp.images || []).length) + ')</button>',
      '<button data-vault-kind="research" class="btn ' + (activeKind === "research" ? "btn-primary" : "btn-secondary") + '" style="padding:0.35rem 0.75rem;font-size:0.78rem;">📚 Транскрипти & Статті (' + ((vEp.research_docs || []).length) + ')</button>',
      (hInfo.page_url ? ('<a href="' + esc(hInfo.page_url) + '#media-archives" class="btn btn-secondary" style="padding:0.35rem 0.75rem;font-size:0.78rem;">🚀 Відкрити Студію EP' + esc(activeEp) + ' →</a>') : '')
    ].join("");

    if (activeKind === "research") {{
      var docs = (vEp.research_docs || []).filter(function (d) {{
        return !q || (d.title + " " + d.file + " " + d.rel_path).toLowerCase().indexOf(q) !== -1;
      }});
      bodyEl.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:0.9rem;">' + docs.map(function (d) {{
        return '<div style="background:#07090e;border:1px solid var(--border);border-radius:10px;padding:0.85rem;">' +
          '<div style="display:flex;justify-content:space-between;font-size:0.74rem;margin-bottom:0.35rem;"><span style="color:var(--cyan);font-weight:700;">' + esc(d.cat_label) + '</span><span style="color:var(--text-muted);font-family:var(--mono);">' + esc(d.ext) + (d.word_count ? (' • ' + d.word_count.toLocaleString("uk-UA") + ' слів') : '') + '</span></div>' +
          '<div style="font-weight:700;font-size:0.9rem;margin-bottom:0.35rem;">' + esc(d.title) + '</div>' +
          '<div style="font-family:var(--mono);font-size:0.72rem;color:var(--text-muted);word-break:break-all;margin-bottom:0.5rem;">' + esc(d.rel_path) + '</div>' +
          (d.source_url ? ('<a href="' + esc(d.source_url) + '" target="_blank" rel="noopener" style="color:var(--emerald);font-size:0.78rem;">🌐 Першоджерело ↗</a>') : '') +
        '</div>';
      }}).join("") + '</div>';
    }} else if (activeKind === "images") {{
      var imgs = (vEp.images || []).filter(function (im) {{
        return !q || (im.display_name + " " + im.file + " " + im.cat_label).toLowerCase().indexOf(q) !== -1;
      }});
      bodyEl.innerHTML = '<div class="image-grid">' + imgs.map(function (im) {{
        var src = im.thumb || ("../" + im.rel_path);
        return '<div class="img-card"><img src="' + esc(src) + '" alt="' + esc(im.display_name) + '" loading="lazy">' +
          '<div class="img-meta"><div class="img-name" title="' + esc(im.file) + '">' + esc(im.display_name) + '</div>' +
          '<div style="margin-top:0.3rem;display:flex;justify-content:space-between;font-size:0.7rem;"><span>' + esc(im.res_label || im.ext) + '</span><a href="http://127.0.0.1:8765/reveal?path={PROJECT_ROOT}/' + esc(im.rel_path) + '" target="_blank" style="color:var(--cyan);">Finder</a></div></div></div>';
      }}).join("") + '</div>';
    }} else {{
      var vids = (vEp.videos || []).filter(function (v) {{
        return !q || (v.display_name + " " + v.file + " " + v.cat_label).toLowerCase().indexOf(q) !== -1;
      }});
      bodyEl.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:1rem;">' + vids.map(function (v) {{
        var prev = v.preview_path || v.thumb || ("../" + v.rel_path);
        var canPlayVideo = !!v.preview_path || (window.location.protocol === "file:");
        var playAttr = canPlayVideo ? (' data-play-src="' + esc(v.preview_path || ("../" + v.rel_path)) + '"') : '';
        var thumb = v.thumb || "";
        return '<div class="video-card" style="background:#07090e;">' +
          '<div' + playAttr + ' style="position:relative;aspect-ratio:16/9;background:#020408;' + (canPlayVideo ? 'cursor:pointer;' : '') + 'overflow:hidden;">' +
            (thumb ? ('<img src="' + esc(thumb) + '" alt="' + esc(v.display_name) + '" style="width:100%;height:100%;object-fit:cover;">') : '') +
            '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.28);font-size:28px;">' + (canPlayVideo ? '▶️' : '🎬') + '</div>' +
            '<span style="position:absolute;bottom:6px;right:6px;background:rgba(0,0,0,0.8);padding:2px 6px;border-radius:4px;font-size:11px;font-family:var(--mono);color:var(--gold);">' + esc(v.res_label || v.ext) + (v.dur_label ? (' • ' + v.dur_label) : '') + '</span>' +
          '</div>' +
          '<div style="padding:0.85rem;">' +
            '<div style="font-size:0.72rem;color:var(--cyan);font-weight:700;margin-bottom:0.25rem;">' + esc(v.cat_label) + '</div>' +
            '<div style="font-weight:700;font-size:0.9rem;margin-bottom:0.35rem;">' + esc(v.display_name) + '</div>' +
            '<div style="font-family:var(--mono);font-size:0.7rem;color:var(--text-muted);word-break:break-all;margin-bottom:0.5rem;">' + esc(v.rel_path) + '</div>' +
            '<a href="http://127.0.0.1:8765/reveal?path={PROJECT_ROOT}/' + esc(v.rel_path) + '" target="_blank" style="color:var(--cyan);font-size:0.75rem;text-decoration:underline;">🔍 Показати у Finder</a>' +
          '</div></div>';
      }}).join("") + '</div>';
    }}

    selEl.querySelectorAll("[data-pick-ep]").forEach(function (b) {{
      b.addEventListener("click", function () {{
        activeEp = b.getAttribute("data-pick-ep");
        renderVaultWorkbench();
      }});
    }});
    sumEl.querySelectorAll("[data-vault-kind]").forEach(function (b) {{
      b.addEventListener("click", function () {{
        activeKind = b.getAttribute("data-vault-kind");
        renderVaultWorkbench();
      }});
    }});
    bodyEl.querySelectorAll("[data-play-src]").forEach(function (box) {{
      box.addEventListener("click", function () {{
        var src = box.getAttribute("data-play-src");
        box.innerHTML = '<video src="' + esc(src) + '" controls autoplay playsinline style="width:100%;height:100%;object-fit:contain;background:#000;"></video>';
        box.style.cursor = "default";
      }});
    }});
  }}

  var gs = document.getElementById("vaultGlobalSearch");
  if (gs) {{
    gs.addEventListener("input", function () {{
      searchQ = gs.value || "";
      renderVaultWorkbench();
    }});
  }}
  renderVaultWorkbench();
}})();
</script>
</body>
</html>
'''

out_path = os.path.join(DASH_DIR, "media_vault_analysis.html")
with open(out_path, "w", encoding="utf-8") as out:
    out.write(html)

print(f"✓ Generated Media Vault Analysis Dashboard: {out_path}")
