# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 10 — ЕНДРЮ ИН
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Вчитель світу та нова електрика»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP10 (Ендрю Ин) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP10.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP10_VO_, EP10_MUS_, EP10_AMB_, EP10_SFX_, EP10_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1358 слів, хронометраж 20:30 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP10_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP10_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP10_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP10_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP10_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP10_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP10_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP10_andrew_ng_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP10_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP10_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та освіта:** Народився у 1976 році у Великій Британії, дитинство та юність провів у Гонконзі та Сінгапурі (навчався у легендарній школі Raffles Institution). Здобув ступінь PhD у Каліфорнійському університеті в Берклі (2002).
* **Стенфорд та Google Brain:** Професор Стенфордського університету, керівник проєкту STAIR (Stanford AI Robot). У 2011 році заснував та очолив **Google Brain**, де реалізував знаменитий експеримент із розпізнаванням котів на базі 16 000 процесорів без попередньої розмітки.
* **Демократизація та Coursera:** Співзасновник **Coursera** (2011), відкривши доступ до найкращих світових курсів з машинного навчання для мільйонів студентів на планеті.
* **Baidu та Data-Centric AI:** Головний науковець китайського гіганта Baidu (2014–2017). Згодом заснував DeepLearning.AI, венчурну студію AI Fund і став головним ідеологом переходу від Model-Centric до **Data-Centric AI** (якість даних важливіша за архітектуру).
* **Місія:** «Штучний інтелект — це нова електрика». Послідовний будівельник інфраструктури, який вірить у те, що кожен може опанувати інструменти майбутнього.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ЕНДРЮ ИН)

1. [Філософія майбутнього] «Штучний інтелект — це нова електрика. Подібно до того, як електрика сто років тому трансформувала кожну галузь, ШІ сьогодні змінює суспільство».
2. [Походження та гарт] «У дитинстві в Сінгапурі я писав свої перші програми на мікрокомп'ютерах із журналів, мріючи про день, коли машини зможуть бачити і вчитися».
3. [Лідерство та екосистема] «Освіта має бути відкритою і доступною для кожної людини на Землі, незалежно від її географічного чи фінансового становища».
4. [Походження та гарт] «Коли ми створювали Coursera у 2011 році, наша мета була простою: дати можливість будь-якому підлітку в глибинці здобути освіту рівня найкращих університетів світу».
5. [Походження та гарт] «У Стенфорді ми завжди навчали студентів головного правилу: почніть із простих моделей, перевірте дані і лише потім будуйте складні архітектури».
6. [Архітектура та наука] «Експеримент Google Brain з розпізнаванням котів у 2011 році довів: неструктуровані дані з інтернету містять у собі закономірності, які мережа здатна знайти самостійно».
7. [Філософія майбутнього] «Ділитись знаннями — це найблагородніша інвестиція в майбутнє нашої цивілізації».
8. [Лідерство та екосистема] «Коли я очолював AI в Baidu, я бачив, як швидке впровадження технологій у традиційний бізнес змінює мільйони робочих процесів».
9. [Архітектура та наука] «Data-Centric AI — це парадигмальний зсув: замість того, щоб нескінченно крутити гіперпараметри моделі, зафіксуйте код і зосередьтеся на покращенні якості даних».
10. [Лідерство та екосистема] «Складний відсоток працює для людських знань точно так само, як і для капіталу: щодня вивчайте щось нове, і за рік ви станете іншою людиною».
11. [Філософія майбутнього] «ШІ не замінить людей, але люди, які використовують ШІ, замінять тих, хто його не використовує».
12. [Етика та безпека ШІ] «Кожен інженер має пам'ятати про етичну сторону своєї роботи: технології мають розширювати можливості людей, а не утискати їх».
13. [Лідерство та екосистема] «Мій перехід від академічних досліджень до створення масових освітніх платформ був усвідомленим кроком до демократизації знань».
14. [Походження та гарт] «Не бійтеся починати з нуля у новій сфері; цікавість і систематична праця долають будь-яку відстань».
15. [Лідерство та екосистема] «AI Fund створює компанії, які вирішують реальні прикладні проблеми у сфері охорони здоров'я, логістики та освіти».
16. [Філософія майбутнього] «Коли ми бачимо успіх наших випускників на DeepLearning.AI, ми розуміємо, що місія виконується щодня».
17. [Архітектура та наука] «Архітектура моделі вторинна порівняно з чистотою та розмірністю датасету, на якому вона навчається».
18. [Походження та гарт] «Сінгапурська школа заклала в мене міцний фундамент дисципліни, точності та поваги до точних наук».
19. [Походження та гарт] «Кожен новий студент, який написав свій перший рядок коду на Python, стає співавтором нашого спільного цифрового майбутнього».
20. [Лідерство та екосистема] «Ми маємо підготувати малий і середній бізнес до використання ШІ, інакше технологічна прірва стане занадто глибокою».
21. [Кризи та стійкість] «Коли криза ставить перед тобою стіну, розбий її на маленькі навчальні модулі і пройди їх крок за кроком».
22. [Архітектура та наука] «Найкращий спосіб навчитися будувати складні системи — це розібрати на деталі роботу простих базових алгоритмів».
23. [Філософія майбутнього] «Успіх у технологіях вимірюється не кількістю патентів у шухляді, а кількістю розв'язаних реальних проблем користувачів».
24. [Філософія майбутнього] «Ми створюємо інструменти, які знімають з людей рутину, вивільняючи час для творчості та спілкування».
25. [Походження та гарт] «Коли ми досліджували можливості робототехніки у Стенфорді (проєкт STAIR), ми зрозуміли, що роботам бракує здорового глузду».
26. [Філософія майбутнього] «Кожен день приносить нові можливості для інновацій, якщо ви зберігаєте гнучкість мислення».
27. [Етика та безпека ШІ] «Ми маємо відмовитися від страху перед новими технологіями через прозоре і зрозуміле навчання суспільства».
28. [Лідерство та екосистема] «Ефективність команди залежить від того, наскільки швидко її учасники можуть обмінюватися чесною конструктивною критикою».
29. [Філософія майбутнього] «Коли ти керуєш великою організацією, твоя головна задача — розчищати шлях для талановитих інженерів».
30. [Філософія майбутнього] «Машинне навчання є настільки потужним, що його принципи можуть покращити майже будь-яку наукову дисципліну».
31. [Лідерство та екосистема] «Коли ми запускали перші курси на Coursera, критики казали, що онлайн-освіта ніколи не замінить аудиторії. Вони помилилися».
32. [Філософія майбутнього] «Технологічний оптимізм має підкріплюватися щоденною наполегливою працею над якістю кожного продукту».
33. [Філософія майбутнього] «Коли ми працювали в Google Brain, ми поєднали величезні ресурси з духом вільного академічного пошуку».
34. [Лідерство та екосистема] «Немає нічого сильнішого за спільну пристрасть команди, яка вірить у те, що змінює світ на краще».
35. [Філософія майбутнього] «Ми маємо навчати роботів діяти в умовах неповних даних, спираючись на ймовірнісні моделі».
36. [Філософія майбутнього] «Коли ми говоримо про демократизацію ШІ, ми маємо на увазі створення інструментів, якими може користуватися кожен».
37. [Лідерство та екосистема] «Принципи Data-Centric AI економлять мільйони доларів і місяці роботи тисячам компаній у всьому світі».
38. [Походження та гарт] «Коли студент пише мені, що курс змінив його життя і допоміг знайти роботу, це надихає сильніше за будь-які нагороди».
39. [Кризи та стійкість] «Ми маємо підтримувати культуру експериментів, де право на помилку є частиною процесу пошуку істини».
40. [Лідерство та екосистема] «Коли технології розвиваються так стрімко, здатність до самоосвіти стає найціннішою навичкою XXI століття».
41. [Філософія майбутнього] «Кожен новий інструмент генеративного ШІ робить поріг входження в розробку нижчим для мільйонів людей».
42. [Філософія майбутнього] «Ми прагнемо побудувати екосистему, де венчурні інвестиції йдуть на користь корисним суспільним проєктам».
43. [Походження та гарт] «Коли ми аналізуємо ринки, ми шукаємо галузі, які застрягли в минулому і потребують термінової автоматизації».
44. [Архітектура та наука] «Справжній інноватор не чекає на досконалі умови; він бере наявні дані і будує першу працюючу версію».
45. [Етика та безпека ШІ] «Ми маємо виховувати відповідальних лідерів, які розуміють і комерційну, і соціальну цінність своєї праці».
46. [Лідерство та екосистема] «Коли ми заснували AI Fund, ми хотіли перетворити ідеї на робочі компанії за лічені тижні».
47. [Архітектура та наука] «Природа створила неймовірні механізми адаптації, які ми намагаємося відтворити в алгоритмах оптимізації».
48. [Походження та гарт] «Коли студент долає перші труднощі в математиці, у нього відкривається зовсім інше бачення власних сил».
49. [Філософія майбутнього] «Ми маємо зробити так, щоб переваги штучного інтелекту відчули не лише мегаполіси, а й найвіддаленіші куточки планети».
50. [Філософія майбутнього] «Кожен успішний проєкт починається з простої і чесної відповіді на запитання: яку проблему ми вирішуємо?».
51. [Походження та гарт] «Коли ми дивимося на розвиток індустрії, ми бачимо перехід від загального галасу до прагматичного вирішення завдань».
52. [Лідерство та екосистема] «Ми маємо поєднувати глибокі технічні знання з гнучкістю бізнес-мислення».
53. [Архітектура та наука] «Коли модель дає збій, ми не звинувачуємо алгоритм — ми йдемо перевіряти мітку в датасеті».
54. [Філософія майбутнього] «Свобода творчості в інженерії базується на міцному засвоєнні базових законів лінійної алгебри та статистики».
55. [Походження та гарт] «Коли ми створювали матеріали для DeepLearning.AI, ми прагнули зробити складну математику доступною для кожного».
56. [Філософія майбутнього] «Технології мають звільняти час для родини, спілкування та пізнання світу, а не перетворювати життя на офісне рабство».
57. [Походження та гарт] «Коли ми бачимо, як малий бізнес автоматизує рутину за допомогою ШІ, ми бачимо реальну користь нашої праці».
58. [Архітектура та наука] «Ми маємо бути відкритими до зворотного зв'язку і готовими змінювати курс щоразу, коли з'являються нові дані».
59. [Кризи та стійкість] «Коли інженер закохується в ідею, а не в проблему клієнта, проєкт приречений на провал».
60. [Філософія майбутнього] «Ми прагнемо створити світ, де кожен може стати творцем власних технологічних рішень».
61. [Філософія майбутнього] «Коли ми аналізуємо ефективність навчання, ми бачимо, що короткі практичні проєкти працюють краще за довгі лекції».
62. [Кризи та стійкість] «Кожен новий рік роботи в ШІ приносить більше змін, ніж попереднє десятиліття».
63. [Філософія майбутнього] «Ми маємо навчати моделі не просто відповідати, а перевіряти достовірність власних джерел».
64. [Походження та гарт] «Коли ми об'єднуємо зусилля з іншими викладачами, ми створюємо глобальний університет майбутнього».
65. [Філософія майбутнього] «Істинна цінність платформ на кшталт Coursera полягає у зміні доль мільйонів людей через знання».
66. [Філософія майбутнього] «Коли ми працювали над розпізнаванням об'єктів, ми розуміли межі того, що може зробити комп'ютерний зір».
67. [Філософія майбутнього] «Ми маємо розвивати інтуїцію щодо даних, бо жодна формула не замінить досвіду роботи з реальними масивами».
68. [Філософія майбутнього] «Коли ми підтримуємо підприємців через AI Fund, ми допомагаємо їм пройти найскладніший нульовий етап».
69. [Філософія майбутнього] «Технологічний прогрес є неминучим, але його напрямок визначаємо ми своєю щоденною працею».
70. [Походження та гарт] «Коли студент розуміє суть градієнтного спуску, перед ним відкривається магія всього машинного навчання».
71. [Архітектура та наука] «Ми маємо прагнути до простоти в коді і прозорості в комунікації з командою».
72. [Архітектура та наука] «Коли ми запускали нові курси, ми завжди тестували їх на людях, які ніколи раніше не кодили».
73. [Архітектура та наука] «Принципи Data-Centric AI дозволяють економити ресурси планети завдяки ефективній роботі з меншими датасетами».
74. [Лідерство та екосистема] «Коли ми дивимося на майбутнє, ми бачимо глибоку інтеграцію ШІ в усі освітні стандарти світу».
75. [Філософія майбутнього] «Ми маємо захищати приватність користувачів і будувати безпечні системи з першого дня розробки».
76. [Кризи та стійкість] «Коли інженер фокусується на головному, він встигає зробити за місяць більше, ніж інші за рік».
77. [Філософія майбутнього] «Ми віримо у світ, де технологічний бар'єр між людьми стає мінімальним завдяки зручним інтерфейсам».
78. [Філософія майбутнього] «Коли ми вивчали нейрони у Берклі, ми закладали основу для нашого сьогоднішнього розуміння архітектур».
79. [Лідерство та екосистема] «Кожен успішний лідер колись був новачком, який боявся запитати про очевидні речі».
80. [Лідерство та екосистема] «Ми маємо підтримувати культуру постійного оновлення знань усередині кожної компанії».
81. [Архітектура та наука] «Коли ми створювали Google Brain, ми довели, що масштаб обчислень здатний творити дива».
82. [Філософія майбутнього] «Технології мають служити містком між різними культурами та економіками світу».
83. [Кризи та стійкість] «Коли модель працює стабільно на тестах, але падає в продакшені — шукайте розбіжність у даних».
84. [Філософія майбутнього] «Ми маємо виховувати покоління творців, які не бояться глобальних викликів».
85. [Філософія майбутнього] «Коли ти бачиш гарячі очі слухачів у залі, ти розумієш силу натхненного слова».
86. [Етика та безпека ШІ] «Ми прагнемо побудувати інфраструктуру, яка прискорить перехід людства до сталого розвитку».
87. [Філософія майбутнього] «Коли закони інформації зустрічаються з підприємництвом, народжуються нові глобальні ринки».
88. [Філософія майбутнього] «Ми маємо поважати час користувачів і створювати швидкі, надійні та корисні рішення».
89. [Філософія майбутнього] «Коли ми аналізуємо тенденції, ми бачимо, що майбутнє належить тим, хто швидко адаптується».
90. [Кризи та стійкість] «Кожен рядок якісного коду — це внесок у стабільність нашого спільного цифрового простору».
91. [Філософія майбутнього] «Ми маємо захищати авторські права та чесну винагороду для творців контенту в епоху ШІ».
92. [Лідерство та екосистема] «Коли ми створюємо венчурні компанії, ми шукаємо команду з бездоганною чесністю та енергією».
93. [Філософія майбутнього] «Технологічний підйом вимагає від нас мудрості у розподілі багатств і благ».
94. [Походження та гарт] «Коли студент долає страх перед штучним інтелектом, він стає архіпелагом нових можливостей».
95. [Філософія майбутнього] «Ми маємо прагнути до досконалості в продуктах, не забуваючи про турботу одне про одного».
96. [Лідерство та екосистема] «Коли ми дивимося на нові горизонти, ми знаємо, що найкращі відкриття ще попереду».
97. [Походження та гарт] «Ми створюємо фундамент для епохи, де кожна людина матиме персонального штучного помічника».
98. [Філософія майбутнього] «Кожен день роботи з даними нагадує мені про неймовірну складність та красу реального світу».
99. [Кризи та стійкість] «Ми маємо ділитися знаннями відкрито, бо ізоляція вбиває будь-яку інновацію».
100. [Лідерство та екосистема] «Усе починається з маленького курсу, однієї мрії і людини, яка повірила, що може змінити своє життя».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1358 слів): `02_SCRIPTS/episode_10_ng/director_script_ng.md`*

### АКТ 1. Сінгапурські журнали та Берклі (0:00 – 4:45)
*Музика: Suno Pro — `EP10_MUS_01_ACT1_92BPM_Raffles_Code.wav`*
* **0:00 - 0:25** | [SFX: Теплий акустичний перебір гітари, м'який гул клавіатури] | **Диктор:** Деякі люди створюють технології заради закритих кабінетів, а інші — заради того, щоб кожен на планеті зміг ними скористатися. Ендрю Ин обрав шлях просвітника і будівничого.
* **0:25 - 2:30** |  | **Диктор:** Дитинство в Гонконзі та Сінгапурі. Перші програми з комп'ютерних журналів. Навчання в Raffles Institution та захист PhD у Берклі у 2002 році.
* **2:30 - 4:45** | [VIDEO: `EP10_VID_01_Singapore_Library.txt`] | **Диктор:** Початок викладацької кар'єри та глибоке переконання: складні алгоритми мають бути простими для розуміння кожної людини.

### АКТ 2. Стенфорд, Google Brain і експеримент із котами (4:45 – 9:30)
*Музика: Suno Pro — `EP10_MUS_05_ACT2_92BPM_Google_Cat.wav`*
* **4:45 - 7:00** |  | **Диктор:** Робота у Стенфорді та заснування проєкту STAIR. У 2011 році він створює та очолює Google Brain.
* **7:00 - 9:30** | [SFX: Мережевий імпульс дата-центру] | **Диктор:** Легендарний експеримент: 16 000 процесорів дивляться мільйони відео на YouTube і самі, без розмітки, вчаться розпізнавати котів. Епоха великих нейромереж починається.

### АКТ 3. Coursera, демократизація та Baidu (9:30 – 15:00)
*Музика: Suno Pro — `EP10_MUS_09_ACT3_92BPM_Coursera_Mission.wav`*
* **9:30 - 12:15** |  | **Диктор:** Співзаснування Coursera у 2011 році. Мільйони студентів одночасно відкривають для себе машинне навчання. Перехід на посаду головного науковця в Baidu (2014–2017).
* **12:15 - 15:00** |  | **Диктор:** Популяризація індустрії в Китаї та світі. Створення DeepLearning.AI — глобального центру підготовки інженерів нового покоління.

### АКТ 4. Data-Centric AI, AI Fund і кодекс будівничого (15:00 – 20:30)
*Музика: Suno Pro — `EP10_MUS_13_ACT4_92BPM_DataCentric_Future.wav`*
* **15:00 - 18:00** |  | **Диктор:** Революційний заклик до **Data-Centric AI**: фіксуйте код моделей, поліпшуйте якість даних. Заснування венчурної студії AI Fund для швидкого перетворення ідей на бізнес.
* **18:30 - 20:30** | [SFX: Теплий фінальний акорд, що переходить у тишу] | **Диктор:** *«Штучний інтелект — це нова електрика. Він трансформує кожну галузь людської діяльності. І кожен із нас може стати творцем цього майбутнього»*.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP10_MUS_01_ACT1_92BPM_Raffles_Code.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Raffles Code', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP10_AMB_02_ACT1_DRONE_Singapore_Morning.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Singapore Morning', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP10_MUS_03_ACT1_92BPM_Berkeley_Campus.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Berkeley Campus', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP10_MUS_04_ACT1_92BPM_Stair_Robotics.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Stair Robotics', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP10_MUS_05_ACT2_92BPM_Google_Cat.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Google Cat', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP10_MUS_06_ACT2_92BPM_Brain_Clusters.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Brain Clusters', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP10_AMB_07_ACT2_DRONE_Cluster_Hum.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Cluster Hum', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP10_MUS_08_ACT2_92BPM_Unsupervised_Learning.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Unsupervised Learning', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP10_MUS_09_ACT3_92BPM_Coursera_Mission.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Coursera Mission', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP10_AMB_10_ACT3_DRONE_Online_Students.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Online Students', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP10_MUS_11_ACT3_92BPM_Baidu_Chief_Scientist.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Baidu Chief Scientist', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP10_MUS_12_ACT3_92BPM_DeepLearning_AI.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'DeepLearning AI', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP10_MUS_13_ACT4_92BPM_DataCentric_Future.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'DataCentric Future', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP10_MUS_14_ACT4_92BPM_AI_Fund_Ventures.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'AI Fund Ventures', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP10_MUS_15_ACT4_92BPM_Builder_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental inspiring global downtempo, 92 bpm, warm acoustic guitar harmonics, steady analog sub-bass groove, soaring strings, uplifting season-finale clarity, cue theme 'Builder Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP10_SFX_16_GLOBAL_AcousticGuitar_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP10_VO_UA_01_ACT1_Singapore_And_Berkeley.wav` | `EP10_VO_EN_01_ACT1_Singapore_And_Berkeley.wav` (ACT1 — Singapore And Berkeley)
* `EP10_VO_UA_02_ACT1_Democratizing_Knowledge.wav` | `EP10_VO_EN_02_ACT1_Democratizing_Knowledge.wav` (ACT1 — Democratizing Knowledge)
* `EP10_VO_UA_03_ACT2_Google_Brain_Genesis.wav` | `EP10_VO_EN_03_ACT2_Google_Brain_Genesis.wav` (ACT2 — Google Brain Genesis)
* `EP10_VO_UA_04_ACT2_The_Cat_Experiment.wav` | `EP10_VO_EN_04_ACT2_The_Cat_Experiment.wav` (ACT2 — The Cat Experiment)
* `EP10_VO_UA_05_ACT3_Coursera_Revolution.wav` | `EP10_VO_EN_05_ACT3_Coursera_Revolution.wav` (ACT3 — Coursera Revolution)
* `EP10_VO_UA_06_ACT3_Baidu_Leadership.wav` | `EP10_VO_EN_06_ACT3_Baidu_Leadership.wav` (ACT3 — Baidu Leadership)
* `EP10_VO_UA_07_ACT4_Data_Centric_Paradigm.wav` | `EP10_VO_EN_07_ACT4_Data_Centric_Paradigm.wav` (ACT4 — Data Centric Paradigm)
* `EP10_VO_UA_08_ACT4_New_Electricity.wav` | `EP10_VO_EN_08_ACT4_New_Electricity.wav` (ACT4 — New Electricity)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP10_VID_001_ACT1_24FPS_Singapore_Library.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* У стародавніх міфах Прометей викрав вогонь у богів Олімпу не для того, щоб замкнути його у своєму палаці — він роздав його простим людям, щоб у кожній хатині було…
     - *Veo Prompt:* `Cinematic wide shot of a bright modern university library in Singapore, students collaborating around glowing laptops, warm tropical sunlight streaming through large glass windows, 35mm film grain, 4k 24fps.`
002. `EP10_VID_002_ACT1_24FPS_Data_Cleaning.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* У стародавніх міфах Прометей викрав вогонь у богів Олімпу не для того, щоб замкнути його у своєму палаці — він роздав його простим людям, щоб у кожній хатині було…
     - *Veo Prompt:* `An interactive holographic data matrix where messy chaotic pixels are cleanly aligned and labeled with golden vectors by a precision algorithm, 8k.`
003. `EP10_VID_003_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом дев'яти епізодів ми бачили, як титани нашої епохи викували божественний вогонь штучного інтелекту у закритих лабораторіях.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP10_VID_004_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом дев'яти епізодів ми бачили, як титани нашої епохи викували божественний вогонь штучного інтелекту у закритих лабораторіях.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP10_VID_005_ACT1_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але ця революція залишилася б привілеєм жменьки обраних мільярдерів, якби не одна людина в простій блакитній сорочці, яка відчинила ворота Стенфорду і роздала цей…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP10_VID_006_ACT1_24FPS_University_Archive_Hall_Macro_Detail.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але ця революція залишилася б привілеєм жменьки обраних мільярдерів, якби не одна людина в простій блакитній сорочці, яка відчинила ворота Стенфорду і роздала цей…
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP10_VID_007_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його звуть Ендрю Ин.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP10_VID_008_ACT1_24FPS_KeyScene_02_London_Tournament_Chessb.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Він народився у Лондоні 1976 року в родині іммігрантів із Гонконгу, а дитинство й юність провів між Гонконгом та Сінгапуром.
     - *Veo Prompt:* `1984 Hong Kong and Singapore montage: a doctor father showing his young son a medical textbook on expert diagnostic systems, tropical sunlight streaming through wooden shutters, warm nostalgic film aesthetic, 4k.`
009. `EP10_VID_009_ACT1_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [00:38 – 00:52 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його батько, Рональд Ин, був лікарем-гематологом, який вечорами читав медичні журнали й намагався написати просту комп'ютерну програму для діагностики хвороб леге…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP10_VID_010_ACT1_24FPS_Silicon_Light_Refraction_A1S10_Optical.mp4` [00:52 – 01:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хлопчик сидів поруч і дивився, як батько перекладає людський досвід мовою умовних операторів.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP10_VID_011_ACT1_24FPS_School_Auditorium_Stage_Silhouette_Moo.mp4` [01:05 – 01:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У легендарній сінгапурській школі Raffles Institution Ендрю проводив години в бібліотеці, вручну передруковуючи лістинги на BASIC із пожовклих журналів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP10_VID_012_ACT1_24FPS_Neural_Horizon_Pulse_A1S12_SlowMo_Inse.mp4` [01:18 – 01:32 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Кожна пропущена кома ламала програму — і це виховувало майже хірургічну повагу до точності.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP10_VID_013_ACT1_24FPS_Planetary_Electricity_Grid_Macro_Detai.mp4` [01:32 – 01:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* «У дитинстві в Сінгапурі я писав свої перші програми з журналів, мріючи про день, коли машини зможуть бачити і навчатися самостійно, звільняючи людей від рутинної…
     - *Veo Prompt:* `Extreme macro push-in shot of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP10_VID_014_ACT1_24FPS_KeyScene_03_Seoul_Move_37_Go_Stone.mp4` [01:45 – 02:00 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Його академічна траєкторія нагадувала ракету з трьома ступенями прискорення: потрійний диплом у Карнегі-Меллон з інформатики, статистики й економіки, магістратура…
     - *Veo Prompt:* `Cinematic architectural tracking shot through Carnegie Mellon and MIT robotic labs in late 1990s, tangled servo wires, early robotic arms hesitating before picking up a coffee mug, moody tungsten lab lighting, 35mm Kodak 2383 look, 4k 24fps.`
015. `EP10_VID_015_ACT1_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [02:00 – 02:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його академічна траєкторія нагадувала ракету з трьома ступенями прискорення: потрійний диплом у Карнегі-Меллон з інформатики, статистики й економіки, магістратура…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP10_VID_016_ACT1_24FPS_University_Archive_Hall_Overhead_GodsE.mp4` [02:15 – 02:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У Берклі двадцятичотирирічний аспірант береться за задачу, яку авіаконструктори вважали майже самогубною для алгоритму — навчити радіокерований гелікоптер літати…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP10_VID_017_ACT1_24FPS_Neural_Horizon_Pulse_A1S17_Optical_Dat.mp4` [02:30 – 02:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Звичайний літак прагне стабільності: відпусти штурвал — і крила вирівняють потік.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP10_VID_018_ACT1_24FPS_Planetary_Electricity_Grid_Silhouette.mp4` [02:45 – 03:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Гелікоптер — це фізична нестабільність у чистому вигляді.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP10_VID_019_ACT1_24FPS_Equation_Notebook_Macro_A1S19_SlowMo_I.mp4` [03:00 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він щосекунди намагається перекинутися й впасти, мов куля на вістрі голки.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP10_VID_020_ACT1_24FPS_KeyScene_04_University_Archive_Hall.mp4` [03:15 – 03:35 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Ставши наймолодшим професором Стенфорду у двадцять шість років, Ин доводить цей експеримент до межі фантастики.
     - *Veo Prompt:* `Dramatic slow-motion wide shot over golden Stanford hills at sunset: an autonomous RC helicopter flying upside-down inches above dry grass, rotor blades slicing volumetric golden dust, researchers watching in breathless silence, IMAX 4k 24fps.`
021. `EP10_VID_021_ACT1_24FPS_University_Archive_Hall_Anamorphic_Wid.mp4` [03:35 – 03:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ставши наймолодшим професором Стенфорду у двадцять шість років, Ин доводить цей експеримент до межі фантастики.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP10_VID_022_ACT1_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [03:55 – 04:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Замість того, щоб писати тисячі рядків рівнянь аеродинаміки вручну, його команда записує рухи живого пілота-віртуоза і запускає навчання з підкріпленням (Reinforc…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP10_VID_023_ACT1_24FPS_University_Archive_Hall_Overhead_GodsE.mp4` [04:15 – 04:35 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На пагорбах за кампусом Стенфорду машина піднімається в небо, перевертається гвинтом униз і зависає за метр від землі, виконуючи фігури вищого пілотажу, які під с…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP10_VID_024_ACT1_24FPS_University_Archive_Hall_Optical_DataVi.mp4` [04:35 – 04:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Паралельно він запускає проєкт STAIR — Стенфордського домашнього робота, серед перших студентів якого працює зовсім юний Сем Альтман.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP10_VID_025_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [04:55 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме тоді Ендрю Ин формулює головний висновок першої половини свого життя: вузьке місце штучного інтелекту лежить не в залізі сервоприводів, а в масштабі самого м…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP10_VID_026_ACT2_24FPS_KeyScene_01_Menlo_Park_Evening_Table.mp4` [05:15 – 05:25 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* До 2010 року під час рідкісних зустрічей із Джеффрі Хінтоном та Іллею Суцкевером Ендрю Ин остаточно переконується у головній гіпотезі: старі алгоритми впираються…
     - *Veo Prompt:* `Infinite dark corridor of Google data center in 2011, thousands of blinking cyan and amber fiber-optic LEDs stretching into perspective vanishing point, cool volumetric mist, anamorphic lens flare, 4k 24fps.`
027. `EP10_VID_027_ACT2_24FPS_Menlo_Park_Evening_Table_Anamorphic_Wi.mp4` [05:25 – 05:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* До 2010 року під час рідкісних зустрічей із Джеффрі Хінтоном та Іллею Суцкевером Ендрю Ин остаточно переконується у головній гіпотезі: старі алгоритми впираються…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP10_VID_028_ACT2_24FPS_Menlo_Park_Evening_Table_Tracking_Medi.mp4` [05:35 – 05:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* До 2010 року під час рідкісних зустрічей із Джеффрі Хінтоном та Іллею Суцкевером Ендрю Ин остаточно переконується у головній гіпотезі: старі алгоритми впираються…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP10_VID_029_ACT2_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [05:45 – 05:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але де в університеті взяти суперкомп'ютер такого масштабу?
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP10_VID_030_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [05:55 – 06:05 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але де в університеті взяти суперкомп'ютер такого масштабу?
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP10_VID_031_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S06_Silhou.mp4` [06:05 – 06:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2011 році Ин приходить у секретну лабораторію Google X у Маунтін-В'ю і об'єднує зусилля з легендарним архітектором розподілених систем Джеффом Діном.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP10_VID_032_ACT2_24FPS_Equation_Notebook_Macro_A2S07_SlowMo_I.mp4` [06:15 – 06:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2011 році Ин приходить у секретну лабораторію Google X у Маунтін-В'ю і об'єднує зусилля з легендарним архітектором розподілених систем Джеффом Діном.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP10_VID_033_ACT2_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [06:25 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Так народжується Google Brain — проєкт, якому судилося назавжди перетворити пошукову корпорацію на імперію штучного інтелекту.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP10_VID_034_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [06:35 – 06:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Так народжується Google Brain — проєкт, якому судилося назавжди перетворити пошукову корпорацію на імперію штучного інтелекту.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP10_VID_035_ACT2_24FPS_KeyScene_02_Hyperscale_Compute_Clust.mp4` [06:45 – 06:58 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У Google ще не було спеціалізованих кластерів GPU для глибокого навчання.
     - *Veo Prompt:* `Macro visualization of 1,000 server motherboards linked by glowing optical filaments, 16,000 CPU cores pulsing in synchronized 92 BPM wave, dark obsidian aesthetic, Octane render, 8k.`
036. `EP10_VID_036_ACT2_24FPS_Hyperscale_Compute_Cluster_Overhead_Go.mp4` [06:58 – 07:11 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У Google ще не було спеціалізованих кластерів GPU для глибокого навчання.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP10_VID_037_ACT2_24FPS_Hyperscale_Compute_Cluster_Optical_Dat.mp4` [07:11 – 07:24 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тому Ин і Дін роблять хід чистої інженерної зухвалості: вони з'єднують у єдину нейронну мережу тисячу звичайних серверів — шістнадцять тисяч процесорних ядер.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP10_VID_038_ACT2_24FPS_Hyperscale_Compute_Cluster_Silhouette.mp4` [07:24 – 07:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тоді вони ставлять експеримент, який нагадував питання з дитячої філософії: що станеться, якщо підключити новонароджений цифровий мозок із мільярдом зв'язків пр…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP10_VID_039_ACT2_24FPS_Architectural_Corridor_A2S14_SlowMo_In.mp4` [07:38 – 07:51 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жодної мітки.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP10_VID_040_ACT2_24FPS_Neural_Horizon_Pulse_A2S15_Macro_Detai.mp4` [07:51 – 08:04 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жодної мітки.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP10_VID_041_ACT2_24FPS_Boardroom_Fracture_Night_Anamorphic_Wi.mp4` [08:04 – 08:17 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жодного підпису «це людина», «це автомобіль», «це будинок».
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP10_VID_042_ACT2_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [08:17 – 08:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом тижня шістнадцять тисяч ядер мовчки вдивляються у десять мільйонів кадрів людського життя.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP10_VID_043_ACT2_24FPS_KeyScene_03_Monastic_White_Sanctuary.mp4` [08:30 – 08:47 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли дослідники відкрили візуалізацію окремих нейронів у верхніх шарах мережі, у лабораторії запала мертва тиша.
     - *Veo Prompt:* `Hauntingly poetic visualization on a dark lab monitor: out of blurry silver static and millions of shifting video frames, a ghostly luminous mathematical reconstruction of a cat's face emerges from pure neural weights, scientist glasses reflecting the glow, 35mm film grain, 4k 24fps.`
044. `EP10_VID_044_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [08:47 – 09:04 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На темному екрані монітора, немов привид із чистої статистики, проступило розмите, але безпомилково впізнаване обличчя кота.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP10_VID_045_ACT2_24FPS_Neural_Horizon_Pulse_A2S20_Silhouette.mp4` [09:04 – 09:21 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Машині ніхто ніколи не казав, що коти взагалі існують у природі.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP10_VID_046_ACT2_24FPS_Visual_Cortex_Convolution_SlowMo_Inser.mp4` [09:21 – 09:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вона самостійно винайшла поняття «кіт»
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP10_VID_047_ACT2_24FPS_Equation_Notebook_Macro_A2S22_Macro_De.mp4` [09:38 – 09:54 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* із хаосу світла й тіні — точно так само, як це робить немовля у колисці.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP10_VID_048_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [09:54 – 10:11 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Наступного ранку стаття на першій шпальті The New York Times облетіла весь світ.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP10_VID_049_ACT2_24FPS_Architectural_Corridor_A2S24_Tracking.mp4` [10:11 – 10:28 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* «Експеримент Google Brain довів фундаментальну річ: необроблений світ навколо нас переповнений закономірностями, і достатньо велика нейромережа здатна самостійно…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP10_VID_050_ACT2_24FPS_Dennys_Midnight_Booth_Overhead_GodsEye.mp4` [10:28 – 10:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але в момент, коли корпорації кинулися скуповувати всіх вчених планети за мільйонні контракти, Ендрю Ин робить розворот, якого від нього не чекав ніхто.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP10_VID_051_ACT3_24FPS_KeyScene_01_University_Archive_Hall.mp4` [10:45 – 10:57 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Щороку в аудиторію Стенфордського університету на його знаменитий курс машинного навчання CS229 приходило чотириста студентів.
     - *Veo Prompt:* `Intimate night shot of a modest home study in Palo Alto, 2011: a professor in a simple blue button-down shirt speaking warmly into a small webcam while drawing gradient descent curves with a stylus on a glowing tablet, warm desk lamp, 35mm film grain, 4k 24fps.`
052. `EP10_VID_052_ACT3_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [10:57 – 11:08 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щороку в аудиторію Стенфордського університету на його знаменитий курс машинного навчання CS229 приходило чотириста студентів.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP10_VID_053_ACT3_24FPS_University_Archive_Hall_Macro_Detail.mp4` [11:08 – 11:20 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ендрю розумів гірку несправедливість елітної освіти: за стінами цієї аудиторії у Лагосі, Києві, Бангалорі, Сан-Паулу та Манілі живуть мільйони таких самих таланов…
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP10_VID_054_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S04_Anamor.mp4` [11:20 – 11:32 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Влітку 2011 року він ставить у маленькій кімнаті звичайну камеру, вмикає планшет і простою, кришталево чесною мовою — не ховаючись за академічним снобізмом — запи…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP10_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [11:32 – 11:43 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Влітку 2011 року він ставить у маленькій кімнаті звичайну камеру, вмикає планшет і простою, кришталево чесною мовою — не ховаючись за академічним снобізмом — запи…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP10_VID_056_ACT3_24FPS_Silicon_Light_Refraction_A3S06_Overhea.mp4` [11:43 – 11:55 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Каже друзям: можливо, збереться кілька тисяч слухачів.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP10_VID_057_ACT3_24FPS_Architectural_Corridor_A3S07_Optical_D.mp4` [11:55 – 12:07 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За кілька тижнів лічильник реєстрацій перетинає позначку 104 000 студентів.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP10_VID_058_ACT3_24FPS_Neural_Horizon_Pulse_A3S08_Silhouette.mp4` [12:07 – 12:18 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За кілька тижнів лічильник реєстрацій перетинає позначку 104 000 студентів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP10_VID_059_ACT3_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [12:18 – 12:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Одна людина з маркером у руці за одне літо навчила стільки людей, скільки в Стенфорді він би навчав двісті п'ятдесят років поспіль.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP10_VID_060_ACT3_24FPS_KeyScene_02_University_Archive_Hall.mp4` [12:30 – 12:45 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Разом із колегою по Стенфорду Дафною Коллер він засновує Coursera, а згодом — DeepLearning.AI.
     - *Veo Prompt:* `Breathtaking orbital view of Earth at night: starting from a single warm point of light in California, millions of tiny golden filaments ignite across South America, Europe, Ukraine, Africa, India, and Asia, forming a planetary neural network of learners, IMAX 8k.`
061. `EP10_VID_061_ACT3_24FPS_University_Archive_Hall_Anamorphic_Wid.mp4` [12:45 – 13:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Разом із колегою по Стенфорду Дафною Коллер він засновує Coursera, а згодом — DeepLearning.AI.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP10_VID_062_ACT3_24FPS_Startup_Night_Workspace_Tracking_Mediu.mp4` [13:00 – 13:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Більшість сучасних інженерів штучного інтелекту на планеті — від стартапів Кремнієвої долини до провідних дослідницьких центрів Європи та Азії — починали свій шля…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP10_VID_063_ACT3_24FPS_Startup_Night_Workspace_Overhead_GodsE.mp4` [13:15 – 13:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Більшість сучасних інженерів штучного інтелекту на планеті — від стартапів Кремнієвої долини до провідних дослідницьких центрів Європи та Азії — починали свій шля…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP10_VID_064_ACT3_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він зняв зі штучного інтелекту мантію жрецького культу.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP10_VID_065_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [13:45 – 14:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він зняв зі штучного інтелекту мантію жрецького культу.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP10_VID_066_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [14:00 – 14:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І в 2014 році вирушив у Пекін на посаду головного науковця технологічного гіганта Baidu, де під його керівництвом команда з тисячі трьохсот дослідників за три рок…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP10_VID_067_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [14:15 – 14:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І в 2014 році вирушив у Пекін на посаду головного науковця технологічного гіганта Baidu, де під його керівництвом команда з тисячі трьохсот дослідників за три рок…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP10_VID_068_ACT3_24FPS_KeyScene_03_Seoul_Move_37_Go_Stone.mp4` [14:30 – 14:43 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Саме на перетині Сходу і Заходу, академії та важкої індустрії він формулює головну історичну метафору двадцять першого століття:

«Штучний інтелект — це нова елек…
     - *Veo Prompt:* `Cinematic split-epoch metamorphosis: 1890s Edison incandescent filament igniting in dark glass bulb seamlessly morphing into a modern glowing silicon AI tensor core illuminating a vast smart factory and hospital, Kodak 2383 film look, 4k 24fps.`
069. `EP10_VID_069_ACT3_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [14:43 – 14:56 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме на перетині Сходу і Заходу, академії та важкої індустрії він формулює головну історичну метафору двадцять першого століття:

«Штучний інтелект — це нова елек…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP10_VID_070_ACT3_24FPS_Planetary_Electricity_Grid_Overhead_Go.mp4` [14:56 – 15:09 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сто років тому електрика трансформувала кожну галузь один за одним — сільське господарство, медицину, транспорт, зв'язок.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP10_VID_071_ACT3_24FPS_Planetary_Electricity_Grid_Optical_Dat.mp4` [15:09 – 15:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сто років тому електрика трансформувала кожну галузь один за одним — сільське господарство, медицину, транспорт, зв'язок.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP10_VID_072_ACT3_24FPS_Architectural_Corridor_A3S22_Silhouett.mp4` [15:22 – 15:36 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні на наших очах те саме робить штучний інтелект».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP10_VID_073_ACT3_24FPS_Neural_Horizon_Pulse_A3S23_SlowMo_Inse.mp4` [15:36 – 15:49 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні на наших очах те саме робить штучний інтелект».
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP10_VID_074_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [15:49 – 16:02 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки медіа лякали суспільство термінаторами, а філософи сперечалися про душу в кремнії, Ендрю Ин дивився на ШІ очима головного електрика цивілізації: де провести…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP10_VID_075_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [16:02 – 16:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки медіа лякали суспільство термінаторами, а філософи сперечалися про душу в кремнії, Ендрю Ин дивився на ШІ очима головного електрика цивілізації: де провести…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP10_VID_076_ACT4_24FPS_KeyScene_01_Neural_Horizon_Pulse_A4S.mp4` [16:15 – 16:27 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Повернувшись до Пало-Альто та заснувавши венчурну студію AI Fund, Ин помічає небезпечну хворобу сучасної науки: всі одержимі гонитвою за дедалі гігантськішими арх…
     - *Veo Prompt:* `Precision industrial macro shot: a robotic optical inspection camera scanning tiny steel parts on a small factory line, chaotic red noise vectors transforming into clean aligned golden bounding boxes on a transparent HUD, 4k 24fps.`
077. `EP10_VID_077_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S02_Optica.mp4` [16:27 – 16:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Повернувшись до Пало-Альто та заснувавши венчурну студію AI Fund, Ин помічає небезпечну хворобу сучасної науки: всі одержимі гонитвою за дедалі гігантськішими арх…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP10_VID_078_ACT4_24FPS_Hyperscale_Compute_Cluster_Silhouette.mp4` [16:38 – 16:50 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На заводі сталевих деталей немає мільярда фотографій дефектів — їх там лише п'ятдесят.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP10_VID_079_ACT4_24FPS_Silicon_Light_Refraction_A4S04_SlowMo.mp4` [16:50 – 17:02 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У сільській клініці немає мільйона рентгенівських знімків рідкісної пухлини.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP10_VID_080_ACT4_24FPS_Architectural_Corridor_A4S05_Macro_Det.mp4` [17:02 – 17:13 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У сільській клініці немає мільйона рентгенівських знімків рідкісної пухлини.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP10_VID_081_ACT4_24FPS_DryCleaner_Steam_Window_Anamorphic_Wid.mp4` [17:13 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Так він проголошує хрестовий похід Data-Centric AI — інженерії, зосередженої на даних:

«Перестаньте безкінечно крутити гіперпараметри коду.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of clouds of backlit white steam rising from a heavy garment press against a rain-streaked New Jersey shopfront, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP10_VID_082_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S07_Tracki.mp4` [17:25 – 17:37 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Зафіксуйте модель і з любовною інженерною ретельністю вичистіть свої дані.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP10_VID_083_ACT4_24FPS_Equation_Notebook_Macro_A4S08_Overhead.mp4` [17:37 – 17:48 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Зафіксуйте модель і з любовною інженерною ретельністю вичистіть свої дані.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP10_VID_084_ACT4_24FPS_Upwind_Atlantic_Sail_Optical_DataViz.mp4` [17:48 – 18:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Чиста крапля істини сильніша за океан шуму».
     - *Veo Prompt:* `Photorealistic scientific optical visualization of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP10_VID_085_ACT4_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [18:00 – 18:13 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли ж у середині двадцятих років індустрію охоплює нова хвиля страху — цього разу спроба закритих монополій переконати уряди, ніби відкритий код штучного інтелек…
     - *Veo Prompt:* `Elegant abstract architectural space: four glowing translucent glass prisms arranged in a feedback loop passing a beam of golden light back and forth, each reflection sharpening the beam into laser perfection, dark slate studio, 8k.`
086. `EP10_VID_086_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [18:13 – 18:26 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли ж у середині двадцятих років індустрію охоплює нова хвиля страху — цього разу спроба закритих монополій переконати уряди, ніби відкритий код штучного інтелек…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP10_VID_087_ACT4_24FPS_Carpenter_Oak_Workbench_Macro_Detail.mp4` [18:26 – 18:39 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Разом із Яном Лекуном він публічно викриває регуляторне захоплення ринку: заборонити відкриті ваги моделей означає спалити сучасний друкарський верстат Гутенберга.
     - *Veo Prompt:* `Extreme macro push-in shot of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP10_VID_088_ACT4_24FPS_Carpenter_Oak_Workbench_Anamorphic_Wid.mp4` [18:39 – 18:52 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Разом із Яном Лекуном він публічно викриває регуляторне захоплення ринку: заборонити відкриті ваги моделей означає спалити сучасний друкарський верстат Гутенберга.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP10_VID_089_ACT4_24FPS_Upwind_Atlantic_Sail_Tracking_Medium.mp4` [18:52 – 19:06 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Більше того, він демонструє елегантну концепцію Agentic Workflows — агентних робочих процесів: навіть невелика відкрита модель, якій дали право не видавати першу…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP10_VID_090_ACT4_24FPS_Constitutional_Crystal_Box_Overhead_Go.mp4` [19:06 – 19:19 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мислення — це не миттєвий спалах оракула.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP10_VID_091_ACT4_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [19:19 – 19:32 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мислення — це не миттєвий спалах оракула.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP10_VID_092_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S17_Silhou.mp4` [19:32 – 19:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мислення — це терпляча ітерація.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP10_VID_093_ACT4_24FPS_KeyScene_03_Seoul_Move_37_Go_Stone.mp4` [19:45 – 19:58 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Озираючись на всю галерею десяти архітекторів розуму — від експоненти Альтмана і кремнієвої кузні Хуанга до біологічного коду Гассабіса, пророчого болю Хінтона, к…
     - *Veo Prompt:* `Final season-closing shot: a teenager at a simple wooden desk in a quiet apartment at dawn closing a notebook filled with handwritten equations, looking out the window as warm golden sunrise illuminates a peaceful futuristic city skyline, 35mm Kodak 2383 film grain, IMAX 4k 24fps.`
094. `EP10_VID_094_ACT4_24FPS_Silicon_Light_Refraction_A4S19_Macro_D.mp4` [19:58 – 20:11 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бо будь-яка революція завершується не в день, коли винайдено двигун, а в день, коли звичайна людина сідає за стіл на світанку, відкриває чистий файл і без страху…
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP10_VID_095_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [20:11 – 20:24 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його останній урок звучить просто, мов формула складного відсотка для людської долі:

«Не питайте, чи замінить вас штучний інтелект.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP10_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:24 – 20:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Читайте по одній статті, пишіть по десять рядків коду щодня — і за рік ви не впізнаєте власної сили.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP10_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [20:38 – 20:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Майбутнє не чекають у новинах.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP10_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [20:51 – 21:04 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Майбутнє збирають власними руками.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP10_VID_099_ACT4_24FPS_Silicon_Light_Refraction_A4S24_Silhoue.mp4` [21:04 – 21:17 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Цеглинка за цеглинкою.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP10_VID_100_ACT4_24FPS_Architectural_Corridor_A4S25_SlowMo_In.mp4` [21:17 – 21:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки в кожному домі не спалахне світло».
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring 1986 Singapore computer magazine BASIC listings under green phosphor glow, inverted Stanford RC helicopter at sunset, 16,000 Google Brain cores forming neural cat, millions of golden learner lights across night Earth, shot on ARRI Alfa Anamorphic 50mm & 35mm Wide, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
