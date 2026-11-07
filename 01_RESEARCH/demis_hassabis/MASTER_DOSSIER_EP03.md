# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 03 — ДЕМІС ГАССАБІС
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Гросмейстер біологічного коду»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP03 (Деміс Гассабіс) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP03.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP03_VO_, EP03_MUS_, EP03_AMB_, EP03_SFX_, EP03_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1465 слів, хронометраж 21:30 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP03_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP03_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP03_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP03_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP03_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP03_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP03_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP03_demis_hassabis_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP03_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP03_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження:** Народився 27 липня 1976 року в Лондоні в родині греко-кіпріота та китайської малайки.
* **Шаховий вундеркінд:** У 13 років став шаховим майстром і другим за рейтингом гравцем до 14 років у світі (поступався лише Юдіт Полгар). Заробляв на карманні гроші грою в шахи на стрічках лондонських турнірів.
* **Гейм-дизайн (Theme Park):** У 17 років заробив перші значні кошти й авторитет, спроєктувавши та запрограмувавши культову відеоігру *Theme Park* під керівництвом Пітера Моліньє.
* **Кембридж та нейробіологія (UCL):** Здобув диплом з інформатики в Кембриджі (1997), заснував студію Elixir Studios, а згодом захистив докторський ступінь (PhD) з когнітивної нейробіології в Університетському коледжі Лондона (UCL, 2009), відкривши ключові механізми людської пам'яті та уяви.
* **DeepMind та Перемога над Го (2010–2016):** Співзасновник DeepMind (2010). У березні 2016 року історична перемога AlphaGo над чемпіоном світу Лі Седолем у Сеулі (знаменитий Хід 37), що перевернула уявлення людства про інтуїцію штучного інтелекту.
* **AlphaFold та Нобелівська премія (2020–2024):** Розв'язання 50-річної біологічної проблеми згортання білків за допомогою AlphaFold2. У жовтні 2024 року Деміс Гассабіс стає лауреатом **Нобелівської премії з хімії**.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ДЕМІС ГАССАБІС)

1. [Філософія майбутнього] «Розв'язати інтелект, а потім використати його для розв'язання всього іншого — ось єдина справжня місія нашого покоління».
2. [Філософія майбутнього] «Шахи навчили мене головного: кожна дія має наслідки, і ти повинен прораховувати свої кроки на кілька рівнів уперед, не піддаючись емоціям».
3. [Філософія майбутнього] «Коли у тринадцять років я грав на турнірах проти дорослих гросмейстерів, я зрозумів, що перемагає не той, хто швидше перебирає варіанти, а той, хто бачить глибинну гармонію позиції».
4. [Філософія майбутнього] «Комп'ютерні ігри та штучний інтелект мають спільне коріння: це пісочниці для перевірки меж можливого в умовах обмежених ресурсів».
5. [Філософія майбутнього] «Коли ми створювали Theme Park у сімнадцять років, я усвідомив силу симуляції: світ можна розкласти на правила, які породжують складну поведінку».
6. [Філософія майбутнього] «Нейробіологія людського мозку — це найвитонченіший витвір еволюції. Ми вивчаємо його не заради цікавості, а щоб зрозуміти архітектуру майбутнього розуму».
7. [Кризи та стійкість] «У 2010 році, коли ми засновували DeepMind у скромному лондонському офісі, більшість інвесторів вважали нейромережі мертвою тупиковою гілкою».
8. [Етика та безпека ШІ] «Система AlphaGo не просто переграла людину в шахи чи го. Вона знайшла нові естетичні ходи, які людство не відкривало тисячоліттями».
9. [Філософія майбутнього] «Хід 37 у матчі проти Лі Седоля був моментом, коли машина продемонструвала те, що ми називаємо творчою інтуїцією».
10. [Архітектура та наука] «Проблема згортання білків вважалася неприступною горою біології протягом п'ятдесяти років. Ми знали, що якщо здолаємо її за допомогою ШІ, перед нами відкриється вся фармакологія майбутнього».
11. [Архітектура та наука] «AlphaFold2 не просто перебирала форми молекул; вона зрозуміла тривимірну фізику амінокислотних ланцюгів на рівні законів квантової хімії».
12. [Етика та безпека ШІ] «Наука — це найблагородніша гра у світі, де правилами є самі закони природи, а призом — нове знання для всього людства».
13. [Етика та безпека ШІ] «Ми маємо підходити до безпеки надінтелекту з такою ж суворістю, з якою інженери-ядерники проєктують захисні оболонки реакторів».
14. [Походження та гарт] «Немає жодної містики у свідомості чи інтелекті. Це складні інформаційні структури, які піддаються математичному аналізу та відтворенню в кремнії».
15. [Філософія майбутнього] «Коли ти занурюєшся у вивчення гіпокампа, ти розумієш, наскільки елегантно мозок оптимізує пам'ять для прийняття рішень в умовах невизначеності».
16. [Філософія майбутнього] «Будь-яка складна проблема розпадається на прості компоненти, якщо ви готові терпляче вибудувати правильну ієрархію абстракцій».
17. [Філософія майбутнього] «Ми створили DeepMind не для того, щоб створювати розважальні додатки чи заробляти на рекламі. Наша мета — фундамент фундаментальних знань».
18. [Філософія майбутнього] «Спільна робота шахового гравця, нейробіолога і програміста дає унікальний погляд на те, як вирішувати завдання, які здаються нерозв'язними».
19. [Архітектура та наука] «Коли AlphaFold розкрив структуру практично кожного відомого білка на Землі, ми побачили, як цифрова наука зливається з життєвою матерією».
20. [Етика та безпека ШІ] «Етика і розвиток ШІ мають йти рука об руку. Не можна створювати потужні інструменти без ретельного прорахунку довгострокових наслідків».
21. [Походження та гарт] «Мій батько прищепив мені любов до логіки, а мати — відкритість до творчості. На стику цих двох світів і народжуються справжні прориви».
22. [Походження та гарт] «У дитинстві я міг годинами сидіти над дошкою, аналізуючи партії колишніх чемпіонів світу. Це виховує дисципліну мислення».
23. [Етика та безпека ШІ] «Коли ми перейшли від ігор до реальних наукових завдань у біології та фізиці, ми зрозуміли справжній масштаб користі штучного інтелекту для людства».
24. [Філософія майбутнього] «Штучний інтелект у медицині дозволить вилікувати хвороби, які століттями вважалися вироком для людини».
25. [Етика та безпека ШІ] «Кожна невдача в лабораторії — це лише один відкинутий неробочий гіпотетичний хід у величезному дереві пошуку».
26. [Філософія майбутнього] «У світі є стільки прекрасних і таємничих речей, що витрачати час на дріб'язкові суперечки просто неприпустимо».
27. [Лідерство та екосистема] «Коли ти керуєш командою найкращих вчених планети, твоє завдання — не заважати їм творити, а забезпечити максимальну концентрацію енергії».
28. [Архітектура та наука] «Нобелівська премія з хімії за AlphaFold — це перемога не однієї команди, це тріумф усього напрямку штучного інтелекту в науці».
29. [Лідерство та екосистема] «Ми стоїмо на порозі нової епохи Відродження, де комп'ютери стануть повноцінними партнерами вчених у відкритті законів Всесвіту».
30. [Філософія майбутнього] «Формування правильної цільової функції — це найголовніше і водночас найскладніше завдання при проєктуванні адаптивного агента».
31. [Етика та безпека ШІ] «Успіх вимірюється не кількістю патентів, а тим, наскільки фундаментально ти змінив здатність людства розуміти реальність».
32. [Лідерство та екосистема] «Коли гравець у го робить дивний хід, спершу всі сміються, а потім виявляється, що це був геніальний стратегічний прорив. ШІ вчить нас бути відкритими до незвичного».
33. [Філософія майбутнього] «Мозок дитини — це найпотужніша у світі машина навчання з підкріпленням і мінімальною кількістю початкових даних».
34. [Філософія майбутнього] «Ми маємо подбати про те, щоб переваги штучного інтелекту були доступні кожній людині на Землі, а не лише привілейованим корпораціям».
35. [Лідерство та екосистема] «Термоядерний синтез — це наступний великий виклик для нашої команди, де ШІ має допомогти приборкати плазму».
36. [Філософія майбутнього] «Коли ти дивишся на складність клітинних процесів, ти відчуваєш глибоке благоговіння перед інженерією самої природи».
37. [Архітектура та наука] «Ніколи не бійтеся амбітних цілей. Якщо ваша мета лякає своєю масштабністю, значить, ви на правильному шляху».
38. [Кризи та стійкість] «Шахи вчать нас жертвувати пішаками заради стратегічної ініціативи. У науці теж доводиться відмовлятися від зручних ілюзій заради істини».
39. [Філософія майбутнього] «Справжній інтелект не обмежується здатністю запам'ятовувати факти; він полягає у здатності узагальнювати досвід у нових ситуаціях».
40. [Філософія майбутнього] «Коли ми запускали симуляції в DeepMind, ми щоразу чекали на момент, коли мережа почне дивувати власних творців».
41. [Філософія майбутнього] «Дисципліна розуму виробляється роками щоденних тренувань і розв'язання задач на межі людських можливостей».
42. [Етика та безпека ШІ] «Технології самі по собі нейтральні. Наша відповідальність полягає в тому, щоб направити їх на подолання глобальних криз».
43. [Архітектура та наука] «Коли я був підлітком, комп'ютери були повільними і обмеженими, але саме це змушувало нас писати неймовірно ефективний код».
44. [Лідерство та екосистема] «Машинне навчання сьогодні нагадує епоху великих географічних відкриттів: ми щодня знаходимо нові континенти у просторі даних».
45. [Філософія майбутнього] «Головний ворог інновацій — це самовдоволення та сліпа віра в те, що старі методи працюватимуть вічно».
46. [Кризи та стійкість] «Коли ми розробляли AlphaGo, ми свідомо відмовилися від жорстко закладених людських баз партій на етапі навчання з підкріпленням, щоб мережа шукала власну істину».
47. [Етика та безпека ШІ] «Науковий метод у поєднанні з потужністю нейромереж здатен пришвидшити прогрес людства в сотні разів».
48. [Кризи та стійкість] «Коли ти виграєш партію, проаналізуй її так само суворо, як і в разі програшу — перемога часто приховує випадкові помилки».
49. [Філософія майбутнього] «Ми прагнемо створити загальний штучний інтелект, який стане надійним інструментом для вирішення будь-яких наукових завдань».
50. [Філософія майбутнього] «Кожна молекула у нашому тілі — це шедевр природного дизайну, який тепер ми можемо розшифрувати».
51. [Кризи та стійкість] «Коли світ сумнівався у нас на старті, ми зосередилися на роботі з рівняннями, а не на PR-кампаніях».
52. [Філософія майбутнього] «Інтелект — це здатність знаходити порядок у хаосі та використовувати його для досягнення цілі».
53. [Архітектура та наука] «Коли ти спостерігаєш за грою найкращих гравців планети, ти бачиш інтуїцію в дії — процес, який ми намагаємося перенести в алгоритми».
54. [Філософія майбутнього] «Світ вимагає від нас глибокого занурення в суть речей, а не поверхневих трендів та одноденних рішень».
55. [Філософія майбутнього] «Ми маємо виховувати нове покоління вчених, які вільно володіють як біологією, так і сучасними методами обчислювального інтелекту».
56. [Кризи та стійкість] «Коли ми перетнули межу в Го, це стало психологічним бар'єром для всього світу: люди зрозуміли, що інтуїція більше не є виключною монополією людини».
57. [Лідерство та екосистема] «Кожне відкриття в біології відкриває двері до нових питань про те, як влаштоване життя на найглибшому рівні».
58. [Філософія майбутнього] «Ми ніколи не зупинимося на досягнутому, бо горизонт людського пізнання не має меж».
59. [Архітектура та наука] «Коли ти проєктуєш архітектуру нейромережі, ти по суті закладаєш закони еволюції для майбутнього цифрового середовища».
60. [Філософія майбутнього] «Наука вимагає повної самовіддачі та щирої пристрасті до розгадки таємниць Всесвіту».
61. [Походження та гарт] «У дитинстві я витратив усі свої заощадження на один із перших комп'ютерів, і це була найкраща інвестиція в моєму житті».
62. [Філософія майбутнього] «Шахова партія — це мініатюрна модель життя, де кожне рішення має свою ціну».
63. [Архітектура та наука] «Коли ми вперше побачили результати AlphaFold, ми зрозуміли, що медицина майбутнього буде зовсім іншою».
64. [Етика та безпека ШІ] «Штучний інтелект стане каталізатором для розв'язання найскладніших екологічних та енергетичних проблем планети».
65. [Філософія майбутнього] «Не бійтеся складних викликів. Саме вони перетворюють звичайного фахівця на справжнього творця».
66. [Філософія майбутнього] «Коли ми аналізуємо діяльність мозку, нас вражає його енергоефективність порівняно з сучасними дата-центрами».
67. [Походження та гарт] «Ми будуємо майбутнє, в якому кожен лікар матиме в руках інструмент для проєктування ліків на молекулярному рівні за лічені хвилини».
68. [Філософія майбутнього] «Кожен великий крок уперед починається зі сміливої гіпотези, яка суперечить загальноприйнятим поглядам».
69. [Філософія майбутнього] «Ми маємо підтримувати баланс між комерційною реалізацією та академічною свободою фундаментальних досліджень».
70. [Архітектура та наука] «Коли команда об'єднана спільною великою місією, будь-які перешкоди стають лише тимчасовими етапами на шляху».
71. [Філософія майбутнього] «Інтелект — це найцінніший ресурс у Всесвіті, здатний перетворювати енергію та матерію на розуміння».
72. [Етика та безпека ШІ] «Коли ми грали матчі в Сеулі, я відчував колосальну відповідальність не лише за нашу компанію, а за весь науковий напрямок».
73. [Архітектура та наука] «Сучасні моделі нагадують нам, скільки ще незвіданого приховано у просторі багатовимірних векторів».
74. [Філософія майбутнього] «Ми повинні навчати машини не просто наслідувати людей, а перевершувати нас у логіці та об'єктивності».
75. [Архітектура та наука] «Коли ти розв'язуєш задачу світового масштабу, кожна хвилина зосередженості має значення».
76. [Філософія майбутнього] «Природа еволюціонувала мільярди років методом випадкових мутацій; ми ж можемо спрямовувати еволюцію за допомогою розуму».
77. [Архітектура та наука] «Коли ми дивимося на результати роботи наших алгоритмів, ми бачимо тріумф людської думки, яка зуміла створити нові форми пізнання».
78. [Архітектура та наука] «Наука не терпить недбалості. Кожна строчка коду і кожна формула мають бути бездоганними».
79. [Філософія майбутнього] «Ми прагнемо створити систему, яка зможе самостійно формулювати нові наукові теорії та перевіряти їх експериментально».
80. [Філософія майбутнього] «Коли у нас виникає складний тупик у проєкті, найкраще рішення — повернутися до першопричин і переосмислити базові аксіоми».
81. [Кризи та стійкість] «Шахова інтуїція — це результат підсвідомого опрацювання тисяч паттернів. Нейромережі працюють за схожим принципом на незрівнянно більших масивах».
82. [Філософія майбутнього] «Ми маємо бути готовими до того, що надінтелект змінить економіку, суспільство і саму природу людської діяльності».
83. [Філософія майбутнього] «Коли ти бачиш радість в очах біологів, яким ми зекономили роки виснажливої лабораторної праці, ти розумієш справжню цінність нашої роботи».
84. [Лідерство та екосистема] «Немає вищої нагороди для дослідника, ніж бачити, як його фундаментальне відкриття рятує життя людей».
85. [Філософія майбутнього] «Кожна гра в го — це полотно, на якому суперники малюють стратегічний баланс сил».
86. [Етика та безпека ШІ] «Ми створюємо інфраструктуру майбутнього розуму, і кожен наш крок має бути вивіреним та етично бездоганним».
87. [Філософія майбутнього] «Коли ми об'єднуємо нейробіологію та машинне навчання, ми відкриваємо нові горизонти для обох дисциплін».
88. [Етика та безпека ШІ] «Справжній лідер проекту бере на себе відповідальність за найскладніші ризики і залишається спокійним у кризові моменти».
89. [Філософія майбутнього] «Ми віримо у світ, де технології допомагають розкрити безмежний потенціал кожного пацієнта та вченого».
90. [Походження та гарт] «Коли ти досліджуєш космос чи структуру білка, ти відчуваєш однакову велич математичного порядку Всесвіту».
91. [Філософія майбутнього] «Ми маємо продовжувати інвестувати у фундаментальні дослідження, бо саме вони є джерелом усіх майбутніх технологічних революцій».
92. [Лідерство та екосистема] «Коли ми перемагали в Сеулі, це був тріумф не лише машин, а й десятиліть наполегливої праці всієї нашої команди».
93. [Філософія майбутнього] «Інтелект є найпотужнішим інструментом подолання будь-яких обмежень, які ставить перед нами фізичний світ».
94. [Кризи та стійкість] «Коли ми проєктували AlphaFold2, ми відмовилися від старих шаблонів і побудували повністю нову архітектуру на базі механізмів уваги».
95. [Філософія майбутнього] «Наука рухається вперед завдяки сміливцям, які не бояться кинути виклик столітнім догмам».
96. [Етика та безпека ШІ] «Коли ми дивимося на майбутнє, ми бачимо не загрозу, а грандіозне запрошення до найбільшого наукового прориву в історії цивілізації».
97. [Кризи та стійкість] «Кожна розв'язана задача відкриває три нові, ще більш захоплюючі та складні загадки».
98. [Філософія майбутнього] «Ми маємо зберегти допитливість дитини і мудрість інженера, щоб побудувати безпечний та гармонійний світ з ШІ».
99. [Філософія майбутнього] «Коли ти віддаєшся науці без залишку, вона відкриває тобі свої найпотаємніші та найпрекрасніші секрети».
100. [Філософія майбутнього] «Розв'язати інтелект — це лише початок. Справжня робота почнеться тоді, коли цей інтелект допоможе нам розв'язати всі інші таємниці буття».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1465 слів): `02_SCRIPTS/episode_03_hassabis/director_script_hassabis.md`*

### АКТ 1. Дерев'яні лицарі та перші симуляції (0:00 – 5:15)
*Музика: Suno Pro — `EP03_MUS_01_ACT1_92BPM_Wooden_Knights.wav`*
* **0:00 - 0:25** | [SFX: М'який стукіт дерев'яної шахової фігури по дошці. Тихе гудіння старих процесорів.] | **Диктор:** Лондон, 1989 рік. Тринадцятирічний хлопчик сидить перед шахівницею, прораховуючи комбінації на десять ходів уперед. Для нього світ — це чиста геометрія логіки.
* **0:25 - 2:30** |  | **Диктор:** У сімнадцять років Деміс Гассабіс заробляє власні кошти на розробці культової гри *Theme Park*. Він розуміє головне: світ можна перекласти на правила і симуляції. Але ігор йому мало. Він іде в Кембридж, а згодом — у нейробіологію UCL.
* **2:30 - 5:15** | [VIDEO: `EP03_VID_01_Chess_Board.txt`] | **Диктор:** Вивчаючи гіпокамп і пам'ять людини, він усвідомлює ключ до справжнього штучного інтелекту: машини мають не просто сліпо перебирати варіанти, а вчитися інтуїції через досвід.

### АКТ 2. Народження DeepMind та Хід 37 у Сеулі (5:15 – 10:30)
*Музика: Suno Pro — `EP03_MUS_05_ACT2_92BPM_Move_37_Seoul.wav`*
* **5:15 - 8:00** |  | **Диктор:** 2010 рік. Скромний офіс у Лондоні. Заснування DeepMind. Усі інвестори вважають нейромережі мертвою темою. Але Гассабіс об'єднує геймдев, нейробіологію та навчання з підкріпленням.
* **8:00 - 10:30** | [SFX: Напружений низький гул синту] | **Диктор:** Березень 2016 року. Сеул. Матч AlphaGo проти чемпіона світу Лі Седоля. Знаменитий Хід 37 — хід, який змусив заніміти всіх грандмайстрів планети і довів: машина здатна на творчу інтуїцію.

### АКТ 3. Орігамі життя та розв'язання AlphaFold (10:30 – 16:45)
*Музика: Suno Pro — `EP03_MUS_09_ACT3_92BPM_Origami_Life.wav`*
* **10:30 - 13:45** |  | **Диктор:** Перехід від ігор до реальної науки. Проблема згортання білків — стіна, перед якою біологи стояли п'ятдесят років. Якщо кожна молекула в тілі згортається за мікросекунди, чому суперкомп'ютери б'ються над цим роками?
* **13:45 - 16:45** | [VIDEO: `EP03_VID_02_Protein_Folding.txt`] | **Диктор:** Випуск AlphaFold2. Проблема розв'язана. Структура практично кожної відомої білкової молекули на Землі стає відкритою. Фармакологія отримує ключ до нових ліків.

### АКТ 4. Термоядерний синтез і Нобелівська вершина (16:45 – 21:30)
*Музика: Suno Pro — `EP03_MUS_13_ACT4_92BPM_Fusion_Plasma.wav`*
* **16:45 - 19:15** |  | **Диктор:** Жовтень 2024 року. Деміс Гассабіс отримує Нобелівську премію з хімії. Але він уже дивиться далі — на приборкання плазми в термоядерному синтезі та нові загадки Всесвіту.
* **19:15 - 21:30** | [SFX: Затихання та кришталевий резонанс] | **Диктор:** *«Розв'язати інтелект, а потім використати його для розв'язання всього іншого»*. Шлях полімата завершує нову епоху пізнання.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP03_MUS_01_ACT1_92BPM_Wooden_Knights.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Wooden Knights', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP03_AMB_02_ACT1_DRONE_Theme_Park_Hum.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Theme Park Hum', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP03_MUS_03_ACT1_92BPM_UCL_Hippocampus.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'UCL Hippocampus', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP03_MUS_04_ACT1_92BPM_London_Office_2010.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'London Office 2010', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP03_MUS_05_ACT2_92BPM_Move_37_Seoul.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Move 37 Seoul', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP03_MUS_06_ACT2_92BPM_AlphaGo_Triumph.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'AlphaGo Triumph', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP03_AMB_07_ACT2_DRONE_Neural_Matrix.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Neural Matrix', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP03_MUS_08_ACT2_92BPM_Science_Pivot.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Science Pivot', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP03_MUS_09_ACT3_92BPM_Origami_Life.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Origami Life', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP03_AMB_10_ACT3_DRONE_Protein_Lab.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Protein Lab', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP03_MUS_11_ACT3_92BPM_AlphaFold2_Success.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'AlphaFold2 Success', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP03_MUS_12_ACT3_92BPM_Nobel_Announcement.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Nobel Announcement', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP03_MUS_13_ACT4_92BPM_Fusion_Plasma.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Fusion Plasma', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP03_MUS_14_ACT4_92BPM_Polymath_Vision.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Polymath Vision', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP03_MUS_15_ACT4_92BPM_Universal_Harmony.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental neo-classical cerebral trip-hop, 92 bpm, crisp wooden chess foley percussion, solo cello harmonics, modular synth arpeggios, biomimetic precision, cue theme 'Universal Harmony', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP03_SFX_16_GLOBAL_Chess_Transitions.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Transitions': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP03_VO_UA_01_ACT1_Chess_Prodigy.wav` | `EP03_VO_EN_01_ACT1_Chess_Prodigy.wav` (ACT1 — Chess Prodigy)
* `EP03_VO_UA_02_ACT1_UCL_Neuroscience.wav` | `EP03_VO_EN_02_ACT1_UCL_Neuroscience.wav` (ACT1 — UCL Neuroscience)
* `EP03_VO_UA_03_ACT2_DeepMind_Founding.wav` | `EP03_VO_EN_03_ACT2_DeepMind_Founding.wav` (ACT2 — DeepMind Founding)
* `EP03_VO_UA_04_ACT2_Move_37_Seoul.wav` | `EP03_VO_EN_04_ACT2_Move_37_Seoul.wav` (ACT2 — Move 37 Seoul)
* `EP03_VO_UA_05_ACT3_Protein_Folding.wav` | `EP03_VO_EN_05_ACT3_Protein_Folding.wav` (ACT3 — Protein Folding)
* `EP03_VO_UA_06_ACT3_AlphaFold_Revolution.wav` | `EP03_VO_EN_06_ACT3_AlphaFold_Revolution.wav` (ACT3 — AlphaFold Revolution)
* `EP03_VO_UA_07_ACT4_Nobel_Chemistry.wav` | `EP03_VO_EN_07_ACT4_Nobel_Chemistry.wav` (ACT4 — Nobel Chemistry)
* `EP03_VO_UA_08_ACT4_Universal_Intelligence.wav` | `EP03_VO_EN_08_ACT4_Universal_Intelligence.wav` (ACT4 — Universal Intelligence)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP03_VID_001_ACT1_24FPS_Chess_Board.mp4` [00:00 – 00:05 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Усе у всесвіті є інформацією.
     - *Veo Prompt:* `Extreme macro cinematic shot of a wooden king chess piece casting a long sharp shadow across a glowing digital grid in a dark room, cinematic depth of field, 35mm Kodak film grain, 4k 24fps.`
002. `EP03_VID_002_ACT1_24FPS_Protein_Folding.mp4` [00:05 – 00:10 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Усе у всесвіті є інформацією.
     - *Veo Prompt:* `Complex 3D holographic protein molecule folding dynamically from an unstructured glowing chain into a majestic stable ribbon structure, dark obsidian background, cyan and gold biomimetic lighting, 8k.`
003. `EP03_VID_003_ACT1_24FPS_London_Tournament_Chessboard_Optical_D.mp4` [00:10 – 00:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Від траєкторії падіння дощової краплі на бруківку Лондона — до того, як молекула гемоглобіну переносить кисень у вашій крові.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP03_VID_004_ACT1_24FPS_Equation_Notebook_Macro_A1S04_Silhouet.mp4` [00:15 – 00:20 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Більшість людей бачать навколо себе хаотичний потік випадковостей.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP03_VID_005_ACT1_24FPS_Carpenter_Oak_Workbench_SlowMo_Insert.mp4` [00:20 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І лише одиниці народжуються зі здатністю бачити за цим потоком — приховане дерево рішень.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP03_VID_006_ACT1_24FPS_KeyScene_02_London_Tournament_Chessb.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Північний Лондон, 1980 рік.
     - *Veo Prompt:* `Moody 1980 North London bohemian living room: acoustic guitars, oil paintings leaning against walls, a four-year-old boy sitting on a carpet staring intensely at a chessboard between two adults, cinematic soft lighting, 4k.`
007. `EP03_VID_007_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [00:38 – 00:51 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У богемній квартирі, де батько — музикант і автор пісень греко-кіпріотського походження — сперечається про мистецтво, чотирирічний хлопчик на ім'я Деміс мовчки ст…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP03_VID_008_ACT1_24FPS_Hippocampus_Memory_Maze_Tracking_Mediu.mp4` [00:51 – 01:04 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Малюк не просить іграшок.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
009. `EP03_VID_009_ACT1_24FPS_Equation_Notebook_Macro_A1S09_Overhead.mp4` [01:04 – 01:17 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він просить пояснити правила.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP03_VID_010_ACT1_24FPS_London_Tournament_Chessboard_Optical_D.mp4` [01:17 – 01:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Для нього шахи не були грою.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP03_VID_011_ACT1_24FPS_KeyScene_03_Architectural_Corridor_A.mp4` [01:30 – 01:45 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У вісім років Деміс виграє свій перший великий дитячий турнір.
     - *Veo Prompt:* `Macro shot of a vintage 1984 Sinclair ZX Spectrum computer with rubber keys on a bedroom desk, glowing CRT television showing 8-bit green code, reflection in young boy's glasses, nostalgic British sci-fi atmosphere, 4k.`
012. `EP03_VID_012_ACT1_24FPS_Montreal_Snow_And_Attention_SlowMo_Ins.mp4` [01:45 – 02:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На отримані призові гроші він купує не велосипед.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of golden filaments of semantic attention bridging across handwritten equations beside a snow-dusted Montreal window, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP03_VID_013_ACT1_24FPS_Macintosh_Logic_Board_Macro_Detail.mp4` [02:00 – 02:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він купує уживаний мікрокомп'ютер ZX Spectrum 48K з гумовими клавішами та книгу з програмування на асемблері Z80.
     - *Veo Prompt:* `Extreme macro push-in shot of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP03_VID_014_ACT1_24FPS_London_Tournament_Chessboard_Anamorphi.mp4` [02:15 – 02:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І саме тоді у восьмирічній голові народжується питання, яке визначить долю двадцять першого століття:

«Коли я граю в шахи, я не рахую мільйони варіантів.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
015. `EP03_VID_015_ACT1_24FPS_Silicon_Light_Refraction_A1S15_Trackin.mp4` [02:30 – 02:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Я просто відчуваю форму позиції.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP03_VID_016_ACT1_24FPS_KeyScene_04_Architectural_Corridor_A.mp4` [02:45 – 03:00 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У тринадцять років Деміс Гассабіс стає майстром ФІДЕ з рейтингом 2300 — другим гравцем планети у своєму віці після легендарної Юдіт Полгар.
     - *Veo Prompt:* `Tense chess tournament hall in 1989: dozens of clocks ticking in unison, a twelve-year-old boy rubbing his temples after a six-hour match, cold fluorescent lighting, psychological exhaustion, 35mm film aesthetic, 4k.`
017. `EP03_VID_017_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [03:00 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але під час виснажливого десятигодинного матчу на турнірі в Ліхтенштейні в нього стається інтелектуальне прозріння.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP03_VID_018_ACT1_24FPS_London_Tournament_Chessboard_Silhouett.mp4` [03:15 – 03:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на зал, заповнений найкращими гросмейстерами світу, і раптом жахається: найвеличніші уми покоління спалюють мільйони годин свого єдиного життя на те,…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP03_VID_019_ACT1_24FPS_Constitutional_Crystal_Box_SlowMo_Inse.mp4` [03:30 – 03:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А за вікном — невиліковні хвороби, старіння клітин, нерозгадана фізика всесвіту.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP03_VID_020_ACT1_24FPS_London_Tournament_Chessboard_Macro_Det.mp4` [03:45 – 04:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Шахи були лише тренажером.
     - *Veo Prompt:* `Extreme macro push-in shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
021. `EP03_VID_021_ACT1_24FPS_KeyScene_05_University_Archive_Hall.mp4` [04:00 – 04:15 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У шістнадцять років він екстерном складає іспити до Кембриджа.
     - *Veo Prompt:* `Visual transition: wooden chess pieces dissolving into millions of isometric pixel sprites of a bustling digital amusement park, vibrant 1990s computer graphics morphing into modern neural networks, 8k.`
022. `EP03_VID_022_ACT1_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [04:15 – 04:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Університет приголомшений, але просить юнака почекати рік — він занадто малий за віком.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP03_VID_023_ACT1_24FPS_Hippocampus_Memory_Maze_Overhead_GodsE.mp4` [04:30 – 04:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І цей рік очікування стає трампліном: сімнадцятирічний Деміс влаштовується до студії Пітера Моліньє і сам-один пише програмне ядро культової гри Theme Park.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP03_VID_024_ACT1_24FPS_Compression_Diamond_Lattice_Optical_Da.mp4` [04:45 – 05:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Гра продається багатомільйонним тиражем.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP03_VID_025_ACT1_24FPS_Macintosh_Logic_Board_Silhouette_Mood.mp4` [05:00 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Підліток заробляє статок ще до першої університетської лекції і вперше бачить на практиці, як тисячі простих цифрових агентів на екрані породжують живу, непередба…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP03_VID_026_ACT2_24FPS_KeyScene_01_University_Archive_Hall.mp4` [05:15 – 05:25 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Закінчивши Кембридж із найвищою відзнакою, Гассабіс робить несподіваний маневр.
     - *Veo Prompt:* `3D medical neuro-visualization: glowing seahorse-shaped hippocampus structure inside a translucent human brain, golden electrical impulses firing along dendritic trees, dark obsidian background, Octane render, 8k.`
027. `EP03_VID_027_ACT2_24FPS_University_Archive_Hall_Anamorphic_Wid.mp4` [05:25 – 05:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Закінчивши Кембридж із найвищою відзнакою, Гассабіс робить несподіваний маневр.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP03_VID_028_ACT2_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [05:35 – 05:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Замість того, щоб одразу будувати технологічну корпорацію, він зачиняється в лабораторіях Університетського коледжу Лондона (UCL) і захищає докторську дисертацію…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP03_VID_029_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [05:45 – 05:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його логіка залізна: неможливо побудувати штучний розум, якщо ти не розібрав до гвинтика єдиний працюючий прототип у всесвіті — мозок людини.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP03_VID_030_ACT2_24FPS_Hippocampus_Memory_Maze_Optical_DataVi.mp4` [05:55 – 06:05 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він досліджує пацієнтів із пошкодженням гіпокампа — людей з амнезією, які не пам'ятають свого минулого.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP03_VID_031_ACT2_24FPS_Hippocampus_Memory_Maze_Silhouette_Moo.mp4` [06:05 – 06:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він досліджує пацієнтів із пошкодженням гіпокампа — людей з амнезією, які не пам'ятають свого минулого.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP03_VID_032_ACT2_24FPS_Hippocampus_Memory_Maze_SlowMo_Insert.mp4` [06:15 – 06:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І відкриває фундаментальний закон, який журнал Science назве одним із десяти головних відкриттів року: люди, які втратили пам'ять про минуле, фізично не здатні уя…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP03_VID_033_ACT2_24FPS_School_Auditorium_Stage_Macro_Detail.mp4` [06:25 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Пам'ять і уява — це один і той самий нейронний механізм конструювання сцен.
     - *Veo Prompt:* `Extreme macro push-in shot of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP03_VID_034_ACT2_24FPS_Hippocampus_Memory_Maze_Anamorphic_Wid.mp4` [06:35 – 06:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мозок не просто записує досвід — він щоночі під час сну програє його заново, будуючи симуляцію завтрашнього дня.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP03_VID_035_ACT2_24FPS_KeyScene_02_Neural_Horizon_Pulse_A2S.mp4` [06:45 – 06:56 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Осінь 2010 року.
     - *Veo Prompt:* `Foggy London street at night, Russell Square architecture, warm light in a high attic window where three silhouettes stand before a glass board covered in reinforcement learning equations, 35mm film grain, 4k.`
036. `EP03_VID_036_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S11_Overhe.mp4` [06:56 – 07:08 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Осінь 2010 року.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP03_VID_037_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [07:08 – 07:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Маючи в руках код комп'ютерних ігор, математику шахів і нейроанатомію гіпокампа, Деміс Гассабіс разом із Шейном Леггом та Мустафою Сулейманом засновує DeepMind.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP03_VID_038_ACT2_24FPS_Silicon_Light_Refraction_A2S13_Silhoue.mp4` [07:19 – 07:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У той час уся Кремнієва долина вважала загальний штучний інтелект (AGI) непристойним фантастичним словом.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP03_VID_039_ACT2_24FPS_Architectural_Corridor_A2S14_SlowMo_In.mp4` [07:30 – 07:41 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Інвестори сміялися їм в обличчя.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP03_VID_040_ACT2_24FPS_Neural_Horizon_Pulse_A2S15_Macro_Detai.mp4` [07:41 – 07:52 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Інвестори сміялися їм в обличчя.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP03_VID_041_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S16_Anamor.mp4` [07:52 – 08:04 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але Гассабіс пише на першому слайді презентації двокроковий план, який увійде в підручники історії:

«Крок перший: Розв'язати проблему інтелекту.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP03_VID_042_ACT2_24FPS_Equation_Notebook_Macro_A2S17_Tracking.mp4` [08:04 – 08:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Крок другий: Використати його, щоб розв'язати все інше».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP03_VID_043_ACT2_24FPS_KeyScene_03_Hippocampus_Memory_Maze.mp4` [08:15 – 08:32 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Вони схрещують глибокі нейромережі з навчанням із підкріпленням (Deep Reinforcement Learning) і додають туди біологічний механізм гіпокампа — Experience Replay (п…
     - *Veo Prompt:* `Extreme close-up of a traditional Japanese wooden Goban board, polished black slate and white clamshell Go stones forming a complex geometric constellation, dramatic top-down spotlight, intense stillness, 8k 24fps.`
044. `EP03_VID_044_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [08:32 – 08:49 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Системі дають класичні ігри Atari — без жодних правил, лише сирі пікселі на екрані та лічильник очок.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP03_VID_045_ACT2_24FPS_Hyperscale_Compute_Cluster_Silhouette.mp4` [08:49 – 09:06 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2014 році Google купує DeepMind за пів мільярда доларів, але Гассабіс виставляє безпрецедентну умову: створення незалежної етичної ради і заборона використання…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP03_VID_046_ACT2_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [09:06 – 09:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Готель Four Seasons у Сеулі.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP03_VID_047_ACT2_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [09:22 – 09:39 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Проти нього — система AlphaGo.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP03_VID_048_ACT2_24FPS_London_Tournament_Chessboard_Anamorphi.mp4` [09:39 – 09:56 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У шахах у середньому 35 можливих ходів у позиції.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP03_VID_049_ACT2_24FPS_Architectural_Corridor_A2S24_Tracking.mp4` [09:56 – 10:13 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це більше, ніж кількість усіх атомів у всьому видимому Всесвіті.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP03_VID_050_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [10:13 – 10:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На Сході Го вважали священним мистецтвом чистого духу, де панує лише людська інтуїція.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP03_VID_051_ACT3_24FPS_KeyScene_01_Seoul_Move_37_Go_Stone.mp4` [10:30 – 10:42 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Друга партія матчу в Сеулі.
     - *Veo Prompt:* `Slow motion macro shot of a single black Go stone being placed on the fifth line from the edge of the board (Move 37), shockwave of golden light rippling through the wood grain into a multidimensional neural network, 8k.`
052. `EP03_VID_052_ACT3_24FPS_Architectural_Corridor_A3S02_SlowMo_In.mp4` [10:42 – 10:53 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Йде тридцять сьомий хід.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP03_VID_053_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [10:53 – 11:05 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Лі Седоль виходить із зали покурити.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP03_VID_054_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [11:05 – 11:17 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Згідно з тисячолітніми канонами шкіл Го в Японії, Китаї та Кореї, на ранній стадії гри камінь ніколи не ставлять на п'яту лінію.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP03_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [11:17 – 11:28 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коментатори в прямому ефірі на сто мільйонів глядачів завмирають, вважаючи це програмним збоєм.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP03_VID_056_ACT3_24FPS_Silicon_Light_Refraction_A3S06_Overhea.mp4` [11:28 – 11:40 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Імовірність того, що такий хід зробила б людина, становила один шанс із десяти тисяч.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP03_VID_057_ACT3_24FPS_Architectural_Corridor_A3S07_Optical_D.mp4` [11:40 – 11:52 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* П'ятнадцять хвилин він сидить нерухомо.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP03_VID_058_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [11:52 – 12:03 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Через сто ходів розрізнені камені по всій дошці раптом сплітаються навколо того самого самотнього тридцять сьомого каменя у смертельну павутину.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP03_VID_059_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [12:03 – 12:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* AlphaGo перемагає.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP03_VID_060_ACT3_24FPS_KeyScene_02_Hippocampus_Memory_Maze.mp4` [12:15 – 12:30 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Наступного ранку після тріумфу в Сеулі Деміс Гассабіс збирає команду в номері готелю і каже: «Ігри закінчилися.
     - *Veo Prompt:* `Breathtaking scientific visualization of a complex biological protein folding in real-time: long ribbon of amino acids twisting, coiling into alpha-helices and beta-sheets with atomic precision, bioluminescent cyan and gold, Octane render, 8k.`
061. `EP03_VID_061_ACT3_24FPS_Silicon_Light_Refraction_A3S11_Anamorp.mp4` [12:30 – 12:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми переходимо до Кроку Другого».
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP03_VID_062_ACT3_24FPS_AlphaFold_Ribbon_Origami_Tracking_Medi.mp4` [12:45 – 13:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Головною загадкою біології протягом п'ятдесяти років залишалася проблема згортання білків — Protein Folding Problem.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP03_VID_063_ACT3_24FPS_AlphaFold_Ribbon_Origami_Overhead_Gods.mp4` [13:00 – 13:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Усе живе на Землі — ваші м'язи, нейрони, імунні антитіла, ферменти — побудоване з білків.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP03_VID_064_ACT3_24FPS_AlphaFold_Ribbon_Origami_Optical_DataV.mp4` [13:15 – 13:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Кожен білок починається як плоска нитка амінокислот, яка за мілісекунди самостійно згортається у неймовірно складний тривимірний вузол — біологічне орігамі.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP03_VID_065_ACT3_24FPS_AlphaFold_Ribbon_Origami_Silhouette_Mo.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме тривимірна форма білка визначає, чи стане він ліками, чи смертельним токсином.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP03_VID_066_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [13:45 – 14:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоб розшифрувати форму лише одного білка в лабораторії за допомогою рентгенівської кристалографії, вчений витрачав до п'яти років життя і сотні тисяч доларів.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP03_VID_067_ACT3_24FPS_AlphaFold_Ribbon_Origami_Macro_Detail.mp4` [14:00 – 14:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У природі існує понад двісті мільйонів білків.
     - *Veo Prompt:* `Extreme macro push-in shot of luminous amino-acid chain folding gracefully into a complex 3D golden-cyan protein structure in dark space, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP03_VID_068_ACT3_24FPS_KeyScene_03_AlphaFold_Ribbon_Origami.mp4` [14:15 – 14:34 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Чотири роки команда Гассабіса будує систему AlphaFold.
     - *Veo Prompt:* `Time-lapse visualization of a glowing sphere of 200 million protein structures expanding like a galaxy, illuminating dark regions of medical science, IMAX documentary scale, 8k 24fps.`
069. `EP03_VID_069_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S19_Tracki.mp4` [14:34 – 14:52 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2018 році вони виходять на головну світову біологічну олімпіаду CASP.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP03_VID_070_ACT3_24FPS_Equation_Notebook_Macro_A3S20_Overhead.mp4` [14:52 – 15:11 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перша версія перемагає, але точність все ще недостатня для медицини.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP03_VID_071_ACT3_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [15:11 – 15:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Гассабіс приймає жорстке рішення: знищити стару архітектуру до основи і написати все з чистого аркуша, інтегрувавши геометричний механізм уваги безпосередньо у фі…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP03_VID_072_ACT3_24FPS_Boardroom_Fracture_Night_Silhouette_Mo.mp4` [15:30 – 15:49 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Листопад 2020 року.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP03_VID_073_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [15:49 – 16:08 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* AlphaFold 2 видає точність на рівні ширини одного атома — дев'яносто два бали зі ста.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP03_VID_074_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S24_Macro.mp4` [16:08 – 16:26 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* П'ятдесятирічну проблему біології розв'язано остаточно.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP03_VID_075_ACT3_24FPS_University_Archive_Hall_Anamorphic_Wid.mp4` [16:26 – 16:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За наступний рік DeepMind розшифровує структури абсолютно всіх двохсот мільйонів відомих науці білків на планеті Земля — і викладає цю бібліотеку у стовідсотково…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP03_VID_076_ACT4_24FPS_KeyScene_01_Neural_Horizon_Pulse_A4S.mp4` [16:45 – 16:55 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Сьогодні під керівництвом Гассабіса об'єднаний Google DeepMind вирішує задачі, від яких перехоплює подих: алгоритми утримують розпечену до ста мільйонів градусів…
     - *Veo Prompt:* `Inside a magnetic tokamak fusion reactor: glowing violet plasma torus held in suspension by invisible AI-controlled magnetic fields, extreme physics precision, cinematic hard sci-fi, 8k.`
077. `EP03_VID_077_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S02_Optica.mp4` [16:55 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні під керівництвом Гассабіса об'єднаний Google DeepMind вирішує задачі, від яких перехоплює подих: алгоритми утримують розпечену до ста мільйонів градусів…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP03_VID_078_ACT4_24FPS_Equation_Notebook_Macro_A4S03_Silhouet.mp4` [17:05 – 17:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні під керівництвом Гассабіса об'єднаний Google DeepMind вирішує задачі, від яких перехоплює подих: алгоритми утримують розпечену до ста мільйонів градусів…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP03_VID_079_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [17:15 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але секрет особистості Деміса Гассабіса лежить у його поліматичності — здатності об'єднувати світи, які інші вважають несумісними.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP03_VID_080_ACT4_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [17:25 – 17:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але секрет особистості Деміса Гассабіса лежить у його поліматичності — здатності об'єднувати світи, які інші вважають несумісними.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP03_VID_081_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [17:35 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але секрет особистості Деміса Гассабіса лежить у його поліматичності — здатності об'єднувати світи, які інші вважають несумісними.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP03_VID_082_ACT4_24FPS_London_Tournament_Chessboard_Tracking.mp4` [17:45 – 17:55 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він щоночі працює у своїй студії з опівночі до четвертої ранку — у години абсолютної тиші, коли весь Лондон спить, пивши зелений чай і слухаючи ембієнт.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP03_VID_083_ACT4_24FPS_London_Tournament_Chessboard_Overhead.mp4` [17:55 – 18:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він щоночі працює у своїй студії з опівночі до четвертої ранку — у години абсолютної тиші, коли весь Лондон спить, пивши зелений чай і слухаючи ембієнт.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP03_VID_084_ACT4_24FPS_London_Tournament_Chessboard_Optical_D.mp4` [18:05 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він щоночі працює у своїй студії з опівночі до четвертої ранку — у години абсолютної тиші, коли весь Лондон спить, пивши зелений чай і слухаючи ембієнт.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP03_VID_085_ACT4_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [18:15 – 18:28 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які правила мислення цього сучасного Леонардо да Вінчі ми можемо інтегрувати у власну свідомість?
     - *Veo Prompt:* `Macro composition: a transparent crystal chess king standing next to a 3D hologram of a DNA double helix and a glowing neural network node, warm golden light uniting all three symbols, 4k.`
086. `EP03_VID_086_ACT4_24FPS_Carpenter_Oak_Workbench_SlowMo_Insert.mp4` [18:28 – 18:41 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тренуйте внутрішнє дерево рішень.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP03_VID_087_ACT4_24FPS_London_Tournament_Chessboard_Macro_Det.mp4` [18:41 – 18:54 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Як чотирирічний шахіст біля дошки, візьміть за правило перед будь-яким важливим кроком прораховувати гілки наслідків на п'ять ходів уперед.
     - *Veo Prompt:* `Extreme macro push-in shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP03_VID_088_ACT4_24FPS_Equation_Notebook_Macro_A4S13_Anamorph.mp4` [18:54 – 19:08 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Найбільші поразки трапляються не через слабкість, а через потрапляння у цугцванг — позицію, куди людина сама себе загнала через відсутність стратегії.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP03_VID_089_ACT4_24FPS_Silicon_Light_Refraction_A4S14_Trackin.mp4` [19:08 – 19:21 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вузькі спеціалісти стають заручниками власних шаблонів.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring carved wooden chess knights on glowing coordinates, black-and-white Go stones in Seoul, cyan-and-gold biomimetic AlphaFold protein ribbons, magnetic tokamak plasma, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP03_VID_090_ACT4_24FPS_London_Tournament_Chessboard_Overhead.mp4` [19:21 – 19:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Прорив DeepMind став можливим лише тому, що в одній голові зустрілися шахова комбінаторика, дизайн відеоігор, нейробіологія гіпокампа і фізика білків.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP03_VID_091_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [19:34 – 19:47 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Використовуйте принцип гри проти самого себе (Self-Play).
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP03_VID_092_ACT4_24FPS_Hippocampus_Memory_Maze_Silhouette_Moo.mp4` [19:47 – 20:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Система AlphaZero стала непереможною, коли відмовилася від людських підручників і зіграла мільйони партій сама з собою, нещадно виправляючи кожну власну слабкість.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP03_VID_093_ACT4_24FPS_KeyScene_03_Hyperscale_Compute_Clust.mp4` [20:00 – 20:11 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Матерія Всесвіту витратила чотирнадцять мільярдів років, щоб скластися в атоми, молекули, білки та нейрони, здатні усвідомити самих себе.
     - *Veo Prompt:* `Slow camera rise from a quiet candlelit chessboard in London up through the clouds into a cosmic view of Earth surrounded by a shimmering golden lattice of biological and digital knowledge, 8k 24fps.`
094. `EP03_VID_094_ACT4_24FPS_Hyperscale_Compute_Cluster_Macro_Detai.mp4` [20:11 – 20:22 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Матерія Всесвіту витратила чотирнадцять мільярдів років, щоб скластися в атоми, молекули, білки та нейрони, здатні усвідомити самих себе.
     - *Veo Prompt:* `Extreme macro push-in shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP03_VID_095_ACT4_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [20:22 – 20:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Матерія Всесвіту витратила чотирнадцять мільярдів років, щоб скластися в атоми, молекули, білки та нейрони, здатні усвідомити самих себе.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP03_VID_096_ACT4_24FPS_Macintosh_Logic_Board_Tracking_Medium.mp4` [20:34 – 20:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І коли посеред ночі у тихому лондонському кабінеті спалахує монітор, це не просто працює комп'ютерна програма.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP03_VID_097_ACT4_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [20:45 – 20:56 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І коли посеред ночі у тихому лондонському кабінеті спалахує монітор, це не просто працює комп'ютерна програма.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP03_VID_098_ACT4_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [20:56 – 21:08 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І коли посеред ночі у тихому лондонському кабінеті спалахує монітор, це не просто працює комп'ютерна програма.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP03_VID_099_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [21:08 – 21:19 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це життя за допомогою створеного ним цифрового телескопа нарешті починає читати власний вихідний код.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP03_VID_100_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [21:19 – 21:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це життя за допомогою створеного ним цифрового телескопа нарешті починає читати власний вихідний код.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on ARRI Master Anamorphic 60mm & Zeiss Supreme Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
