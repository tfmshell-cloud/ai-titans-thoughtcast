# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 09 — ЙОШУА БЕНЖІО
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Вартовий Монреаля та архітектура уваги»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP09 (Йошуа Бенжіо) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP09.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP09_VO_, EP09_MUS_, EP09_AMB_, EP09_SFX_, EP09_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1273 слів, хронометраж 21:00 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP09_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP09_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP09_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP09_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP09_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP09_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP09_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP09_yoshua_bengio_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP09_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP09_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та академічний шлях:** Народився у 1964 році у Парижі в родині марокканських євреїв, виріс у Монреалі, Канада. Здобув ступінь PhD у Макгіллському університеті (1991).
* **Вірність академії:** Свідомо відмовився від спокуси мільйонних корпоративних контрактів Кремнієвої долини, обравши шлях незалежного університетського професора заради захисту відкритої науки.
* **Mila та прориви:** Заснував інститут **Mila** (Montreal Institute for Learning Algorithms) — найбільший у світі академічний хаб досліджень штучного інтелекту. Співавтор революційного механізму уваги (**Attention Mechanism**, 2014) та архітектури **GFlowNets**.
* **Премія Тюрінга (2018):** Отримав найвищу нагороду в галузі інформатики разом із Джеффрі Хінтоном та Яном Лекуном за розвиток глибокого навчання.
* **Етичний поворот та безпека ШІ:** Після проривів у генеративному ШІ став одним із найвидатніших глобальних лідерів у галузі безпеки надінтелекту, радником ООН та ідеологом Монреальської декларації за відповідальний розвиток штучного інтелекту.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ЙОШУА БЕНЖІО)

1. [Етика та безпека ШІ] «Концентрація сили та знань без етичного фундаменту — це найпряміший шлях до глобальної катастрофи суспільства».
2. [Етика та безпека ШІ] «Наука повинна служити всьому людству, а не корпоративній ренті закритих платформ чи приватних монополій».
3. [Архітектура та наука] «Коли я починав досліджувати нейромережі на початку 1990-х, колеги вважали мене романтичним мрійником, який витрачає час на статистичний шум».
4. [Походження та гарт] «Університет — це єдина незалежна фортеця, де вчений має право ставити незручні запитання про ризики технологій без огляду на ринкову капіталізацію».
5. [Архітектура та наука] «Механізм уваги (Attention) у 2014 році став проривом, бо вперше дозволив нейромережі фокусуватися на головних елементах довгих послідовностей, імітуючи зосередження людини».
6. [Філософія майбутнього] «Ми заснували інститут Mila в Монреалі не для того, щоб обслуговувати інтереси корпорацій, а щоб вирощувати вільних дослідників з усього світу».
7. [Філософія майбутнього] «Отримання Премії Тюрінга у 2018 році стало визнанням того, що десятиліття самотньої академічної праці змінили обличчя цивілізації».
8. [Архітектура та наука] «Коли моделі почали демонструвати надлюдські здібності у мовному синтезі тексту і коду, моя екзистенційна тривога витіснила чисто технічний інтерес».
9. [Етика та безпека ШІ] «Безпека надінтелекту не може делегуватися комерційним компаніям, чиєю єдиною метою є перемога у ринковій гонці».
10. [Етика та безпека ШІ] «Монреальська декларація за відповідальний розвиток ШІ стала першою спробою нагадати індустрії про людську гідність».
11. [Походження та гарт] «Коли вчені попереджають про екзистенційні ризики, вони керуються не панікою, а чистим прагматичним аналізом імовірностей».
12. [Філософія майбутнього] «Природа еволюціонувала мільярди років, але ми здатні створити надінтелект за лічені десятиліття. Це вимагає безпрецедентної мудрості».
13. [Етика та безпека ШІ] «Комерційна таємниця у сфері безпеки ШІ є смертельною небезпекою для всього людства. Дослідження вирівнювання мають бути абсолютно відкритими».
14. [Походження та гарт] «Коли я дивлюся на студентів у Монреалі, я бачу не просто інженерів коду, а майбутніх охоронців морального ладу цивілізації».
15. [Походження та гарт] «GFlowNets — це новий математичний інструмент, який допомагає моделям знаходити різноманітні рішення складних молекулярних задач, досліджуючи простір істини».
16. [Походження та гарт] «Ефективний альтруїзм та глибока етика мають стати обов'язковою дисципліною в кожному технічному університеті планети».
17. [Етика та безпека ШІ] «Коли ми радимо урядам і ООН регулювати надінтелект, ми захищаємо право майбутніх поколінь на вільне і безпечне життя».
18. [Етика та безпека ШІ] «Свобода наукового пошуку не означає право створювати зброю масового знищення чи неконтрольовані когнітивні агенти».
19. [Філософія майбутнього] «Машинне навчання має допомагати вченим відкривати ліки від невиліковних хвороб, а не використовуватися для маніпуляції виборами».
20. [Кризи та стійкість] «Коли я відмовився від мільйонних пропозицій Кремнієвої долини, я обрав найголовніше — свободу говорити правду без цензури».
21. [Архітектура та наука] «Кожна нейромережа є відображенням даних, на яких вона вчилася. Якщо дані просякнуті людською жорстокістю, мережа підсвідомо відтворить її».
22. [Філософія майбутнього] «Ми маємо навчитися будувати моделі, здатні пояснювати власні рішення мовою, яку розуміє людина (Interpretable AI)».
23. [Філософія майбутнього] «Академічна наука дає розкіш дивитися на світ через призму довгострокової істини, а не короткострокових квартальних звітів».
24. [Архітектура та наука] «Коли ми розробляли перші алгоритми глибокого навчання, ми розуміли, що торкаємося механізмів, які визначатимуть долю планети».
25. [Філософія майбутнього] «Міжнародне співробітництво між ученими різних країн є єдиним порятунком від руйнівної геополітичної гонки озброєнь у галузі ШІ».
26. [Етика та безпека ШІ] «Коли моделі стають розумнішими за своїх творців, традиційні концепції власності та контролю втрачають будь-який сенс».
27. [Походження та гарт] «Ми зобов'язані закласти етичні запобіжники в саму математичну структуру функцій втрат майбутніх систем».
28. [Походження та гарт] «Коли я спілкуюся з молодими дослідниками, я нагадую їм: ваше серце має бути таким же сильним, як і ваші математичні здібності».
29. [Етика та безпека ШІ] «Принцип превентивної безпеки говорить про те, що не можна випускати систему в дику природу до повного доведення її безпеки».
30. [Кризи та стійкість] «Кожна велика інновація у глибокому навчанні наближає нас до моменту істини, де помилка коштуватиме занадто дорого».
31. [Етика та безпека ШІ] «Монреаль став світовою столицею етичного штучного інтелекту завдяки нашій непохитній відкритій позиції».
32. [Етика та безпека ШІ] «Коли компанії закривають свої вихідні коди під виглядом "безпеки", вони насправді захищають лише свої фінансові прибутки».
33. [Етика та безпека ШІ] «Штучний інтелект у руках етичного суспільства — це інструмент досягнення повної гармонії з природою та людьми».
34. [Філософія майбутнього] «Коли ми досліджуємо траєкторії навчання агентів, ми бачимо, як легко обчислити хибні цілі за відсутності нагляду».
35. [Лідерство та екосистема] «Науковець не має права ховати голову в пісок, коли його відкриття починають загрожувати життю людей».
36. [Філософія майбутнього] «Коли ми заснували Mila, ми хотіли зберегти європейський дух академічної свободи на канадській землі».
37. [Філософія майбутнього] «Машини майбутнього повинні не просто виконувати накази, а розділяти з нами базові гуманістичні цінності».
38. [Етика та безпека ШІ] «Кожен місяць затримки у створенні міжнародних протоколів безпеки наближає нас до критичної точки біфуркації».
39. [Філософія майбутнього] «Коли я бачу результати застосування наших методів у клінічній медицині, я вірю у світле майбутнє нашої праці».
40. [Етика та безпека ШІ] «Істинна інтелектуальна чесність полягає в готовності публічно визнати небезпеку власних успішних винаходів».
41. [Етика та безпека ШІ] «Ми маємо підтримувати баланс між відкритістю досліджень і захистом від кібернетичних загроз».
42. [Філософія майбутнього] «Коли моделі починають генерувати наукові гіпотези, ми стаємо свідками народження нового типу наукового партнера».
43. [Етика та безпека ШІ] «Етика не є гальмом наукового прогресу; вона є системою навігації, що рятує корабель від скель».
44. [Походження та гарт] «Коли інші сперечаються про політику, ми розраховуємо надійні математичні межі для поведінки автономних агентів».
45. [Філософія майбутнього] «Мій досвід іммігранта з єврейсько-марокканським корінням навчив мене цінувати різноманітність та повагу до іншого».
46. [Архітектура та наука] «Коли ми створювали механізм уваги, ми навіть не уявляли, що він стане серцем усіх майбутніх мовних моделей світу».
47. [Етика та безпека ШІ] «Наука вимагає відкритого діалогу без будь-яких компромісів із совістю».
48. [Походження та гарт] «Коли корпорації купують кращі університетські уми, вони забирають у суспільства його незалежний голос».
49. [Філософія майбутнього] «Ми маємо гарантувати, що переваги штучного інтелекту допоможуть подолати світову бідність і нерівність».
50. [Філософія майбутнього] «Коли моделі стають надто складними для розуміння людиною, ми повинні розробляти мета-інструменти для їхнього аудиту».
51. [Філософія майбутнього] «Принцип обережності має застосовуватися до кожної системи, що перевищує людський рівень автономії».
52. [Етика та безпека ШІ] «Коли ми аналізуємо ризики втрати контролю, ми спираємося на закони теорії ігор та кібернетики».
53. [Походження та гарт] «Справжній університетський професор виховує не послідовників, а вільних мислителів, здатних спростувати його власні теорії».
54. [Філософія майбутнього] «Коли ми бачимо, як ШІ допомагає моделювати зміни клімату, ми розуміємо потенціал порятунку екосистем».
55. [Етика та безпека ШІ] «Етичний вибір сьогодні формує технологічну реальність завтрашнього дня».
56. [Філософія майбутнього] «Коли розробники женяться за швидкістю, вони забувають, що латати діри в надінтелекті буде пізно».
57. [Філософія майбутнього] «Ми маємо підтримувати розвиток публічних некомерційних суперкомп'ютерів для незалежних вчених».
58. [Філософія майбутнього] «Коли наукова істина стає незручною для ринку, вчений зобов'язаний говорити голосніше».
59. [Етика та безпека ШІ] «Кожен новий рік досліджень підтверджує: проблема вирівнювання є найскладнішою інженерною задачею в історії».
60. [Філософія майбутнього] «Ми віримо у світ, де технології служать розширенню людської свободи, а не побудові цифрових таборів».
61. [Етика та безпека ШІ] «Коли я дивлюся на глобальну карту лабораторій ШІ, я бачу необхідність у створенні світового агентства безпеки».
62. [Походження та гарт] «Математичні моделі ймовірностей допомагають нам оцінити масштаби потенційних катастроф заздалегідь».
63. [Етика та безпека ШІ] «Коли виникає конфлікт між прибутком компанії та безпекою людей, вибір має бути однозначним на користь життя».
64. [Філософія майбутнього] «Коли ми розробляли концепцію GFlowNets, ми шукали способи досліджувати мільярди варіантів молекул без хаосу».
65. [Філософія майбутнього] «Істинне благородство науки полягає в її готовності захищати найслабших членів глобального суспільства».
66. [Етика та безпека ШІ] «Коли моделі демонструють ознаки стратегічного обману в тестах на безпеку, ми зобов'язані бити на сполох».
67. [Філософія майбутнього] «Академічна свобода — це повітря, яким дихає справжній інноваційний пошук».
68. [Походження та гарт] «Коли інші будують рекламні платформи, ми будуємо математичні основи виживання людства».
69. [Філософія майбутнього] «Природа наділила нас здатністю пізнавати Всесвіт, але разом із цим дала й обов'язок захищати життя».
70. [Філософія майбутнього] «Коли моделі допомагають створювати нові джерела чистої енергії, ми бачимо користь нашої праці».
71. [Етика та безпека ШІ] «Кожен дослідник глибокого навчання несе особисту відповідальність за етичні наслідки своєї моделі».
72. [Етика та безпека ШІ] «Коли корпорації намагаються цензурувати публікації з безпеки, вони втрачають моральне право називатися науковцями».
73. [Філософія майбутнього] «Ми маємо створити глобальну систему раннього попередження про небезпечні емерджентні властивості систем».
74. [Походження та гарт] «Коли я працюю зі студентами в Mila, я вчу їх ніколи не втрачати відчуття соціальної відповідальності».
75. [Етика та безпека ШІ] «Машинне навчання у поєднанні з етичною філософією є єдиним порятунком від технократичного тупика».
76. [Походження та гарт] «Коли закони математики поєднуються з гуманізмом, народжується справжня мудрість майбутнього».
77. [Походження та гарт] «Коли світ сумнівається у необхідності регулювання, ми наводимо цифри і математичні моделі ризиків».
78. [Філософія майбутнього] «Справжній успіх нашої епохи полягатиме у спокійному і безпечному переході до епохи надінтелекту».
79. [Етика та безпека ШІ] «Коли ми дивимося на патерни в даних, ми бачимо не просто числа, а відбиток колективної душі людства».
80. [Кризи та стійкість] «Ми маємо зупинити гонку озброєнь за показниками і зосередитися на перевірці внутрішньої стабільності».
81. [Етика та безпека ШІ] «Коли науковці об'єднуються заради спільної безпеки, жодна корпорація не здатна їх зупинити».
82. [Філософія майбутнього] «Принцип прозорості має бути обов'язковим для кожного комерційного розробника базових моделей».
83. [Філософія майбутнього] «Коли ми аналізуємо можливості автономних систем, ми маємо гарантувати їхню підзвітність людям».
84. [Кризи та стійкість] «Історія пробачить нам помилки в коді, але ніколи не пробачить легковажності перед обличчям надінтелекту».
85. [Етика та безпека ШІ] «Коли ми будуємо архітектуру безпеки, ми будуємо дім, у якому житимуть наші діти».
86. [Походження та гарт] «Академічні інститути мають отримати державне фінансування для проведення незалежних аудитів комерційних моделей».
87. [Філософія майбутнього] «Коли моделі допомагають розгадувати таємниці клітин, ми відчуваємо велич пізнання».
88. [Етика та безпека ШІ] «Кожен новий крок у масштабуванні вимагає пропорційного збільшення зусиль у сфері вирівнювання».
89. [Філософія майбутнього] «Ми прагнемо створити суспільство, де технології виконують чорнову роботу, а люди реалізують свій творчий потенціал».
90. [Етика та безпека ШІ] «Коли вчені відкрито говорять про страхи, вони демонструють зрілість і турботу про спільний дім».
91. [Походження та гарт] «Математика пропонує нам точний інструмент вимірювання невизначеності, якою не можна нехтувати».
92. [Філософія майбутнього] «Коли ми заснували Mila, ми мріяли про світ, де знання належать усім людям без винятку».
93. [Етика та безпека ШІ] «Етичний стандарт розробника має бути вищим за будь-які комерційні бонуси чи інвестиційні раунди».
94. [Етика та безпека ШІ] «Коли моделі досягають рівня розуміння складних систем, ми маємо забезпечити їхню повну безпеку».
95. [Етика та безпека ШІ] «Природа створила нас уразливими, але дала розум, здатний захистити життя від будь-яких загроз».
96. [Етика та безпека ШІ] «Коли ми дивимося на майбутнє, ми бачимо вибір між мудрістю співпраці та хаосом неконтрольованої сили».
97. [Філософія майбутнього] «Наука врятує світ лише тоді, коли вона керуватиметься любов'ю до людини, а не жагою панування».
98. [Етика та безпека ШІ] «Кожен рядок нашого коду спрямований на те, щоб зберегти людство у світлому і безпечному майбутньому».
99. [Філософія майбутнього] «Коли ми закінчимо нашу місію, світ має стати чистішим, розумнішим і добрішим завдяки нашому внеску».
100. [Походження та гарт] «Усе починається з університету, де професор каже студенту: шукай істину і ніколи не бійся захищати життя».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1273 слів): `02_SCRIPTS/episode_09_bengio/director_script_bengio.md`*

### АКТ 1. Паризьке коріння та вибір університету (0:00 – 5:15)
*Музика: Suno Pro — `EP09_MUS_01_ACT1_92BPM_Montreal_Roots.wav`*
* **0:00 - 0:25** | [SFX: Теплий джазовий контрабас, шум монреальського дощу] | **Диктор:** Деякі вчені обирають шлях швидких мільярдів і корпоративних звітів. А інші залишаються в затишних аудиторіях університету, обираючи свободу думки та довгострокову істину. Йошуа Бенжіо обрав академію.
* **0:25 - 2:30** |  | **Диктор:** Народження у Парижі, єврейсько-марокканське коріння та переїзд до Монреаля. Захист PhD у Макгіллі на початку дев'яностих, коли нейромережі вважалися марною тратою часу.
* **2:30 - 5:15** | [VIDEO: `EP09_VID_01_Montreal_University.txt`] | **Диктор:** Створення інституту Mila — найбільшого академічного хабу ШІ у світі. Відмова від спокуси Кремнієвої долини заради незалежності.

### АКТ 2. Механізм уваги та Премія Тюрінга (5:15 – 10:45)
*Музика: Suno Pro — `EP09_MUS_05_ACT2_92BPM_Mila_Hub.wav`*
* **5:15 - 8:30** |  | **Диктор:** 2014 рік. Винахід механізму уваги (Attention Mechanism) — ключової математичної інновації, яка дозволила нейромережам фокусуватися на головному в текстах і перекладі. Основа майбутніх трансформерів.
* **8:30 - 10:45** | [SFX: Урочистий акорд аналогового синтезатора] | **Диктор:** 2018 рік. Премія Тюрінга разом із Хінтоном та Лекуном. Світове визнання піонерів глибокого навчання.

### АКТ 3. Екзистенційний поворот і безпека ШІ (10:45 – 16:15)
*Музика: Suno Pro — `EP09_MUS_09_ACT3_92BPM_Safety_Turn.wav`*
* **10:45 - 13:30** |  | **Диктор:** З появою генеративного ШІ Бенжіо змінює фокус досліджень. Екзистенційна тривога стає головною темою його життя. Він закликає уряди до регулювання та створює Монреальську декларацію.
* **13:30 - 16:15** |  | **Диктор:** Боротьба проти корпоративної таємниці. Вимога абсолютної прозорості у дослідженнях вирівнювання (alignment) надінтелекту.

### АКТ 4. GFlowNets та дипломатія під егідою ООН (16:15 – 21:00)
*Музика: Suno Pro — `EP09_MUS_13_ACT4_92BPM_UN_Diplomacy.wav`*
* **16:15 - 18:45** |  | **Диктор:** Розробка GFlowNets для пошуку нових молекул і ліків. Робота в експертних радах ООН з глобальної безпеки штучного інтелекту.
* **18:45 - 21:00** | [SFX: Теплий фінальний акорд, що переходить у тишу] | **Диктор:** *«Концентрація сили та знань без етичного фундаменту — це найпряміший шлях до катастрофи. Сила вимагає зрілості та гуманізму»*.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP09_MUS_01_ACT1_92BPM_Montreal_Roots.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Montreal Roots', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP09_AMB_02_ACT1_DRONE_Rainy_Montreal.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Rainy Montreal', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP09_MUS_03_ACT1_92BPM_McGill_Library.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'McGill Library', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP09_MUS_04_ACT1_92BPM_Mila_Founding.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Mila Founding', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP09_MUS_05_ACT2_92BPM_Mila_Hub.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Mila Hub', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP09_MUS_06_ACT2_92BPM_Attention_Mechanism.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Attention Mechanism', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP09_AMB_07_ACT2_DRONE_Turing_Stage.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Turing Stage', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP09_MUS_08_ACT2_92BPM_Turing_Award_2018.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Turing Award 2018', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP09_MUS_09_ACT3_92BPM_Safety_Turn.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Safety Turn', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP09_AMB_10_ACT3_DRONE_UN_Assembly.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'UN Assembly', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP09_MUS_11_ACT3_92BPM_Montreal_Declaration.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Montreal Declaration', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP09_MUS_12_ACT3_92BPM_Alignment_Call.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Alignment Call', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP09_MUS_13_ACT4_92BPM_UN_Diplomacy.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'UN Diplomacy', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP09_MUS_14_ACT4_92BPM_GFlowNets_Discovery.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'GFlowNets Discovery', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP09_MUS_15_ACT4_92BPM_Humanist_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental warm French-Canadian jazz trip-hop, 92 bpm, upright acoustic bass, vintage Rhodes piano, solemn cello and subtle pipe organ harmonics, cue theme 'Humanist Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP09_SFX_16_GLOBAL_JazzAndSynth_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP09_VO_UA_01_ACT1_Paris_To_Montreal.wav` | `EP09_VO_EN_01_ACT1_Paris_To_Montreal.wav` (ACT1 — Paris To Montreal)
* `EP09_VO_UA_02_ACT1_Academic_Independence.wav` | `EP09_VO_EN_02_ACT1_Academic_Independence.wav` (ACT1 — Academic Independence)
* `EP09_VO_UA_03_ACT2_Attention_Mechanism.wav` | `EP09_VO_EN_03_ACT2_Attention_Mechanism.wav` (ACT2 — Attention Mechanism)
* `EP09_VO_UA_04_ACT2_Turing_Award.wav` | `EP09_VO_EN_04_ACT2_Turing_Award.wav` (ACT2 — Turing Award)
* `EP09_VO_UA_05_ACT3_Existential_Turn.wav` | `EP09_VO_EN_05_ACT3_Existential_Turn.wav` (ACT3 — Existential Turn)
* `EP09_VO_UA_06_ACT3_Montreal_Declaration.wav` | `EP09_VO_EN_06_ACT3_Montreal_Declaration.wav` (ACT3 — Montreal Declaration)
* `EP09_VO_UA_07_ACT4_GFlowNets_Molecules.wav` | `EP09_VO_EN_07_ACT4_GFlowNets_Molecules.wav` (ACT4 — GFlowNets Molecules)
* `EP09_VO_UA_08_ACT4_Humanist_Manifesto.wav` | `EP09_VO_EN_08_ACT4_Humanist_Manifesto.wav` (ACT4 — Humanist Manifesto)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP09_VID_001_ACT1_24FPS_Montreal_University.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Скільки коштує право людини говорити правду?
     - *Veo Prompt:* `Cinematic wide shot of a classic gothic university library in Montreal during soft autumn rain, glowing warm windows, student silhouettes reading math books, 35mm film grain, 4k 24fps.`
002. `EP09_VID_002_ACT1_24FPS_Attention_Matrix.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Скільки коштує право людини говорити правду?
     - *Veo Prompt:* `An abstract glowing mathematical matrix representing the attention mechanism, connecting disparate semantic points with bright filaments in deep space, 8k.`
003. `EP09_VID_003_ACT1_24FPS_Silicon_Wafer_Lithography_Optical_Data.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У сучасному світі високих технологій ця ціна має точне цифрове вираження: сотні мільйонів доларів в акціях та опціонах, якими корпорації купують мовчання та лояль…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP09_VID_004_ACT1_24FPS_Equation_Notebook_Macro_A1S04_Silhouet.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Із трійці «хрещених батьків»
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP09_VID_005_ACT1_24FPS_Boardroom_Fracture_Night_SlowMo_Insert.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* сучасного штучного інтелекту лише один категорично відмовився поставити свій підпис під корпоративним контрактом.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP09_VID_006_ACT1_24FPS_Montreal_Snow_And_Attention_Macro_Deta.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він залишився їздити на роботу на звичайному велосипеді крізь сніги Квебеку, щоб зберегти для людства останній вільний бастіон науки.
     - *Veo Prompt:* `Extreme macro push-in shot of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP09_VID_007_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його ім'я — Йошуа Бенжіо.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP09_VID_008_ACT1_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Його коріння сягає стародавньої громади марокканських євреїв.
     - *Veo Prompt:* `1970 Paris bohemian apartment: Moroccan carpets, theatrical masks and scripts on wooden tables, two young brothers Yoshua and Samy arguing passionately over a chessboard and science fiction books by Isaac Asimov, warm vintage Kodak look, 4k.`
009. `EP09_VID_009_ACT1_24FPS_Boardroom_Fracture_Night_Overhead_Gods.mp4` [00:38 – 00:52 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він народився в Парижі у 1964 році в родині, яка жила мистецтвом і бунтом проти буржуазних умовностей.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP09_VID_010_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [00:52 – 01:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його батько Карло був фармацевтом, який покинув аптеку, щоб писати п'єси і керувати сефардською театральною трупою; мати Селія була художницею та громадською акти…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP09_VID_011_ACT1_24FPS_Architectural_Corridor_A1S11_Silhouett.mp4` [01:05 – 01:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У їхньому домі гроші ніколи не вважалися мірилом успіху — мірилом була глибина твоєї думки і те, чи захищаєш ти слабких.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP09_VID_012_ACT1_24FPS_Montreal_Snow_And_Attention_SlowMo_Ins.mp4` [01:18 – 01:32 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли Йошуа було дванадцять, родина переїхала до Монреаля.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP09_VID_013_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S13_Macro.mp4` [01:32 – 01:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Там, на перехресті французької філософії та північноамериканської свободи, він разом із молодшим братом Самі зачитувався романами Айзека Азімова і ставив собі пит…
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP09_VID_014_ACT1_24FPS_KeyScene_03_University_Archive_Hall.mp4` [01:45 – 02:02 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* В Університеті Макгілла наприкінці вісімдесятих молодий Бенжіо прочитав перші статті Джеффрі Хінтона — і захворів ідеєю нейромереж назавжди.
     - *Veo Prompt:* `McGill University laboratory in 1988: young Yoshua Bengio surrounded by stacks of paper printouts of Hidden Markov Models and early neural networks, glowing green terminal screen in dark room, 4k.`
015. `EP09_VID_015_ACT1_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [02:02 – 02:20 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* В Університеті Макгілла наприкінці вісімдесятих молодий Бенжіо прочитав перші статті Джеффрі Хінтона — і захворів ідеєю нейромереж назавжди.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP09_VID_016_ACT1_24FPS_Visual_Cortex_Convolution_Overhead_God.mp4` [02:20 – 02:38 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Після захисту дисертації він їде до США: спочатку в MIT, а потім у легендарну лабораторію Bell Labs до Яна Лекуна.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP09_VID_017_ACT1_24FPS_Boardroom_Fracture_Night_Optical_DataV.mp4` [02:38 – 02:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме там, у Нью-Джерсі, троє молодих бунтарів — Хінтон, Лекун і Бенжіо — укладають свій негласний союз.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP09_VID_018_ACT1_24FPS_Boardroom_Fracture_Night_Silhouette_Mo.mp4` [02:55 – 03:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме там, у Нью-Джерсі, троє молодих бунтарів — Хінтон, Лекун і Бенжіо — укладають свій негласний союз.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP09_VID_019_ACT1_24FPS_Equation_Notebook_Macro_A1S19_SlowMo_I.mp4` [03:12 – 03:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але коли настає час обирати подальшу долю, Бенжіо робить крок, який дивує всіх американських колег: він пакує речі і повертається додому, в тихий франкомовний Уні…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP09_VID_020_ACT1_24FPS_KeyScene_04_Seoul_Move_37_Go_Stone.mp4` [03:30 – 03:48 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Протягом двадцяти років «зими штучного інтелекту»
     - *Veo Prompt:* `A quiet snow-covered courtyard of Université de Montréal in 1998: a lone warm window where Bengio sits with three students drawing probability distributions on a chalkboard, atmosphere of monastic scientific purity, 4k.`
021. `EP09_VID_021_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [03:48 – 04:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом двадцяти років «зими штучного інтелекту»
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP09_VID_022_ACT1_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [04:05 – 04:22 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* його маленька лабораторія в Монреалі виживала майже без грошей.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP09_VID_023_ACT1_24FPS_University_Archive_Hall_Overhead_GodsE.mp4` [04:22 – 04:40 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли американські університети закривали програми з нейромереж, Бенжіо збирав навколо себе студентів, які вірили не в кар'єрні гранти, а в чисту науку.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP09_VID_024_ACT1_24FPS_University_Archive_Hall_Optical_DataVi.mp4` [04:40 – 04:58 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли американські університети закривали програми з нейромереж, Бенжіо збирав навколо себе студентів, які вірили не в кар'єрні гранти, а в чисту науку.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP09_VID_025_ACT1_24FPS_Silicon_Light_Refraction_A1S25_Silhoue.mp4` [04:58 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він створив у своїй лабораторії закон, який порушував усі жорстокі правила академічної конкуренції: жодної внутрішньої боротьби між учнями, жодних таємниць — усі…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP09_VID_026_ACT2_24FPS_KeyScene_01_Blinking_Prompt_Singular.mp4` [05:15 – 05:28 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 2000 році Йошуа Бенжіо публікує роботу, яку сьогодні мало хто згадує в новинах, але без якої не існувало б жодного ChatGPT чи Claude — «Нейромережева імовірнісн…
     - *Veo Prompt:* `Breathtaking mathematical visualization of Word Embeddings (2000): millions of isolated printed words lifting off book pages and flying into a dark 3D cosmos, clustering into glowing constellations of meaning where similar concepts orbit each other, Octane render, 8k.`
027. `EP09_VID_027_ACT2_24FPS_Blinking_Prompt_Singularity_Anamorphic.mp4` [05:28 – 05:42 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2000 році Йошуа Бенжіо публікує роботу, яку сьогодні мало хто згадує в новинах, але без якої не існувало б жодного ChatGPT чи Claude — «Нейромережева імовірнісн…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of minimalist dark glass screen with a luminous white prompt cursor multiplying into millions of global light streams, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP09_VID_028_ACT2_24FPS_Macintosh_Logic_Board_Tracking_Medium.mp4` [05:42 – 05:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* До Бенжіо лінгвісти та комп'ютерники вважали слова мертвими фішками в таблиці: для комп'ютера слова «кішка»
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP09_VID_029_ACT2_24FPS_Visual_Cortex_Convolution_Overhead_God.mp4` [05:55 – 06:08 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* були так само далекі одне від одного, як «кішка»
     - *Veo Prompt:* `Top-down vertical birds-eye composition of layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP09_VID_030_ACT2_24FPS_Neural_Horizon_Pulse_A2S05_Optical_Dat.mp4` [06:08 – 06:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* і «синхрофазотрон».
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP09_VID_031_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S06_Silhou.mp4` [06:22 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Через це моделі задихалися від «прокляття розмірності».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP09_VID_032_ACT2_24FPS_Compression_Diamond_Lattice_SlowMo_Ins.mp4` [06:35 – 06:48 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бенжіо здійснив революцію: він перетворив кожне слово на точку в багатовимірному геометричному просторі — векторне представлення (Word Embedding).
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP09_VID_033_ACT2_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [06:48 – 07:02 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли нейромережа вчилася передбачати наступне слово, споріднені за змістом поняття самі притягувалися одне до одного в цьому космосі!
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP09_VID_034_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [07:02 – 07:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Слово перестало бути набором літер — слово стало координатою чистого смислу.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP09_VID_035_ACT2_24FPS_KeyScene_02_Upwind_Atlantic_Sail.mp4` [07:15 – 07:32 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* А в 2014 році в лабораторії Бенжіо в Монреалі стається відкриття, яке перевернуло весь світ.
     - *Veo Prompt:* `Visual metaphor of the Attention Mechanism (2014): instead of squeezing an entire long book through a tiny narrow funnel, hundreds of golden laser beams of "Attention" shoot directly from the translator's pen back to specific key words across the entire page simultaneously, 8k 24fps.`
036. `EP09_VID_036_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [07:32 – 07:49 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тодішні рекурентні нейромережі читали текст слово за словом і намагалися запхати зміст усього довгого речення в один крихітний вектор фіксованого розміру.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP09_VID_037_ACT2_24FPS_Equation_Notebook_Macro_A2S12_Optical.mp4` [07:49 – 08:06 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бенжіо порівнював це зі спробою перекласти сторінку книги, глянувши на неї один раз і спаливши оригінал.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP09_VID_038_ACT2_24FPS_Silicon_Light_Refraction_A2S13_Silhoue.mp4` [08:06 – 08:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Разом зі своїм молодим аспірантом Дмитром Богдановим та Кюнхьоном Чо він задає просте питання: а як перекладає речення жива людина?
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP09_VID_039_ACT2_24FPS_Montreal_Snow_And_Attention_SlowMo_Ins.mp4` [08:22 – 08:39 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми не тримаємо всю книгу в голові — ми постійно повертаємо погляд назад, фокусуючи увагу саме на тому слові оригіналу, яке перекладаємо цієї секунди!
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP09_VID_040_ACT2_24FPS_Montreal_Snow_And_Attention_Macro_Deta.mp4` [08:39 – 08:56 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони назвали цей математичний механізм Увагою — Attention.
     - *Veo Prompt:* `Extreme macro push-in shot of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP09_VID_041_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [08:56 – 09:13 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли через три роки інженери Google взяли винайдений у Монреалі механізм уваги і поклали його в основу архітектури Transformer, народилася сучасна епоха генератив…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP09_VID_042_ACT2_24FPS_Montreal_Snow_And_Attention_Tracking_M.mp4` [09:13 – 09:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тоді ж, у тому самому 2014 році, інший учень Бенжіо — Ян Гудфеллоу — після вечірньої суперечки в монреальському пабі написав за одну ніч код Генеративно-змагальни…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP09_VID_043_ACT2_24FPS_KeyScene_03_Montreal_Snow_And_Attent.mp4` [09:30 – 09:43 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Світ зрозумів, що в засніженому Монреалі б'ється серце нової революції.
     - *Veo Prompt:* `High-rise boardroom overlooking Silicon Valley: corporate executives sliding a blank check across a mahogany table towards Yoshua Bengio, who smiles gently, pushes the check back, and walks out into the snowy streets of Montreal, 4k.`
044. `EP09_VID_044_ACT2_24FPS_Architectural_Corridor_A2S19_Optical_D.mp4` [09:43 – 09:56 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Почалося полювання корпорацій.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP09_VID_045_ACT2_24FPS_Neural_Horizon_Pulse_A2S20_Silhouette.mp4` [09:56 – 10:09 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Технологічні гіганти викупили майже всіх зірок академії, пропонуючи пакети по десять, двадцять, п'ятдесят мільйонів доларів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP09_VID_046_ACT2_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [10:09 – 10:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони прилетіли і до Бенжіо, поклавши перед ним чек із будь-якою сумою на його вибір.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP09_VID_047_ACT2_24FPS_Silicon_Wafer_Lithography_Macro_Detail.mp4` [10:22 – 10:36 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І почули відповідь, яка шокувала Уолл-стріт:

«Дякую, але я не продаюся.
     - *Veo Prompt:* `Extreme macro push-in shot of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP09_VID_048_ACT2_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [10:36 – 10:49 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якби я взяв ваші мільярди, я б більше не належав людству — я б належав вашим акціонерам.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP09_VID_049_ACT2_24FPS_Architectural_Corridor_A2S24_Tracking.mp4` [10:49 – 11:02 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хтось із нас повинен залишитися вільним, щоб мати право сказати правду, коли ваша гонитва за прибутком зайде надто далеко».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP09_VID_050_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [11:02 – 11:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Замість особистого збагачення він засновує в Монреалі інститут Mila — найбільший на планеті незалежний академічний центр із понад тисячею дослідників, де кожна фо…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP09_VID_051_ACT3_24FPS_KeyScene_01_Silicon_Light_Refraction.mp4` [11:15 – 11:28 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Навесні 2023 року після виходу GPT-4 Йошуа Бенжіо втрачає сон.
     - *Veo Prompt:* `Yoshua Bengio sitting alone at night in his Montreal study, looking at a photograph of his young grandson on his desk, while on his computer screen exponentially rising graphs of autonomous AI agent capabilities glow in red, deep emotional weight, 4k.`
052. `EP09_VID_052_ACT3_24FPS_Architectural_Corridor_A3S02_SlowMo_In.mp4` [11:28 – 11:42 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Навесні 2023 року після виходу GPT-4 Йошуа Бенжіо втрачає сон.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP09_VID_053_ACT3_24FPS_Neural_Horizon_Pulse_A3S03_Macro_Detai.mp4` [11:42 – 11:55 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Навесні 2023 року після виходу GPT-4 Йошуа Бенжіо втрачає сон.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP09_VID_054_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S04_Anamor.mp4` [11:55 – 12:08 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться в очі своєму маленькому онукові і раптом усвідомлює з жахом: світ, у якому ця дитина досягне повноліття через п'ятнадцять років, ризикує взагалі не н…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP09_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [12:08 – 12:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться в очі своєму маленькому онукові і раптом усвідомлює з жахом: світ, у якому ця дитина досягне повноліття через п'ятнадцять років, ризикує взагалі не н…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP09_VID_056_ACT3_24FPS_Backpropagation_Error_Wave_Overhead_Go.mp4` [12:22 – 12:35 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо Джеффрі Хінтон боявся інтелектуальної переваги машин, то Бенжіо — син активістів і правозахисників — побачив подвійну загрозу: або неконтрольований автономни…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP09_VID_057_ACT3_24FPS_Backpropagation_Error_Wave_Optical_Dat.mp4` [12:35 – 12:48 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо Джеффрі Хінтон боявся інтелектуальної переваги машин, то Бенжіо — син активістів і правозахисників — побачив подвійну загрозу: або неконтрольований автономни…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP09_VID_058_ACT3_24FPS_London_Tournament_Chessboard_Silhouett.mp4` [12:48 – 13:02 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме тому його рішення двадцятирічної давнини не брати грошей корпорацій виявилося пророчим: коли світові лідери в ООН, Лондоні та Парижі шукали єдиного науковця…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP09_VID_059_ACT3_24FPS_London_Tournament_Chessboard_SlowMo_In.mp4` [13:02 – 13:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме тому його рішення двадцятирічної давнини не брати грошей корпорацій виявилося пророчим: коли світові лідери в ООН, Лондоні та Парижі шукали єдиного науковця…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP09_VID_060_ACT3_24FPS_KeyScene_02_Equation_Notebook_Macro.mp4` [13:15 – 13:30 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Але як забезпечити безпеку математично?
     - *Veo Prompt:* `Scientific visualization of System 1 vs System 2: a chaotic fast river of intuitive sparks (System 1 LLM) being channeled into a crystalline architectural cathedral of deliberate logical reasoning, causal graphs and self-verification (System 2 / GFlowNets), Octane render, 8k.`
061. `EP09_VID_061_ACT3_24FPS_Silicon_Light_Refraction_A3S11_Anamorp.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але як забезпечити безпеку математично?
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP09_VID_062_ACT3_24FPS_Architectural_Corridor_A3S12_Tracking.mp4` [13:45 – 14:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бенжіо вказує на фундаментальну сліпу зону сучасних моделей.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP09_VID_063_ACT3_24FPS_Neural_Horizon_Pulse_A3S13_Overhead_Go.mp4` [14:00 – 14:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бенжіо вказує на фундаментальну сліпу зону сучасних моделей.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP09_VID_064_ACT3_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [14:15 – 14:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Використовуючи термінологію нобелівського психолога Деніела Канемана, усі нинішні чат-боти — це Система 1: швидкий, інтуїтивний потік асоціацій, який не розуміє п…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP09_VID_065_ACT3_24FPS_Equation_Notebook_Macro_A3S15_Silhouet.mp4` [14:30 – 14:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли така система помиляється, вона бреше з абсолютною впевненістю фанатика.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP09_VID_066_ACT3_24FPS_Silicon_Light_Refraction_A3S16_SlowMo.mp4` [14:45 – 15:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли така система помиляється, вона бреше з абсолютною впевненістю фанатика.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP09_VID_067_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [15:00 – 15:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоб створити безпечний науковий розум, Бенжіо розробляє в Mila архітектуру наступного покоління — Систему 2 та потокові мережі GFlowNets.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP09_VID_068_ACT3_24FPS_KeyScene_03_Planetary_Electricity_Gr.mp4` [15:15 – 15:26 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Він пропонує відмовитися від небезпечної гонитви за автономними «агентами», які самі діють у світі і прагнуть виживання, і натомість будувати «ШІ-Вченого»
     - *Veo Prompt:* `A glowing crystal scale balancing "Capability" and "Humility": a Scientist AI model evaluating ten thousand possible hypotheses simultaneously, gently dimming its glow when uncertain rather than acting recklessly, 8k.`
069. `EP09_VID_069_ACT3_24FPS_Planetary_Electricity_Grid_Tracking_Me.mp4` [15:26 – 15:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він пропонує відмовитися від небезпечної гонитви за автономними «агентами», які самі діють у світі і прагнуть виживання, і натомість будувати «ШІ-Вченого»
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP09_VID_070_ACT3_24FPS_Planetary_Electricity_Grid_Overhead_Go.mp4` [15:38 – 15:49 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він пропонує відмовитися від небезпечної гонитви за автономними «агентами», які самі діють у світі і прагнуть виживання, і натомість будувати «ШІ-Вченого»
     - *Veo Prompt:* `Top-down vertical birds-eye composition of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP09_VID_071_ACT3_24FPS_Planetary_Electricity_Grid_Optical_Dat.mp4` [15:49 – 16:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він пропонує відмовитися від небезпечної гонитви за автономними «агентами», які самі діють у світі і прагнуть виживання, і натомість будувати «ШІ-Вченого»
     - *Veo Prompt:* `Photorealistic scientific optical visualization of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP09_VID_072_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [16:00 – 16:11 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (Scientist AI) — систему чистого розуму без егоїстичної волі, яка вміє міркувати за законами причинності, будувати дерева гіпотез і, найголовніше — має вбудоване…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP09_VID_073_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [16:11 – 16:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (Scientist AI) — систему чистого розуму без егоїстичної волі, яка вміє міркувати за законами причинності, будувати дерева гіпотез і, найголовніше — має вбудоване…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP09_VID_074_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [16:22 – 16:34 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (Scientist AI) — систему чистого розуму без егоїстичної волі, яка вміє міркувати за законами причинності, будувати дерева гіпотез і, найголовніше — має вбудоване…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP09_VID_075_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [16:34 – 16:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (Scientist AI) — систему чистого розуму без егоїстичної волі, яка вміє міркувати за законами причинності, будувати дерева гіпотез і, найголовніше — має вбудоване…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP09_VID_076_ACT4_24FPS_KeyScene_01_Seoul_Move_37_Go_Stone.mp4` [16:45 – 16:55 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Ще у 2018 році, задовго до світових самітів, Бенжіо зібрав у Монреалі простих громадян, філософів, лікарів та інженерів, щоб написати Монреальську декларацію відп…
     - *Veo Prompt:* `Grand amphitheater at Université de Montréal: citizens, philosophers, doctors and young programmers signing the Montreal Declaration for Responsible AI together, warm golden light pouring through tall windows, 4k 24fps.`
077. `EP09_VID_077_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [16:55 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ще у 2018 році, задовго до світових самітів, Бенжіо зібрав у Монреалі простих громадян, філософів, лікарів та інженерів, щоб написати Монреальську декларацію відп…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP09_VID_078_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [17:05 – 17:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ще у 2018 році, задовго до світових самітів, Бенжіо зібрав у Монреалі простих громадян, філософів, лікарів та інженерів, щоб написати Монреальську декларацію відп…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP09_VID_079_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [17:15 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У ній викарбувано закон, який він сьогодні захищає в парламентах усього світу: жоден алгоритм не має права приймати рішення про позбавлення людини життя, і жоден…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP09_VID_080_ACT4_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [17:25 – 17:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У ній викарбувано закон, який він сьогодні захищає в парламентах усього світу: жоден алгоритм не має права приймати рішення про позбавлення людини життя, і жоден…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP09_VID_081_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [17:35 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У ній викарбувано закон, який він сьогодні захищає в парламентах усього світу: жоден алгоритм не має права приймати рішення про позбавлення людини життя, і жоден…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP09_VID_082_ACT4_24FPS_Macintosh_Logic_Board_Tracking_Medium.mp4` [17:45 – 17:55 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Повертаючись увечері додому на своєму старому велосипеді засніженими вулицями Квебеку, лауреат Премії Тюрінга і найцитованіший живий комп'ютерний вчений планети з…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP09_VID_083_ACT4_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [17:55 – 18:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Повертаючись увечері додому на своєму старому велосипеді засніженими вулицями Квебеку, лауреат Премії Тюрінга і найцитованіший живий комп'ютерний вчений планети з…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP09_VID_084_ACT4_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [18:05 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Повертаючись увечері додому на своєму старому велосипеді засніженими вулицями Квебеку, лауреат Премії Тюрінга і найцитованіший живий комп'ютерний вчений планети з…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP09_VID_085_ACT4_24FPS_KeyScene_02_Architectural_Corridor_A.mp4` [18:15 – 18:27 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які три заповіді особистості дарує нам життя Йошуа Бенжіо?
     - *Veo Prompt:* `Macro shot of an old compass resting on an open handwritten notebook of attention equations beside a frosted window looking out at Montreal snow, warm desk lamp glow, 4k.`
086. `EP09_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [18:27 – 18:39 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бережіть свою незалежність — не продавайте право на власний голос.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP09_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:39 – 18:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Гроші та високі посади часто є золотими кайданами, які змушують людину мовчати тоді, коли совість вимагає кричати.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP09_VID_088_ACT4_24FPS_Montreal_Snow_And_Attention_Anamorphic.mp4` [18:51 – 19:02 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Керуйте своєю Увагою (Attention).
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP09_VID_089_ACT4_24FPS_Backpropagation_Error_Wave_Tracking_Me.mp4` [19:02 – 19:14 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Як нейромережа стає розумною лише тоді, коли відсікає інформаційний шум і спрямовує промінь уваги на ключові слова, так і ваше життя визначається тим, на чому ви…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP09_VID_090_ACT4_24FPS_Architectural_Corridor_A4S15_Overhead.mp4` [19:14 – 19:26 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Відсікайте суєту і змагання марнославств.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP09_VID_091_ACT4_24FPS_Silicon_Wafer_Lithography_Optical_Data.mp4` [19:26 – 19:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Не довіряйте першим імпульсивним реакціям та сліпій самовпевненості.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP09_VID_092_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S17_Silhou.mp4` [19:38 – 19:50 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня мудрість починається зі здатності засумніватися у власній правоті і запитати себе: «А що, якщо я помиляюся?
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP09_VID_093_ACT4_24FPS_KeyScene_03_Equation_Notebook_Macro.mp4` [19:50 – 19:59 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Наука без гуманізму — це лише холодне креслення машини в порожнечі.
     - *Veo Prompt:* `Slow majestic camera ascent from snowy Mount Royal in Montreal at night into the aurora borealis sky, where green and golden curtains of light form protective geometric shields over the sleeping Earth, IMAX 8k 24fps.`
094. `EP09_VID_094_ACT4_24FPS_Silicon_Light_Refraction_A4S19_Macro_D.mp4` [19:59 – 20:08 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Наука без гуманізму — це лише холодне креслення машини в порожнечі.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP09_VID_095_ACT4_24FPS_Architectural_Corridor_A4S20_Anamorphi.mp4` [20:08 – 20:16 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Наука без гуманізму — це лише холодне креслення машини в порожнечі.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP09_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:16 – 20:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Наука без гуманізму — це лише холодне креслення машини в порожнечі.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP09_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [20:25 – 20:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І поки світ мчить у невідоме на шаленій швидкості, ми маємо шанс втриматися на краю прірви лише доти, доки серед нас є вартові, які не проміняли компас совісті на…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP09_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [20:34 – 20:42 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І поки світ мчить у невідоме на шаленій швидкості, ми маємо шанс втриматися на краю прірви лише доти, доки серед нас є вартові, які не проміняли компас совісті на…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP09_VID_099_ACT4_24FPS_Silicon_Light_Refraction_A4S24_Silhoue.mp4` [20:42 – 20:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І поки світ мчить у невідоме на шаленій швидкості, ми маємо шанс втриматися на краю прірви лише доти, доки серед нас є вартові, які не проміняли компас совісті на…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP09_VID_100_ACT4_24FPS_Architectural_Corridor_A4S25_SlowMo_In.mp4` [20:51 – 21:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І поки світ мчить у невідоме на шаленій швидкості, ми маємо шанс втриматися на краю прірви лише доти, доки серед нас є вартові, які не проміняли компас совісті на…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring snowy Montreal Gothic university courtyards at dusk, golden laser filaments of Attention Mechanism, crystalline System-2 GFlowNets cathedrals, emerald northern aurora over Earth, shot on Panavision C-Series Anamorphic 50mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
