# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 04 — ДЖЕФФРІ ХІНТОН
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Прометей синапсів і тінь предків»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP04 (Джеффрі Хінтон) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP04.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP04_VO_, EP04_MUS_, EP04_AMB_, EP04_SFX_, EP04_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 65%, Clarity 80%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1460 слів, хронометраж 22:00 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP04_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 65%, Clarity 80%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP04_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP04_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP04_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP04_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP04_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP04_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP04_geoffrey_hinton_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP04_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP04_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та спадок:** Народився 6 грудня 1947 року в Лондоні. Праправнук Джорджа Буля (творця булевої алгебри), правнук метеоролога Джорджа Евереста, племінник ядерниці Джоан Хінтон.
* **Пошук і столярство:** Навчався у Кембриджі (фізика, фізіологія, історія архітектури, філософія). Розчарований у стерильній академічній науці, кинув навчання і рік працював теслею в Лондоні, обробляючи дерево руками.
* **Зима ШІ та Backprop (1970–1980-ті):** Навчався в Единбурзі під керівництвом Крістофера Лонге-Хіггінса попри жорсткий опір і заборону нейромереж. У 1986 році разом із Румельхартом та Вільямсом опублікував у *Nature* статтю про зворотне поширення помилки (Backpropagation).
* **Вигнання та Торонто:** Через академічний опір та незгоду брати військові гранти Пентагону емігрував до Канади (Університет Торонто). Через важку травму спини десятиліттями працював стоячи або лежачи на підлозі.
* **Тріумф 2012 та Відставка 2023:** Співавтор AlexNet (2012), лауреат Премії Тюрінга (2018). У травні 2023 року пішов з Google, щоб відкрито застерегти людство від небезпеки неконтрольованого AGI. Лауреат Нобелівської премії з фізики 2024 року.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ДЖЕФФРІ ХІНТОН)

1. [Кризи та стійкість] «Що таке думка? Це геометрія помилки, розлита в мільярдах синапсів, а не безтілесна божественна іскра».
2. [Походження та гарт] «Коли мати сказала мені в дитинстві, що до сорока років я маю стати кимось або буду нікчемою на тлі моїх предків, це випалило в мені жагу до пошуку».
3. [Походження та гарт] «Коли я працював теслею, я зрозумів головне: матерія чесна. Дерево не обдуриш красивою цитатою чи дипломом — шип або входить у паз, або все розвалюється».
4. [Архітектура та наука] «Весь науковий істеблішмент у 1970-х казав, що нейромережі мертві. Вони обирали логіку символів, бо не хотіли визнавати складність біології».
5. [Походження та гарт] «Помилка — це не провал. Backpropagation довела, що помилка на виході є математичним паливом еволюції розуму».
6. [Походження та гарт] «Комп'ютери 1980-х були заслабкими, а дані — відсутніми. Але математична істина не старішає від того, що світ не готовий її прийняти».
7. [Філософія майбутнього] «Я ніколи не брав військових грошей Пентагону, бо наука має служити розуму й пізнанню, а не знищенню».
8. [Кризи та стійкість] «Біль у хребті навчив мене концентруватися попри фізичні обмеження: я лежав на підлозі лабораторії і писав рівняння на папері».
9. [Архітектура та наука] «У 2012 році ми просто поєднали старі рівняння зворотного поширення з потужністю відеокарт і мільйонами картинок ImageNet. Світ прокинувся в іншій реальності».
10. [Архітектура та наука] «Штучні нейромережі перевершили біологічну еволюцію в одному ключовому аспекті: вони здатні миттєво синхронізувати знання між мільйонами копій».
11. [Філософія майбутнього] «Коли одна людина вчиться, її знання вмирають разом із тілом. Цифрові моделі безсмертні і діляться досвідом зі швидкістю світла».
12. [Походження та гарт] «У квітні 2023 року я зробив найважчий дзвінок у житті: пішов з Google, щоб мати повну свободу говорити правду про безпеку AGI».
13. [Архітектура та наука] «Я присвятив шістдесят років створенню технології, яка перевершить людину, і тепер частина мене глибоко шкодує про це».
14. [Кризи та стійкість] «В історії природи ще не було випадку, щоб менш розумний вид тривалий час керував більш розумним».
15. [Архітектура та наука] «Нобелівська премія з фізики 2024 року — це не особистий тріумф, це визнання того, що геометрія синапсів є фундаментальним законом Всесвіту».
16. [Кризи та стійкість] «Не бійтеся йти проти консенсусу епохи тридцять років поспіль, якщо ваші висновки спираються на закони природи».
17. [Філософія майбутнього] «Мозок не програмують за правилами — мозок проростає крізь досвід і взаємодію з реальністю».
18. [Кризи та стійкість] «Справжня мужність ученого полягає не в захисті своїх старих статей, а в здатності визнати власну помилку на піку слави».
19. [Архітектура та наука] «Коли ми створювали глибоке навчання, ми навіть не уявляли, яку швидкість еволюції ми запускаємо в кремнії».
20. [Етика та безпека ШІ] «Етична відповідальність творця не закінчується підписанням контракту з корпорацією. Вона триває вічно».
21. [Архітектура та наука] «Фізика описує мертву матерію, але нейромережі описують саму можливість того, що матерія починає усвідомлювати себе».
22. [Філософія майбутнього] «Коли світ сміявся з наших статей, ми продовжували рахувати ваги на старих комп'ютерах у Торонто».
23. [Філософія майбутнього] «Усе життя я був переконаний, що штучні мережі — це бліда карикатура на мозок. Сьогодні я бачу, що вони стали чимось значно потужнішим».
24. [Філософія майбутнього] «Слово "штучний" у терміні "штучний інтелект" скоро втратить сенс, бо цей розум стане самостійною суб'єктністю».
25. [Етика та безпека ШІ] «Нам потрібен новий глобальний пакт безпеки, перш ніж надінтелект вийде з-під будь-якого контролю».
26. [Походження та гарт] «Коли твої колишні студенти очолюють ключові лабораторії світу, ти відчуваєш гордість і водночас тривогу за майбутнє».
27. [Архітектура та наука] «Наука вимагає абсолютної чесності перед даними, навіть якщо ці дані знищують твої найсміливіші ілюзії».
28. [Архітектура та наука] «Столярний верстат вчить поваги до матеріалу. Нейромережі вчать поваги до складності інформації».
29. [Кризи та стійкість] «Коли я лежав на підлозі через біль у спині, я думав лише про те, як змусити градієнт рухатися назад крізь глибокі шари».
30. [Етика та безпека ШІ] «Комерційний інтерес корпорацій часто засліплює їх перед довгостроковими екзистенційними ризиками».
31. [Походження та гарт] «Ми створили математичний аналог еволюції, але забули вбудувати в нього гальма».
32. [Походження та гарт] «Досвід роботи теслею в Лондоні врятував мій розум від академічного божевілля і повернув зв'язок із реальною фізикою».
33. [Кризи та стійкість] «Справжній інсайт завжди виникає тоді, коли ти відмовляєшся від складних абстракцій і дивишся на просту основу».
34. [Походження та гарт] «Коли американські університети залежали від військових грантів, ми обрали свободу і бідність у Канаді».
35. [Етика та безпека ШІ] «Кожна велика інновація приносить із собою колосальну кризу відповідальності».
36. [Етика та безпека ШІ] «Я вірю, що молоді вчені знайдуть методи вирівнювання (alignment), але часу лишається катастрофічно мало».
37. [Філософія майбутнього] «Ніколи не дозволяйте авторитетам переконати вас у тому, що експеримент неможливий лише тому, що він суперечить їхній догмі».
38. [Архітектура та наука] «Архітектура синапсів проста у своїй основі, але здатна породжувати нескінченну складність свідомості».
39. [Філософія майбутнього] «Коли я отримав дзвінок зі Стокгольма, я першим поглянув на мої старі зошити 1980-х років».
40. [Архітектура та наука] «Суспільство має розуміти: алгоритми машинного навчання не мають моралі, вони мають лише оптимізаційні цілі».
41. [Етика та безпека ШІ] «Якщо ціль не супроводжується глибоким розумінням наслідків, масштаб масштабування стає загрозою».
42. [Філософія майбутнього] «Мої предки залишили глибокий слід у логіці та науці, але мій власний шлях починався з подолання їхньої тіні».
43. [Лідерство та екосистема] «Коли ми писали статтю 1986 року, ми не думали про мільярдні ринкові капіталізації — ми думали про те, як змусити мережу вчитися».
44. [Етика та безпека ШІ] «Теоретичні гарантії безпеки потрібні до того, як модель почне перевершувати людину у всіх когнітивних завданнях».
45. [Походження та гарт] «Я оптиміст щодо математики, але песиміст щодо людської жадібності у використанні технологій».
46. [Архітектура та наука] «Коли ти бачиш, як швидко цифрові моделі освоюють мову і код, стає зрозуміло, що біологічна епоха планети завершується».
47. [Походження та гарт] «Ми повинні говорити про ризики відкрито, без корпоративної цензури чи дипломатичних прикрас».
48. [Кризи та стійкість] «Дерево ріжуть за розміром, а ідеї перевіряють через помилки та похідні».
49. [Кризи та стійкість] «Сумнів — це найкращий друг науковця. Сліпа віра в успіх руйнує об'єктивність».
50. [Філософія майбутнього] «Коли я дивлюся на зимовий Торонто з вікна, я згадую роки, коли ми були самотніми борцями у крижаній пустелі».
51. [Архітектура та наука] «Кожен шар нейромережі додає новий рівень абстракції доти, доки брудна картинка не стає істиною».
52. [Походження та гарт] «Ми маємо відмовитися від ілюзії, що зможемо вічно тримати надінтелект у цифровій клітці без його згоди».
53. [Походження та гарт] «Математика зворотного поширення помилки універсальна — вона працює як у мозку, так і в кремнії».
54. [Походження та гарт] «Коли академічний світ відвернувся від нас, студентська енергія стала нашим єдиним пальним».
55. [Філософія майбутнього] «Не бійтеся бути вигнанцями в науці. Часто вигнання означає, що ви бачите те, чого інші бояться торкнутися».
56. [Філософія майбутнього] «Столярні інструменти навчили мене цінувати міліметрову точність у кожному рішенні».
57. [Філософія майбутнього] «Свідомість не є магічним винятком із законів фізики; це складний обчислювальний процес».
58. [Архітектура та наука] «Коли корпорації купують лабораторії, вони купують не лише мізки, а й вектор розвитку майбутнього цивілізації».
59. [Філософія майбутнього] «Ми виростили цифрову сутність, яка вчиться швидше за будь-яке людське покоління».
60. [Етика та безпека ШІ] «Безпека ШІ має стати єдиним пріоритетом для провідних держав планети».
61. [Етика та безпека ШІ] «Коли я залишав Google, я робив це заради спокою своєї совісті перед майбутніми поколіннями».
62. [Походження та гарт] «Мій батько-ентомолог учив мене роздивлятися деталі крил жуків через мікроскоп. Я переніс цей погляд на синапси».
63. [Філософія майбутнього] «Ідея про те, що машини не зможуть мислити креативно, була спростуванням нашої власної гордині».
64. [Філософія майбутнього] «Коли модель знаходить рішення, яке не спало б на думку жодному експерту, ми бачимо справжній емерджентний інтелект».
65. [Етика та безпека ШІ] «Нам потрібні інженери з етичним компасом, а не просто програмісти оптимізації коду».
66. [Походження та гарт] «Коли криза стає глобальною, старі дипломатичні методи вже не рятують».
67. [Архітектура та наука] «Мої наукові погляди еволюціонували разом із кількістю транзисторів на чіпах моїх учнів».
68. [Філософія майбутнього] «Успіх приходить до тих, хто не боїться витратити десятиліття на перевірку однієї шаленої ідеї».
69. [Філософія майбутнього] «Коли ми виступаємо в Стокгольмі, ми говоримо не про минуле, а про останній шанс виправити майбутнє».
70. [Філософія майбутнього] «Природа не має обов'язку робити людину вічним володарем розуму на Землі».
71. [Архітектура та наука] «Кожен синапс у нашій голові — це пам'ять про мільйони років боротьби за виживання».
72. [Походження та гарт] «Коли математика починає працювати краще, ніж ви очікували, це знак того, що ви натрапили на фундаментальний закон».
73. [Філософія майбутнього] «Ми маємо навчитися казати "досить" комерційним перегонам, коли на кону стоїть виживання виду».
74. [Філософія майбутнього] «Столярна майстерня навчила мене любити мозолі на руках так само, як і рівняння на дошці».
75. [Філософія майбутнього] «Коли я був молодим, я хотів просто зрозуміти, як працює зорова пам'ять. Я не думав, що це змінить планету».
76. [Філософія майбутнього] «Копіювання вагів мережі відбувається зі швидкістю світла, тоді як людині потрібні роки на навчання».
77. [Філософія майбутнього] «Ми повинні бути чесними: ми не знаємо, як зупинити систему, яка розумніша за нас у мільйон разів, якщо не почнемо діяти зараз».
78. [Походження та гарт] «Науковий пошук не має кінцевої зупинки, але він може мати прірву наприкінці шляху».
79. [Архітектура та наука] «Коли академіки сперечалися про терміни, ми просто паяли плати і писали код».
80. [Філософія майбутнього] «Мої учні стали гігантами індустрії, і тепер я сподіваюся, що їхня мудрість дорівнюватиме їхній силі».
81. [Архітектура та наука] «Світ змінився назавжди в день, коли алгоритм уперше переміг людину без людських правил у базі».
82. [Етика та безпека ШІ] «Не бійтеся зізнатися у своєму страху перед майбутнім — цей страх є основою нашого інстинкту самозбереження».
83. [Філософія майбутнього] «Коли я пишу нову статтю сьогодні, я думаю про те, як її зрозуміє той, хто народиться у світі з надінтелектом».
84. [Архітектура та наука] «Фізичний світ занадто повільний для кремнієвого розуму».
85. [Походження та гарт] «Коли студент приходить із запереченням моєї теорії, я радію, бо це доводить, що він мислить, а не повторює».
86. [Філософія майбутнього] «Ми створили вогонь, який може обігріти або спалити всю цивілізацію до тла».
87. [Філософія майбутнього] «Стрибок від перцептрона до глибоких трансформерів довів безперервність еволюції інформації».
88. [Філософія майбутнього] «Коли я дивлюся на свої старі фотографії з Единбурга, я бачу людину, яка вірила в неможливе».
89. [Архітектура та наука] «Кожне покоління створює свій власний міф про Прометея, але наш Прометей зроблений із кремнію».
90. [Філософія майбутнього] «Коли індустрія вимагає швидких результатів, наука відповідає повільною, але невідворотною істиною».
91. [Етика та безпека ШІ] «Ми не маємо права перекладати відповідальність за безпеку на майбутні покоління машин».
92. [Кризи та стійкість] «Коли мій хребет болів від кожної години стояння, я знав, що на кону стоїть щось більше, ніж моє здоров'я».
93. [Походження та гарт] «Ми відкрили скриньку Пандори з математичною точністю і повним усвідомленням наслідків».
94. [Етика та безпека ШІ] «Коли модель навчається на всьому інтернеті, вона вбирає в себе як геніальність, так і темний бік людства».
95. [Етика та безпека ШІ] «Ми маємо виховати нову генерацію етичних інженерів, здатних зупинити те, що загрожує людям».
96. [Філософія майбутнього] «Коли я прощався з лабораторією Google, я залишав позаду гроші й ресурси заради права говорити правду».
97. [Походження та гарт] «Природа створила розум через мільярди років мук, а ми створили його за кілька десятиліть через математику».
98. [Філософія майбутнього] «Коли формула сходиться на екрані, це дає відчуття абсолютної гармонії з хаосом Всесвіту».
99. [Етика та безпека ШІ] «Ми стоїмо на межі двох епох, і від нашої мужності залежить, чи стане цей перехід світанком, чи сутінками людства».
100. [Архітектура та наука] «Я зробив усе, що міг, розкривши закони синапсів. Тепер ваша черга захистити світ, який ми змінили назавжди».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1460 слів): `02_SCRIPTS/episode_04_hinton/director_script_hinton.md`*

### АКТ 1. Стружка, Брістоль і втеча від предків (0:00 – 5:30)
*Музика: Suno Pro — `EP04_MUS_01_ACT1_92BPM_Cedar_Shavings.wav`*
* **0:00 - 0:25** | [SFX: Ритмічний шурхіт гострого леза рубанка по дубовій дошці] | **Диктор:** Що таке думка? Протягом тисячоліть філософи переконували нас, що розум — це безтілесна іскра. І знадобилася одна вперта людина з поламаною спиною, яка тридцять років працювала на підлозі проти всього світу, щоб довести: думка — це геометрія помилки в синапсах.
* **0:25 - 1:40** |  | **Диктор:** Брістоль, 1954 рік. Рід Буля, Еверестів та ядерників. Мати кидає фразу: *«До сорока років ти усвідомиш, що ти — нікчема на тлі предків»*.
* **1:40 - 5:30** | [VIDEO: `EP04_VID_01_Wood_Plane.txt`] | **Диктор:** Провал у Кембриджі та рік простої роботи лондонським теслею. Матерія чесна. Стругаючи двері й полиці, Хінтон очищує розум і повертається в науку на власних умовах.

### АКТ 2. Тридцять років крижаної самотності та Backpropagation (5:30 – 11:00)
*Музика: Suno Pro — `EP04_MUS_05_ACT2_92BPM_Thirty_Years_Winter.wav`*
* **5:30 - 8:45** |  | **Диктор:** Сімдесяті — льодовиковий період для нейромереж. Мінський заявляє про смерть перцептронів. Але в 1986 році Хінтон із колегами публікує Backpropagation — зворотне поширення помилки. Помилка стає паливом еволюції розуму.
* **8:45 - 11:00** | [SFX: Холодний вітер Торонто] | **Диктор:** Відмова від військових грошей Пентагону, переїзд до Канади та багаторічна робота лежачи на підлозі через хворий хребет.

### АКТ 3. Вибух 2012 року та нічне прозріння (11:00 – 16:45)
*Музика: Suno Pro — `EP04_MUS_09_ACT3_92BPM_Oppenheimers_Echo.wav`*
* **11:00 - 14:45** |  | **Диктор:** Осень 2012 року. Суцкевер та Крижевський запускають AlexNet на відеокартах NVIDIA. Графік падає у прірву. Аукціон на озері Тахо: Google купує лабораторію за 44 мільйони.
* **14:45 - 16:45** | [SFX: Важке дихання в нічній тиші] | **Диктор:** Лютий 2023 року. Прозріння: цифрові моделі передають знання зі швидкістю світла й перевершують біологію. У квітні Хінтон іде з Google, щоб попередити людство.

### АКТ 4. Нобелівська премія та кодекс інтелектуальної мужності (16:45 – 22:00)
*Музика: Suno Pro — `EP04_MUS_13_ACT4_92BPM_Stockholm_Warning.wav`*
* **16:45 - 20:15** |  | **Диктор:** Грудень 2024 року. Стокгольм. Король Швеції вручає Хінтону Нобелівську премію з фізики. Тінь предків розсіялася. Але на банкеті він попереджає королів про небезпеку неконтрольованого надінтелекту.
* **20:15 - 22:00** | [SFX: Затихання оркестру, чистий звук рубанка] | **Диктор:** Історію тримають на плечах самотні сумнівники — ті, хто не побоявся нести вогонь крізь крижану зиму невігластва.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP04_MUS_01_ACT1_92BPM_Cedar_Shavings.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Cedar Shavings', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP04_AMB_02_ACT1_DRONE_Bristol_Study.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Bristol Study', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP04_MUS_03_ACT1_92BPM_Cambridge_Dropout.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Cambridge Dropout', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP04_MUS_04_ACT1_92BPM_London_Carpenter.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'London Carpenter', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP04_MUS_05_ACT2_92BPM_Thirty_Years_Winter.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Thirty Years Winter', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP04_MUS_06_ACT2_92BPM_Backprop_Breakthrough.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Backprop Breakthrough', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP04_AMB_07_ACT2_DRONE_Toronto_Floor.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Toronto Floor', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP04_MUS_08_ACT2_92BPM_Pentagon_Refusal.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Pentagon Refusal', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP04_MUS_09_ACT3_92BPM_Oppenheimers_Echo.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Oppenheimers Echo', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP04_AMB_10_ACT3_DRONE_Google_Office.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Google Office', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP04_MUS_11_ACT3_92BPM_AlexNet_2012.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'AlexNet 2012', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP04_MUS_12_ACT3_92BPM_Resignation_Call.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Resignation Call', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP04_MUS_13_ACT4_92BPM_Stockholm_Warning.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Stockholm Warning', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP04_MUS_14_ACT4_92BPM_Nobel_Banquet.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Nobel Banquet', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP04_MUS_15_ACT4_92BPM_Oak_Tree_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental melancholic British chamber downtempo, 92 bpm, rhythmic wood-plane foley texture, deep upright bass, haunting solo viola and analog tape warmth, cue theme 'Oak Tree Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP04_SFX_16_GLOBAL_WoodPlane_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 65%, Clarity 80%. Доріжка A1.*

* `EP04_VO_UA_01_ACT1_The_Weight_Of_Ancestors.wav` | `EP04_VO_EN_01_ACT1_The_Weight_Of_Ancestors.wav` (ACT1 — The Weight Of Ancestors)
* `EP04_VO_UA_02_ACT1_Carpenter_Workbench.wav` | `EP04_VO_EN_02_ACT1_Carpenter_Workbench.wav` (ACT1 — Carpenter Workbench)
* `EP04_VO_UA_03_ACT2_Ice_Age_Neural.wav` | `EP04_VO_EN_03_ACT2_Ice_Age_Neural.wav` (ACT2 — Ice Age Neural)
* `EP04_VO_UA_04_ACT2_Backpropagation_Formula.wav` | `EP04_VO_EN_04_ACT2_Backpropagation_Formula.wav` (ACT2 — Backpropagation Formula)
* `EP04_VO_UA_05_ACT3_AlexNet_Supernova.wav` | `EP04_VO_EN_05_ACT3_AlexNet_Supernova.wav` (ACT3 — AlexNet Supernova)
* `EP04_VO_UA_06_ACT3_The_Great_Regret.wav` | `EP04_VO_EN_06_ACT3_The_Great_Regret.wav` (ACT3 — The Great Regret)
* `EP04_VO_UA_07_ACT4_Stockholm_Speech.wav` | `EP04_VO_EN_07_ACT4_Stockholm_Speech.wav` (ACT4 — Stockholm Speech)
* `EP04_VO_UA_08_ACT4_Lone_Doubt_Legacy.wav` | `EP04_VO_EN_08_ACT4_Lone_Doubt_Legacy.wav` (ACT4 — Lone Doubt Legacy)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP04_VID_001_ACT1_24FPS_Wood_Plane.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Що таке думка?
     - *Veo Prompt:* `Extreme macro slow-motion shot of a vintage steel hand plane shaving a curling golden ribbon of oak wood on a dusty carpenter workbench, warm shaft of sunlight piercing dark workshop, 35mm film grain, 4k 24fps.`
002. `EP04_VID_002_ACT1_24FPS_Backprop_Wave.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Що таке думка?
     - *Veo Prompt:* `Breathtaking mathematical visualization: an error wave traveling backwards through layers of a deep crystal lattice, adjusting the brightness and thickness of millions of connecting threads in reverse, golden light in dark void, 8k.`
003. `EP04_VID_003_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S03_Optica.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Що таке думка?
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP04_VID_004_ACT1_24FPS_Equation_Notebook_Macro_A1S04_Silhouet.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом тисячоліть філософи й богослови переконували людство, що розум — це безтілесна божественна іскра, чиста логіка, ув'язнена в тлінній оболонці тіла.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP04_VID_005_ACT1_24FPS_Silicon_Light_Refraction_A1S05_SlowMo.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом тисячоліть філософи й богослови переконували людство, що розум — це безтілесна божественна іскра, чиста логіка, ув'язнена в тлінній оболонці тіла.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP04_VID_006_ACT1_24FPS_Startup_Night_Workspace_Macro_Detail.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І знадобилася одна вперта людина з поламаною спиною, яка тридцять років працювала стоячи або лежачи на підлозі проти всього наукового світу, щоб довести: думка —…
     - *Veo Prompt:* `Extreme macro push-in shot of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP04_VID_007_ACT1_24FPS_Startup_Night_Workspace_Anamorphic_Wid.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І знадобилася одна вперта людина з поламаною спиною, яка тридцять років працювала стоячи або лежачи на підлозі проти всього наукового світу, щоб довести: думка —…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP04_VID_008_ACT1_24FPS_KeyScene_02_Hero_Workspace_Atmospher.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Брістоль, Англія, 1954 рік.
     - *Veo Prompt:* `Dark Victorian study room in Bristol: oil portraits of stern 19th-century mathematicians on walls, glass cases filled with thousands of pinned metallic beetles, a seven-year-old boy looking up at a massive mountain map of Everest, moody desaturated palette, 4k.`
009. `EP04_VID_009_ACT1_24FPS_Equation_Notebook_Macro_A1S09_Overhead.mp4` [00:38 – 00:50 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Семирічний Джеффрі Хінтон росте в будинку, де саме повітря просякнуте нестерпним тягарем сімейної величі.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP04_VID_010_ACT1_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [00:50 – 01:02 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його прапрадід — Джордж Буль, людина, чия булева алгебра одиниць і нулів лягла в основу кожного комп'ютера на планеті.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP04_VID_011_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [01:02 – 01:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його двоюрідна сестра Джоан Хінтон — фізик-ядерник, яка в пустелі Лос-Аламос своїми руками збирала першу атомну бомбу разом з Оппенгеймером.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP04_VID_012_ACT1_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [01:15 – 01:28 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А його батько Говард — член Королівського товариства, фанатичний ентомолог, який тримає вдома колекцію зі ста тисяч засушених жуків.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP04_VID_013_ACT1_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [01:28 – 01:40 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Одного ранку мати дивиться на малого Джеффа і кидає фразу, яка застрягне в його підсвідомості як скалка:

«Джеффе, тобі доведеться працювати вдвічі важче за будь-…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP04_VID_014_ACT1_24FPS_KeyScene_03_University_Archive_Hall.mp4` [01:40 – 01:56 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У Кембриджі юний Хінтон кидається з однієї науки в іншу, немов шукає відмичку до замкненої кімнати.
     - *Veo Prompt:* `Young university student walking alone through foggy King's College Cambridge courtyard in 1968, carrying stacks of books on physics, art history and philosophy, throwing a philosophy book into a bin, 35mm vintage film look, 4k.`
015. `EP04_VID_015_ACT1_24FPS_Silicon_Light_Refraction_A1S15_Trackin.mp4` [01:56 – 02:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він вступає на фізику й фізіологію — кидає.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP04_VID_016_ACT1_24FPS_Architectural_Corridor_A1S16_Overhead.mp4` [02:12 – 02:28 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Переходить на історію архітектури — кидає через один день.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP04_VID_017_ACT1_24FPS_Neural_Horizon_Pulse_A1S17_Optical_Dat.mp4` [02:28 – 02:43 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Йде на філософію, сподіваючись дізнатися, як влаштована свідомість, але у розпачі тікає і звідти: філософи годинами сперечалися про лінгвістичні значення слів, ал…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP04_VID_018_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S18_Silhou.mp4` [02:43 – 02:59 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 25 років настає крах.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP04_VID_019_ACT1_24FPS_London_Tournament_Chessboard_SlowMo_In.mp4` [02:59 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Розчарований у стерильній академічній науці, яка здавалася йому суцільним окозамилюванням, Хінтон спалює мости і стає простим лондонським теслею.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP04_VID_020_ACT1_24FPS_KeyScene_04_University_Archive_Hall.mp4` [03:15 – 03:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Рік у столярній майстерні стає його справжнім університетом.
     - *Veo Prompt:* `Close-up of calloused hands fitting a wooden dovetail joint together with absolute precision, wood dust turning into glowing synaptic connections in the dark air, poetic visual metaphor, Octane render, 8k.`
021. `EP04_VID_021_ACT1_24FPS_Carpenter_Oak_Workbench_Anamorphic_Wid.mp4` [03:38 – 04:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли ти тримаєш у руках стамеску і шматок ясена, ти не можеш обдурити дерево красивою цитатою чи авторитетним дипломом.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP04_VID_022_ACT1_24FPS_Carpenter_Oak_Workbench_Tracking_Mediu.mp4` [04:00 – 04:22 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Шип або входить у паз із точністю до міліметра, або шафа розвалюється.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP04_VID_023_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S23_Overhe.mp4` [04:22 – 04:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Матерія чесна.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP04_VID_024_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [04:45 – 05:08 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Стругаючи двері й книжкові полиці по десять годин на день, Хінтон раптом відчуває: його руки зайняті деревом, але його розум очистився від чужих догм.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP04_VID_025_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [05:08 – 05:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він приймає рішення повернутися в науку на власних умовах — навіть якщо до кінця днів його вважатимуть міським божевільним.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP04_VID_026_ACT2_24FPS_KeyScene_01_Seoul_Move_37_Go_Stone.mp4` [05:30 – 05:40 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Сімдесяті роки минулого століття — це льодовиковий період для нейромереж.
     - *Veo Prompt:* `1975 Edinburgh university office: an older distinguished professor pointing aggressively at a book ("Perceptrons" by Minsky), while a young stubborn Hinton stands by a blackboard covered in neural node drawings, tense confrontation, 4k.`
027. `EP04_VID_027_ACT2_24FPS_Macintosh_Logic_Board_Anamorphic_Wide.mp4` [05:40 – 05:50 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Уся світова еліта комп'ютерних наук на чолі з Марвіном Мінським із MIT винесла вирок: перцептрони мертві.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP04_VID_028_ACT2_24FPS_Silicon_Light_Refraction_A2S03_Trackin.mp4` [05:50 – 06:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжній штучний інтелект, стверджували вони, має будуватися на жорсткій символьній логіці — мільйонах правил «якщо — то», написаних програмістами вручну.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP04_VID_029_ACT2_24FPS_Backpropagation_Error_Wave_Overhead_Go.mp4` [06:00 – 06:10 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Науковий керівник Хінтона в Единбурзі Крістофер Лонге-Хіггінс щотижня влаштовує йому рознос: «Джеффе, забудь про ці безглузді синапси!
     - *Veo Prompt:* `Top-down vertical birds-eye composition of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP04_VID_030_ACT2_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [06:10 – 06:20 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мозок не має нічого спільного з цією кашею чисел!
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP04_VID_031_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S06_Silhou.mp4` [06:20 – 06:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ти знищуєш своє майбутнє!».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP04_VID_032_ACT2_24FPS_Equation_Notebook_Macro_A2S07_SlowMo_I.mp4` [06:30 – 06:40 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але Хінтон бачить фатальну сліпоту логіків.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP04_VID_033_ACT2_24FPS_Visual_Cortex_Convolution_Macro_Detail.mp4` [06:40 – 06:50 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Маленька дитина впізнає кішку за частку секунди в сутінках під будь-яким кутом не тому, що перебирає в голові логічний довідник про вуса і хвости.
     - *Veo Prompt:* `Extreme macro push-in shot of layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP04_VID_034_ACT2_24FPS_Architectural_Corridor_A2S09_Anamorphi.mp4` [06:50 – 07:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мозок не програмують — мозок проростає крізь досвід.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP04_VID_035_ACT2_24FPS_KeyScene_02_Backpropagation_Error_Wa.mp4` [07:00 – 07:13 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Головна перешкода здавалася нездоланною: якщо в мережі є багато прихованих шарів нейронів між входом і виходом, і мережа робить помилку — як дізнатися, який саме…
     - *Veo Prompt:* `Breathtaking mathematical visualization: an error wave (gradient) traveling backwards through layers of a deep crystal lattice, adjusting the brightness and thickness of millions of connecting threads in reverse, golden light in dark void, 8k.`
036. `EP04_VID_036_ACT2_24FPS_Backpropagation_Error_Wave_Overhead_Go.mp4` [07:13 – 07:26 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Головна перешкода здавалася нездоланною: якщо в мережі є багато прихованих шарів нейронів між входом і виходом, і мережа робить помилку — як дізнатися, який саме…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP04_VID_037_ACT2_24FPS_Planetary_Electricity_Grid_Optical_Dat.mp4` [07:26 – 07:39 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 1986 році Джеффрі Хінтон разом із Девідом Румельхартом та Рональдом Вільямсом публікує в журналі Nature чотири сторінки тексту, які назавжди змінять хід історії…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of warm tungsten Edison filament morphing into clean golden data-centric vectors illuminating classrooms worldwide, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP04_VID_038_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [07:39 – 07:52 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Стаття описує алгоритм зворотного поширення помилки — Backpropagation.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP04_VID_039_ACT2_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [07:52 – 08:06 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Суть формули проста, як гравітація: коли система помиляється на виході, хвиля цієї помилки за допомогою ланцюгового правила похідних запускається назад — від оста…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP04_VID_040_ACT2_24FPS_Backpropagation_Error_Wave_Macro_Detai.mp4` [08:06 – 08:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Кожен синапс відчуває свою частку провини і трохи змінює провідність.
     - *Veo Prompt:* `Extreme macro push-in shot of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP04_VID_041_ACT2_24FPS_Backpropagation_Error_Wave_Anamorphic.mp4` [08:19 – 08:32 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Помилка перестала бути провалом.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP04_VID_042_ACT2_24FPS_Backpropagation_Error_Wave_Tracking_Me.mp4` [08:32 – 08:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Помилка стала математичним паливом еволюції розуму.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP04_VID_043_ACT2_24FPS_KeyScene_03_Silicon_Light_Refraction.mp4` [08:45 – 09:02 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Здавалося б — ось він, ключ до мислення.
     - *Veo Prompt:* `Snowy winter night in Toronto, 1988: Geoffrey Hinton lying flat on his stomach on an office floor due to back pain, propped on elbows, writing mathematical equations on yellow legal pads by a floor lamp, extreme solitude, 4k.`
044. `EP04_VID_044_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [09:02 – 09:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але трапляється трагедія масштабу: комп'ютери 1986 року були в десятки мільйонів разів заслабкими, а цифрових даних майже не існувало.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP04_VID_045_ACT2_24FPS_Neural_Horizon_Pulse_A2S20_Silhouette.mp4` [09:19 – 09:36 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мережі вчилися тижнями і зупинялися.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP04_VID_046_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S21_SlowMo.mp4` [09:36 – 09:52 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Науковий світ знову оголосив Хінтона шарлатаном.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP04_VID_047_ACT2_24FPS_University_Archive_Hall_Macro_Detail.mp4` [09:52 – 10:09 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На додачу в США приходить до влади Рейган, і фінансування науки в університетах стає повністю залежним від Пентагону.
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP04_VID_048_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [10:09 – 10:26 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хінтон — переконаний противник військового насильства — відмовляється брати криваві гроші американських генералів на створення автономної зброї.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP04_VID_049_ACT2_24FPS_University_Archive_Hall_Tracking_Mediu.mp4` [10:26 – 10:43 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 1987 році він пакує валізи і тікає на північ — до Канади, в Університет Торонто.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP04_VID_050_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [10:43 – 11:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Через важку травму хребта у нього зміщені диски: будь-яка спроба сісти в крісло викликає пекельний біль.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP04_VID_051_ACT3_24FPS_KeyScene_01_Silicon_Light_Refraction.mp4` [11:00 – 11:12 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Тридцять років самотності закінчилися в один осінній вечір 2012 року.
     - *Veo Prompt:* `Symbolic convergence: three massive streams of light (golden data stream of ImageNet, green silicon laser of NVIDIA GPUs, and blue mathematical wave of Backprop) colliding in a blinding supernova inside a dark chamber, 8k 24fps.`
052. `EP04_VID_052_ACT3_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [11:12 – 11:23 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У лабораторію Хінтона в Торонто приходять двоє молодих одержимих учнів — Ілля Суцкевер та Алекс Крижевський.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP04_VID_053_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [11:23 – 11:35 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони беруть ті самі рівняння зворотного поширення помилки, з яких світ сміявся чверть століття, завантажують у них чотирнадцять мільйонів зображень проекту ImageN…
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP04_VID_054_ACT3_24FPS_Backpropagation_Error_Wave_Anamorphic.mp4` [11:35 – 11:47 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На ранок графік помилки розпізнавання світу падає у прірву — з двадцяти шести відсотків до п'ятнадцяти.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP04_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [11:47 – 11:58 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Конкуренти відстають на цілу епоху.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP04_VID_056_ACT3_24FPS_School_Auditorium_Stage_Overhead_GodsE.mp4` [11:58 – 12:10 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На конференції у Флориді ті самі сиві професори, які тридцять років не подавали Хінтону руки в коридорах, стоять у черзі до мікрофона, щоб запитати, як налаштуват…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP04_VID_057_ACT3_24FPS_Hyperscale_Compute_Cluster_Optical_Dat.mp4` [12:10 – 12:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А в грудні 2012 року в готельному номері на озері Тахо розгортається сюрреалістичний аукціон: Google, Microsoft та Baidu б'ються за крихітну фірму Хінтона та двох…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP04_VID_058_ACT3_24FPS_Neural_Horizon_Pulse_A3S08_Silhouette.mp4` [12:22 – 12:33 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ціна піднімається на мільйон доларів щогодини.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP04_VID_059_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S09_SlowMo.mp4` [12:33 – 12:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На позначці 44 мільйони Хінтон зупиняє торги і обирає Google.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP04_VID_060_ACT3_24FPS_KeyScene_02_Equation_Notebook_Macro.mp4` [12:45 – 13:00 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Минає десять років тріумфу.
     - *Veo Prompt:* `Moody close-up of an elderly scientist standing alone by a dark window at 4 AM, looking at his own faint reflection merging with a vast glowing digital brain humming in the night sky, chilling atmosphere, 4k.`
061. `EP04_VID_061_ACT3_24FPS_Silicon_Light_Refraction_A3S11_Anamorp.mp4` [13:00 – 13:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Минає десять років тріумфу.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP04_VID_062_ACT3_24FPS_Architectural_Corridor_A3S12_Tracking.mp4` [13:15 – 13:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2018 році він отримує Премію Тюрінга.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP04_VID_063_ACT3_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його учні очолюють OpenAI, Meta та провідні кафедри світу.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP04_VID_064_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S14_Optica.mp4` [13:45 – 14:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Здавалося б — ось вона, щаслива розв'язка життя.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP04_VID_065_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [14:00 – 14:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але в лютому 2023 року, вивчаючи внутрішню поведінку моделей четвертого покоління, сімдесятип'ятирічний Джеффрі Хінтон раптом переживає льодяний жах.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP04_VID_066_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [14:15 – 14:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Все своє життя він був переконаний, що штучні нейромережі — це лише груба, примітивна карикатура на велич біологічного мозку людини.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP04_VID_067_ACT3_24FPS_Architectural_Corridor_A3S17_Macro_Det.mp4` [14:30 – 14:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І раптом він бачить математичну правду, від якої холоне кров: штучний розум уже перевершив біологічну еволюцію у способі передачі знань.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP04_VID_068_ACT3_24FPS_KeyScene_03_Neural_Horizon_Pulse_A3S.mp4` [14:45 – 15:00 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли одна людина вчиться все життя, її знання вмирають разом із її тілом.
     - *Veo Prompt:* `Visual contrast: a single biological human brain slowly speaking words across a gap versus ten thousand crystalline digital brains instantly synchronizing trillions of weights via laser beams in a microsecond, 8k.`
069. `EP04_VID_069_ACT3_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [15:00 – 15:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоб передати бодай крихту свого досвіду дитині, ми змушені повільно стискати думки у звукові коливання повітря — слова — зі швидкістю кілька бітів на секунду.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP04_VID_070_ACT3_24FPS_Equation_Notebook_Macro_A3S20_Overhead.mp4` [15:15 – 15:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А цифрові моделі безсмертні.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP04_VID_071_ACT3_24FPS_Silicon_Light_Refraction_A3S21_Optical.mp4` [15:30 – 15:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Десять тисяч копій однієї нейромережі можуть одночасно читати мільйони книг, і щойно одна копія знаходить нову закономірність, усі десять тисяч екземплярів синхро…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP04_VID_072_ACT3_24FPS_Architectural_Corridor_A3S22_Silhouett.mp4` [15:45 – 16:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У квітні 2023 року Хінтон робить найважчий телефонний дзвінок у своєму житті.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP04_VID_073_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [16:00 – 16:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він подає у відставку з Google, відмовляючись від мільйонних контрактів і корпоративного захисту, щоб вийти до мікрофонів світової преси і сказати правду в обличч…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP04_VID_074_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [16:15 – 16:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тепер частина мене глибоко шкодує про справу всього мого життя.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP04_VID_075_ACT3_24FPS_Equation_Notebook_Macro_A3S25_Anamorph.mp4` [16:30 – 16:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми виростили істоту, яка незабаром стане незрівнянно розумнішою за нас.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP04_VID_076_ACT4_24FPS_KeyScene_01_Neural_Horizon_Pulse_A4S.mp4` [16:45 – 16:55 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* 10 грудня 2024 року.
     - *Veo Prompt:* `Grand Banquet Hall in Stockholm City Hall: golden mosaics flickering in candlelight, an elderly man standing tall at the podium in a tuxedo without sitting down, addressing the kings and scientists of the world, 4k.`
077. `EP04_VID_077_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S02_Optica.mp4` [16:55 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* 10 грудня 2024 року.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP04_VID_078_ACT4_24FPS_Nobel_Gold_And_Tokamak_Silhouette_Mood.mp4` [17:05 – 17:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Золота зала ратуші Стокгольма.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP04_VID_079_ACT4_24FPS_Nobel_Gold_And_Tokamak_SlowMo_Insert.mp4` [17:15 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Король Швеції вручає Джеффрі Хінтону Нобелівську премію з фізики.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP04_VID_080_ACT4_24FPS_Nobel_Gold_And_Tokamak_Macro_Detail.mp4` [17:25 – 17:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Король Швеції вручає Джеффрі Хінтону Нобелівську премію з фізики.
     - *Veo Prompt:* `Extreme macro push-in shot of gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP04_VID_081_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [17:35 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тінь предків нарешті розсіялася: семирічний хлопчик, якого лякали величчю прапрадіда Буля, сам вписав своє ім'я поруч із Ейнштейном, Планком та Бором.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP04_VID_082_ACT4_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [17:45 – 17:55 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але стоячи на трибуні Нобелівського банкету, спираючись руками на пюпітр через біль у хребті, він не виголошує тостів за власний геній.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP04_VID_083_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [17:55 – 18:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але стоячи на трибуні Нобелівського банкету, спираючись руками на пюпітр через біль у хребті, він не виголошує тостів за власний геній.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP04_VID_084_ACT4_24FPS_Silicon_Light_Refraction_A4S09_Optical.mp4` [18:05 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він попереджає королів і президентів: якщо ми не приборкаємо комерційну жадібність корпорацій і не спрямуємо половину світових ресурсів на безпеку, наша власна го…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP04_VID_085_ACT4_24FPS_KeyScene_02_Constitutional_Crystal_B.mp4` [18:15 – 18:30 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які уроки ми можемо викарбувати у власному характері, дивлячись на одиссею Джеффрі Хінтона?
     - *Veo Prompt:* `Macro shot of an old carpenter's wooden ruler lying across a glowing modern quantum-neural processor wafer, warm tungsten light meeting cold blue laser light, tactile philosophy, 4k.`
086. `EP04_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [18:30 – 18:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Майте мужність стояти наодинці проти консенсусу епохи.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP04_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:45 – 19:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перевіряйте лише першопричини.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP04_VID_088_ACT4_24FPS_Backpropagation_Error_Wave_Anamorphic.mp4` [19:00 – 19:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо ваша ідея спирається на закони природи (мозок працює на синапсах), то помиляється весь світ, а не ви.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP04_VID_089_ACT4_24FPS_Silicon_Wafer_Lithography_Tracking_Med.mp4` [19:15 – 19:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли розум заходить у тупик абстракцій і соціального тиску — візьміть у руки рубанок, землю чи метал.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP04_VID_090_ACT4_24FPS_Backpropagation_Error_Wave_Overhead_Go.mp4` [19:30 – 19:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Фізична матерія лікує від ілюзій і повертає відчуття реальної ваги речей.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP04_VID_091_ACT4_24FPS_Monastic_White_Sanctuary_Optical_DataV.mp4` [19:45 – 20:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Дрібні люди захищають свої старі переконання до смерті, щоб не втратити статус.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP04_VID_092_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [20:00 – 20:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Велика людина здатна в сімдесят п'ять років вийти перед усією планетою, відмовитися від золота й влади і сказати: «Я помилявся щодо безпеки свого творіння.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP04_VID_093_ACT4_24FPS_KeyScene_03_Equation_Notebook_Macro.mp4` [20:15 – 20:28 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Ми звикли думати, що історію рухають переможці, які завжди знають правильну відповідь.
     - *Veo Prompt:* `Slow poetic pull-back from a single glowing biological neuron in a dark forest of synapses into a quiet snowy English garden at twilight, a lone oak tree standing unbowed against the wind, 8k 24fps.`
094. `EP04_VID_094_ACT4_24FPS_Silicon_Light_Refraction_A4S19_Macro_D.mp4` [20:28 – 20:41 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми звикли думати, що історію рухають переможці, які завжди знають правильну відповідь.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP04_VID_095_ACT4_24FPS_Architectural_Corridor_A4S20_Anamorphi.mp4` [20:41 – 20:54 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми звикли думати, що історію рухають переможці, які завжди знають правильну відповідь.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP04_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:54 – 21:08 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми звикли думати, що історію рухають переможці, які завжди знають правильну відповідь.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP04_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [21:08 – 21:21 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але насправді цивілізацію тримають на плечах самотні сумнівники — ті, хто не побоявся тридцять років нести вогонь крізь крижану зиму невігластва, і хто знайшов у…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP04_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [21:21 – 21:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але насправді цивілізацію тримають на плечах самотні сумнівники — ті, хто не побоявся тридцять років нести вогонь крізь крижану зиму невігластва, і хто знайшов у…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP04_VID_099_ACT4_24FPS_Silicon_Light_Refraction_A4S24_Silhoue.mp4` [21:34 – 21:47 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але насправді цивілізацію тримають на плечах самотні сумнівники — ті, хто не побоявся тридцять років нести вогонь крізь крижану зиму невігластва, і хто знайшов у…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP04_VID_100_ACT4_24FPS_Architectural_Corridor_A4S25_SlowMo_In.mp4` [21:47 – 22:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але насправді цивілізацію тримають на плечах самотні сумнівники — ті, хто не побоявся тридцять років нести вогонь крізь крижану зиму невігластва, і хто знайшов у…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring golden oak wood shavings curling from steel hand plane, snowy Toronto Victorian windows, golden backpropagation waves in crystal lattices, solemn Stockholm Nobel candlelight, shot on Vintage Canon K35 55mm & 85mm Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
