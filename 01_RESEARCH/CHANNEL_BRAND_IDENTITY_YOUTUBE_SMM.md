# Анатомія генія. Код цивілізації
## Anatomy of Genius. The Civilization Code
### Офіційна структура заповнення YouTube-каналу (UA / EN), ліміти, правила та промпти

---

## 1. РЕАЛЬНІ ТЕХНІЧНІ ЛІМІТИ ТА ПОЛІТИКА YOUTUBE STUDIO

Усі поля нижче підготовлено з урахуванням жорстких лімітів YouTube Studio (включно з `\r\n` для переносів рядків та прихованими лапками `"..."`, які YouTube додає при підрахунку багатослівних тегів):

| Поле / елемент YouTube Studio | Де знаходиться | Офіційний ліміт / вимога | Перевірене значення у нашому пакеті |
| :--- | :--- | :--- | :--- |
| **Назва каналу (Name)** | Налаштування каналу → Профіль | **До 50 символів** (зміна: не частіше 3 разів на 90 днів) | UA: **31 симв.** • EN: **40 симв.** |
| **Псевдонім (@handle)** | Налаштування каналу → Профіль | **3–30 символів** (`a-z`, `0-9`, `_`, `-`, `.`) | `@AnatomyOfGenius` (**16 симв.**) |
| **Опис каналу (Description)** | Налаштування каналу → Профіль | **До 1 000 символів** (перші ~150 видно до кнопки «Ще») | UA: **875 симв.** • EN: **931 симв.** • Гібрид: **916 симв.** |
| **Посилання (Links)** | Налаштування каналу → Профіль | До **14 посилань**; назва посилання: бажано **до 30 символів** | До 21 символу (UA / EN) |
| **Контактний email** | Налаштування каналу → Профіль | Дійсна адреса електронної пошти | Плейсхолдер під вашу пошту |
| **Ключові слова каналу** | Налаштування → Канал → Основна інф. | **До 500 символів** сумарно (з комами й лапками) | **403 симв.** за формулою YouTube (373 без лапок) |
| **Переклад каналу** | Налаштування каналу → Мови | Локалізація назви та опису каналу під мову глядача | Точний 1-в-1 переклад UA ↔ EN |
| **Назва відео (Title)** | Відомості про відео | **До 100 символів** (на мобільних обрізається після ~55–60) | Структура: головна інтрига в перших 55 символах |
| **Опис відео (Description)** | Завантаження → Основна інформація | **До 5 000 символів**; перші ~150 видно до згортання | Хук до 140 симв. + таймкоди + 5 хештегів |
| **Теги відео (Tags)** | Відомості про відео → Розгорнути | **До 500 символів** (враховуючи коми й приховані лапки) | UA: **288 симв.** • EN: **308 симв.** |
| **Хештеги в описі** | Опис відео / назва | **Макс. 60** (інакше YouTube ігнорує всі); видно перші **3** | **5 хештегів** (без переспаму) |
| **Назва плейлиста** | Списки відтворення | **До 150 символів** | UA: **34 симв.** • EN: **19 симв.** |
| **Аватар (Profile picture)** | Налаштування каналу → Профіль | **800×800 px** (відображається 98×98 px у колі), до **15 МБ** | 1:1 квадрат, головний символ строго в центрі |
| **Банер (Banner image)** | Налаштування каналу → Профіль | **2560×1440 px** (мін. 2048×1152), до **6 МБ**; **Safe Area: 1546×423 px** (мін. **1235×338 px**) по центру | Чиста центральна зона без обрізання на мобільних і ТБ |
| **Водяний знак відео** | Налаштування каналу → Профіль | **150×150 px** (1:1), PNG/GIF, до **1 МБ** | Лаконічний монохромний символ |
| **Прев'ю (Thumbnail)** | Відомості про відео | **1280×720 px** (16:9, мін. ширина 640 px), до **2 МБ** | Портрет справа, вільна зона для тексту зліва |
| **Маркування AI-контенту** | Відомості про відео → Змінений контент | Обов'язкове для реалістичних AI-сцен реальних подій/людей | Чітке правило: вмикати «Так» для фотореалістичного Veo |

> **Політика AI-контенту (Altered or Synthetic Content):** Якщо відео містить реалістичну генерацію голосу/відео реальних людей у сценах, яких не було, або фотореалістичну реконструкцію подій (Veo/Flow), під час завантаження потрібно обрати **«Так»** у пункті «Змінений або синтетичний контент». Використання AI для написання сценарію, корекції кольору чи абстрактної графіки маркування не потребує.

---

## 2. ПОКРОКОВЕ ЗАПОВНЕННЯ YOUTUBE STUDIO (НАЛАШТУВАННЯ КАНАЛУ → ПРОФІЛЬ)

Найефективніший спосіб для двомовного каналу — задати **українську версію як основну**, а **англійську — через функцію перекладу в YouTube Studio** (*Налаштування каналу → Профіль → Мова перекладу: Англійська*). Тоді україномовні глядачі бачитимуть назву та опис українською, а міжнародна аудиторія — дослівну англійську версію.

### 2.1. Назва каналу (Name) — ліміт 50 символів
* **Українською (основна, 31 символ):**
  `Анатомія генія. Код цивілізації`
* **Англійською (переклад, 40 символів):**
  `Anatomy of Genius. The Civilization Code`

### 2.2. Псевдонім (Handle) — ліміт 30 символів
1. `@AnatomyOfGenius` *(16 символів — основний варіант)*
2. `@AnatomyOfGeniusUA` *(18 символів — якщо перший зайнятий)*
3. `@CivilizationCode` *(17 символів — запасний варіант)*

### 2.3. Опис каналу (Description) — ліміт 1 000 символів

#### 🇺🇦 Основний текст українською (875 символів / 888 з CRLF)
```text
«Анатомія генія. Код цивілізації» — документальна кіностудія про мислення, психологію та наукові відкриття людей, які змінили хід історії.

Ми не переповідаємо енциклопедії, а розкриваємо внутрішню механіку геніальності:
• Як одна людина долає сумніви, самотність та опір системи заради прориву?
• Які кризи та випробування формують характер творця?
• Як ідея стає алгоритмом, мікрочипом, кодом життя чи космічною технологією?

План сезонів:
• Сезон 1: Титани штучного інтелекту (Альтман, Хуанг, Гассабіс, Хінтон, Лекун, Суцкевер, Амодей, Лі, Бенжіо, Ин)
• Сезон 2: Кремнієві титани (Джобс, Маск, Мур, Чанг, Возняк та ін.)
• Сезон 3: Код життя (біотехнології та геноміка)
• Сезон 4: Глибокий горизонт (космос, енергія, квантова фізика)

Документальні фільми 4K на основі першоджерел, архівів та оригінального саундтреку. Підписуйтеся, щоб зрозуміти розум творців майбутнього.
```

#### 🇬🇧 Дослівний переклад англійською (931 символ / 944 з CRLF)
*(Для поля «Переклад опису каналу → Англійська»)*
```text
"Anatomy of Genius. The Civilization Code" is a documentary studio about the thinking, psychology, and scientific discoveries of people who changed the course of history.

We do not retell encyclopedias, we reveal the inner mechanics of genius:
• How does one person overcome doubt, loneliness, and systemic resistance for a breakthrough?
• What crises and trials shape a creator's character?
• How does an idea become an algorithm, a microchip, the code of life, or space technology?

Season roadmap:
• Season 1: AI Titans (Altman, Huang, Hassabis, Hinton, LeCun, Sutskever, Amodei, Li, Bengio, Ng)
• Season 2: Silicon Titans (Jobs, Musk, Moore, Chang, Wozniak, etc.)
• Season 3: Code of Life (biotechnology and genomics)
• Season 4: Deep Horizon (space, energy, quantum physics)

4K documentary films based on primary sources, archives, and an original soundtrack. Subscribe to understand the minds of the creators of the future.
```

#### 🌐 Комбінований опис UA + EN в одному полі (916 символів / 933 з CRLF)
*(Використовуйте лише в разі, якщо хочете показати обидві мови одразу в одному текстовому вікні без локалізації):*
```text
«Анатомія генія. Код цивілізації» — документальна кіностудія про мислення, психологію та відкриття людей, які змінили хід історії.

Ми розкриваємо механіку геніальності:
• Як долаються сумніви, самотність і тиск системи?
• Як ідея стає алгоритмом, мікрочипом, кодом життя чи космічною технологією?

4 сезони: Титани ШІ • Кремнієві титани • Код життя • Глибокий горизонт.
Фільми 4K • Першоджерела та архіви • Оригінальний саундтрек.

---
"Anatomy of Genius. The Civilization Code" is a documentary studio about the thinking, psychology, and discoveries of people who changed the course of history.

We reveal the mechanics of genius:
• How are doubt, loneliness, and systemic pressure overcome?
• How does an idea become an algorithm, a microchip, the code of life, or space technology?

4 seasons: AI Titans • Silicon Titans • Code of Life • Deep Horizon.
4K films • Primary sources & archives • Original soundtrack.
```

### 2.4. Посилання (Links) та Контактна інформація
*До 14 посилань. Назви тримаємо до 30 символів, із перекладом UA ↔ EN:*
* `Інтерактивний дашборд` *(21 симв.)* / `Interactive Dashboard` *(21 симв.)* → `https://tfmshell-cloud.github.io/ai-titans-thoughtcast/`
* `Telegram` *(8 симв.)* / `Telegram` *(8 симв.)* → `[посилання на ваш Telegram]`
* `Instagram` *(9 симв.)* / `Instagram` *(9 симв.)* → `[посилання на ваш Instagram]`
* `X (Twitter)` *(11 симв.)* / `X (Twitter)` *(11 симв.)* → `[посилання на ваш X]`
* `TikTok` *(6 симв.)* / `TikTok` *(6 симв.)* → `[посилання на ваш TikTok]`
* **Контактна електронна адреса:** `[вкажіть вашу актуальну робочу пошту]`

---

## 3. НАЛАШТУВАННЯ → КАНАЛ → ОСНОВНА ІНФОРМАЦІЯ (КЛЮЧОВІ СЛОВА)

*Суворий ліміт YouTube: **500 символів** (разом із комами та прихованими лапками для фраз із пробілами). У YouTube Studio це одне спільне поле, тому воно об'єднує ключові запити обома мовами.*  
*Довжина блоку нижче: 373 символи без лапок / **403 символи** за підрахунком YouTube (перевірено):*

```text
Анатомія генія,Код цивілізації,Анатомія генія Код цивілізації,Anatomy of Genius,The Civilization Code,Anatomy of Genius The Civilization Code,штучний інтелект,документальні фільми,біографія,історія технологій,нейромережі,наука,Кремнієва долина,інженерія,artificial intelligence,documentary,biography,tech history,neural networks,science,Silicon Valley,engineering,AI Titans
```

---

## 4. НАЛАШТУВАННЯ ЗАВАНТАЖЕННЯ (UPLOAD DEFAULTS) — ДОСЛІВНІ ПАРИ UA / EN

### 4.1. Шаблон опису під кожним відео (ліміт 5 000 символів)

#### 🇺🇦 Українська версія:
```text
«[Цитата героя випуску або головне запитання фільму — до 140 символів]»

У цьому документальному фільмі каналу «Анатомія генія. Код цивілізації» ми досліджуємо шлях [Ім'я Героя]: від [перших кроків / ранньої кризи] до [головного наукового чи технологічного прориву]. Це історія подолання, внутрішньої боротьби та ідеї, яка стала частиною коду сучасної цивілізації.

⏱️ Таймкоди:
00:00 — Пролог
02:15 — Акт 1: Походження та перші випробування
07:40 — Акт 2: Криза та сумніви
13:10 — Акт 3: Прорив і точка неповернення
18:25 — Акт 4: Спадщина та код цивілізації

📺 Дивіться також:
• Попередній випуск: [Посилання]
• Усі випуски Сезону 1 «Титани ШІ»: [Посилання на плейлист]
• Інтерактивна карта проєкту: https://tfmshell-cloud.github.io/ai-titans-thoughtcast/

🎵 Музика та звук:
Оригінальний саундтрек студії (92 BPM) • Зведення звуку 48 kHz / 24-bit.

🎙️ Двомовне аудіо:
Випуск доступний з українською та англійською звуковими доріжками (оберіть мову в налаштуваннях плеєра ⚙️ → Звукова доріжка).

📌 Соцмережі каналу:
• Telegram: [Посилання]
• Instagram: [Посилання]
• X (Twitter): [Посилання]
• TikTok: [Посилання]

#АнатоміяГенія #КодЦивілізації #Документалістика #Наука #ШтучнийІнтелект
```

#### 🇬🇧 Дослівна англійська версія (для вкладки перекладу відео):
```text
"[Quote from the episode's hero or the film's main question — up to 140 characters]"

In this documentary film on the "Anatomy of Genius. The Civilization Code" channel, we explore the journey of [Hero's Name]: from [first steps / early crisis] to [the main scientific or technological breakthrough]. This is a story of perseverance, inner struggle, and an idea that became part of modern civilization's code.

⏱️ Chapters:
00:00 — Prologue
02:15 — Act 1: Origins and First Trials
07:40 — Act 2: Crisis and Doubt
13:10 — Act 3: Breakthrough and Point of No Return
18:25 — Act 4: Legacy and the Civilization Code

📺 Watch also:
• Previous episode: [Link]
• Full Season 1 "AI Titans" playlist: [Playlist Link]
• Interactive project dashboard: https://tfmshell-cloud.github.io/ai-titans-thoughtcast/

🎵 Music and sound:
Original studio soundtrack (92 BPM) • Audio mastering 48 kHz / 24-bit.

🎙️ Multi-language audio:
This episode is available with Ukrainian and English audio tracks (select your language in the player settings ⚙️ → Audio track).

📌 Channel social media:
• Telegram: [Link]
• Instagram: [Link]
• X (Twitter): [Link]
• TikTok: [Link]

#AnatomyOfGenius #TheCivilizationCode #Documentary #Science #ArtificialIntelligence
```

### 4.2. Базові теги відео (ліміт 500 символів)
*(Решту ~190–210 символів у кожному конкретному відео додавайте на ім'я героя та тему випуску)*

* **UA базові теги (288 символів за підрахунком YouTube):**
```text
Анатомія генія,Код цивілізації,документальний фільм,штучний інтелект,нейромережі,історія технологій,біографія,наука і технології,інженерія,Кремнієва долина,Титани ШІ,майбутнє,технологічна революція,документалістика українською,глибоке навчання,філософія технологій
```

* **EN базові теги — дослівний переклад (308 символів за підрахунком YouTube):**
```text
Anatomy of Genius,The Civilization Code,documentary film,artificial intelligence,neural networks,history of technology,biography,science and technology,engineering,Silicon Valley,AI Titans,future,technological revolution,documentary in English,deep learning,philosophy of technology
```

---

## 5. ПЛЕЙЛИСТИ, «СПІЛЬНОТА» ТА СОЦМЕРЕЖІ (З ТОЧНИМИ ЛІМІТАМИ)

### 5.1. Назви перших плейлистів (ліміт YouTube: 150 символів)
* **UA:** `Сезон 1: Титани штучного інтелекту` *(34 симв.)*
* **EN:** `Season 1: AI Titans` *(19 симв.)*

### 5.2. Вкладка «Спільнота» (Community) — Перше опитування перед запуском
*Питання: до 500 символів. Варіанти відповіді: до 65 символів кожен.*

* **🇺🇦 Питання (90 симв.):** `Про якого героя чи тему ви хотіли б побачити поглиблений документальний розбір насамперед?`
  * `Сем Альтман: шлях OpenAI` *(24 симв.)*
  * `Дженсен Хуанг: ставка на CUDA` *(29 симв.)*
  * `Деміс Гассабіс: DeepMind і AlphaFold` *(36 симв.)*
  * `Ілля Суцкевер: філософія масштабування` *(38 симв.)*

* **🇬🇧 Дослівний переклад питання (85 симв.):** `Which hero or topic would you like to see an in-depth documentary breakdown on first?`
  * `Sam Altman: the OpenAI journey` *(30 симв.)*
  * `Jensen Huang: the bet on CUDA` *(29 симв.)*
  * `Demis Hassabis: DeepMind & AlphaFold` *(36 симв.)*
  * `Ilya Sutskever: philosophy of scaling` *(37 симв.)*

### 5.3. Профілі в соцмережах (біо під ліміти кожної платформи)

* **Telegram (ліміт: 255 символів):**
  * **UA (157 симв.):** `Офіційний канал студії «Анатомія генія. Код цивілізації». Досьє на візіонерів науки й технологій, архівні документи, ментальні моделі та премʼєри фільмів 4K.`
  * **EN (176 симв.):** `Official channel of "Anatomy of Genius. The Civilization Code" studio. Dossiers on science and technology visionaries, archival documents, mental models, and 4K film premieres.`

* **Instagram (ліміт: 150 символів):**
  * **UA (132 симв.):**
    ```text
    Анатомія генія. Код цивілізації
    Документальна кіностудія 4K про мислення тих, хто змінив світ.
    Титани ШІ • Кремній • Біотех • Космос
    ```
  * **EN (148 симв.):**
    ```text
    Anatomy of Genius. The Civilization Code
    4K documentary studio on the thinking of those who changed the world.
    AI Titans • Silicon • Biotech • Space
    ```

* **X / Twitter (ліміт: 160 символів):**
  * **UA (132 симв.):** `Анатомія генія. Код цивілізації — документальна студія про психологію, наукові прориви та ідеї людей, які формують майбутнє людства.`
  * **EN (147 симв.):** `Anatomy of Genius. The Civilization Code — a documentary studio about the psychology, breakthroughs, and ideas of people shaping humanity's future.`

* **TikTok (ліміт: 80 символів):**
  * **UA (66 симв.):** `Анатомія генія. Код цивілізації — короткі історії великих розумів.`
  * **EN (72 симв.):** `Anatomy of Genius. The Civilization Code — short stories of great minds.`

---

## 6. НОВІ ЧИСТІ ПРОМПТИ ДЛЯ ГЕНЕРАЦІЇ ЗОБРАЖЕНЬ

Промпти очищено від hex-кодів і чисел пікселів усередині текстового опису, щоб нейромережа не малювала зайвих написів та візуального шуму. Для української версії банера текст накладається окремо поверх чистої центральної смуги в межах YouTube Safe Area (**1235×338 px**).

### 6.1. Аватар каналу (Profile Picture — 1:1)
*Після генерації збережіть у розмірі 800×800 px. Світлий центр не виходить за межі круглої маски.*

```text
Minimalist emblem icon centered inside a dark obsidian space, refined silver-titanium silhouette of a human head in profile where the mind subtly transforms into luminous cyan geometric circuit lines and warm gold architectural curves, deep matte slate background with wide dark margin on all edges so nothing touches the frame border, Scandinavian studio design, clean 3D vector-inspired render, soft studio rim light, no text, no letters, no numbers --ar 1:1
```

### 6.2. Фон шапки YouTube-каналу (Banner Background — 16:9, без тексту)
*Генерується в 16:9, експортується у 2560×1440 px. Центральна горизонтальна смуга спеціально темна й чиста під накладання українського або англійського напису у Safe Area (1546×423 / 1235×338 px).*

```text
Ultra-wide cinematic documentary studio background in triptych balance, keeping a wide dark clean empty obsidian center horizontal strip completely uncluttered for typography overlay. On the far left edge: atmospheric retro archival engineering laboratory softly lit by warm amber tungsten lamps, blueprint sketches and glass vacuum tubes. On the far right edge: deep space horizon with luminous cyan neural light filaments, microscopic silicon wafer lattice and subtle gravitational arc light. Deep dark slate blue-black shadows, subtle anamorphic flare, 35mm fine film grain, IMAX documentary mood, no text, no words, no logos --ar 16:9
```

### 6.3. Шапка каналу з англійським написом (варіант для Imagen / Nano Banana / Ideogram)
*Якщо хочете спробувати згенерувати банер одразу з готовим англійським заголовком у центральній безпечній зоні:*

```text
Minimalist wide cinematic YouTube channel banner on a deep matte dark slate background. Centered strictly inside a compact horizontal middle area with very wide empty dark margins on top, bottom, left, and right: crisp white luxury sans-serif typography reading "ANATOMY OF GENIUS" on the first line and slightly smaller subtle cyan uppercase text "THE CIVILIZATION CODE" directly below it. Softly faded near the far left and far right edges: faint atmospheric silhouettes of silicon chip pathways and cosmic light arcs, understated Christopher Nolan documentary aesthetic --ar 16:9
```

### 6.4. Водяний знак плеєра (Video Watermark — 1:1, 150×150 px)
```text
Ultra-simple minimalist monochrome white geometric icon centered on a solid pure black background, single continuous crisp architectural line forming a human profile fused with a single square microchip node, thick clean lines readable at very small icon scale, flat graphic design, wide black margins, no text, no gradients --ar 1:1
```

### 6.5. Майстер-шаблон прев'ю відео (YouTube Thumbnail — 16:9, 1280×720 px)
*Підставте ім'я потрібного героя. Обличчя зміщене праворуч, ліва частина темна й чиста під великий заголовок (2–4 слова).*

```text
Dramatic cinematic documentary YouTube thumbnail frame, tight emotional close-up portrait of [HERO NAME] placed on the right third of the frame looking intensely toward the camera. High-contrast split lighting with cool cyan light sculpting one side of the face and warm amber rim light along the jaw and shoulders. Blurred deep dark studio background with subtle out-of-focus server lights. Generous clean dark shadow space across the left half of the frame for bold headline typography. Shot on ARRI Alexa, 85mm portrait lens, shallow depth of field, authentic skin texture, cinematic film color grade, no text --ar 16:9
```
