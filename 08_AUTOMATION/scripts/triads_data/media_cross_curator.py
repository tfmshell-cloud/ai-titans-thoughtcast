#!/usr/bin/env python3
"""
Precision Visual Cross-Hero Curation & Semantic Title Registry across 234 Videos & 293 Images.

Strict rules enforced after full 3-frame (start / mid / end) visual audit of all videos:
1. Off-topic / test files (e.g., Icelandic flashcard fjall_jokull_flashcard.png, test_typewriter.mp4)
   are excluded from all Titan studios so editors never see unrelated clutter.
2. Stylized anime / Seedance persona clips, Sam Altman actor lookalikes, Apple Macintosh LC II props,
   OpenAI / Loopt / Psychological Friction screen text, and Hassabis-specific chess/ZX Spectrum/London
   scenes stay STRICTLY isolated to their native hero.
3. Blueprint wireframes (flow_previs_animatics & ep02..ep10_flow_01 previs grids) are tagged as `previs`
   and never cross-shared as finished cinematic B-Roll.
4. Only genuinely clean, visually verified abstract / scientific / hardware / cosmic / neural assets
   (or rare 100%-biographical matches like Hinton's carpentry plane & Sutskever's TAU/Regret artifacts)
   are curated across episodes, strictly deduplicated by file MD5 per episode.
"""

# Completely hidden from EP01..EP10 studios (still accounted for honestly in global telemetry _meta)
HIDDEN_NON_PROJECT_PATHS = {
    "04_assets/user_ai_images/fjall_jokull_flashcard.png",
    "05_raw_footage/dossiers_press/test_typewriter.mp4",
}

# Clean Ukrainian titles for cryptic filenames, non-Latin filenames, and multi-language Hassabis prompts
CRYPTIC_TITLE_OVERRIDES = {
    # EP01 user_ai_images
    "04_assets/user_ai_images/,io.png": "Хлопчик біля вінтажного CRT-монітора (теплий кадр)",
    "04_assets/user_ai_images/vfre.png": "Хлопчик біля вінтажного CRT-монітора (копія)",
    "04_assets/user_ai_images/2026-11-09_14.45.29.jpg": "Комп'ютерний клас 1990-х: ретро ПК у школі",
    "04_assets/user_ai_images/;ll;.png": "Нічна аеропанорама затоки Сан-Франциско та Долини",
    "04_assets/user_ai_images/_df.png": "Зелений код і хлопчик на старому CRT-екрані",
    "04_assets/user_ai_images/mymyy.png": "Зелений код і хлопчик на CRT-екрані (копія)",
    "04_assets/user_ai_images/_fgxfhcg.png": "Ділове рукостискання в скляному хмарочосі вночі",
    "04_assets/user_ai_images/_nkbh.png": "Юний програміст у нічній кімнаті перед CRT-терміналом",
    "04_assets/user_ai_images/nlbv.png": "Нічне робоче місце з трьома зеленими терміналами",
    "04_assets/user_ai_images/_v.png": "Студент із рюкзаком на нічній дощовій вулиці кампуса",
    "04_assets/user_ai_images/_yfht.png": "Засновник наодинці в темному кабінеті перед монітором",
    "04_assets/user_ai_images/b_cgbxtd.png": "Силует перед гіперпросторовим тунелем даних",
    "04_assets/user_ai_images/bhnuyvtf.png": "Інженери тестують серверний GPU-блейд у лабораторії",
    "04_assets/user_ai_images/ghnfbyd.png": "Інженери тестують GPU-сервер (тепле освітлення)",
    "04_assets/user_ai_images/bvcb.png": "Сценічна трибуна у залі з високими вікнами",
    "04_assets/user_ai_images/by.png": "Ч/Б кінопортрет на фоні формул і плівки",
    "04_assets/user_ai_images/byr.png": "Камера спостереження біля воріт вілли ввечері",
    "04_assets/user_ai_images/utyfgv.png": "Дрон-HUD телеметрія над особняком Долини",
    "04_assets/user_ai_images/cdwrf.png": "Біологічний нейрон зі спалахами синапсів",
    "04_assets/user_ai_images/cfz.png": "Керівник із бейджем заходить до скляного офісу",
    "04_assets/user_ai_images/image.png": "Керівник із бейджем заходить до офісу (копія)",
    "04_assets/user_ai_images/csr.png": "Макро райдужного логотипу на корпусі Macintosh LC II",
    "04_assets/user_ai_images/dv.png": "Дослідник пише рівняння Cost Function J(w,b) на дошці",
    "04_assets/user_ai_images/dxf_g.png": "Золоті електричні сигнали біжать доріжками плати",
    "04_assets/user_ai_images/edsfrdtf.png": "Хлопчик розбирає системну плату в сонячній кімнаті",
    "04_assets/user_ai_images/mk.png": "Хлопчик розбирає системну плату (копія 1)",
    "04_assets/user_ai_images/vcx.png": "Хлопчик розбирає системну плату (копія 2)",
    "04_assets/user_ai_images/xzcs.png": "Хлопчик розбирає системну плату (варіант 3)",
    "04_assets/user_ai_images/hmufj.png": "Портрет юного дослідника (великий план)",
    "04_assets/user_ai_images/jlgyf.png": "Ноутбук із кодом на дерев'яному столі біля вікна",
    "04_assets/user_ai_images/kjh.png": "Нескінченний футуристичний тунель серверних стійок",
    "04_assets/user_ai_images/kut.png": "Ч/Б студент за ноутбуком у кімнаті гуртожитку",
    "04_assets/user_ai_images/sdgfhtyj.png": "Студент за ноутбуком у гуртожитку 2000-х (колір)",
    "04_assets/user_ai_images/lknjb.png": "Макро вентиляційних решіток Macintosh LC II із сяйвом",
    "04_assets/user_ai_images/mmjghnfgbdf.png": "Аніме-концепт: дитина відкриває сяючий ПК",
    "04_assets/user_ai_images/sax.png": "Аніме-концепт: дитина відкриває сяючий ПК (копія)",
    "04_assets/user_ai_images/p;.png": "Типографічна заставка EXPONENTIAL",
    "04_assets/user_ai_images/rvdst.png": "Великий план очей візіонера (прямий погляд)",
    "04_assets/user_ai_images/rvt.png": "Напружений портрет у темному кабінеті",
    "04_assets/user_ai_images/scesxcsr.png": "Планета Земля в золотих орбітальних кільцях зв'язку",
    "04_assets/user_ai_images/tredf.png": "Аніме-концепт: юний фаундер виходить у нічне місто",
    "04_assets/user_ai_images/vscds.png": "Глобальна мережа золотих волокон над Землею",
    "04_assets/user_ai_images/ybr.png": "Глобальна мапа вузлів інновацій (Global Network)",
    "04_assets/user_ai_images/xas.png": "Нічний відеодзвінок ради директорів у темряві",
    "04_assets/user_ai_images/xasdwrc.png": "Макро золотого пера з краплею чорнила на папері",
    "04_assets/user_ai_images/xdgcfh.png": "Світанок над мегаполісом біля океану",
    "04_assets/user_ai_images/xdry.png": "Виступ перед мікрофоном у залі",
    # EP01 Seedance animations
    "elevenlabs_video_seedance-2-5_authentic_histo_2026-11-09t12_29_51.mp4": "Seedance (EP01): хлопчик вивчає материнську плату",
    "elevenlabs_video_seedance-2-5_dynamic_camera__2026-11-09t12_53_36.mp4": "Seedance (EP01): перехід зі скетчу в нічний Стенфорд",
    "elevenlabs_video_seedance-2-5_intense_macro_r_2026-11-09t12_58_53.mp4": "Seedance (EP01): погляд програміста перед CRT-монітором",
    "elevenlabs_video_seedance-2-5_seamless_stylis_2026-11-09t11_32_59.mp4": "Seedance (EP01): скетч у хлопчика біля плати (варіант А)",
    "elevenlabs_video_seedance-2-5_seamless_stylis_2026-11-09t12_34_37.mp4": "Seedance (EP01): скетч у хлопчика біля плати (варіант B)",
    "elevenlabs_video_seedance-2-5_slow,_powerful__2026-11-09t12_52_53.mp4": "Seedance (EP01): морф до сцени виступу біля мікрофона",
    # EP03 Hassabis non-English filenames -> Clean Ukrainian
    "80-കളിലെ zx spectrum ഡെസ്ക് രംഗം (1).png": "ZX Spectrum 1980-х — ретро-стіл із касетами (дубль)",
    "80-കളിലെ zx spectrum ഡെസ്ക് രംഗം.png": "ZX Spectrum 1980-х — ретро-стіл із касетами",
    "gylltur tímagöng með fornum klukkum.png": "Золотий тунель часу зі старовинними годинниками (PNG)",
    "gylltur_tímagöng_með_fornum_klukkum.png_2387450b.jpg": "Золотий тунель часу зі старовинними годинниками",
    "poiss malemäng boheemlaslikus elutoas.png": "Юний шахіст у богемній лондонській вітальні (PNG)",
    "poiss_malemäng_boheemlaslikus_elutoas.png_26e37029.jpg": "Юний шахіст у богемній лондонській вітальні",
    "skákborð_endurspeglast_í_augum_barns.png_82f4e399.jpg": "Шахівниця у відблиску очей дитини (JPG)",
    "skákborð endurspeglast í augum barns (1).png": "Шахівниця у відблиску очей дитини (копія 1)",
    "skákborð endurspeglast í augum barns (2).png": "Шахівниця у відблиску очей дитини (копія 2)",
    "skákborð endurspeglast í augum barns.png": "Шахівниця у відблиску очей дитини",
    # EP02 Jensen Huang Real Archives, Dossiers, Quote Cards & Ken Burns 4K Stills -> Clean Ukrainian
    "ep02_vid_arch_01_act3_24fps_huang_gtc_stage_walk.mp4": "Архів EP02 #01 • Вихід Дженсена Хуанга на сцену GTC",
    "ep02_vid_arch_02_act3_24fps_huang_blackwell_wafer_reveal.mp4": "Архів EP02 #02 • Презентація кремнієвої пластини Blackwell B200",
    "ep02_vid_arch_03_act1_24fps_huang_oneida_bathrooms_age9.mp4": "Архів EP02 #03 • Oneida (Кентуккі, 9 років): чищення туалетів (Stripe)",
    "ep02_vid_arch_04_act1_24fps_huang_dennys_dishwasher_notaskbeneath.mp4": "Архів EP02 #04 • «Немає низької праці» — Stanford GSB 2024",
    "ep02_vid_arch_05_act1_24fps_huang_dennys_booth_founding_60min.mp4": "Архів EP02 #05 • Повернення у Denny's Berryessa (CBS 60 Minutes)",
    "ep02_vid_arch_06_act1_24fps_huang_dennys_booth_inside_60min.mp4": "Архів EP02 #06 • Табличка «$2T Booth» + фото молодого Хуанга 1990-х",
    "ep02_vid_arch_07_act2_24fps_huang_2009_osu_we_failed.mp4": "Архів EP02 #07 • Рідкісний запис 2009 (OSU): «Ми провалилися»",
    "ep02_vid_arch_08_act2_24fps_huang_sega_lifeline_ntu2023.mp4": "Архів EP02 #08 • Сповідь перед CEO Sega на межі банкрутства (NTU 2023)",
    "ep02_vid_arch_09_act2_24fps_huang_invented_cuda_stripe2024.mp4": "Архів EP02 #09 • Як NVIDIA винайшла CUDA у нульовий ринок (Stripe 2024)",
    "ep02_vid_arch_10_act3_24fps_huang_gtc2016_dgx1_reveal.mp4": "Архів EP02 #10 • Прем'єра першого ШІ-суперкомп'ютера DGX-1 (GTC 2016)",
    "ep02_vid_arch_11_act4_24fps_huang_stanford_pain_and_suffering.mp4": "Архів EP02 #11 • Стенфорд: «Я бажаю вам болю та страждань» (SIEPR 2024)",
    "ep02_vid_arch_12_act4_24fps_huang_ntu2023_run_dont_walk.mp4": "Архів EP02 #12 • Фінальний заклик: «Біжіть, не йдіть!» (NTU 2023)",
    "ep02_vid_arch_13_act4_24fps_nvidia_endeavor_aerial_pressroom.mp4": "Архів EP02 #13 (Pressroom) • Аерообліт кампусів NVIDIA Endeavor & Voyager",
    "ep02_vid_arch_14_act4_24fps_huang_stage_blackvoid_pressroom.mp4": "Архів EP02 #14 (Pressroom) • Хуанг на темній сцені GTC (чистий силует)",
    "ep02_vid_arch_15_act3_24fps_nvidia_dgx_server_hallway_pressroom.mp4": "Архів EP02 #15 (Pressroom) • Коридор суперкомп'ютерних стійок DGX",
    "ep02_vid_arch_16_act3_24fps_nvidia_nvlink_fiber_rack_pressroom.mp4": "Архів EP02 #16 (Pressroom) • Макро оптоволокна NVLink та шин серверного кластера",
    "ep02_vid_arch_17_act1_24fps_huang_chm_oneida_kentucky.mp4": "Архів EP02 #17 (CHM Oral History) • Інтернат Oneida у Кентуккі",
    "ep02_vid_arch_18_act2_24fps_huang_chm_sega_generosity.mp4": "Архів EP02 #18 (CHM Oral History) • Сповідь CEO Sega та рятівний чек",
    "ep02_vid_arch_19_act3_24fps_huang_acquired_dgx_scale.mp4": "Архів EP02 #19 (Acquired) • Створення DGX-1 (10 000 А, 35 000 деталей)",
    "ep02_vid_arch_20_act2_24fps_huang_2013_no_business_plan.mp4": "Архів EP02 #20 (2013) • Молодший Хуанг: «Ми так і не написали бізнес-план»",
    "ep02_img_arch_01_taiwan_tamsui_1970_childhood_era.jpg": "Фотоархів #01 • Тайвань 1970 (Тамсуй) — дитинство до еміграції",
    "ep02_img_arch_02_oneida_kentucky_dorm_farm_campus.jpg": "Фотоархів #02 • Інтернат Oneida Baptist Institute (Кентуккі)",
    "ep02_img_arch_03_aloha_high_school_oregon_1981.jpg": "Фотоархів #03 • Aloha High School, Орегон (випуск 1981)",
    "ep02_img_arch_04_oregon_state_university_campus_1984.jpg": "Фотоархів #04 • Кампус Oregon State University (випуск 1984)",
    "ep02_img_arch_05_dennys_2484_berryessa_san_jose_1993.jpg": "Фотоархів #05 • Ресторан Denny's на 2484 Berryessa Rd (заснування 1993)",
    "ep02_img_arch_06_nvidia_nv1_500nm_silicon_die_1995.jpg": "Фотоархів #06 • Кристал першого чипа NVIDIA NV1 (1995, 500nm)",
    "ep02_img_arch_07_nvidia_riva_128_chip_1997.jpg": "Фотоархів #07 • Рятівний чип NVIDIA RIVA 128 (1997)",
    "ep02_img_arch_08_morris_chang_tsmc_founder.jpg": "Фотоархів #08 • Моріс Чанг — засновник TSMC, союзник Хуанга",
    "ep02_img_arch_09_nvidia_geforce_256_worlds_first_gpu_1999.jpg": "Фотоархів #09 • NVIDIA GeForce 256 (1999) — перший GPU у світі",
    "ep02_img_arch_10b_evga_geforce_gtx_580_card_2012.jpg": "Фотоархів #10 • Відеокарта GeForce GTX 580 (залізо AlexNet 2012)",
    "ep02_img_arch_10_evga_geforce_gtx_580_alexnet_2012.jpg": "Фотоархів #11 • Кристал Fermi GF110 (GTX 580 • 40nm)",
    "ep02_img_arch_11_jenhsun_huang_engineering_center_stanford.jpg": "Фотоархів #12 • Інженерний центр Джен-Сун Хуанга у Стенфорді",
    "ep02_img_arch_12_huang_early_leather_jacket_2014_portrait.jpg": "Фотоархів #13 • Студійний портрет Хуанга (архів 2014)",
    "ep02_img_arch_13_jensen_huang_gtc_keynote_2016.jpg": "Фотоархів #14 • Хуанг на сцені GTC біля слайда 1995 року",
    "ep02_img_arch_14_nvidia_dgx_supercomputer_front.jpg": "Фотоархів #15 • Компактний суперкомп'ютер NVIDIA DGX Spark",
    "ep02_img_arch_15_nvidia_dgx_b200_hgx_system.jpg": "Фотоархів #16 • Серверна платформа NVIDIA DGX B200 HGX",
    "ep02_img_arch_16_nvidia_endeavor_hq_santa_clara.jpg": "Фотоархів #17 • Штаб-квартира NVIDIA Endeavor (Санта-Клара)",
    "ep02_img_arch_16b_nvidia_endeavor_grand_opening_lobby.jpg": "Фотоархів #18 • Вхідна алея NVIDIA Endeavor",
    "ep02_img_arch_17_jensen_huang_stanford_keynote_portrait.jpg": "Фотоархів #19 • Хуанг зі студентами Стенфорду",
    "ep02_doc_02_act2_dennys_founding_charter_1993.png": "Досьє #02 (4K) • Хартія заснування у Denny's (1993)",
    "ep02_doc_03_act2_sega_nv2_rescue_memorandum_1997.png": "Досьє #03 (4K) • Провал NV1 та порятунок Sega за $5M (1997)",
    "ep02_doc_04_act2_riva128_geforce256_first_gpu_1999.png": "Досьє #04 (4K) • RIVA 128 → GeForce 256 (1997–1999)",
    "ep02_doc_05_act3_alexnet_gtx580_turning_point_2012.png": "Досьє #05 (4K) • AlexNet 2012 на двох GTX 580",
    "ep02_doc_06_act3_dgx1_openai_delivery_2016.png": "Досьє #06 (4K) • Перший DGX-1 для OpenAI (2016)",
    "ep02_ua_clip_card_01_no_task_beneath_10s.mp4": "Цитата #01 (4K • 10с) • «Не буває низької праці»",
    "ep02_ua_clip_card_02_dennys_dishwasher_10s.mp4": "Цитата #02 (4K • 10с) • «Найкращий посудомийник Denny's»",
    "ep02_ua_clip_card_03_sega_lifeline_12s.mp4": "Цитата #03 (4K • 12с) • «Наш чип не спрацює, але врятуйте нас»",
    "ep02_ua_clip_card_04_thirty_days_8s.mp4": "Цитата #04 (4K • 8с) • «До банкрутства — 30 днів»",
    "ep02_ua_clip_card_05_zero_market_cuda_10s.mp4": "Цитата #05 (4K • 10с) • «Будуємо ринок на нуль доларів»",
    "ep02_ua_clip_card_06_flat_org_55_reports_10s.mp4": "Цитата #06 (4K • 10с) • «Правда помирає на п'яти поверхах»",
    "ep02_ua_clip_card_07_pain_suffering_10s.mp4": "Цитата #07 (4K • 10с) • «Бажаю вам болю та страждань»",
    "ep02_ua_clip_card_08_run_dont_walk_12s.mp4": "Цитата #08 (4K • 12с) • «Біжіть, не йдіть!»",
    "ep02_clip_still_tamsui_1970_6s.mp4": "Ken Burns (4K • 6с) • Тайвань Тамсуй 1970",
    "ep02_clip_still_oneida_kentucky_6s.mp4": "Ken Burns (4K • 6с) • Інтернат Oneida, Кентуккі",
    "ep02_clip_still_aloha_high_5s.mp4": "Ken Burns (4K • 5с) • Школа Aloha High School",
    "ep02_clip_still_osu_campus_6s.mp4": "Ken Burns (4K • 6с) • Кампус Oregon State University",
    "ep02_clip_still_dennys_berryessa_7s.mp4": "Ken Burns (4K • 7с) • Забігайлівка Denny's, Сан-Хосе",
    "ep02_clip_still_nv1_die_6s.mp4": "Ken Burns (4K • 6с) • Кристал NVIDIA NV1 (500nm)",
    "ep02_clip_still_riva_128_6s.mp4": "Ken Burns (4K • 6с) • Рятівний чип RIVA 128",
    "ep02_clip_still_morris_chang_5s.mp4": "Ken Burns (4K • 5с) • Засновник TSMC Моріс Чанг",
    "ep02_clip_still_geforce_256_6s.mp4": "Ken Burns (4K • 6с) • Перший у світі GPU GeForce 256",
    "ep02_clip_still_evga_gtx580_card_6s.mp4": "Ken Burns (4K • 6с) • Відеокарта GeForce GTX 580",
    "ep02_clip_still_gf110_gtx580_die_6s.mp4": "Ken Burns (4K • 6с) • Кристал Fermi GF110 (GTX 580)",
    "ep02_clip_still_huang_center_stanford_5s.mp4": "Ken Burns (4K • 5с) • Центр Хуанга в Стенфорді",
    "ep02_clip_still_huang_2014_headshot_5s.mp4": "Ken Burns (4K • 5с) • Ранній портрет Хуанга 2014",
    "ep02_clip_still_huang_gtc_2016_6s.mp4": "Ken Burns (4K • 6с) • Сцена GTC поруч зі слайдом 1995",
    "ep02_clip_still_dgx_b200_hgx_6s.mp4": "Ken Burns (4K • 6с) • Платформа DGX B200 HGX",
    "ep02_clip_still_nvidia_endeavor_hq_6s.mp4": "Ken Burns (4K • 6с) • Штаб-квартира NVIDIA Endeavor",
    # EP03 Demis Hassabis Real Archives, Photos, Dossiers, Quote Cards & Ken Burns 4K Stills -> Clean Ukrainian
    "ep03_vid_arch_01_act4_24fps_hassabis_nobel_lecture_2024.mp4": "Архів EP03 #01 • Нобелівська лекція Деміса Гассабіса (Стокгольм 2024)",
    "ep03_vid_arch_02_act3_24fps_alphago_seoul_move37_reaction.mp4": "Архів EP03 #02 • Шок у Сеулі після Ходу 37 AlphaGo (2016)",
    "ep03_vid_arch_03_act1_24fps_hassabis_chess_age4_wsj.mp4": "Архів EP03 #03 (WSJ) • Гассабіс про шахи в 4 роки та збірну Англії",
    "ep03_vid_arch_04_act1_24fps_hassabis_childhood_chess_thinkinggame.mp4": "Архів EP03 #04 (Thinking Game) • Дитяча хроніка: юний шахіст Англії",
    "ep03_vid_arch_05_act1_24fps_hassabis_playing_chess_board.mp4": "Архів EP03 #05 • Жива шахова партія Гассабіса (з Лексом Фрідманом)",
    "ep03_vid_arch_06_act1_24fps_hassabis_leaving_chess_realization.mp4": "Архів EP03 #06 • Прозріння в 13 років: «300 умів мають лікувати рак»",
    "ep03_vid_arch_07_act1_24fps_hassabis_bullfrog_themepark_gapyear.mp4": "Архів EP03 #07 • 17 років: Gap Year у Bullfrog і створення Theme Park",
    "ep03_vid_arch_08_act2_24fps_hassabis_neuroscience_brain_goal.mp4": "Архів EP03 #08 • Шлях у когнітивну нейробіологію в UCL (PhD)",
    "ep03_vid_arch_09_act2_24fps_deepmind_solve_intelligence_plan.mp4": "Архів EP03 #09 (Stanford GSB) • Маніфест 2010: «Solve intelligence -> all else»",
    "ep03_vid_arch_10_act2_24fps_deepmind_atari_breakout_tunnel.mp4": "Архів EP03 #10 • Прорив Atari Breakout DQN: тунель за стіною цеглин",
    "ep03_vid_arch_11_act2_24fps_google_650m_deal_military_ethics.mp4": "Архів EP03 #11 • Угода Google $650M: заборона автономної зброї",
    "ep03_vid_arch_12_act3_24fps_alphago_move37_fifth_line_shock.mp4": "Архів EP03 #12 • Хід 37 на 5-й лінії: коментар гросмейстерів Го",
    "ep03_vid_arch_13_act3_24fps_alphafold_200m_proteins_open_data.mp4": "Архів EP03 #13 • Рішення подарувати людству всі 200M білків безкоштовно",
    "ep03_vid_arch_14_act3_24fps_alphafold_protein_fold_60minutes.mp4": "Архів EP03 #14 (CBS 60 Minutes) • AlphaFold: від 1% до 200M структур",
    "ep03_vid_arch_15_act4_24fps_nobel_lecture_casp14_atomic_accuracy.mp4": "Архів EP03 #15 (Nobel 2024) • Графік стрибка AlphaFold 2 на CASP14",
    "ep03_vid_arch_16_act4_24fps_hassabis_agi_horizon_life_moment.mp4": "Архів EP03 #16 • Фінальне бачення AGI на горизонті (Thinking Game)",
    "ep03_img_arch_01_north_london_finchley_youth_era.jpg": "Фотоархів EP03 #01 • Північний Лондон, East Finchley (дитинство Деміса)",
    "ep03_img_arch_02_staunton_chess_board_strategy.jpg": "Фотоархів EP03 #02 • Шахівниця Staunton — перший космос 64 клітинок",
    "ep03_img_arch_03_garde_mechanical_chess_clock.jpg": "Фотоархів EP03 #03 • Механічний турнірний годинник Garde (Ело 2300)",
    "ep03_img_arch_04_sinclair_zx_spectrum_48k_1984.jpg": "Фотоархів EP03 #04 • Sinclair ZX Spectrum 48K (куплений у 8 років)",
    "ep03_img_arch_05_zx_spectrum_48k_keyboard_detail.jpg": "Фотоархів EP03 #05 • Гумова клавіатура ZX Spectrum і код на Z80",
    "ep03_img_arch_06_queens_college_cambridge_gatehouse.jpg": "Фотоархів EP03 #06 • Queens' College, Кембридж (1994–1997)",
    "ep03_img_arch_07_queens_college_mathematical_bridge.jpg": "Фотоархів EP03 #07 • Математичний міст у Queens' College, Кембридж",
    "ep03_img_arch_08_ucl_main_quad_cognitive_neuroscience.jpg": "Фотоархів EP03 #08 • Університетський коледж Лондона (UCL • PhD 2009)",
    "ep03_img_arch_09_demis_hassabis_deepmind_early_talk_2014.jpg": "Фотоархів EP03 #09 • Доповідь про Atari Space Invaders (2014)",
    "ep03_img_arch_10_deepmind_london_hq_kings_cross.jpg": "Фотоархів EP03 #10 • Штаб-квартира Google DeepMind у Лондоні (King's Cross)",
    "ep03_img_arch_11_goban_board_go_move37_strategy.jpg": "Фотоархів EP03 #11 • Дерев'яна дошка гобан з базальтовими каменями Го",
    "ep03_img_arch_12_demis_hassabis_deepmind_era_portrait.jpg": "Фотоархів EP03 #12 • Лекція Деміса Гассабіса на трибуні EPFL",
    "ep03_img_arch_13_alphafold_znf555_protein_structure.jpg": "Фотоархів EP03 #13 • 3D-структура білка ZNF555 з бази AlphaFold",
    "ep03_img_arch_14_alphafold2_transformer_architecture.jpg": "Фотоархів EP03 #14 • Наукова схема Evoformer AlphaFold 2 (CASP14)",
    "ep03_img_arch_15_royal_society_london_carlton_terrace.jpg": "Фотоархів EP03 #15 • Королівське товариство у Лондоні (FRS 2018)",
    "ep03_img_arch_16_nobel_lectures_2024_hassabis_stockholm.jpg": "Фотоархів EP03 #16 • Нобелівська лекція з хімії у Стокгольмі 2024",
    "ep03_img_arch_17_nobel_2024_laureates_hassabis_jumper_baker.jpg": "Фотоархів EP03 #17 • Нобелівські лауреати 2024: Бейкер, Гассабіс, Джампер",
    "ep03_img_arch_18_demis_hassabis_nobel_week_2024_portrait.jpg": "Фотоархів EP03 #18 • Портрет Деміса Гассабіса на Нобелівському тижні",
    "ep03_doc_01_act3_alphago_move37_nature_2016.png": "Досьє EP03 #01 (4K) • Nature 2016: Хід 37 AlphaGo vs Лі Седоль",
    "ep03_doc_02_act1_chess_elo2300_liechtenstein_1990.png": "Досьє EP03 #02 (4K) • Рейтинг Ело 2300 та прозріння в Ліхтенштейні",
    "ep03_doc_03_act1_bullfrog_themepark_1994_specs.png": "Досьє EP03 #03 (4K) • Архітектура мультиагентної гри Theme Park (1994)",
    "ep03_doc_04_act2_pnas_hippocampus_imagination_2007.png": "Досьє EP03 #04 (4K) • PNAS 2007: Пам'ять і уява гіпокампа (UCL)",
    "ep03_doc_05_act3_nature_alphafold2_casp14_2021.png": "Досьє EP03 #05 (4K) • Nature 2021: AlphaFold 2 (92.4 GDT_TS на CASP14)",
    "ep03_doc_06_act4_nobel_chemistry_2024_citation.png": "Досьє EP03 #06 (4K) • Нобелівський диплом з хімії 2024 (Стокгольм)",
    "ep03_ua_clip_card_01_chess_order_10s.mp4": "Цитата EP03 #01 (4K • 10с) • «Космос із 64 клітинок без удачі»",
    "ep03_ua_clip_card_02_zx_spectrum_intuition_10s.mp4": "Цитата EP03 #02 (4K • 10с) • «Чому мозок відчуває позицію, а машина перебирає?»",
    "ep03_ua_clip_card_03_liechtenstein_pivot_10s.mp4": "Цитата EP03 #03 (4K • 10с) • «300 умів мають розгадувати хвороби та Всесвіт»",
    "ep03_ua_clip_card_04_ucl_hippocampus_10s.mp4": "Цитата EP03 #04 (4K • 10с) • «Пам'ять і уява — один механізм гіпокампа»",
    "ep03_ua_clip_card_05_two_step_plan_10s.mp4": "Цитата EP03 #05 (4K • 10с) • «Крок 1: Інтелект. Крок 2: Усе інше»",
    "ep03_ua_clip_card_06_move37_seoul_12s.mp4": "Цитата EP03 #06 (4K • 12с) • «Машинна креативність вільна від 3000 років догм»",
    "ep03_ua_clip_card_07_alphafold_gift_10s.mp4": "Цитата EP03 #07 (4K • 10с) • «Згорнули 200M білків і подарували світу безкоштовно»",
    "ep03_ua_clip_card_08_source_code_finale_12s.mp4": "Цитата EP03 #08 (4K • 12с) • «Життя читає свій вихідний код через телескоп ШІ»",
    "ep03_clip_still_finchley_london_6s.mp4": "Ken Burns (4K • 6с) • Північний Лондон, East Finchley",
    "ep03_clip_still_staunton_chess_6s.mp4": "Ken Burns (4K • 6с) • Дерев'яна шахівниця Staunton",
    "ep03_clip_still_garde_clock_5s.mp4": "Ken Burns (4K • 5с) • Турнірний годинник Garde",
    "ep03_clip_still_zx_spectrum_6s.mp4": "Ken Burns (4K • 6с) • Sinclair ZX Spectrum 48K",
    "ep03_clip_still_zx_keyboard_5s.mp4": "Ken Burns (4K • 5с) • Гумова клавіатура ZX Spectrum",
    "ep03_clip_still_cambridge_gatehouse_6s.mp4": "Ken Burns (4K • 6с) • Брама Queens' College, Кембридж",
    "ep03_clip_still_math_bridge_6s.mp4": "Ken Burns (4K • 6с) • Математичний міст Кембриджа",
    "ep03_clip_still_ucl_main_building_6s.mp4": "Ken Burns (4K • 6с) • Корпус UCL у Лондоні",
    "ep03_clip_still_deepmind_2014_stage_6s.mp4": "Ken Burns (4K • 6с) • Виступ 2014 року про ігри Atari",
    "ep03_clip_still_deepmind_kingscross_6s.mp4": "Ken Burns (4K • 6с) • Офіс Google DeepMind King's Cross",
    "ep03_clip_still_goban_stones_6s.mp4": "Ken Burns (4K • 6с) • Камені Го на дошці гобан",
    "ep03_clip_still_hassabis_epfl_talk_6s.mp4": "Ken Burns (4K • 6с) • Виступ Гассабіса на EPFL",
    "ep03_clip_still_alphafold_znf555_6s.mp4": "Ken Burns (4K • 6с) • 3D білок ZNF555 AlphaFold",
    "ep03_clip_still_alphafold2_diagram_6s.mp4": "Ken Burns (4K • 6с) • Архітектура AlphaFold 2 CASP14",
    "ep03_clip_still_royal_society_london_6s.mp4": "Ken Burns (4K • 6с) • Королівське товариство у Лондоні",
    "ep03_clip_still_nobel_lecture_podium_6s.mp4": "Ken Burns (4K • 6с) • Стокгольм: трибуна Нобелівської лекції",
    "ep03_clip_still_nobel_laureates_trio_6s.mp4": "Ken Burns (4K • 6с) • Тріо Нобелівських лауреатів 2024",
    "ep03_clip_still_hassabis_nobel_week_6s.mp4": "Ken Burns (4K • 6с) • Портрет на Нобелівському тижні 2024",
    # EP04 Geoffrey Hinton Real Archives, Photos, Dossiers, Quote Cards & Ken Burns 4K Stills -> Clean Ukrainian
    "ep04_vid_arch_01_act4_24fps_hinton_nobel_warning_2024.mp4": "Архів EP04 #01 • Застереження на банкеті у Стокгольмі (2024)",
    "ep04_vid_arch_02_act1_24fps_hinton_ancestry_boole_everest.mp4": "Архів EP04 #02 • Родовід: прадід Джордж Буль та сер Джордж Еверест",
    "ep04_vid_arch_03_act1_24fps_hinton_joan_los_alamos_cousin.mp4": "Архів EP04 #03 • Кузина Джоан Хінтон у Манхеттенському проєкті",
    "ep04_vid_arch_04_act2_24fps_hinton_second_ai_winter_turing.mp4": "Архів EP04 #04 (ACM Turing) • Льодовиковий період «Зими ШІ»",
    "ep04_vid_arch_05_act2_24fps_hinton_boltzmann_machine_nobel_lecture.mp4": "Архів EP04 #05 (Nobel 2024) • Пояснення машин Больцмана",
    "ep04_vid_arch_06_act2_24fps_hinton_backpropagation_nobel_lecture.mp4": "Архів EP04 #06 (Nobel 2024) • Алгоритм Backpropagation",
    "ep04_vid_arch_07_act2_24fps_hinton_sejnowski_1980s_neuroscience.mp4": "Архів EP04 #07 (Nobel Interview) • Спільні праці 1980-х із Сейновським",
    "ep04_vid_arch_08_act3_24fps_hinton_two_students_gpus_turing.mp4": "Архів EP04 #08 (ACM Turing) • Ігрові GPU та двоє студентів у Торонто",
    "ep04_vid_arch_09_act3_24fps_hinton_alexnet_dnnresearch_auction.mp4": "Архів EP04 #09 • AlexNet 2012 і таємний аукціон DNNresearch ($44M)",
    "ep04_vid_arch_10_act3_24fps_hinton_turing_2018_three_fathers.mp4": "Архів EP04 #10 • Премія Тюрінга 2018: Хінтон, Лекун та Бенжіо",
    "ep04_vid_arch_11_act3_24fps_hinton_leaving_google_speak_freely.mp4": "Архів EP04 #11 • Відставка з Google 2023 заради свободи слова",
    "ep04_vid_arch_12_act3_24fps_hinton_bbc_regret_warning_2023.mp4": "Архів EP04 #12 (BBC News) • «Хрещений батько ШІ» застерігає людство",
    "ep04_vid_arch_13_act3_24fps_hinton_digital_weights_trillions_bits.mp4": "Архів EP04 #13 • 10 біт/с мови проти трильйонів біт/с ШІ",
    "ep04_vid_arch_14_act3_24fps_hinton_60minutes_species_control.mp4": "Архів EP04 #14 (CBS 60 Minutes) • Скотт Пеллі: ризик втрати контролю",
    "ep04_vid_arch_15_act4_24fps_hinton_uoft_students_nobel_presser.mp4": "Архів EP04 #15 (U of T) • Пресконференція Хінтона в Торонто 2024",
    "ep04_vid_arch_16_act4_24fps_hinton_banquet_existential_threat.mp4": "Архів EP04 #16 (Stockholm) • Екзистенційне застереження королям 2024",
    "ep04_img_arch_01_george_boole_logician_ancestor.jpg": "Фотоархів EP04 #01 • Джордж Буль (1847) — творець алгебри 0 і 1",
    "ep04_img_arch_02_mount_everest_peak_survey_lineage.jpg": "Фотоархів EP04 #02 • Північний схил Евересту (спадщина родини)",
    "ep04_img_arch_03_kings_college_cambridge_front_court.jpg": "Фотоархів EP04 #03 • King's College, Кембридж (1967–1970)",
    "ep04_img_arch_04_london_carpentry_hand_plane_oak.jpg": "Фотоархів EP04 #04 • Сталевий рубанок і стружка (теслярство 1972)",
    "ep04_img_arch_05_university_of_edinburgh_informatics_forum.jpg": "Фотоархів EP04 #05 • Університет Единбурга (PhD з нейромереж)",
    "ep04_img_arch_06_cmu_hamerschlag_hall_pittsburgh.jpg": "Фотоархів EP04 #06 • Університет Карнегі-Меллона (CMU 1982–1987)",
    "ep04_img_arch_07_university_of_toronto_sandford_fleming.jpg": "Фотоархів EP04 #07 • Зимовий корпус Sandford Fleming (Торонто)",
    "ep04_img_arch_08_university_of_toronto_bahen_centre.jpg": "Фотоархів EP04 #08 • Bahen Centre Університету Торонто",
    "ep04_img_arch_09_university_of_toronto_convocation_hall.jpg": "Фотоархів EP04 #09 • Ротонда Convocation Hall у Торонто",
    "ep04_img_arch_10_geoffrey_hinton_toronto_tech_stage.jpg": "Фотоархів EP04 #10 • Джеффрі Хінтон на сцені в Торонто",
    "ep04_img_arch_11_lake_tahoe_dnnresearch_auction_2012.jpg": "Фотоархів EP04 #11 • Stateline, Озеро Тахо (аукціон $44M 2012)",
    "ep04_img_arch_12_three_godfathers_deep_learning_turing_2018.jpg": "Фотоархів EP04 #12 • Троє Хрещених батьків: Бенжіо, Хінтон, Лекун",
    "ep04_img_arch_13_ai_benchmarks_1998_2024_exponential.jpg": "Фотоархів EP04 #13 • Крива стрибка точності ШІ 1998–2024",
    "ep04_img_arch_14_geoffrey_hinton_collision_2023_stage.jpg": "Фотоархів EP04 #14 • Перший виступ після Google на Collision 2023",
    "ep04_img_arch_15_geoffrey_hinton_collision_2024_toronto.jpg": "Фотоархів EP04 #15 • Портрет Джеффрі Хінтона у Торонто 2024",
    "ep04_img_arch_16_hinton_nobel_physics_lectures_2024_stockholm.jpg": "Фотоархів EP04 #16 • Нобелівська лекція з фізики 2024 у Стокгольмі",
    "ep04_img_arch_17_hopfield_hinton_2024_nobel_laureates.jpg": "Фотоархів EP04 #17 • Джон Гопфілд і Джеффрі Хінтон (Нобель 2024)",
    "ep04_img_arch_18_hinton_2024_nobel_prize_conference.jpg": "Фотоархів EP04 #18 • Пресконференція Хінтона в Стокгольмі 2024",
    "ep04_doc_01_act2_hinton_backprop_nature_1986.png": "Досьє EP04 #01 (4K) • Nature 1986: Стаття Backpropagation",
    "ep04_doc_02_act1_bristol_lineage_boole_everest_1947.png": "Досьє EP04 #02 (4K) • Тінь предків (Буль, Еверест) & Столярство",
    "ep04_doc_03_act2_ackley_hinton_sejnowski_boltzmann_1985.png": "Досьє EP04 #03 (4K) • Машини Больцмана 1985 & Торонто",
    "ep04_doc_04_act3_alexnet_imagenet_nips_2012.png": "Досьє EP04 #04 (4K) • AlexNet 2012 & Аукціон на озері Тахо ($44M)",
    "ep04_doc_05_act3_turing_2018_and_google_resignation_2023.png": "Досьє EP04 #05 (4K) • Тюрінг 2018 → Відставка з Google 2023",
    "ep04_doc_06_act4_nobel_physics_2024_stockholm_citation.png": "Досьє EP04 #06 (4K) • Нобель з фізики 2024 (Стокгольм)",
    "ep04_ua_clip_card_01_error_geometry_10s.mp4": "Цитата EP04 #01 (4K • 10с) • «Думка — це геометрія помилки в синапсах»",
    "ep04_ua_clip_card_02_carpenter_honesty_10s.mp4": "Цитата EP04 #02 (4K • 10с) • «Дерево не обдуриш дипломом — матерія чесна»",
    "ep04_ua_clip_card_03_backprop_fuel_10s.mp4": "Цитата EP04 #03 (4K • 10с) • «Помилка стала паливом еволюції розуму»",
    "ep04_ua_clip_card_04_thirty_years_winter_10s.mp4": "Цитата EP04 #04 (4K • 10с) • «Якщо мозок на синапсах — помиляється світ»",
    "ep04_ua_clip_card_05_pentagon_toronto_10s.mp4": "Цитата EP04 #05 (4K • 10с) • «Без грошей Пентагону — лежачи на підлозі Торонто»",
    "ep04_ua_clip_card_06_alexnet_2012_10s.mp4": "Цитата EP04 #06 (4K • 10с) • «За одну ніч 30 років темряви закінчилися»",
    "ep04_ua_clip_card_07_google_exit_regret_12s.mp4": "Цитата EP04 #07 (4K • 12с) • «Не буває, щоб менш розумний вид керував сильнішим»",
    "ep04_ua_clip_card_08_nobel_warning_finale_12s.mp4": "Цитата EP04 #08 (4K • 12с) • «Цивілізацію тримають самотні сумнівники»",
    "ep04_clip_still_george_boole_1847_6s.mp4": "Ken Burns (4K • 6с) • Джордж Буль, прапрадід Хінтона",
    "ep04_clip_still_mount_everest_lineage_6s.mp4": "Ken Burns (4K • 6с) • Північний схил Евересту",
    "ep04_clip_still_cambridge_kingscollege_6s.mp4": "Ken Burns (4K • 6с) • King's College, Кембридж",
    "ep04_clip_still_london_carpentry_plane_6s.mp4": "Ken Burns (4K • 6с) • Рубанок і ясенева стружка 1972",
    "ep04_clip_still_edinburgh_informatics_6s.mp4": "Ken Burns (4K • 6с) • Університет Единбурга",
    "ep04_clip_still_cmu_pittsburgh_6s.mp4": "Ken Burns (4K • 6с) • Кампус CMU у Піттсбурзі",
    "ep04_clip_still_toronto_sandford_fleming_6s.mp4": "Ken Burns (4K • 6с) • Корпус Sandford Fleming, Торонто",
    "ep04_clip_still_toronto_bahen_centre_6s.mp4": "Ken Burns (4K • 6с) • Bahen Centre, Торонто",
    "ep04_clip_still_toronto_convocation_hall_6s.mp4": "Ken Burns (4K • 6с) • Ротонда Convocation Hall, Торонто",
    "ep04_clip_still_hinton_collision_stage_6s.mp4": "Ken Burns (4K • 6с) • Сцена Collision у Канаді",
    "ep04_clip_still_lake_tahoe_2012_6s.mp4": "Ken Burns (4K • 6с) • Озеро Тахо, місце аукціону $44M",
    "ep04_clip_still_three_godfathers_turing_6s.mp4": "Ken Burns (4K • 6с) • Тріо Тюрінга: Бенжіо, Хінтон, Лекун",
    "ep04_clip_still_ai_benchmarks_curve_6s.mp4": "Ken Burns (4K • 6с) • Графік експоненти точності ШІ",
    "ep04_clip_still_hinton_collision_2023_6s.mp4": "Ken Burns (4K • 6с) • Виступ 2023 після виходу з Google",
    "ep04_clip_still_hinton_collision_2024_6s.mp4": "Ken Burns (4K • 6с) • Портрет Хінтона на Collision 2024",
    "ep04_clip_still_hinton_nobel_lecture_6s.mp4": "Ken Burns (4K • 6с) • Нобелівська лекція з фізики 2024",
    "ep04_clip_still_hopfield_hinton_nobel_6s.mp4": "Ken Burns (4K • 6с) • Джон Гопфілд і Джеффрі Хінтон",
    "ep04_clip_still_hinton_stockholm_conf_6s.mp4": "Ken Burns (4K • 6с) • Пресконференція у Стокгольмі 2024",
    "ep05_img_arch_01_paris_1977_opera_youth_era.jpg": "Фотоархів EP05 #01 • Париж 1977 (Епоха дитинства Лекуна)",
    "ep05_img_arch_02_tektronix_475a_oscilloscope_1977.jpg": "Фотоархів EP05 #02 • Осцилограф Tektronix 475A (1977)",
    "ep05_img_arch_03_mos_6502_microprocessor_die.jpg": "Фотоархів EP05 #03 • Кристал процесора MOS 6502",
    "ep05_img_arch_04_esiee_paris_engineering_school.jpg": "Фотоархів EP05 #04 • Інженерна школа ESIEE Paris (1983)",
    "ep05_img_arch_05_sorbonne_paris_phd_campus.jpg": "Фотоархів EP05 #05 • Університет Сорбонна / UPMC (PhD 1987)",
    "ep05_img_arch_06_marvin_minsky_perceptrons_rival.jpg": "Фотоархів EP05 #06 • Марвін Мінський (автор «Персептронів»)",
    "ep05_img_arch_07_bell_labs_holmdel_aerial_1987.jpg": "Фотоархів EP05 #07 • Аерофото Bell Labs Holmdel (1987)",
    "ep05_img_arch_08_bell_labs_holmdel_mirror_building.jpg": "Фотоархів EP05 #08 • Bell Labs Holmdel (батьківщина LeNet)",
    "ep05_img_arch_09_courant_institute_nyu_weaver_hall.jpg": "Фотоархів EP05 #09 • Інститут Куранта NYU (кафедра Лекуна)",
    "ep05_img_arch_10_yann_lecun_minnesota_cnn_lecture.jpg": "Фотоархів EP05 #10 • Лекун біля слайду NIPS 1989 про згортки",
    "ep05_img_arch_11_meta_menlo_park_hq_one_hacker_way.jpg": "Фотоархів EP05 #11 • Meta Menlo Park HQ (пакт FAIR 2013)",
    "ep05_img_arch_12_yann_lecun_data_science_keynote.jpg": "Фотоархів EP05 #12 • Лекція у Парижі (Data Science Summer)",
    "ep05_img_arch_13_yann_lecun_turing_2018_portrait.jpg": "Фотоархів EP05 #13 • Портрет епохи Премії Тюрінга (2018)",
    "ep05_img_arch_14_gutenberg_printing_press_mainz.jpg": "Фотоархів EP05 #14 • Друкарський верстат Гутенберга (відкритий ШІ)",
    "ep05_img_arch_15_cat_physics_animal_locomotion.jpg": "Фотоархів EP05 #15 • Хронофотографія стрибка кота (фізика реальності)",
    "ep05_img_arch_16_yann_lecun_ip_paris_2025_portrait.jpg": "Фотоархів EP05 #16 • Портрет на конференції IP Paris 2025",
    "ep05_img_arch_17_yann_lecun_brussels_eu_summit_2026.jpg": "Фотоархів EP05 #17 • Саміт у Брюсселі 2026 (епоха AMI Labs)",
    "ep05_img_arch_18_sailing_close_hauled_badewind.jpg": "Фотоархів EP05 #18 • Вітрильник курсом бейдевінд проти вітру",
    "ep05_doc_01_act2_lecun_lenet5_ieee_1998.png": "Досьє EP05 #01 (4K) • IEEE 1998: LeNet-5 & MNIST",
    "ep05_doc_02_act1_paris_electronics_esiee_piaget_1974.png": "Досьє EP05 #02 (4K) • Паризька майстерня, ESIEE & Піаже",
    "ep05_doc_03_act2_sorbonne_backprop_minsky_1987.png": "Досьє EP05 #03 (4K) • PhD Сорбонна 1987 & Bell Labs Holmdel",
    "ep05_doc_04_act2_at_t_checks_djvu_svm_wilderness.png": "Досьє EP05 #04 (4K) • 20% чеків США, DjVu & 15 років SVM",
    "ep05_doc_05_act3_meta_fair_pytorch_llama_gutenberg.png": "Досьє EP05 #05 (4K) • Пакт Meta FAIR, PyTorch & LLaMA",
    "ep05_doc_06_act4_turing_2018_jepa_world_models_ami_2026.png": "Досьє EP05 #06 (4K) • Тюрінг 2018 → JEPA & AMI Labs $1.03B",
    "ep05_ua_clip_card_01_soldering_eye_10s.mp4": "Цитата EP05 #01 (4K • 10с) • «Розум почався з першого ока в океані»",
    "ep05_ua_clip_card_02_piaget_constructivism_10s.mp4": "Цитата EP05 #02 (4K • 10с) • «Мозок будує модель світу через фізику (Піаже)»",
    "ep05_ua_clip_card_03_minsky_pencil_10s.mp4": "Цитата EP05 #03 (4K • 10с) • «Мінський довів межу 1 шару — та галузь боялася глибини»",
    "ep05_ua_clip_card_04_lenet_checks_10s.mp4": "Цитата EP05 #04 (4K • 10с) • «Згортки Bell Labs читали кожен п'ятий чек у США»",
    "ep05_ua_clip_card_05_supersonic_exile_10s.mp4": "Цитата EP05 #05 (4K • 10с) • «Надзвуковий винищувач за 15 років до бетонних смуг»",
    "ep05_ua_clip_card_06_gutenberg_openai_10s.mp4": "Цитата EP05 #06 (4K • 10с) • «Відкритий ШІ — це друкарський верстат Гутенберга»",
    "ep05_ua_clip_card_07_cat_vs_llm_12s.mp4": "Цитата EP05 #07 (4K • 12с) • «Домашній кіт розуміє фізику краще за будь-який LLM»",
    "ep05_ua_clip_card_08_close_hauled_finale_12s.mp4": "Цитата EP05 #08 (4K • 12с) • «Курсом бейдевінд під гострим кутом проти вітру»",
    "ep05_clip_still_paris_1977_opera_6s.mp4": "Ken Burns (4K • 6с) • Париж 1977 (ера дитинства)",
    "ep05_clip_still_tektronix_475a_1977_6s.mp4": "Ken Burns (4K • 6с) • Осцилограф Tektronix 475A",
    "ep05_clip_still_mos_6502_die_6s.mp4": "Ken Burns (4K • 6с) • Кристал процесора MOS 6502",
    "ep05_clip_still_esiee_paris_6s.mp4": "Ken Burns (4K • 6с) • Інженерна школа ESIEE Paris",
    "ep05_clip_still_sorbonne_paris_6s.mp4": "Ken Burns (4K • 6с) • Кампус Сорбонни (PhD 1987)",
    "ep05_clip_still_marvin_minsky_6s.mp4": "Ken Burns (4K • 6с) • Марвін Мінський",
    "ep05_clip_still_bell_labs_1987_aerial_6s.mp4": "Ken Burns (4K • 6с) • Bell Labs Holmdel з висоти (1987)",
    "ep05_clip_still_bell_labs_holmdel_6s.mp4": "Ken Burns (4K • 6с) • Дзеркальний Bell Labs Holmdel",
    "ep05_clip_still_courant_nyu_6s.mp4": "Ken Burns (4K • 6с) • Інститут Куранта NYU",
    "ep05_clip_still_lecun_minnesota_cnn_6s.mp4": "Ken Burns (4K • 6с) • Лекун біля слайду NIPS 1989",
    "ep05_clip_still_meta_menlo_park_6s.mp4": "Ken Burns (4K • 6с) • Meta Menlo Park HQ (FAIR)",
    "ep05_clip_still_lecun_data_science_6s.mp4": "Ken Burns (4K • 6с) • Лекція у Парижі",
    "ep05_clip_still_lecun_turing_2018_6s.mp4": "Ken Burns (4K • 6с) • Премія Тюрінга 2018",
    "ep05_clip_still_gutenberg_press_mainz_6s.mp4": "Ken Burns (4K • 6с) • Верстат Гутенберга (Майнц)",
    "ep05_clip_still_cat_animal_locomotion_6s.mp4": "Ken Burns (4K • 6с) • Хронофотографія стрибка кота",
    "ep05_clip_still_lecun_ip_paris_2025_6s.mp4": "Ken Burns (4K • 6с) • IP Paris 2025",
    "ep05_clip_still_lecun_eu_2026_6s.mp4": "Ken Burns (4K • 6с) • Саміт ЄС 2026 (Брюссель)",
    "ep05_clip_still_sailing_badewind_6s.mp4": "Ken Burns (4K • 6с) • Вітрильник курсом бейдевінд",
    "ep06_img_arch_01_gorky_nizhny_novgorod_winter_1986.jpg": "Фотоархів EP06 #01 • Горький (Нижній Новгород), зима дитинства 1986",
    "ep06_img_arch_02_jerusalem_golden_limestone_walls.jpg": "Фотоархів EP06 #02 • Мури Єрусалима 1991–2001",
    "ep06_img_arch_03_jerusalem_old_city_panorama.jpg": "Фотоархів EP06 #03 • Золотий вапняк Єрусалима (панорама)",
    "ep06_img_arch_04_university_college_toronto.jpg": "Фотоархів EP06 #04 • University College (Торонто, 2002)",
    "ep06_img_arch_05_uoft_sandford_fleming_2001_room_4306.jpg": "Фотоархів EP06 #05 • Sandford Fleming UofT (кабінет Хінтона №4306)",
    "ep06_img_arch_06_nvidia_gtx580_gf110_alexnet_die.jpg": "Фотоархів EP06 #06 • Кристал NVIDIA GTX 580 Fermi GF110 (AlexNet)",
    "ep06_img_arch_07_alexnet_cnn_architecture_2012.jpg": "Фотоархів EP06 #07 • Архітектура AlexNet (2012)",
    "ep06_img_arch_08_stanford_university_quad_2012.jpg": "Фотоархів EP06 #08 • Стенфордський університет (постдок 2012)",
    "ep06_img_arch_09_googleplex_google_brain_2014.jpg": "Фотоархів EP06 #09 • Googleplex Маунтін-В'ю (Google Brain 2014)",
    "ep06_img_arch_10_ilya_sutskever_google_brain_stage_2014.jpg": "Фотоархів EP06 #10 • Ілля Суцкевер у команді Google Brain (2014)",
    "ep06_img_arch_11_ilya_sutskever_stanford_solo_2014.jpg": "Фотоархів EP06 #11 • Портрет Іллі Суцкевера на сцені Стенфорда (2014)",
    "ep06_img_arch_12_openai_pioneer_building_sf.jpg": "Фотоархів EP06 #12 • OpenAI Pioneer Building у Сан-Франциско",
    "ep06_img_arch_13_supercomputer_cluster_scaling_laws.jpg": "Фотоархів EP06 #13 • Суперкомп'ютерний кластер (закони масштабу)",
    "ep06_img_arch_14_agi_effigy_retreat_bonfire_2023.jpg": "Фотоархів EP06 #14 • Багаття ретриту (символ неконтрольованого AGI)",
    "ep06_img_arch_15_sutskever_altman_tel_aviv_2023.jpg": "Фотоархів EP06 #15 • Суцкевер і Альтман у Тель-Авіві (2023)",
    "ep06_img_arch_16_tel_aviv_university_ssi_hub.jpg": "Фотоархів EP06 #16 • Тель-Авівський університет (центр SSI)",
    "ep06_img_arch_17_toronto_convocation_hall_2025.jpg": "Фотоархів EP06 #17 • Convocation Hall Торонто (почесний докторат 2025)",
    "ep06_img_arch_18_safe_superintelligence_ssi_monolith.jpg": "Фотоархів EP06 #18 • Логотип Safe Superintelligence Inc. (SSI)",
    "ep06_doc_01_act2_sutskever_alexnet_nips_2012.png": "Досьє EP06 #01 (4K) • NIPS 2012: AlexNet & GPUs",
    "ep06_doc_02_act1_gorky_jerusalem_toronto_room_4306.png": "Досьє EP06 #02 (4K) • Горький → Єрусалим → Кабінет Хінтона №4306",
    "ep06_doc_03_act2_seq2seq_vector_space_googlebrain_2014.png": "Досьє EP06 #03 (4K) • Seq2Seq (Google Brain 2014 / NeurIPS Test of Time)",
    "ep06_doc_04_act3_compression_agatha_christie_scaling_gpt4.png": "Досьє EP06 #04 (4K) • Стиснення, Детектив Агати Крісті & GPT-4",
    "ep06_doc_05_act3_agi_effigy_superalignment_nov2023_rift.png": "Досьє EP06 #05 (4K) • Багаття AGI, Superalignment & Листопад 2023",
    "ep06_doc_06_act4_ssi_monolith_paloalto_telaviv_2026.png": "Досьє EP06 #06 (4K) • Safe Superintelligence (SSI) $32B & Торонто 2025",
    "ep06_ua_clip_card_01_jerusalem_axion_10s.mp4": "Цитата EP06 #01 (4K • 10с) • «Єдина непорушна опора лежить усередині розуму»",
    "ep06_ua_clip_card_02_room4306_toronto_10s.mp4": "Цитата EP06 #02 (4K • 10с) • «Стукіт у двері №4306 і повернення за два дні»",
    "ep06_ua_clip_card_03_seq2seq_vector_10s.mp4": "Цитата EP06 #03 (4K • 10с) • «Seq2Seq стиснула ціле речення у чисту думку»",
    "ep06_ua_clip_card_04_agatha_christie_10s.mp4": "Цитата EP06 #04 (4K • 10с) • «Щоб вгадати вбивцю в романі Крісті, модель симулює світ»",
    "ep06_ua_clip_card_05_scaling_10x_10s.mp4": "Цитата EP06 #05 (4K • 10с) • «Ми збільшували обчислення вдесятеро — і стеля зникала»",
    "ep06_ua_clip_card_06_bonfire_superalignment_10s.mp4": "Цитата EP06 #06 (4K • 10с) • «Безпека надінтелекту не чекає релізів чат-ботів»",
    "ep06_ua_clip_card_07_ssi_scale_in_peace_12s.mp4": "Цитата EP06 #07 (4K • 12с) • «SSI: одна мета і один продукт — масштабування в тиші»",
    "ep06_ua_clip_card_08_silent_sanctuary_finale_12s.mp4": "Цитата EP06 #08 (4K • 12с) • «Зрушення історії народжуються беззвучно в тиші»",
    "ep06_clip_still_gorky_winter_1986_6s.mp4": "Ken Burns (4K • 6с) • Зима в Горькому 1986",
    "ep06_clip_still_jerusalem_walls_6s.mp4": "Ken Burns (4K • 6с) • Мури Єрусалима",
    "ep06_clip_still_jerusalem_panorama_6s.mp4": "Ken Burns (4K • 6с) • Панорама Єрусалима",
    "ep06_clip_still_uoft_university_college_6s.mp4": "Ken Burns (4K • 6с) • University College Торонто",
    "ep06_clip_still_uoft_sandford_fleming_6s.mp4": "Ken Burns (4K • 6с) • Sandford Fleming UofT (№4306)",
    "ep06_clip_still_gtx580_alexnet_die_6s.mp4": "Ken Burns (4K • 6с) • Кристал GTX 580 GF110 (AlexNet)",
    "ep06_clip_still_alexnet_diagram_2012_6s.mp4": "Ken Burns (4K • 6с) • Схема AlexNet (2012)",
    "ep06_clip_still_stanford_quad_2012_6s.mp4": "Ken Burns (4K • 6с) • Стенфордський університет",
    "ep06_clip_still_googleplex_brain_2014_6s.mp4": "Ken Burns (4K • 6с) • Googleplex Маунтін-В'ю",
    "ep06_clip_still_sutskever_googlebrain_2014_6s.mp4": "Ken Burns (4K • 6с) • Суцкевер у Google Brain (2014)",
    "ep06_clip_still_sutskever_stanford_solo_6s.mp4": "Ken Burns (4K • 6с) • Портрет Суцкевера (2014)",
    "ep06_clip_still_openai_pioneer_building_6s.mp4": "Ken Burns (4K • 6с) • OpenAI Pioneer Building SF",
    "ep06_clip_still_scaling_laws_servers_6s.mp4": "Ken Burns (4K • 6с) • Сервери масштабування",
    "ep06_clip_still_agi_effigy_bonfire_6s.mp4": "Ken Burns (4K • 6с) • Вогнище статуї AGI",
    "ep06_clip_still_sutskever_tau_2023_6s.mp4": "Ken Burns (4K • 6с) • Виступ у Тель-Авіві (2023)",
    "ep06_clip_still_tel_aviv_university_6s.mp4": "Ken Burns (4K • 6с) • Тель-Авівський університет",
    "ep06_clip_still_convocation_hall_2025_6s.mp4": "Ken Burns (4K • 6с) • Convocation Hall Торонто (2025)",
    "ep06_clip_still_ssi_monolith_2024_6s.mp4": "Ken Burns (4K • 6с) • Логотип Safe Superintelligence (SSI)",
    "ep07_img_arch_01_san_francisco_victorian_childhood_era.jpg": "Фотоархів EP07 #01 • Вікторіанські будинки Сан-Франциско (1983)",
    "ep07_img_arch_02_tuscan_leather_working_tools.jpg": "Фотоархів EP07 #02 • Тосканські інструменти ремісника шкіри (спадок батька)",
    "ep07_img_arch_03_stanford_university_physics_quad.jpg": "Фотоархів EP07 #03 • Стенфордський квад фізики (2006)",
    "ep07_img_arch_04_princeton_carl_icahn_biophysics_lab.jpg": "Фотоархів EP07 #04 • Лабораторія Карла Айкана в Принстоні",
    "ep07_img_arch_05_princeton_jadwin_hall_physics.jpg": "Фотоархів EP07 #05 • Jadwin Hall у Принстоні (PhD з фізики 2011)",
    "ep07_img_arch_06_retinal_ganglion_neurons_microscopy.jpg": "Фотоархів EP07 #06 • Нейрони сітківки ока під мікроскопом 50x",
    "ep07_img_arch_07_baidu_headquarters_shangdi.jpg": "Фотоархів EP07 #07 • Baidu Шанді (Deep Speech 2, 2014)",
    "ep07_img_arch_08_googleplex_building43_brain_era.jpg": "Фотоархів EP07 #08 • Googleplex Corpus 43 (Google Brain 2015)",
    "ep07_img_arch_09_openai_pioneer_building_sf.jpg": "Фотоархів EP07 #09 • OpenAI Pioneer Building у Сан-Франциско",
    "ep07_img_arch_10_google_tpu_v3_scaling_laws_pod.jpg": "Фотоархів EP07 #10 • Кристали Google TPU v3 (Закони масштабу)",
    "ep07_img_arch_11_claude_shannon_information_theory.jpg": "Фотоархів EP07 #11 • Клод Шеннон (натхнення для імені Claude)",
    "ep07_img_arch_12_anthropic_howard_street_sf_hq.jpg": "Фотоархів EP07 #12 • 500 Howard Street SF (Штаб Anthropic)",
    "ep07_img_arch_13_white_house_ai_ceo_summit_2023.jpg": "Фотоархів EP07 #13 • Саміт ШІ у Білому домі (травень 2023)",
    "ep07_img_arch_14_downing_street_pm_ai_developers_2023.jpg": "Фотоархів EP07 #14 • Переговори на Даунінг-стріт 10 (2023)",
    "ep07_img_arch_15_dario_amodei_techcrunch_disrupt_2023_portrait.jpg": "Фотоархів EP07 #15 • Виступ Даріо Амодея на TechCrunch Disrupt 2023",
    "ep07_img_arch_16_dario_amodei_tokyo_ai_diplomacy_2025.jpg": "Фотоархів EP07 #16 • Саміт ШІ-дипломатії у Токіо (2025)",
    "ep07_img_arch_17_bsl4_containment_asl_protocol.jpg": "Фотоархів EP07 #17 • Біоізоляція BSL-4 (прототип рівнів ASL)",
    "ep07_img_arch_18_cancer_dna_fluorescence_loving_grace.jpg": "Фотоархів EP07 #18 • Флуоресценція ДНК онкоклітин («Машини благодаті»)",
    "ep07_doc_01_act3_amodei_constitutional_ai_2022.png": "Досьє EP07 #01 (4K) • Constitutional AI & Пороги ASL-1..4",
    "ep07_doc_02_act1_sf_leather_princeton_retina_2011.png": "Досьє EP07 #02 (4K) • Шкіра батька, втрата 2006 & Принстон (2011)",
    "ep07_doc_03_act2_scaling_laws_7orders_openai_2020.png": "Досьє EP07 #03 (4K) • Закони масштабу 2020 (7 порядків величини)",
    "ep07_doc_04_act2_silent_exit_anthropic_shannon_2021.png": "Досьє EP07 #04 (4K) • Тихий вихід 2020 → Anthropic PBC & Шеннон",
    "ep07_doc_05_act3_constitutional_ai_mech_interp_2024.png": "Досьє EP07 #05 (4K) • RLAIF & МРТ чорної скриньки Claude 3 (2024)",
    "ep07_doc_06_act4_asl_biosecurity_machines_loving_grace.png": "Досьє EP07 #06 (4K) • Протоколи ASL-4 & «Машини благодаті» (2024)",
    "ep07_ua_clip_card_01_leather_and_illness_10s.mp4": "Цитата EP07 #01 (4K • 10с) • «Світ тримається на ремеслі й крихкому тілі»",
    "ep07_ua_clip_card_02_princeton_retina_2011_10s.mp4": "Цитата EP07 #02 (4K • 10с) • «Сітківка ока — живий біологічний комп'ютер»",
    "ep07_ua_clip_card_03_scaling_laws_line_10s.mp4": "Цитата EP07 #03 (4K • 10с) • «Інтелект виявився прямою крізь 7 порядків»",
    "ep07_ua_clip_card_04_silent_exodus_anthropic_10s.mp4": "Цитата EP07 #04 (4K • 10с) • «Коли перегони втрачають гальма — будуй наново»",
    "ep07_ua_clip_card_05_claude_shannon_prism_10s.mp4": "Цитата EP07 #05 (4K • 10с) • «Конституція ШІ — це прозора призма принципів»",
    "ep07_ua_clip_card_06_mech_interp_microscope_10s.mp4": "Цитата EP07 #06 (4K • 10с) • «Інтерпретованість — це МРТ усередині чорної скриньки»",
    "ep07_ua_clip_card_07_asl_biosecurity_vow_12s.mp4": "Цитата EP07 #07 (4K • 12с) • «На порозі ASL-4 ми зупинимо навчання моделі»",
    "ep07_ua_clip_card_08_loving_grace_finale_12s.mp4": "Цитата EP07 #08 (4K • 12с) • «Стиснути століття біології в 10 років зцілення»",
    "ep07_clip_still_sf_mission_era_6s.mp4": "Ken Burns (4K • 6с) • Сан-Франциско 1983 (дитинство)",
    "ep07_clip_still_tuscan_leather_tools_6s.mp4": "Ken Burns (4K • 6с) • Тосканські інструменти шкіряника",
    "ep07_clip_still_stanford_quad_6s.mp4": "Ken Burns (4K • 6с) • Стенфордський квад фізики",
    "ep07_clip_still_princeton_icahn_6s.mp4": "Ken Burns (4K • 6с) • Лабораторія Карла Айкана, Принстон",
    "ep07_clip_still_princeton_jadwin_6s.mp4": "Ken Burns (4K • 6с) • Jadwin Hall у Принстоні",
    "ep07_clip_still_retinal_ganglion_6s.mp4": "Ken Burns (4K • 6с) • Нейрони сітківки ока (50x)",
    "ep07_clip_still_baidu_shangdi_6s.mp4": "Ken Burns (4K • 6с) • Штаб Baidu (Deep Speech 2)",
    "ep07_clip_still_googleplex43_6s.mp4": "Ken Burns (4K • 6с) • Googleplex Corpus 43",
    "ep07_clip_still_openai_pioneer_6s.mp4": "Ken Burns (4K • 6с) • OpenAI Pioneer Building SF",
    "ep07_clip_still_tpu_v3_scaling_6s.mp4": "Ken Burns (4K • 6с) • Плата Google TPU v3",
    "ep07_clip_still_claude_shannon_6s.mp4": "Ken Burns (4K • 6с) • Портрет Клода Шеннона",
    "ep07_clip_still_anthropic_howard_6s.mp4": "Ken Burns (4K • 6с) • 500 Howard Street SF (Anthropic)",
    "ep07_clip_still_white_house_2023_6s.mp4": "Ken Burns (4K • 6с) • Саміт у Білому домі (2023)",
    "ep07_clip_still_downing_street_2023_6s.mp4": "Ken Burns (4K • 6с) • Даунінг-стріт 10 (2023)",
    "ep07_clip_still_amodei_disrupt_2023_6s.mp4": "Ken Burns (4K • 6с) • Даріо Амодей на Disrupt 2023",
    "ep07_clip_still_amodei_tokyo_2025_6s.mp4": "Ken Burns (4K • 6с) • Саміт ШІ у Токіо (2025)",
    "ep07_clip_still_bsl4_containment_6s.mp4": "Ken Burns (4K • 6с) • Біозахист BSL-4",
    "ep07_clip_still_cancer_fluorescence_6s.mp4": "Ken Burns (4K • 6с) • Флуоресценція ДНК онкоклітин",
    "ep08_img_arch_01_chengdu_sichuan_heritage_street.jpg": "Фотоархів EP08 #01 • Вулиця у Ченду, Сичуань (1976–1992)",
    "ep08_img_arch_02_father_repaired_35mm_camera_lens.jpg": "Фотоархів EP08 #02 • Механічний фотоапарат (ремесло батька)",
    "ep08_img_arch_03_english_chinese_study_dictionary.jpg": "Фотоархів EP08 #03 • Англо-китайський словник (переклад фізики)",
    "ep08_img_arch_04_immigrant_laundry_pressing_steam_silhouette.jpg": "Фотоархів EP08 #04 • Прасування біля вікна в Нью-Джерсі (1992)",
    "ep08_img_arch_05_ormont_cleaners_heavy_iron_press.jpg": "Фотоархів EP08 #05 • Важка гаряча праска хімчистки Ormont Cleaners",
    "ep08_img_arch_06_princeton_nassau_hall_dusk_physics.jpg": "Фотоархів EP08 #06 • Вечірній Nassau Hall (Прінстон 1995–1999)",
    "ep08_img_arch_07_wall_street_nyse_rejected_offers.jpg": "Фотоархів EP08 #07 • Уолл-стріт NYSE (відмова заради науки 1999)",
    "ep08_img_arch_08_caltech_beckman_institute_pasadena.jpg": "Фотоархів EP08 #08 • Інститут Бекмана у Калтеху (PhD 2005)",
    "ep08_img_arch_09_cambrian_trilobite_evolution_eyes.jpg": "Фотоархів EP08 #09 • Скам'янілі трилобіти (Кембрій 540 млн р.)",
    "ep08_img_arch_10_sleeping_cat_computer_vision_challenge.jpg": "Фотоархів EP08 #10 • Згорнутий кіт (криза комп'ютерного зору 2006)",
    "ep08_img_arch_11_stanford_gates_cs_sail_building.jpg": "Фотоархів EP08 #11 • Корпус Gates CS у Стенфорді (SAIL)",
    "ep08_img_arch_12_imagenet_alexnet_error_rate_crash.jpg": "Фотоархів EP08 #12 • Крива зниження похибки ImageNet (2012)",
    "ep08_img_arch_13_googleplex_cloud_ai_2017.jpg": "Фотоархів EP08 #13 • Googleplex (Chief Scientist Google Cloud)",
    "ep08_img_arch_14_feifei_li_ai_for_good_2017_keynote.jpg": "Фотоархів EP08 #14 • Виступ на саміті ООН AI for Good (2017)",
    "ep08_img_arch_15_stanford_hai_roundtable_feifei_li.jpg": "Фотоархів EP08 #15 • Круглий стіл Stanford HAI",
    "ep08_img_arch_16_hospital_bedside_ambient_healthcare_ai.jpg": "Фотоархів EP08 #16 • Лікарняна палата (амбієнтний ШІ милосердя)",
    "ep08_img_arch_17_feifei_li_global_humanitarian_award_2024.jpg": "Фотоархів EP08 #17 • Гуманітарна нагорода Джеймса Моргана (2024)",
    "ep08_img_arch_18_world_labs_3d_spatial_point_cloud.jpg": "Фотоархів EP08 #18 • 3D-хмара точок LiDAR (World Labs 2024)",
    "ep08_doc_01_act2_feifeili_imagenet_cvpr_2009.png": "Досьє EP08 #01 (4K) • ImageNet CVPR 2009 (14M зображень)",
    "ep08_doc_02_act1_chengdu_parsippany_ormont_cleaners_1992.png": "Досьє EP08 #02 (4K) • Ченду → $20 → Пральня Ormont Cleaners",
    "ep08_doc_03_act1_princeton_caltech_neuro_vision_2005.png": "Досьє EP08 #03 (4K) • Благословення матері → Калтех PhD",
    "ep08_doc_04_act2_imagenet_14m_mturk_miami_boycott_2009.png": "Досьє EP08 #04 (4K) • 50K MTurk & Стенд біля туалетів (Маямі)",
    "ep08_doc_05_act3_alexnet_2012_hospital_hai_dignity_2019.png": "Досьє EP08 #05 (4K) • AlexNet 2012 → Stanford HAI & Медицина",
    "ep08_doc_06_act4_world_labs_spatial_intelligence_2024_northstar.png": "Досьє EP08 #06 (4K) • World Labs 3D & Полярна зірка",
    "ep08_ua_clip_card_01_cambrian_eye_540m_10s.mp4": "Цитата EP08 #01 (4K • 10с) • «Кембрійський вибух почався з першого ока»",
    "ep08_ua_clip_card_02_ormont_double_life_10s.mp4": "Цитата EP08 #02 (4K • 10с) • «Прінстон у будні, пара Ormont Cleaners на вихідних»",
    "ep08_ua_clip_card_03_mother_blessing_1999_10s.mp4": "Цитата EP08 #03 (4K • 10с) • «Твоя голова належить науці — іди у Калтех!»",
    "ep08_ua_clip_card_04_dark_basement_data_10s.mp4": "Цитата EP08 #04 (4K • 10с) • «Жоден алгоритм не оживе в підвалі без даних»",
    "ep08_ua_clip_card_05_imagenet_14m_miami_10s.mp4": "Цитата EP08 #05 (4K • 10с) • «50 000 людей зібрали 14M вікон у видимий світ»",
    "ep08_ua_clip_card_06_maternity_ward_alexnet_10s.mp4": "Цитата EP08 #06 (4K • 10с) • «Дзвінок у пологову палату про тріумф AlexNet»",
    "ep08_ua_clip_card_07_hai_human_dignity_12s.mp4": "Цитата EP08 #07 (4K • 12с) • «У центрі кожного алгоритму — гідність людини»",
    "ep08_ua_clip_card_08_spatial_north_star_finale_12s.mp4": "Цитата EP08 #08 (4K • 12с) • «Скарб там, де інші бояться забруднити руки»",
    "ep08_clip_still_chengdu_heritage_6s.mp4": "Ken Burns (4K • 6с) • Вулиця у Ченду",
    "ep08_clip_still_father_camera_lens_6s.mp4": "Ken Burns (4K • 6с) • Камера Minolta 35mm (батько)",
    "ep08_clip_still_english_chinese_dict_6s.mp4": "Ken Burns (4K • 6с) • Англо-китайський словник",
    "ep08_clip_still_laundry_silhouette_6s.mp4": "Ken Burns (4K • 6с) • Силует біля праски 1992",
    "ep08_clip_still_ormont_iron_press_6s.mp4": "Ken Burns (4K • 6с) • Гаряча праска Ormont Cleaners",
    "ep08_clip_still_princeton_nassau_6s.mp4": "Ken Burns (4K • 6с) • Вечірній Nassau Hall, Прінстон",
    "ep08_clip_still_wall_street_nyse_6s.mp4": "Ken Burns (4K • 6с) • NYSE Уолл-стріт (1999)",
    "ep08_clip_still_caltech_beckman_6s.mp4": "Ken Burns (4K • 6с) • Beckman Institute у Калтеху",
    "ep08_clip_still_cambrian_trilobite_6s.mp4": "Ken Burns (4K • 6с) • Скам'янілі трилобіти Кембрію",
    "ep08_clip_still_sleeping_cat_vision_6s.mp4": "Ken Burns (4K • 6с) • Згорнутий кіт у тіні",
    "ep08_clip_still_stanford_gates_cs_6s.mp4": "Ken Burns (4K • 6с) • Gates CS Building, Стенфорд",
    "ep08_clip_still_imagenet_curve_6s.mp4": "Ken Burns (4K • 6с) • Графік похибки ImageNet",
    "ep08_clip_still_googleplex_cloud_2017_6s.mp4": "Ken Burns (4K • 6с) • Googleplex Cloud AI",
    "ep08_clip_still_feifei_aiforgood_2017_6s.mp4": "Ken Burns (4K • 6с) • Трибуна ООН AI for Good 2017",
    "ep08_clip_still_stanford_hai_roundtable_6s.mp4": "Ken Burns (4K • 6с) • Круглий стіл Stanford HAI",
    "ep08_clip_still_hospital_bedside_6s.mp4": "Ken Burns (4K • 6с) • Лікарняна палата (догляд)",
    "ep08_clip_still_humanitarian_award_2024_6s.mp4": "Ken Burns (4K • 6с) • Гуманітарна відзнака 2024",
    "ep08_clip_still_world_labs_3d_lidar_6s.mp4": "Ken Burns (4K • 6с) • 3D LiDAR карта World Labs",
    "EP09_DOC_02_ACT1_paris_mcgill_bell_labs_montreal_1993.mp4": "4K Досьє EP09 #02 • Париж, Макгілл, Bell Labs та УдМ (1964–1993)",
    "EP09_DOC_03_ACT2_word_embeddings_2000_ai_winter_open_lab.mp4": "4K Досьє EP09 #03 • 20 років зими ШІ & Word Embeddings (2000)",
    "EP09_DOC_04_ACT2_attention_2014_gan_mila_refusing_billions.mp4": "4K Досьє EP09 #04 • Механізм Уваги (2014), GAN і Mila",
    "EP09_DOC_05_ACT3_un_ai_safety_report_system2_gflownets.mp4": "4K Досьє EP09 #05 • Звіт безпеки ООН, GFlowNets & Scientist AI",
    "EP09_DOC_06_ACT4_montreal_declaration_conscience_compass.mp4": "4K Досьє EP09 #06 • Монреальська декларація & Кодекс Вартового",
    "ep09_ua_clip_card_01_bicycle_moral_bastion_10s.mp4": "Цитата EP09 #01 (4K • 10с) • «Останній вільний бастіон науки»",
    "ep09_ua_clip_card_02_paris_theatre_asimov_10s.mp4": "Цитата EP09 #02 (4K • 10с) • «У їхньому домі мірилом була глибина думки»",
    "ep09_ua_clip_card_03_ai_winter_family_lab_10s.mp4": "Цитата EP09 #03 (4K • 10с) • «Лабораторія-родина без таємниць і боротьби»",
    "ep09_ua_clip_card_04_word_embeddings_cosmos_10s.mp4": "Цитата EP09 #04 (4K • 10с) • «Слово стало координатою чистого смислу»",
    "ep09_ua_clip_card_05_attention_2014_goodfellow_10s.mp4": "Цитата EP09 #05 (4K • 10с) • «Погляд назад: так народився Attention»",
    "ep09_ua_clip_card_06_not_for_sale_mila_10s.mp4": "Цитата EP09 #06 (4K • 10с) • «Дякую, але я не продаюся акціонерам!»",
    "ep09_ua_clip_card_07_grandson_scientist_ai_12s.mp4": "Цитата EP09 #07 (4K • 12с) • «ШІ-Вчений зупиняється перед 1% ризику»",
    "ep09_ua_clip_card_08_conscience_compass_finale_12s.mp4": "Цитата EP09 #08 (4K • 12с) • «Ми встоїмо, поки є вартові совісті»",
    "ep09_clip_still_paris_latin_quarter_6s.mp4": "Ken Burns (4K • 6с) • Латинський квартал Парижа 1978",
    "ep09_clip_still_paris_theatre_carlo_6s.mp4": "Ken Burns (4K • 6с) • Сцена Théâtre de Paris (батько Карло)",
    "ep09_clip_still_isaac_asimov_books_6s.mp4": "Ken Burns (4K • 6с) • Айзек Азімов та книжки «Фундації»",
    "ep09_clip_still_mcgill_arts_phd_6s.mp4": "Ken Burns (4K • 6с) • Корпус McGill University Arts (1991)",
    "ep09_clip_still_bell_labs_holmdel_6s.mp4": "Ken Burns (4K • 6с) • AT&T Bell Labs Холмдел (1992)",
    "ep09_clip_still_udem_roger_gaudry_6s.mp4": "Ken Burns (4K • 6с) • Університет Монреаля Roger-Gaudry",
    "ep09_clip_still_montreal_winter_skyline_6s.mp4": "Ken Burns (4K • 6с) • Засніжений Монреаль з Мон-Рояль",
    "ep09_clip_still_word_embeddings_board_6s.mp4": "Ken Burns (4K • 6с) • Математична дошка векторів слів",
    "ep09_clip_still_attention_mechanism_6s.mp4": "Ken Burns (4K • 6с) • Схема Encoder Cross-Attention",
    "ep09_clip_still_saint_laurent_mila_6s.mp4": "Ken Burns (4K • 6с) • Бульвар Сен-Лоран / Міле-Екс (Mila)",
    "ep09_clip_still_bengio_open_science_6s.mp4": "Ken Burns (4K • 6с) • Портрет Йошуа Бенжіо за трибуною",
    "ep09_clip_still_gflownet_molecules_6s.mp4": "Ken Burns (4K • 6с) • 3D-молекула пошуку GFlowNets",
    "ep09_clip_still_bengio_iclr_stage_6s.mp4": "Ken Burns (4K • 6с) • Виступ Бенжіо на сцені ICLR",
    "ep09_clip_still_us_capitol_senate_6s.mp4": "Ken Burns (4K • 6с) • Капітолій США у сутінках (Сенат)",
    "ep09_clip_still_bletchley_summit_6s.mp4": "Ken Burns (4K • 6с) • Саміт безпеки AI у Блетчлі-Парку",
    "ep09_clip_still_un_security_council_6s.mp4": "Ken Burns (4K • 6с) • Зала Ради Безпеки ООН",
    "ep09_clip_still_winter_bicycle_quebec_6s.mp4": "Ken Burns (4K • 6с) • Зимовий велосипед на снігу Квебеку",
    "ep09_clip_still_canada_aurora_finale_6s.mp4": "Ken Burns (4K • 6с) • Північне сяйво над Канадою з орбіти",
}

# Verified CLEAN cross-hero rules:
# - ZERO actor faces from EP01, ZERO anime Seedance, ZERO Macintosh/Apple, ZERO foreign text/UI, ZERO previs blueprints.
# - Each video/image inspected across start, middle, and end frames.
CROSS_CURATION_RULES = [
    # ======================== CLEAN ABSTRACT & HARDWARE 4K/1080p VIDEOS (16:9) ========================
    {
        "match": "ep01_clip_v1_12_waferhero_16s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["23", "26", "44"], "reason": "Макро проліт лазера по кремнієвій пластині (4K 16:9, без написів) — виробництво чипів та архітектура CUDA NVIDIA."},
            "05": {"scenes": ["02"], "reason": "Мікроелектроніка та фізична архітектура кремнієвих плат."},
            "06": {"scenes": ["04"], "reason": "Кремнієвий фундамент для глибокого навчання та прискорення матриць."},
        },
    },
    {
        "match": "ep01_clip_v1_16_servercold_8s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Абстрактний холодний коридор дата-центру (4K 16:9, 0 людей) — AI-фабрики NVIDIA."},
            "06": {"scenes": ["07", "10"], "reason": "Чистий обчислювальний моноліт у залі масштабування."},
            "10": {"scenes": ["03"], "reason": "Серверний масив на 1000+ вузлів для проєкту Google Brain."},
        },
    },
    {
        "match": "ep01_flow_06_server_monolith.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["31", "45"], "reason": "Тунель дата-центру переходить у сяючу кремнієву решітку суперкомп'ютера."},
            "06": {"scenes": ["07"], "reason": "Архітектура великого обчислювального кластера."},
        },
    },
    {
        "match": "ep01_v1_creative_06_obsessive_builders_14s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["31", "45"], "reason": "Темний дата-центр із велетенською серверною вежею GPU (безіменний загальний план 4K)."},
            "06": {"scenes": ["05", "07"], "reason": "Інженери в закритій обчислювальній залі перед масштабуванням моделі."},
            "10": {"scenes": ["03"], "reason": "Лабораторія великомасштабних експериментів Google X."},
        },
    },
    {
        "match": "ep01_v1_b2_06_server_matrix_billions_15s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["44", "45", "50"], "reason": "Сфера Дайсона із серверних GPU-плат навколо зорі (4K, без облич/тексту) — планетарна інфраструктура NVIDIA."},
            "06": {"scenes": ["07"], "reason": "Метафора десятикратного енергетичного та обчислювального масштабування."},
            "07": {"scenes": ["04"], "reason": "Енергетичний масштаб законів масштабування (Scaling Laws)."},
        },
    },
    {
        "match": "ep01_clip_v1_19_curvehero_17s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["30", "39"], "reason": "Чиста золота експоненційна крива в космосі (4K 16:9, без жодного слова) — прорив NVIDIA."},
            "06": {"scenes": ["07"], "reason": "Степенева крива масштабування інтелекту."},
            "07": {"scenes": ["04"], "reason": "Пряма логарифмічна лінія Законів Масштабування на 7 порядках величини (2020)."},
        },
    },
    {
        "match": "neuron_morphs_into_gpu_chip_23314d03",
        "kind": "video",
        "targets": {
            "01": {"scenes": ["28", "46"], "reason": "Чистий морф біологічного нейрона -> нічний ЦОД -> глобальна мережа (без облич)."},
            "02": {"scenes": ["29", "44", "45"], "reason": "Нейрон стає обчислювальним центром і мережею світу (1080p 16:9) — AlexNet на GPU NVIDIA та глобальні AI-фабрики."},
            "04": {"scenes": ["07"], "reason": "Торонто 2012: біологічна ідея нейромережі Хінтона переноситься на обчислювальні кластери."},
            "05": {"scenes": ["07"], "reason": "Обчислювальний фундамент сучасного Deep Learning."},
            "06": {"scenes": ["04"], "reason": "Масштабування нейронних систем на графічних кластерах."},
            "10": {"scenes": ["03"], "reason": "Глобальний масштаб навчання без нагляду на тисячах машин."},
        },
    },
    {
        "match": "ep01_v1_creative_08_gold_melting_brain_15s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["25", "39"], "reason": "Золото переплавляється в нейронний мозок (4K абстракт) — шлях від IPO до 3-трильйонної вартості."},
            "07": {"scenes": ["04"], "reason": "Конвертація ресурсів у чисту обчислювальну потужність."},
        },
    },
    {
        "match": "ep01_v1_creative_07_golden_transistor_dust_8s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["21", "23", "31"], "reason": "Золоте транзисторне рукостискання (без облич) — союз із Sega / TSMC / OpenAI."},
            "03": {"scenes": ["40"], "reason": "Стратегічне технологічне партнерство 2014 року."},
            "05": {"scenes": ["07"], "reason": "Науковий альянс навколо відкритого коду FAIR та PyTorch."},
        },
    },
    {
        "match": "ep01_clip_v1_07_phosphor_12s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["22"], "reason": "Абстрактні зелені субпіксельні решітки в 4K — народження 3D-рендерингу."},
            "05": {"scenes": ["04", "05"], "reason": "Матриця пікселів як вхідні канали згорткової мережі LeNet-5."},
            "08": {"scenes": ["04"], "reason": "Базова цифрова матриця зображення перед класифікацією."},
        },
    },
    {
        "match": "electrical_spark_traveling_neuro",
        "kind": "video",
        "targets": {
            "01": {"scenes": ["28"], "reason": "Абстрактний розряд нейрона, що переходить у багатошарову мережу."},
            "04": {"scenes": ["04", "05"], "reason": "Синаптичний імпульс -> штучна багатошарова мережа (1080p 16:9) — ілюстрація Backpropagation."},
            "05": {"scenes": ["04"], "reason": "Від біологічних рецепторів до згорткових шарів."},
            "07": {"scenes": ["03"], "reason": "Лабораторія Прінстона: підслуховування сигналів живих нейронів."},
            "09": {"scenes": ["02", "04"], "reason": "Імпульс у нейронній структурі як фундамент досліджень у Монреалі."},
        },
    },
    {
        "match": "ep01_flow_05_neural_lattice.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["33", "34"], "reason": "Абстрактна 3D-решітка нейронів у русі (16:9)."},
            "04": {"scenes": ["05"], "reason": "Спалахи ваг у глибоких прихованих шарах нейромережі."},
            "05": {"scenes": ["05", "07"], "reason": "Динамічна нейронна мережа розпізнавання образів."},
            "06": {"scenes": ["04"], "reason": "Векторні шари глибоких моделей послідовностей."},
            "09": {"scenes": ["04", "05"], "reason": "Багатовимірна мережа зважених зв'язків слів."},
        },
    },
    {
        "match": "ep01_v1_creative_01_equations_void_8s.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Золоті математичні рівняння в космічній безодні (4K, без облич) — формули градієнтного спуску."},
            "06": {"scenes": ["02", "04"], "reason": "Занурення у чисті математичні закономірності."},
            "07": {"scenes": ["04"], "reason": "Степеневі закони обчислень у просторі рівнянь."},
            "09": {"scenes": ["04", "09"], "reason": "Простір імовірнісних потоків (GFlowNets) та векторної математики."},
        },
    },
    {
        "match": "ep01_v1_creative_02_galaxies_axons_12s.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["47", "50"], "reason": "Космічні галактики, поєднані золотими синаптичними нитками (4K абстракт)."},
            "04": {"scenes": ["05"], "reason": "Всесвіт розподілених уявлень пам'яті."},
            "06": {"scenes": ["04", "07"], "reason": "Багатовимірний семантичний простір думок."},
            "09": {"scenes": ["04"], "reason": "Сузір'я слів-векторів у семантичному космосі Бенжіо (2000)."},
        },
    },
    {
        "match": "ep01_v1_creative_04_mind_radiating_light_12s.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["05", "09"], "reason": "Абстрактна скляна скульптура розуму випромінює золоте світло в обсидіановий кристал (4K)."},
            "06": {"scenes": ["06", "08"], "reason": "Діалог між людською інтуїцією та синтетичним розумом."},
            "07": {"scenes": ["08"], "reason": "Просвічування прихованих фіч усередині моделі Claude 3."},
            "09": {"scenes": ["09"], "reason": "Усвідомлена архітектура мислення (Система 2)."},
        },
    },
    {
        "match": "ep01_v1_b3_03_two_silhouettes_nadella_12s.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["08"], "reason": "Два чисті темні силуети без облич обмінюються золотими хвилями думок (4K)."},
            "06": {"scenes": ["05", "09"], "reason": "Інтелектуальний резонанс та співпраця вчених."},
            "07": {"scenes": ["05"], "reason": "Спільне бачення брата й сестри Амодей."},
            "09": {"scenes": ["05"], "reason": "Точна метафора Механізму Уваги (Attention) Богданова–Чо–Бенжіо 2014."},
        },
    },
    {
        "match": "ep01_v1_b2_03_singularity_threat_12s.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["09", "10"], "reason": "Абстрактне руйнування скляного купола перед порталом сингулярності (4K) — застереження Хінтона."},
            "06": {"scenes": ["08", "10"], "reason": "Стихія неконтрольованого масштабу та потреба в безпечному SSI."},
            "07": {"scenes": ["06", "09"], "reason": "Коли потужність двигуна вимагає надійних гальм безпеки."},
            "09": {"scenes": ["08"], "reason": "Наукова тривога перед глобальними ризиками ШІ."},
        },
    },
    {
        "match": "ep01_flow_08_golden_signatures.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["49", "50"], "reason": "Чисте золоте сяйво конвергенції наукових відкриттів (16:9)."},
            "06": {"scenes": ["04"], "reason": "Згортка векторів думки в єдиний смисловий центр."},
            "07": {"scenes": ["07"], "reason": "Узгодження параметрів навколо єдиних етичних принципів."},
            "09": {"scenes": ["08"], "reason": "Єдність міжнародної наукової спільноти заради безпеки."},
            "10": {"scenes": ["10"], "reason": "Чисте світло знань на світанку фіналу Сезону."},
        },
    },
    {
        "match": "ep01_v1_b3_04_golden_grid_stabilizing_15s.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["45", "47"], "reason": "Золота координатна сфера вгамовує океанський циклон (4K) — прогнозування погоди GraphCast."},
            "07": {"scenes": ["06", "09"], "reason": "Захисна координатна сітка стандартів безпеки ASL-1..4."},
            "09": {"scenes": ["07", "08"], "reason": "Глобальна кліматична та безпекова координація інституту Mila й ООН."},
        },
    },
    {
        "match": "ep01_v1_b2_10_earth_horizon_finale_550f.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Планета Земля у золотих світлових артеріях обчислень (4K, 23s, без дублів)."},
            "03": {"scenes": ["47", "49"], "reason": "Подарунок 200 мільйонів білкових структур усьому людству."},
            "09": {"scenes": ["08"], "reason": "Планетарна відповідальність фундаментальної науки."},
            "10": {"scenes": ["06", "07", "10"], "reason": "Глобальне охоплення Coursera та «нова електрика» у кожному домі."},
        },
    },
    {
        "match": "ep01_v1_b2_08_silicon_metropolis_14s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Місто трансформується у тривимірні золоті схеми (4K) — цифровий двійник світу NVIDIA."},
            "10": {"scenes": ["07", "10"], "reason": "Економічна трансформація індустрій через повсюдний ШІ."},
        },
    },
    {
        "match": "physical_matter_dissolves_into_b_clip_f843df4f_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Реальний мегаполіс на узбережжі перетікає в золоту обчислювальну сферу (1080p 16:9)."},
            "05": {"scenes": ["08", "09"], "reason": "Переклад фізичної реальності у внутрішню модель світу (JEPA)."},
            "08": {"scenes": ["09"], "reason": "Просторове тривимірне моделювання фізичного світу."},
            "10": {"scenes": ["07"], "reason": "Електрифікація сучасної економіки алгоритмами."},
        },
    },
    {
        "match": "light_point_explodes_into_streaks_0827d703_1080p.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Золоте перо запалює папір і формує мапу глобальної науки (без чужих облич) — стаття в Nature 1986."},
            "05": {"scenes": ["05"], "reason": "Публікація IEEE 1998 про згорткові мережі LeNet-5."},
            "07": {"scenes": ["07", "10"], "reason": "Конституційний маніфест та трактат про медицину й біологію."},
            "09": {"scenes": ["08"], "reason": "Складання Міжнародного наукового звіту про безпеку ШІ."},
        },
    },
    {
        "match": "camera_plunges_into_terminal_screen_11075f8d_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["26", "46"], "reason": "Занурення крізь нейтральний ноутбук у тунель обчислювальної архітектури (1080p)."},
            "05": {"scenes": ["07"], "reason": "Потік інженерного коду відкритих бібліотек."},
            "06": {"scenes": ["04"], "reason": "Код тренування глибоких векторних мереж."},
            "10": {"scenes": ["01", "10"], "reason": "Десять рядків коду щодня — вхід у світ алгоритмічного мислення."},
        },
    },
    {
        "match": "ep01_v1_b2_04_robotic_dexterity_15s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Роботизовані маніпулятори сплітають золоту мережу в повітрі (4K) — фізика NVIDIA Isaac/GR00T."},
            "05": {"scenes": ["08", "09"], "reason": "Втілений інтелект та взаємодія з фізичним простором."},
            "08": {"scenes": ["09", "10"], "reason": "Просторова інженерія та робототехніка World Labs."},
        },
    },
    {
        "match": "ep01_v1_creative_05_holo_geo_matrix_16s.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["46", "47"], "reason": "Голографічна геометрична мапа морфує в біологічну й просторову мережу (4K)."},
            "05": {"scenes": ["09"], "reason": "Внутрішня топологія світу без зайвих слів."},
            "08": {"scenes": ["05", "09"], "reason": "Ієрархія об'єктів та тривимірна геометрія середовища."},
            "10": {"scenes": ["08"], "reason": "Чиста структурована інженерія даних (Data-Centric AI)."},
        },
    },
    {
        "match": "glass_shatters_into_voxel_bricks_6403835d_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Світ розкривається на 3D-вокселі й голографічну галерею (1080p 16:9, силует спиною)."},
            "05": {"scenes": ["09"], "reason": "Розкладання реальності на 3D-структуру для JEPA."},
            "08": {"scenes": ["09"], "reason": "Вихід із пласких 2D-пікселів у тривимірний простір World Labs."},
        },
    },
    {
        "match": "ep01_v1_assoc_01_lidar_city_grid_8s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45", "50"], "reason": "Абстрактна бірюзова LiDAR-сітка сканує міський квартал у темряві (4K)."},
            "05": {"scenes": ["05", "09"], "reason": "Комп'ютерне бачення та геометрія вулиці в реальному часі."},
            "08": {"scenes": ["05", "09"], "reason": "3D-сканування простору для Spatial Intelligence."},
        },
    },
    {
        "match": "ep01_v1_b2_05_swarm_gaming_rl_12s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["16", "45"], "reason": "Рій лазерних ігрових геометричних юнітів у симуляції (4K абстракт)."},
        },
    },
    {
        "match": "digital_hud_tracking_vehicles_d7d30811_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Телеметрія автопілота та розпізнавання об'єктів (без облич акторів)."},
            "05": {"scenes": ["05"], "reason": "Прикладне комп'ютерне бачення на основі згорткових мереж."},
            "08": {"scenes": ["04", "05"], "reason": "Візуальна детекція об'єктів у реальному середовищі (спадщина ImageNet)."},
            "10": {"scenes": ["02"], "reason": "Сенсорна навігація та автономний зір у повітрі й місті."},
        },
    },
    {
        "match": "aerial_view_of_city_center_41b81743_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Оптичне сканування великого міста з повітря (1080p)."},
            "08": {"scenes": ["05", "09"], "reason": "Панорамне просторове сприйняття міської сцени."},
            "10": {"scenes": ["02"], "reason": "Політ автономного апарату над міським рельєфом."},
        },
    },
    {
        "match": "ep01_v1_b2_01_retro_cellular_14s.mp4",
        "kind": "video",
        "targets": {
            "03": {"scenes": ["46", "50"], "reason": "Золоті нитки репарації живої клітини (4K) — AlphaFold та Isomorphic Labs."},
            "07": {"scenes": ["02", "10"], "reason": "Точний 4K візуал для медичного трактату Даріо Амодея (лікування хвороб)."},
            "08": {"scenes": ["08"], "reason": "Технологічний захист здоров'я людини в лікарнях."},
        },
    },
    {
        "match": "ep01_flow_09_fusion_torus.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Термоядерний реактор як джерело гігаватної енергії майбутнього."},
            "03": {"scenes": ["48"], "reason": "Приборкання плазми в токамаку — проєкт DeepMind."},
        },
    },
    {
        "match": "ep08_sci_01_asteroid_approaching_earth_orbit_1080p.mp4",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["09", "10"], "reason": "Метафора наближення екзистенційної загрози в попередженні Хінтона (1080p 16:9)."},
            "07": {"scenes": ["09"], "reason": "Небезпека неконтрольованих біо- чи кіберризиків."},
            "09": {"scenes": ["08"], "reason": "Цивілізаційний ризик у доповіді Йошуа Бенжіо."},
        },
    },
    {
        "match": "ep01_v1_b2_07_corporate_transmutation_15s.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["18", "19"], "reason": "Абстрактний силует спиною перед гравітаційним вихором (4K) — момент «30 днів до банкрутства»."},
            "06": {"scenes": ["10"], "reason": "Крок у невідомість перед масштабами майбутнього."},
        },
    },
    {
        "match": "finger_slamming_clock_plunger_dd1a4152_1080p.mp4",
        "kind": "video",
        "targets": {
            "02": {"scenes": ["18", "24"], "reason": "Натиск таймера -> золоті шестерні часу (без шахів у 2-3 кадрі!) — «До банкрутства рівно 30 днів»."},
            "07": {"scenes": ["06", "09"], "reason": "Невблаганний відлік перегонів безпеки проти швидкості."},
        },
    },

    # ============== RARE 100%-BIOGRAPHICAL MATCHES (STRICTLY ONLY MATCHING HERO) ==============
    {
        "match": "plane_blade_transforming_into_ci",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["03"], "reason": "100% біографія Джеффрі Хінтона: столярний рубанок у лондонській майстерні перетворюється на мікросхему!"},
        },
    },
    {
        "match": "timber_dissolving_into_crystal_m",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["03", "04"], "reason": "Деревина перетворюється на кристалічну решітку — перехід Хінтона від теслі до нейронауки."},
        },
    },
    {
        "match": "carpenters_plane_making_oak_shaving",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["03"], "reason": "Робота рубанком і дубова стружка: лондонська столярна майстерня Джеффрі Хінтона."},
        },
    },
    {
        "match": "camera_glides_over_glassy_water_87530444",
        "kind": "video",
        "targets": {
            "04": {"scenes": ["02"], "reason": "Історичний кампус Кембриджа на світанку — студентські роки Хінтона."},
        },
    },
    {
        "match": "gothic_library_interior_with_boo",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["02"], "reason": "Кембриджські академічні зали — пошуки природи пам'яті."},
            "08": {"scenes": ["02"], "reason": "Класичні зали Прінстонського університету."},
            "09": {"scenes": ["01"], "reason": "Фундаментальні бібліотеки філософії та математики."},
        },
    },
    {
        "match": "ep01_v2_b2_03_altman_sutskever_tau_10s.mp4",
        "kind": "video",
        "targets": {
            "06": {"scenes": ["05", "09"], "reason": "АРХІВНЕ ВІДЕО (TAU 2023): реальний спільний виступ Іллі Суцкевера та Сема Альтмана."},
        },
    },
    {
        "match": "altman_ilya_sutskever_tau_2023",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["05", "09"], "reason": "ІСТОРИЧНЕ ФОТО (TAU 2023): Ілля Суцкевер та Сем Альтман на одній сцені."},
        },
    },
    {
        "match": "ep01_clip_still_sutskever_regret_doc_4s.mp4",
        "kind": "video",
        "targets": {
            "06": {"scenes": ["09"], "reason": "ІСТОРИЧНЕ ДОСЬЄ: офіційний допис Іллі Суцкевера про жаль від 20 листопада 2023."},
        },
    },
    {
        "match": "ep01_doc_04_act3_sutskever_regret_post",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["09"], "reason": "4K ПЛАШКА ДОСЬЄ: твіт Іллі Суцкевера «I deeply regret my participation...»."},
        },
    },
    {
        "match": "ep01_clip_still_730_letter_doc_9s.mp4",
        "kind": "video",
        "targets": {
            "06": {"scenes": ["09"], "reason": "АРХІВНИЙ ЛИСТ: 730+ співробітників OpenAI включно з підписом Іллі Суцкевера."},
        },
    },
    {
        "match": "ep01_doc_05_act3_730_employees",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["09"], "reason": "4K ДОСЬЄ: ультиматум ради директорів OpenAI з підписом Суцкевера."},
        },
    },
    {
        "match": "ep01_doc_02_act2_openai_introducing",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["05"], "reason": "4K ДОСЬЄ: маніфест заснування OpenAI 2015 року, де Суцкевер став головним науковцем."},
        },
    },

    # ============== SPECIFIC 9:16 SCIENTIFIC ANIMATIONS (EXPLICITLY TAGGED AS 9:16) ==============
    {
        "match": "ep01_sci_01_supersonic_prandtl_glauert",
        "kind": "video",
        "targets": {
            "05": {"scenes": ["01", "06"], "reason": "📐 [9:16 Вертикальне VFX] Надзвуковий літак — пряма метафора сцени #06 Лекуна («аж поки не прилетів надзвуковий літак»)."},
        },
    },
    {
        "match": "ep03_sci_01_rna_polymerase_dna",
        "kind": "video",
        "targets": {
            "07": {"scenes": ["02", "10"], "reason": "📐 [9:16 Вертикальне VFX] 3D транскрипція ДНК — наукова метафора стиснення століття біомедицини (Амодей)."},
        },
    },
    {
        "match": "ep07_sci_01_camera_traversing_human_retina",
        "kind": "video",
        "targets": {
            "05": {"scenes": ["04"], "reason": "📐 [9:16 Вертикальне VFX] Анатомія зорової сітківки та передачі оптичного сигналу (Лекун)."},
            "08": {"scenes": ["04", "10"], "reason": "📐 [9:16 Вертикальне VFX] Живий зір людини як орієнтир комп'ютерного зору (Фей-Фей Лі)."},
        },
    },
    {
        "match": "human_zygote_cell_division_timel",
        "kind": "video",
        "targets": {
            "07": {"scenes": ["03", "10"], "reason": "📐 [9:16 Вертикальне VFX] Поділ клітини — біофізика живих систем (Трактат Даріо Амодея)."},
        },
    },

    # ======================== CLEAN 2K/4K ABSTRACT & SCIENTIFIC IMAGES ========================
    {
        "match": "dxf_g.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["26", "44"], "reason": "Золоті світлові траси на материнській платі (без логотипів) — CUDA та GPU."},
            "05": {"scenes": ["02"], "reason": "Травлення електронних плат та імпульси обчислень."},
            "06": {"scenes": ["04"], "reason": "Швидкісні матричні тракти обчислень."},
            "10": {"scenes": ["07"], "reason": "Кремнієві артерії нової індустріальної електрифікації."},
        },
    },
    {
        "match": "bhnuyvtf.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["23", "31", "46"], "reason": "Двоє інженерів тестують GPU-сервер у лабораторії (безіменний індустріальний 2K кадр)."},
            "06": {"scenes": ["04", "07"], "reason": "Апаратний тест обчислювальної стійки."},
            "08": {"scenes": ["07"], "reason": "Лабораторна підтримка запуску глибоких моделей."},
            "10": {"scenes": ["03"], "reason": "Перевірка обладнання Google Brain."},
        },
    },
    {
        "match": "dv.png",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Формула функції втрат Cost Function J(w,b) на скляній дошці — градієнтний спуск."},
            "05": {"scenes": ["03"], "reason": "Оптимізація градієнта на білій дошці."},
            "09": {"scenes": ["04"], "reason": "Математичне виведення втрат мережі."},
            "10": {"scenes": ["05", "06"], "reason": "100% ЗБІГ: фірмова формула Ендрю Ина COST FUNCTION J(w,b) з легендарного курсу CS229 та Coursera!"},
        },
    },
    {
        "match": "cdwrf.png",
        "kind": "image",
        "targets": {
            "03": {"scenes": ["34"], "reason": "Детальний 2K макро-нейрон зі синаптичними спалахами."},
            "04": {"scenes": ["04", "05"], "reason": "Біологічний нейрон, роботу якого Хінтон моделював 50 років."},
            "05": {"scenes": ["04"], "reason": "Ієрархічні нейрони кори головного мозку."},
            "07": {"scenes": ["03"], "reason": "Живі нейрони під мікроскопом у лабораторії Прінстона."},
            "09": {"scenes": ["04"], "reason": "Синаптична структура зв'язків мозку."},
        },
    },
    {
        "match": "ep01_flow_img_03_silicon_wafer_cyan_laser_hero",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["23", "26"], "reason": "Стартовий 2K кадр для сцен проектування архітектури чипів та CUDA."},
            "05": {"scenes": ["02"], "reason": "Мікроелектронна доріжка під лазерним променем."},
            "06": {"scenes": ["04"], "reason": "Кремнієвий тракт матричних обчислень."},
        },
    },
    {
        "match": "ep01_flow_img_04_golden_exponential_curve_hero",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["30"], "reason": "Золота експонента зростання екосистеми CUDA."},
            "06": {"scenes": ["07"], "reason": "Експонента законів масштабування."},
            "07": {"scenes": ["04"], "reason": "Степенева крива Законів Масштабування на 7 порядках."},
        },
    },
    {
        "match": "ep01_flow_img_05_neural_lattice_glowing_nodes_2k",
        "kind": "image",
        "targets": {
            "03": {"scenes": ["33", "34"], "reason": "Чиста геометрична нейронна решітка активації."},
            "04": {"scenes": ["05"], "reason": "2K кадр багатошарової нейромережі для Backpropagation."},
            "05": {"scenes": ["05", "07"], "reason": "Вузли глибокої згорткової архітектури."},
            "06": {"scenes": ["04", "07"], "reason": "Граф векторного представлення сенсів."},
            "08": {"scenes": ["07"], "reason": "Прорив глибоких візуальних мереж 2012."},
            "09": {"scenes": ["04", "05"], "reason": "Координатна решітка токенів і механізму уваги."},
        },
    },
    {
        "match": "ep01_flow_img_06_supercomputer_servers_cold_hall_2k",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["31", "45"], "reason": "Холодний суперкомп'ютерний коридор NVIDIA DGX/Blackwell (2K)."},
            "06": {"scenes": ["07"], "reason": "Обчислювальний кластер великих моделей."},
            "10": {"scenes": ["03"], "reason": "Масив із 1000 серверів Google Brain."},
        },
    },
    {
        "match": "ep01_flow_img_08_golden_signatures_light_threads_2k",
        "kind": "image",
        "targets": {
            "03": {"scenes": ["49"], "reason": "Золотий резонанс наукової спадщини (2K)."},
            "06": {"scenes": ["04"], "reason": "Згортка сенсів у векторному просторі."},
            "07": {"scenes": ["07"], "reason": "Синхронізація етичних орієнтирів."},
            "09": {"scenes": ["08"], "reason": "Глобальна наукова солідарність."},
        },
    },
    {
        "match": "ep01_flow_img_09_fusion_torus_plasma_2k",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Термоядерна енергетика для надпотужних ЦОД."},
            "03": {"scenes": ["48"], "reason": "Токамак термоядерної плазми для керування полем DeepMind."},
        },
    },
    {
        "match": "ep01_flow_img_10_earth_horizon_neural_grid_2k",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Планетарна обчислювальна інфраструктура (2K)."},
            "09": {"scenes": ["08"], "reason": "Глобальна відповідальність людства."},
            "10": {"scenes": ["06", "10"], "reason": "Світло освіти Coursera в кожному домі на Землі."},
        },
    },
    {
        "match": "kjh.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["45", "50"], "reason": "Футуристичний тунель серверних стійок."},
            "06": {"scenes": ["07"], "reason": "Архітектура надвеликих кластерів."},
            "10": {"scenes": ["03"], "reason": "Глибина обчислювальної системи Google X."},
        },
    },
    {
        "match": "b_cgbxtd.png",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Абстрактний силует перед багатовимірним потоком даних."},
            "09": {"scenes": ["04"], "reason": "Занурення у семантичний тунель значень слів."},
        },
    },
    {
        "match": "scesxcsr.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Планета Земля у золотих орбітах цифрового двійника."},
            "07": {"scenes": ["10"], "reason": "Глобальний ефект медичних проривів для всього людства."},
            "09": {"scenes": ["08"], "reason": "Міжнародні кліматичні й безпекові ініціативи."},
            "10": {"scenes": ["06", "10"], "reason": "Світове поширення онлайн-освіти та індустрії ШІ."},
        },
    },
    {
        "match": "vscds.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Глобальна нейромережа зв'язків над континентами."},
            "09": {"scenes": ["07", "08"], "reason": "Світова наукова мережа дослідників Mila."},
            "10": {"scenes": ["06"], "reason": "Слухачі Coursera по всій планеті."},
        },
    },
    {
        "match": "ybr.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["50"], "reason": "Світова мапа технологічної інфраструктури."},
            "08": {"scenes": ["06"], "reason": "Глобальна мережа тисяч асистентів розмітки ImageNet."},
            "10": {"scenes": ["06", "07"], "reason": "Масштабування знань і «нової електрики» по всьому світу."},
        },
    },
    {
        "match": "xasdwrc.png",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Золоте перо на папері — епохальна стаття в Nature 1986."},
            "05": {"scenes": ["05"], "reason": "Фундаментальна публікація IEEE про LeNet-5."},
            "07": {"scenes": ["07", "10"], "reason": "Написання принципів Constitutional AI та Трактату 2024."},
            "09": {"scenes": ["08"], "reason": "Фіксація наукових висновків у Звіті безпеки ШІ."},
        },
    },
    {
        "match": "jlgyf.png",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["33"], "reason": "Ноутбук із чистим кодом на дерев'яному столі вранці (без чужих брендів)."},
            "10": {"scenes": ["10"], "reason": "Чистий файл і перші десять рядків коду на світанку."},
        },
    },
    {
        "match": "mathematical_decision_tree_in_space",
        "kind": "image",
        "targets": {
            "03": {"scenes": ["06", "42"], "reason": "Золоте математичне дерево варіантів у просторі."},
            "04": {"scenes": ["05"], "reason": "Дерево обчислення градієнтів."},
            "06": {"scenes": ["04"], "reason": "Дерево пошуку варіантів у векторних моделях."},
            "09": {"scenes": ["09"], "reason": "Розгалуження думки в архітектурах System 2."},
        },
    },
    {
        "match": "electrical_pulses_firing_through",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["45"], "reason": "Сяючий тунель дата-центру в 2K."},
            "06": {"scenes": ["07"], "reason": "Швидкісний обмін між тисячами обчислювальних вузлів."},
            "10": {"scenes": ["03"], "reason": "Масштабна архітектура серверів Google X."},
        },
    },
    {
        "match": "ep06_flow_study_04b_motherboard_traces_gpu_2k",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["13", "22", "44"], "reason": "Друкована плата та доріжки GPU великим планом (без логотипів)."},
            "05": {"scenes": ["02"], "reason": "Конструювання та паяння плат у майстерні."},
        },
    },
    {
        "match": "ep06_flow_img_04_researcher_viewing_gpus_alexnet_2k",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["29"], "reason": "2012 рік: обчислювальний експеримент AlexNet на GPU NVIDIA."},
            "04": {"scenes": ["07"], "reason": "Запуск AlexNet на ігрових відеокартах у лабораторії Хінтона."},
            "08": {"scenes": ["07"], "reason": "Прорив ImageNet у жовтні 2012 року."},
        },
    },
    {
        "match": "dna_transcription_molecular_model",
        "kind": "image",
        "targets": {
            "07": {"scenes": ["10"], "reason": "Молекулярна структура ДНК для візуалізації медичного трактату Амодея."},
        },
    },
    {
        "match": "stages_of_cell_division",
        "kind": "image",
        "targets": {
            "07": {"scenes": ["10"], "reason": "Стадії поділу живої клітини — біологічні відкриття за допомогою ШІ."},
        },
    },
    {
        "match": "neural_network_nodes_firing_bef7f30b",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Багатошарова нейромережа (2K)."},
            "05": {"scenes": ["05"], "reason": "Активація згорткових шарів."},
            "09": {"scenes": ["05"], "reason": "Вузли уваги (Attention)."},
        },
    },
    {
        "match": "artificial_neural_network_nodes_",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Нейронний граф прямого та зворотного проходу."},
            "09": {"scenes": ["04"], "reason": "Семантичні вузли мережі."},
        },
    },
    {
        "match": "microscopy_of_brain_hippocampal_…_28e029e0".replace("…_", ""),
        "kind": "image",
        "targets": {
            "04": {"scenes": ["04"], "reason": "Мікроскопія гіпокампа — природний прототип нейронної пам'яті."},
            "07": {"scenes": ["03"], "reason": "Електрофізіологічний зріз нейронів."},
        },
    },
    {
        "match": "28e029e0_2k.jpg",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["04"], "reason": "Мікроскопія живих нейронів мозку (2K)."},
            "07": {"scenes": ["03"], "reason": "Нейробіологічний дослід у лабораторії Прінстона."},
        },
    },
    {
        "match": "neural_core_pulsing_in_laboratory_1c257942",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["31", "45"], "reason": "Футуристична зала з пульсуючим нейроядром (без таблички LONDON)."},
            "06": {"scenes": ["10"], "reason": "Тихий дослідницький центр надрозуму."},
        },
    },
    {
        "match": "researcher_standing_near_hologra",
        "kind": "image",
        "targets": {
            "05": {"scenes": ["08", "09"], "reason": "Голографічні сцени реального світу перед дослідником (World Models)."},
            "08": {"scenes": ["05", "09"], "reason": "Візуальна бібліотека світів та об'єктів (ImageNet / World Labs)."},
        },
    },
    {
        "match": "ep02_flow_img_05_hand_shaking_golden_transistor_dust",
        "kind": "image",
        "targets": {
            "01": {"scenes": ["31"], "reason": "Рукостискання технологій та капіталу (2K ключ)."},
            "03": {"scenes": ["40"], "reason": "Стратегічний союз науки та індустрії."},
            "05": {"scenes": ["07"], "reason": "Альянс навколо відкритого коду."},
        },
    },
    {
        "match": "ep02_flow_img_06_magma_flowing_into_supercomputer",
        "kind": "image",
        "targets": {
            "01": {"scenes": ["47"], "reason": "Чиста енергія живить гігаватні обчислення."},
            "10": {"scenes": ["07"], "reason": "Енергетичний ресурс «нової електрики»."},
        },
    },
    {
        "match": "ep03_flow_img_10_lidar_scanning_tactical_map",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["45"], "reason": "2K кадр лазерного LiDAR-сканування 3D-середовища."},
            "08": {"scenes": ["09"], "reason": "Просторова тривимірна карта для World Labs."},
        },
    },
    {
        "match": "ep03_flow_img_14_galaxies_connected_by_golden_axons",
        "kind": "image",
        "targets": {
            "04": {"scenes": ["05"], "reason": "Всесвіт нейронних зв'язків (2K)."},
            "06": {"scenes": ["04"], "reason": "Космічна геометрія векторів."},
            "09": {"scenes": ["04"], "reason": "Світовий простір смислових координат."},
        },
    },
    {
        "match": "ep04_flow_img_04_human_head_cracking_releasing_light",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["06"], "reason": "Світло абстракції, що народжується всередині розуму (2K)."},
            "07": {"scenes": ["08"], "reason": "Просвічування прихованих фіч Claude 3 Sonnet."},
            "09": {"scenes": ["09"], "reason": "Глибоке міркування Системи 2."},
        },
    },
    {
        "match": "ep08_flow_img_01_human_eye_merging_with_data",
        "kind": "image",
        "targets": {
            "05": {"scenes": ["04"], "reason": "Біологічний і машинний зір (2K ключ)."},
            "07": {"scenes": ["03"], "reason": "Зорова сітківка та оптичний аналіз."},
        },
    },
    {
        "match": "ep01_doc_01_act2_nvidia_riva128" if False else "ep02_doc_01_act2_nvidia_riva128",
        "kind": "image",
        "targets": {},
    },
    {
        "match": "sutskever_alexnet_nips",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["29"], "reason": "ІСТОРИЧНЕ ДОСЬЄ (NIPS 2012): AlexNet запускався саме на двох відеокартах NVIDIA GTX 580!"},
            "04": {"scenes": ["07"], "reason": "ІСТОРИЧНЕ ДОСЬЄ: спільна проривна публікація Хінтона, Крижевського й Суцкевера 2012."},
            "08": {"scenes": ["07"], "reason": "ІСТОРИЧНЕ ДОСЬЄ: перемога AlexNet на датасеті Фей-Фей Лі ImageNet."},
        },
    },
    {
        "match": "ep08_doc_01_act2_feifeili_imagenet",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["29"], "reason": "Прес-досьє бенчмарку ImageNet, де проявилася сила GPU NVIDIA."},
            "04": {"scenes": ["07"], "reason": "Прес-досьє змагання ImageNet (обвал помилки з 26% до 15%)."},
            "06": {"scenes": ["04"], "reason": "Історичний контекст змагання ImageNet 2012."},
        },
    },
    {
        "match": "ep04_doc_01_act2_hinton_backprop_nature",
        "kind": "image",
        "targets": {
            "05": {"scenes": ["03"], "reason": "Класична стаття Nature 1986 про зворотне поширення помилки."},
            "09": {"scenes": ["02"], "reason": "Фундамент спільного шляху «хрещених батьків» ШІ."},
        },
    },
    {
        "match": "ep09_doc_01_act2_bengio_attention",
        "kind": "image",
        "targets": {
            "06": {"scenes": ["04"], "reason": "Наукова робота про Attention — прямий розвиток підходу Seq2Seq Суцкевера."},
        },
    },
    {
        "match": "ep10_doc_01_act2_andrewng_googlebrain",
        "kind": "image",
        "targets": {
            "02": {"scenes": ["29"], "reason": "Порівняння 16 000 CPU Google Brain vs кількох GPU NVIDIA у дослідницьких кластерах."},
            "06": {"scenes": ["05"], "reason": "Середовище Google Brain, з якого Суцкевер перейшов до OpenAI."},
        },
    },
]


def get_display_title_override(rel_path, default_display):
    rel_l = (rel_path or "").lower()
    fname_l = rel_l.split("/")[-1]
    if rel_l in CRYPTIC_TITLE_OVERRIDES:
        return CRYPTIC_TITLE_OVERRIDES[rel_l]
    if fname_l in CRYPTIC_TITLE_OVERRIDES:
        return CRYPTIC_TITLE_OVERRIDES[fname_l]
    return default_display


def is_hidden_non_project(rel_path):
    return (rel_path or "").lower() in HIDDEN_NON_PROJECT_PATHS


def _universal_cross_category(entry, media_type):
    """Map cross-shared assets to neutral thematic categories so foreign folder names
    like Chess / ZX Spectrum / Go never confuse another Titan's studio UI."""
    rl = (entry.get("rel_path") or "").lower()
    if entry.get("cat") in ("archive", "dossiers", "portraits"):
        return entry["cat"], entry["cat_label"]
    if entry.get("is_portrait") or "scientific_animations" in rl:
        return "sci_vfx_cross", "🔬 Науковий VFX"
    if any(k in rl for k in ("wafer", "server", "silicon", "phosphor", "motherboard", "gpu", "dxf_g", "bhnuyvtf", "kjh", "build", "comput")):
        return "cross_hardware", "💻 Кремній, Сервери & GPU"
    if any(k in rl for k in ("lidar", "voxel", "holo", "robotic", "hud", "aerial", "swarm", "metropolis", "physical_matter", "dv.png", "mathematical")):
        return "cross_spatial", "🌐 3D-Простір, Код & Симуляції"
    if any(k in rl for k in ("cellular", "dna", "zygote", "retina", "neuron", "electrical_spark", "cdwrf", "hippocampal", "bio")):
        return "cross_bio_neuro", "🧠 Нейронаука & Біофізика"
    return "cross_abstract", "🌌 Абстрактний Кіно-B-Roll"


def curate_cross_assets_for_inventory(native_entries_by_ep):
    """
    Given {ep: {"videos": [...], "images": [...]}}, return curated CLEAN cross-matched
    entries per target episode WITHOUT duplicating files by path OR by MD5 byte content,
    and NEVER pulling previs schematics, off-topic items, or mismatched personas.
    """
    cross_by_ep = {ep: {"videos": [], "images": []} for ep in native_entries_by_ep}
    seen_paths = {
        ep: {
            "video": {it["rel_path"].lower() for it in native_entries_by_ep[ep]["videos"]},
            "image": {it["rel_path"].lower() for it in native_entries_by_ep[ep]["images"]},
        }
        for ep in native_entries_by_ep
    }
    seen_md5 = {
        ep: {
            "video": {it.get("md5", "") for it in native_entries_by_ep[ep]["videos"] if it.get("md5")},
            "image": {it.get("md5", "") for it in native_entries_by_ep[ep]["images"] if it.get("md5")},
        }
        for ep in native_entries_by_ep
    }

    ep_names_short = {
        "01": "Альтман / Базовий фонд",
        "02": "Хуанг / GPU",
        "03": "Хассабіс / Science & AI",
        "04": "Хінтон",
        "05": "Лекун",
        "06": "Суцкевер",
        "07": "Амодей",
        "08": "Фей-Фей Лі",
        "09": "Бенжіо",
        "10": "Ендрю Ин",
    }

    matched_rules_count = 0
    for rule in CROSS_CURATION_RULES:
        needle = rule["match"].lower()
        r_kind = rule.get("kind", "any")
        targets = rule.get("targets", {})
        if not needle or not targets:
            continue

        for src_ep, bucket in native_entries_by_ep.items():
            for kind_key, media_type in (("videos", "video"), ("images", "image")):
                if r_kind != "any" and r_kind != media_type:
                    continue
                for entry in bucket[kind_key]:
                    rel_l = entry["rel_path"].lower()
                    if is_hidden_non_project(rel_l):
                        continue
                    if entry.get("cat") == "previs":
                        continue
                    hay = rel_l + " " + entry["file"].lower()
                    if needle not in hay:
                        continue

                    matched_rules_count += 1
                    e_md5 = entry.get("md5", "")
                    for target_ep, meta in targets.items():
                        if target_ep == src_ep or target_ep not in cross_by_ep:
                            continue
                        if rel_l in seen_paths[target_ep][media_type]:
                            continue
                        if e_md5 and e_md5 in seen_md5[target_ep][media_type]:
                            continue

                        seen_paths[target_ep][media_type].add(rel_l)
                        if e_md5:
                            seen_md5[target_ep][media_type].add(e_md5)

                        cloned = dict(entry)
                        cloned["is_cross"] = True
                        cloned["is_dup_md5"] = False
                        c_cat, c_label = _universal_cross_category(entry, media_type)
                        cloned["cat"] = c_cat
                        cloned["cat_label"] = c_label
                        cloned["source_ep"] = src_ep
                        cloned["source_label"] = f"🌌 Універсальний B-Roll (з EP{src_ep} · {ep_names_short.get(src_ep, 'Проєкт')})"
                        cloned["match_reason"] = meta["reason"]
                        cloned["suggested_scenes"] = list(meta.get("scenes", []))
                        cross_by_ep[target_ep][kind_key].append(cloned)

    return cross_by_ep, matched_rules_count


def link_cross_candidates_to_triads(ep, triads, vault_ep):
    """Attach clean reusable assets from vault_ep onto matching Triads as `cross_candidates`."""
    by_scene = {}
    for media_kind, arr in (("video", vault_ep.get("videos", [])), ("image", vault_ep.get("images", []))):
        for item in arr:
            if not item.get("is_cross"):
                continue
            for sc in item.get("suggested_scenes", []):
                by_scene.setdefault(sc, []).append({
                    "media_type": media_kind,
                    "file": item["file"],
                    "display_name": item["display_name"],
                    "rel_path": item["rel_path"],
                    "thumb": item.get("thumb", ""),
                    "preview_path": item.get("preview_path", ""),
                    "res_label": item.get("res_label", ""),
                    "dur_label": item.get("dur_label", ""),
                    "is_portrait": bool(item.get("is_portrait", False)),
                    "source_ep": item.get("source_ep", ""),
                    "source_label": item.get("source_label", ""),
                    "match_reason": item.get("match_reason", ""),
                })

    for t in triads:
        cands = by_scene.get(t["num"], [])
        cands.sort(key=lambda c: (0 if c["media_type"] == "video" else 1, 1 if c.get("is_portrait") else 0, c["file"].lower()))
        t["cross_candidates"] = cands
