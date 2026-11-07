# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 07 — ДАРІО АМОДЕЙ
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Фізика совісті та машини благодаті»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP07 (Даріо Амодей) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP07.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP07_VO_, EP07_MUS_, EP07_AMB_, EP07_SFX_, EP07_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1223 слів, хронометраж 20:30 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP07_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP07_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP07_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP07_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP07_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP07_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP07_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP07_dario_amodei_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP07_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP07_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та освіта:** Народився 1983 року в Сан-Франциско, Каліфорнія. Отримав ступінь бакалавра з фізики в Стенфорді та захистив докторський ступінь (PhD) з біофізики в Прінстонському університеті (2011), досліджуючи електрофізіологію нейронних мереж.
* **Шлях у великому ШІ:** Працював у Baidu та Google Brain, після чого приєднався до OpenAI у 2016 році. Очолював напрям безпеки та розробку моделей GPT-2 і GPT-3, став співавтором емпіричних законів масштабування (Scaling Laws).
* **Створення Anthropic (2021):** Через стратегічні розбіжності та питання безпеки залишив OpenAI разом із сестрою Даніелою та іншими провідними дослідниками. Заснував Anthropic, створивши сімейство моделей Claude.
* **Конституційний ШІ (Constitutional AI):** Піонер у галузі безпеки на основі принципів (Constitutional AI), що дозволяє моделям самостійно налаштовувати свою поведінку за допомогою прозорих етичних інструкцій.
* **Філософія майбутнього:** Автор маніфесту «Machines of Loving Grace» (2024), що описує оптимістичний сценарій ліквідації хвороб і подолання біологічних обмежень людини за допомогою надінтелекту.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ДАРІО АМОДЕЙ)

1. [Філософія майбутнього] «Штучний інтелект у найближчі роки здатен подвоїти тривалість здорового життя людини і подолати глобальні хвороби».
2. [Етика та безпека ШІ] «Безпека не є гальмом прогресу — вона є єдиною дорогою, яка дозволяє взагалі дістатися до фінішу».
3. [Походження та гарт] «Коли я вивчав біофізику нейронів у Прінстоні, я шукав базову фізику розуму, яка тепер оживає у кремнії».
4. [Архітектура та наука] «Закони масштабування — це не просто емпірична крива; це фундаментальний закон того, як кількість інформації стає якістю мислення».
5. [Архітектура та наука] «Коли ми створювали GPT-3 в OpenAI, ми вперше побачили появу справжніх емерджентних здібностей у мовних моделях».
6. [Етика та безпека ШІ] «Розрив з OpenAI у 2020 році був найважчим рішенням, але ми мали створити простір, де безпека стоїть вище за ринкові перегони».
7. [Етика та безпека ШІ] «Anthropic народилася з простої ідеї: ми можемо будувати найпотужніші моделі у світі і водночас робити їх керованими, чесними та етичними».
8. [Етика та безпека ШІ] «Конституційний ШІ (Constitutional AI) дозволяє моделям спиратися на прозорий звід людських цінностей, а не на закриті заборони цензорів».
9. [Архітектура та наука] «Моделі серії Claude створені не просто для того, щоб відповідати на запити, а щоб бути надійними партнерами у найскладніших інтелектуальних завданнях».
10. [Походження та гарт] «Технологічний оптимізм має бути обґрунтований жорсткою інженерною дисципліною та математичними гарантіями безпеки».
11. [Філософія майбутнього] «Коли ми говоримо про потенціал вилікувати рак чи хворобу Альцгеймера за допомогою ШІ, ми маємо на увазі пришвидшення медичних досліджень у тисячу разів».
12. [Етика та безпека ШІ] «Неконтрольований надінтелект є реальною загрозою, і ігнорувати цей ризик через сліпу віру в технології — злочинно».
13. [Філософія майбутнього] «Ефективний альтруїзм та раціоналізм вчать нас дивитися на довгострокові наслідки наших дій без рожевих окулярів».
14. [Етика та безпека ШІ] «Кожен терафлопс обчислень має бути спрямований на розширення свободи та добробуту людства».
15. [Етика та безпека ШІ] «Маніфест "Machines of Loving Grace" відображає мою віру в те, що технологія може принести людям не загрозу, а небачене звільнення від хвороб».
16. [Походження та гарт] «Фізика та біофізика навчили мене шукати прості математичні закономірності за мільйонами складних клітинних сигналів».
17. [Філософія майбутнього] «Коли ми писали перші статті про Scaling Laws, ми зрозуміли, що якість моделі передбачувано зростає разом із ресурсами».
18. [Архітектура та наука] «Співпраця з моєю сестрою Даніелою в Anthropic дала нам рідкісну єдність мети і цінностей у побудові компанії».
19. [Етика та безпека ШІ] «Ми не прагнемо до домінування на ринку ціною втрати контролю над внутрішньою поведінкою наших нейромереж».
20. [Етика та безпека ШІ] «Прозора етика в архітектурі моделей — це єдиний спосіб заслужити довіру суспільства та урядів».
21. [Архітектура та наука] «Коли ми бачимо, як Claude допомагає програмістам знаходити критичні баги або аналізувати біологічні статті, ми відчуваємо реальну користь».
22. [Етика та безпека ШІ] «Інтелект є найбільшим інструментом у ящику інструментів людства, і наше завдання — використати його для скасування людських страждань».
23. [Етика та безпека ШІ] «Бути дослідником у галузі ШІ сьогодні — це нести тягар відповідальності за майбутнє всієї цивілізації».
24. [Філософія майбутнього] «Ми не маємо права помилитися у момент переходу до надінтелекту, бо другої спроби у нас не буде».
25. [Етика та безпека ШІ] «Кожна нова модель має бути більш інтерпретованою та зрозумілою для наших дослідників безпеки».
26. [Етика та безпека ШІ] «Коли ми об'єднуємо зусилля з гігантами на кшталт Amazon та Google, ми зберігаємо нашу автономію у прийнятті рішень щодо безпеки».
27. [Філософія майбутнього] «Науковий метод у поєднанні з глибоким навчанням здатний перетворити медицину з емпіричної науки на точну інженерію».
28. [Етика та безпека ШІ] «Не бійтеся зізнатися у складних ризиках перед громадськістю — чесність є основою довіри».
29. [Етика та безпека ШІ] «Коли моделі досягають рівня експертів у біології та програмуванні, їхня користь стає неймовірною, але й ризики зростають пропорційно».
30. [Етика та безпека ШІ] «Ми маємо побудувати такий фундамент вирівнювання, який витримає будь-які спроби маніпуляції ззовні».
31. [Філософія майбутнього] «Фізична реальність і біологія людини мають крихкі обмеження, які ШІ допоможе подолати завдяки новим лікам і матеріалам».
32. [Походження та гарт] «Коли я був студентом у Прінстоні, я проводив ночі в лабораторії, намагаючись зрозуміти, як сітківка ока кодує світло в імпульси».
33. [Кризи та стійкість] «Закон масштабування працює безвідмовно, якщо ви готові інвестувати колосальні ресурси в інфраструктуру».
34. [Лідерство та екосистема] «Ми маємо підтримувати баланс між відкритим науковим обміном та необхідністю захисту моделей від зловмисного використання».
35. [Кризи та стійкість] «Коли інші поспішають випустити сирий продукт, ми ретельно перевіряємо його на стійкість до небезпечних запитів».
36. [Філософія майбутнього] «Технологічний прогрес має покращувати якість життя кожного жителя планети, а не лише створювати нові ринкові міхури».
37. [Етика та безпека ШІ] «Коли ми створювали Constitutional AI, ми хотіли дати моделям чіткі моральні орієнтири, закладені в тексті декларацій».
38. [Архітектура та наука] «Свідомість і розуміння в кремнії розвиваються за власними законами, які ми зобов'язані ретельно вивчати».
39. [Кризи та стійкість] «Кожна ітерація моделі Claude стає дедалі більш нюансованою, інтелігентною та безпечною для користувача».
40. [Філософія майбутнього] «Ми віримо у світ, де технології виконують найважчу роботу, а люди зосереджуються на творчості, спілкуванні та щасті».
41. [Лідерство та екосистема] «Коли ти керуєш компанією на передньому краї науки, ти приймаєш рішення під тиском колосальної невизначеності».
42. [Походження та гарт] «Математичні моделі нейронів у Прінстоні заклали основу для мого розуміння штучних великих нейромереж».
43. [Кризи та стійкість] «Ми не прагнемо замінити людську творчість; ми прагнемо підсилити здатність людей вирішувати глобальні кризи».
44. [Філософія майбутнього] «Коли наука дає нам інструменти для порятунку мільйонів життів, ми зобов'язані застосувати їх негайно і без зволікань».
45. [Етика та безпека ШІ] «Етична стійкість організації перевіряється в моменти, коли комерційний інтерес вимагає заплющити очі на безпеку».
46. [Етика та безпека ШІ] «Коли ми залишали OpenAI, ми знали, що попереду нас чекає виснажлива боротьба за ресурси, але наша совість була чистою».
47. [Етика та безпека ШІ] «Закони природи суворі, але справедливі: якщо ви не врахували ризики, система карає вас неминуче».
48. [Філософія майбутнього] «Коли моделі допомагають створювати нові антибіотики, ми бачимо найкраще втілення нашої місії».
49. [Етика та безпека ШІ] «Ми маємо забезпечити міжнародний контроль за розробкою надінтелекту, щоб уникнути неконтрольованої гонки озброєнь».
50. [Філософія майбутнього] «Кожен успішний експеримент в Anthropic наближає нас до епохи повної перемоги над найтяжчими недугами людини».
51. [Архітектура та наука] «Коли ми аналізуємо внутрішні репрезентації нейромережі, ми бачимо, як поняття утворюють складні геометричні кластери».
52. [Етика та безпека ШІ] «Наука вимагає відкритості до нових даних, навіть якщо вони суперечать твоїм старим теоретичним поглядам».
53. [Філософія майбутнього] «Коли ми говоримо про майбутнє довголіття, ми спираємося на конкретні успіхи обчислювальної біології».
54. [Архітектура та наука] «Не бійтеся ставити перед собою завдання планетарного масштабу — це єдине, що варте зусиль усього життя».
55. [Архітектура та наука] «Коли ми створювали перші версії Claude, ми хотіли уникнути токсичності й маніпуляцій, характерних для ранніх ботів».
56. [Етика та безпека ШІ] «Етичний кодекс компанії має бути прописаний не у рекламних проспектах, а в архітектурних шарах коду».
57. [Філософія майбутнього] «Коли світ сперечається про дрібниці, ми маємо фокусуватися на головному — керованості й безпеці майбутнього розуму».
58. [Філософія майбутнього] «Фізика і біофізика навчили мене поважати складність систем, які неможливо осягнути простими правилами».
59. [Етика та безпека ШІ] «Коли ми бачимо результати роботи наших моделей у реальному секторі, ми розуміємо, що епоха теоретичного ШІ закінчилася».
60. [Етика та безпека ШІ] «Ми маємо виховати нове покоління дослідників, для яких безпека і корисність є єдиним стандартом якості».
61. [Архітектура та наука] «Коли ти бачиш потенціал вирішення проблеми зміни клімату за допомогою нових матеріалів, ти розумієш масштаб допомоги ШІ».
62. [Архітектура та наука] «Закони масштабування дають нам компас у тумані невизначеності на шляху до надінтелекту».
63. [Філософія майбутнього] «Коли ми працювали в Google Brain та OpenAI, ми збирали пазл, який тепер склався в повноцінну індустрію Anthropic».
64. [Філософія майбутнього] «Машини майбутнього стануть нашими інтелектуальними партнерами у всіх сферах наукового пошуку».
65. [Етика та безпека ШІ] «Кожна помилка моделі при тестуванні на безпеку — це цінний урок для покращення нашої конституції».
66. [Філософія майбутнього] «Коли ми говоримо про машини милосердя, ми віримо у світ, де технології служать захисту найслабших».
67. [Походження та гарт] «Ефективний захист майбутнього вимагає прагматичного розрахунку і глибокої емпатії до людей».
68. [Етика та безпека ШІ] «Коли обчислення подвоюються кожні кілька місяців, наші протоколи безпеки мають еволюціонувати ще швидше».
69. [Етика та безпека ШІ] «Ми створюємо інфраструктуру розуму, яка допоможе людству подолати власні обмеження».
70. [Архітектура та наука] «Коли вчені об'єднують зусилля з моделями Claude, народжуються відкриття, на які раніше йшли десятиліття».
71. [Філософія майбутнього] «Природа створила біологічне життя через мільярди років виснажливої еволюції, а ми створюємо цифрову еволюцію за роки».
72. [Етика та безпека ШІ] «Коли ми аналізуємо ризики, ми розглядаємо найгірші сценарії, щоб ніколи не допустити їх у реальності».
73. [Етика та безпека ШІ] «Справжній лідер технологій має бути готовим зупинити випуск моделі, якщо вона не відповідає критеріям безпеки».
74. [Етика та безпека ШІ] «Коли ми закладали принципи Anthropic, ми хотіли довести, що етика та комерційний успіх можуть йти пліч-о-пліч».
75. [Етика та безпека ШІ] «Кожна нова лабораторія безпеки робить увесь світ дещо стійкішим перед обличчям невідомого».
76. [Філософія майбутнього] «Коли моделі демонструють здатність до самокритики, ми бачимо зачатки справжньої інженерної рефлексії».
77. [Кризи та стійкість] «Наука вимагає повної відмови від гордині та готовності вчитися у власних експериментів».
78. [Філософія майбутнього] «Коли ми дивимося на динаміку індустрії, ми знаємо, що виграють ті, хто робить ставку на надійність і якість даних».
79. [Лідерство та екосистема] «Ми маємо забезпечити, щоб бідні країни також отримали доступ до рятівних медичних та освітніх переваг ШІ».
80. [Етика та безпека ШІ] «Коли ти бачиш радість молодих вчених, які працюють над безпекою, ти знаєш, що наше майбутнє в надійних руках».
81. [Походження та гарт] «Фізичні процеси в мозку та процеси в кремнії підпорядковані загальній математиці інформації».
82. [Етика та безпека ШІ] «Коли ми створювали принципи для моделі, ми спиралися на найкращі етичні кодекси людства».
83. [Філософія майбутнього] «Не бійтеся складних компромісів, якщо вони ведуть до створення довговічних і надійних систем».
84. [Етика та безпека ШІ] «Коли моделі пишуть код і знаходять вразливості, ми бачимо їхню двояку природу, яку маємо строго контролювати».
85. [Кризи та стійкість] «Ефективний альтруїзм вчить нас максимізувати користь для найбільшої кількості живих істот у довгостроковій перспективі».
86. [Лідерство та екосистема] «Коли ми аналізуємо ефективність наших капіталовкладень, ми бачимо колосальну результативність невеликих, але талановитих команд».
87. [Філософія майбутнього] «Ми прагнемо створити інтелект, який поважатиме людську автономію і не намагатиметься маніпулювати людьми».
88. [Походження та гарт] «Коли закони математики збігаються з етичними принципами, ми отримуємо міцний і стійкий фундамент компанії».
89. [Архітектура та наука] «Кожен новий етап масштабування приносить нові виклики інтерпретованості, які ми зобов'язані розв'язати».
90. [Філософія майбутнього] «Природа подарувала нам розум для того, щоб ми досліджували Всесвіт і рятували життя від руйнування».
91. [Філософія майбутнього] «Коли ми дивимося на результати роботи наших дослідників, ми бачимо тріумф раціонального мислення».
92. [Філософія майбутнього] «Ми маємо зробити все можливе, щоб технологія слугувала джерелом радості й миру, а не тривоги».
93. [Походження та гарт] «Коли моделі допомагають моделювати кліматичні зміни, ми отримуємо шанс врятувати екосистеми планети».
94. [Етика та безпека ШІ] «Справжня сила компанії вимірюється її здатністю сказати "ні" прибутку заради дотримання принципів безпеки».
95. [Етика та безпека ШІ] «Коли ми об'єднуємо біофізику, машинне навчання та етику, ми створюємо нову професію майбутнього».
96. [Етика та безпека ШІ] «Кожен успішний крок Anthropic доводить, що відповідальний підхід може бути лідером ринку».
97. [Філософія майбутнього] «Ми прагнемо побудувати світ, у якому надінтелект є нашим найкращим другом і захисником».
98. [Кризи та стійкість] «Коли ми дивимося в майбутнє, ми бачимо не стіну катастрофи, а найбільшу медичну і соціальну революцію в історії».
99. [Етика та безпека ШІ] «Етика і масштабування мають стати єдиним цілим в архітектурі будь-якої передової системи».
100. [Архітектура та наука] «Ми почали цей шлях заради порятунку людей і ми доведемо його до кінця з абсолютною відданістю істині».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1223 слів): `02_SCRIPTS/episode_07_amodei/director_script_amodei.md`*

### АКТ 1. Прінстонська сітківка та закони масштабу (0:00 – 5:00)
*Музика: Suno Pro — `EP07_MUS_01_ACT1_92BPM_Princeton_Retina.wav`*
* **0:00 - 0:25** | [SFX: Тонкий пульс електрофізіологічного сигналу, низький ембієнт] | **Диктор:** Деякі вчені женуться за гучними міфами, а інші терпляче вивчають фундаментальну фізику процесів. Даріо Амодей починав як біофізик, досліджуючи в Прінстоні те, як нейрони сітківки перетворюють світло на код.
* **0:25 - 2:30** |  | **Диктор:** Перехід у великий ШІ через Baidu та Google Brain. У 2016 році він приєднується до OpenAI, очолюючи безпеку та розробку GPT-2 і GPT-3.
* **2:30 - 5:00** | [VIDEO: `EP07_VID_01_Biophysics_Lab.txt`] | **Диктор:** Формулювання емпіричних законів масштабування (Scaling Laws). Висновок простий: якість розуму росте передбачувано з обчисленнями.

### АКТ 2. Розрив з OpenAI та народження Anthropic (5:00 – 10:30)
*Музика: Suno Pro — `EP07_MUS_05_ACT2_92BPM_Scaling_Laws.wav`*
* **5:00 - 8:00** |  | **Диктор:** 2020–2021 роки. Зростаюча прірва між комерційною гонкою та безпекою. Даріо та його сестра Даніела разом із провідними дослідниками залишають OpenAI.
* **8:00 - 10:30** | [SFX: Звук закриття важких шлюзових дверей, чистий синт] | **Диктор:** Заснування Anthropic. Ставка на капітальну ефективність, невелику талановиту команду та створення безпечних моделей сімейства Claude.

### АКТ 3. Конституційний ШІ та інженерія безпеки (10:30 – 16:00)
*Музика: Suno Pro — `EP07_MUS_09_ACT3_92BPM_Constitutional_AI.wav`*
* **10:30 - 13:15** |  | **Диктор:** Винахід Конституційного ШІ (Constitutional AI). Замість закритих цензорів — прозорий звід етичних принципів, за яким модель сама налаштовує свою поведінку.
* **13:15 - 16:00** | [VIDEO: `EP07_VID_02_Constitutional_Grid.txt`] | **Диктор:** Прориви в біології та програмуванні. Використання Claude для пошуку нових ліків і пришвидшення медичних досліджень.

### АКТ 4. Маніфест «Machines of Loving Grace» (16:00 – 20:30)
*Музика: Suno Pro — `EP07_MUS_13_ACT4_92BPM_Loving_Grace.wav`*
* **16:00 - 18:30** |  | **Диктор:** Публікація маніфесту «Machines of Loving Grace». Відмова від апокаліптичного песимізму: ШІ здатний реально вилікувати хвороби і подвоїти здорове життя людей.
* **18:30 - 20:30** | [SFX: Теплий, гармонійний фінальний акорд] | **Диктор:** *«Безпека не є гальмом прогресу — вона є єдиною дорогою, яка дозволяє взагалі дістатися до фінішу»*.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP07_MUS_01_ACT1_92BPM_Princeton_Retina.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Princeton Retina', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP07_AMB_02_ACT1_DRONE_Retina_Pulse.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Retina Pulse', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP07_MUS_03_ACT1_92BPM_Google_Brain_Days.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Google Brain Days', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP07_MUS_04_ACT1_92BPM_Scaling_Laws_Discovery.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Scaling Laws Discovery', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP07_MUS_05_ACT2_92BPM_Scaling_Laws.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Scaling Laws', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP07_MUS_06_ACT2_92BPM_OpenAI_Departure.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'OpenAI Departure', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP07_AMB_07_ACT2_DRONE_Anthropic_Birth.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Anthropic Birth', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP07_MUS_08_ACT2_92BPM_Claude_First_Step.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Claude First Step', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP07_MUS_09_ACT3_92BPM_Constitutional_AI.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Constitutional AI', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP07_AMB_10_ACT3_DRONE_Ethics_Matrix.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Ethics Matrix', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP07_MUS_11_ACT3_92BPM_Biology_Breakthrough.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Biology Breakthrough', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP07_MUS_12_ACT3_92BPM_Safety_First.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Safety First', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP07_MUS_13_ACT4_92BPM_Loving_Grace.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Loving Grace', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP07_MUS_14_ACT4_92BPM_Longevity_Vision.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Longevity Vision', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP07_MUS_15_ACT4_92BPM_Optimistic_Future_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental precision biophysical trip-hop, 92 bpm, soft electrophysiological pulse percussion, warm felt piano, luminous modular synth pads, calm rational clarity, cue theme 'Optimistic Future Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP07_SFX_16_GLOBAL_Biophysics_Transitions.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Transitions': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP07_VO_UA_01_ACT1_Princeton_Biophysics.wav` | `EP07_VO_EN_01_ACT1_Princeton_Biophysics.wav` (ACT1 — Princeton Biophysics)
* `EP07_VO_UA_02_ACT1_Empirical_Scaling.wav` | `EP07_VO_EN_02_ACT1_Empirical_Scaling.wav` (ACT1 — Empirical Scaling)
* `EP07_VO_UA_03_ACT2_Anthropic_Founding.wav` | `EP07_VO_EN_03_ACT2_Anthropic_Founding.wav` (ACT2 — Anthropic Founding)
* `EP07_VO_UA_04_ACT2_Safety_Road.wav` | `EP07_VO_EN_04_ACT2_Safety_Road.wav` (ACT2 — Safety Road)
* `EP07_VO_UA_05_ACT3_Constitutional_Framework.wav` | `EP07_VO_EN_05_ACT3_Constitutional_Framework.wav` (ACT3 — Constitutional Framework)
* `EP07_VO_UA_06_ACT3_Medical_Aids.wav` | `EP07_VO_EN_06_ACT3_Medical_Aids.wav` (ACT3 — Medical Aids)
* `EP07_VO_UA_07_ACT4_Loving_Grace_Manifesto.wav` | `EP07_VO_EN_07_ACT4_Loving_Grace_Manifesto.wav` (ACT4 — Loving Grace Manifesto)
* `EP07_VO_UA_08_ACT4_Healthy_Future.wav` | `EP07_VO_EN_08_ACT4_Healthy_Future.wav` (ACT4 — Healthy Future)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP07_VID_001_ACT1_24FPS_Biophysics_Lab.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Як приборкати вогонь, який розумніший за того, хто його запалив?
     - *Veo Prompt:* `Cinematic macro shot of a single retinal neuron firing electrical impulses under a confocal microscope, glowing cyan bioluminescence on dark glass slide, 35mm film grain, 4k 24fps.`
002. `EP07_VID_002_ACT1_24FPS_Constitutional_Grid.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Як приборкати вогонь, який розумніший за того, хто його запалив?
     - *Veo Prompt:* `A vast 3D geometric constitutional grid of ethical principles glowing in soft golden light, stabilizing chaotic neural data streams in a clean futuristic lab, 8k.`
003. `EP07_VID_003_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли фізики середини двадцятого століття розщепили ядро атома, вони мали справу зі сліпою силою природи.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP07_VID_004_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Алгоритми двадцять першого століття — це інша стихія.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP07_VID_005_ACT1_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Алгоритми двадцять першого століття — це інша стихія.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP07_VID_006_ACT1_24FPS_Architectural_Corridor_A1S06_Macro_Det.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це вогонь, який вміє думати, будувати плани і приховувати свої наміри.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP07_VID_007_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І щоб зазирнути всередину цього вогню без страху й ілюзій, історії знадобився не просто програміст — їй знадобився фізик із серцем біолога.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP07_VID_008_ACT1_24FPS_KeyScene_02_Hero_Workspace_Atmospher.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Сан-Франциско, кінець вісімдесятих.
     - *Veo Prompt:* `Sunlit 1988 San Francisco Mission District workshop: smell of Italian leather, an artisan father crafting leather goods while his young son Dario and daughter Daniela read books on astronomy and literature at a wooden bench, warm nostalgic Kodak look, 4k.`
009. `EP07_VID_009_ACT1_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [00:38 – 00:52 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Даріо Амодей та його молодша сестра Даніела ростуть у світі, де інженерна точність переплелася з глибокою людяністю.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP07_VID_010_ACT1_24FPS_Silicon_Light_Refraction_A1S10_Optical.mp4` [00:52 – 01:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Їхній батько, Ріккардо Амодей — італійський майстер художньої роботи зі шкірою з Тоскани, людина, яка свято вірила, що кожна річ, створена руками, повинна мати бе…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP07_VID_011_ACT1_24FPS_University_Archive_Hall_Silhouette_Moo.mp4` [01:05 – 01:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Їхня мати, Елена — бібліотекарка з Чикаго, яка наповнила дім книгами від античної філософії до астрофізики.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP07_VID_012_ACT1_24FPS_School_Auditorium_Stage_SlowMo_Insert.mp4` [01:18 – 01:32 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У школі Даріо демонструє феноменальний математичний талант, стаючи переможцем національних олімпіад з фізики.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP07_VID_013_ACT1_24FPS_University_Archive_Hall_Macro_Detail.mp4` [01:32 – 01:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але коли юнак навчається в університеті, у родину приходить біда: батько повільно згасає від рідкісної, невиліковної хвороби.
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP07_VID_014_ACT1_24FPS_KeyScene_03_Seoul_Move_37_Go_Stone.mp4` [01:45 – 02:00 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Найстрашніша іронія долі полягала в тому, що хвороба, яка забрала життя батька у 2006 році, через лічені роки після його смерті стала виліковною майже на сто відс…
     - *Veo Prompt:* `Somber hospital window at rain: a young physicist holding his father's hand, reflection of medical monitors merging with complex differential equations of human biology in the glass, emotional restraint, 4k.`
015. `EP07_VID_015_ACT1_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [02:00 – 02:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Найстрашніша іронія долі полягала в тому, що хвороба, яка забрала життя батька у 2006 році, через лічені роки після його смерті стала виліковною майже на сто відс…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP07_VID_016_ACT1_24FPS_Architectural_Corridor_A1S16_Overhead.mp4` [02:15 – 02:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Цей удар назавжди викарбував у свідомості Даріо Амодея відчуття ціни часу: кожен рік зволікання науки коштує мільйонів людських життів.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP07_VID_017_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [02:30 – 02:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але водночас медицина була безпорадною, бо біологія живого організму виявилася занадто складною для людського розуму.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP07_VID_018_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [02:45 – 03:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але водночас медицина була безпорадною, бо біологія живого організму виявилася занадто складною для людського розуму.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP07_VID_019_ACT1_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [03:00 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він залишає теоретичну фізику елементарних частинок і йде до Прінстона вивчати біофізику нейронних мереж.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP07_VID_020_ACT1_24FPS_KeyScene_04_University_Archive_Hall.mp4` [03:15 – 03:35 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У темній лабораторії Прінстона Амодей роками вивчає сітківку ока — тонкий шар нервової тканини, який перетворює світло на мову мозку.
     - *Veo Prompt:* `Close-up of a high-density multi-electrode array recording simultaneous signals from hundreds of ganglion cells, chaotic noise transforming on a monitor into clean mathematical scaling curves, Octane render, 8k.`
021. `EP07_VID_021_ACT1_24FPS_Retinal_Ganglion_Sparks_Anamorphic_Wid.mp4` [03:35 – 03:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він підключає масиви із сотень мікроелектродів до живих клітин і слухає їхній хор.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP07_VID_022_ACT1_24FPS_Retinal_Ganglion_Sparks_Tracking_Mediu.mp4` [03:55 – 04:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Один нейрон здається випадковим шумом.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP07_VID_023_ACT1_24FPS_Retinal_Ganglion_Sparks_Overhead_GodsE.mp4` [04:15 – 04:35 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Два нейрони — хаосом.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP07_VID_024_ACT1_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [04:35 – 04:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але коли ти записуєш сотні клітин одночасно і застосовуєш строгий апарат статистичної фізики, крізь шум раптом проступає залізна колективна гармонія.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP07_VID_025_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [04:55 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме тоді, дивлячись на білкові спектри й нейронні імпульси, Амодей усвідомлює: людський мозок вченого більше не здатен осягнути цю складність самотужки.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP07_VID_026_ACT2_24FPS_KeyScene_01_Hero_Workspace_Atmospher.mp4` [05:15 – 05:27 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Пройшовши крізь лабораторії Baidu Ендрю Ина та Google Brain, у 2016 році Даріо Амодей стає ключовим архітектором досліджень в OpenAI.
     - *Veo Prompt:* `Inside OpenAI research lab in 2019: a glowing logarithmic coordinate grid in dark 3D space where scattered data points align into a razor-sharp straight diagonal line (Scaling Laws), physicists watching in silence, 8k.`
027. `EP07_VID_027_ACT2_24FPS_Equation_Notebook_Macro_A2S02_Anamorph.mp4` [05:27 – 05:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На посаді віцепрезидента з науки він керує створенням моделей GPT-2 та GPT-3.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP07_VID_028_ACT2_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [05:38 – 05:50 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але там, де звичайні програмісти бачили просто вдалий код, фізик із Прінстона побачив закон природи.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP07_VID_029_ACT2_24FPS_Architectural_Corridor_A2S04_Overhead.mp4` [05:50 – 06:02 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2020 році разом зі своїм другом-фізиком Джаредом Капланом Амодей публікує роботу, яка назавжди змінила економіку планети — «Закони масштабування нейромережевих…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP07_VID_030_ACT2_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [06:02 – 06:13 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* (Scaling Laws).
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP07_VID_031_ACT2_24FPS_Hyperscale_Compute_Cluster_Silhouette.mp4` [06:13 – 06:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони нанесли на логарифмічну шкалу точність відповідей моделі залежно від трьох змінних: кількості обчислень, обсягу даних і числа параметрів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP07_VID_032_ACT2_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [06:25 – 06:37 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І побачили ідеально пряму лінію, яка тягнулася через сім порядків величини без жодного вигину!
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP07_VID_033_ACT2_24FPS_Macintosh_Logic_Board_Macro_Detail.mp4` [06:37 – 06:48 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* «Це виглядало не як комп'ютерна програма.
     - *Veo Prompt:* `Extreme macro push-in shot of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP07_VID_034_ACT2_24FPS_Architectural_Corridor_A2S09_Anamorphi.mp4` [06:48 – 07:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це виглядало як закон термодинаміки або гравітації.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP07_VID_035_ACT2_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [07:00 – 07:15 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Але відкриття цього закону поставило перед Амодеєм страшне питання.
     - *Veo Prompt:* `Dramatic fork in the road: a dimly lit San Francisco bridge in fog, seven silhouettes of top scientists walking away from a glowing corporate tower towards an uncharted horizon, 35mm cinematic look, 4k.`
036. `EP07_VID_036_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [07:15 – 07:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але відкриття цього закону поставило перед Амодеєм страшне питання.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP07_VID_037_ACT2_24FPS_Equation_Notebook_Macro_A2S12_Optical.mp4` [07:30 – 07:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо лінія масштабування не зупиниться — це означає, що за кілька років у руках людей опиниться сила, здатна як зцілити світ, так і спопелити його.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP07_VID_038_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [07:45 – 08:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Для такого реактора потрібна безпрецедентна система захисту та контролю.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP07_VID_039_ACT2_24FPS_Hyperscale_Compute_Cluster_SlowMo_Inse.mp4` [08:00 – 08:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Проте всередині OpenAI після приходу першого мільярда від Microsoft почала перемагати інша логіка — логіка швидких комерційних релізів і гонитви за ринком.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP07_VID_040_ACT2_24FPS_Boardroom_Fracture_Night_Macro_Detail.mp4` [08:15 – 08:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Наприкінці 2020 року Даріо Амодей, його сестра Даніела та ще п'ятеро провідних дослідників кладуть на стіл заяви про звільнення.
     - *Veo Prompt:* `Extreme macro push-in shot of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP07_VID_041_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S16_Anamor.mp4` [08:30 – 08:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони не влаштовують публічних скандалів і не дають інтерв'ю пресі.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP07_VID_042_ACT2_24FPS_Equation_Notebook_Macro_A2S17_Tracking.mp4` [08:45 – 09:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони просто виходять у ніч, щоб збудувати нову фортецю з нуля.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP07_VID_043_ACT2_24FPS_KeyScene_03_Silicon_Light_Refraction.mp4` [09:00 – 09:13 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Так у 2021 році народжується Anthropic.
     - *Veo Prompt:* `Minimalist architectural workspace of Anthropic: warm natural wood, glass boards filled with interpretability diagrams and the word "CLAUDE", atmosphere of calm academic rigor, 4k 24fps.`
044. `EP07_VID_044_ACT2_24FPS_Architectural_Corridor_A2S19_Optical_D.mp4` [09:13 – 09:26 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Так у 2021 році народжується Anthropic.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP07_VID_045_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [09:26 – 09:39 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Назва походить від грецького слова Anthropos — «людина».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP07_VID_046_ACT2_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [09:39 – 09:52 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Назва походить від грецького слова Anthropos — «людина».
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP07_VID_047_ACT2_24FPS_Monastic_White_Sanctuary_Macro_Detail.mp4` [09:52 – 10:06 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони реєструють компанію як Корпорацію суспільної користі (Public Benefit Corporation), де у статуті юридично закріплено: безпека людства стоїть вище за фінансові…
     - *Veo Prompt:* `Extreme macro push-in shot of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP07_VID_048_ACT2_24FPS_Constitutional_Crystal_Box_Anamorphic.mp4` [10:06 – 10:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони називають свою модель Claude — на честь Клода Шеннона, батька теорії інформації.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP07_VID_049_ACT2_24FPS_Constitutional_Crystal_Box_Tracking_Me.mp4` [10:19 – 10:32 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони називають свою модель Claude — на честь Клода Шеннона, батька теорії інформації.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP07_VID_050_ACT2_24FPS_Neural_Horizon_Pulse_A2S25_Overhead_Go.mp4` [10:32 – 10:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І формулюють головний принцип інженерії розуму: ви не маєте права масштабувати потужність двигуна швидше, ніж масштабуєте надійність гальм.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP07_VID_051_ACT3_24FPS_KeyScene_01_Silicon_Light_Refraction.mp4` [10:45 – 10:58 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Перша проблема, яку вирішує команда Амодея — як навчити надпотужну систему совісті?
     - *Veo Prompt:* `Symbolic visualization of Constitutional AI: an ancient parchment scroll of human rights morphing into a glowing geometric compass suspended inside the core of a neural network, guiding millions of light streams away from dark chaotic edges, Octane render, 8k.`
052. `EP07_VID_052_ACT3_24FPS_Architectural_Corridor_A3S02_SlowMo_In.mp4` [10:58 – 11:12 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перша проблема, яку вирішує команда Амодея — як навчити надпотужну систему совісті?
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP07_VID_053_ACT3_24FPS_Neural_Horizon_Pulse_A3S03_Macro_Detai.mp4` [11:12 – 11:25 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Старий метод індустрії (RLHF) полягав у тому, що тисячі низькооплачуваних операторів вручну ставили оцінки відповідям бота.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP07_VID_054_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S04_Anamor.mp4` [11:25 – 11:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але це тупик: по-перше, модель вчиться підлабузництву — вона починає брехати, щоб догодити людині; по-друге, коли ШІ стане розумнішим за людину, звичайний операто…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP07_VID_055_ACT3_24FPS_Constitutional_Crystal_Box_Tracking_Me.mp4` [11:38 – 11:52 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Амодей пропонує революцію — Конституційний штучний інтелект (Constitutional AI).
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP07_VID_056_ACT3_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [11:52 – 12:05 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Замість ручного дресирування моделі дають «Конституцію»
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP07_VID_057_ACT3_24FPS_Upwind_Atlantic_Sail_Optical_DataViz.mp4` [12:05 – 12:18 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* — відкритий звід етичних принципів, від Декларації прав людини ООН до правил нерозповсюдження зброї.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP07_VID_058_ACT3_24FPS_Constitutional_Crystal_Box_Silhouette.mp4` [12:18 – 12:32 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Під час навчання модель сама оцінює кожну свою думку крізь призму цієї Конституції, виправляючи себе мільйони разів на секунду.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP07_VID_059_ACT3_24FPS_Constitutional_Crystal_Box_SlowMo_Inse.mp4` [12:32 – 12:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Етика перестає бути зовнішнім намордником — вона стає внутрішнім характером розуму.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP07_VID_060_ACT3_24FPS_KeyScene_02_Equation_Notebook_Macro.mp4` [12:45 – 13:02 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Але як перевірити, чи модель справді стала чесною, чи вона лише прикидається слухняною під час іспиту, приховуючи всередині небезпечні цілі?
     - *Veo Prompt:* `Mechanistic Interpretability visualization: camera flies inside a dark opaque "Black Box" which suddenly turns transparent like crystal glass, revealing distinct glowing golden constellations for concepts like "Golden Gate Bridge", "Truth", and "Deception", 8k 24fps.`
061. `EP07_VID_061_ACT3_24FPS_Silicon_Light_Refraction_A3S11_Anamorp.mp4` [13:02 – 13:19 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але як перевірити, чи модель справді стала чесною, чи вона лише прикидається слухняною під час іспиту, приховуючи всередині небезпечні цілі?
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP07_VID_062_ACT3_24FPS_Hyperscale_Compute_Cluster_Tracking_Me.mp4` [13:19 – 13:36 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вся індустрія повторювала: «Нейромережа — це непізнавана чорна скринька з мільярдів незрозумілих чисел».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP07_VID_063_ACT3_24FPS_Hyperscale_Compute_Cluster_Overhead_Go.mp4` [13:36 – 13:52 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вся індустрія повторювала: «Нейромережа — це непізнавана чорна скринька з мільярдів незрозумілих чисел».
     - *Veo Prompt:* `Top-down vertical birds-eye composition of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP07_VID_064_ACT3_24FPS_University_Archive_Hall_Optical_DataVi.mp4` [13:52 – 14:09 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тут у Даріо Амодеї знову прокидається біофізик із Прінстона.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP07_VID_065_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [14:09 – 14:26 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він запускає програму Механістичної інтерпретованості (Mechanistic Interpretability) — створення першого в історії мікроскопа для штучного мозку.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP07_VID_066_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [14:26 – 14:43 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він запускає програму Механістичної інтерпретованості (Mechanistic Interpretability) — створення першого в історії мікроскопа для штучного мозку.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP07_VID_067_ACT3_24FPS_Constitutional_Crystal_Box_Macro_Detai.mp4` [14:43 – 15:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Навесні 2024 року вчені Anthropic здійснюють науковий подвиг: вони просвічують наскрізь робочу модель Claude 3 Sonnet і складають анатомічний атлас із мільйонів ї…
     - *Veo Prompt:* `Extreme macro push-in shot of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP07_VID_068_ACT3_24FPS_KeyScene_03_Constitutional_Crystal_B.mp4` [15:00 – 15:11 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Чорна скринька стала прозорою.
     - *Veo Prompt:* `High-security laboratory protocol panel showing "ASL-1, ASL-2, ASL-3, ASL-4" containment levels glowing in amber, heavy steel blast doors of cyber-defense locking into place, 4k.`
069. `EP07_VID_069_ACT3_24FPS_Constitutional_Crystal_Box_Tracking_Me.mp4` [15:11 – 15:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Чорна скринька стала прозорою.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP07_VID_070_ACT3_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [15:22 – 15:34 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тепер інженери можуть не просто читати те, що модель пише на екрані — вони можуть бачити на томографії ваг, чи не зароджується в її глибині брехня ще до першого с…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP07_VID_071_ACT3_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [15:34 – 15:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тепер інженери можуть не просто читати те, що модель пише на екрані — вони можуть бачити на томографії ваг, чи не зароджується в її глибині брехня ще до першого с…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP07_VID_072_ACT3_24FPS_Architectural_Corridor_A3S22_Silhouett.mp4` [15:45 – 15:56 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На додачу Амодей вводить залізний стандарт — Рівні безпеки ШІ (ASL-1 — ASL-4) за зразком біологічних лабораторій, що працюють зі смертельними вірусами.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP07_VID_073_ACT3_24FPS_Neural_Horizon_Pulse_A3S23_SlowMo_Inse.mp4` [15:56 – 16:08 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На додачу Амодей вводить залізний стандарт — Рівні безпеки ШІ (ASL-1 — ASL-4) за зразком біологічних лабораторій, що працюють зі смертельними вірусами.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP07_VID_074_ACT3_24FPS_Compression_Diamond_Lattice_Macro_Deta.mp4` [16:08 – 16:19 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Anthropic бере на себе публічну юридичну клятву: якщо під час тестів нова модель покаже здатність допомагати у створенні біологічної зброї чи автономних кібератак…
     - *Veo Prompt:* `Extreme macro push-in shot of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP07_VID_075_ACT3_24FPS_Compression_Diamond_Lattice_Anamorphic.mp4` [16:19 – 16:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Anthropic бере на себе публічну юридичну клятву: якщо під час тестів нова модель покаже здатність допомагати у створенні біологічної зброї чи автономних кібератак…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP07_VID_076_ACT4_24FPS_KeyScene_01_Constitutional_Crystal_B.mp4` [16:30 – 16:42 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Восени 2024 року Даріо Амодей сідає за стіл і пише трактат на п'ятнадцять тисяч слів під назвою «Machines of Loving Grace»
     - *Veo Prompt:* `Poetic dawn over a futuristic green city: inside a bright laboratory, a digital AI model simulates millions of cellular therapies in seconds, dissolving cancer cells into harmless light, warm golden sunrise, IMAX 8k.`
077. `EP07_VID_077_ACT4_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [16:42 – 16:53 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Восени 2024 року Даріо Амодей сідає за стіл і пише трактат на п'ятнадцять тисяч слів під назвою «Machines of Loving Grace»
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP07_VID_078_ACT4_24FPS_Equation_Notebook_Macro_A4S03_Silhouet.mp4` [16:53 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* («Машини сповненої любові благодаті»).
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP07_VID_079_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [17:05 – 17:17 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У ньому він пояснює світові те, заради чого він насправді так прискіпливо будує гальма та запобіжники.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP07_VID_080_ACT4_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [17:17 – 17:28 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він робить це не зі страху перед майбутнім — він робить це, щоб ніщо не завадило людству дійти до найбільшого тріумфу у своїй історії.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP07_VID_081_ACT4_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [17:28 – 17:40 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За розрахунками Амодея, щойно ми безпечно перетнемо поріг потужного ШІ — країни з «геніальною державою в дата-центрі»
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP07_VID_082_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S07_Tracki.mp4` [17:40 – 17:52 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* — ми за п'ять-десять років стиснемо ціле століття біології та медицини!
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP07_VID_083_ACT4_24FPS_Constitutional_Crystal_Box_Overhead_Go.mp4` [17:52 – 18:03 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми остаточно переможемо більшість видів раку, хворобу Альцгеймера, інфекційні епідемії, депресію та вдвічі подовжимо здорове людське життя.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP07_VID_084_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [18:03 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Жоден син і жодна донька на Землі більше не стоятимуть безпорадно біля ліжка батька, чиї ліки мали з'явитися всього на три роки пізніше.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP07_VID_085_ACT4_24FPS_KeyScene_02_Architectural_Corridor_A.mp4` [18:15 – 18:27 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які уроки мислення та честі дає нам історія Даріо Амодея?
     - *Veo Prompt:* `Macro shot of a finely stitched Tuscan leather notebook lying next to a glowing glass tablet displaying the Constitutional AI principles, warm afternoon light uniting human craftsmanship and digital ethics, 4k.`
086. `EP07_VID_086_ACT4_24FPS_Constitutional_Crystal_Box_SlowMo_Inse.mp4` [18:27 – 18:39 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Керуйтеся внутрішньою конституцією, а не оплесками натовпу.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP07_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:39 – 18:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Як слабка мовна модель деградує від бажання догодити кожному користувачеві, так і особистість руйнується від спроб подобатися всім.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP07_VID_088_ACT4_24FPS_Equation_Notebook_Macro_A4S13_Anamorph.mp4` [18:51 – 19:02 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ніколи не розганяйте систему швидше за ваші гальма.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP07_VID_089_ACT4_24FPS_Silicon_Light_Refraction_A4S14_Trackin.mp4` [19:02 – 19:14 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Великі амбіції без самоконтролю та управління ризиками неминуче ведуть до катастрофи.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP07_VID_090_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [19:14 – 19:26 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Будуйте власні запобіжники та межі допустимого ще тоді, коли справи йдуть спокійно.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP07_VID_091_ACT4_24FPS_Neural_Horizon_Pulse_A4S16_Optical_Dat.mp4` [19:26 – 19:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Не задовольняйтеся тим, що щось у вашому житті чи бізнесі «просто якось працює»
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP07_VID_092_ACT4_24FPS_Constitutional_Crystal_Box_Silhouette.mp4` [19:38 – 19:50 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* як чорна скринька.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP07_VID_093_ACT4_24FPS_KeyScene_03_Equation_Notebook_Macro.mp4` [19:50 – 20:01 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Справжня сила ніколи не буває галасливою чи безвідповідальною.
     - *Veo Prompt:* `Slow majestic camera pull-back from a glowing retina cell into a vast, peaceful Earth bathed in golden morning light, where technology and living nature exist in seamless grace, 8k 24fps.`
094. `EP07_VID_094_ACT4_24FPS_Silicon_Light_Refraction_A4S19_Macro_D.mp4` [20:01 – 20:11 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила ніколи не буває галасливою чи безвідповідальною.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP07_VID_095_ACT4_24FPS_Architectural_Corridor_A4S20_Anamorphi.mp4` [20:11 – 20:22 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила ніколи не буває галасливою чи безвідповідальною.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP07_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:22 – 20:32 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила ніколи не буває галасливою чи безвідповідальною.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cyan bioluminescent retinal neurons under Princeton confocal microscope, razor-sharp logarithmic Scaling Laws grid, transparent crystal black-box interpretability constellations, warm Tuscan leather and sunlit greenery, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP07_VID_097_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [20:32 – 20:43 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила — це тиха зосередженість майстра, який знає: найвище призначення розуму у Всесвіті полягає не у владі над слабкими, а в захисті крихкого дива людськ…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP07_VID_098_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [20:43 – 20:54 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила — це тиха зосередженість майстра, який знає: найвище призначення розуму у Всесвіті полягає не у владі над слабкими, а в захисті крихкого дива людськ…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP07_VID_099_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [20:54 – 21:04 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила — це тиха зосередженість майстра, який знає: найвище призначення розуму у Всесвіті полягає не у владі над слабкими, а в захисті крихкого дива людськ…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP07_VID_100_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [21:04 – 21:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжня сила — це тиха зосередженість майстра, який знає: найвище призначення розуму у Всесвіті полягає не у владі над слабкими, а в захисті крихкого дива людськ…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Zeiss Master Anamorphic 50mm & Microscopic Optics, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
