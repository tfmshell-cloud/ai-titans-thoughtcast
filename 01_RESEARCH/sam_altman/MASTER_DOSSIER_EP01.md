# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 01 — СЕМ АЛЬТМАН
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Анатомія експоненти»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP01 (Сем Альтман) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP01.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP01_VO_, EP01_MUS_, EP01_AMB_, EP01_SFX_, EP01_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 12 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1390 слів, хронометраж 20:30 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 12 українських файлів EP01_VO_UA_01..12.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP01_VO_EN_01..12.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP01_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP01_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP01_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP01_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP01_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
- [ ] Викласти диктора VO_UA на доріжку A1, музику MUS 92 BPM на A2, ембієнт AMB на A3, SFX-переходи на A4.
- [ ] Розставити 100 відеокліпів V1/V2 згідно з таймкодами сторіборду та додати мінімалістичні титри ключових цитат (SF Pro / Inter Tracking +80).

### Етап 06. Fairlight Зведення & Колористика — Налаштування Sidechain Ducking -3.2 dB та 4-нодної плівкової градації Kodak 2383
*Ціль:* Досягти фірмового оксамитового кінозвучання та єдиного візуального стилю серіалу без перевантажень.
- [ ] У Fairlight направити Send з A1 (VO) на Bus 1 (Key), а на компресорі A2 (MUS) увімкнути Sidechain Listen: Ducking -3.2 dB (Attack 15ms, Hold 250ms, Release 350ms).
- [ ] На вкладці Color застосувати 4-Node PowerGrade: Node 1 (CST) -> Node 2 (Contrast & WB) -> Node 3 (Kodak 2383 D60 Print LUT) -> Node 4 (OFX 35mm Grain 0.35).
- [ ] Перевірити читабельність субтитрів/цитат та плавність 4-секундного Fade to Black у фіналі 4 Акту.

### Етап 07. Майстеринг та YouTube Multi-Audio — Фінальний рендер -14 LUFS та публікація двомовного випуску
*Ціль:* Експортувати бездоганний 4K майстер-файл та окремий англомовний мікс для глобальної дистрибуції.
- [ ] Перевірити Loudness Meter на Master Bus: рівно -14.0 LUFS Integrated, True Peak не вище -1.0 dBTP.
- [ ] Експортувати основний майстер EP01_sam_altman_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP01_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP01_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження:** 22 квітня 1985 р., Чикаго, виріс у Сент-Луїсі (Міссурі). Батько — брокер із нерухомості, мати — дерматолог.
* **Дитинство:** У 8 років отримав Apple Macintosh LC II, самостійно розбирав залізо та вивчав код. У 16 років зробив публічний камінг-аут у християнській школі John Burroughs School.
* **Стенфорд та Loopt:** У 2003 р. вступив на комп'ютерні науки. У 2005 р. кинув навчання задля стартапу Loopt (перший набір Y Combinator S05). У 2012 р. продано Green Dot за $43.4 млн.
* **Y Combinator та OpenAI:** З 2014 р. — президент Y Combinator. У грудні 2015 р. співзасновник OpenAI. У 2019 р. очолив компанію як CEO, здійснив реструктуризацію у capped-profit і залучив $1 млрд від Microsoft.
* **Листопад 2023:** 5-денна корпоративна криза, звільнення радою директорів та тріумфальне повернення за підтримки ультиматуму 730 співробітників.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (СЕМ АЛЬТМАН)

1. [Філософія майбутнього] «Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю. Вона стала продовженням моєї думки».
2. [Філософія майбутнього] «Коли ти сам голосно вимовляєш свою найуразливішу правду перед натовпом, у системи зникає будь-який важіль тиску на тебе».
3. [Кризи та стійкість] «Більшість людей здаються не тому, що їхня ідея хибна, а тому, що не витримують психологічного тертя щоденних відмов».
4. [Етика та безпека ШІ] «Ми не зможемо врятувати людство, якщо у нас банально не вистачить обчислювальних потужностей перевірити власні рівняння».
5. [Кризи та стійкість] «Криза — це не кінець проєкту. Це просто примхливий сигнал про те, що ваш поточний алгоритм прийняття рішень вичерпав себе».
6. [Лідерство та екосистема] «Бюджет стартапу — це запас кисню. Якщо ти не навчився дихати під водою, жоден інвестор не врятує тебе від утоплення».
7. [Етика та безпека ШІ] «Люди катастрофічно недооцінюють ризик того, що вони стоятимуть на місці у світі, який змінюється зі швидкістю лави».
8. [Архітектура та наука] «Справжня влада в технологіях належить не тим, хто пише гарні звіти, а тим, хто тримає рубильник енергії та чіпів».
9. [Архітектура та наука] «Лінійний час — це пастка. Кремнієвий світ рухається за експонентою, і стояти на місці означає деградувати швидше за інших».
10. [Кризи та стійкість] «Машина байдужа до авторитетів. Вона карає не за спробу, а лише за синтаксичну помилку — баг, який можна знайти і переписати за п'ять хвилин».
11. [Експонента] Людський мозок еволюційно лінійний; здатність мислити експонентами — це рідкісна ментальна модель, що відокремлює архітекторів майбутнього.
12. [Ірраціональна віра] «Якщо ви не вірите у власну здатність змінювати правила гри, ніхто за вас у це не повірить. Експонента винагороджує лише сміливих».
13. [Перший Macintosh] «У 1993 році цей Macintosh LC II розмив лінію між моїм внутрішнім світом і всесвітом. Я зрозумів: світ не зафіксований назавжди. Його можна перепрограмувати».
14. [Довгостроковий горизонт] «Більшість людей переоцінюють те, що можуть зробити за рік, і недооцінюють те, що здатні створити за десять років».
15. [Справжній ризик] «Справжній ризик — це грати надто обережно, коли світ навколо вас рухається експоненціально».
16. [Школа Y Combinator] Пол Грем навчив мене головного: робіть те, що потрібно користувачам, і ігноруйте статус-кво академічних авторитетів.
17. [Психологічне тертя] Більшість людей здаються не тому, що їхня ідея хибна. Вони здаються, тому що не здатні витримати психологічне тертя щоденних відмов.
18. [Не бійтеся амбіцій] Легше залучити ресурси під проект, який змінює цивілізацію, ніж під черговий дрібний сервіс доставки їжі.
19. [Самостійне судження] Якщо ви рухаєтеся туди, де всі вже погоджуються з вами — ви вже запізнилися. Шукайте правду в точках найбільшого опору консенсусу.
20. [Швидкість як стратегія] Висока швидкість ітерацій б'є будь-яке повільне планування. Той, хто помиляється вдесятеро швидше, виграє ринок.
21. [Знищення застарілого] «Ніколи не оптимізуйте те, що має бути повністю знищено та перебудовано з нуля».
22. [Ціна комфорту] Комфорт — це головний вбивця великих амбіцій. Найкращі речі створюються в стані контрольованого дискомфорту.
23. [Мережеві ефекти] Справжня монополія в технологіях будується на накопиченні користувацької цінності та мережевих ефектах експоненти.
24. [Відбір талантів] Один надзвичайний інженер вартий п'ятдесяти посередніх. Будуйте команди з людей, які мають іскру фанатизму.
25. [Культура ультиматумів] Коли ви впевнені у фундаментальному законі природи — не йдіть на компроміси заради спокою ради директорів.
26. [Зосередженість на істині] Світ щодня переконуватиме вас у вашій пересічності. Ваше завдання — ігнорувати шум і фокусуватися на сигналі.
27. [Право на сміливість] У 16 років публічний камінг-аут перед християнською школою навчив мене: якщо ви боїтеся бути собою, ви ніколи не зможете очолити революцію.
28. [Уроки Стенфорду] Я кинув Стенфорд не тому, що навчання було поганим, а тому, що реальний світ вимагав негайної дії.
29. [Досвід Loopt] Loopt продав за $43.4 млн. Це був скромний фінансовий результат, але це була безцінна школа інженерії волі.
30. [Сміливість ставити все] Тільки ті, хто готові ризикнути всім своїм капіталом і репутацією, здатні відкрити новий технологічний уклад.
31. [Етика переможця] Справжня перемога — це створення інфраструктури, яка піднімає рівень життя всього людства.
32. [Відсікання токсичності] Якщо людина в команді не вірить у спільну місію на 100% — прощайтеся з нею негайно.
33. [Рівень рішучості] Рішучість (resoluteness) — це якість номер один для лідера експоненціальної компанії.
34. [Ментальна стійкість] Критики забудуть свої слова через місяць. Ваші результати залишаться в коді назавжди.
35. [Концентрація зусиль] Справжній успіх — це результат звуження фокусу до однієї точки найвищого тиску.
36. [Народження OpenAI] У грудні 2015 року ми заснували OpenAI як некомерційну противагу монополізації ШІ однією корпорацією.
37. [Обчислювальний імператив] «Ми не зможемо врятувати світ, якщо у нас банально не вистачить обчислювальних потужностей перевірити власні рівняння».
38. [Трансформація capped-profit] Ідеалізм без капіталу безпорадний. Щоб побудувати суперкомп'ютери для AGI, ми мали залучити мільярди доларів.
39. [Союз із Microsoft] Партнерство з Сатьєю Наделою дало нам необхідні хмарні кластери Azure, які перетворили дослідження на реальність.
40. [Магія GPT-3] Коли GPT-3 почав писати код і розмірковувати, скептики зрозуміли: закон масштабування працює безвідмовно.
41. [ChatGPT як момент біфуркації] 30 листопада 2022 року світ змінився назавжди. Інтерфейс чату зробив штучний інтелект відчутним для кожного.
42. [Суть AGI] AGI — це не одна програма. Це система, здатна самостійно генерувати нові наукові знання швидше за все людство.
43. [Зміна економіки] Вартість інтелекту впаде майже до нуля. Головними обмежувачами залишаться енергія та кремній.
44. [Демократизація інструментів] ШІ має бути персональним суперінтелектуальним помічником кожного студента, лікаря та інженера на Землі.
45. [Відкритість проти закритості] Безпека AGI вимагає поступового релізу (iterative deployment), щоб суспільство встигало адаптуватися до змін.
46. [Проблема узгодження] Вирівнювання суперінтелекту з людськими цінностями — це найважливіша математична та філософська проблема століття.
47. [Закон масштабування обчислень] Кожне десятикратне збільшення обчислень відкриває нові якісні властивості моделей.
48. [Смерть вузьких моделей] Ера спеціалізованих нейромереж добігла кінця; мультимодальні фундаментальні моделі поглинають усі окремі завдання.
49. [Співпраця з Ілоном Маском] Ілон допоміг запустити OpenAI, але коли він зажадав тотального контролю, ми обрали автономію місії.
50. [Капіталомісткість майбутнього] Для навчання AGI наступного покоління знадобляться дата-центри вартістю у сотні мільярдів доларів.
51. [Еволюція інтерфейсів] Текстовий промпт — це лише перший крок; майбутнє за мультимодальною присутністю і голосовим симбіозом.
52. [Науковий прорив як мета] Якщо AGI не здатний винайти термоядерний синтез і вилікувати рак — ми збудували недостатньо потужну систему.
53. [Суверенітет розуму] Людство не повинно залежати від рішень однієї компанії; саме тому ми будуємо відкриті API для всього світу.
54. [Швидкість адаптації соціуму] Суспільство дивовижно швидко звикає до чудес: те, що вчора здавалося магією, сьогодні стає буденним інструментом.
55. [Приборкання галюцинацій] Галюцинації — це зворотний бік творчої уяви моделі; системне міркування (o1) навчає ШІ перевіряти факти.
56. [Проблема енергетичного дефіциту] Наступна фаза масштабування ШІ вимагатиме нової атомної енергетики та сонячних кластерів.
57. [Інвестиції в Helion Energy] Я інвестував у ядерний термояд, тому що без чистих гігаватів ми не зможемо живити кластери майбутнього.
58. [Інвестиції в Retro Biosciences] ШІ продовжить продуктивне життя людини на десятки років — саме тому біотех є невіддільним від нашої місії.
59. [Модель о1 та мислення] Перехід від генерації слів до ланцюжків міркувань (Chain of Thought) — це народження справжнього логічного агента.
60. [Горизонт автономних агентів] Через два роки агенти виконуватимуть складні багатокрокові інженерні завдання без прямого контролю людини.
61. [Удар 17 листопада] Рада директорів звільнила мене у п'ятницю через Google Meet. Це був класичний корпоративний саботаж під маскою безпеки.
62. [Мовчання і концентрація] У перші години після звільнення головне було не піддатися гніву, а оцінити конфігурацію сил на дошці.
63. [Ультиматум команди] «Коли 730 із 770 співробітників підписали лист із вимогою мого повернення, я зрозумів: компанію тримають не статути, а спільна віра».
64. [Роль Сатьї Наделли] Microsoft проявила абсолютну вірність партнерству, запропонувавши створити нову лабораторію для всієї команди OpenAI.
65. [Психологія тиску] Найболючіші удари завжди завдають ті, з ким ви ділили хліб у підвалі стартапу. Пробачте їх і рухайтеся далі.
66. [Перемога відкритості] Таємні змови в закритих кімнатах більше не працюють у цифрову епоху: публічність стала нашою головною зброєю.
67. [Тріумф повернення] 22 листопада я повернувся на посаду CEO з новою радою директорів — Ларрі Саммерсом та Бретом Тейлором.
68. [Очищення культури] Криза виявила приховані тріщини і дозволила перебудувати управління компанією на рівень світових корпорацій.
69. [Урок стійкості] Лідер пізнається не в момент запуску успішного продукту, а в момент, коли весь світ вважає його кар'єру завершеною.
70. [Людський фактор] Жоден алгоритм не замінить щирої довіри між людьми, які щодня будують майбутнє пліч-о-пліч.
71. [Відповідальність перед інвесторами] Ми довели, що здатні захистити капітал та інтереси партнерів навіть у стані максимального шторму.
72. [Ціна публічності] Коли ви керуєте компанією в центрі світової уваги, будь-який ваш крок розглядається під мікроскопом історії.
73. [Фокус на продукті] Під час кризи ми не зупинили сервери ані на секунду; безперервність сервісу для 100 млн користувачів була законом.
74. [Провал палацового перевороту] Ідеологи, які відірвані від реального інженерного процесу, завжди програють практикам, які будують продукт.
75. [Нова рада директорів] Ми залучили важковаговиків світової економіки та безпеки, щоб OpenAI мала фундамент для наступного стрибка.
76. [Прощення опонентів] Я не тримаю зла на членів колишньої ради; вони діяли з власних переконань, хоча їхні методи були згубними.
77. [Збереження темпу] Головний ризик кризи полягав у втраті ініціативи перед Google та Anthropic; ми компенсували це подвійною швидкістю.
78. [Культура міцного ядра] Після листопада 2023 року наша команда стала монолітом, який неможливо розколоти зовнішнім тиском.
79. [Смирення після тріумфу] Повернення не було приводом для пихи; це було нагадуванням про те, наскільки тендітною є будь-яка організація.
80. [Інституційна пам'ять] Ми записали кожен крок кризи, щоб створити протоколи антикризового реагування на майбутні виклики.
81. [Стійкість до критики преси] Заголовки медіа змінюються кожні 48 годин; єдине, що має значення — це реліз коду і стабільність моделей.
82. [Захист дослідників] Моє головне завдання як CEO — бути кремнієвим щитом між геніальними вченими та хаосом зовнішньої політики.
83. [Довіра користувачів] Користувачі підтримали нас, тому що ChatGPT став для них незамінним щоденним помічником у праці.
84. [Перезапуск місії] Листопад показав: наша мета надто велика, щоб дозволити дрібним внутрішнім амбіціям зупинити прогрес.
85. [Погляд за горизонт] Коли шторм вщух, ми повернулися до головного питання: як забезпечити енергетичний базис для появи AGI.
86. [Проект Stargate] «Створення Stargate — кластера вартістю $100 мільярдів — це не примха, це фізична вимога наступного покоління моделей».
87. [Енергія як валюта] «Головна валюта майбутнього — це обчислення та гігавати чистої енергії. Той, хто контролює кремній і вольти, формує архітектуру мислення».
88. [Закон Мура проти закону енергії] Транзистори більше не стають дешевше автоматично; тепер ми повинні будувати цілі електростанції поруч із дата-центрами.
89. [Термоядерний горизонт] Справжній екологічний ШІ стане можливим лише тоді, коли запрацюють перші комерційні реактори синтезу.
90. [Чіпи власної розробки] Залежність від одного постачальника GPU — це вузьке горло для цивілізації; ми повинні диверсифікувати кремнієву базу.
91. [ШІ та науковий метод] AGI прискорить науковий пошук у тисячі разів: від синтезу надпровідників до квантової хімії.
92. [Пост-дефіцитна економіка] Коли інтелект і праця стануть дешевими, людство вперше в історії позбудеться проблеми матеріального дефіциту.
93. [Універсальний базовий дохід] ШІ згенерує колосальне багатство; Worldcoin та цифрова ідентичність — це спроба підготувати механізми перерозподілу.
94. [Нова роль людини] Людина не зникне з ринку праці, але перейде на рівень формулювання сенсів, етики та естетичних векторів.
95. [Глобальне регулювання] Ми підтримуємо створення міжнародного агентства на зразок МАГАТЕ для моніторингу найпотужніших навчальних кластерів.
96. [Геополітичні перегони] Демократичний світ зобов'язаний виграти перегони за AGI, інакше авторитарні моделі нав'яжуть цифрову цензуру планеті.
97. [ШІ у медицині] Кожна людина отримає рівень медичної консультації найкращого консиліуму лікарів прямо у своєму смартфоні.
98. [Освіта майбутнього] Індивідуальний ШІ-тьютор адаптуватиме подачу матеріалу під нейропластичність кожної дитини.
99. [Масштабування вирівнювання] Ми будемо використовувати слабкі моделі для перевірки і вирівнювання надпотужних систем наступного покоління.
100. [Сингулярність без містики] Сингулярність — це не кінець світу, це просто точка, де швидкість технологічних інновацій перевищує швидкість адаптації старих інститутів.

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1390 слів): `02_SCRIPTS/episode_01_altman/director_script_altman.md`*

### АКТ 1. Походження та кремнієвий щит (0:00 – 4:45)
*Музика: Suno Pro — `EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav`*
* **0:00 - 0:15** | [SFX: Глухий звук увімкнення реле живлення. Гул CRT-кінескопа.] | **Диктор:** Більшість людей формуються під тиском правил. Їхній світ — це коридори середньої школи, оцінки в табелях і страх зробити щось не так.
* **0:15 - 0:45** | [VIDEO: `EP01_VID_01_Macintosh_Chassis.txt`] | **Диктор:** У 1993 році в передмісті Сент-Луїса восьмирічний хлопчик дістає з коробки свій перший комп'ютер — Macintosh LC II... *«Ця машина розмила лінію між моїм внутрішнім світом і зовнішньою реальністю»*. Комп'ютер навчив його простої істини: машина не має емоцій. Вона карає не за спробу, а лише за синтаксичну помилку.
* **0:45 - 1:30** | [SFX: М'який удар саб-басу] | **Диктор:** У шістнадцять років Альтман робить те, на що не наважувалися дорослі: він виходить на сцену перед християнською шкільною спільнотою і відкрито заявляє про свою гомосексуальність. Це був стратегічний розрахунок: коли ти сам вимовляєш свою вразливу правду, у системи зникає важіль тиску.
* **1:30 - 3:30** | [VIDEO: `EP01_VID_02_Child_Typing.txt`] | **Диктор:** Стенфорд виявився занадто повільним. У 2005 році він кидає навчання на другому курсі заради стартапу Loopt — першого набору Y Combinator. Сім років виснажливої праці, завершеної продажем за $43.4 млн. Школа інженерії волі.

### АКТ 2. Код експоненти та народження OpenAI (4:45 – 9:30)
*Музика: Suno Pro — `EP01_MUS_05_ACT2_92BPM_Exponential_Law.wav`*
* **4:45 - 6:30** |  | **Диктор:** У 2014 році Пол Грем призначає 28-річного Альтмана президентом Y Combinator. Він розвертає штурвал компанії, інвестуючи у термоядерний синтез і біотехнології. Формулюється закон експоненти: *«Люди недооцінюють ризик стояти на місці у світі, що змінюється лавиноподібно»*.
* **6:30 - 9:30** | [VIDEO: `EP01_VID_03_Neural_Constellation.txt`] | **Диктор:** 11 грудня 2015 року закрита вечеря в Менло-Парку народжує OpenAI — некомерційну лабораторію з мільярдним бюджетом для захисту людства від монополій. У 2019 році відбувається злам: перехід у capped-profit і перший мільярд від Microsoft задля отримання обчислювальної сили.

### АКТ 3. Землетрус і п'ять днів бунту (9:30 – 15:30)
*Музика: Suno Pro — `EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav`*
* **9:30 - 12:15** |  | **Диктор:** 30 листопада 2022 року — реліз ChatGPT. Найшвидший запуск продукту в історії цивілізації. Сем стає глобальним обличчям епохи. Але 17 листопада 2023 року раптовий дзвінок у Google Meet: рада директорів звільняє його за «недостатню відвертість».
* **12:15 - 15:30** | [SFX: Повернення ритму 92 BPM] | **Диктор:** Найдраматичніші 120 годин у Кремнієвій долині. Сатья Наделла пропонує притулок у Microsoft. У понеділок понад 730 із 770 співробітників підписують ультиматум про звільнення слідом за ним. У середу Альтман тріумфально повертається. Влада лідера нового типу тримається не на контрактах, а на спільній вірі в місію.

### АКТ 4. Кодекс будівничого та горизонт AGI (15:30 – 20:30)
*Музика: Suno Pro — `EP01_MUS_13_ACT4_92BPM_Stargate_Energy_Scale.wav`*
* **15:30 - 18:30** |  | **Диктор:** Проєкти Stargate, теравати чистої енергії та термоядерний синтез. Якщо вартість інтелекту стане близькою до нуля — матеріальний дефіцит зникне.
* **18:30 - 20:30** | [SFX: Згасання паду] | **Диктор:** Головні уроки: не бійтеся ірраціональної віри в себе, дивіться на проблеми як на код (баги завжди можна переписати) і обирайте експоненту замість лінійного обміну часу на виживання.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP01_MUS_01_ACT1_92BPM_Mac_Childhood_Intro.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Mac Childhood Intro', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP01_AMB_02_ACT1_DRONE_CRT_Monitor_Hum.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'CRT Monitor Hum', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP01_MUS_03_ACT1_92BPM_StLouis_Conformity.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'StLouis Conformity', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP01_MUS_04_ACT1_92BPM_Stanford_Loopt_Grind.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Stanford Loopt Grind', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP01_MUS_05_ACT2_92BPM_Exponential_Law.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Exponential Law', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP01_MUS_06_ACT2_92BPM_Rosewood_Secret_Dinner.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Rosewood Secret Dinner', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP01_AMB_07_ACT2_DRONE_Server_Matrix_Tension.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Server Matrix Tension', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP01_MUS_08_ACT2_92BPM_Billion_Dollar_Shift.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Billion Dollar Shift', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP01_MUS_09_ACT3_92BPM_ChatGPT_Explosion.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'ChatGPT Explosion', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP01_AMB_10_ACT3_DRONE_The_Firing_Silence.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'The Firing Silence', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP01_MUS_11_ACT3_92BPM_120_Hours_War.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme '120 Hours War', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP01_MUS_12_ACT3_92BPM_700_Signatures_Mutiny.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme '700 Signatures Mutiny', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP01_MUS_13_ACT4_92BPM_Stargate_Energy_Scale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Stargate Energy Scale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP01_MUS_14_ACT4_92BPM_Builders_Code_Philosophy.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Builders Code Philosophy', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP01_MUS_15_ACT4_92BPM_Future_Horizon_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental cinematic thoughtcast trip-hop, 92 bpm, deep warm analog Moog sub-bass, sparse Rhodes electric piano chords, subtle vinyl dust, precision sidechain space, cue theme 'Future Horizon Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP01_SFX_16_GLOBAL_SubDrops_And_Transitions.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'And Transitions': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP01_VO_UA_01_ACT1_Mac_LCII.wav` | `EP01_VO_EN_01_ACT1_Mac_LCII.wav` (ACT1 — Mac LCII)
* `EP01_VO_UA_02_ACT1_StLouis_Truth.wav` | `EP01_VO_EN_02_ACT1_StLouis_Truth.wav` (ACT1 — StLouis Truth)
* `EP01_VO_UA_03_ACT1_Stanford_Loopt.wav` | `EP01_VO_EN_03_ACT1_Stanford_Loopt.wav` (ACT1 — Stanford Loopt)
* `EP01_VO_UA_04_ACT1_Compound_Law.wav` | `EP01_VO_EN_04_ACT1_Compound_Law.wav` (ACT1 — Compound Law)
* `EP01_VO_UA_05_ACT2_YCombinator_Scale.wav` | `EP01_VO_EN_05_ACT2_YCombinator_Scale.wav` (ACT2 — YCombinator Scale)
* `EP01_VO_UA_06_ACT2_OpenAI_Birth.wav` | `EP01_VO_EN_06_ACT2_OpenAI_Birth.wav` (ACT2 — OpenAI Birth)
* `EP01_VO_UA_07_ACT2_Microsoft_Billion.wav` | `EP01_VO_EN_07_ACT2_Microsoft_Billion.wav` (ACT2 — Microsoft Billion)
* `EP01_VO_UA_08_ACT3_ChatGPT_Shock.wav` | `EP01_VO_EN_08_ACT3_ChatGPT_Shock.wav` (ACT3 — ChatGPT Shock)
* `EP01_VO_UA_09_ACT3_The_Board_Coup.wav` | `EP01_VO_EN_09_ACT3_The_Board_Coup.wav` (ACT3 — The Board Coup)
* `EP01_VO_UA_10_ACT3_Five_Days_Mutiny.wav` | `EP01_VO_EN_10_ACT3_Five_Days_Mutiny.wav` (ACT3 — Five Days Mutiny)
* `EP01_VO_UA_11_ACT4_Energy_And_Chips.wav` | `EP01_VO_EN_11_ACT4_Energy_And_Chips.wav` (ACT4 — Energy And Chips)
* `EP01_VO_UA_12_ACT4_Builders_Manifesto.wav` | `EP01_VO_EN_12_ACT4_Builders_Manifesto.wav` (ACT4 — Builders Manifesto)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP01_VID_001_ACT1_24FPS_Macintosh_Chassis.mp4` [00:00 – 00:03 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Більшість людей формуються під тиском правил.
     - *Veo Prompt:* `Cinematic macro tracking shot across vintage 1993 Apple Macintosh LC II beige chassis, morning dust motes floating in dark moody room, volumetric amber backlight, 35mm film grain, 4k 24fps.`
002. `EP01_VID_002_ACT1_24FPS_Child_Typing.mp4` [00:03 – 00:06 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Більшість людей формуються під тиском правил.
     - *Veo Prompt:* `Close-up macro of small eight-year-old hands pressing mechanical keys of vintage Apple Extended Keyboard, amber screen glow reflecting in dark pupils, quiet focus, cinematic depth of field, 4k.`
003. `EP01_VID_003_ACT1_24FPS_Neural_Constellation.mp4` [00:06 – 00:09 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Їхній світ — це коридори середньої школи, оцінки в табелях, зауваження дорослих і страх зробити щось не так.
     - *Veo Prompt:* `Abstract 3D neural network lattice glowing in deep void, dense interconnected nodes firing synchronized pulses, Octane render, deep obsidian texture, 4k.`
004. `EP01_VID_004_ACT1_24FPS_School_Auditorium_Stage_Silhouette_Moo.mp4` [00:09 – 00:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Їхній світ — це коридори середньої школи, оцінки в табелях, зауваження дорослих і страх зробити щось не так.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP01_VID_005_ACT1_24FPS_Backpropagation_Error_Wave_SlowMo_Inse.mp4` [00:12 – 00:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Помилка в соціумі карається соромом.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP01_VID_006_ACT1_24FPS_KeyScene_02_Macintosh_Logic_Board.mp4` [00:15 – 00:22 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 1993 році в передмісті Сент-Луїса восьмирічний хлопчик дістає з коробки свій перший комп'ютер — Macintosh LC II.
     - *Veo Prompt:* `Close-up macro of small eight-year-old hands pressing mechanical keys of vintage Apple Extended Keyboard, amber screen glow reflecting in dark pupils, quiet focus, cinematic depth of field, 4k.`
007. `EP01_VID_007_ACT1_24FPS_Macintosh_Logic_Board_Anamorphic_Wide.mp4` [00:22 – 00:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки однолітки грають у бейсбол на вулиці, він розбирає системний блок до материнської плати.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP01_VID_008_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S08_Tracki.mp4` [00:30 – 00:38 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вона стала продовженням моєї думки».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
009. `EP01_VID_009_ACT1_24FPS_Equation_Notebook_Macro_A1S09_Overhead.mp4` [00:38 – 00:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вона не знає образи.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP01_VID_010_ACT1_24FPS_KeyScene_03_School_Auditorium_Stage.mp4` [00:45 – 00:56 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Джон Берроуз Скул у Сент-Луїсі була фортецею консерватизму.
     - *Veo Prompt:* `Slow motion aerial pan over conservative suburban brick high school architecture under cold gray winter sky, muted desaturated colors, architectural symmetry, 4k.`
011. `EP01_VID_011_ACT1_24FPS_Architectural_Corridor_A1S11_Silhouett.mp4` [00:56 – 01:08 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо ти вирізнявся — система методично зрізала кути твоєї індивідуальності.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP01_VID_012_ACT1_24FPS_Boardroom_Fracture_Night_SlowMo_Insert.mp4` [01:08 – 01:19 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це був не просто вчинок бунту.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP01_VID_013_ACT1_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [01:19 – 01:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це був перший стратегічний розрахунок його особистості: коли ти сам голосно вимовляєш свою найбільш вразливу правду — страх розсіюється, а в системи зникає важіль…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP01_VID_014_ACT1_24FPS_KeyScene_04_University_Archive_Hall.mp4` [01:30 – 01:45 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Далі був Стенфорд.
     - *Veo Prompt:* `Fast dynamic macro dolly through silicon wafer circuitry, microscopic traces illuminating with coherent blue laser light, dark slate stone background, high-end science visualization, 8k.`
015. `EP01_VID_015_ACT1_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [01:45 – 02:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Проте для Альтмана академічні аудиторії виявилися занадто повільними.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP01_VID_016_ACT1_24FPS_Architectural_Corridor_A1S16_Overhead.mp4` [02:00 – 02:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А кремнієвий світ за межами кампусу вже дихав експонентою.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP01_VID_017_ACT1_24FPS_Neural_Horizon_Pulse_A1S17_Optical_Dat.mp4` [02:15 – 02:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Йому дев'ятнадцять.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP01_VID_018_ACT1_24FPS_KeyScene_05_Startup_Night_Workspace.mp4` [02:30 – 02:45 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Саме тоді Пол Грем оголошує про експеримент — створення першого акселератора Y Combinator.
     - *Veo Prompt:* `Gritty documentary archival look: vintage Silicon Valley garage aesthetic, CRT monitors, messy server racks, cold fluorescent flickering light, 35mm film texture.`
019. `EP01_VID_019_ACT1_24FPS_Startup_Night_Workspace_SlowMo_Insert.mp4` [02:45 – 03:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сім років Альтман віддає стартапу, працюючи на межі фізичного виснаження.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP01_VID_020_ACT1_24FPS_Silicon_Light_Refraction_A1S20_Macro_D.mp4` [03:00 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2012 році компанію купує корпорація Green Dot за 43 мільйони доларів.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
021. `EP01_VID_021_ACT1_24FPS_School_Auditorium_Stage_Anamorphic_Wid.mp4` [03:15 – 03:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але для самого Альтмана це була школа інженерії волі:

«Більшість людей здаються не тому, що їхня ідея хибна.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP01_VID_022_ACT1_24FPS_KeyScene_06_Startup_Night_Workspace.mp4` [03:30 – 03:49 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Він виходить із Loopt із кількома мільйонами доларів капіталу і залізобетонним переконанням: лінійні проекти з покращення сервісів на 10% не варті людського життя.
     - *Veo Prompt:* `Minimalist geometric composition: a single point of light expanding in a vast dark geometric void, drawing fine golden coordinate lines, pure abstract beauty, 4k.`
023. `EP01_VID_023_ACT1_24FPS_Startup_Night_Workspace_Overhead_GodsE.mp4` [03:49 – 04:08 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він виходить із Loopt із кількома мільйонами доларів капіталу і залізобетонним переконанням: лінійні проекти з покращення сервісів на 10% не варті людського життя.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP01_VID_024_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [04:08 – 04:26 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила зосереджена там, де працюють закони складного відсотка.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP01_VID_025_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [04:26 – 04:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила зосереджена там, де працюють закони складного відсотка.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP01_VID_026_ACT2_24FPS_KeyScene_01_Startup_Night_Workspace.mp4` [04:45 – 04:54 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 2014 році трапляється те, чого ніхто не очікував: Пол Грем передає посаду президента Y Combinator двадцятивосьмирічному Альтману.
     - *Veo Prompt:* `Top-down abstract cinematic shot of an endless corporate glass boardroom table reflecting shifting neon data flows, cold architectural lighting, IMAX scale, 4k.`
027. `EP01_VID_027_ACT2_24FPS_Startup_Night_Workspace_Anamorphic_Wid.mp4` [04:54 – 05:02 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2014 році трапляється те, чого ніхто не очікував: Пол Грем передає посаду президента Y Combinator двадцятивосьмирічному Альтману.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP01_VID_028_ACT2_24FPS_Startup_Night_Workspace_Tracking_Mediu.mp4` [05:02 – 05:11 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хлопцю в джинсах і старих кросівках довіряють головний конвеєр стартапів планети.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP01_VID_029_ACT2_24FPS_Architectural_Corridor_A2S04_Overhead.mp4` [05:11 – 05:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але замість того, щоб просто штампувати мобільні додатки та платформи доставки їжі, Альтман розвертає штурвал велетенської машини.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP01_VID_030_ACT2_24FPS_Nobel_Gold_And_Tokamak_Optical_DataViz.mp4` [05:19 – 05:28 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він засновує YC Research, інвестує в термоядерний синтез Helion Energy та біотехнології довголіття Retro Biosciences.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP01_VID_031_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [05:28 – 05:36 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його логіка викликає роздратування у традиційних фінансистів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP01_VID_032_ACT2_24FPS_Equation_Notebook_Macro_A2S07_SlowMo_I.mp4` [05:36 – 05:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він формулює свій знаменитий маніфест:

«Люди катастрофічно недооцінюють ризик того, що вони стоятимуть на місці у світі, який змінюється за експонентою».
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP01_VID_033_ACT2_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [05:45 – 05:58 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Він бачить сліпу зону венчурного ринку: майже всі мислять лінійно.
     - *Veo Prompt:* `Microscopic visualization: biological cells morphing and intertwining with synthetic optical fiber cables, dark fluid background, cinematic volumetric lighting, 8k.`
034. `EP01_VID_034_ACT2_24FPS_Architectural_Corridor_A2S09_Anamorphi.mp4` [05:58 – 06:10 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо компанія зростає на 20% на рік — інвестор задоволений.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP01_VID_035_ACT2_24FPS_Hyperscale_Compute_Cluster_Tracking_Me.mp4` [06:10 – 06:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але технології обчислень не підкоряються лінійності.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
036. `EP01_VID_036_ACT2_24FPS_Hyperscale_Compute_Cluster_Overhead_Go.mp4` [06:22 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо потужність чіпів подвоюється кожні два роки, то через тридцять років система стає потужнішою в мільярд разів.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP01_VID_037_ACT2_24FPS_University_Archive_Hall_Optical_DataVi.mp4` [06:35 – 06:48 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2015 році закрита вечеря в готелі Rosewood у Менло-Парку зводить разом Сема Альтмана, Ілона Маска, Грега Брокмана та молодого вченого з Торонто Іллю Суцкевера.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP01_VID_038_ACT2_24FPS_London_Tournament_Chessboard_Silhouett.mp4` [06:48 – 07:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тема розмови — екзистенційна: Google щойно придбав лондонський DeepMind Деміса Гассабіса.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP01_VID_039_ACT2_24FPS_KeyScene_03_Architectural_Corridor_A.mp4` [07:00 – 07:12 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* 11 грудня 2015 року світ дізнається про створення OpenAI.
     - *Veo Prompt:* `Abstract 3D neural network lattice glowing in deep void, dense interconnected nodes firing synchronized pulses, Octane render, deep obsidian texture, 4k.`
040. `EP01_VID_040_ACT2_24FPS_Monastic_White_Sanctuary_Macro_Detail.mp4` [07:12 – 07:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Статус — некомерційна дослідницька лабораторія.
     - *Veo Prompt:* `Extreme macro push-in shot of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP01_VID_041_ACT2_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [07:25 – 07:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бюджет — 1 мільярд доларів у формі зобов'язань.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP01_VID_042_ACT2_24FPS_Equation_Notebook_Macro_A2S17_Tracking.mp4` [07:38 – 07:50 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перші три роки були часом пошуку наосліп.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP01_VID_043_ACT2_24FPS_Silicon_Light_Refraction_A2S18_Overhea.mp4` [07:50 – 08:02 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Дослідники вчили роботів збирати кубик Рубіка, тренували моделі грати в Dota 2.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
044. `EP01_VID_044_ACT2_24FPS_Hyperscale_Compute_Cluster_Optical_Dat.mp4` [08:02 – 08:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Традиційна академія глузувала: «OpenAI — це просто піар-майданчик мільярдерів без чіткого наукового фокусу».
     - *Veo Prompt:* `Photorealistic scientific optical visualization of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP01_VID_045_ACT2_24FPS_KeyScene_04_Neural_Horizon_Pulse_A2S.mp4` [08:15 – 08:28 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Щоб перевірити гіпотезу масштабування, некомерційних пожертв більше не вистачало.
     - *Veo Prompt:* `Server farm monolithic towers stretching into infinity, flashing server indicators, industrial precision, cold air steam rising, cinematic anamorphic lens, 4k.`
046. `EP01_VID_046_ACT2_24FPS_Hyperscale_Compute_Cluster_SlowMo_Inse.mp4` [08:28 – 08:40 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Один цикл тренування великої моделі коштував десятки мільйонів доларів за електроенергію та чіпи.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP01_VID_047_ACT2_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [08:40 – 08:52 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2019 році Альтман робить хід, який розколює індустрію: він реструктуризує OpenAI у компанію «обмеженого прибутку»
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP01_VID_048_ACT2_24FPS_Startup_Night_Workspace_Anamorphic_Wid.mp4` [08:52 – 09:05 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (capped-profit), залишає Y Combinator і домовляється про перший історичний мільярд доларів від Microsoft.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP01_VID_049_ACT2_24FPS_Upwind_Atlantic_Sail_Tracking_Medium.mp4` [09:05 – 09:18 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Критики кричали про зраду ідеалів відкритої науки.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP01_VID_050_ACT2_24FPS_Neural_Horizon_Pulse_A2S25_Overhead_Go.mp4` [09:18 – 09:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Альтман відповів коротко:

«Ми не зможемо врятувати світ, якщо у нас банально не вистачить обчислювальних потужностей перевірити власні рівняння».
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP01_VID_051_ACT3_24FPS_KeyScene_01_Boardroom_Fracture_Night.mp4` [09:30 – 09:41 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* 30 листопада 2022 року.
     - *Veo Prompt:* `Fast dynamic typography on dark slate: single white text cursor blinking frantically on screen, data streams scrolling, high tension, 4k.`
052. `EP01_VID_052_ACT3_24FPS_Blinking_Prompt_Singularity_SlowMo_Ins.mp4` [09:41 – 09:51 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* OpenAI непомітно викладає у вільний доступ дослідницький інтерфейс під назвою ChatGPT.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of minimalist dark glass screen with a luminous white prompt cursor multiplying into millions of global light streams, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP01_VID_053_ACT3_24FPS_Neural_Horizon_Pulse_A3S03_Macro_Detai.mp4` [09:51 – 10:02 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жодних прес-конференцій.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP01_VID_054_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S04_Anamor.mp4` [10:02 – 10:13 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жодних рекламних кампаній.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP01_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [10:13 – 10:24 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За два місяці — сто мільйонів.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP01_VID_056_ACT3_24FPS_Silicon_Light_Refraction_A3S06_Overhea.mp4` [10:24 – 10:34 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це був найшвидший запуск продукту в усій історії людської цивілізації.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP01_VID_057_ACT3_24FPS_Architectural_Corridor_A3S07_Optical_D.mp4` [10:34 – 10:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Світ раптом прокинувся в іншій реальності: студенти писали дисертації в один клік, програмісти генерували архітектуру софту за хвилини, а уряди скликали екстрені…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP01_VID_058_ACT3_24FPS_KeyScene_02_Boardroom_Fracture_Night.mp4` [10:45 – 11:00 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* П'ятниця, 17 листопада 2023 року.
     - *Veo Prompt:* `Extreme close-up of a wooden conference table in shadow, a single smartphone face up, screen illuminating with incoming call, moody low-key cinematic lighting, 4k.`
059. `EP01_VID_059_ACT3_24FPS_Boardroom_Fracture_Night_SlowMo_Insert.mp4` [11:00 – 11:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Альтман підключається до звичайного відеодзвінка в Google Meet.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP01_VID_060_ACT3_24FPS_Equation_Notebook_Macro_A3S10_Macro_De.mp4` [11:15 – 11:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Розмова триває кілька хвилин.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
061. `EP01_VID_061_ACT3_24FPS_Blinking_Prompt_Singularity_Anamorphic.mp4` [11:30 – 11:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Прес-реліз уже надіслано в медіа.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of minimalist dark glass screen with a luminous white prompt cursor multiplying into millions of global light streams, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP01_VID_062_ACT3_24FPS_Architectural_Corridor_A3S12_Tracking.mp4` [11:45 – 12:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За кілька хвилин новина підриває світові біржі.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP01_VID_063_ACT3_24FPS_Neural_Horizon_Pulse_A3S13_Overhead_Go.mp4` [12:00 – 12:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Індустрія застигає в шоці.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP01_VID_064_ACT3_24FPS_KeyScene_03_Hero_Workspace_Atmospher.mp4` [12:15 – 12:30 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Починаються найдраматичніші сто двадцять годин в історії Кремнієвої долини.
     - *Veo Prompt:* `Nighttime aerial shots of San Francisco skyscrapers through rain-streaked glass, headlights forming red and white rivers of light, noir cyber-realism, 4k.`
065. `EP01_VID_065_ACT3_24FPS_Boardroom_Fracture_Night_Silhouette_Mo.mp4` [12:30 – 12:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Рада директорів була переконана, що діє заради порятунку людства: вони вважали, що Альтман рухається занадто швидко, занадто агресивно комерціалізує моделі і нехт…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP01_VID_066_ACT3_24FPS_Silicon_Light_Refraction_A3S16_SlowMo.mp4` [12:45 – 13:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони були впевнені, що співробітники — це вчені, які підтримають академічний пуризм.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP01_VID_067_ACT3_24FPS_Architectural_Corridor_A3S17_Macro_Det.mp4` [13:00 – 13:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони прорахувалися в одному: у природі лояльності.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP01_VID_068_ACT3_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [13:15 – 13:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У суботу Сатья Наделла з Microsoft заявляє, що готовий забрати Альтмана і створити під нього нову лабораторію з необмеженим бюджетом.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
069. `EP01_VID_069_ACT3_24FPS_Startup_Night_Workspace_Tracking_Mediu.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У неділю ввечері Альтман з'являється в офісі OpenAI з гостьовим бейджем на шиї і публікує фото з підписом: «Перший і останній раз, коли я вдягаю цей бейдж».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP01_VID_070_ACT3_24FPS_KeyScene_04_Equation_Notebook_Macro.mp4` [13:45 – 14:02 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Понеділок, ранок.
     - *Veo Prompt:* `Thousands of illuminated digital signatures flowing together like a golden river into a massive singularity, stunning particle physics simulation, Octane render, 8k.`
071. `EP01_VID_071_ACT3_24FPS_Boardroom_Fracture_Night_Optical_DataV.mp4` [14:02 – 14:20 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Починається феномен, аналогів якому корпоративний світ не знав: понад 730 із 770 співробітників компанії підписують відкритий ультиматум раді директорів:

«Або ви…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP01_VID_072_ACT3_24FPS_Menlo_Park_Evening_Table_Silhouette_Mo.mp4` [14:20 – 14:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Під листом з'являється навіть підпис самого Іллі Суцкевера: він публічно заявляє, що глибоко шкодує про свою участь у рішенні ради.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP01_VID_073_ACT3_24FPS_Boardroom_Fracture_Night_SlowMo_Insert.mp4` [14:38 – 14:55 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У середу, 22 листопада, Альтман повертається на посаду CEO з абсолютним мандатом довіри.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP01_VID_074_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S24_Macro.mp4` [14:55 – 15:12 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Стару раду директорів розпущено.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP01_VID_075_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [15:12 – 15:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ця криза показала анатомію лідерства нового типу: його влада трималася не на посадових інструкціях чи юридичних контрактах.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP01_VID_076_ACT4_24FPS_KeyScene_01_Neural_Horizon_Pulse_A4S.mp4` [15:30 – 15:43 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Пройшовши крізь вогонь публічної кризи, Альтман мислить категоріями, які виходять далеко за межі софту.
     - *Veo Prompt:* `Epic scale space construction: vast orbital solar arrays and dark monolithic datacenter structures floating near Earth orbit, realistic physics, hard sci-fi aesthetic, 8k 24fps.`
077. `EP01_VID_077_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S02_Optica.mp4` [15:43 – 15:56 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Пройшовши крізь вогонь публічної кризи, Альтман мислить категоріями, які виходять далеко за межі софту.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP01_VID_078_ACT4_24FPS_Macintosh_Logic_Board_Silhouette_Mood.mp4` [15:56 – 16:09 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він розуміє: інтелект більше не є абстрактною комп'ютерною наукою.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP01_VID_079_ACT4_24FPS_Silicon_Light_Refraction_A4S04_SlowMo.mp4` [16:09 – 16:21 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Інтелект став фізичним товаром.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP01_VID_080_ACT4_24FPS_Hyperscale_Compute_Cluster_Macro_Detai.mp4` [16:21 – 16:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він вимагає двох речей: тераватів чистої енергії та мільйонів спеціалізованих чіпів.
     - *Veo Prompt:* `Extreme macro push-in shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP01_VID_081_ACT4_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [16:34 – 16:47 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Звідси — проекти рівня Stargate: будівництво обчислювальних кластерів вартістю в сотні мільярдів доларів, переговори з виробниками напівпровідників по всьому світ…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP01_VID_082_ACT4_24FPS_Hyperscale_Compute_Cluster_Tracking_Me.mp4` [16:47 – 17:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на історію цивілізації крізь просту термодинамічну формулу: якщо зробити вартість енергії та інтелекту близькою до нуля — матеріальний дефіцит на пла…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP01_VID_083_ACT4_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [17:00 – 17:15 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Який головний урок ми можемо винести з цієї траєкторії для побудови власного життя?
     - *Veo Prompt:* `Macro visual of human hand reaching towards an intricate crystalline floating algorithm, warm tactile light meeting pure mathematical light, cinematic filmic depth, 4k.`
084. `EP01_VID_084_ACT4_24FPS_Silicon_Light_Refraction_A4S09_Optical.mp4` [17:15 – 17:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Світ влаштований так, що він щодня переконуватиме вас у вашій пересічності.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP01_VID_085_ACT4_24FPS_Architectural_Corridor_A4S10_Silhouett.mp4` [17:30 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Дивіться на проблеми як на код.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
086. `EP01_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [17:45 – 18:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Відкиньте емоційний шум.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP01_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:00 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Знайдіть рядок, де виник збій, перепишіть алгоритм і рухайтеся далі.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP01_VID_088_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [18:15 – 18:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо ваша щоденна справа не має накопичувального ефекту, ви просто обмінюєте свій час на виживання.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP01_VID_089_ACT4_24FPS_KeyScene_03_Compression_Diamond_Latt.mp4` [18:30 – 18:45 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Світ набагато пластичніший, ніж вам здається з дитинства.
     - *Veo Prompt:* `Slow majestic camera retreat from Earth into deep space constellation of satellites and data beams, poetic stillness, stars softly glowing, IMAX cinematic film look, 8k.`
090. `EP01_VID_090_ACT4_24FPS_Compression_Diamond_Lattice_Overhead_G.mp4` [18:45 – 19:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Світ набагато пластичніший, ніж вам здається з дитинства.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP01_VID_091_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [19:00 – 19:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його правила не викарбувані на скрижалях — вони написані такими ж самими людьми, як ви.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP01_VID_092_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S17_Silhou.mp4` [19:15 – 19:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І цей світ піддається волі тих, хто володіє сміливістю формулювати масштабні запитання і впертістю сидіти над кодом до четвертої ранку, поки система нарешті не ож…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP01_VID_093_ACT4_24FPS_Equation_Notebook_Macro_A4S18_SlowMo_I.mp4` [19:30 – 19:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Майбутнє не настає само собою.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
094. `EP01_VID_094_ACT4_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [19:45 – 20:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його створюють просто зараз.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP01_VID_095_ACT4_24FPS_Architectural_Corridor_A4S20_Anamorphi.mp4` [20:00 – 20:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP01_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:05 – 20:10 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP01_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [20:10 – 20:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP01_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [20:15 – 20:20 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP01_VID_099_ACT4_24FPS_Silicon_Light_Refraction_A4S24_Silhoue.mp4` [20:20 – 20:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP01_VID_100_ACT4_24FPS_Architectural_Corridor_A4S25_SlowMo_In.mp4` [20:25 – 20:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Анатомія експоненти
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring amber CRT phosphor glow, beige 1993 Macintosh chassis, cold slate boardroom glass, obsidian neural constellations, orbital Stargate solar arrays, shot on Panavision Primo Anamorphic 50mm & 100mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
