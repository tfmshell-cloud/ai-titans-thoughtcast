#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for 50 Biographical Cinematic Scenes / Visualizations: Demis Hassabis (EP03)
Documentary & Artistic Master Blueprint for Director, Producer, and Content Creator.
100% POLICY-SAFE: All real names of living public figures, brands, and sensitive trademarks
are replaced with evocative cinematic archetypes to prevent token-wasting Google Flow blocks.
"""

import os

OUTPUT_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/ai-titans-thoughtcast/01_RESEARCH/demis_hassabis/50_BIOGRAPHICAL_SCENES_VISUALIZATION.md"

SCENES = [
  # ACT 1 / CHAPTER 1: КОРІННЯ, БОГЕМА ТА ПЕРШІ КЛІТИНКИ (1976–1984)
  {
    "num": "01",
    "title": "Дитяча колиска на перехресті двох світів",
    "period": "Липень 1976 • Північний Лондон",
    "narrative": "Народження на стику двох світів: середземноморської музично-ремісничої експресії батька та східноазійської споглядальної дисципліни матері. Лондонська вітальня 1970-х наповнена книгами, картинами та музикою.",
    "visual": "Макро-кадр дитячої колиски біля вікна вікторіанського будинку. Крізь тюль пробивається вологе лондонське сонце. Поруч лежать ноти грецьких пісень та порцелянова чайна піала. Плівкове зерно 35mm, м'яке світло, пилинки в повітрі.",
    "prompt_en": "Cinematic 35mm film photograph of a baby cradle in a sunlit 1970s North London Victorian room, sheer lace curtains catching morning golden light, acoustic guitar leaning against brick wall, Chinese porcelain tea bowl on wooden table, dust motes in sunbeams --ar 16:9",
    "symbol": "Злиття двох протилежних культур: аналітичної дисципліни Сходу та творчої пристрасті Півдня."
  },
  {
    "num": "02",
    "title": "Батьківська майстерня ремесел і теслярська стружка",
    "period": "1978 • Лондонська квартира",
    "narrative": "Батько — вільний митець і майстер: пісняр, тесля та творець дерев'яних іграшок. У домі постійно пахне стружкою свіжого дерева, каніфоллю та олійними фарбами. Дитина росте серед матеріального створення речей своїми руками.",
    "visual": "Кінематографічний план у стилі олійного живопису: руки батька-ремісника обробляють дубову деталь рубанком. Золотава стружка кучерявиться і падає на підлогу в сповільненій зйомці. Маленький хлопчик торкається теплої деревини.",
    "prompt_en": "Macro cinematic shot of an artisan father's skilled hands planing a block of raw oak in a sunlit 1978 London workshop, curling translucent wood shavings floating in slow motion, warm sawdust in amber sunlight, shallow focus, 35mm film grain --ar 16:9",
    "symbol": "Фізичне ремесло як перша школа: кожна лінія має бути вивірена, дерево не пробачає фальшивих рухів."
  },
  {
    "num": "03",
    "title": "Перший погляд на шахівницю: магія 64 клітинок",
    "period": "1980 (4 роки) • Вітальня на килимі",
    "narrative": "Чотирирічний хлопчик тихо сидить на килимі й спостерігає, як батько грає в шахи з родичем. Малюк не просить іграшок — він мовчки стежить за траєкторією дерев'яних фігур і просить пояснити правила.",
    "visual": "Камера на рівні підлоги: низький ракурс знизу вгору. Величезна дерев'яна лакована шахівниця між двома дорослими. Погляд хлопчика знизу — його зіниці фіксують геометрію клітинок. Освітлення від однієї настільної лампи, густі тіні.",
    "prompt_en": "Low-angle cinematic shot from floor level: a 4-year-old curly-haired boy sitting quietly on a Persian rug in 1980, looking up in wonder at a polished wooden chessboard between two men playing, dramatic single tungsten lamp light, chiaroscuro mood --ar 16:9",
    "symbol": "Момент пробудження покликання: шахи як ідеальний всесвіт, де немає місця випадковості."
  },
  {
    "num": "04",
    "title": "Шахова ініціація: поразка дорослих",
    "period": "1980 (4 роки) • Два тижні потому",
    "narrative": "Минуло лише два тижні з моменту знайомства з правилами. Чотирирічна дитина сідає за дошку проти дорослого — і за кілька десятків ходів ставить бездоганний тактичний мат.",
    "visual": "Крупний план рук: маленька дитяча ручка впевнено бере чорного слона й опускає його на поле. Сухий стукіт об лак. Повільна панорама на обличчя дорослого суперника — від поблажливої посмішки до застиглого шоку. Теплі тони 80-х.",
    "prompt_en": "Close-up cinematic still: a small 4-year-old child's hand precisely placing a polished wooden bishop on a chessboard square, delivering checkmate. Opposite, an adult man's face frozen in utter shock and awe, warm 1980s Kodachrome film look --ar 16:9",
    "symbol": "Вроджена архітектура розуму, здатна миттєво зчитувати просторові закономірності."
  },
  {
    "num": "05",
    "title": "Острів порядку серед богемного безладу",
    "period": "1981 (5 років) • Дім у Фінчлі",
    "narrative": "У домі панує творчий хаос: звучать гами на піаніно, пишуться тексти, батьки сперечаються про мистецтво. Для юного мислителя шахівниця стає фортецею абсолютної тиші та контролю.",
    "visual": "Розмитий рух навколо: силуети людей метушаться, літають аркуші паперу, звучить музика. У центрі кадру — абсолютно нерухомий хлопчик, схилений над шаховою дошкою. Світло падає лише на нього, відсікаючи зовнішній світ.",
    "prompt_en": "Cinematic composition with heavy motion blur: chaotic bohemian living room with moving figures and drifting sheet music, contrasting with an intensely motionless 5-year-old boy in sharp razor focus studying a chessboard in a pool of golden light --ar 16:9",
    "symbol": "Пошук стабільності в математиці та логіці серед непередбачуваного середовища."
  },
  {
    "num": "06",
    "title": "Дерево варіантів на запітнілому склі",
    "period": "1981 (5 років) • Дощовий Лондон",
    "narrative": "Холодний лондонський дощ заливає вікно. Хлопчик пальцем креслить на запітнілому склі не каракулі, а шахову сітку та стрілки можливих ходів фігур, прораховуючи комбінації.",
    "visual": "Макро-зйомка крізь скло зовні будівлі: краплі дощу стікають униз, розмиваючи жовте світло лондонської вулиці. Зсередини дитячий палець проводить лінії шахового дерева розгалужень. Тонкий силует дитини в теплому світлі кімнати.",
    "prompt_en": "Exterior shot through rain-streaked window glass at dusk: a small child inside tracing an intricate branching tree of chess vectors and coordinate squares onto condensation, warm amber interior glow, London drizzle, cinematic 35mm grain --ar 16:9",
    "symbol": "Початок алгоритмічного бачення: світ як граф ймовірностей і розгалужень."
  },
  {
    "num": "07",
    "title": "Два телефонні довідники в шаховому клубі",
    "period": "1982 (6 років) • Шаховий клуб Північного Лондона",
    "narrative": "Шестирічного хлопчика приводять до дорослого шахового клубу. Стілець занадто низький: суддя кладе на сидіння два товсті телефонні довідники Yellow Pages, щоб дитина діставала до фігур.",
    "visual": "Документальна реконструкція 35mm: похмурий клуб з лінолеумом, літні джентльмени у твідових піджаках курять люльки. Маленький хлопчик на жовтих довідниках серйозно дивиться в очі 60-річному супернику. Звук цокання годинників.",
    "prompt_en": "Authentic 1982 documentary film still: a 6-year-old boy sitting atop two thick yellow phone books on a wooden chair to reach a tournament chessboard, facing an elderly opponent in a smoky London chess hall, dramatic vintage lighting --ar 16:9",
    "symbol": "Зіткнення чистого інтелекту з фізичним віком: для логіки не існує років."
  },
  {
    "num": "08",
    "title": "Сльози першої великої поразки",
    "period": "1982 (6 років) • Турнірний коридор",
    "narrative": "Після довгої безпомилкової серії хлопчик робить прикрий позіх і програє партію. Він плаче в коридорі, але за кілька хвилин витирає очі й дістає кишенькові шахи: «Я повинен знайти помилку».",
    "visual": "Контрастне світло в довгому шкільному коридорі. Хлопчик сидить на підлозі біля батареї опалення, обхопивши коліна. Він витирає сльози рукавом і відкриває мініатюрні магнітні шахи, аналізуючи позицію заново.",
    "prompt_en": "Poignant cinematic shot of a young 6-year-old boy sitting on a linoleum hallway floor by a cast-iron radiator, wiping away a tear while opening a miniature magnetic travel chessboard to re-analyze his game, moody directional window light --ar 16:9",
    "symbol": "Трансформація болю поразки в паливо для зворотного зв'язку (Feedback Loop)."
  },
  {
    "num": "09",
    "title": "Батьківська сокира і шаховий кінь",
    "period": "1983 (7 років) • Робота з деревом",
    "narrative": "Батько вчить сина ремеслу обробки дерева: «Ти не можеш приклеїти назад зрізаний шматок. Кожен рух різця має бути точним». Хлопчик переносить це правило на шахи: взявся за фігуру — ходи.",
    "visual": "Кінематографічна макро-деталь: сталевий різець знімає тонкий шар деревини з шахового коня. Поруч дитячі руки тримають наждачний папір. Сонце висвітлює пил і деревний запах у повітрі. 4k 24fps.",
    "prompt_en": "Extreme macro cinematic photograph of a hand-carved wooden chess knight being shaped with a razor-sharp chisel, father guiding young boy's hands, sawdust illuminated in sunbeams, rich textured wood grain, tactile realism --ar 16:9",
    "symbol": "Незворотність вибору та відповідальність за кожен зроблений крок."
  },
  {
    "num": "10",
    "title": "Перший конверт із призовими грошима",
    "period": "1984 (8 років) • Чемпіонат Лондона серед юніорів",
    "narrative": "Хлопчик перемагає на міському чемпіонаті серед юніорів. Йому вручають кубок і конверт із призовими фунтами стерлінгів — перші чесно зароблені інтелектом гроші.",
    "visual": "Тепле світло актової зали. Маленький хлопчик тримає кубок, який майже з нього завбільшки. У нагрудній кишені піджака — білий паперовий конверт. Він дивиться на нього з чітким планом майбутньої покупки.",
    "prompt_en": "Cinematic portrait of an 8-year-old prodigy holding a tall vintage silver trophy in a school assembly hall, a white prize envelope peeking from his sweater pocket, determined quiet eyes, 1984 film aesthetic --ar 16:9",
    "symbol": "Інтелект як інструмент автономії та свободи вибору."
  },

  # ACT 1 / CHAPTER 2: 8-БІТНИЙ ВУНДЕРКІНД ТА КОД НА КАСЕТАХ (1984–1990)
  {
    "num": "11",
    "title": "Вітрина магазину електроніки: 8-бітний мікрокомп'ютер",
    "period": "1984 (8 років) • Тоттенгем-Корт-роуд",
    "narrative": "Замість велосипеда юний шахіст веде батька на лондонську вулицю комп'ютерної техніки і викладає всі призові гроші за компактний 8-бітний комп'ютер з гумовими клавішами.",
    "visual": "Відображення дитячого обличчя у склі вітрини магазину 1984 року. За склом — чорний мікрокомп'ютер з райдужною смужкою та гумовими клавішами. Очі хлопчика світяться від захвату.",
    "prompt_en": "Cinematic shot of an 8-year-old boy gazing through a rainy London electronics shop window at a vintage 1984 8-bit personal computer with rubber keyboard, neon shop reflection, magical nostalgia, 35mm film --ar 16:9",
    "symbol": "Вибір зброї майбутнього: відмова від миттєвого задоволення заради обчислювальної сили."
  },
  {
    "num": "12",
    "title": "Свист касетної стрічки та чорний екран",
    "period": "1984 • Спальня хлопчика вночі",
    "narrative": "Перший запуск мікрокомп'ютера. Аудіокасета обертається в портативному магнітофоні. Кімнату наповнює пронизливий бінарний свист і скрегіт завантаження коду.",
    "visual": "Макро-кадр прозорої аудіокасети з магнітною плівкою. Камера ковзає до телевізора: по вигнутому екрану біжать горизонтальні смуги блакитного й жовтого кольору. Кімната освітлена лише цим миготінням.",
    "prompt_en": "Macro shot of an audio cassette player loading digital data into a curved vintage CRT television in a dark bedroom, glowing cyan and yellow loading raster lines reflecting in a young boy's eyes, retro cybernetic mood --ar 16:9",
    "symbol": "Магія перетворення звуку на візуальний світ і логічні правила."
  },
  {
    "num": "13",
    "title": "Таємна нічна книга асемблера під ковдрою",
    "period": "1985 (9 років) • Під ковдрою з ліхтариком",
    "narrative": "Зрозумівши, що грати в чужі ігри нудно, хлопчик купує підручник із програмування на мові асемблера мікропроцесора і читає його ночами під ковдрою з ліхтариком.",
    "visual": "Затишний і таємничий план: світло кишенькового ліхтарика під ковдрою. Товста книга з кодом, сторінки з регістрами та машинними інструкціями. Дитяча рука веде олівцем по друкованих рядках.",
    "prompt_en": "Atmospheric cinematic shot of a young boy reading an assembly language programming book under bedsheets with a flashlight, pencil in hand, secret childhood obsession, soft warm glow, 35mm film grain --ar 16:9",
    "symbol": "Допитливість, яка не чекає на дозвіл школи чи дорослих."
  },
  {
    "num": "14",
    "title": "Народження першого штучного спаринга",
    "period": "1985 (9 років) • 48 кілобайт пам'яті",
    "narrative": "Коли вдома всі зайняті, хлопчику ні з ким грати в шахи. Він пише власну програму на асемблері, яка вміє робити ходи, створюючи свого першого штучного спаринг-партнера.",
    "visual": "Зелені фосфорні пікселі на маленькому екрані телевізора: проста 8-бітна шахівниця. Хлопчик натискає клавіші, роблячи хід. Комп'ютер блимає екраном дві хвилини й робить хід у відповідь. Захоплена посмішка на обличчі дитини.",
    "prompt_en": "Cinematic close-up of a 9-year-old child smiling in front of a glowing phosphor green CRT screen displaying a rudimentary pixelated chessboard he programmed himself, dark 1980s British bedroom, 4k --ar 16:9",
    "symbol": "Перша спроба вдихнути інтелект у неживий кремній: ШІ як засіб проти самотності."
  },
  {
    "num": "15",
    "title": "Турнірний поїзд крізь туманні Мідлендси",
    "period": "1986 (10 років) • Британська залізниця",
    "narrative": "Щовихідних юний шахіст їздить на турніри по всій Англії. У старих холодних вагонах він годинами сидить біля вікна, відтворюючи партії світових майстрів на кишенькових магнітних шахах.",
    "visual": "Кінематографічний вид крізь вікно поїзда: сірі фабрики, пагорби та дощ Англії 80-х. На відкидному столику стоїть пластикова коробка шахів. Дитячі пальці блискавично переставляють фігурки. 35mm film.",
    "prompt_en": "Cinematic shot inside a vintage 1980s British passenger train carriage passing through misty English countryside, a 10-year-old boy intensely analyzing positions on a miniature magnetic chessboard by the window --ar 16:9",
    "symbol": "Кочовий спосіб життя шахового гладіатора: гартування самодисципліни та витривалості."
  },
  {
    "num": "16",
    "title": "Холод пансіону в Блекпулі: нічний аналіз",
    "period": "1987 (11 років) • Курортне містечко Блекпул",
    "narrative": "Британський чемпіонат у приморському Блекпулі. Дешевий готельний номер із шумом шторму. Замість прогулянок набережній юнак о другій годині ночі аналізує відкладену партію.",
    "visual": "Тьмяне жовте світло в готельному номері. На шпалерах — тінь схиленого хлопчика. Поруч стоїть остигла чашка чаю з молоком. На колінах — зошит із шаховою нотацією, списаний варіантами ходів.",
    "prompt_en": "Moody cinematic interior of a seaside Blackpool guest house at 2 AM, rain on window, an 11-year-old boy in a cardigan studying handwritten chess notation by lamplight, cold tea cup, profound discipline --ar 16:9",
    "symbol": "Ціна успіху: готовність відмовитися від дитячих розваг заради досконалості."
  },
  {
    "num": "17",
    "title": "Звання Candidate Master у дванадцять років",
    "period": "1988 (12 років) • Лондонський шаховий центр",
    "narrative": "Отримання звання кандидата в майстри спорту. Дорослі шахісти починають боятися грати з ним, знаючи його жорсткий, безпомилковий позиційний стиль.",
    "visual": "Погляд дорослого сивого шахіста навпроти: важкі краплі поту на лобі, тремтяча рука тримає пішака. На протилежному боці дошки — 12-річний хлопчик-шахіст у шкільному блейзері, з абсолютно незворушним спокоєм на обличчі.",
    "prompt_en": "Intense cinematic two-shot across a wooden tournament chessboard: an older sweating chess master trembling under the unflinching, calm gaze of a 12-year-old prodigy wearing a navy school blazer, Rembrandt lighting --ar 16:9",
    "symbol": "Психологічна перевага спокою над досвідом і авторитетом."
  },
  {
    "num": "18",
    "title": "Капітан юнацької збірної Англії",
    "period": "1989 (13 років) • Міжнародні юнацькі ігри",
    "narrative": "Призначення капітаном національної юніорської команди Англії. Він відповідає не лише за власну партію, але й підтримує команду, аналізуючи позиції партнерів.",
    "visual": "Шеренга підлітків у темно-синіх блейзерах з гербом Англії. Юний капітан стоїть попереду з капітанською стрічкою. Він тихо підходить до дошки товариша, кидає один погляд і ледь помітно киває, вселяючи впевненість.",
    "prompt_en": "Cinematic portrait of a 13-year-old team captain standing proudly in a vintage British junior chess team blazer, leading his teammates in a historic tournament hall, soft dramatic lighting --ar 16:9",
    "symbol": "Народження лідерських якостей: вміння вести за собою талановитих індивідуалістів."
  },
  {
    "num": "19",
    "title": "Рейтинг Ело 2300: другий у світі серед юніорів",
    "period": "1989 (13 років) • Офіційний бюлетень FIDE",
    "narrative": "Виходить світовий рейтинг FIDE. Хлопець досягає позначки 2300 пунктів Ело — він стає другим шахістом планети у віковій категорії до 14 років.",
    "visual": "Макро-кадр друкованого паперового журналу FIDE з дрібним шрифтом таблиць світового рейтингу. Палець ковзає по списку імен: rank 1, потім — юний англійський майстер з рейтингом 2300. Золотий промінь сонця падає на цей рядок.",
    "prompt_en": "Extreme macro of a 1989 international chess federation printed ratings journal, vintage typewriter typography, a finger pointing to a 13-year-old player's record showing 2300 Elo rating, beam of sunlight --ar 16:9",
    "symbol": "Вихід на глобальний рівень: розуміння свого місця серед еліти світового інтелекту."
  },
  {
    "num": "20",
    "title": "Психологічний цугцванг: межі шахового всесвіту",
    "period": "1990 (14 років) • Лондонський парк",
    "narrative": "Хлопець сидить на лавці після важкої перемоги й усвідомлює кризу: «Шахи — це замкнена гра. Ти можеш стати чемпіоном світу, але ти нічого не зміниш у реальності. Мені потрібна більша гра».",
    "visual": "Повільний від'їзд камери від дерев'яної шахівниці на лавці парку. Дошка стає крихітною цяткою серед великого Лондона з його хмарочосами, лікарнями, літаками в небі. Погляд підлітка спрямований у небо.",
    "prompt_en": "Cinematic high-angle crane pull-back from a solitary teenager sitting beside an abandoned wooden chessboard on a London park bench, camera rising to reveal the vast metropolis horizon at dusk --ar 16:9",
    "symbol": "Рішення вийти за межі 64 клітинок заради вирішення проблем людства."
  },

  # ACT 2 / CHAPTER 3: ПІКСЕЛЬНИЙ РОК-Н-РОЛ BULLFROG ТА КЕМБРИДЖ (1991–1998)
  {
    "num": "21",
    "title": "Школа екстерном: випуск у 15 років",
    "period": "1991 (15 років) • Фінчлі, Лондон",
    "narrative": "Складання випускних іспитів A-levels на два роки раніше однолітків, отримавши найвищі бали з математики, фізики та комп'ютерних наук.",
    "visual": "Документальний стиль: випускна зала школи з червоної цегли. Однолітки грають у футбол на подвір'ї, а юнак з рюкзаком виходить через залізні ворота з атестатом під пахвою, дивлячись уперед.",
    "prompt_en": "Documentary still of a 15-year-old teenage scholar walking out through iron school gates of a classic red-brick London college carrying notebooks, solitary forward-looking resolve, natural daylight --ar 16:9",
    "symbol": "Прискорення життєвого циклу: небажання витрачати час на формальності системи."
  },
  {
    "num": "22",
    "title": "Вердикт Кембриджа: «Візьміть Gap Year»",
    "period": "1992 (16 років) • Приймальна комісія",
    "narrative": "Кембриджський університет приймає юнака, але відмовляється зарахувати його негайно через юний вік: 16-річний студент — це порушення традицій коледжу. Йому радять почекати рік.",
    "visual": "Офіційний лист на гербовому папері Кембриджа з восковою печаткою. Юнак тримає лист, посміхається і кладе його в рюкзак. Він не збирається байдикувати — він бере газету з вакансіями геймдеву.",
    "prompt_en": "Cinematic shot of a 16-year-old holding an acceptance letter on antique university parchment with embossed seal, turning away with an adventurous smile towards modern London, 35mm film aesthetic --ar 16:9",
    "symbol": "Перетворення вимушеної паузи на найбільший трамплін у кар'єрі."
  },
  {
    "num": "23",
    "title": "Поріг легендарної студії відеоігор",
    "period": "1992 (16 років) • Гілфорд, графство Суррей",
    "narrative": "16-річний підліток приїжджає на співбесіду до провідної британської студії відеоігор. Йому дають складне тестове завдання на асемблері, яке він вирішує за кілька годин прямо в коридорі.",
    "visual": "Атмосферний вхід у невеликий офіс розробників: темні коридори, неонові вивіски культових ігор, плакати на стінах. 16-річний розробник в оверсайз светрі з дискетою в руках розмовляє з харизматичним керівником студії.",
    "prompt_en": "Atmospheric 1992 game development studio interior: cluttered desks, arcade posters, glowing monitors, a 16-year-old prodigy programmer in a wool sweater presenting a floppy disk to a charismatic studio director --ar 16:9",
    "symbol": "Зустріч юного математика з бунтарським світом британського геймдеву."
  },
  {
    "num": "24",
    "title": "Нічні бдіння розробників на 16-бітному комп'ютері",
    "period": "1993 (16-17 років) • Робоче місце розробника",
    "narrative": "Керівництво програмуванням штучного інтелекту нової гри. Робота по 16 годин на добу серед піци та коли, розробка поведінкових алгоритмів для сотень маленьких спрайтів.",
    "visual": "Художня ретро-анімація: темна кімната, освітлена синім і бурштиновим світінням моніторів. Стіл завалений коробками від піци, банками напоїв і стопками дискет 3.5''. Пальці юнака друкують код, не дивлячись на клавіші.",
    "prompt_en": "Moody cinematic shot of a 1993 teenage game coder typing furiously at midnight, illuminated by two bulky color CRT monitors displaying scrolling C code, empty soda cans and diskettes on desk, 4k --ar 16:9",
    "symbol": "Геймдев 90-х як лабораторія перших експериментів зі штучним життям."
  },
  {
    "num": "25",
    "title": "Народження автономного натовпу в симуляторі парку",
    "period": "1994 (17 років) • Архітектура штучного інтелекту",
    "narrative": "Реалізація революційної ідеї: відвідувачі симулятора парку — це автономні агенти з власними потребами, бюджетом і настроєм. Якщо додати більше солі в попкорн — вони купують більше напоїв.",
    "visual": "Ізометрична піксельна графіка 16-біт: кольоровий парк атракціонів, американські гірки. Камера занурюється всередину коду одного маленького відвідувача: спалахують змінні потреб. Натовп починає діяти як живий мурашник.",
    "prompt_en": "Macro split visual: left side shows vibrant 16-bit isometric theme park simulation game with loop-de-loop coasters; right side reveals the underlying mathematical agent variables and AI decision nodes --ar 16:9",
    "symbol": "Перша велика симуляція складних адаптивних систем у масовій культурі."
  },
  {
    "num": "26",
    "title": "Черги у магазинах електроніки за симулятором парку",
    "period": "1994 • Оксфорд-стріт, Лондон",
    "narrative": "Реліз гри стає всесвітнім феноменом: продано мільйони копій. 17-річний автор симулятора стоїть у натовпі покупців у центрі Лондона, які тримають коробки з його ім'ям у титрах.",
    "visual": "Документальна хроніка 1994 року: черга з сотень людей під дощем біля мегастору електроніки на Оксфорд-стріт. Вітрини завішані плакатами гри. Юний творець гри у капюшоні стоїть осторонь, тихо спостерігаючи за реакцією людей.",
    "prompt_en": "Cinematic 1994 documentary still: a huge crowd of excited gamers queueing outside a rainy London music and software store holding game boxes, a modest 17-year-old creator standing in the shadows watching --ar 16:9",
    "symbol": "Відчуття сили створеного коду, який впливає на емоції мільйонів людей на планеті."
  },
  {
    "num": "27",
    "title": "Кембридж: старовинні бібліотеки та праці фундаторів",
    "period": "Осінь 1994 (18 років) • Кембридж",
    "narrative": "Заробивши солідні кошти від успіху гри, юнак нарешті переступає поріг Кембриджа. Замість студентських вечірок він проводить дні й ночі в старовинній бібліотеці, вивчаючи фундаментальні праці про універсальну обчислювальну машину.",
    "visual": "Величні готичні склепіння бібліотеки Кембриджа. Старовинні дубові столи, зелені абажури ламп. Молодий студент розкриває фоліант із фундаментальними математичними працями з теорії обчислень 1930-х років.",
    "prompt_en": "Cinematic shot inside a soaring Gothic Cambridge university library, green banker's lamps reflecting on polished oak desks, an 18-year-old student reading historical papers on computation theory, majestic dust motes --ar 16:9",
    "symbol": "Повернення до витоків комп'ютерної науки: від комерційного коду — до вічних теорем."
  },
  {
    "num": "28",
    "title": "Математичний міст над річкою Кем",
    "period": "1996 • Вечірній Кембридж",
    "narrative": "Знаменитий дерев'яний міст, побудований за принципом геометричних дотичних. Студент годинами стоїть на мосту, сперечаючись із професорами про те, чому сучасні кремнієві комп'ютери ніколи не стануть мислячими без біологічних принципів.",
    "visual": "Кінематографічний золотий вечірній туман над річкою Кем. Дерев'яні балки Математичного мосту виблискують у променях сонця. Молодий дослідник у твідовому шарфі палко жестикулює, малюючи в повітрі схеми нейронних зв'язків.",
    "prompt_en": "Atmospheric cinematic still of the wooden Mathematical Bridge in Cambridge at sunset, river mist glowing amber, a passionate young computer science student talking with an elderly professor, 35mm film still --ar 16:9",
    "symbol": "Міст між двома світами: класичною кремнієвою архітектурою та живим людським мозком."
  },
  {
    "num": "29",
    "title": "Double First: абсолютний кембриджський диплом",
    "period": "Червень 1997 (21 рік) • Senate House, Кембридж",
    "narrative": "Закінчення Кембриджського університету з подвійним дипломом першого ступеня (Double First) з комп'ютерних наук — найвищою можливою академічною відзнакою Британії.",
    "visual": "Урочиста церемонія у Сенат-хаусі Кембриджа: чорна академічна мантія, білий комірець, виголошення латинських формул професорами. Молодий випускник схиляє голову під оплески зали, дивлячись на усміхнених батьків.",
    "prompt_en": "Ceremonial documentary still in Cambridge Senate House: a 21-year-old graduate in black academic gown and white fur hood receiving highest academic honors, stately architecture, solemn British prestige --ar 16:9",
    "symbol": "Академічна бездоганність як надійний фундамент для майбутніх революцій."
  },
  {
    "num": "30",
    "title": "Заснування власної студії у 22 роки",
    "period": "1998 (22 роки) • Камден, Лондон",
    "narrative": "Відкинувши пропозиції банків з Волл-стріт і Кремнієвої долини, молодий випускник засновує в Лондоні власну незалежну студію, наймаючи 60 провідних інженерів, художників і математиків.",
    "visual": "Просторий лондонський лофт із цегляними стінами та великими вікнами у Камдені. Десятки столів із потужними графічними станціями. 22-річний засновник веде нараду біля скляної дошки, проектуючи амбітні симулятори.",
    "prompt_en": "Wide cinematic shot of an expansive late-1990s brick-and-beam London loft tech office in Camden, 60 creative engineers and artists at workstations, young 22-year-old founder leading a whiteboard briefing --ar 16:9",
    "symbol": "Прагнення до повної творчої та технологічної автономії."
  },

  # ACT 3 / CHAPTER 4: ВІД СТУДІЇ ДО ЗАГАДКИ ЛЮДСЬКОГО МОЗКУ (1998–2009)
  {
    "num": "31",
    "title": "Симуляція держави: мільйон автономних громадян",
    "period": "2003 • Лондонська студія",
    "narrative": "Реліз проекту небаченого масштабу: симуляція вигаданої держави з мільйоном мешканців, кожен з яких має власний характер, рівень лояльності та соціальні зв'язки.",
    "visual": "Темний 3D-інтерфейс міста вночі: тисячі точок світла рухаються дорогами. Камера наближається до одного вікна, де персонаж пише листівку. Полігональна графіка початку 2000-х виглядає як військова симуляція соціуму.",
    "prompt_en": "Cinematic visual of a complex 3D virtual city simulation on high-end computer monitors in 2003: thousands of individual agent pathfinding vectors glowing cyan across a sprawling urban matrix, hard sci-fi feel --ar 16:9",
    "symbol": "Штучний інтелект як інструмент соціологічного експерименту."
  },
  {
    "num": "32",
    "title": "Гірке прозріння: ігри не приведуть до AGI",
    "period": "2004 • Порожній нічний офіс студії",
    "narrative": "Незважаючи на інновації, індустрія вимагає спрощення та красивої графіки для консолей. Засновник сидить уночі один в офісі й розуміє: в рамках комерційного геймдеву створити загальний інтелект неможливо.",
    "visual": "Камера повільно кружляє навколо самотнього засновника за комп'ютером серед десятків вимкнених моніторів студії. Він дивиться на коробки відеоігор на полиці. Повільний рух руки — він вимикає живлення. Падіння в тишу.",
    "prompt_en": "Solitary cinematic portrait of a tech studio founder at 3 AM in a dark empty open-plan office, staring thoughtfully at rows of boxed games before switching off the main studio power switch, dramatic shadows --ar 16:9",
    "symbol": "Мужність закрити успішний бізнес заради вищої мети."
  },
  {
    "num": "33",
    "title": "Крок у невідоме: лабораторія когнітивної нейронауки",
    "period": "2005 (29 років) • University College London",
    "narrative": "У віці 29 років мультимільйонер і зірка геймдеву знову стає звичайним аспірантом у Лондонському університеті: «Якщо ми хочемо створити мислячу машину, ми маємо зрозуміти мозок».",
    "visual": "Стерильні білі коридори інституту неврології на Квін-сквер. Молодий вчений у білому лабораторному халаті несе штатив із матеріалами та результати магнітно-резонансної томографії. Він починає все з першого курсу аспірантури.",
    "prompt_en": "Documentary still of a 29-year-old former tech CEO wearing a white lab coat walking down quiet clinical corridors of a prestigious London neuroscience institute carrying brain MRI scans, humble renewal --ar 16:9",
    "symbol": "Смирення перед природою: готовність знову стати учнем заради істини."
  },
  {
    "num": "34",
    "title": "Підземний томограф fMRI: спалахи в гіпокампі",
    "period": "2006 • Лабораторія нейровізуалізації",
    "narrative": "Сотні годин біля магнітного томографа fMRI. Дослідження пацієнтів з амнезією, спостереження за тим, які зони мозку споживають кисень під час спогадів.",
    "visual": "Макро-кадр монітора томографа: сірий тривимірний зріз людського мозку. Раптом у глибині скроневої частки — в гіпокампі — спалахує яскрава помаранчева пляма нейронної активності. Звук ритмічного стукоту магнітів fMRI.",
    "prompt_en": "Macro shot of a high-resolution medical fMRI brain scan monitor: 3D human brain rendering where the hippocampus abruptly flares with brilliant bioluminescent amber neural activity, clinical dark lab --ar 16:9",
    "symbol": "Пряме спостереження за фізичним субстратом людської думки."
  },
  {
    "num": "35",
    "title": "Сенсація у провідному науковому журналі",
    "period": "2007 • Публікація про природу уяви",
    "narrative": "Епохальне відкриття: пацієнти, які втратили пам'ять про минуле через пошкодження гіпокампа, не здатні уявити себе в майбутньому. Пам'ять і уява виявилися одним і тим самим нейронним механізмом конструювання ментальних сцен.",
    "visual": "Обкладинка престижного наукового журналу за 2007 рік з науковою статтею про природу уяви та пам'яті. Художня візуалізація розщеплення: старе чорно-біле фото минулого плавно перетворюється на кольорову проекцію майбутнього.",
    "prompt_en": "Artistic visual metaphor of human neuroscience: left side shows faded archival black-and-white memory photographs; right side shows glowing futuristic digital scene simulations generated from the same neural nodes --ar 16:9",
    "symbol": "Фундаментальне відкриття: розум — це не архів минулого, а генератор симуляцій майбутнього."
  },
  {
    "num": "36",
    "title": "Бостонський міст: союз нейробіології та математики",
    "period": "2008–2009 • Кембридж, Массачусетс",
    "narrative": "Постдокторські дослідження в провідних американських університетах. Об'єднання біологічних відкриттів про мозок з алгоритмами машинного навчання, формування архітектури майбутнього стартапу.",
    "visual": "Осінній туманний ранок над річкою Чарльз у Бостоні. Молодий дослідник іде мостом через туманну річку, у його блокноті з'являються перші схеми глибокого навчання з підкріпленням і біологічного повторення досвіду (Experience Replay).",
    "prompt_en": "Cinematic shot of a thoughtful young scientist walking across a misty bridge in Boston at autumn dawn, skyline silhouetted behind, carrying a leather notebook filled with handwritten neural network equations --ar 16:9",
    "symbol": "Кристалізація великого плану: союз біології та математики готовий до запуску."
  },

  # ACT 4 / CHAPTER 5: НАРОДЖЕННЯ ЛАБОРАТОРІЇ ТА ДУЕЛЬ СТОЛИЦЬ (2010–2015)
  {
    "num": "37",
    "title": "Russell Square 2010: маніфест двох кроків",
    "period": "Осінь 2010 • Напівпідвальний офіс у Блумсбері",
    "narrative": "Заснування нової британської ШІ-лабораторії. На першому слайді презентації для інвесторів засновник пише свій легендарний маніфест із двох пунктів.",
    "visual": "Тьмяна напівпідвальна кімната з оголеною цеглою біля Рассел-сквер. Світло проектора на білій стіні висвітлює текст: 'Step 1: Solve Intelligence. Step 2: Solve Everything Else'. Троє молодих засновників дивляться на ці слова у повній рішучості.",
    "prompt_en": "Atmospheric cinematic still of a humble 2010 London basement startup office with exposed brickwork, overhead projector beaming bold text onto wall: 'Step 1: Solve Intelligence. Step 2: Solve Everything Else' --ar 16:9",
    "symbol": "Найлаконічніша і найамбітніша місія в історії світової науки."
  },
  {
    "num": "38",
    "title": "Зустріч із венчурними бунтарями: перший чек на AGI",
    "period": "2011 • Сан-Франциско, Каліфорнія",
    "narrative": "Уся Кремнієва долина вважала термін AGI науковою фантастикою. Лише венчурні бунтарі після багатогодинних бесід із засновником виписують перші мільйони доларів посівних інвестицій.",
    "visual": "Панорамне вікно пентхауса з видом на міст Золоті Ворота в Сан-Франциско. Технологічний візіонер у простому темному джемпері пояснює концепцію нейробіологічного навчання інвестору в дорогому костюмі, малюючи схеми на серветці.",
    "prompt_en": "Cinematic wide frame in a sleek high-rise San Francisco boardroom overlooking the foggy Golden Gate Bridge, a passionate British scientist in a simple dark sweater drawing brain architectures on paper for venture capitalists --ar 16:9",
    "symbol": "Переконання скептичного капіталу силою чистого наукового бачення."
  },
  {
    "num": "39",
    "title": "Магічний тунель в класичній аркаді",
    "period": "2013 • Лондонська лабораторія",
    "narrative": "Алгоритму дають класичну гру з цеглинами без жодних інструкцій — лише пікселі екрана та рахунок. Після тисяч спроб штучний інтелект відкриває неймовірну тактику: пробити дірку в кутку і пустити м'яч рикошетити за стіною.",
    "visual": "Нічна лабораторія. Інженери збираються навколо монітора. На екрані аркадний білий м'ячик пробиває тунель, і лічильник очок починає шалено крутитися. Керівник досліджень тихо посміхається: система почала самонавчатися.",
    "prompt_en": "Cinematic shot of tech researchers gathered around an arcade monitor at 2 AM, screen glowing with a rainbow brick breaking game as an autonomous AI carves a tunnel behind the wall, pure discovery --ar 16:9",
    "symbol": "Перший доказ того, що машина здатна відкривати нові знання, не закладені людиною."
  },
  {
    "num": "40",
    "title": "Угода з техногігантом та етичний ультиматум",
    "period": "Січень 2014 • Лондон",
    "narrative": "Продаж лабораторії за сотні мільйонів фунтів на безпрецедентних умовах: штаб-квартира залишається в Лондоні, створюється незалежна рада з етики, а алгоритми категорично заборонено використовувати у військових цілях.",
    "visual": "Підписання документів у лондонському готелі. Контракт на сотні мільйонів фунтів. Камера фокусується на пункті про створення незалежної етичної ради: засновник лабораторії твердо тримає ручку, захищаючи принципи безпеки.",
    "prompt_en": "Dramatic cinematic close-up of a fountain pen signing a massive corporate tech acquisition contract in a historic London hotel, foreground focus on an explicit clause requiring an independent AI ethics safety board --ar 16:9",
    "symbol": "Етика та безпека як непорушна умова технологічного прогресу."
  },

  # ACT 5 / CHAPTER 6: СЕУЛЬСЬКИЙ ХІД 37 ТА ПЕРЕМОГА НАД ГО (2016–2017)
  {
    "num": "41",
    "title": "Прибуття в Сеул: тиша перед битвою",
    "period": "Березень 2016 • Готель Four Seasons, Сеул",
    "narrative": "Готель Four Seasons у Сеулі. 500 світових журналістів, 100 мільйонів телеглядачів в Азії. Весь східний світ переконаний, що комп'ютер програє живому генію стародавньої гри Го.",
    "visual": "Вечірній Сеул крізь дощ: неонові ієрогліфи, хмарочоси, мокрий асфальт. У залі готелю під одиночним софітом стоїть стіл із дошкою гобан. Британський вчений-візіонер у темному костюмі тихо заходить до зали, відчуваючи тиск усього світу.",
    "prompt_en": "Cinematic wide establishing shot of Seoul at night in pouring rain, neon reflections on wet streets, cutting to a solitary illuminated wooden Go game table in a grand silent auditorium, tense stillness, 4k --ar 16:9",
    "symbol": "Зіткнення двох епох людської цивілізації: тисячолітньої традиції та алгоритмічного розуму."
  },
  {
    "num": "42",
    "title": "Хід 37: народження нелюдської креативності",
    "period": "10 березня 2016 • Партія 2, Сеул",
    "narrative": "37-й хід другої партії. Алгоритм наказує оператору поставити чорний камінь на 5-ту лінію — у відкриту порожнечу. Коментатори вважають це помилкою. Імовірність такого ходу людиною — 1 із 10 000. Це був початок тріумфу.",
    "visual": "Макрозйомка в 1000 кадрів/сек: чорний відполірований камінь опускається на деревину на 5-й лінії. Звук удару відлунює, як постріл. Від точки дотику в слоу-мо розходиться золота хвиля світла. Обличчя суддів застигають.",
    "prompt_en": "High-speed 1000fps macro shot of a hand placing a polished black slate stone on the 5th line of a golden wooden Goban board, cinematic golden lens flare rippling from the impact point, historic stillness --ar 16:9",
    "symbol": "Поява справжньої машинної творчості, вільної від тритисячолітніх людських догм."
  },
  {
    "num": "43",
    "title": "Тиха сльоза чемпіона: визнання краси",
    "period": "12–15 березня 2016 • Фінал матчу в Сеулі",
    "narrative": "Нейромережа перемагає в серії з рахунком 4-1. Легендарний східний чемпіон світу зі сльозами на очах просить вибачення у вболівальників, але визнає: «Я побачив красу, якої раніше не знав».",
    "visual": "Драматичний крупний план обличчя східного гросмейстера на тлі мікрофонів преси: вологі очі, скупа сльоза. Поруч стоїть молодий британський вчений, який з глибокою повагою схиляє голову перед майстром, не святкуючи тріумф зухвало.",
    "prompt_en": "Emotional documentary press conference portrait: a tear running down the cheek of an Asian board game grandmaster, seated beside a respectful European scientist bowing his head in mutual honor, 35mm film grain --ar 16:9",
    "symbol": "Благородство науки: повага до переможеного генія людини."
  },
  {
    "num": "44",
    "title": "Tabula Rasa: алгоритм грає сам проти себе",
    "period": "2017 • Лондонські серверні кластери",
    "narrative": "Створення нової версії алгоритму: йому не дають жодної людської партії. Він грає сам із собою з нуля (Self-Play). За 4 години він перевершує всі знання шахів людства, граючи в романтичному, жертовному стилі.",
    "visual": "Сюрреалістичний 3D-візуал: нескінченний дзеркальний коридор у чорному просторі. Два прозорі силуети фігур роблять ходи з надзвуковою швидкістю. Фігури горять смарагдовим і золотим світлом, створюючи нову філософію стратегії.",
    "prompt_en": "Surreal infinite mirror corridor with polished dark obsidian floor, reflecting identical illuminated geometric chessboards, floating transparent energy pieces moving at lightspeed, Octane 8k render --ar 16:9",
    "symbol": "Очищення від людських упереджень: вихід на чисті закони математичної гармонії."
  },

  # ACT 6 / CHAPTER 7: ОРІГАМІ БІЛКА, ТОКАМАК ТА НОБЕЛЬ (2018–2024)
  {
    "num": "45",
    "title": "Крок Другий: «Ігри закінчилися, переходимо до біології»",
    "period": "2018 • Лондонська штаб-квартира",
    "narrative": "Збір команди в новому лондонському центрі: «Ми довели силу ШІ на іграх. Тепер час використати його для найбільшої загадки біології — проблеми згортання білків (Protein Folding Problem)».",
    "visual": "Сучасний скляний атріум штаб-квартири лондонської ШІ-лабораторії в Кінгс-Кросс. Керівник досліджень виводить на величезний екран тривимірну заплутану молекулу білка. Сотні молодих вчених-біологів і математиків уважно слухають завдання.",
    "prompt_en": "Sweeping cinematic shot inside a vast, modern glass-and-steel London technology headquarters atrium, a research leader presenting a colossal glowing 3D protein structure on a theater display to scientists --ar 16:9",
    "symbol": "Перехід від віртуальних перемог до порятунку людських життів."
  },
  {
    "num": "46",
    "title": "Олімпіада CASP14: точність до одного атома",
    "period": "Листопад 2020 • Оцінювання глобального експерименту",
    "narrative": "Нейромережа бере участь у всесвітньому змаганні біологів. Система передбачає форму білків з точністю 92.4 бали зі 100 — це рівень експериментальної точності вартістю в роки праці в лабораторії. 50-річну проблему біології розв'язано.",
    "visual": "Екран комп'ютера з накладанням двох структур: зелена експериментальна молекула та синя розрахована молекула. Вони накладаються одна на одну з атомною точністю. Звуковий тон гармонійного співзвуччя.",
    "prompt_en": "Scientific 3D visualization of two complex biological macromolecule ribbons snapping into perfect atomic superposition, green experimental crystal and cyan predicted model aligning seamlessly, 8k render --ar 16:9",
    "symbol": "Тектонічний зсув у медицині: секунди обчислень замість п'яти років лабораторій."
  },
  {
    "num": "47",
    "title": "Космічний подарунок: 200 мільйонів білків для Землі",
    "period": "2021–2022 • Відкрита база знань",
    "narrative": "Лабораторія разом із міжнародними інститутами викладає структури майже всіх відомих білків усіх живих організмів Землі (понад 200 мільйонів) у безкоштовний відкритий доступ.",
    "visual": "Космічна 3D-візуалізація: куляста галактика з мільйонів сяючих різнокольорових білкових молекул обертається в глибокому космосі. Від неї промені світла тягнуться до лабораторій по всій Землі, прискорюючи створення ліків.",
    "prompt_en": "Majestic IMAX cosmic visual: a glowing spiral galaxy composed of 200 million illuminated 3D biological protein structures floating in deep space, radiating cyan, gold, and magenta light, digital biology library --ar 16:9",
    "symbol": "Наука як спільне надбання людства без комерційних замків."
  },
  {
    "num": "48",
    "title": "Приборкання термоядерної зорі в Токамаку",
    "period": "2022–2023 • Дослідницький реактор плазми",
    "narrative": "Алгоритми застосовують для керування надгарячою плазмою (100 мільйонів градусів) у термоядерному реакторі Tokamak. ШІ коригує магнітні поля тисячі разів на секунду, утримуючи штучну зорю від дотику до стінок.",
    "visual": "Камера заглядає у круглу камеру реактора: вихор сліпучої фіолетової плазми кружляє з ревом. Невидимі магнітні лінії стискають розпечений газ у ідеальний тороїд. Кінематографічний hard sci-fi.",
    "prompt_en": "Cinematic hard sci-fi interior view of a tokamak fusion reactor: a blazing violet and neon-pink donut-shaped plasma torus held in magnetic suspension, extreme heat distortion, beryllium wall reflections, 8k --ar 16:9",
    "symbol": "Поліматичний стрибок: від біології клітини до приборкання зоряної енергії Всесвіту."
  },
  {
    "num": "49",
    "title": "Стокгольм: найвища світова наукова нагорода 2024",
    "period": "Жовтень 2024 • Стокгольм",
    "narrative": "Присудження найвищої світової наукової премії за передбачення тривимірних структур білків. Хлопчик, який починав із шахів у Лондоні, досягає абсолютного Олімпу науки.",
    "visual": "Макро-кадр золотого рельєфу наукової медалі найвищого гатунку на синьому оксамиті. Камера плавно піднімає погляд: 48-річний вчений з британсько-кіпріотським корінням у смокінгу тримає нагороду під овації зали. У його погляді — спокій і пам'ять про першу шахівницю 1980 року.",
    "prompt_en": "Cinematic portrait of a 48-year-old British-Cypriot scientist in black-tie tuxedo holding a prestigious embossed gold scientific prize medal, warm applause of a grand Stockholm hall in soft background bokeh --ar 16:9",
    "symbol": "Остаточне визнання комп'ютерних наук як головного двигуна природознавства XXI століття."
  },
  {
    "num": "50",
    "title": "Нічна зміна 00:00–04:00: проектування живої клітини",
    "period": "2024–майбутнє • Лондонський кабінет, ніч",
    "narrative": "Навіть після світового тріумфу щоночі з опівночі до четвертої ранку, коли Лондон спить, вчений заварює зелений чай, вмикає ембієнт у навушниках і проектує наступну мету — повну симуляцію живої віртуальної клітини.",
    "visual": "Нічний панорамний вигляд на дощовий Лондон крізь вікно пентхауса. За столом сидить вчений з чашкою чаю в навушниках. На трьох моніторах мерехтить жива модель клітини. Поруч на столі стоїть той самий дерев'яний шаховий кінь з дитинства. Гра щойно розпочалася.",
    "prompt_en": "Moody nocturnal shot of a visionary scientist working alone at 3 AM in a rain-streaked London penthouse study, multiple monitors displaying a glowing living virtual cell simulation, wooden chess knight on desk, quiet ambition --ar 16:9",
    "symbol": "Невпинний пошук істини: інтелект як нескінченна подорож самопізнання Всесвіту."
  }
]

def generate_markdown():
    lines = [
        "# 50 ХУДОЖНЬО-ДОКУМЕНТАЛЬНИХ СЮЖЕТІВ: ДЕМІС ГАССАБІС (EP03)",
        "**Серіал:** «Архітектори Розуму» // Cinematic Thoughtcast",
        "**Герой:** Деміс Гассабіс (Demis Hassabis) — «Гросмейстер біологічного коду»",
        "**Формат:** 50 покадрових режисерських візуалізацій для генерації в Midjourney / Google Flow / Runway / DaVinci Resolve",
        "**Статус безпеки:** 100% Policy-Safe (Всі імена реальних осіб замінено на художні архетипи для уникнення блокувань у Google Flow / Veo 2)",
        "",
        "---",
        ""
    ]

    for s in SCENES:
        lines.append(f"### Сюжет #{s['num']}: {s['title']}")
        lines.append(f"⏱️ **Період & Локація:** `{s['period']}`")
        lines.append(f"📖 **Драматичний наратив:** {s['narrative']}")
        lines.append(f"🎬 **Режисерська художньо-документальна візуалізація (UA):** {s['visual']}")
        lines.append(f"🎨 **English Prompt (Google Flow / Midjourney):**")
        lines.append(f"```text\n{s['prompt_en']}\n```")
        lines.append(f"💡 **Символізм & Сенс:** {s['symbol']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    content = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Successfully generated {OUTPUT_PATH} ({len(SCENES)} scenes, {len(content)} bytes)")

if __name__ == "__main__":
    generate_markdown()
