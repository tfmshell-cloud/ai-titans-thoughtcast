#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Episode 02 (Jensen Huang) - 20 Cinematic Triads (Start -> Morph -> End)
Tailored for Google Flow / Veo 2, 100% Policy-Safe, with DaVinci Resolve recipes & SFX cues.
"""

import os

INNOVATIONS = [
  {
    "id": 1,
    "num": "01",
    "name_ua": "Рентген фаянсу та кремнію",
    "name_en": "The Porcelain-to-Silicon Displace",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "00:00 – 00:20",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Безшовний перехід від брудної підлоги реформаторію до кремнієвої кузні сучасності",
    "concept": "Камера дивиться впритул на тріснуту білу кахельну плитку в темній душовій 1970-х років. Холодна крапля води стікає вниз, торкається іржавої труби. У момент падіння краплі фаянс стає напівпрозорим, а тріщини перетворюються на золоті мікродоріжки кремнієвого кристала надвисокої щільності.",
    "why_it_works": "Миттєво задає головний контраст життя героя: найнижча фізична праця як підґрунтя для будівництва найпотужнішої технологічної імперії століття.",
    "p1_start": "Extreme macro cinematic shot of cold water droplets sliding down cracked white porcelain tile in a dark 1970s institutional dormitory restroom, rusty iron plumbing pipe in foreground, moody desaturated cyan and amber lighting, heavy 35mm film grain, shallow depth of field --ar 16:9",
    "p2_flow": "Continuous macro push-in camera plunging through the cracked white tile into the microscopic substrate. Solid ceramic dissolves into crystalline green silicon wafer, water drops morph into liquid gold binary laser tracks pulsing at high speed through billions of microscopic transistors, seamless physical morph, 24fps.",
    "p3_end": "Hyperrealistic scientific electron-microscope style photograph of an ultra-dense emerald-green and gold semiconductor microchip wafer. Nanoscale transistor gates illuminated with coherent azure laser pulses, dark slate background, volumetric depth, photorealistic semiconductor geometry, 8k render --ar 16:9",
    "davinci_recipe": "Fusion Page: Displace Node з альфа-маскою тріщин фаянсу. Застосувати Color Match між відтінками іржі та мідних доріжок. Монтажний стик на звуці удару краплі води (Sub-boom 40Hz).",
    "sfx_cue": "Важкий глухий звук падіння краплі води в порожньому кахельному приміщенні (ревер 4.5с). На переході — раптовий наростаючий високочастотний гул кремнієвого імпульсу на -6 dB."
  },
  {
    "id": 2,
    "num": "02",
    "name_ua": "Туманний шлях до Аппалачів",
    "name_en": "The Appalachian Forest Mist Drift",
    "cat": "retro",
    "cat_label": "📻 Ретро-хроніка",
    "cat_color": "purple",
    "tc": "00:20 – 00:45",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Одинокий силует дитини біля розбитої гірської дороги та темні ялиці Онейди",
    "concept": "Камера на рівні колін повільно веде по вологій гравійній дорозі в горах Аппалачі. Попереду — самотній дев'ятирічний хлопчик з дешевою вініловою валізою. Камера входить у густий гірський туман, з якого поступово проступає суворий червоний цегляний корпус баптистського інституту-реформаторію.",
    "why_it_works": "Передає почуття повної самотності та відірваності від рідного дому дев'ятирічного емігранта, який ще не розуміє мови чужої країни.",
    "p1_start": "Moody 1972 vintage 35mm color photograph of a lonely 9-year-old Taiwanese-American boy standing on a wet gravel mountain road holding a worn brown vinyl suitcase, Appalachian pine trees shrouded in mist, autumnal cold dusk light, authentic vintage Kodachrome grain --ar 16:9",
    "p2_flow": "Slow atmospheric dolly forward tracking through dense mountain fog. The silhouette of the boy remains anchored while the mist rolls across the lens; trees part to reveal the imposing red-brick Victorian facade of a remote mountain reformatory boarding school with dim yellow tungsten windows, 24fps.",
    "p3_end": "Atmospheric cinematic dusk shot of the remote Appalachian red-brick boarding academy, yellow tungsten windows glowing faintly through misty pine trees, wet asphalt road in foreground, cinematic anamorphic lens, melancholic mood, 4k --ar 16:9",
    "davinci_recipe": "Edit Page: Повільний Linear Push-In 105% -> 118%. Color Page: лут Kodak 5207, підсилений синій у тінях (Lift +0.03 Blue), спад насиченості на 18% для створення відчуття холоду.",
    "sfx_cue": "Далекий порив вітру в ялинових гілках, шелест гравію під підошвами дитячого черевика. Тихий мінорний перебір електрогітари з глибоким тремоло на -14 dB."
  },
  {
    "id": 3,
    "num": "03",
    "name_ua": "Пакт виживання: світло і тінь",
    "name_en": "The Survival Pact Shadow Two-Shot",
    "cat": "split",
    "cat_label": "⚡ Драматичний розкол",
    "cat_color": "amber",
    "tc": "00:45 – 01:15",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Від аніме-графіки до жорсткого кінематографічного реалізму кімнати гуртожитку",
    "concept": "Починається як стилізований графічний роман: маленький хлопчик сидить на нижньому ярусі двох'ярусного ліжка навпроти 17-річного сусіда, вкритого тюремними татуюваннями та шрамами. Контурні лінії малюнка плавно розчиняються, поступаючись місцем живій текстурі шкіри, дереву ліжка та пилу під тьмяною лампою.",
    "why_it_works": "Показує момент прийняття дорослого рішення: замість сліз маленький хлопчик пропонує силу інтелекту в обмін на фізичний захист.",
    "p1_start": "Graphic novel animation style: an expressive cinematic two-shot of an 8-year-old boy sitting on a bunk bed opposite a 17-year-old rugged teenager covered in tattoos in a dim rustic dormitory room, high-contrast expressive line art, deep shadows, dramatic mood --ar 16:9",
    "p2_flow": "Seamless morph from graphic novel illustration to hyperrealistic 35mm live-action cinema. Hand-drawn ink outlines soften and dissolve; flat tones transform into nuanced skin textures, warm tungsten lamp falloff, floating dust particles, and weathered wooden bunk textures, 24fps.",
    "p3_end": "Gritty 1973 cinematic film still: intimate two-shot in a dim dormitory room, a quiet 8-year-old boy reading an English textbook beside a rough older teenage boy whittling wood with a pocketknife, authentic period atmosphere, soft golden rim light, 35mm film grain, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Morph Dissolve з ручною маскою контурів обличчя та рук. Застосувати Film Damage (Jitter 0.02, Dust 0.05) для зшивання анімації з живою плівкою.",
    "sfx_cue": "Глухий удар саб-басу 40Hz. Сухий звук розкриття старої книги, тихе шкрябання леза по дереву, яке розчиняється в гулі приміщення."
  },
  {
    "id": 4,
    "num": "04",
    "name_ua": "Алхімія словника",
    "name_en": "The Tactile Dictionary Typography Bloom",
    "cat": "typo",
    "cat_label": "🔤 Кінетична типографіка",
    "cat_color": "cyan",
    "tc": "01:15 – 02:15",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Як дитячий палець на пожовклих сторінках перетворює хаос чужої мови на алгоритм розуміння",
    "concept": "Макро-кадр сторінки кишенькового англійського словника 1970-х років. Маленький палець дитини веде під друкованими рядками. Літери починають випромінювати бурштинове сяйво, відриваються від сторінки у вигляді тривимірних векторів і формують структурований потік символів навколо очей хлопчика.",
    "why_it_works": "Візуалізує народження аналітичного розуму: кожне нове слово стає цеглиною у побудові мосту до влади над світом.",
    "p1_start": "Extreme macro top-down photograph of an open yellowed 1970s English paperback dictionary page on a scratched wooden table, a small child's finger tracing beneath printed phonetic definitions, tactile fibrous paper texture, warm single tungsten desk lamp lighting --ar 16:9",
    "p2_flow": "Camera glides into an extreme low-angle macro tilt. The printed black ink letters start to glow with warm amber luminescence, physically lifting off the fibrous page into floating 3D typography particles, swirling around the child's hand into a structured stream of glowing semantic vectors, 24fps.",
    "p3_end": "Cinematic 35mm close-up of a young boy's dark, determined eyes in soft warm profile lighting, pupils reflecting streams of floating illuminated golden letterforms and linguistic glyphs, shallow depth of field, atmospheric room tone, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Text+ з модифікатором Follower, 3D Particle Emitter по траєкторії руху пальця. Color: Glow на каналі Highlights, теплий золотий відтінок (Hue 42°).",
    "sfx_cue": "Шелест паперу високої чіткості, сухий шорох пучки пальця по волокнах сторінки. Тонкий кришталевий дзвін (Chime) на підйомі літер."
  },
  {
    "id": 5,
    "num": "05",
    "name_ua": "Гідравлічна геометрія приниження",
    "name_en": "The Hydro-Mechanical Choreography",
    "cat": "macro",
    "cat_label": "🔬 Макро-світ",
    "cat_color": "emerald",
    "tc": "02:15 – 03:30",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Перетворення чищення унітазів на бездоганну інженерну оптимізацію траєкторій",
    "concept": "Починається з динамічного мультфільму/аніме: рух щітки, мильна піна розлітається по кахлю, утворюючи математичні спіралі. Потім камера опускається вниз, піна змивається струменем чистої води, і під нею відкривається дзеркально чистий білий фаянс, у якому відбивається ранкове сонце.",
    "why_it_works": "Ілюструє ключовий життєвий принцип героя: будь-яка праця, навіть найбрудніша, може бути перетворена на високе мистецтво інженерної дисципліни.",
    "p1_start": "Stylized graphic novel animation frame: high-angle dramatic shot of a young boy vigorously scrubbing restroom floor tiles with a stiff brush, soapy foam swirling in dynamic motion lines, sharp ink cross-hatching, vibrant comic contrast --ar 16:9",
    "p2_flow": "High-angle camera tilts smoothly downward. The cartoonish soap foam swirls into a perfect logarithmic Archimedean spiral; water foam dissolves into clean engineering grid lines as a powerful cascade of clear water washes across the floor, wiping away all stylized ink into living reality, 24fps.",
    "p3_end": "Photorealistic macro live-action frame of sparkling, pristine white bathroom tile reflecting clean morning sunbeams cutting through high frosted windows, wet water droplets glistening on porcelain, tangible 35mm film texture, 4k --ar 16:9",
    "davinci_recipe": "Edit: Match cut на сплеску води. Fusion: FastNoise Displacement з маскою води для переходу текстури. Fairlight: різкий зріз шумів щітки на -20 dB при появі чистого кахлю.",
    "sfx_cue": "Ритмічний жорсткий скрип щетини по мокрому кахлю в ревері. Раптовий потужний сплеск чистої прохолодної води, що змиває всі звуки в кришталеву тишу."
  },
  {
    "id": 6,
    "num": "06",
    "name_ua": "Неоновий пар закусочної Denny's",
    "name_en": "The Roadside Diner Steam Warp",
    "cat": "retro",
    "cat_label": "📻 Ретро-хроніка",
    "cat_color": "purple",
    "tc": "03:30 – 05:15",
    "act": "Акт 1 • Холод Кентуккі 1972",
    "tagline": "Нічна зміна 15-річного посудомийника: подолання страху через ритм киплячої води",
    "concept": "Камера дивиться крізь залите дощем нічне вікно придорожньої закусочної 1978 року. Жовтий і червоний неоновий напис тремтить у мокрому асфальті. Камера безшовно проходить крізь скло, пробивається через хмари гарячої білої пари на кухні й вихоплює 15-річного підлітка у білому фартуху, який сортує тарілки зі швидкістю конвеєра.",
    "why_it_works": "Показує момент, де згорів підлітковий страх перед людьми. Закусочна стає університетом характеру та інкубатором майбутнього стартапу.",
    "p1_start": "Vintage 1978 neon exterior shot through rain-streaked plate glass of an American 24-hour roadside diner at 2 AM, glowing neon reflections vibrating on wet black asphalt, misty rain, cinematic Kodak 5247 film aesthetic --ar 16:9",
    "p2_flow": "Camera moves continuously forward, phasing through the rain-covered glass into thick rising plumes of dense white culinary steam. Steam swirls around the lens, warm orange kitchen lighting replaces the cool exterior rain, revealing a bustling stainless-steel commercial dishwashing station, 24fps.",
    "p3_end": "Gritty 35mm documentary film still of a 15-year-old Taiwanese-American teenage busboy in a white cotton apron sorting heavy ceramic diner plates with robotic speed at a commercial dish machine, sweat on brow, warm copper overhead heat lamps, 4k --ar 16:9",
    "davinci_recipe": "Color: Split-toning: холодний Teal назовні (Gain Blue/Cyan), глибокий теплий Amber на кухні (Gamma Orange/Red). Повільний Whip Pan через хмару пари.",
    "sfx_cue": "Приглушений шум зливи за вікном, далекий гудок вантажівки. На проході крізь скло — різке шипіння пари посудомийної машини на -4 dB та гуркіт порцелянових тарілок."
  },
  {
    "id": 7,
    "num": "07",
    "name_ua": "Креслення на паперовій серветці",
    "name_en": "The Napkin Blueprint Ignition",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "emerald",
    "tc": "05:15 – 06:30",
    "act": "Акт 2 • Тридцять днів до темряви 1993",
    "tagline": "Як кілька ліній синьої кулькової ручки запалили революцію тривимірної графіки",
    "concept": "Макро-кадр дешевої паперової серветки на пластиковому столику в закусочній. Поруч стоїть товста кавова чашка з чорною кавою. На серветці нашвидкуруч кульковою ручкою накреслено схему графічного співпроцесора. Чорнило на серветці починає світитися смарагдово-зеленим світлом і піднімається у повітря у вигляді об'ємної 3D-голограми чіпа.",
    "why_it_works": "Культовий момент народження кремнієвого гіганта: перехід від абстрактної мрії за чашкою кави до конкретної фізичної мікроархітектури.",
    "p1_start": "Extreme macro close-up of a cheap white fibrous paper napkin on a green laminate roadside diner booth table, rough hand-drawn microprocessor architecture diagrams in blue ballpoint pen ink, beside a ceramic mug of steaming black coffee, warm morning light --ar 16:9",
    "p2_flow": "Camera glides into a 45-degree isometric tilt. The blue ballpoint pen ink lines begin to warm up, glowing with coherent emerald-green laser illumination. The strokes physically detach from the paper napkin, rising vertically into a rotating multi-layered 3D holographic wireframe schematic, 24fps.",
    "p3_end": "Hyperrealistic 3D holographic schematic of a parallel graphics processing architecture hovering over the dark diner table, glowing green and gold geometric vectors, volumetric light beams cutting through coffee steam, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Camera Tracker по столу та чашці кави. Мердж об'ємної сітки через Additive Mode. Налаштування Glow (Threshold 0.65, Spread 0.25) для смарагдового контуру.",
    "sfx_cue": "Тихий дзвін ложечки об край кавової чашки. Тихе потріскування статичної електрики (Arc weld sound) у момент спалаху ліній серветки."
  },
  {
    "id": 8,
    "num": "08",
    "name_ua": "Скляні кулі Сан-Хосе",
    "name_en": "The Bullet-Hole Window Parallax",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "06:00 – 06:30",
    "act": "Акт 2 • Тридцять днів до темряви 1993",
    "tagline": "Стартап під кулями: пробите скло закусочної як оптична лінза у майбутнє",
    "concept": "Камера дивиться зсередини нічної закусочної: троє молодих інженерів у півтіні за столиком. На передньому плані у вітринному склі — круглий слід від кулі каліфорнійської вуличної банди. Камера наближається до тріщин навколо кульового отвору, проходить крізь нього у ніч, де вогні траси перетворюються на смуги даних.",
    "why_it_works": "Підкреслює абсурдну жорсткість умов, у яких створювалася компанія: ніякого захищеного венчурного раю, тільки холодний ризик і віра в ідею.",
    "p1_start": "Cinematic 3-person silhouette in a dimly lit roadside diner booth at 3 AM: three young tech founders leaning over blueprints, a prominent bullet impact hole in the heavy plate-glass window in foreground with spiderweb cracks, moody neon lighting --ar 16:9",
    "p2_flow": "Slow macro dolly push-in directly aiming into the center of the bullet hole fracture. Lens flares catch the spiderweb glass cracks; as the camera punches through the glass void, the distant city freeway tail-lights warp into infinite anamorphic horizontal streaks of data light, 24fps.",
    "p3_end": "Cinematic wide shot of the dark rainy California expressway at 3 AM, streaks of red and white taillights reflecting on wet pavement, towering industrial silicon valley billboards, cinematic anamorphic lens, 4k --ar 16:9",
    "davinci_recipe": "Color Page: Глибокий нуар-контраст, Lift опущений до 0.02. Optical Flow для розтягування світлових ліній автомобілів на задньому плані. Vignette з акцентом на центр кадру.",
    "sfx_cue": "Приглушений басовитий гул нічного шосе. Раптовий дзвінкий мікро-тріск скла при проходженні камери крізь отвір, що переходить у глибокий синтезаторний дрон."
  },
  {
    "id": 9,
    "num": "09",
    "name_ua": "Розтрощений кристал NV1",
    "name_en": "The Silicon Failure Deconstruction",
    "cat": "macro",
    "cat_label": "🔬 Макро-світ",
    "cat_color": "emerald",
    "tc": "06:30 – 08:00",
    "act": "Акт 2 • Тридцять днів до темряви 1993",
    "tagline": "Крах першого чіпа: краса інженерної помилки та 30 днів до повного банкрутства",
    "concept": "Макрозйомка розбитого кремнієвого кристала першого процесора на темному сталевому столі лабораторії. Осколки виблискують холодним блакитним світлом. Раптом час уповільнюється: осколки піднімаються в невагомості і починають складатися в нову, фундаментально іншу трикутну полігональну геометрію майбутнього чіпа.",
    "why_it_works": "Драматична візуалізація першої поразки стартапу, яка не зламала засновника, а змусила перевинайти підхід до 3D-графіки.",
    "p1_start": "Macro photograph of a fractured, shattered silicon processor die lying on a dark brushed-metal workbench, cold cyan studio laboratory spotlighting, sharp metallic fragments, symbol of technological failure, shallow depth of field --ar 16:9",
    "p2_flow": "Time reverse physics in ultra slow motion: sharp silicon shards hover in zero gravity, glowing with internal ember heat. The fragments rotate and reconstruct themselves into an entirely new, flawless triangular polygon mesh lattice, 24fps.",
    "p3_end": "Luminous triangular 3D wireframe polygon mesh forming an abstract architectural microchip sculpture, dark obsidian void, amber and gold edge luminescence, cleanroom precision, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Replicate3D Node з інверсією вектора швидкості. Color: перехід від холодного Ice Blue (поразка) до вогняного Gold/Amber (переродження).",
    "sfx_cue": "Сухий кришталевий дзвін падаючого скла, що раптово зупиняється у вакуумі. На зворотному русі — глибокий наростаючий резонанс металевого гонгу."
  },
  {
    "id": 10,
    "num": "10",
    "name_ua": "Самурайський вердикт у Токіо",
    "name_en": "The Tokyo Boardroom Bow of Honor",
    "cat": "split",
    "cat_label": "⚡ Драматичний розкол",
    "cat_color": "amber",
    "tc": "08:00 – 09:30",
    "act": "Акт 2 • Тридцять днів до темряви 1993",
    "tagline": "Чесність перед смертю компанії: як уклін у Токіо врятував стартап від банкрутства",
    "concept": "Починається як витончена аніме-сцена в стилі класичної японської анімації: молодий тайвансько-американський засновник низько схиляє голову в поклоні перед літнім японським топ-менеджером ігрового гіганта за темним столом переговорів. Аніме-штрихи плавно перетікають у живий 35-мм кінематографічний кадр вечірнього Токіо.",
    "why_it_works": "Показує момент безпрецедентної моральної сміливості: визнати провал перед партнером, але запропонувати партнерство, яке врятує обох.",
    "p1_start": "Expressive Japanese animation style: a dramatic high-contrast two-shot of a 30-year-old tech entrepreneur bowing with deep respect across a dark polished rosewood boardroom table to an elderly Japanese corporate executive in Tokyo, evening dusk outside shoji screens --ar 16:9",
    "p2_flow": "Cell animation artwork softly dissolves into realistic 35mm film textures. Shoji paper screens give way to panoramic plate-glass windows revealing the glowing twilight skyline of Tokyo 1996; lighting softens into warm tungsten and twilight blue, 24fps.",
    "p3_end": "Master 35mm cinematic film still: the young tech entrepreneur and the Japanese corporate chairman shaking hands with mutual honor against a panoramic high-rise Tokyo skyline at sunset, authentic period suits, emotional depth, 4k --ar 16:9",
    "davinci_recipe": "Edit: Slow Dissolve 16 кадрів на розфокусі вечірніх вогнів Токіо. Color: Японська палітра 90-х: глибокий індиго та золотистий захід сонця.",
    "sfx_cue": "Повна тиша японської переговорної кімнати. Сухий звук шурхоту тканини костюма при поклоні, потім тихий, глибокий удар храмового дзвону далеко в місті."
  },
  {
    "id": 11,
    "num": "11",
    "name_ua": "Спалах Riva 128: ставка ва-банк",
    "name_en": "The High-Stakes Wire Bonding Spark",
    "cat": "macro",
    "cat_label": "🔬 Макро-світ",
    "cat_color": "emerald",
    "tc": "09:30 – 10:45",
    "act": "Акт 2 • Тридцять днів до темряви 1993",
    "tagline": "Останні долари компанії перетворюються на надзвукове зварювання золотих мікродротів",
    "concept": "Надшвидкісна макрозйомка промислового верстата термозвукового мікророзварювання. Золота голка на надзвуковій швидкості торкається кремнієвого кристала. Кожен мікроудар висікає сліпучі іскри чистих фотонів, сплітаючи мікросхему першого рятівного прискорювача.",
    "why_it_works": "Передає шалену напругу останнього шансу: якщо цей чіп вийде з браком, компанії настане кінець наступного понеділка.",
    "p1_start": "Extreme macro close-up of an automated high-precision semiconductor wire-bonder capillary poised microns above a bare silicon microprocessor die, industrial laboratory lighting, metallic reflections, shallow depth of field --ar 16:9",
    "p2_flow": "High-speed camera captures the wire-bonding needle firing at supersonic velocity. Dazzling microscopic golden plasma sparks erupt at 1000fps slow motion with each contact, rapidly weaving an intricate geometric web of ultra-fine golden micro-wires across the die, 24fps.",
    "p3_end": "Completed pristine high-performance graphics card circuit board in razor-sharp macro focus, deep green multi-layer PCB substrate, gleaming gold contacts, dark studio background, industrial engineering triumph, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Lens Flare Node на кожному спалаху голки (синхронізовано з биттям барабана 92 BPM). Color: Glow з підсиленням червоного спектра для іскор.",
    "sfx_cue": "Надшвидкісний кулеметний звук клацання мікроверстата (Micro-taps 20 ударів/сек). Кожен спалах супроводжується електричним тріском високої напруги."
  },
  {
    "id": 12,
    "num": "12",
    "name_ua": "Двобій світів: CPU проти GPU",
    "name_en": "The Parallel Wave Confrontation",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "10:45 – 11:30",
    "act": "Акт 3 • Велика єресь CUDA 2006",
    "tagline": "Один геніальний кур'єр проти армії з десяти тисяч синхронних робітників",
    "concept": "Екран розділений на дві концептуальні площини. Зліва — один самотній яскравий синій промінь рухається довгою вузькою звивистою доріжкою (послідовний центральний процесор). Справа — велетенська стіна з десяти тисяч паралельних смарагдових світлових точок рушає вперед одночасно, наче цунамі чистої енергії.",
    "why_it_works": "Найпростіша і найпотужніша візуальна метафора різниці між послідовними та паралельними обчисленнями, зрозуміла будь-якому глядачеві.",
    "p1_start": "Split-screen abstract visualization: left side shows a single solitary bright azure laser particle slowly navigating a winding copper labyrinth trace; right side is a dormant, massive dark grid of 10,000 hexagonal nodes, deep black background --ar 16:9",
    "p2_flow": "Dynamic visual eruption: while the left single beam advances one step, the entire dormant right grid instantly detonates with 10,000 synchronized neon emerald laser pulses, advancing simultaneously forward like a tidal wave of light, 24fps.",
    "p3_end": "Monumental wide architectural 3D visualization of an infinite parallel computational matrix, millions of emerald and gold light points pulsing in harmonious mathematical resonance, volumetric atmospheric haze, Octane 8k render --ar 16:9",
    "davinci_recipe": "Edit: Split Screen 50/50. Ліва частина замкнена в повільному темпі (0.5x), права частина вибухає на 1-му такті музики Акту 3 (92 BPM drop).",
    "sfx_cue": "Зліва — повільне поодиноке клацання годинника. Справа — наростаючий колосальний рокіт цифрової лавини (Low-end sweep від 30Hz до 120Hz на -3 dB)."
  },
  {
    "id": 13,
    "num": "13",
    "name_ua": "Кузня CUDA: десятиліття самотності",
    "name_en": "The Desert Highway of Solitude",
    "cat": "retro",
    "cat_label": "📻 Ретро-хроніка",
    "cat_color": "purple",
    "tc": "11:30 – 12:15",
    "act": "Акт 3 • Велика єресь CUDA 2006",
    "tagline": "Десять років глузувань Уолл-стріт і самотній шлях крізь пустелю нерозуміння",
    "concept": "Починається як похмура графічна ілюстрація в стилі Моебіуса: одинокий мандрівник у чорній шкіряній куртці стоїть посеред безплідної розтрісканої пустелі під грозовими хмарами. Малюнок оживає: тріщини в землі спалахують зеленим неоновим світлом, а на горизонті крізь зливу виростають гігантські серверні моноліти.",
    "why_it_works": "Показує психологічний тягар лідера, який 10 років вкладав півмільярда доларів щороку в технологію, яку інвестори називали марною забаганкою.",
    "p1_start": "Graphic novel comic aesthetic: a solitary stylized man in a dark jacket standing on a cracked desert road under an ominous bruised purple thundercloud sky, distant lightning flashes, high contrast graphic linework --ar 16:9",
    "p2_flow": "Atmospheric dissolution: 2D drawing lines wash away under torrential cinematic rain. The cracked arid earth fissures start glowing with subsurface green neon energy lines, which branch forward into the stormy horizon, rising into architectural data monoliths, 24fps.",
    "p3_end": "Hyperrealistic cinematic shot of a determined tech founder standing on a dark wet desert highway at twilight, distant supercomputer datacenter towers illuminated with green beacons on the stormy horizon, anamorphic 35mm film grain, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Sky Replacement з шаром грозових хмар і спалахів блискавок (Merge Multiply). Color: Зниження насиченості зеленого до 40%, окрім світлових доріжок.",
    "sfx_cue": "Гуркіт далекого грому в пустелі, шум важких крапель дощу по шкіряній куртці. Тривожний тривалий шлейф аналогового синтезатора (Vangelis tone)."
  },
  {
    "id": 14,
    "num": "14",
    "name_ua": "Червоний обвал Уолл-стріт",
    "name_en": "The Financial Abyss Reflection",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "12:15 – 13:45",
    "act": "Акт 3 • Велика єресь CUDA 2006",
    "tagline": "Падіння акцій на 80% крізь нерухомі очі лідера, який бачить інший вимір",
    "concept": "Камера дивиться впритул в обличчя засновника вночі. В його окулярах відбивається нескінченний водоспад червоних цифр біржових котирувань, що летять униз. Камера проходить вглиб зіниці, де червоні котирування розчиняються, поступаючись місцем спокійному зеленому математичному коду паралельних ядер.",
    "why_it_works": "Наочно протиставляє короткозору біржову паніку довгостроковому інженерному баченню, яке не зважає на квартальні звіти.",
    "p1_start": "Cinematic low-key portrait of a 45-year-old Taiwanese-American CEO in a dark boardroom at midnight, his unblinking dark eyes framed by stylish glasses reflecting a chaotic cascade of bright red stock market numbers falling, tense mood --ar 16:9",
    "p2_flow": "Extreme macro push-in directly into the dark pupil of the eye. The falling red financial numbers blur and dissolve into pure abstraction, replaced from the depth of the retina by steady, calm rows of green binary algorithmic logic, 24fps.",
    "p3_end": "Macro photograph of a human eye in sharp clinical focus, iris illuminated by soft emerald reflections of neural network mathematical formulas, calm determination, authentic skin pores and micro-details, 8k --ar 16:9",
    "davinci_recipe": "Fusion: Planar Tracker по лінзах окулярів. Композитинг шару цифр із режимом накладання Screen. Color: різкий перепад колірної температури від 2800K (червоний жах) до 6500K (холодна впевненість).",
    "sfx_cue": "Хаотичний гул біржової зали Уолл-стріт із криками трейдерів, який різко зрізається фільтром Low-Pass на 200Hz, поступаючись рівному гулу вентилятора сервера."
  },
  {
    "id": 15,
    "num": "15",
    "name_ua": "Кімната прориву в Торонто",
    "name_en": "The Dorm Room Revelation 2012",
    "cat": "retro",
    "cat_label": "📻 Ретро-хроніка",
    "cat_color": "purple",
    "tc": "13:45 – 15:00",
    "act": "Акт 3 • Велика єресь CUDA 2006",
    "tagline": "Дві ігрові відеокарти на підлозі студентської кімнати, що змінили долю цивілізації",
    "concept": "Темна кімната гуртожитку в Торонто, 2012 рік. На підлозі лежить відкритий системний блок комп'ютера з двома з'єднаними кабелями ігровими відеокартами. Вентилятори шалено обертаються. Зелене світло світлодіодів висвітлює дошку зі складними рівняннями згорткових нейромереж. Раптом повітря над чіпами починає мерехтіти, формуючи першу розпізнану нейромережею живу форму.",
    "why_it_works": "Історична сцена злиття двох світів: десятиліття праці над відеокартами раптово знаходять своє справжнє космічне призначення у нейромережах Хінтона та Суцкевера.",
    "p1_start": "Authentic archival-style photograph of a cluttered 2012 university apartment bedroom at night: an open PC case lying flat on the floor with two exposed gaming graphics cards connected, cooling fans spinning, white dry-erase board covered in math equations, 35mm film grain --ar 16:9",
    "p2_flow": "Camera orbits the open desktop chassis. The high-speed fan blades blur into a smooth transparent vortex; thermal heat distortion rises off the heatsinks, coalescing into a glowing 3D convolutional neural lattice hovering above the motherboard, 24fps.",
    "p3_end": "Hyper-detailed 3D visual of a multi-layer deep convolutional neural network processing millions of image pixels in real time, glowing emerald synaptic junctions floating in spatial depth, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Heat Shimmer (Displacement + FastNoise) над відеокартами. 3D Camera Orbit 45 градусів навколо відкритого системника.",
    "sfx_cue": "Високий турбінний свист двох маленьких комп'ютерних кулерів на 4000 RPM. На переході — глибокий резонансний акорд органа чи аналогового синту."
  },
  {
    "id": 16,
    "num": "16",
    "name_ua": "Народження AI суперкомп'ютера",
    "name_en": "The First Server Monolith Handover",
    "cat": "macro",
    "cat_label": "🔬 Макро-світ",
    "cat_color": "emerald",
    "tc": "15:00 – 16:15",
    "act": "Акт 3 • Велика єресь CUDA 2006",
    "tagline": "Перший у світі короб суперінтелекту: білий маркер на алюмінієвій броні",
    "concept": "Макрозйомка важкої лицьової панелі промислового AI-сервера з матового алюмінію. По металу білим маркером виведено рукописне побажання команді дослідників. Камера плавно від'їжджає: світлодіодна панель оживає пульсуючим смарагдовим сяйвом, освітлюючи стерильну лабораторію майбутнього.",
    "why_it_works": "Символ передачі фізичної зброї штучного інтелекту: від заліза до алгоритмів, що перевернуть людство.",
    "p1_start": "Extreme macro close-up of a heavy industrial brushed aluminum server faceplate, authentic handwritten encouraging message scrawled across the metal in permanent white paint pen, engineering workshop lighting, tactile industrial finish --ar 16:9",
    "p2_flow": "Slow majestic crane pull-back. The handwritten white ink lines catch directional light; the server unit abruptly powers on, an array of emerald and azure status LEDs sweeping across the front grill, illuminating a sterile research cleanroom in dramatic chiaroscuro, 24fps.",
    "p3_end": "Monumental industrial photography of a cutting-edge AI supercomputer rack operating in a pristine, climate-controlled datacenter cleanroom, glowing blue and green fiber-optic telemetry indicators, cinematic atmospheric fog, 4k 24fps --ar 16:9",
    "davinci_recipe": "Edit: Повільний Linear Pull-Out. Color: Збалансований скандинавський холодний тон (6000K), акцент на чистоту білого напису та яскраві діоди.",
    "sfx_cue": "Сухий скрип маркера по холодному алюмінію. Потім — оглушливий запуск промислових вентиляторів серверної стійки з наростаючим тиском повітря."
  },
  {
    "id": 17,
    "num": "17",
    "name_ua": "Трикутна цитадель без стін",
    "name_en": "The Open Architecture Fly-Through",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "16:15 – 17:45",
    "act": "Акт 4 • Анатомія лідера без кабінету 2024",
    "tagline": "Штаб-квартира як фізичне втілення плоского управління: нуль кабінетів, суцільне світло",
    "concept": "Камера дивиться на архітектурне креслення гігантського трикутного кампусу. Лінії креслення вертикально виростають у сталеві трикутні ферми, бетон і гігантські скляні світлові ліхтарі. Камера пікірує крізь скляний дах усередину величезного відкритого простору, де сотні інженерів працюють за спільними дерев'яними столами без жодної стіни чи дверей.",
    "why_it_works": "Візуалізує унікальну управлінську філософію: відсутність кабінету як гарантія того, що правда не помирає по дорозі через поверхи менеджерів.",
    "p1_start": "Architectural technical blueprint drawing of a massive futuristic triangular headquarters building, crisp white lines on dark graphite paper, isometric elevation angles, geometric perfection --ar 16:9",
    "p2_flow": "Camera dives downward as the 2D blueprint lines extrude vertically into solid steel pillars, geometric triangular glass skylights, and polished concrete. Glass panes reflect morning sunlight as camera swoops down through the ceiling into the interior volume, 24fps.",
    "p3_end": "Sweeping cinematic interior shot of a vast open-plan architectural tech headquarters: soaring triangular wooden and glass ceilings flooded with natural daylight, hundreds of engineers collaborating around open wooden tables with zero private executive offices, 4k --ar 16:9",
    "davinci_recipe": "Fusion: 3D Camera Projection з переходом від каркасної сітки Wireframe до PBR-матеріалів скла і деревини. Плавний Motion Blur на швидкості польоту.",
    "sfx_cue": "Шелест креслярського паперу. При прольоті крізь скло — теплий гул просторого світлого атріуму: тихі голоси, стукіт клавіатур, дзвін чашок кави."
  },
  {
    "id": 18,
    "num": "18",
    "name_ua": "Кодекс болю та гарт кремнію",
    "name_en": "The Volcanic Forge of Character",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "emerald",
    "tc": "17:45 – 18:45",
    "act": "Акт 4 • Анатомія лідера без кабінету 2024",
    "tagline": "«Я щиро бажаю вам багато болю і страждань»: як дика порода перетворюється на кристал",
    "concept": "Макрозйомка розпеченого шматка грубої вулканічної породи, що тріскається під шаленим тиском і температурою. З тріщин б'є полум'я. Повільно матеріал плавиться, очищується від домішок і охолоджується, перетворюючись на бездоганно круглий дзеркальний монокристал чистого кремнію.",
    "why_it_works": "Пряма візуальна метафора стенфордської промови героя: велич гартується лише тиском невдач і подоланням болю.",
    "p1_start": "Extreme macro close-up of rough black volcanic rock cracking under intense geothermal heat and pressure, vivid orange magma glowing inside internal fissures, tactile mineral roughness, cinematic documentary look --ar 16:9",
    "p2_flow": "Thermal thermodynamic transformation: extreme heat melts the raw mineral into a radiant pool of liquid golden silica. Camera tracks smoothly as the molten liquid cools, crystallizing outward into an atomically perfect mirror-reflective circular semiconductor ingot, 24fps.",
    "p3_end": "Flawless, mirror-polished 300mm cylindrical silicon semiconductor crystal ingot standing upright in a cleanroom, surface reflecting pristine laboratory lights with absolute perfection, hyperrealistic 8k render --ar 16:9",
    "davinci_recipe": "Color: Heat Map Color Palette на старті, плавний перехід кривими Saturation vs Temp до крижаного монохрому кремнію. Fairlight: гучний рев полум'я, що згасає.",
    "sfx_cue": "Низькочастотний підземний гул магми і тріск каменю. На кристалізації — дзвінкий, чистий звук загартованого металу, що занурюється у воду."
  },
  {
    "id": 19,
    "num": "19",
    "name_ua": "Шкіряна броня та погляд о 5 ранку",
    "name_en": "The Leather Armor Identity",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "18:45 – 19:45",
    "act": "Акт 4 • Анатомія лідера без кабінету 2024",
    "tagline": "Чорна шкіряна куртка як уніформа коваля і погляд, у якому все ще живе той хлопчик із Кентуккі",
    "concept": "Макро-кадр чорної текстурованої шкіряної байкерської куртки, що висить на спинці стільця на світанку. Камера плавно переводить фокус на темне дзеркало ванної кімнати: 61-річний сивий засновник вмивається холодною водою о 5-й ранку і дивиться собі в очі. У відбитті на частку секунди проступає обличчя 9-річного хлопчика біля туалетного йоржика.",
    "why_it_works": "Показує джерело невгасимої енергії: людина на вершині світу ніколи не забуває, з якого пекла вона піднялася.",
    "p1_start": "Macro close-up of a weathered, textured black leather motorcycle jacket hanging over a chair, subtle blue twilight spilling through venetian blinds at dawn, tactile leather grain in razor-sharp focus --ar 16:9",
    "p2_flow": "Camera racks focus smoothly to the bathroom mirror behind. A 61-year-old Taiwanese-American CEO with distinguished silver hair splashes cold water on his face; as droplets slide down the mirror, a faint ghosted double-exposure reveals the reflection of the 9-year-old immigrant boy looking back, 24fps.",
    "p3_end": "Intimate, powerful 35mm film portrait of the 61-year-old tech leader looking directly into the camera lens with quiet iron resolve, water droplets on skin, wearing the black leather jacket, soft morning window light, cinematic depth of field, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Rack Focus через Depth Map. Тонкий Ghosting Effect (Opacity 14%) обличчя хлопчика у відблиску дзеркала. Color: теплий скінтон на холодному синьому тлі.",
    "sfx_cue": "Сплеск холодної води в умивальнику, важкий спокійний видих. Тихий скрип натягнутої шкіри куртки при русі плечима."
  },
  {
    "id": 20,
    "num": "20",
    "name_ua": "Цифровий двійник планети",
    "name_en": "The Omniverse Planetary Finale",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "19:45 – 21:00",
    "act": "Акт 4 • Анатомія лідера без кабінету 2024",
    "tagline": "Від мікрона до космічного масштабу: Земля як жива цифрова симуляція",
    "concept": "Камера починається з макро-фокусу на крихітному зеленому кристалі процесора в руках інженера. Потім камера починає безперервний гіпер-від'їзд угору: мікросхема розширюється в материнську плату, в суперкомп'ютерний кластер, у будівлю дата-центру, у вогні міст, і нарешті виривається на орбіту Землі, яка вся світиться золотою живою сіткою цифрового двійника Omniverse.",
    "why_it_works": "Грандіозний фінал епізоду: відчуття завершеного колосального шляху — від самотнього приниження в Кентуккі до створення віртуального всесвіту для всього людства.",
    "p1_start": "Macro close-up of an ultra-dense glowing emerald semiconductor processor chip held in gloved hands under pristine cleanroom optical lighting, golden microscopic bus lines visible, high-tech realism --ar 16:9",
    "p2_flow": "Continuous cosmic camera pull-back through exponential orders of magnitude: microchip expands into server blade, into towering datacenter rack, through the ceiling into glowing city grids, soaring into upper atmosphere to reveal the full curvature of Earth, 24fps.",
    "p3_end": "Breathtaking IMAX-scale visual of planet Earth floating in deep space, completely enveloped in an ethereal glowing golden digital-twin neural mesh simulating global weather, oceans, and interconnected cities, poetic cinematic sci-fi finale, 8k 24fps --ar 16:9",
    "davinci_recipe": "Fusion: Camera 3D з безперервним логарифмічним масштабуванням (Exponential Zoom curve). На фіналі — спад рівня звуку до тиші з повільним затемненням у чорне (Fade to Black 48 кадрів).",
    "sfx_cue": "Останній важкий удар індустріального молота у бездонному ревері (Suno Theme 4). На орбіті — повний вакуум космосу, крізь який ледь чутно пробивається шипіння води з посудомийки 1978 року."
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
              <div class="section-label">🎬 Концепція & Драматичний ефект</div>
              <p class="section-text">{item['concept']}</p>
              <div class="highlight-text" style="margin-top:8px;">💡 <strong>Психологія сприйняття:</strong> {item['why_it_works']}</div>
            </div>

            <!-- THE 3-PROMPT TRIAD -->
            <div class="triad-container">
              <div class="triad-title">🎯 ТРИАДНА ФОРМУЛА GOOGLE FLOW (СТАРТ ➡️ МОРФІНГ ➡️ ФІНАЛ)</div>
              
              <!-- PROMPT 1 -->
              <div class="prompt-box prompt-p1">
                <div class="prompt-header">
                  <div class="prompt-tag tag-p1">
                    <span class="p-num">1</span>
                    <span>🎨 ПРОМПТ 1: Стартове зображення (Start Frame A)</span>
                  </div>
                  <button class="copy-btn" onclick="copyText('p1-{item['num']}', this)">📋 Копіювати Промпт 1</button>
                </div>
                <div class="prompt-hint">Вставте в Midjourney / Imagen 3 для генерації точки входу А:</div>
                <pre class="code-block" id="p1-{item['num']}">{item['p1_start']}</pre>
              </div>

              <!-- PROMPT 2 -->
              <div class="prompt-box prompt-p2">
                <div class="prompt-header">
                  <div class="prompt-tag tag-p2">
                    <span class="p-num">2</span>
                    <span>🌀 ПРОМПТ 2: Трансформація & Рух (Google Flow Action)</span>
                  </div>
                  <button class="copy-btn" onclick="copyText('p2-{item['num']}', this)">📋 Копіювати Промпт 2 (Flow)</button>
                </div>
                <div class="prompt-hint">Вставте в текстове поле Google Flow / Veo 2 між кадрами А і В:</div>
                <pre class="code-block" id="p2-{item['num']}">{item['p2_flow']}</pre>
              </div>

              <!-- PROMPT 3 -->
              <div class="prompt-box prompt-p3">
                <div class="prompt-header">
                  <div class="prompt-tag tag-p3">
                    <span class="p-num">3</span>
                    <span>📸 ПРОМПТ 3: Фінальне зображення (End Frame B)</span>
                  </div>
                  <button class="copy-btn" onclick="copyText('p3-{item['num']}', this)">📋 Копіювати Промпт 3</button>
                </div>
                <div class="prompt-hint">Вставте в Midjourney / Imagen 3 для генерації фінальної точки В:</div>
                <pre class="code-block" id="p3-{item['num']}">{item['p3_end']}</pre>
              </div>
            </div>

            <!-- PRODUCTION RECIPE -->
            <div class="recipe-grid">
              <div class="recipe-box">
                <div class="recipe-title">✂️ Рецепт монтажу в DaVinci Resolve 19</div>
                <p class="recipe-text">{item['davinci_recipe']}</p>
              </div>
              <div class="recipe-box">
                <div class="recipe-title">🔊 Звуковий ландшафт & SFX (Fairlight)</div>
                <p class="recipe-text">{item['sfx_cue']}</p>
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
  <title>20 Кінематографічних Тріад (Епізод 02: Дженсен Хуанг) • Google Flow Standard</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #0b0f17;
      --surface: #111724;
      --surface-elevated: #161e2e;
      --surface-hover: #1c273c;
      --border: #1e293b;
      --border-subtle: #172132;
      --text-primary: #f8fafc;
      --text-secondary: #cbd5e1;
      --text-muted: #94a3b8;
      --cyan: #38bdf8;
      --emerald: #34d399;
      --amber: #fbbf24;
      --purple: #c084fc;
      --rose: #f43f5e;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text-primary);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 5rem;
    }}

    /* Top Sticky Navigation Bar */
    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(11, 15, 23, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0.75rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 14px;
      color: var(--text-primary);
      text-decoration: none;
    }}
    .nav-brand span {{
      background: linear-gradient(135deg, var(--emerald), var(--cyan));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .nav-actions {{
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .btn {{
      padding: 0.45rem 0.9rem;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}
    .btn-outline {{
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-secondary);
    }}
    .btn-outline:hover {{
      background: var(--surface-hover);
      color: var(--text-primary);
      border-color: var(--text-muted);
    }}
    .btn-emerald {{
      background: rgba(52, 211, 153, 0.15);
      border: 1px solid rgba(52, 211, 153, 0.4);
      color: var(--emerald);
    }}
    .btn-emerald:hover {{
      background: rgba(52, 211, 153, 0.25);
    }}

    /* Container */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: radial-gradient(circle at top right, rgba(52, 211, 153, 0.12), transparent 45%),
                  radial-gradient(circle at bottom left, rgba(56, 189, 248, 0.08), transparent 45%),
                  var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 2.5rem 2rem;
      margin-bottom: 2rem;
      position: relative;
      overflow: hidden;
    }}
    .hero-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      background: rgba(52, 211, 153, 0.16);
      border: 1px solid rgba(52, 211, 153, 0.45);
      color: var(--emerald);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 28px;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 0.75rem;
      background: linear-gradient(135deg, #ffffff 40%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-desc {{
      font-size: 15px;
      color: var(--text-secondary);
      max-width: 900px;
      margin-bottom: 1.5rem;
    }}

    /* Triad Explainer Box */
    .triad-explainer {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 12px;
      margin-top: 1.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border);
    }}
    .expl-box {{
      background: var(--surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1rem;
    }}
    .expl-tag {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}
    .expl-text {{
      font-size: 12.5px;
      color: var(--text-secondary);
    }}

    /* Filter Bar */
    .filter-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}
    .filter-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .filter-pill {{
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 600;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .filter-pill:hover {{
      background: var(--surface-hover);
      color: var(--text-primary);
    }}
    .filter-pill.active {{
      background: var(--emerald);
      color: #0b0f17;
      border-color: var(--emerald);
      font-weight: 700;
    }}
    .search-input {{
      padding: 0.45rem 1rem;
      border-radius: 8px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-primary);
      font-size: 13px;
      width: 240px;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--emerald);
    }}

    /* Cards Grid */
    .cards-grid {{
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }}
    .innov-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      overflow: hidden;
      transition: border-color 0.2s ease;
    }}
    .innov-card:hover {{
      border-color: rgba(52, 211, 153, 0.4);
    }}

    /* Card Header */
    .innov-header {{
      padding: 1.5rem 1.75rem 1rem;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .innov-meta {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 0.6rem;
      flex-wrap: wrap;
    }}
    .innov-num {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--emerald);
      background: rgba(52, 211, 153, 0.12);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }}
    .badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 0.2rem 0.55rem;
      border-radius: 999px;
    }}
    .badge-subtle {{ background: var(--surface-elevated); color: var(--text-muted); border: 1px solid var(--border-subtle); }}
    .badge-tc {{ font-family: var(--font-mono); background: rgba(251, 191, 36, 0.12); color: var(--amber); border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-emerald {{ background: rgba(52, 211, 153, 0.12); color: var(--emerald); border: 1px solid rgba(52, 211, 153, 0.3); }}
    .badge-purple {{ background: rgba(192, 132, 252, 0.12); color: var(--purple); border: 1px solid rgba(192, 132, 252, 0.3); }}
    .badge-amber {{ background: rgba(251, 191, 36, 0.12); color: var(--amber); border: 1px solid rgba(251, 191, 36, 0.3); }}
    .badge-cyan {{ background: rgba(56, 189, 248, 0.12); color: var(--cyan); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-rose {{ background: rgba(244, 63, 94, 0.12); color: var(--rose); border: 1px solid rgba(244, 63, 94, 0.3); }}

    .innov-title {{
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 0.3rem;
    }}
    .innov-en {{
      font-size: 15px;
      font-weight: 500;
      color: var(--text-muted);
    }}
    .innov-tagline {{
      font-size: 14px;
      font-style: italic;
      color: var(--cyan);
    }}

    /* Card Body */
    .innov-body {{
      padding: 1.5rem 1.75rem;
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .section-label {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--text-muted);
      margin-bottom: 0.4rem;
    }}
    .section-text {{
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.6;
    }}
    .highlight-text {{
      font-size: 13px;
      color: #e2e8f0;
      background: var(--surface-elevated);
      padding: 0.65rem 0.9rem;
      border-radius: 6px;
      border-left: 3px solid var(--emerald);
    }}

    /* Triad Layout */
    .triad-container {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      background: var(--surface-elevated);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.25rem;
    }}
    .triad-title {{
      font-size: 12px;
      font-weight: 800;
      color: var(--emerald);
      letter-spacing: 0.8px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 4px;
    }}

    .prompt-box {{
      background: #080c14;
      border-radius: 8px;
      padding: 0.9rem 1rem;
      border: 1px solid var(--border-subtle);
      position: relative;
    }}
    .prompt-p1 {{ border-left: 3px solid var(--purple); }}
    .prompt-p2 {{ border-left: 3px solid var(--cyan); background: #060e1a; }}
    .prompt-p3 {{ border-left: 3px solid var(--emerald); }}

    .prompt-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.4rem;
      gap: 8px;
    }}
    .prompt-tag {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
    }}
    .tag-p1 {{ color: var(--purple); }}
    .tag-p2 {{ color: var(--cyan); }}
    .tag-p3 {{ color: var(--emerald); }}
    .p-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      font-size: 11px;
      background: rgba(255,255,255,0.1);
    }}
    .prompt-hint {{
      font-size: 11.5px;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
      font-style: italic;
    }}
    .code-block {{
      font-family: var(--font-mono);
      font-size: 12.5px;
      line-height: 1.55;
      color: #e2e8f0;
      white-space: pre-wrap;
      word-break: break-word;
      background: rgba(0,0,0,0.3);
      padding: 0.65rem 0.85rem;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.05);
    }}
    .copy-btn {{
      background: var(--surface-hover);
      border: 1px solid var(--border);
      color: var(--text-secondary);
      font-size: 11px;
      font-weight: 600;
      padding: 0.3rem 0.65rem;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .copy-btn:hover {{
      background: var(--emerald);
      color: #0b0f17;
      border-color: var(--emerald);
    }}

    /* Recipe & SFX */
    .recipe-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }}
    @media (max-width: 768px) {{
      .recipe-grid {{ grid-template-columns: 1fr; }}
    }}
    .recipe-box {{
      background: var(--surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.85rem 1rem;
    }}
    .recipe-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--amber);
      margin-bottom: 0.3rem;
    }}
    .recipe-text {{
      font-size: 12.5px;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    /* Toast Notification */
    .toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: var(--emerald);
      color: #0b0f17;
      font-weight: 700;
      font-size: 13px;
      padding: 0.75rem 1.25rem;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      z-index: 1000;
      opacity: 0;
      transform: translateY(10px);
      transition: all 0.25s ease;
      pointer-events: none;
    }}
    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Bar -->
  <nav class="top-nav">
    <a href="../index.html" class="nav-brand">
      <span>AI Titans</span> Thoughtcast Studio
    </a>
    <div class="nav-actions">
      <a href="index.html" class="btn btn-outline">← Назад до Дашборду</a>
      <a href="cinematic_innovations.html" class="btn btn-outline">🎬 Тріади Еп. 01</a>
      <a href="cinematic_innovations_ep02.html" class="btn btn-emerald">🔥 Тріади Еп. 02</a>
      <a href="cinematic_innovations_ep03.html" class="btn btn-outline" style="border-color:var(--purple);color:var(--purple);">♟️ Тріади Еп. 03</a>
      <a href="episodes/ep01_altman.html" class="btn btn-outline">🎙️ Студія 01</a>
      <a href="episodes/ep02_huang.html" class="btn btn-outline">🎙️ Студія 02</a>
      <a href="episodes/ep03_hassabis.html" class="btn btn-outline">🎙️ Студія 03</a>
    </div>
  </nav>

  <main class="container">
    <!-- Hero Section -->
    <section class="hero-banner">
      <span class="hero-badge">🛡️ 100% Policy-Safe • Zero Banned Keywords • Епізод 02</span>
      <h1 class="hero-title">20 Кінематографічних Тріад Епізоду 02 (Дженсен Хуанг)</h1>
      <p class="hero-desc">
        Повна система генерації відео для рушія <strong>Google Flow / Veo 2</strong> за формулою «First Frame &amp; Last Frame». Кожна тріада складається з 3 точних команд: опорний початковий кадр (Start Frame A), кінематографічна дія морфінгу (Motion Action), та фінальний фотореалістичний кадр реального життя (End Frame B). Усі чутливі імена, бренди та товарні знаки замінено на контекстні кінематографічні архетипи.
      </p>

      <div class="triad-explainer">
        <div class="expl-box" style="border-left: 3px solid var(--purple);">
          <div class="expl-tag" style="color:var(--purple);">1. ПРОМПТ 1: Start Image</div>
          <p class="expl-text">Генерує опорну точку кадру А (вінтаж 1970-х, аніме-графіка, кахель реформаторію або нічний Denny's). Завантажується у поле <strong>Start Image</strong>.</p>
        </div>
        <div class="expl-box" style="border-left: 3px solid var(--cyan);">
          <div class="expl-tag" style="color:var(--cyan);">2. ПРОМПТ 2: Video Morph Action</div>
          <p class="expl-text">Інструкція для Google Flow: описує фізику руху камери, оптичний рентген, розчинення пари, надзвукове розварювання та перехід в інший вимір.</p>
        </div>
        <div class="expl-box" style="border-left: 3px solid var(--emerald);">
          <div class="expl-tag" style="color:var(--emerald);">3. ПРОМПТ 3: End Image</div>
          <p class="expl-text">Генерує цільову точку трансформації: 100% фотореалістичний кадр реального життя без згадки заборонених імен. Завантажується у <strong>End Image</strong>.</p>
        </div>
      </div>
    </section>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <div class="filter-pills">
        <button class="filter-pill active" data-filter="all">Всі 20 тріад</button>
        <button class="filter-pill" data-filter="optics">🔍 Оптичні трюки</button>
        <button class="filter-pill" data-filter="retro">📻 Ретро-хроніка & Аніме</button>
        <button class="filter-pill" data-filter="matrix">🌐 Цифрова матриця</button>
        <button class="filter-pill" data-filter="macro">🔬 Макро-світ кремнію</button>
        <button class="filter-pill" data-filter="split">⚡ Драматичний розкол</button>
        <button class="filter-pill" data-filter="noir">🕵️ Нуар & Тіні</button>
        <button class="filter-pill" data-filter="typo">🔤 Кінетична типографіка</button>
      </div>
      <input type="text" id="searchInput" class="search-input" placeholder="Пошук по тріадах (напр. кахель, Denny's)...">
    </div>

    <!-- Cards Grid -->
    <div class="cards-grid" id="cardsGrid">
      {cards_html}
    </div>
  </main>

  <div class="toast" id="toast">✓ Скопійовано!</div>

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
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/cinematic_innovations_ep02.html",
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/docs/cinematic_innovations_ep02.html"
    ]
    for p in paths:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Generated {p} ({len(html_content)} bytes)")
