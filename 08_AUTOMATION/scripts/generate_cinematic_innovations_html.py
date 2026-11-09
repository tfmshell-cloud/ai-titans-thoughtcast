#!/usr/bin/env python3
import json, os

INNOVATIONS = [
  {
    "id": 1,
    "num": "01",
    "name_ua": "Оптичний рентген мікрочіпа",
    "name_en": "The Silicon X-Ray Zoom",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "00:15 – 00:45",
    "act": "Акт 1 • Дитинство 1993",
    "tagline": "Безшовне занурення від повсякденного предмета в кремнієве серце комп'ютера",
    "concept": "Камера наближається впритул до бежевого пластику Macintosh LC II, проходить крізь його структуру і без монтажної склейки опиняється всередині кремнієвого кристала. Золоті мікродоріжки спалахують бінарними імпульсами, трансформуючись у живу нейронну мережу.",
    "why_it_works": "Глядач на фізичному рівні відчуває те, про що говорить диктор: комп'ютер перестає бути коробкою і стає розширенням людського мозку.",
    "prompt_ai": "Seamless macro push-in camera shot plunging directly into the beige plastic chassis of a vintage 1993 Macintosh computer, penetrating solid matter into microscopic green silicon wafer traces. Microscopic copper and gold circuits illuminate with pulsing coherent azure light, expanding into an infinite architectural city of transistors. Photorealistic electron microscope aesthetic meets Hollywood sci-fi, 8k render, 24fps.",
    "davinci_recipe": "Fusion Page: 3D Camera Projection + FastNoise Displacement. Ефект 'Displace' з маскою ліній кремнію. Перехід через оптичний зум на доріжці V1 (Blur Disolve 4 кадри, Smooth Curve).",
    "sfx_cue": "Глибокий суб-дроп 35Hz + наростаючий високочастотний гул котушки індуктивності (Coil Whine) з подальшим різким переходом у дзвін кристала."
  },
  {
    "id": 2,
    "num": "02",
    "name_ua": "Екранний привид 90-х",
    "name_en": "The CRT Ghosting Reflection",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "00:30 – 00:45",
    "act": "Акт 1 • Перший код",
    "tagline": "Вигнуте темне скло кінескопа як дзеркало внутрішнього світу",
    "concept": "Замість показу плоского монітора ми дивимося прямо на вигнуте скло CRT. По склу біжать рядки зеленого/бурштинового терміналу, а в глибокому дзеркальному відбитті ми бачимо очі 8-річного хлопчика, його подих і кімнату 1993 року.",
    "why_it_works": "Поєднує в одному кадрі два виміри: внутрішнє мислення героя (код) та його фізичну вразливість у реальному світі.",
    "prompt_ai": "Extreme close-up of a vintage 1993 curved glass CRT monitor in a dark room. Glowing green phosphor terminal text scrolls vertically across the screen, while the dark reflective glass acts as a subtle mirror showing the reflection of an 8-year-old Caucasian boy's focused eyes and face. Visible raster scanlines, chromatic aberration on edges, Fincher style, 4k 24fps.",
    "davinci_recipe": "Color Page: Нода зі сканлайнами (OFX Scanlines) + нода Composite (Screen/Add) для шару відбиття обличчя диктора. Легка бочкова дисторсія (Lens Distortion -0.08).",
    "sfx_cue": "Високочастотний свист строчного трансформатора 15.6 kHz + сухий приглушений стукіт механічних клавіш Alps."
  },
  {
    "id": 3,
    "num": "03",
    "name_ua": "Стиснення епохи в одній точці",
    "name_en": "The Architectural Time-Lapse Collapse",
    "cat": "temporal",
    "cat_label": "⏳ Час і простір",
    "cat_color": "purple",
    "tc": "03:30 – 04:45",
    "act": "Акт 1 -> Акт 2 • Складний відсоток",
    "tagline": "30 років історії за 5 секунд на нерухомому штативі",
    "concept": "Мертвий штатив. Силует Сема сидить у центрі кадру. Навколо нього за 5 секунд світло і декорації змінюються 4 рази: 1993 (дитяча кімната) -> 2005 (гараж Loopt) -> 2015 (штаб YC) -> 2024 (офіс OpenAI). Сем залишається незмінною віссю Всесвіту.",
    "why_it_works": "Наочна візуалізація експоненційного часу: людина не змінює фокус, змінюється масштаб її впливу на цивілізацію.",
    "prompt_ai": "Locked-off tripod cinematic time-lapse sequence: silhouette of a tech founder sitting at a central desk as the entire room around him morphs across eras in rapid succession: 1990s cozy suburban bedroom dissolves into messy 2000s startup garage, then sleek modern glass corporate boardroom, and finally glowing futuristic AI data hub. Center figure stays anchored, 4k 24fps.",
    "davinci_recipe": "Edit Page: 4 окремих шоти, вирівняних за координатами очей (Position X/Y Lock). Плавний Morph Cut на стиках тривалістю 8 кадрів + накладання світлового шлейфу (Optical Flow).",
    "sfx_cue": "Звук прокручування магнітофонної стрічки на надшвидкості (Tape Rewind) + клацання затворів камер кожну секунду."
  },
  {
    "id": 4,
    "num": "04",
    "name_ua": "Тепловізор стратегічної напруги",
    "name_en": "The Thermal FLIR Intelligence Map",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "05:45 – 07:00",
    "act": "Акт 2 • Готель Rosewood",
    "tagline": "Градус історичного рішення через інфрачервоний спектр",
    "concept": "Під час вечері чотирьох титанів (Альтман, Маск, Суцкевер, Брокман) кадр із кінематографічного нуару на мить перемикається в режим тепловізора військового класу. Холодний синій зал засідань раптово показує палаючі помаранчеві голови та гаряче дихання — температура ідей у кімнаті зашкалює.",
    "why_it_works": "Показує невидиму енергію інтелектуальної битви: зовні це спокійна вечеря мільярдерів, всередині — зіткнення надрозумів.",
    "prompt_ai": "Military-grade high-definition FLIR thermal infrared camera view of four tech visionaries in discussion around a dark table. Cold cyan and indigo room background contrasting violently with bright glowing orange, yellow, and white thermal heat signatures radiating from their foreheads, hands, and coffee cups. Sicario surveillance style, 4k 24fps.",
    "davinci_recipe": "Color Page: Нода OFX False Color або градієнтна карта (Ironbow Palette) з анімацією міксу (Opacity від 0% до 85% на ключовій фразі про загрозу Google).",
    "sfx_cue": "Приглушення звуків кімнати (Low-pass filter на 400Hz), пульсуючий звук ультразвукового датчика та електронний тон 80Hz."
  },
  {
    "id": 5,
    "num": "05",
    "name_ua": "Двофокусна лінза конфлікту",
    "name_en": "The Split-Diopter Dual Reality",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "10:45 – 12:15",
    "act": "Акт 3 • Переворот ради директорів",
    "tagline": "Оптичний трюк Браяна Де Пальми: подвійна різкість у кадрі",
    "concept": "Ліва половина кадру: надчіткий макро-план (рука Сема спокійно крутить гостьовий бейдж або стискає чашку). Права половина кадру: на такій самій бритвеній різкості, за 10 метрів позаду — четверо членів ради директорів сперечаються за склом.",
    "why_it_works": "Знищує розмиття фону, змушуючи мозок глядача одночасно бачити дві протилежні правди в одному просторі без склейки.",
    "prompt_ai": "Cinematic split-diopter shot, Brian De Palma aesthetic: extreme razor-sharp macro close-up on the left of a tech leader's calm hand holding a coffee cup, while on the far right deep background, equally in razor-sharp focus, four corporate executives argue behind a glass office wall. No depth of field blur, deep optical tension, Panavision 35mm, 4k 24fps.",
    "davinci_recipe": "Fusion Page: Складання двох планів (Foreground Mask + Background Plate) з вертикальною плавною градієнтною маскою та трекінгом камери.",
    "sfx_cue": "Повний стерео-розподіл: зліва — кришталево чистий звук дихання та фарфору, справа — глухі, мов під водою, приглушені голоси з кабінету."
  },
  {
    "id": 6,
    "num": "06",
    "name_ua": "Оживлення першоджерел",
    "name_en": "The Living Archival Blueprint",
    "cat": "hud",
    "cat_label": "🖥️ Графіка & HUD",
    "cat_color": "cyan",
    "tc": "07:00 – 08:15",
    "act": "Акт 2 • Заснування OpenAI",
    "tagline": "Історичний аркуш паперу, який проростає тривимірним світлом",
    "concept": "Реальний прес-реліз або договір заснування OpenAI від 11 грудня 2015 року лежить на столі. Камера нахиляється під кутом 45 градусів — і друковані чорні літери починають світитися білим неоном, відриваються від паперу і розгортаються вгору як 3D-голограма серверного кластера.",
    "why_it_works": "Перетворює нудний архівний документ на живу магію інженерної думки.",
    "prompt_ai": "Archival document lying on dark walnut table, vintage black printed typeface suddenly illuminating with coherent cyan laser light. Printed letters physically elevate from the paper surface into a suspended 3D wireframe hologram of neural network nodes, volumetric glowing vectors, hyper-detailed macro lighting, 4k 24fps.",
    "davinci_recipe": "Fusion Page: 3D Text + Camera Tracker поверх фотоскану прес-релізу. Нода Glow + Displace з анімацією Z-позиції літер.",
    "sfx_cue": "Шурхіт старого паперу, який переростає в електронний шелест заряду іонізованого повітря."
  },
  {
    "id": 7,
    "num": "07",
    "name_ua": "Сейсмограф думки",
    "name_en": "The Typewriter Oscilloscope Punch",
    "cat": "hud",
    "cat_label": "🖥️ Графіка & HUD",
    "cat_color": "cyan",
    "tc": "02:30 – 03:30",
    "act": "Акт 1 • YC Batch 1",
    "tagline": "Звукова хвиля голосу диктора малює текст на екрані",
    "concept": "Ключова цитата Альтмана («Більшість людей здаються через психологічне тертя») малюється тонким зеленим променем аналогового лабораторного осцилографа. Лінія коливається точно в такт амплітуді голосу диктора, фіксуючи кожне слово ударом реле.",
    "why_it_works": "Глядач бачить і чує звук одночасно — фраза буквально вкарбовується в підсвідомість.",
    "prompt_ai": "Dark laboratory analog green vector oscilloscope screen displaying glowing kinetic typographic characters reacting to audio waveforms. Sharp phosphorescent phosphor decay, grid line overlay, electrical analog authenticity, moody cybernetic minimalism, 4k.",
    "davinci_recipe": "Fairlight + Fusion: Скрипт перетворення гучності аудіо A1 у параметри скейлу та сяйва ноди Text+ (Audio-driven Modifier).",
    "sfx_cue": "Синхронізовані аналогові клацання важкого тумблера + м'який тріск радіоперешкод."
  },
  {
    "id": 8,
    "num": "08",
    "name_ua": "Матч-кат масштабів: від нейрона до орбіти",
    "name_en": "The Infinite Scale Match-Cut",
    "cat": "transitions",
    "cat_label": "⚡ Монтажний перехід",
    "cat_color": "amber",
    "tc": "15:30 – 17:00",
    "act": "Акт 4 • Stargate та енергія",
    "tagline": "Безперервний політ через 7 порядків величини Всесвіту",
    "concept": "Камера летить назад без жодної зупинки: починаємо з синапсу в мозку людини -> пролітаємо крізь транзистор чіпа H100 -> крізь оптоволокно сервера -> через дах гігантського дата-центру в пустелі -> у стратосферу -> до сяючої нічної планети Земля.",
    "why_it_works": "Дає відчуття космічного масштабу штучного інтелекту як нового планетарного явища.",
    "prompt_ai": "Continuous, unbroken monumental zoom-out tracking backwards through powers of ten: from an organic microscopic glowing neural synapse, pulling out through silicon microprocessor geometry, continuing through server rack cooling fans, exiting a massive desert data center campus, soaring into Earth orbit showing illuminated continent networks against black space, 8k 24fps.",
    "davinci_recipe": "Edit Page: 5 шотів, зв'язаних через 'Scale Match' та центральний центровий трекінг. Додавання Radial Blur (Strength 0.15) на стиках переходів.",
    "sfx_cue": "Низькочастотний наростаючий гул (Shepard Tone), який створює ілюзію нескінченного прискорення."
  },
  {
    "id": 9,
    "num": "09",
    "name_ua": "Паралакс-занурення в архівні фото",
    "name_en": "The 2.5D Parallax Photo Dimensionalizer",
    "cat": "temporal",
    "cat_label": "⏳ Час і простір",
    "cat_color": "purple",
    "tc": "01:30 – 02:30",
    "act": "Акт 1 • Стенфорд 2005",
    "tagline": "Пласке старе фото перетворюється на живу тривимірну кімнату",
    "concept": "Автентичне чорно-біле фото 2005 року розділяється за допомогою AI Depth Map на 6 шарів: підлога, Сем, ноутбук, кабелі, фонова стіна. Віртуальна кінокамера обертається навколо Сема на 30 градусів, показуючи об'єм кімнати і живі тіні.",
    "why_it_works": "Знімає відчуття музейної нудьги від старих фотокарток — архів починає дихати.",
    "prompt_ai": "Stereoscopic 2.5D camera parallax move through an authentic 2005 photograph of young tech founder at desk. Layered spatial depth separation, subtle dust particles drifting between foreground cables and background wall, smooth cinematic camera orbit, photorealistic optical lighting, 4k.",
    "davinci_recipe": "Fusion: Нода Displace з використанням карти глибини (Depth Map). 3D Camera з легким покачуванням (Wobble 0.2) для ефекту живої операторської роботи.",
    "sfx_cue": "Звук старого плівкового проектора (8mm / 16mm shutter rattle) на низькій гучності -24dB."
  },
  {
    "id": 10,
    "num": "10",
    "name_ua": "Строб негативного простору",
    "name_en": "The Negative Space Strobe Transition",
    "cat": "transitions",
    "cat_label": "⚡ Монтажний перехід",
    "cat_color": "amber",
    "tc": "10:45 – 11:15",
    "act": "Акт 3 • Звільнення Сема",
    "tagline": "Психологічний удар через 3 кадри інверсії кольору",
    "concept": "На слові «Звільнено» екран на рівно 3 кадри (1/8 секунди) вибухає негативом плівки: чорні костюми стають сліпуче білими, обличчя — примарними силуетами, а світлий фон — глибоким обсидіаном. Після цього ми повертаємося в надконтрастний кінематографічний кадр.",
    "why_it_works": "Фізіологічний шоковий тригер: мозок глядача реагує на різку інверсію контрасту як на спалах блискавки.",
    "prompt_ai": "High-contrast photonegative black-and-white flash frame of a corporate boardroom betrayal, sharp silhouette inversion, stark white light bleeding from shadows, psychological shock, 35mm film flash, 4k.",
    "davinci_recipe": "Edit Page: Розріз на 3 кадри. Color Page: Нода Invert (Curves Invert) + підвищення Contrast до 1.8. Сайдчейн приглушує музику в момент спалаху.",
    "sfx_cue": "Сухий, важкий звук удару гільйотини або вимикача промислового рубильника (Metal Clank)."
  },
  {
    "id": 11,
    "num": "11",
    "name_ua": "Текстовий портал у сцену",
    "name_en": "The Kinetic Typography Teleport",
    "cat": "hud",
    "cat_label": "🖥️ Графіка & HUD",
    "cat_color": "cyan",
    "tc": "03:30 – 04:00",
    "act": "Акт 1 • Закон експоненти",
    "tagline": "Слово як фізичний тунель у наступну локацію",
    "concept": "Монументальне слово «EXPONENTIAL» виникає на весь екран у шрифті Neue Haas Grotesk. Камера на швидкості звуку летить у внутрішній круглий отвір літери «O», який виявляється вікном у хмарочосі Сан-Франциско на світанку.",
    "why_it_works": "Поєднує графічний дизайн та кінозйомку в єдиний агресивний рух без швів.",
    "prompt_ai": "Camera accelerates at warp speed through the center negative space of a giant bold white architectural letter 'O' standing in a dark void. As camera passes through, it seamlessly emerges into a panoramic sunrise aerial view of the Golden Gate Bridge and foggy San Francisco hills, 4k 24fps.",
    "davinci_recipe": "Fusion: Шар тексту використовується як Alpha Matte для відеоряду Сан-Франциско, швидкий зум (Camera Z translation 0 -> 5000) з motion blur.",
    "sfx_cue": "Стрімкий вітровий свіш (Whoosh Braam) з переходом у прозорий ембієнт ранкового міста."
  },
  {
    "id": 12,
    "num": "12",
    "name_ua": "Цифровий розвідувальний слід",
    "name_en": "The Surveillance OSINT Telemetry HUD",
    "cat": "hud",
    "cat_label": "🖥️ Графіка & HUD",
    "cat_color": "cyan",
    "tc": "06:00 – 07:00",
    "act": "Акт 2 • Готель Rosewood",
    "tagline": "Естетика розсекреченого досьє ЦРУ та супутникової аналітики",
    "concept": "Кадри вечері чи офісу супроводжуються ледь помітною монохромною моноширинною телеметрією в кутах екрана: супутникові координати Менло-Парку [37.4529° N, 122.1817° W], час UTC, висота над рівнем моря, таймер зворотного відліку до запуску ChatGPT.",
    "why_it_works": "Перетворює відео на документальний розслідувальний трилер високого рівня.",
    "prompt_ai": "Minimalist tactical surveillance HUD overlay on a luxurious nighttime Silicon Valley estate: sharp monospace telemetry coordinates, subtle green reticle crosshairs, satellite tracking vector data, elegant translucent glass aesthetic, Sicario meets Zero Dark Thirty, 4k.",
    "davinci_recipe": "Fusion: Генератор Text+ з даними витягується на окремий трек V3, режим накладання Screen, колір #38bdf8 з прозорістю 35%.",
    "sfx_cue": "Тихий звук клавіатурного терміналу або супутникового пілінгу кожні 15 секунд."
  },
  {
    "id": 13,
    "num": "13",
    "name_ua": "Центрований погляд крізь роки",
    "name_en": "The Match-Motion Eye Lock",
    "cat": "transitions",
    "cat_label": "⚡ Монтажний перехід",
    "cat_color": "amber",
    "tc": "00:00 – 00:15",
    "act": "Акт 1 • Інтродукція",
    "tagline": "Очі героя зафіксовані в одних координатах крізь 30 років",
    "concept": "Швидкий ритмічний монтаж (по 12 кадрів на людину): очі Сема зафіксовані рівно по центру екрана на рівні пікселів. 1993 (8 років) -> 2001 (16 років) -> 2008 (23 роки) -> 2015 (30 років) -> 2023 (38 років). Світ навколо обертається, але погляд залишається нерухомим.",
    "why_it_works": "Гіпнотичний візуальний якір, який створює відчуття фатальності та неперервності долі.",
    "prompt_ai": "Series of perfectly centered cinematic portraits aligned exactly by eye coordinates: young 8-year-old boy morphs through 16-year-old teen, 23-year-old founder, and 38-year-old executive. Eyes locked in dead center, lighting dynamically evolves from vintage 90s amber into sleek cold slate modern, 4k.",
    "davinci_recipe": "Edit Page: Функція Stabilization -> Mode: Classic Stabs -> Point Tracker (виставити трекінг на зіниці очей обох кадрів).",
    "sfx_cue": "Метроном або стукіт серця рівно 92 удари на хвилину, що збігається зі склейками."
  },
  {
    "id": 14,
    "num": "14",
    "name_ua": "Акустичний глітч-перехід",
    "name_en": "The Sound-Activated Glitch Dissolve",
    "cat": "transitions",
    "cat_label": "⚡ Монтажний перехід",
    "cat_color": "amber",
    "tc": "08:15 – 08:30",
    "act": "Акт 2 • Розрив з Маском",
    "tagline": "Звуковий клацальний імпульс розщеплює кольорові канали відео",
    "concept": "Перехід між темою некомерційної OpenAI та мільярдним контрактом Microsoft: клацання реле викликає 2-кадрове розщеплення RGB-каналів (червоний зсувається вліво на 15 пікселів, синій — вправо). Кадр ламається як аналогова плівка і збирається у новий кадр.",
    "why_it_works": "Фізичне відчуття технічного зламу системи — перехід на новий рівень гри.",
    "prompt_ai": "Two-frame intense analog CRT signal disruption, RGB color channel split, electrical chromatic aberration, subtle horizontal tracking distortion tearing across frame, dark moody cyberpunk realism, 4k.",
    "davinci_recipe": "Color Page: Розщеплення каналів через ноду Splitter/Combiner, зміщення ноди Red на 10 пікселів у трансформації.",
    "sfx_cue": "Автентичний звук електростатичного розряду (Spark Discharge) тривалістю 0.08с."
  },
  {
    "id": 15,
    "num": "15",
    "name_ua": "Чорнильна капілярність долі",
    "name_en": "The Fluid Ink Bleed Decision Tree",
    "cat": "temporal",
    "cat_label": "⏳ Час і простір",
    "cat_color": "purple",
    "tc": "04:45 – 05:45",
    "act": "Акт 2 • Президентство YC",
    "tagline": "Крапля чорнила, яка розгалужується у венчурну імперію",
    "concept": "Ультрамакрозйомка: перо торкається білого паперу. Крапля чорнила в сповільненій зйомці розтікається по волокнах. Її відгалуження перетворюються на світяться золоті гілки інвестиційного графа — Reddit, Stripe, Airbnb, Coinbase, Helion.",
    "why_it_works": "Метафора того, як один розчерк пера та одне рішення розгалужує реальність на трильйони доларів.",
    "prompt_ai": "Macro slow motion shot of black and gold ink dropping onto textured cotton paper, capillary fibers absorbing the liquid as it branches outward into an organic fractal pattern resembling venture capital decision tree and neural networks. Hyper-detailed fluid dynamics, 8k 24fps.",
    "davinci_recipe": "Fusion: Режим Composite (Multiply) макро-футажу розтікання чорнила + трекінг золотих точок-вузлів (Tracker 3D).",
    "sfx_cue": "Глибокий водяний звук краплі з довгим ревербераційним хвостом (Sub Aquatic Drop)."
  },
  {
    "id": 16,
    "num": "16",
    "name_ua": "Горизонтальний світловий розгін",
    "name_en": "The Anamorphic Streak Speed Warp",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "09:30 – 10:15",
    "act": "Акт 3 • Запуск ChatGPT",
    "tagline": "Анаморфотні сині промені гіперпростору на форматі 2.39:1",
    "concept": "Коли ChatGPT набирає 100 мільйонів користувачів, фон за спиною героя перетворюється на горизонтальні розтягнуті сині світлові смуги анаморфотного об'єктива (Cineovision Anamorphic Flare). Людина стоїть у центрі, а світ навколо летить у гіперпростір.",
    "why_it_works": "Класичний прийом масштабної наукової фантастики Крістофера Нолана для позначення сингулярності.",
    "prompt_ai": "Cinematic wide 2.39:1 scope shot: central silhouette of a thinker standing completely still while background city architecture warps into intense horizontal cyan and cobalt anamorphic light streaks, warp speed optical streaks, Interstellar aesthetic, 4k 24fps.",
    "davinci_recipe": "Color Page: Нода OFX Anamorphic Flares (Streak Angle: 0 deg, Threshold 0.8, Color: Deep Cyan #0ea5e9).",
    "sfx_cue": "Стереофонічний наростаючий резонанс реактивної турбіни (Jet Engine spooling down into low hum)."
  },
  {
    "id": 17,
    "num": "17",
    "name_ua": "Плівковий опік Kodak 2383",
    "name_en": "The Chromatic Halation Flash",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "07:45 – 08:00",
    "act": "Акт 2 • Масштаб вирішує все",
    "tagline": "Червоно-помаранчевий оксамитовий ореол хімічної плівки",
    "concept": "У момент озвучення ключової гіпотези («Масштаб вирішує все») всі яскраві джерела світла в кадрі (лампи, вікна, відблиски на склі) спалахують оксамитовим червоним свіченням (Halation) — фізичним ефектом відбиття світла від підкладки справжньої 35-мм плівки Kodak.",
    "why_it_works": "Додає теплоти та аналогової душі в стерильний комп'ютерний світ штучного інтелекту.",
    "prompt_ai": "Photorealistic 35mm film frame showing authentic warm red-orange photographic halation bleeding around highlights, vintage Kodak 2383 chemical film response, rich organic textures, moody cinematic warmth, 4k.",
    "davinci_recipe": "Color Page: Нода OFX Halation (Spread: 0.65, Hue: 0.05, Saturation: 1.2, Blend: 0.45 на ключових кадрах).",
    "sfx_cue": "Легкий теплий шурхіт вінілової платівки та низький теплий тон віолончелі."
  },
  {
    "id": 18,
    "num": "18",
    "name_ua": "Дзеркальний тунель рекурсії AGI",
    "name_en": "The Recursive Screen Infinity",
    "cat": "temporal",
    "cat_label": "⏳ Час і простір",
    "cat_color": "purple",
    "tc": "16:00 – 17:00",
    "act": "Акт 4 • Самовдосконалення AGI",
    "tagline": "Камера, що нескінченно залітає в саму себе крізь екрани",
    "concept": "Ноутбук на столі показує вікно коду, де запускається модель. Камера залітає в екран — і всередині нього знову стоїть цей стіл з цим ноутбуком, де запускається потужніша модель. Нескінченний фрактальний рух углиб рекурсії.",
    "why_it_works": "Найточніша візуальна метафора технологічної сингулярності: модель, яка навчає ще розумнішу модель.",
    "prompt_ai": "Hypnotic recursive infinite zoom through computer screens: camera continuously flies forward into a terminal window on a desk, which opens into an identical room with an identical computer at exponentially higher resolution, fractal technological infinity, Christopher Nolan Inception style, 4k 24fps.",
    "davinci_recipe": "Fusion: Поєднання однакового футажу у 3D-просторі з циклічним зміщенням TimeSpeed та Scale 0.5 на кожен шар.",
    "sfx_cue": "Аудіо-ефект безкінечного падіння тону (Risset Drum / Shepard Tone Glissando)."
  },
  {
    "id": 19,
    "num": "19",
    "name_ua": "Вакуум тиші та світловий обвал",
    "name_en": "The Silence Vacuum / Blackout Snap",
    "cat": "acoustic",
    "cat_label": "🔊 Звук і тиша",
    "cat_color": "rose",
    "tc": "10:45 – 11:00",
    "act": "Акт 3 • Момент перевороту",
    "tagline": "Повна абсолютна тиша 0.0 dB як найгучніший момент фільму",
    "concept": "За 1.5 секунди до фрази про звільнення вся музика, ембієнт, фонові шуми і дихання моментально зрізаються в 0.0 dB. Екран стає абсолютно чорним. Глядач затримує подих у повній темряві. Потім — надточний сухий звук клацання мишки і спалах кадру.",
    "why_it_works": "Контраст — найсильніша зброя режисера. Повна тиша б'є по сприйняттю сильніше за будь-який вибух.",
    "prompt_ai": "Absolute void graphite-black screen snapping abruptly into a high-tension close-up of a laptop camera lens reflecting a shockwave of cold daylight, stark dramatic minimalism, 4k.",
    "davinci_recipe": "Fairlight: Master Bus Mute на 1.5 секунди (жорсткий Cut без Fade). Edit Page: Чорний генеруючий кліп (Solid Color Black) на 36 кадрів.",
    "sfx_cue": "Повний вакуум 0.0 dB (навіть шум приміщення вимкнено), потім один сухий клік мишки Apple Magic Mouse на -2 dB."
  },
  {
    "id": 20,
    "num": "20",
    "name_ua": "Розчинення матеріального світу у вектори",
    "name_en": "The Horizon Blueprint Wireframe Finale",
    "cat": "temporal",
    "cat_label": "⏳ Час і простір",
    "cat_color": "purple",
    "tc": "18:30 – 20:00",
    "act": "Акт 4 • Фінал епізоду",
    "tagline": "Фізичні будинки та мости розпадаються на золотий бінарний код",
    "concept": "Нічний панорамний вид Сан-Франциско та серверних кластерів. Поступово бетон, асфальт і метал втрачають щільність, просвічуючись золотою тривимірною сіткою векторів. Місто стає струменями коду, які піднімаються в зоряне небо.",
    "why_it_works": "Фінальний акорд до слів: «Світ набагато пластичніший, ніж здається. Його створюють просто зараз».",
    "prompt_ai": "Majestic nocturnal cityscape of San Francisco and modern suspension bridges slowly dissolving into vertical rising streams of golden binary code and luminous vector wireframes. Physical architecture becomes pure light energy ascending into deep starry space, Oppenheimer meets Matrix poetic realism, 4k 24fps.",
    "davinci_recipe": "Color + Fusion: Нода Edge Detect (Колір золотий #f59e0b) змішується через Dissolve з реальним нічним планом міста.",
    "sfx_cue": "Фінальний акорд саундтреку Suno з довгим 6-секундним ревербераційним згасанням у зоряний шум."
  }
]

def generate_html():
    cards_html = ""
    for item in INNOVATIONS:
        cards_html += f"""
        <article class="innov-card" data-cat="{item['cat']}" id="innov-{item['num']}">
          <div class="innov-header">
            <div class="innov-meta">
              <span class="innov-num">#{item['num']}</span>
              <span class="badge badge-{item['cat_color']}">{item['cat_label']}</span>
              <span class="badge badge-subtle">{item['act']}</span>
              <span class="badge badge-tc">⏱️ {item['tc']}</span>
            </div>
            <h3 class="innov-title">{item['name_ua']} <span class="innov-en">/ {item['name_en']}</span></h3>
            <p class="innov-tagline">«{item['tagline']}»</p>
          </div>

          <div class="innov-body">
            <div class="innov-section">
              <div class="section-label">🎬 Концепція & Візуальний ефект</div>
              <p class="section-text">{item['concept']}</p>
            </div>

            <div class="innov-section">
              <div class="section-label">🧠 Чому це працює на глядача (Психологія сприйняття)</div>
              <p class="section-text highlight-text">{item['why_it_works']}</p>
            </div>

            <div class="innov-section">
              <div class="section-label" style="display:flex;justify-content:space-between;align-items:center;">
                <span>✨ Промпт для Google Veo 2 / Flow / Midjourney</span>
                <button class="copy-btn" onclick="copyText('prompt-{item['num']}', this)">📋 Копіювати промпт</button>
              </div>
              <pre class="code-block" id="prompt-{item['num']}">{item['prompt_ai']}</pre>
            </div>

            <div class="innov-footer-grid">
              <div class="footer-box">
                <span class="footer-label">🛠️ Рецепт монтажу в DaVinci Resolve 19</span>
                <p class="footer-text">{item['davinci_recipe']}</p>
              </div>
              <div class="footer-box">
                <span class="footer-label">🔊 Саунд-дизайн (Fairlight SFX)</span>
                <p class="footer-text">{item['sfx_cue']}</p>
              </div>
            </div>
          </div>
        </article>
        """

    full_html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>20 Кінематографічних Фішок & Інновацій Монтажу • AI Titans Thoughtcast</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-dark: #08090d;
      --bg-card: #0f121a;
      --bg-card-hover: #151a26;
      --border: rgba(255, 255, 255, 0.08);
      --border-accent: rgba(56, 189, 248, 0.3);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --cyan: #38bdf8;
      --emerald: #34d399;
      --amber: #fbbf24;
      --purple: #a78bfa;
      --rose: #fb7185;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      padding-bottom: 5rem;
    }}

    /* Header Bar */
    .top-header {{
      background: rgba(15, 18, 26, 0.85);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.9rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
    }}
    .brand-logo {{
      width: 34px;
      height: 34px;
      border-radius: 9px;
      background: linear-gradient(135deg, #0284c7, #6366f1);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      box-shadow: 0 0 16px rgba(56, 189, 248, 0.35);
    }}
    .brand-title {{ font-size: 15px; font-weight: 700; letter-spacing: -0.3px; }}
    .brand-sub {{ font-size: 11.5px; color: var(--text-muted); }}

    .nav-actions {{ display: flex; gap: 0.75rem; align-items: center; }}
    .btn {{
      padding: 0.5rem 1rem;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-outline {{
      background: transparent;
      border: 1px solid var(--border);
      color: var(--text-muted);
    }}
    .btn-outline:hover {{ border-color: var(--cyan); color: #fff; background: rgba(56, 189, 248, 0.08); }}
    .btn-cyan {{
      background: linear-gradient(135deg, #0284c7, #0ea5e9);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #fff;
    }}
    .btn-cyan:hover {{ filter: brightness(1.15); transform: translateY(-1px); }}

    /* Hero Banner */
    .hero-banner {{
      max-width: 1300px;
      margin: 2rem auto 1.5rem;
      padding: 0 1.5rem;
    }}
    .hero-box {{
      background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.12), transparent 70%),
                  radial-gradient(circle at top right, rgba(167, 139, 250, 0.1), transparent 60%),
                  var(--bg-card);
      border: 1px solid var(--border-accent);
      border-radius: 18px;
      padding: 2.2rem;
      position: relative;
      overflow: hidden;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 0.3rem 0.8rem;
      border-radius: 999px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--cyan);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -0.8px;
      line-height: 1.25;
      margin-bottom: 0.8rem;
    }}
    .hero-desc {{
      font-size: 15px;
      color: var(--text-muted);
      max-width: 880px;
      line-height: 1.65;
    }}

    /* Filter Bar */
    .filter-wrap {{
      max-width: 1300px;
      margin: 0 auto 2rem;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .filters {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }}
    .filter-pill {{
      padding: 0.45rem 0.9rem;
      border-radius: 8px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .filter-pill:hover {{ color: #fff; border-color: rgba(255,255,255,0.25); }}
    .filter-pill.active {{
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--cyan);
      color: var(--cyan);
    }}
    .search-box {{
      position: relative;
      min-width: 260px;
    }}
    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border);
      color: #fff;
      padding: 0.48rem 0.85rem 0.48rem 2.2rem;
      border-radius: 8px;
      font-size: 12.5px;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{ border-color: var(--cyan); }}
    .search-icon {{
      position: absolute;
      left: 10px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 13px;
      color: var(--text-muted);
    }}

    /* Cards Grid */
    .grid-wrap {{
      max-width: 1300px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(580px, 1fr));
      gap: 1.5rem;
    }}
    @media (max-width: 768px) {{
      .grid-wrap {{ grid-template-columns: 1fr; }}
    }}

    .innov-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1.6rem;
      display: flex;
      flex-direction: column;
      gap: 1.1rem;
      transition: all 0.25s ease;
      position: relative;
    }}
    .innov-card:hover {{
      border-color: rgba(56, 189, 248, 0.35);
      background: var(--bg-card-hover);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4);
      transform: translateY(-2px);
    }}

    .innov-meta {{
      display: flex;
      gap: 0.5rem;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 0.6rem;
    }}
    .innov-num {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.12);
      padding: 2px 7px;
      border-radius: 5px;
    }}
    .badge {{
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 5px;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.15); color: var(--emerald); border: 1px solid rgba(52, 211, 153, 0.3); }}
    .badge-purple {{ background: rgba(167, 139, 250, 0.15); color: var(--purple); border: 1px solid rgba(167, 139, 250, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.15); color: var(--amber); border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.15); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-rose {{ background: rgba(251, 113, 133, 0.15); color: var(--rose); border: 1px solid rgba(251, 113, 133, 0.3); }}
    .badge-subtle {{ background: rgba(255, 255, 255, 0.05); color: var(--text-muted); }}
    .badge-tc {{ background: rgba(0, 0, 0, 0.4); color: var(--text-main); font-family: var(--font-mono); font-size: 11px; }}

    .innov-title {{
      font-size: 19px;
      font-weight: 700;
      letter-spacing: -0.4px;
      color: #fff;
      line-height: 1.35;
    }}
    .innov-en {{
      color: var(--text-muted);
      font-weight: 500;
      font-size: 15px;
    }}
    .innov-tagline {{
      font-size: 13px;
      color: var(--cyan);
      font-style: italic;
      margin-top: 4px;
    }}

    .section-label {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      letter-spacing: 0.6px;
      margin-bottom: 5px;
    }}
    .section-text {{
      font-size: 13.5px;
      color: #cbd5e1;
      line-height: 1.55;
    }}
    .highlight-text {{
      color: #f1f5f9;
      background: rgba(255, 255, 255, 0.03);
      padding: 0.6rem 0.8rem;
      border-radius: 7px;
      border-left: 2px solid var(--amber);
      font-size: 13px;
    }}

    .code-block {{
      background: #06070a;
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 8px;
      padding: 0.85rem;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: #93c5fd;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }}

    .copy-btn {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 3px 8px;
      border-radius: 5px;
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .copy-btn:hover {{
      background: var(--cyan);
      color: #000;
      border-color: var(--cyan);
    }}

    .innov-footer-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.85rem;
      margin-top: 0.4rem;
      padding-top: 0.85rem;
      border-top: 1px solid var(--border);
    }}
    @media (max-width: 600px) {{
      .innov-footer-grid {{ grid-template-columns: 1fr; }}
    }}
    .footer-box {{
      background: rgba(0, 0, 0, 0.25);
      padding: 0.65rem 0.8rem;
      border-radius: 7px;
      border: 1px solid rgba(255, 255, 255, 0.04);
    }}
    .footer-label {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      display: block;
      margin-bottom: 3px;
      letter-spacing: 0.5px;
    }}
    .footer-text {{
      font-size: 12px;
      color: #94a3b8;
      line-height: 1.45;
    }}

    /* Toast */
    #toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0284c7;
      color: #fff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 600;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.25s ease;
      z-index: 999;
      pointer-events: none;
    }}
    #toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header class="top-header">
    <a href="index.html" class="brand">
      <div class="brand-logo">✨</div>
      <div>
        <div class="brand-title">AI TITANS THOUGHTCAST</div>
        <div class="brand-sub">Режисерська Лабораторія Візуальних Інновацій</div>
      </div>
    </a>
    <div class="nav-actions">
      <a href="index.html" class="btn btn-outline">⬅️ Головна Студія</a>
      <a href="episodes/ep01_altman.html" class="btn btn-outline">🎙️ Епізод 01 (Альтман)</a>
      <a href="#innov-01" class="btn btn-cyan">🚀 До першої фішки</a>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-banner">
    <div class="hero-box">
      <span class="hero-badge">Auteur Cinema Lookbook • 20 Master Devices</span>
      <h1 class="hero-title">20 Кінематографічних Фішок & Інновацій Монтажу</h1>
      <p class="hero-desc">
        Повний арсенал авторських візуальних трюків, оптичних ефектів, кінетичної графіки та саунд-дизайну для подолання рандомності ШІ-відео. Кожна фішка прив'язана до точного таймкоду Епізоду 01 (Сем Альтман) і містить готовий промпт для Google Veo 2 / Flow та покроковий рецепт зведення у DaVinci Resolve 19 Studio.
      </p>
    </div>
  </section>

  <!-- Filter & Search Bar -->
  <div class="filter-wrap">
    <div class="filters">
      <button class="filter-pill active" data-filter="all">Всі 20 Фішок</button>
      <button class="filter-pill" data-filter="optics">🔍 Оптичні трюки (6)</button>
      <button class="filter-pill" data-filter="transitions">⚡ Монтажні переходи (5)</button>
      <button class="filter-pill" data-filter="hud">🖥️ Графіка & HUD (4)</button>
      <button class="filter-pill" data-filter="temporal">⏳ Час і простір (4)</button>
      <button class="filter-pill" data-filter="acoustic">🔊 Звук і тиша (1)</button>
    </div>
    <div class="search-box">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" class="search-input" placeholder="Пошук по назві або промпту...">
    </div>
  </div>

  <!-- Cards Grid -->
  <main class="grid-wrap" id="innovGrid">
    {cards_html}
  </main>

  <div id="toast">Скопійовано в буфер обміну!</div>

  <script>
    function copyText(elemId, btn) {{
      var text = document.getElementById(elemId).innerText;
      navigator.clipboard.writeText(text).then(function() {{
        showToast("✓ Промпт скопійовано для генерації!");
        var orig = btn.innerText;
        btn.innerText = "✓ Скопійовано!";
        btn.style.background = "#34d399";
        btn.style.color = "#000";
        setTimeout(function() {{
          btn.innerText = orig;
          btn.style.background = "";
          btn.style.color = "";
        }}, 2000);
      }});
    }}

    function showToast(msg) {{
      var t = document.getElementById("toast");
      t.innerText = msg;
      t.classList.add("show");
      setTimeout(function() {{ t.classList.remove("show"); }}, 2500);
    }}

    // Filter Pills
    var pills = document.querySelectorAll(".filter-pill");
    pills.forEach(function(pill) {{
      pill.addEventListener("click", function() {{
        pills.forEach(function(p) {{ p.classList.remove("active"); }});
        pill.classList.add("active");
        var cat = pill.getAttribute("data-filter");
        filterCards(cat, document.getElementById("searchInput").value);
      }});
    }});

    // Search Input
    document.getElementById("searchInput").addEventListener("input", function(e) {{
      var activePill = document.querySelector(".filter-pill.active");
      var cat = activePill ? activePill.getAttribute("data-filter") : "all";
      filterCards(cat, e.target.value);
    }});

    function filterCards(cat, searchStr) {{
      var q = searchStr.toLowerCase().trim();
      var cards = document.querySelectorAll(".innov-card");
      cards.forEach(function(card) {{
        var cardCat = card.getAttribute("data-cat");
        var text = card.innerText.toLowerCase();
        var matchCat = (cat === "all" || cardCat === cat);
        var matchSearch = (!q || text.indexOf(q) !== -1);
        if (matchCat && matchSearch) {{
          card.style.display = "";
        }} else {{
          card.style.display = "none";
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    return full_html

if __name__ == "__main__":
    html_content = generate_html()
    
    paths = [
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/cinematic_innovations.html",
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/docs/cinematic_innovations.html"
    ]
    for p in paths:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Generated {p} ({len(html_content)} bytes)")
