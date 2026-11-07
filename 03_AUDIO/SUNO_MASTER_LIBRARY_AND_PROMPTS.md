# МАЙСТЕР-БІБЛІОТЕКА SUNO PRO (92 BPM) ТА КАТАЛОГ ПРОМПТІВ СЕЗОНУ 1
**Проєкт:** Cinematic Thoughtcast // «Архітектори Розуму (AI Titans)»  
**Локальні директорії WAV-майстрів (48 kHz, Stereo):**
- Оригінали з метаданими C2PA Suno: `03_AUDIO/suno_stems/00_MASTER_POOL_ORIGINAL/`
- Готові файли під авто-сортування DaVinci Smart Bins: `03_AUDIO/suno_stems/EP01_ALTMAN_SMART_BINS/`

---

## 1. Архітектурна відповідь: для першого епізоду чи на весь проєкт?

Згенеровані **10 WAV-треків (загальний хронометраж `37 хв 17 с`, `431.6 МБ`, `48 000 Hz`)** працюють у **дворівневій системі**:

1. **На весь проєкт (Наскрізне звукове ДНК / Universal Master Stem Pool):**
   Ті 3 базові промпти зі Слайду 6–7 Генеральної Архітектурної Специфікації та аудіо-паспорта (`Модуль A: Introspection`, `Модуль B: Tension & Crisis`, `Модуль C: Transcendence`) — це **універсальний каркас усього серіалу**. Вони тримають фірмовий почерк каналу, тому ці 10 треків можна вільно використовувати як основну музичну підкладку в будь-якому з 10 випусків.
2. **На 100% закритий Епізод 01 (Сем Альтман — «Анатомія експоненти», 20:30 хв):**
   У папці `03_AUDIO/suno_stems/EP01_ALTMAN_SMART_BINS/` усі 10 файлів уже перейменовані за суворим стандартом DaVinci Smart Bins (`EP01_MUS_...` та `EP01_AMB_...`) і повністю перекривають усі 4 акти першого випуску з запасом у 16 хвилин.
3. **Індивідуальний тембр для Епізодів 02–10 (опціональне підсилення):**
   Базу (суб-бас, дрони тиску та фінальний катарсис із цих 10 треків) можна брати для всіх серій, додаючи лише по **1–2 характерні лейтмотиви героя** (наприклад, віолончель і шаховий годинник для Гассабіса, столярну перкусію для Хінтона, французький аналоговий синт 70-х для Лекуна, джазовий контрабас під дощем для Бенжіо). Усі ці промпти зведені в Розділі 3 нижче та на сторінках героїв.

---

## 2. Технічний реєстр 10 імпортованих WAV-треків (Аудит C2PA + Акустика)

| № | Оригінальний файл Suno (`00_MASTER_POOL_ORIGINAL/`) | Ім'я для DaVinci Smart Bins (`EP01_ALTMAN_SMART_BINS/`) | Модуль / Акт | Час | Пік / RMS | Рекомендація для монтажу (Fairlight A2/A3) |
|---|---|---|---|---|---|---|
| **01** | `Dusty Analog Reverie.wav` | `EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav` | **Модуль A: Introspection** (Акт 1) | `3:58` | `-4.3 dB` / `-17.0 dB` | **Еталонне відкриття (92 BPM):** теплий Rhodes, вініловий пил, м'який суб-бас. Ідеально під дитинство та Mac LC II (`0:00–4:00`). |
| **02** | `Warm Analog Pulse-2.wav` | `EP01_MUS_03_ACT1_92BPM_StLouis_Conformity.wav` | **Модуль A: Introspection** (Акт 1) | `4:14` | `-4.8 dB` / `-17.3 dB` | Рівний гіпнотичний пульс (`~91–92 BPM`), чудово тримає ритм під розповідь про школу, Стенфорд і старт кар'єри. |
| **03** | `Warm Analog Pulse.wav` | `EP01_MUS_04_ACT1_92BPM_Stanford_Loopt_Grind.wav` | **Модуль A: Introspection** (Акт 1 / Переходи) | `3:58` | `-4.8 dB` / `-16.6 dB` | Повільніший, розріджений атмосферний дубль (`~82 BPM` відчуття half-time) — ідеальний для рефлексивних пауз між актами. |
| **04** | `Clockwork Dread.wav` | `EP01_MUS_05_ACT2_92BPM_Exponential_Law.wav` | **Модуль B: Tension & Crisis** (Акт 2) | `3:33` | `-5.0 dB` / `-15.9 dB` | Годинникова металева перкусія + темний модульний синт і саксофонний дрон. Нагнітання ставок (Y Combinator, народження OpenAI, криза NV1 у Хуанга). |
| **05** | `Clockwork Dread-2.wav` | `EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav` | **Модуль B: Tension Climax** (Акт 3) | `3:33` | `-4.1 dB` / `-14.0 dB` | **Найщільніший драйвовий трек пулу (`-14.0 dB RMS`):** ставити на кульмінацію конфлікту (120 годин бунту в OpenAI, битва за CUDA, вибух AlexNet). |
| **06** | `Deep Water Pressure.wav` | `EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension.wav` | **Доріжка A3: AMB / DRONE** (Акти 2–3) | `3:49` | `-3.9 dB` / `-16.7 dB` | Темний глибоководний саб-тиск. Ідеально під цитату Альтмана про «запас кисню під водою», 30 днів до банкрутства (EP02) та 30 років зими ШІ (EP04). |
| **07** | `Monumental Silence.wav` | `EP01_AMB_10_ACT3_DRONE_The_Firing_Silence.wav` | **Модуль C / AMB Bridge** (Акт 3–4) | `3:33` | `-6.1 dB` / `-18.7 dB` | **Чистий 92 BPM катарсис тиші:** момент шоку після звільнення в Google Meet АБО головна тема **EP06 (Ілля Суцкевер — «Монастир тиші SSI»)**. |
| **08** | `Celestial Ascent.wav` | `EP01_MUS_13_ACT4_92BPM_Stargate_Energy_Scale.wav` | **Модуль C: Transcendence** (Акт 4) | `3:35` | `-4.5 dB` / `-19.0 dB` | Урочисті аналогові брас-синтезатори у стилі Vangelis. Масштаб Stargate, енергії та космічного горизонту. |
| **09** | `Celestial Ascent-2.wav` | `EP01_MUS_14_ACT4_92BPM_Builders_Code_Philosophy.wav` | **Модуль C: Transcendence** (Акт 4) | `3:40` | `-3.8 dB` / `-18.2 dB` | Широка панорама IMAX для формулювання 3 життєвих законів героя (Нобелівські фінали EP03 Гассабіса та EP04 Хінтона). |
| **10** | `Celestial Ascent-3.wav` | `EP01_MUS_15_ACT4_92BPM_Future_Horizon_Finale.wav` | **Модуль C: Transcendence** (Фінал / Титри) | `3:35` | `-6.8 dB` / `-18.3 dB` | Найделікатніший за піками (`-6.8 dB`) фінальний трек — залишає максимум повітря під фінальну цитату диктора та плавне згасання в тишу. |

> **Примітка для DaVinci Resolve Fairlight:** Усі 10 треків згенеровані у частоті дискретизації **`48 000 Hz`** (стандарт відеовиробництва — нуль ресемплінгу на таймлайні!). Оскільки `Clockwork Dread-2.wav` має високу щільність (`-14.0 dB RMS`), на доріжці `A2` обов'язково тримай базовий фейдер на `-9..-11 dB` + активний `Sidechain Listen 1 (-3.2 dB)` від голосу диктора `A1`.

---

## 3. Індивідуальні промпти характерних тем для Епізодів 02–10 (92 BPM Custom Instrumental)

Якщо захочеш додати по 1–2 унікальні тембральні фарби до нашого базового пулу з 10 треків для наступних героїв:

- **EP02 — Дженсен Хуанг (Кремній та індустріальний гарт):**
  `Instrumental dark industrial trip-hop, 92 bpm, deep sub-bass pulse, distant metallic anvil textures, melancholic clean electric guitar with slow tremolo, rain on diner glass atmosphere, no vocals.`
- **EP03 — Деміс Гассабіс (Шахи, нейробіологія та білки):**
  `Instrumental neo-classical ambient trip-hop, 92 bpm, felt piano melody, subtle mechanical chess clock ticking percussion, soaring solo cello over warm analog synth pads, London rain mood, no vocals.`
- **EP04 — Джеффрі Хінтон (Столярна майстерня та драма Прометея):**
  `Instrumental dramatic chamber trip-hop, 92 bpm, deep upright double bass, organic wood workshop foley rhythm, Oppenheimer style tragic solo cello and violin tension, solemn philosophical mood, no vocals.`
- **EP05 — Ян Лекун (Паризька радіомайстерня та вітрило в Атлантиці):**
  `Instrumental French touch ambient downtempo, 92 bpm, Air and Jean-Michel Jarre style warm analog synthesizer bassline, vintage phaser guitar chords, crisp ocean wind atmosphere, wide stereo, no vocals.`
- **EP06 — Ілля Суцкевер (Камінь Єрусалима та тиша SSI):**
  `Instrumental ascetic meditative downtempo, 92 bpm, crystalline glass harmonica resonance, deep warm Moog sub-bass drone, vast monastic reverb, sacred mathematical stillness, no vocals.`
- **EP07 — Даріо Амодей (Біофізика світла та Machines of Loving Grace):**
  `Instrumental precision electronic neo-classical, 92 bpm, soft marimba and analog pluck arpeggios, warm pulsing sub-bass, hopeful golden ambient pads, clean scientific clarity, no vocals.`
- **EP08 — Фей-Фей Лі (Туман Ченду, пара пральні та просторовий світ):**
  `Instrumental emotional cinematic trip-hop, 92 bpm, delicate acoustic piano and warm cello, subtle rhythmic steam hiss percussion, deep comforting sub-bass, humanist warmth, IMAX soundstage, no vocals.`
- **EP09 — Йошуа Бенжіо (Монреальський дощ та совість академії):**
  `Instrumental nocturnal jazz-infused trip-hop, 92 bpm, warm acoustic upright bass groove, brushed snare, melancholic Rhodes piano, soft autumn Montreal rain texture, reflective dignity, no vocals.`
- **EP10 — Ендрю Ин (Сінгапурський світанок та нова електрика):**
  `Instrumental uplifting cinematic downtempo, 92 bpm, warm fingerpicked acoustic guitar harmonics, clean modern sub-bass pulse, bright airy analog synth pads, inspiring mentor atmosphere, no vocals.`
