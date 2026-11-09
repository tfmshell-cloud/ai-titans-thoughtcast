#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Episode 03 (Demis Hassabis) - 30 Cinematic Triads (Start -> Morph -> End)
Tailored for Google Flow / Veo 2, 100% Policy-Safe, with DaVinci Resolve recipes & SFX cues.
Theme: Chess, 90s Gaming, Neurobiology, London vs Silicon Valley / OpenAI, Move 37, Protein Origami & Nobel.
"""

import os

INNOVATIONS = [
  # ACT 1: ЧОТИРИ РОКИ, ШІСТДЕСЯТ ЧОТИРИ КЛІТИНКИ ТА ZX SPECTRUM (0:00 - 5:15)
  {
    "id": 1,
    "num": "01",
    "name_ua": "Різьблений кінь на темному горісі",
    "name_en": "The Hand-Carved Knight Blueprint",
    "cat": "chess",
    "cat_label": "♟️ Шаховий інтелект",
    "cat_color": "purple",
    "tc": "00:00 – 00:25",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Від теплого дерева лакованої фігури до розгалуженого дерева рішень у гіперпросторі",
    "concept": "Екстремальне макро дерев'яного шахового коня ручної роботи на темній клітинці з горіха. Камінне полум'я відбивається на лаку. Камера занурюється вглиб дерева: волокна розчиняються, відкриваючи золоту тривимірну сітку комбінаторного дерева ходів, що простягається у нескінченність.",
    "why_it_works": "Задає головну філософію мислення гросмейстера: бачити за кожною фізичною фігурою нескінченний простір математичних наслідків на десять кроків уперед.",
    "p1_start": "Extreme macro cinematic photograph of a hand-carved dark walnut wooden chess knight on a polished chessboard square, amber fireplace reflections glimmering on the smooth varnish, suspended dust motes in a beam of light, shallow depth of field, 35mm film grain --ar 16:9",
    "p2_flow": "Continuous macro push-in camera penetrating through the wood varnish into the microscopic grain. Solid timber dissolves into a translucent crystalline matrix, internal cellulose fibers igniting with glowing golden vector lines that branch outward into an expansive multi-dimensional decision tree, seamless physical morph, 24fps.",
    "p3_end": "Monumental abstract 3D visualization of an infinite mathematical decision tree: thousands of luminous golden nodes and interconnected probability branches suspended in deep space, volumetric lighting, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion Page: 3D Camera Projection з Displace по текстурі дерева. Перехід через Light Wrap та Glow (Threshold 0.60) на золоті вузли. Звуковий стик на клацанні шахової кнопки.",
    "sfx_cue": "Сухий, вагомий стукіт дерев'яної фігури об лаковану дошку. Відлуння в кімнаті з високою стелею. Різкий металевий звук зведеної пружини шахового годинника."
  },
  {
    "id": 2,
    "num": "02",
    "name_ua": "Чотирирічний мовчазний погляд",
    "name_en": "The Four-Year-Old Prodigy Observer",
    "cat": "chess",
    "cat_label": "♟️ Шаховий інтелект",
    "cat_color": "purple",
    "tc": "00:25 – 00:50",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Серед богемного хаосу Північного Лондона народжується архітектор порядку",
    "concept": "Лондон, 1980 рік. Богемна вітальня: картини на підлозі, акустичні гітари. Камера вихоплює чотирирічного хлопчика з темними кучерями, який сидить на килимі й не кліпаючи дивиться на шахівницю між дорослими. У його зіницях відображається не гра, а геометрична формула простору.",
    "why_it_works": "Показує момент, коли дитина відкриває для себе шахи як єдиний острів абсолютного порядку у хаотичному світі дорослих.",
    "p1_start": "Atmospheric 1980 North London bohemian living room in soft warm afternoon light, oil paintings resting against brick walls, a 4-year-old British-Cypriot boy with dark curly hair sitting motionless on a Persian rug, staring with intense focus at a wooden chessboard, 35mm film still --ar 16:9",
    "p2_flow": "Slow cinematic push-in towards the child's face. The room surroundings gently defocus into a warm bokeh; camera tightens into extreme macro of his dark pupils, across which transparent glowing geometric coordinate lines and chess algebraic notation softly glide, 24fps.",
    "p3_end": "Extreme macro cinematic portrait of a young child's dark eyes in razor-sharp focus, pupils mirroring an illuminated 8x8 matrix of light squares and tactical vectors, soft warm rim light, cinematic Kodachrome 35mm film grain, 4k --ar 16:9",
    "davinci_recipe": "Color Page: Емуляція теплої плівки Kodachrome 64. Маска на райдужку ока з підвищенням локального контрасту та яскравості відбиття на 15%.",
    "sfx_cue": "Приглушений звук вінілового програвача з тихою фортепіанною темою (Suno Theme 1). Потім — повна тиша концентрації, крізь яку чути рівне дитяче дихання."
  },
  {
    "id": 3,
    "num": "03",
    "name_ua": "Механічний хронометр Garde",
    "name_en": "The Garde Dual-Clock Spring Tension",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "amber",
    "tc": "00:50 – 01:20",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Червоний прапорець секундної стрілки як символ невідворотності часу",
    "concept": "Макрозйомка класичного німецького дерев'яного шахового годинника Garde. Червоний прапорець повільно піднімається хвилинною стрілкою. Кнопка різко натискається пальцем — час перемикається на інший циферблат, а механічні шестерні всередині годинника починають світитися й прискорюватися у тайм-лапс.",
    "why_it_works": "Фізичне втілення психологічного тиску шахової боротьби: уникнення цейтноту та контроль над темпом мислення.",
    "p1_start": "Extreme macro of a vintage mechanical wooden chess tournament clock, two circular dials with brass bezels, a red metal flag hovering at the 12 o'clock mark, ticking mechanism visible through subtle glass refraction, warm tungsten lighting, shallow focus --ar 16:9",
    "p2_flow": "High-speed camera captures an index finger slamming the wooden clock plunger. The red flag drops instantly; time accelerates into an optical motion blur as clock hands whirl into hyper-speed, mechanical brass gears glowing with intense cyan friction sparks, 24fps.",
    "p3_end": "Abstract kinetic time-lapse visual: spinning golden clock dials and streaks of phosphor light trails converging into a singularity point in space, representing relativistic cognitive processing speed, Octane 8k render --ar 16:9",
    "davinci_recipe": "Edit Page: Speed Ramp від 100% до 800% на падінні прапорця. Fusion: Directional Blur + Chromatic Aberration на шлейфах стрілок.",
    "sfx_cue": "Гучне клацання металевої кнопки шахового годинника (транзієнт на 0 dB). На прискоренні — наростаючий дзижчащий звук заводної пружини годинника."
  },
  {
    "id": 4,
    "num": "04",
    "name_ua": "Гумові клавіші ZX Spectrum 48K",
    "name_en": "The Sinclair Z80 Tape Drive Pulse",
    "cat": "gaming",
    "cat_label": "🕹️ Геймінг & Пікселі 90-х",
    "cat_color": "cyan",
    "tc": "01:20 – 01:50",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Перший комп'ютер, куплений на призові гроші від шахового турніру",
    "concept": "Макро-кадр гумових клавіш мікрокомп'ютера Sinclair ZX Spectrum 1984 року. Поруч стоїть портативний касетний магнітофон, з якого через аудіокабель завантажується гра. Звукова хвиля передачі даних перетворюється на горизонтальні червоні та сині смуги завантаження на вигнутому екрані CRT телевізора.",
    "why_it_works": "Початок союзу між шаховою логікою та обчислювальною машиною: комп'ютер як партнер для спарингу, який ніколи не втомлюється.",
    "p1_start": "Macro vintage shot of a 1984 British Sinclair ZX Spectrum 48K microcomputer with distinctive rubber keyboard on a wooden school desk, beside a portable cassette recorder with spinning tape reels, warm desk lamp, nostalgic British tech grain --ar 16:9",
    "p2_flow": "Camera tracks from the rubber keys up to the vintage color CRT television monitor. The screen erupts with vibrant cyan, red, and yellow loading border bars, high-frequency audio data streams morphing into cascading lines of green assembly machine code, 24fps.",
    "p3_end": "Close-up of a glowing CRT screen curved glass in a darkened room, displaying crisp 8-bit phosphor green assembly code and a rudimentary pixelated chessboard sprite, scanlines visible, authentic retro aesthetic, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Scanlines Node + CRT Monitor Warp (Barrel Distortion 0.08). Колірна корекція: розведення червоно-блакитних смуг завантаження ZX Spectrum.",
    "sfx_cue": "Автентичний пронизливий свист і скрегіт завантаження даних із касети ZX Spectrum (8-bit data chirps на -8 dB). М'яке чавкання гумових клавіш під пальцями."
  },
  {
    "id": 5,
    "num": "05",
    "name_ua": "Турнірний дитячий тріумф",
    "name_en": "The 13-Year-Old Grandmaster Ring",
    "cat": "chess",
    "cat_label": "♟️ Шаховий інтелект",
    "cat_color": "purple",
    "tc": "01:50 – 02:25",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Рейтинг Ело 2300 у тринадцять років: другий у світовому табелі після Юдіт Полгар",
    "concept": "Холодний, напівтемний шаховий турнірний зал у Лондоні. Десятки столів із зеленими сукняними скатертинами. Камера фокусується на 13-річному хлопчикові, який грає проти сивого дорослого майстра. Хлопчик робить жертовний хід турою, навіть не дивлячись на дошку.",
    "why_it_works": "Фіксує феноменальну силу інтуїції: здатність миттєво оцінювати глибину позиції без перебору мільйонів варіантів.",
    "p1_start": "Cinematic wide-angle shot of a quiet 1989 London chess tournament hall, rows of wooden tables with green felt covers, a 13-year-old British-Cypriot boy in a simple navy sweater sitting opposite an older bearded chess master, dramatic overhead pendant lighting --ar 16:9",
    "p2_flow": "Slow tracking camera pushes past the tense, sweating opponent directly toward the young prodigy's hand. His fingers smoothly slide a white rook into an aggressive sacrifice square; air around the chessboard ripples with an invisible kinetic wave of mental energy, 24fps.",
    "p3_end": "Intimate cinematic close-up of the 13-year-old boy looking up with calm, absolute certainty, dark focused eyes, soft Rembrandt lighting, moody tournament hall bokeh, 35mm film grain, 4k --ar 16:9",
    "davinci_recipe": "Color: Знебарвлення фону (Saturation 70%), підсилення зеленого сукна столу та теплого світла над дошці. М'який Lens Blur на супернику.",
    "sfx_cue": "Приглушений шелест кроків суддів по паркету, поодинокі тихі клацання годинників у залі. Сухий удар турою по клітинці та глибокий видих суперника."
  },
  {
    "id": 6,
    "num": "06",
    "name_ua": "Піксельна студія Bullfrog у Гілфорді",
    "name_en": "The 1993 Bullfrog CRT Sanctum",
    "cat": "gaming",
    "cat_label": "🕹️ Геймінг & Пікселі 90-х",
    "cat_color": "cyan",
    "tc": "02:25 – 03:00",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "16-річний підліток серед дискет, коробок від піци та моніторів Commodore Amiga",
    "concept": "Захаращена кімната легендарної ігрової студії 1993 року. Скрізь коробки з-під піци, банки з газованою водою, стопки 3.5-дюймових дискет. 16-річний хлопець в оверсайз-светрі сидить за комп'ютером Commodore Amiga 500 і пише код симуляції штучного інтелекту відвідувачів парку.",
    "why_it_works": "Показує практичний вхід у геймдев: як створення ігор стало для героя першою пісочницею для тестування систем штучного інтелекту.",
    "p1_start": "Nostalgic 1993 video game studio interior: messy desks littered with floppy disks, pizza boxes, cathode-ray monitors glowing in a dimly lit room, a 16-year-old teenage programmer in an oversized vintage wool sweater typing intensely, authentic 90s aesthetic --ar 16:9",
    "p2_flow": "Camera tracks over mountains of floppy disks and CRT monitors. The camera glides directly into the curvature of the Amiga monitor, where scrolling lines of C-code dissolve seamlessly into vibrant colorful 2D isometric pixel-art sprites of a theme park roller-coaster, 24fps.",
    "p3_end": "Macro shot of a high-resolution CRT monitor displaying charming 1990s isometric 16-bit pixel-art theme park simulation with tiny moving visitors and looping rollercoasters, vibrant color palette, visible phosphor RGB mask, 4k --ar 16:9",
    "davinci_recipe": "Fusion: RGB Split на краях екрана CRT. Color Page: тепла лампова гама 90-х, підняття зеленого та жовтого в тінях.",
    "sfx_cue": "Шум вентиляторів старих комп'ютерів, кулеметний стукіт клавіатури Amiga з високим пружинним звуком. Свист дисковода при читанні флоппі-диска."
  },
  {
    "id": 7,
    "num": "07",
    "name_ua": "Оживлення парку розваг: Theme Park",
    "name_en": "The Isometric Theme Park AI Genesis",
    "cat": "gaming",
    "cat_label": "🕹️ Геймінг & Пікселі 90-х",
    "cat_color": "cyan",
    "tc": "03:00 – 03:45",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Як піксельна гра з мільйонним накладом стала симулятором тисяч автономних агентів",
    "concept": "Починається з класичного ізометричного вигляду гри Theme Park 1994 року: маленькі піксельні чоловічки купують попкорн і катаються на гірках. Раптом камера опускається під кутом 45 градусів, пікселі згладжуються, і сцена перетворюється на гіперреалістичний кінематографічний луна-парк на заході сонця.",
    "why_it_works": "Візуалізує концепцію штучного інтелекту як агента, наділеного бажаннями, бюджетом та емоціями — першу масштабовану симуляцію героя.",
    "p1_start": "Iconic vintage 1994 isometric video game screenshot style: colorful bustling theme park with loop-the-loop rollercoasters, Ferris wheels, popcorn stalls, and thousands of tiny pixelated animated crowd sprites on paved paths, vibrant retro art --ar 16:9",
    "p2_flow": "Camera swoops smoothly down into the miniature pixel world. Flat 2D isometric tiles gain physical volumetric depth, shadows lengthen under an atmospheric setting sun, cartoon textures morph into hyperrealistic brushed steel, glowing neon bulbs, and living crowds, 24fps.",
    "p3_end": "Spectacular wide cinematic aerial shot of a magnificent seaside amusement park at golden hour twilight: glowing Ferris wheel, rushing rollercoaster tracks illuminated by fairy lights, bustling photorealistic crowds, 35mm film still, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Camera 3D Tracker по ізометричній сітці. Плавний Cross-Dissolve текстур від пікселів до PBR-матеріалів металу й неону.",
    "sfx_cue": "8-бітний чіптюн-дзвін аркадних атракціонів, що плавно перетікає в живий гул справжнього парку: сміх людей, крики на американських гірках, шум морського прибою."
  },
  {
    "id": 8,
    "num": "08",
    "name_ua": "Republic: симуляція мільйона душ",
    "name_en": "The 3D Autonomous City Simulation",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "03:45 – 05:15",
    "act": "Акт 1 • Шахи, ZX Spectrum та Bullfrog",
    "tagline": "Створення віртуальної пострадянської держави з мільйоном живих цифрових громадян",
    "concept": "Камера летить над низькополігональною 3D-моделлю похмурого східноєвропейського міста з гри Republic (2003). Полігональні будівлі обростають текстурами бетону, скла і ліхтарів, а траєкторії руху жителів перетворюються на світяться вектори прийняття рішень штучного інтелекту.",
    "why_it_works": "Показує масштаб амбіцій: моделювати не просто гру, а соціологію, політику та психологію всього суспільства всередині коду.",
    "p1_start": "Stylized early 2000s 3D computer game graphics: wireframe and low-polygon architectural model of a sprawling gloomy Eastern European capital city square, monument in center, surveillance camera overlays --ar 16:9",
    "p2_flow": "Smooth aerial fly-through descending into the city center. Low-poly meshes subdivide infinitely into photorealistic weathered concrete facades, asphalt puddles reflecting flickering neon signs; crowds of thousands of citizens walking with autonomous AI intent, 24fps.",
    "p3_end": "Atmospheric cinematic drone shot of a dark cinematic European metropolis at dusk in pouring rain: wet cobblestones reflecting warm tram headlights and cold architectural floodlights, complex atmospheric depth, 4k 24fps --ar 16:9",
    "davinci_recipe": "Color Page: Холодний східноєвропейський нуар (Blue Lift, Yellow Gamma). Додати шар плівкового зерна 35mm та Rain Overlays на верхній доріжці V3.",
    "sfx_cue": "Синтезований низький гул комп'ютерного генератора міста, що переходить у реальний шум дощу по бруківці та далекий дзвін міського трамвая."
  },

  # ACT 2: КЕМБРИДЖ, НЕЙРОБІОЛОГІЯ ТА НАРОДЖЕННЯ DEEPMIND (05:15 - 10:30)
  {
    "id": 9,
    "num": "09",
    "name_ua": "Готичний міст Queens' College",
    "name_en": "The Mathematical Bridge Reverie",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "amber",
    "tc": "05:15 – 05:45",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Кембридж: дерев'яний міст Ньютона через річку Кем як зв'язок математики і природи",
    "concept": "Камера пливе на рівні темної води річки Кем повз знаменитий Математичний міст коледжу Квінс. Ранковий туман над вікторіанською готикою. Дерев'яні балки мосту, побудовані за суворими законами геометричних дотичних, починають світитися оптоволоконними лініями знань.",
    "why_it_works": "Символ академічного фундаменту героя: подвійний диплом Кембриджа з комп'ютерних наук у 21 рік.",
    "p1_start": "Majestic morning mist rising over the River Cam in Cambridge, looking towards the historic wooden Mathematical Bridge and Queens' College Gothic stone facades, soft golden sunrise filtering through weeping willows, 35mm film still --ar 16:9",
    "p2_flow": "Camera glides forward just above the glassy water surface. The intricate wooden geometric beams of the bridge begin to glow with internal azure fiber-optic light, transforming the bridge into an illuminated mathematical neural bridge spanning across time, 24fps.",
    "p3_end": "Cinematic wide frame of Cambridge Gothic architecture bathed in morning amber sunlight, crystalline clear river reflecting stone arches, glowing subtle cyan algorithmic formulas suspended in morning mist, ethereal academic prestige, 4k --ar 16:9",
    "davinci_recipe": "Fusion: Planar Tracker по воді річки для інтеграції відбиття неонових ліній мосту. Color: золотистий Teal & Orange з м'яким спадом контрасту в тінях.",
    "sfx_cue": "Плескіт весла по спокійній воді річки, далекий передзвін кембриджських дзвонів. Теплий акорд акустичної віолончелі на -10 dB."
  },
  {
    "id": 10,
    "num": "10",
    "name_ua": "Флуоресцентний зріз гіпокампа",
    "name_en": "The Hippocampal Dendritic Tree",
    "cat": "neuro",
    "cat_label": "🧠 Нейробіологія & fMRI",
    "cat_color": "emerald",
    "tc": "05:45 – 06:15",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Дослідження людського мозку в UCL: пошук архітектури пам'яті під мікроскопом",
    "concept": "Мікроскопічний зріз тканин людського гіпокампа, пофарбований флуоресцентними барвниками. Живі нейрони світяться смарагдовим і фіолетовим. Камера слідує за електричним імпульсом уздовж аксона, який плавно переходить у цифровий штучний перцептрон штучної нейромережі.",
    "why_it_works": "Пояснює секрет успіху DeepMind: замість сліпого копіювання комп'ютерного коду вони перенесли в алгоритми реальну архітектуру мозку.",
    "p1_start": "High-magnification confocal fluorescence microscopy of human brain hippocampal tissue, glowing green dendritic spines and purple pyramidal neurons interconnected in organic density, dark scientific background --ar 16:9",
    "p2_flow": "Camera zooms down a single fluorescent neuron axon as a bright violet action potential electrical spark travels along its length. The organic biological tissue seamlessly transitions into a sleek geometric silicon lattice of artificial neural network nodes, 24fps.",
    "p3_end": "Hyperrealistic 3D visualization of a multi-layer deep artificial neural network: glowing emerald and violet synaptic nodes firing in complex rhythm, floating in a clean optical cybernetic void, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: FastNoise + Glow на розрядах аксонів. Застосувати Color Match між органічним флуоресцентним зеленим та фірмовим смарагдовим кольором DeepMind.",
    "sfx_cue": "Глибокий ультразвуковий гул медичного томографа fMRI (ритмічний стукіт магнітів). Раптовий сухий електричний клацання біологічного синапсу."
  },
  {
    "id": 11,
    "num": "11",
    "name_ua": "Дзеркало пам'яті та уяви",
    "name_en": "The Memory-Imagination Dual Mirror",
    "cat": "split",
    "cat_label": "⚡ Драматичний розкол",
    "cat_color": "amber",
    "tc": "06:15 – 06:45",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Відкриття в журналі Science: людина без пам'яті не здатна уявити власне майбутнє",
    "concept": "Екран розділений на дві дзеркальні половини: зліва — архів спогадів (старі фотографії, теплі сепієві кадри минулого), справа — порожнеча майбутнього, яка конструюється з тих самих блоків у режимі реального часу. Камера проходить крізь межу, поєднуючи пам'ять і уяву в єдиний симуляційний двигун.",
    "why_it_works": "Філософський стрижень епізоду: штучний інтелект повинен не просто запам'ятовувати дані, а симулювати варіанти майбутнього.",
    "p1_start": "Split-screen cinematic composition: left side shows warm nostalgic sepia photographs floating in vintage liquid amber; right side is a cold crystalline dark blue void with empty spatial grids, conceptual fine art lighting --ar 16:9",
    "p2_flow": "The dividing glass line shatters into microscopic prisms. Fragments of the past on the left dissolve into glowing voxel bricks that fly across the frame into the right void, automatically assembling into a futuristic architectural simulation, 24fps.",
    "p3_end": "Mesmerizing surrealist film still: a solitary researcher standing at the nexus of past memories and future digital simulations, illuminated by floating golden holographic panels, cinematic anamorphic lens, 4k --ar 16:9",
    "davinci_recipe": "Edit: Split Screen з вертикальною маскою Wipe. Fusion: Shatter Effect на розділовій смузі. Color: теплий Tungsten зліва проти холодного Cyan справа.",
    "sfx_cue": "Шелест старих фотографій, що переходить у тонкий кришталевий дзвін розбитого дзеркала. Потім — тихий космічний суб-бас 50Hz."
  },
  {
    "id": 12,
    "num": "12",
    "name_ua": "Experience Replay: як спить алгоритм",
    "name_en": "The Sleep Replay Dream Cycle",
    "cat": "neuro",
    "cat_label": "🧠 Нейробіологія & fMRI",
    "cat_color": "emerald",
    "tc": "06:45 – 07:15",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Перенесення механізму сну в код: прискорене повторення досвіду вночі",
    "concept": "Темна лабораторія. Силует дослідника, що схилив голову на стіл поруч із чашкою чаю. Навколо нього в повітрі з шаленою швидкістю кружляють сотні напівпрозорих екранів, на яких прискорено програються записи минулих ігор, закріплюючи нейронні ваги алгоритму.",
    "why_it_works": "Пояснює проривний алгоритмічний прийом: машина вчиться не під час самої гри, а коли багаторазово переглядає свої помилки під час «сну».",
    "p1_start": "Cinematic low-key shot of an empty technology laboratory at 3 AM, a single desk illuminated by a green banker's lamp, steam rising from a ceramic mug of tea, deep shadows and atmosphere --ar 16:9",
    "p2_flow": "Camera pulls back smoothly. Out of the darkness around the desk emerge dozens of semi-transparent holographic video frames floating in orbital rings, replaying game actions at 100x speed, streams of glowing cyan particles flowing between the monitors into a central neural core, 24fps.",
    "p3_end": "Stunning sci-fi documentary frame: a glowing cerebral neural core pulsing in the center of a dark London laboratory, surrounded by floating ribbons of high-speed training simulations, moody architectural lighting, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Duplicate з круговою спіральною траєкторією. Режим накладання Screen для плаваючих екранів. Color: глибокий синій монохром з акцентом на зелену лампу.",
    "sfx_cue": "Рівний тихий шум кондиціонера серверної, звук прискореного перемотування відеоплівки (High-speed tape whirr на -12 dB) з ритмічним серцебиттям алгоритму."
  },
  {
    "id": 13,
    "num": "13",
    "name_ua": "Russell Square: маніфест двох кроків",
    "name_en": "The Two-Step AGI Manifesto",
    "cat": "typo",
    "cat_label": "🔤 Кінетична типографіка",
    "cat_color": "cyan",
    "tc": "07:15 – 07:45",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "«Крок перший: Розв'язати інтелект. Крок другий: Використати його, щоб розв'язати все інше»",
    "concept": "Лондон, осінь 2010 року. Напівпідвальний офіс на площі Рассел-сквер. На білій маркерній дошці рукою засновника виведено два короткі пункти плану. Літери чорного маркера спалахують сліпучим білим світлом і трансформуються у монументальні тривимірні титри, що ширяють над нічним Лондоном.",
    "why_it_works": "Культовий маніфест, який сформулював мету AGI задовго до того, як це стало трендом у Кремнієвій Долині.",
    "p1_start": "Close-up of a dry-erase whiteboard in a modest 2010 London office with exposed brick walls, handwritten black marker text reading 'Step 1: Solve Intelligence. Step 2: Solve Everything Else.', natural grey London window light --ar 16:9",
    "p2_flow": "Camera tracks across the written words as the black marker strokes ignite with brilliant phosphor white luminescence, detaching from the whiteboard surface into three-dimensional typographic monoliths hovering in cinematic air, 24fps.",
    "p3_end": "Monumental typographic art: the words 'SOLVE INTELLIGENCE' rendered as colossal brushed-steel typographic sculptures standing against the dramatic stormy London twilight skyline, British flag on horizon, 4k 24fps --ar 16:9",
    "davinci_recipe": "Fusion: Text+ 3D Extrusion по вектору рукописного шрифту. Color: Film Look 35mm, насичений графітовий тон цегляної стіни.",
    "sfx_cue": "Сухий скрип повстяного маркера по дошці. Потім — потужний, глибокий кінематографічний саб-дроп (Braam 35Hz на -3 dB), що струшує кімнату."
  },
  {
    "id": 14,
    "num": "14",
    "name_ua": "Дуель столиць: Лондон проти Каліфорнії",
    "name_en": "The Transatlantic AI Standoff",
    "cat": "split",
    "cat_label": "⚡ Драматичний розкол",
    "cat_color": "amber",
    "tc": "07:45 – 08:15",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Академічна стриманість Блумсбері проти агресивного венчурного капіталу Сан-Франциско",
    "concept": "Екран розділений контрастом двох культур: зліва — дощовий Лондон, старовинні університетські бібліотеки, твідові піджаки і тиша лабораторій. Справа — сліпуче сонце Кремнієвої долини, скляні кампуси стартапів, венчурні чеки на мільярди. Камера пролітає крізь атлантичний підводний оптоволоконний кабель, що з'єднує два світи.",
    "why_it_works": "Показує унікальну позицію Гассабіса: відмова переїжджати до Долини і перетворення Лондона на світову столицю фундаментального штучного інтелекту.",
    "p1_start": "Split-composition: left half shows rain-slicked Victorian streetlamps and brick libraries of Bloomsbury London at dusk; right half shows blazing sunny California glass tech skyscrapers and palm trees in San Francisco, architectural contrast --ar 16:9",
    "p2_flow": "Camera plunges below sea level into the deep Atlantic Ocean. A glowing transoceanic fiber-optic cable pulses with blinding packets of azure and gold data, bridging the two hemispheres at supersonic speed, 24fps.",
    "p3_end": "Dramatic aerial cinematic shot over London St. Pancras and King's Cross tech quarter at dusk, rain-washed futuristic glass structures glowing alongside historic Victorian brickwork, epic scale, 4k --ar 16:9",
    "davinci_recipe": "Edit: Dynamic Wipe переход через лінію кабелю. Color: холодний дощовий Cyan для Лондона, теплий золотистий Amber для Каліфорнії.",
    "sfx_cue": "Зліва — шум лондонського дощу та гудки кебів. Справа — дзвін кавових апаратів Сан-Франциско. На кабелі — підводний низький вакуумний гул."
  },
  {
    "id": 15,
    "num": "15",
    "name_ua": "Atari Breakout: винахід тунелю",
    "name_en": "The Reinforcement Q-Learning Breakthrough",
    "cat": "gaming",
    "cat_label": "🕹️ Геймінг & Пікселі 90-х",
    "cat_color": "cyan",
    "tc": "08:15 – 08:45",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Алгоритм без жодних правил відкриває стратегію, невідому навіть людям",
    "concept": "Екран класичної гри Breakout на аркадному автоматі 1976 року: стіна з кольорових цеглин, платформа і м'ячик. Спочатку алгоритм безпорадно пропускає м'яч. Потім кількість спроб перескакує на 100 000: м'яч з неймовірною швидкістю пробиває тонкий вертикальний тунель у лівому кутку і починає рикошетити за спиною стіни, знищуючи все.",
    "why_it_works": "Перший тріумф Deep Reinforcement Learning: штучний інтелект відкриває власну геніальну стратегію, спираючись лише на підкріплення очками.",
    "p1_start": "Extreme macro of a 1970s vintage arcade monitor screen displaying the classic Breakout game: horizontal rows of rainbow colored pixel blocks, a moving white paddle at the bottom, scanlines visible on curved glass --ar 16:9",
    "p2_flow": "Ultra high-speed gameplay evolution: the white pixel ball accelerates into a glowing laser trail. It methodically carves a narrow tunnel through the left wall of bricks, breaking out into the space behind the wall, detonating all remaining blocks in a cascade of neon particles, 24fps.",
    "p3_end": "Explosion of 8-bit digital neon sparks against a pitch black void, glowing rectangular voxel blocks shattering outward in zero gravity, vivid retro-futuristic arcade aesthetics, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Particle Emitter для розльоту неонових блоків. На кожному ударі м'яча — Frame Flash (яскравість +20% на 1 кадр).",
    "sfx_cue": "Автентичні аркадні звуки біпів та пінгів гри Breakout, які перетворюються на кулеметний каскад вибухів під час знищення верхнього ряду цеглин."
  },
  {
    "id": 16,
    "num": "16",
    "name_ua": "Кодекс етичного вето: замок від зброї",
    "name_en": "The Ethics Board Firewall Covenant",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "08:45 – 09:15",
    "act": "Акт 2 • Кембридж та нейронаука DeepMind",
    "tagline": "Умова продажу за пів мільярда доларів: абсолютна заборона на військове застосування",
    "concept": "Важкий юридичний контракт на темному дерев'яному столі. На тексті пункту про поглинання лежить важка срібна печатка. По чорнилу документа спалахує захисний голографічний фаєрвол, який символічно блокує будь-які спроби використати алгоритми для автономної зброї чи стеження.",
    "why_it_works": "Демонструє принциповість Гассабіса: збереження контролю над призначенням технології навіть перед лицем колосальних грошей.",
    "p1_start": "Macro cinematic shot of a formal legal contract lying on a dark executive mahogany desk, crisp printed typography with prominent clauses, an embossed metallic seal resting beside a fountain pen, moody dramatic lighting --ar 16:9",
    "p2_flow": "Camera pans across the contract clauses as a glowing translucent cybernetic firewall grid emerges from the paper fibers, forming a protective domed barrier of interlocking amber security shields above the document, 24fps.",
    "p3_end": "Photorealistic 3D holographic security emblem hovering over the parchment contract, glowing amber and cyan geometric shields projecting mathematical proofs of safety and ethical protocols, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Shield з нодою Glow та Displace. Color: нуарний монохромний контраст із теплим золотим сяйвом печатки.",
    "sfx_cue": "Важкий глухий удар металевої печатки об стіл. Потім — низький захисний гул активованого силового поля (Energy shield hum на -6 dB)."
  },

  # ACT 3: ХІД 37, СЕУЛ ТА ОРІГАМІ ЖИВОГО БІЛКА (09:15 - 16:45)
  {
    "id": 17,
    "num": "17",
    "name_ua": "Гобан із вікового дерева кайя",
    "name_en": "The Sacred Kaya Wood Goban Grid",
    "cat": "chess",
    "cat_label": "♟️ Шаховий інтелект",
    "cat_color": "purple",
    "tc": "09:15 – 10:00",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Стародавня дошка для гри в Го: десять у сто сімдесятому ступені можливих всесвітів",
    "concept": "Екстремальне макро традиційної японської дошки гобан із цілісного масиву вікового дерева кайя. Чорні базальтові та білі перламутрові камені з раковин молюсків лежать на сітці 19х19 ліній. Дерево випромінює теплий смолистий блиск, а лінії сітки вигинаються, показуючи викривлення простору комбінацій.",
    "why_it_works": "Підкреслює колосальну складність гри: комбінацій у Го більше, ніж усіх атомів у видимому Всесвіті. Перебором цю гру не розв'язати ніколи.",
    "p1_start": "Extreme macro photograph of a traditional Japanese Kaya wood Goban board, carved grid lines on rich golden timber, one smooth black slate stone and one iridescent white clamshell Go stone resting on intersections, shallow depth of field --ar 16:9",
    "p2_flow": "Camera tracks across the 19x19 black grid lines. The carved lines begin to hum with subtle optical luminescence, warping and bending like spacetime around black holes as the black and white stones mirror distant planetary orbits, 24fps.",
    "p3_end": "Breathtaking macro view of a Go board transforming into a cosmic star chart: black stones acting as dark matter singularities, white stones glowing as bright newborn stars connected by constellations of probability, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Grid Warp Node для м'якого викривлення сітки ліній. Color: теплий медовий тон дерева кайя (Hue 38°) та глибокий матовий чорний для базальту.",
    "sfx_cue": "Глибокий, соковитий клацаючий стукіт каменя Го об дерево кайя (знаменитий звук 'клак' з довгим резонансом порожнини дошки)."
  },
  {
    "id": 18,
    "num": "18",
    "name_ua": "Сеульська ніч у Four Seasons",
    "name_en": "The Seoul Midnight Arena",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "10:00 – 10:45",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Березень 2016: 500 журналістів, подих Азії та погляд легендарного Лі Седоля",
    "concept": "Величезний прес-зал готелю Four Seasons у Сеулі. Темрява навколо сцени, де під одиночним прожектором сидить чемпіон світу Лі Седоль у темному костюмі. Перед ним — дошка. Камера повільно наїжджає на його напружене обличчя, в очах якого відбивається тисячолітня традиція людської інтуїції.",
    "why_it_works": "Створює відчуття історичної дуелі: людина захищає останній бастіон чистого духу проти машинного інтелекту.",
    "p1_start": "Cinematic wide shot of the grand Four Seasons Seoul press auditorium in March 2016, dim room packed with hundreds of international journalists, a solitary illuminated stage with a wooden table, two players in sharp dark suits, intense silence --ar 16:9",
    "p2_flow": "Slow, hypnotic crane push-in across the silent auditorium towards the wooden table. Lighting focuses into a single theatrical spotlight; room background fades into absolute graphite void, isolating the champion master staring at the board in profound concentration, 24fps.",
    "p3_end": "Intimate cinematic 35mm film still of the Asian Go grandmaster's face: sweat glinting on his brow, dark pupils locked on the board, cigarette smoke drifting through spotlight beams, profound psychological gravity, 4k --ar 16:9",
    "davinci_recipe": "Color: Зниження експозиції залу на -2.5 EV, залишаючи лише вузький промінь прожектора на гравцеві. Підсилення плівкового шуму 35mm на обличчі.",
    "sfx_cue": "Повна вакуумна тиша 500 людей у залі. Ледь чутне клацання фотозатворів далеко позаду та гучний стукіт власного серця гравця (Low-end thud 60 BPM)."
  },
  {
    "id": 19,
    "num": "19",
    "name_ua": "Хід 37: удар у порожнечу п'ятої лінії",
    "name_en": "The Move 37 Extraterrestrial Stone",
    "cat": "chess",
    "cat_label": "♟️ Шаховий інтелект",
    "cat_color": "purple",
    "tc": "10:45 – 11:30",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Один шанс із десяти тисяч: народження нелюдської креативності у прямому ефірі",
    "concept": "Надповільна зйомка (1000 кадрів/сек): рука оператора опускає чорний камінь на нечувану позицію — п'яту лінію від краю дошки, у повну порожнечу. У момент дотику каменя дерево вибухає безшумною ударною хвилею чистого золотого світла, яка розгортає нову парадигму мислення.",
    "why_it_works": "Кульмінація серіалу: машина зробила хід, який жодна людина не робила за 3000 років історії, довівши наявність власної справжньої креативності.",
    "p1_start": "Super slow-motion close-up of a human hand placing a single polished black slate Go stone onto an unconventional intersection on the 5th line of a wooden Goban, dramatic rim lighting, dust motes frozen in air --ar 16:9",
    "p2_flow": "The instant the black stone touches the wood, a circular golden sonic shockwave ripples outward through the timber grain. The surrounding grid lines detach from the surface, expanding into an alien multi-dimensional geometric web of pure intuition, 24fps.",
    "p3_end": "Breathtaking visual of a solitary black stone radiating coherent golden laser lattice lines across an infinite obsidian plane, symbol of an alien intelligence creating new knowledge, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Ripple Node + 3D Shockwave з маскою від точки дотику каменя. Color: яскравий спалах Golden Core на 2 кадри в точці контакту.",
    "sfx_cue": "Сухий, кришталевий звук удару каменя (на 0 dB), за яким миттєво слідує глибокий інфразвуковий космічний рокіт (Sub-bass 25Hz), що розходиться луною."
  },
  {
    "id": 20,
    "num": "20",
    "name_ua": "П'ятнадцять хвилин шоку: погляд чемпіона",
    "name_en": "The 15-Minute Champion Stupor",
    "cat": "split",
    "cat_label": "⚡ Драматичний розкол",
    "cat_color": "amber",
    "tc": "11:30 – 12:15",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "П'ятнадцять хвилин нерухомості перед дошкою та усвідомлення нової епохи",
    "concept": "Камера застигає навпроти обличчя чемпіона, який повертається в залу і бачить Хід 37. Він сідає в крісло і не рухається п'ятнадцять хвилин. Тіні від вікон повільно рухаються по його обличчю у прискореному часі, поки його очі намагаються осягнути логіку, яку не писав жоден смертний майстер.",
    "why_it_works": "Передає психологічний злам людського его перед лицем вищого нелюдського інтелекту: від заперечення до глибокої поваги.",
    "p1_start": "Intense portrait of the Asian Go grandmaster sitting completely motionless at the wooden match table, pale face bathed in cold studio light, his unblinking dark eyes fixed on the board in profound disbelief, 35mm film grain --ar 16:9",
    "p2_flow": "Time-lapse shadows sweep smoothly across the grandmaster's face as the world around him accelerates. The air temperature visually cools into cyan tones; his motionless silhouette remains an anchor while transparent digital heat waves shimmer above the board, 24fps.",
    "p3_end": "Poignant cinematic close-up of the grandmaster's eyes: a single tear reflecting the illuminated Go board, quiet acceptance of a new era of intelligence dawning upon humanity, master documentary photography, 4k --ar 16:9",
    "davinci_recipe": "Color: Поступовий спад колірної температури від 4500K до 3200K (ефект поступового охолодження сцени). М'який Optical Flow на тінях.",
    "sfx_cue": "Повний вакуум звуку (Mute 0.0 dB). Потім — один єдиний важкий удар серця на -4 dB і далекий приглушений голос коментатора: 'That is not a human move'."
  },
  {
    "id": 21,
    "num": "21",
    "name_ua": "AlphaZero: гра проти власної тіні",
    "name_en": "The Mirror Dimension Self-Play",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "12:15 – 13:00",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Мільйони партій алгоритму проти самого себе: нуль людських підручників, абсолютна сила",
    "concept": "Дзеркальний коридор нескінченності. З двох боків дзеркала стоять однакові шахові та го-позиції. Прозорі енергетичні фігури грають самі проти себе на світловій швидкості. Кожна помилка однієї сторони миттєво стає зброєю іншої, поки система не досягає абсолютного божественного рівня гри.",
    "why_it_works": "Візуалізує концепцію Self-Play: відмову від людських знань заради досягнення чистих математичних істин Всесвіту.",
    "p1_start": "Surreal infinite mirror corridor with polished dark obsidian floor, reflecting identical illuminated chessboards receding into infinity, cold monochrome lighting with cyan edge glow --ar 16:9",
    "p2_flow": "High-speed optical recursion: pieces on both sides of the mirror move simultaneously without hands, striking and countering at lightspeed. The mirror barrier dissolves into a swirling fluid vortex of golden binary probability equations, 24fps.",
    "p3_end": "Monumental symmetrical visualization of two mirrored crystalline entities engaging in an infinite game of hyper-dimensional strategy, glowing emerald and gold energy ribbons intertwining, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Mirror Node + Feedback Loop з дифузійним розмиттям на кожному циклі. Color: симетричний контраст із неоновим смарагдовим свіченням у центрі.",
    "sfx_cue": "Прискорений калейдоскоп сотень сухих клацань фігур, що зливаються в єдиний монолітний гул високої частоти (Drone sweep)."
  },
  {
    "id": 22,
    "num": "22",
    "name_ua": "Крок Другий: ранковий декрет у номері",
    "name_en": "The Hotel Room Step-Two Decree",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "13:00 – 13:45",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "«Ігри закінчилися. Ми переходимо до біології»: ранок після тріумфу в Сеулі",
    "concept": "Ранок після матчу. Номер готелю Four Seasons. На столику стоїть недопита чашка кави. Засновник закриває кришку ноутбука з грою в Го і відкриває файл із тривимірною кристалічною моделлю людського білка. Погляд холодний і зосереджений: тріумф уже в минулому, попереду — найбільша таємниця життя.",
    "why_it_works": "Показує невблаганну стратегічну дисципліну: не спочивати на лаврах поп-культури, а спрямувати зброю ШІ на порятунок людських життів.",
    "p1_start": "Cinematic morning interior of a luxury Seoul hotel suite overlooking misty glass skyscrapers at dawn, an open laptop on a desk showing Go board logs, a ceramic coffee cup, cool morning daylight, 35mm film grain --ar 16:9",
    "p2_flow": "A man's hand reaches out and closes the laptop lid. As the screen folds down, camera pans to a second vertical monitor awakening with brilliant color, rendering an intricate 3D biological protein macromolecule rotating in space, 24fps.",
    "p3_end": "Hyperrealistic scientific 3D render of a biological enzyme protein on a dark lab monitor screen: complex amino acid ribbon twisting in spatial depth, glowing cyan alpha-helices and gold beta-sheets, clean modern laboratory aesthetic, 8k --ar 16:9",
    "davinci_recipe": "Edit: Match Cut на закритті ноутбука та появі молекули. Color: перехід від холодного синього світанку до теплого біолюмінесцентного сяйва білка.",
    "sfx_cue": "Сухий звук захлопування кришки ноутбука. Потім — тихий космічний акорд струнних, що сигналізує про початок нової великої місії."
  },
  {
    "id": 23,
    "num": "23",
    "name_ua": "Рентгенівська кристалографія: 50 років сліпоти",
    "name_en": "The Crystallography Frozen Lattice",
    "cat": "bio",
    "cat_label": "🧬 Молекулярне орігамі",
    "cat_color": "rose",
    "tc": "13:45 – 14:30",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "П'ять років праці та мільйон доларів заради розшифровки форми лише однієї молекули",
    "concept": "Холодна, стерильна наукова лабораторія кінця XX століття. Рентгенівська дифракційна трубка випромінює синє світло крізь заморожений кристал білка. На фотопластинці проступають складні концентричні точки дифракції. Камера занурюється в ці точки: темрява невідомості, яка мучила людство пів століття.",
    "why_it_works": "Пояснює масштаб проблеми: у природі 200 мільйонів білків. Фізичними методами людству знадобився б мільярд років на їх розшифровку.",
    "p1_start": "Archival scientific laboratory photograph: a heavy industrial X-ray crystallography apparatus in a darkened room, cold beam of ultraviolet light striking a microscopic frozen protein crystal in a loop, metallic apparatus, sterile realism --ar 16:9",
    "p2_flow": "Camera moves into the circular X-ray diffraction detector screen. Concentric patterns of black diffraction dots begin to vibrate and radiate coherent azure laser beams, expanding outward like a mathematical galaxy of spatial coordinates, 24fps.",
    "p3_end": "Complex diffraction pattern of thousands of glowing turquoise data points suspended in dark space, casting delicate shadow projections of atomic positions, high-end scientific visualization, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Displace з використанням маски дифракційних кілець. Color: холодний кобальтовий монохромний вигляд (Blue Gain +0.08).",
    "sfx_cue": "Шипіння рідкого азоту, важкий клацаючий затвор рентгенівського апарата, монотонний гул вакуумних насосів лабораторії."
  },
  {
    "id": 24,
    "num": "24",
    "name_ua": "Амінокислотна стрічка: молекулярне орігамі",
    "name_en": "The Molecular Origami Transformer",
    "cat": "bio",
    "cat_label": "🧬 Молекулярне орігамі",
    "cat_color": "rose",
    "tc": "14:30 – 15:15",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Як плоска нитка амінокислот за мілісекунди згортається у найскладніший тривимірний вузол життя",
    "concept": "Довга плоска нитка з амінокислотних ланок вільно пливе у воді. Раптом під дією алгоритмічної сили уваги нитка починає шалено крутитися: формуються альфа-спіралі, складаються бета-листи, атоми водню знаходять свої пари, і за частку секунди виникає бездоганна тривимірна архітектура білка.",
    "why_it_works": "Найвеличніше візуальне видовище сучасної науки: розгадка таємниці орігамі білка, за яку Гассабіс отримав Нобелівську премію.",
    "p1_start": "Scientific macro visualization: a linear, flexible unfolded ribbon polypeptide chain of amino acids floating in aquatic cellular fluid, individual atomic spheres softly glowing in cyan and gold, shallow depth of field --ar 16:9",
    "p2_flow": "Real-time molecular folding simulation: invisible spatial attention vectors grip the ribbon. In hypnotic fluid motion, the chain coils into tight alpha-helices, pleats into beta-sheets, and snaps with atomic precision into a dense 3D functional protein knot, 24fps.",
    "p3_end": "Breathtaking scientific masterpiece render: completed biological protein macromolecule in full atomic detail, shimmering translucent ribbons, golden active binding pocket illuminated from within, Octane 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Alembic/FBX імпорт молекули білка. Застосувати PBR-матеріали Subsurface Scattering (SSS) для напівпрозорості органіки.",
    "sfx_cue": "Підводний органічний звук текучої води. На згортанні білка — чарівний каскадний шелест тисяч мікроскопічних магнітів, що зчіплюються докупи."
  },
  {
    "id": 25,
    "num": "25",
    "name_ua": "Олімпіада CASP14: точність до одного атома",
    "name_en": "The Atomic Precision CASP Revelation",
    "cat": "bio",
    "cat_label": "🧬 Молекулярне орігамі",
    "cat_color": "rose",
    "tc": "15:15 – 16:00",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Листопад 2020: 92.4 бали зі 100. П'ятдесятирічну загадку біології розв'язано",
    "concept": "На екрані вченого CASP зливаються дві моделі: експериментальна кристалічна структура білка (зелена) та прогноз нейромережі AlphaFold 2 (синя). Вони накладаються одна на одну з атомною точністю — розбіжність становить менше товщини одного атома вуглецю. Зал світових біологів завмирає у благоговінні.",
    "why_it_works": "Момент історичної перемоги: штучний інтелект вперше вирішив фундаментальну наукову проблему такого рівня, ставши інструментом пізнання всесвіту.",
    "p1_start": "Split 3D wireframe render of two separate complex protein models hovering side by side: one glowing green experimental lattice, one glowing cyan algorithmic prediction lattice, dark background --ar 16:9",
    "p2_flow": "The two protein wireframes drift toward each other and snap into perfect superposition. Every atom and chemical bond aligns with absolute mathematical perfection, glowing with a harmonious unified emerald aura as precision telemetry reads 92.4 GDT, 24fps.",
    "p3_end": "Flawless atomic-resolution molecular model with holographic telemetry readouts displaying zero deviation, golden hydrogen bonds sparkling, scientific triumph aesthetic, 8k render --ar 16:9",
    "davinci_recipe": "Edit: швидкий Snap Zoom на моменті повного збігу моделей. Color: зелений і синій спектри зливаються у фірмовий смарагдовий колір перемоги.",
    "sfx_cue": "Тонкий високочастотний тон калібрування, який у момент ідеального збігу перетворюється на дзвінкий кришталевий акорд фортепіано."
  },
  {
    "id": 26,
    "num": "26",
    "name_ua": "Галактика 200 мільйонів білків",
    "name_en": "The 200-Million Protein Cosmogenesis",
    "cat": "bio",
    "cat_label": "🧬 Молекулярне орігамі",
    "cat_color": "rose",
    "tc": "16:00 – 16:45",
    "act": "Акт 3 • Хід 37 та орігамі живого білка",
    "tagline": "Безкоштовний дар людству: повне дерево життя Землі розшифровано за кілька місяців",
    "concept": "Камера від'їжджає від однієї молекули білка у відкритий космос. Поруч спалахує друга, третя, десята... Мільйони білкових структур заповнюють простір, утворюючи гігантську спіральну галактику з 200 мільйонів молекул — усю біологічну біосферу планети Земля, освітлену світлом знань.",
    "why_it_works": "Показує безпрецедентну щедрість науки: DeepMind виклав усю базу AlphaFold у відкритий доступ, прискоривши медицину на сотні років уперед.",
    "p1_start": "Macro shot of a single glowing biological protein molecule floating in a dark vacuum, radiating soft cyan luminescence from its peptide bonds --ar 16:9",
    "p2_flow": "Exponential exponential camera pull-back: millions of diverse protein structures emerge across all spatial coordinates, clustering into dense glowing arms of a vast biological spiral galaxy, pulsating with organic life, 24fps.",
    "p3_end": "Majestic IMAX-scale cosmic visual: an entire galaxy composed of 200 million illuminated 3D protein structures rotating in deep space, glowing gold, magenta and turquoise, the ultimate digital library of terrestrial life, 8k 24fps --ar 16:9",
    "davinci_recipe": "Fusion: 3D Particle Cloud з 50 000 інстансів для створення галактичного рукава. Повільний повільний рух камери Orbit 360°.",
    "sfx_cue": "Монументальне симфонічне крещендо (Suno Theme 3: Origami of Life на -2 dB) з космічним ревербераційним шлейфом та звуком зоряного пилу."
  },

  # ACT 4: ПОЛІМАТИЧНИЙ РОЗУМ, НОБЕЛЬ ТА ТЕЛЕСКОП ЖИТТЯ (16:45 - 21:30)
  {
    "id": 27,
    "num": "27",
    "name_ua": "Термоядерний тороїд: магнітна клітка плазми",
    "name_en": "The Magnetic Tokamak Plasma Cage",
    "cat": "quantum",
    "cat_label": "⚛️ Термояд & Фізика",
    "cat_color": "purple",
    "tc": "16:45 – 17:30",
    "act": "Акт 4 • Поліматичний розум і Нобелівський тріумф",
    "tagline": "Штучний інтелект утримує зорю на Землі: керування плазмою у 100 мільйонів градусів",
    "concept": "Камера заглядає всередину вакуумної камери термоядерного реактора Tokamak. Велетенський тороїд із розпеченої до 100 мільйонів градусів фіолетової плазми кружляє з шаленою швидкістю. Невидимі магнітні поля, якими в реальному часі керує штучний інтелект, утримують вогняну зорю за міліметри від сталевих стінок.",
    "why_it_works": "Показує поліматичний масштаб: після біології алгоритми Гассабіса приборкують фундаментальну фізику зірок для отримання нескінченної чистої енергії.",
    "p1_start": "Cinematic interior view of a massive experimental fusion tokamak reactor: curved metallic beryllium armor tiles in a circular chamber, industrial engineering perfection, cold slate lighting --ar 16:9",
    "p2_flow": "The reactor ignites: a blinding vortex of incandescent violet and magenta thermonuclear plasma flares into existence, stabilized dynamically by invisible AI-controlled magnetic flux lines pulsing at thousands of adjustments per second, 24fps.",
    "p3_end": "Hyperrealistic scientific hard sci-fi frame: a stable donut-shaped torus of blinding 100-million-degree thermonuclear plasma hovering perfectly suspended inside the magnetic vacuum chamber, extreme optical flares, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: Lens Flare + Glow + Heat Distortion. Color: контраст між холодним титаном стінок і надгарячим фіолетовим ультрафіолетом плазми.",
    "sfx_cue": "Глухий потужний наростаючий рокіт магнітного поля (Sub-bass drop від 100Hz до 30Hz), що переходить у високий гул іонізованого газу."
  },
  {
    "id": 28,
    "num": "28",
    "name_ua": "Стокгольм 2024: Нобелівське золото за мову життя",
    "name_en": "The Nobel Medal of Living Matter",
    "cat": "optics",
    "cat_label": "🔍 Оптичний трюк",
    "cat_color": "amber",
    "tc": "17:30 – 18:30",
    "act": "Акт 4 • Поліматичний розум і Нобелівський тріумф",
    "tagline": "Жовтень 2024: найвища наукова нагорода людства хлопчику, який починав із шахів",
    "concept": "Макрозйомка важкої золотої Нобелівської медалі з хімії на темно-синьому оксамиті. Камера наближається впритул до рельєфного профілю Альфреда Нобеля. Золотий метал починає плавитися світлом: рельєф оживає і перетворюється на подвійну спіраль ДНК, переплетену з шаховим конем та білковою спіраллю.",
    "why_it_works": "Офіційне визнання світом: комп'ютерні вчені стали найважливішими біологами XXI століття, відкривши нову еру в історії науки.",
    "p1_start": "Extreme macro cinematic photograph of an official solid gold Nobel Prize medal resting on deep royal blue velvet, intricate classical engraved profiles in razor-sharp focus, warm dramatic directional studio lighting, 35mm film grain --ar 16:9",
    "p2_flow": "Camera tracks across the golden medal surface. The engraved allegorical figures softly ignite with golden photoluminescence; the metallic relief dissolves into a living 3D double helix of DNA intertwined with an intricate biological protein ribbon and a transparent crystal chess knight, 24fps.",
    "p3_end": "Harmonious artistic masterpiece: a crystalline chess knight, a glowing DNA double helix, and an origami protein molecule united into a singular golden trinity sculpture against a dark velvet void, 8k render --ar 16:9",
    "davinci_recipe": "Fusion: 3D Morphing між поверхнею золотої медалі та моделями молекул. Color: насичений золотий тон (Gain Red/Green) на королівському синьому тлі.",
    "sfx_cue": "Урочистий відголосок оплесків Стокгольмської концертної зали, що розчиняється в чистому, пронизливому соло скрипки на високій ноті."
  },
  {
    "id": 29,
    "num": "29",
    "name_ua": "Нічна зміна: 00:00 – 04:00",
    "name_en": "The Midnight-to-4AM Polymath Sanctuary",
    "cat": "noir",
    "cat_label": "🕵️ Шпигунський нуар",
    "cat_color": "rose",
    "tc": "18:30 – 19:45",
    "act": "Акт 4 • Поліматичний розум і Нобелівський тріумф",
    "tagline": "Години абсолютної лондонської тиші: зелений чай, ембієнт та проектування віртуальної клітини",
    "concept": "Лондон, друга година ночі. За великим вікном тихо спить місто. У кабінеті горить лише одна настільна лампа. 48-річний вчений сидить у зручному кріслі з чашкою зеленого чаю в навушниках. На його трьох моніторах мерехтять симуляції віртуальної живої клітини проекту Isomorphic Labs.",
    "why_it_works": "Відкриває інтимний щоденний ритуал мислителя: захищений нічний простір без зустрічей та дзвінків, де народжуються проривні ідеї наступного десятиліття.",
    "p1_start": "Moody cinematic wide shot of a modern private London penthouse study at 2 AM, large panoramic window showing rainy London night skyline, warm desk lamp illuminating a 48-year-old British-Cypriot scientist with short dark hair in headphones, steam from tea --ar 16:9",
    "p2_flow": "Slow tracking camera pushes past the tea mug towards the glowing multi-monitor workstation. The screens display an astonishing living simulation of an entire human biological cell, millions of organelles and molecular machines operating in real-time symphonic harmony, 24fps.",
    "p3_end": "Master documentary still: close-up profile of the visionary scientist looking into the soft monitor glow with quiet intellectual wonder, calm thoughtful smile, cinematic naturalistic lighting, shallow depth of field, 4k --ar 16:9",
    "davinci_recipe": "Color: Британський нічний інтер'єр: глибокий індиго за вікном, теплий золотистий тон лампи (2800K) на обличчі героя.",
    "sfx_cue": "Тихий звук нічного лондонського дощу за склом, дзвін порцелянової чашки чаю. У навушниках героя ледь чутно грає медитативний ембієнт Brian Eno."
  },
  {
    "id": 30,
    "num": "30",
    "name_ua": "Космічний телескоп життя: фінал",
    "name_en": "The Biological Singularity Telescope",
    "cat": "matrix",
    "cat_label": "🌐 Цифрова матриця",
    "cat_color": "cyan",
    "tc": "19:45 – 21:30",
    "act": "Акт 4 • Поліматичний розум і Нобелівський тріумф",
    "tagline": "Життя за допомогою створеного ним цифрового телескопа нарешті починає читати власний код",
    "concept": "Камера починається з одиночної шахової дошки на столі в Лондоні, де стоїть кінь. Потім камера піднімається крізь дах будинку, крізь лондонські хмари, виривається на навколоземну орбіту. Вся Земля огорнута золотою живою сіткою розшифрованого білкового та цифрового коду, що дихає в унісон із Всесвітом.",
    "why_it_works": "Філософський акорд усього епізоду: штучний інтелект як найвищий інструмент самопізнання природи — від шахів до безсмертя.",
    "p1_start": "Cinematic shot of a lone wooden chessboard on a table next to an open window in London at night, rain outside, the dark knight chess piece standing proud under moonlight --ar 16:9",
    "p2_flow": "Infinite continuous vertical camera ascent: rising through the room ceiling, soaring above illuminated rainy London landmarks (Big Ben, Tower Bridge), punching through dense purple storm clouds into the sublime silence of outer space above Earth, 24fps.",
    "p3_end": "Breathtaking IMAX orbital view of planet Earth floating in cosmic space, enmeshed in a luminous, shimmering golden neural-biological matrix connecting every living organism, city, and star, sublime poetic sci-fi finale, 8k 24fps --ar 16:9",
    "davinci_recipe": "Fusion: 3D Camera Flythrough з логарифмічним прискоренням. Фінальний плавний Fade to Black (48 кадрів) на останній ноті музики.",
    "sfx_cue": "Останнє сухе клацання шахового коня, що відлунює у вакуумі космосу. Потім — величний, пронизливий фінальний акорд віолончелі та абсолютна тиша."
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
  <title>30 Кінематографічних Тріад (Епізод 03: Деміс Гассабіс) • Google Flow Standard</title>
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
      background: rgba(11, 15, 23, 0.94);
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
      background: linear-gradient(135deg, var(--purple), var(--cyan));
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
    .btn-purple {{
      background: rgba(192, 132, 252, 0.15);
      border: 1px solid rgba(192, 132, 252, 0.45);
      color: var(--purple);
    }}
    .btn-purple:hover {{
      background: rgba(192, 132, 252, 0.25);
    }}

    /* Container */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 2rem 1.5rem;
    }}

    /* Hero Banner */
    .hero-banner {{
      background: radial-gradient(circle at top right, rgba(192, 132, 252, 0.15), transparent 45%),
                  radial-gradient(circle at bottom left, rgba(56, 189, 248, 0.1), transparent 45%),
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
      background: rgba(192, 132, 252, 0.16);
      border: 1px solid rgba(192, 132, 252, 0.45);
      color: var(--purple);
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
      max-width: 950px;
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
      background: var(--purple);
      color: #0b0f17;
      border-color: var(--purple);
      font-weight: 700;
    }}
    .search-input {{
      padding: 0.45rem 1rem;
      border-radius: 8px;
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--text-primary);
      font-size: 13px;
      width: 260px;
    }}
    .search-input:focus {{
      outline: none;
      border-color: var(--purple);
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
      border-color: rgba(192, 132, 252, 0.4);
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
      color: var(--purple);
      background: rgba(192, 132, 252, 0.12);
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
      border-left: 3px solid var(--purple);
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
      color: var(--purple);
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
      background: var(--purple);
      color: #0b0f17;
      border-color: var(--purple);
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
      background: var(--purple);
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
      <a href="cinematic_innovations.html" class="btn btn-outline">🎬 Тріади Еп. 01 (Альтман)</a>
      <a href="cinematic_innovations_ep02.html" class="btn btn-outline">🔥 Тріади Еп. 02 (Хуанг)</a>
      <a href="cinematic_innovations_ep03.html" class="btn btn-purple">♟️ 30 Тріад Еп. 03</a>
      <a href="50_scenes_hassabis.html" class="btn btn-outline" style="border-color:var(--rose);color:var(--rose);font-weight:700;">🎬 50 Сюжетів</a>
      <a href="episodes/ep01_altman.html" class="btn btn-outline">🎙️ Студія 01</a>
      <a href="episodes/ep02_huang.html" class="btn btn-outline">🎙️ Студія 02</a>
      <a href="episodes/ep03_hassabis.html" class="btn btn-outline">🎙️ Студія 03 (Гассабіс)</a>
    </div>
  </nav>

  <main class="container">
    <!-- Hero Section -->
    <section class="hero-banner">
      <span class="hero-badge">🛡️ 100% Policy-Safe • Zero Banned Keywords • Епізод 03</span>
      <h1 class="hero-title">30 Кінематографічних Тріад Епізоду 03 (Деміс Гассабіс)</h1>
      <p class="hero-desc">
        Повна 30-тріадна система генерації відео для <strong>Google Flow / Veo 2</strong>: від дитячих шахів 1980 року, коду ZX Spectrum та розробки ігор у Bullfrog Productions — до прориву в Кембриджі, нейронауки гіпокампа, історичного Ходу 37 проти Лі Седоля, розв'язання проблеми орігамі білка та Нобелівської премії 2024 року. Всі чутливі імена та бренди замінено на кінематографічні контекстні архетипи.
      </p>

      <div class="triad-explainer">
        <div class="expl-box" style="border-left: 3px solid var(--purple);">
          <div class="expl-tag" style="color:var(--purple);">1. ПРОМПТ 1: Start Image</div>
          <p class="expl-text">Генерує опорну точку кадру А (дерев'яний шаховий кінь, Amiga 500, гобан, готель Сеула або кристал білка). Завантажується у поле <strong>Start Image</strong>.</p>
        </div>
        <div class="expl-box" style="border-left: 3px solid var(--cyan);">
          <div class="expl-tag" style="color:var(--cyan);">2. ПРОМПТ 2: Video Morph Action</div>
          <p class="expl-text">Інструкція для Google Flow: описує фізику руху камери, розчинення пікселів у реальність, згортання білка, ударну хвилю Ходу 37 та поліматичні стрибки.</p>
        </div>
        <div class="expl-box" style="border-left: 3px solid var(--emerald);">
          <div class="expl-tag" style="color:var(--emerald);">3. ПРОМПТ 3: End Image</div>
          <p class="expl-text">Генерує цільову точку трансформації: 100% фотореалістичний кадр реального життя або наукова візуалізація 8k. Завантажується у <strong>End Image</strong>.</p>
        </div>
      </div>
    </section>

    <!-- Filter Bar -->
    <div class="filter-bar">
      <div class="filter-pills">
        <button class="filter-pill active" data-filter="all">Всі 30 тріад</button>
        <button class="filter-pill" data-filter="chess">♟️ Шахи & Інтелект</button>
        <button class="filter-pill" data-filter="gaming">🕹️ Геймінг & 90-ті</button>
        <button class="filter-pill" data-filter="neuro">🧠 Нейробіологія & fMRI</button>
        <button class="filter-pill" data-filter="bio">🧬 Молекулярне орігамі</button>
        <button class="filter-pill" data-filter="matrix">🌐 Матриця & Self-Play</button>
        <button class="filter-pill" data-filter="quantum">⚛️ Термояд & Фізика</button>
        <button class="filter-pill" data-filter="noir">🕵️ Нуар & Сеул</button>
        <button class="filter-pill" data-filter="optics">🔍 Оптичні трюки</button>
      </div>
      <input type="text" id="searchInput" class="search-input" placeholder="Пошук по 30 тріадах (напр. хід 37, білок, шахи)...">
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
        btn.style.background = "#c084fc";
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
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/07_DASHBOARD/cinematic_innovations_ep03.html",
        "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/docs/cinematic_innovations_ep03.html"
    ]
    for p in paths:
        with open(p, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"✓ Generated {p} ({len(html_content)} bytes)")
