# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 05 — ЯН ЛЕКУН
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Єретик світла та світових моделей»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP05 (Ян Лекун) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP05.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP05_VO_, EP05_MUS_, EP05_AMB_, EP05_SFX_, EP05_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 60%, Clarity 85%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1387 слів, хронометраж 21:00 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP05_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 60%, Clarity 85%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP05_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP05_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP05_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP05_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP05_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP05_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP05_yann_lecun_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP05_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP05_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та інженерія:** Народився 8 липня 1960 року в передмісті Парижа. З дитинства паяв радіоапаратуру, збирав підсилювачі та програмував мікропроцесори.
* **Освіта і бунт:** Закінчив ESIEE Paris (1983), захистив PhD у Парижі (1987), де незалежно вивів ранню форму зворотного поширення помилки, виступивши проти академічного істеблішменту.
* **AT&T Bell Labs та CNN:** У легендарній лабораторії Bell Labs винайшов згорткові нейронні мережі (CNN) та архітектуру LeNet-5, яка в 1990-х роках автоматично зчитувала до 20% усіх банківських чеків у США.
* **Ізоляція та визнання:** Протягом півтора десятиліття згорткові мережі вважалися «необґрунтованою інженерною магією», доки в 2012 році архітектура AlexNet не підтвердила правоту Лекуна. Лауреат Премії Тюрінга (2018).
* **Meta AI (FAIR) та Open Source:** У 2013 році очолив FAIR за умови відкритого коду. Творець PyTorch, сімейства відкритих моделей LLaMA та новаторських архітектур Світових Моделей (JEPA) для подолання обмежень мовних моделей.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ЯН ЛЕКУН)

1. [Походження та гарт] «Я народився в передмісті Парижа і з дитинства хворів радіоелектронікою: паяв транзистори, збирав підсилювачі та програмував мікропроцесори».
2. [Філософія майбутнього] «Інженерна практика без фундаментальної науки — це ремісництво, але наука без інженерного втілення — це порожні слова на папері».
3. [Походження та гарт] «Коли я навчався в Парижі у 1980-х, академічний істеблішмент дивився на нейромережі зі зневажливим скепсисом. Усі молилися на символьний штучний інтелект».
4. [Походження та гарт] «Мій науковий керівник у Парижі казав, що зворотне поширення помилки — це іграшка. Мені довелося доводити протилежне самотужки».
5. [Філософія майбутнього] «Постдокторантура у Джеффрі Хінтона в Торонто у 1987 році відкрила мені очі на те, що справжні прориви робляться на стику психології мозку та оптимізації».
6. [Лідерство та екосистема] «У легендарних AT&T Bell Labs ми мали повну свободу досліджень і водночас чітку бізнес-місію: вирішити реальну інженерну проблему».
7. [Кризи та стійкість] «Своє найбільше відкриття — згорткові нейронні мережі (CNN) — я зробив, надихаючись біологічними експериментами на зоровій корі котів».
8. [Архітектура та наука] «Згорткові мережі імітують те, як біологічний зоровий аналізатор послідовно виділяє локальні ознаки — від ліній до складних об'єктів».
9. [Філософія майбутнього] «Коли ми створили архітектуру LeNet-5 у Bell Labs, ніхто не вірив, що мережа здатна читати рукописні цифри в реальному часі».
10. [Архітектура та наука] «До кінця 1990-х до 20% усіх банківських чеків у США оброблялися моїми згортковими мережами. Це був момент, коли теорія стала життьовою інфраструктурою».
11. [Філософія майбутнього] «Коли корпорація AT&T розпалася і закрила дослідницький підрозділ, я відчув, наскільки вразливою є наука перед короткостроковими інтересами менеджерів».
12. [Філософія майбутнього] «Спільно з колегами я розробив технологію стиснення документів DjVu, яка дозволила передавати важкі сторінки через повільний інтернет того часу».
13. [Походження та гарт] «У 2003 році я став професором в Інституті математичних наук Куранта при NYU. Академічне середовище дало мені простір для виховання найкращих інженерів».
14. [Лідерство та екосистема] «Коли Марк Цукерберг запросив мене у 2013 році очолити FAIR, у нас була одна умова: ми публікуємо 100% наших відкриттів у відкритому доступі».
15. [Архітектура та наука] «Наука розвивається найшвидше тоді, коли дослідники з усього світу можуть вільно перевіряти, критикувати і доповнювати чужий код без патентів».
16. [Архітектура та наука] «Фреймворк PyTorch, створений нашою командою у FAIR, став революцією в індустрії, бо дав дослідникам гнучкий інструмент замість старих бібліотек».
17. [Філософія майбутнього] «Я завжди був найпослідовнішим критиком підходу з підкріпленим навчанням для створення загального інтелекту. Це неефективно і сліпо».
18. [Філософія майбутнього] «Тварини і діти вчаться спостерігати за світом пасивно за лічені години, не вимагаючи мільярдів спроб. Машини повинні навчитися тому ж».
19. [Архітектура та наука] «Я запропонував архітектуру світових моделей — JEPA. Машина повинна не вгадувати кожен піксель, а передбачати абстрактні концепції у просторі».
20. [Етика та безпека ШІ] «Пророцтва про неминучий кінець людства через появу AGI — це не науковий аналіз, це інфантильна фантастика, помножена на маркетинг».
21. [Етика та безпека ШІ] «Штучний інтелект ніколи не стане загрозою з волі чи злого умислу, бо у машин немає емоцій чи інстинкту домінування».
22. [Філософія майбутнього] «Інтелект не означає прагнення до влади. Подивіться на кішок: вони розумні, але не будують планів захоплення світу».
23. [Етика та безпека ШІ] «Заклики зупинити дослідження або запровадити ліцензійний контроль над кожним рядком коду — це спроба монополій захистити свій ринок».
24. [Архітектура та наука] «Відкритий код — це єдиний надійний захист суспільства від монополізації інтелекту в руках кількох закритих корпорацій».
25. [Лідерство та екосистема] «Моделі сімейства LLaMA довели, що відкрита модель, навчена спільнотою, може перевершувати закриті пропрієтарні системи».
26. [Філософія майбутнього] «Коли кажуть, що машини ось-ось перевершать людський розум у кожній сфері, люди забувають, скільки еволюційних шарів стоїть за нами».
27. [Філософія майбутнього] «Ми ще далекі від створення AGI. Сучасні великі мовні моделі — це просто дуже вправні папуги зі стохастичною пам'яттю».
28. [Філософія майбутнього] «Мовна модель не розуміє фізичного світу; вона просто знає, яке слово з високою ймовірністю має йти за попереднім».
29. [Філософія майбутнього] «Щоб створити справжній інтелект, ми маємо навчити машини розуміти фізичну реальність: що предмети падають вниз, а стіна тверда».
30. [Кризи та стійкість] «Я ніколи не вірив у те, що просте збільшення кількості параметрів у мовних моделях приведе нас до розуміння фізики світу».
31. [Філософія майбутнього] «Наука — це перевірка гіпотез через експеримент, а не віра в авторитети, які обіцяють сингулярність за розкладом».
32. [Походження та гарт] «Мій батько був аерокосмічним інженером. Від нього я успадкував захоплення тим, як думка матеріалізується в апаратах».
33. [Походження та гарт] «У дитинстві я розбирав старі радіоприймачі — це найкраща школа для майбутнього вченого: не боятися зламати річ, щоб зрозуміти її».
34. [Філософія майбутнього] «Коли експеримент дає негативний результат, це не поразка. Це чіткий сигнал природи про те, що поточна гіпотеза була хибною».
35. [Походження та гарт] «Немає нічого шкідливішого для дослідника, ніж займатися модною темою лише заради легких грантів».
36. [Лідерство та екосистема] «Найглибші відкриття ховаються в темних кутках, куди ніхто не дивиться, бо вважає тему безперспективною».
37. [Архітектура та наука] «Протягом майже десяти років наші заявки на фінансування нейромереж відхилялися. Ми продовжували працювати всупереч системі».
38. [Кризи та стійкість] «Стійкість дослідника вимірюється кількістю разів, коли він спокійно переписував свій код після краху архітектури».
39. [Походження та гарт] «Ми повинні навчати студентів не користуватися чорними скриньками, а розуміти кожну операцію на рівні машинного коду».
40. [Філософія майбутнього] «Коли інженер каже, що модель сама все зрозуміла, він розписується у власній некомпетентності».
41. [Філософія майбутнього] «ШІ в майбутньому стане шоломом доповненої реальності чи цифровим помічником, який підсилюватиме людську пам'ять і логіку».
42. [Походження та гарт] «Ми не повинні боятися автоматизації. Протягом історії технології знищували старі професії, створюючи в рази більше нових».
43. [Філософія майбутнього] «Суспільство звільниться від рутинної праці, присвятивши себе мистецтву, науці та філософії».
44. [Філософія майбутнього] «Критичне мислення — це головна вакцина проти масової істерії перед новими технологіями».
45. [Походження та гарт] «Я француз, але американський прагматизм навчив мене: ідея варта нуля доти, доки вона не оформлена в робочий код».
46. [Філософія майбутнього] «Коли медіа кричать про повстання машин, вони шукають сенсацій замість пояснення механіки оптимізації».
47. [Архітектура та наука] «Штучні нейромережі мають дуже мало спільного з біологічною архітектурою мозку, хоча надихаються ним».
48. [Лідерство та екосистема] «Нейробіологія і комп'ютерні науки сьогодні йдуть паралельними курсами і рано чи пізно зійдуться в єдину теорію».
49. [Архітектура та наука] «Найкращий спосіб перевірити надійність алгоритму — дати йому задачу з невизначеністю у реальному світі».
50. [Філософія майбутнього] «Я ніколи не соромився виступати проти загальноприйнятого консенсусу на міжнародних конференціях».
51. [Етика та безпека ШІ] «Наукова етика полягає не в цензуруванні ідей, а в прозорості досліджень і готовності відповідати за наслідки».
52. [Походження та гарт] «Коли корпорації намагаються запатентувати базові математичні операції, вони душать майбутнє заради ренти».
53. [Лідерство та екосистема] «Відкрита наука — це єдиний спосіб забезпечити рівний доступ до благ цифрової революції для всього світу».
54. [Етика та безпека ШІ] «Світ потребує не заборон на дослідження, а створення надійних систем контролю і відкритих протоколів».
55. [Філософія майбутнього] «Коли ви створюєте архітектуру, почніть з паперу і ручки. Якщо ви не можете виписати формулу на серветці, ви її не розумієте».
56. [Філософія майбутнього] «Комп'ютерний зір має супроводжуватися розумінням фізичних обмежень нашого тривимірного світу».
57. [Етика та безпека ШІ] «Кожна епоха має свої страхи: колись боялися парових машин, сьогодні — алгоритмів. Страх живиться невіглаством».
58. [Лідерство та екосистема] «Просвітництво і поширення наукової освіти — це єдиний спосіб подолати технофобію у суспільстві».
59. [Походження та гарт] «Мої студенти знають: якщо код працює з першого разу, тест був надто простим або вони чогось не помітили».
60. [Філософія майбутнього] «Успішне дослідження — це 99% рутинного налагодження помилок та 1% осяяння».
61. [Філософія майбутнього] «Ми маємо пишатися тим, що будуємо інструменти розширення розуму, а не намагатися створити штучну людину з емоціями».
62. [Кризи та стійкість] «Машини не мають свідомості, і нам не потрібно наділяти їх суб'єктивним досвідом чи стражданнями».
63. [Філософія майбутнього] «Мета інженера — створити корисний механізм, а не містичний культ навколо чорної скриньки».
64. [Архітектура та наука] «Коли люди захоплюються містикою навколо моделей, я кажу: опустіться на землю, це лінійна алгебра і множення матриць».
65. [Походження та гарт] «Математика не обманює. Якщо модель робить помилку, причина завжди криється у функції втрат або упереджених даних».
66. [Філософія майбутнього] «Коли ми заснували FAIR у Нью-Йорку, ми хотіли довести, що дослідження ШІ не обов'язково концентруватися в Долині».
67. [Філософія майбутнього] «Таланти розсіяні по всій планеті, і головне завдання — об'єднати їх навколо спільної мети».
68. [Архітектура та наука] «Я ніколи не женувся за багатством. Моєю валютою завжди були цитування, вирішені рівняння і працюючий код».
69. [Архітектура та наука] «Отримання Премії Тюрінга стало визнанням того, що десятиліття віри у нейромережі не були марними».
70. [Філософія майбутнього] «Але нагороди — це лише епітафія минулим досягненням. Вченого цікавить те, що за наступним поворотом».
71. [Філософія майбутнього] «Світові моделі майбутнього дозволять роботам орієнтуватися в кімнаті і діяти автономно в будь-якій ситуації».
72. [Філософія майбутнього] «Ми ще не маємо роботів із таким же рівнем координації, як звичайна кішка. Нам є куди рости».
73. [Філософія майбутнього] «Фізичний світ настільки невичерпний, що будь-яка симуляція є лише грубим наближенням реальності».
74. [Філософія майбутнього] «Коли ви проєктуєте систему машинного зору, уявіть, що дивитесь на світ крізь крихітну щілину».
75. [Філософія майбутнього] «Звичка щодня читати нові статті на arXiv стала для мене такою ж природною, як чистити зуби вранці».
76. [Філософія майбутнього] «Не читайте лише те, що підтверджує ваші погляди. Читайте те, що спростовує гіпотези — це шлях до зростання».
77. [Походження та гарт] «Комунікація в науці має бути прозорою. Якщо ви не можете пояснити суть алгоритму студенту, ви заплуталися самі».
78. [Філософія майбутнього] «Технології є підсилювачем людських намірів — як темних, так і світлих».
79. [Лідерство та екосистема] «Я вірю у суспільство, де закон сильніший за монопольний капітал, а свобода досліджень захищена державою».
80. [Філософія майбутнього] «Будьте впертими у виборі проблеми і гнучкими у виборі методів її розв'язання».
81. [Філософія майбутнього] «Ніколи не бійтеся здатися дивними зі своїми науковими ідеями. Усі прориви починалися як єресь».
82. [Архітектура та наука] «Мої згорткові мережі колись вважали дивацтвом, а сьогодні на них працюють мільярди камер у світі».
83. [Філософія майбутнього] «Кожен із нас залишає слід у цифровому просторі. Подбайте про те, щоб він був чистим і корисним».
84. [Кризи та стійкість] «ШІ у руках чесних людей стає інструментом подолання бідності, хвороб та екологічних криз».
85. [Архітектура та наука] «Ми стоїмо на порозі створення нових матеріалів і ліків завдяки нейромережам».
86. [Архітектура та наука] «Переписання коду з нуля — це нормальний стан роботи інженера вищої кваліфікації».
87. [Походження та гарт] «Справжня свобода дослідника полягає в праві сказати інвесторам правду про закони математики».
88. [Філософія майбутнього] «Коли світ охрип від паніки, завдання науковця — увімкнути холодну логіку і спокійно пояснити механіку».
89. [Етика та безпека ШІ] «Я вірю в Європу та її потенціал створювати відкриті та етичні інструменти ШІ».
90. [Філософія майбутнього] «Ми бачимо не стіну невідомості, а величезне поле для інженерної творчості».
91. [Філософія майбутнього] «Наука вимагає жертв, але ніколи — за рахунок людської гідності чи свободи обміну думками».
92. [Архітектура та наука] «Кожен рядок оптимізованого коду — це маленька перемога над хаосом і ентропією матеріального світу».
93. [Філософія майбутнього] «Зберігайте ясність думки і скептицизм до будь-яких гучних маркетингових заяв».
94. [Філософія майбутнього] «Я пишаюся тим, що моя лабораторія була місцем, де панує рівність і повага до аргументів».
95. [Філософія майбутнього] «Машини навчаються на наших даних, але ми відповідаємо за цінності, які вони несуть».
96. [Філософія майбутнього] «Майбутнє не пророкують — майбутнє програмують і тестують руками тих, хто не боїться брудних даних».
97. [Філософія майбутнього] «Немає вищої нагороди, ніж бачити, як рівняння оживають у мільйонах пристроїв».
98. [Філософія майбутнього] «Кожне покоління інженерів розширює межі можливого. Ми побудували міст між статистикою і зоровим світом».
99. [Філософія майбутнього] «Залишайтеся допитливими дітьми, які розбирають прилади на килимі, навіть у вісімдесят років».
100. [Філософія майбутнього] «Найлютіший шторм епохи перетворюється на попутний потік, якщо ваші вітрила налаштовані за законами фізики».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1387 слів): `02_SCRIPTS/episode_05_lecun/director_script_lecun.md`*

### АКТ 1. Дим каніфолі та бунт проти Парижа (0:00 – 5:15)
*Музика: Suno Pro — `EP05_MUS_01_ACT1_92BPM_Soldering_Wind.wav`*
* **0:00 - 0:25** | [SFX: Шипіння каніфолі на паяльнику, свист осцилографа] | **Диктор:** Коли всі навколо встають на коліна перед новою іконою — справжній вчений бере викрутку і перевіряє, чи не захований за іконою звичайний грамофон. Ян Лекун сміється в обличчя і торговцям дивами, і пророкам апокаліпсису.
* **0:25 - 3:15** |  | **Диктор:** Передмістя Парижа, сімейна майстерня аерокосмічного інженера. Університетський бунт проти стерильної абстракції. Перевірка книги Мінського та самостійне виведення раннього Backprop.
* **3:15 - 5:15** | [VIDEO: `EP05_VID_01_Soldering_Board.txt`] | **Диктор:** Зустріч із Хінтоном та переїзд до Торонто. Початок великого шляху в нейромережах.

### АКТ 2. Зорова кора кота та Bell Labs (5:15 – 10:45)
*Музика: Suno Pro — `EP05_MUS_05_ACT2_92BPM_Bell_Labs_Optics.wav`*
* **5:15 - 8:30** |  | **Диктор:** Робота в AT&T Bell Labs. Винахід згорткових нейромереж (CNN) на основі зорової кори кота. Успіх LeNet-5: мільйони банківських чеків США читаються автоматами.
* **8:30 - 10:45** |  | **Диктор:** Розпад Bell Labs і шістнадцять років наукової ізоляції через моду на метод опорних векторів (SVM). Уроки стійкості проти консенсусу.

### АКТ 3. Битва за Open Source та кішка проти LLM (10:45 – 16:30)
*Музика: Suno Pro — `EP05_MUS_09_ACT3_92BPM_Open_Horizon.wav`*
* **10:45 - 12:30** |  | **Диктор:** 2013 рік. Марк Цукерберг переманює Лекуна очолити FAIR за умови повної відкритості. Народження PyTorch та моделі LLaMA, що зруйнували монополію закритих корпорацій.
* **12:30 - 16:30** | [SFX: Муркотіння кішки, перехід у чистий синт] | **Диктор:** Головна єресь: критика мовних моделей. *«Навіть звичайна кішка розуміє фізику краще, ніж трильйонна LLM»*. Розробка Світових Моделей (JEPA).

### АКТ 4. Парус в океані та кодекс воїна (16:30 – 21:00)
*Музика: Suno Pro — `EP05_MUS_13_ACT4_92BPM_Atlantic_Sail.wav`*
* **16:30 - 19:45** |  | **Диктор:** Яхта в Атлантиці як метафора бейдевінду — ходу прямо проти зустрічного вітру. Зневага до екзистенційних страхів і віра в нову епоху Відродження.
* **19:45 - 21:00** | [SFX: Хлопок паруса на вітрі] | **Диктор:** Страх народжується від темряви. Холодне світло інженерного знання перетворює шторм на попутний потік.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP05_MUS_01_ACT1_92BPM_Soldering_Wind.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Soldering Wind', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP05_AMB_02_ACT1_DRONE_Paris_Lab.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Paris Lab', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP05_MUS_03_ACT1_92BPM_ESIEE_Suburbs.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'ESIEE Suburbs', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP05_MUS_04_ACT1_92BPM_Toronto_Arrival.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Toronto Arrival', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP05_MUS_05_ACT2_92BPM_Bell_Labs_Optics.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Bell Labs Optics', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP05_MUS_06_ACT2_92BPM_LeNet5_Scans.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'LeNet5 Scans', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP05_AMB_07_ACT2_DRONE_Isolation_Years.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Isolation Years', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP05_MUS_08_ACT2_92BPM_SVM_Shadow.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'SVM Shadow', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP05_MUS_09_ACT3_92BPM_Open_Horizon.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Open Horizon', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP05_AMB_10_ACT3_DRONE_FAIR_Servers.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'FAIR Servers', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP05_MUS_11_ACT3_92BPM_PyTorch_Revolution.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'PyTorch Revolution', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP05_MUS_12_ACT3_92BPM_JEPA_Worlds.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'JEPA Worlds', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP05_MUS_13_ACT4_92BPM_Atlantic_Sail.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Atlantic Sail', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP05_MUS_14_ACT4_92BPM_Cartesian_Code.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Cartesian Code', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP05_MUS_15_ACT4_92BPM_Sailing_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental French electronic Cartesian trip-hop, 92 bpm, crisp analog modular synth sequences (Jean-Michel Jarre meets Massive Attack), warm bassline, Atlantic wind texture, cue theme 'Sailing Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP05_SFX_16_GLOBAL_Oscillator_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 60%, Clarity 85%. Доріжка A1.*

* `EP05_VO_UA_01_ACT1_Paris_Workshop.wav` | `EP05_VO_EN_01_ACT1_Paris_Workshop.wav` (ACT1 — Paris Workshop)
* `EP05_VO_UA_02_ACT1_Perceptrons_Myth.wav` | `EP05_VO_EN_02_ACT1_Perceptrons_Myth.wav` (ACT1 — Perceptrons Myth)
* `EP05_VO_UA_03_ACT2_Bell_Labs_CNN.wav` | `EP05_VO_EN_03_ACT2_Bell_Labs_CNN.wav` (ACT2 — Bell Labs CNN)
* `EP05_VO_UA_04_ACT2_Fifteen_Years_Exile.wav` | `EP05_VO_EN_04_ACT2_Fifteen_Years_Exile.wav` (ACT2 — Fifteen Years Exile)
* `EP05_VO_UA_05_ACT3_Meta_FAIR_Pact.wav` | `EP05_VO_EN_05_ACT3_Meta_FAIR_Pact.wav` (ACT3 — Meta FAIR Pact)
* `EP05_VO_UA_06_ACT3_Cat_Vs_LLM.wav` | `EP05_VO_EN_06_ACT3_Cat_Vs_LLM.wav` (ACT3 — Cat Vs LLM)
* `EP05_VO_UA_07_ACT4_Bedeveind_Wind.wav` | `EP05_VO_EN_07_ACT4_Bedeveind_Wind.wav` (ACT4 — Bedeveind Wind)
* `EP05_VO_UA_08_ACT4_Cartesian_Freedom.wav` | `EP05_VO_EN_08_ACT4_Cartesian_Freedom.wav` (ACT4 — Cartesian Freedom)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP05_VID_001_ACT1_24FPS_Soldering_Board.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Коли всі навколо встають на коліна перед новою іконою — справжній вчений бере викрутку і перевіряє, чи не захований за іконою звичайний механічний грамофон.
     - *Veo Prompt:* `Extreme macro cinematic shot of a hot soldering iron tip melting silver solder onto a green copper circuit board in 1974 Paris suburb, wispy white rosin smoke curling in warm desk lamp light, 35mm film grain, 4k 24fps.`
002. `EP05_VID_002_ACT1_24FPS_Cat_Vision.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Коли всі навколо встають на коліна перед новою іконою — справжній вчений бере викрутку і перевіряє, чи не захований за іконою звичайний механічний грамофон.
     - *Veo Prompt:* `Slow motion cinematic shot of a sleek black house cat calculating a complex jump across a cluttered bookshelf, overlaid with glowing green geometric physics vectors inside the cat's visual field, 8k.`
003. `EP05_VID_003_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S03_Optica.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли всі навколо встають на коліна перед новою іконою — справжній вчений бере викрутку і перевіряє, чи не захований за іконою звичайний механічний грамофон.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP05_VID_004_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У сучасному світі штучного інтелекту, охопленому містичною лихоманкою та пророцтвами скорого кінця світу, є лише одна людина такого масштабу, яка відкрито смієтьс…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP05_VID_005_ACT1_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У сучасному світі штучного інтелекту, охопленому містичною лихоманкою та пророцтвами скорого кінця світу, є лише одна людина такого масштабу, яка відкрито смієтьс…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP05_VID_006_ACT1_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його звуть Ян Лекун.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP05_VID_007_ACT1_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його звуть Ян Лекун.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP05_VID_008_ACT1_24FPS_KeyScene_02_DryCleaner_Steam_Window.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Передмістя Парижа, Суазі-су-Монморансі, початок сімдесятих.
     - *Veo Prompt:* `1972 French suburban garage: wind tunnel model airplanes hanging from ceiling, aerodynamic blueprints on table, a twelve-year-old boy with his engineer father adjusting a brass wing flap, warm Kodak film look, 4k.`
009. `EP05_VID_009_ACT1_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [00:38 – 00:50 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Маленький Ян росте в майстерні батька — аерокосмічного інженера.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP05_VID_010_ACT1_24FPS_Silicon_Light_Refraction_A1S10_Optical.mp4` [00:50 – 01:02 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Тут не вірять у магію.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP05_VID_011_ACT1_24FPS_Backpropagation_Error_Wave_Silhouette.mp4` [01:02 – 01:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо планер падає — винна не доля, винна помилка в розрахунку кута атаки крила.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP05_VID_012_ACT1_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [01:15 – 01:28 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У десять років хлопчик читає книгу про еволюцію ока і застигає від подиву: виявляється, ми бачимо світ не очима — ми бачимо його корою головного мозку, яка миттєв…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP05_VID_013_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S13_Macro.mp4` [01:28 – 01:40 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але коли Ян виростає і стикається з елітною французькою системою вищої освіти, у ньому прокидається лють.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP05_VID_014_ACT1_24FPS_KeyScene_03_Silicon_Wafer_Lithograph.mp4` [01:40 – 01:56 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Французька академічна каста поклонялася чистій, стерильній математичній абстракції.
     - *Veo Prompt:* `Grand marble hall of a prestigious Parisian academy filled with aloof professors in suits, contrasted with a gritty underground electronics lab where young Yann LeCun is etching circuit boards in acid bath, 4k.`
015. `EP05_VID_015_ACT1_24FPS_Paris_Rosin_Solder_Smoke_Tracking_Medi.mp4` [01:56 – 02:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Бруднити руки об паяльник, дроти чи сирий програмний код вважалося долею нижчої касти ремісників.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of glowing soldering iron tip melting silver solder on a vintage green circuit board with curling rosin smoke, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP05_VID_016_ACT1_24FPS_School_Auditorium_Stage_Overhead_GodsE.mp4` [02:12 – 02:28 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Лекун робить зухвалий жест: він відмовляється від кар'єри теоретика і йде до інженерної школи ESIEE, де можна ночами сидіти біля осцилографів і власноруч травити…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP05_VID_017_ACT1_24FPS_University_Archive_Hall_Optical_DataVi.mp4` [02:28 – 02:43 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Одного дня в університетській бібліотеці він натрапляє на філософську дуель між лінгвістом Ноамом Хомським і психологом Жаном Піаже.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP05_VID_018_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S18_Silhou.mp4` [02:43 – 02:59 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хомський стверджував, що мова і розум закладені в людину генетично від народження, як готовий кресленик.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP05_VID_019_ACT1_24FPS_Equation_Notebook_Macro_A1S19_SlowMo_I.mp4` [02:59 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Піаже заперечував: розум самоорганізується з нуля через зіткнення дитини з матеріальним світом.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP05_VID_020_ACT1_24FPS_KeyScene_04_Seoul_Move_37_Go_Stone.mp4` [03:15 – 03:35 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Кожен професор у Парижі повторював як мантру: «Книга Мінського 1969 року довела, що нейромережі ніколи не зможуть навчатися складних функцій».
     - *Veo Prompt:* `Close-up of a dusty 1969 book "Perceptrons" opening on a library table, camera zooms into mathematical inequalities on the page which dissolve into a multi-layered glowing 3D grid, Octane render, 8k.`
021. `EP05_VID_021_ACT1_24FPS_Architectural_Corridor_A1S21_Anamorphi.mp4` [03:35 – 03:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але двадцятирічний Лекун не вірить авторитетам на слово.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP05_VID_022_ACT1_24FPS_Neural_Horizon_Pulse_A1S22_Tracking_Me.mp4` [03:55 – 04:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він відкриває оригінал книги, бере олівець, перераховує кожне рівняння — і не вірить власним очам: Мінський довів обмеженість лише примітивної одношарової мережі!
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP05_VID_023_ACT1_24FPS_Compression_Diamond_Lattice_Overhead_G.mp4` [04:15 – 04:35 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Багатошарові системи просто не вміли тоді тренувати.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP05_VID_024_ACT1_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [04:35 – 04:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Авторитети всього світу двадцять років переказували чужий міф, полінувавшись перевірити першоджерело.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP05_VID_025_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [04:55 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У своєму підвалі в Парижі, наодинці, не знаючи про роботи Хінтона за океаном, молодий француз самостійно виводить ранню форму алгоритму зворотного поширення помилки.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP05_VID_026_ACT2_24FPS_KeyScene_01_Visual_Cortex_Convolutio.mp4` [05:15 – 05:25 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 1988 році Ян Лекун потрапляє у святая святих світової інженерії — лабораторію AT&T Bell Labs у Нью-Джерсі.
     - *Veo Prompt:* `Scientific macro visualization: light rays passing through the lens of a cat's eye onto the retina, activating hierarchical geometric receptive fields in the visual cortex (edges, corners, shapes), cyan and gold bioluminescence, 8k.`
027. `EP05_VID_027_ACT2_24FPS_Visual_Cortex_Convolution_Anamorphic_W.mp4` [05:25 – 05:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 1988 році Ян Лекун потрапляє у святая святих світової інженерії — лабораторію AT&T Bell Labs у Нью-Джерсі.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of layered optical glass filters extracting edges, contours, and geometry like biological feline visual cortex, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP05_VID_028_ACT2_24FPS_Paris_Rosin_Solder_Smoke_Tracking_Medi.mp4` [05:35 – 05:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме в цих стінах раніше винайшли транзистор, лазер, операційну систему UNIX та мову Сі.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of glowing soldering iron tip melting silver solder on a vintage green circuit board with curling rosin smoke, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP05_VID_029_ACT2_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [05:45 – 05:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перед молодим французом ставлять прикладну задачу, об яку зламали зуби сотні програмістів: навчити комп'ютер безпомилково читати каракулі людського почерку на пош…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP05_VID_030_ACT2_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [05:55 – 06:05 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перед молодим французом ставлять прикладну задачу, об яку зламали зуби сотні програмістів: навчити комп'ютер безпомилково читати каракулі людського почерку на пош…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP05_VID_031_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S06_Silhou.mp4` [06:05 – 06:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Звичайні повнозв'язні нейромережі захлиналися: якщо цифру «7»
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP05_VID_032_ACT2_24FPS_Macintosh_Logic_Board_SlowMo_Insert.mp4` [06:15 – 06:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* посунути на два міліметри вліво або трохи нахилити — для комп'ютера це була вже абсолютно інша картинка.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP05_VID_033_ACT2_24FPS_Macintosh_Logic_Board_Macro_Detail.mp4` [06:25 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* посунути на два міліметри вліво або трохи нахилити — для комп'ютера це була вже абсолютно інша картинка.
     - *Veo Prompt:* `Extreme macro push-in shot of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP05_VID_034_ACT2_24FPS_Nobel_Gold_And_Tokamak_Anamorphic_Wide.mp4` [06:35 – 06:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тоді Лекун згадує експерименти нобелівських лауреатів Г'юбела та Візела над зоровою корою кота.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of gleaming gold Nobel medal resting beside a holographic magnetic confinement tokamak plasma torus, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP05_VID_035_ACT2_24FPS_KeyScene_02_Retinal_Ganglion_Sparks.mp4` [06:45 – 06:58 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Нейрони ока не дивляться на всю картину одночасно.
     - *Veo Prompt:* `3D architectural animation of LeNet-5 Convolutional Neural Network: a sliding geometric filter scanning across a handwritten number "5", extracting edges, pooling layers compressing data into pure mathematical essence, Octane render, 8k.`
036. `EP05_VID_036_ACT2_24FPS_Retinal_Ganglion_Sparks_Overhead_GodsE.mp4` [06:58 – 07:11 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Нейрони ока не дивляться на всю картину одночасно.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP05_VID_037_ACT2_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [07:11 – 07:24 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перший шар клітин реагує лише на крихітні локальні нахили ліній у своїй маленькій зоні.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP05_VID_038_ACT2_24FPS_Silicon_Light_Refraction_A2S13_Silhoue.mp4` [07:24 – 07:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Другий шар збирає ці лінії у кути й дуги.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP05_VID_039_ACT2_24FPS_London_Tournament_Chessboard_SlowMo_In.mp4` [07:38 – 07:51 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Третій — у цілісні фігури.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP05_VID_040_ACT2_24FPS_Retinal_Ganglion_Sparks_Macro_Detail.mp4` [07:51 – 08:04 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Лекун переносить цю біологічну архітектуру в кремній і створює Згорткові нейронні мережі — Convolutional Neural Networks (CNN).
     - *Veo Prompt:* `Extreme macro push-in shot of confocal microscope view of living retinal neurons firing synchronized cyan bio-electric pulses, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP05_VID_041_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S16_Anamor.mp4` [08:04 – 08:17 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Головний фокус — розділення ваг (Weight Sharing): один і той самий математичний фільтр ковзає по всьому зображенню, шукаючи знайому рису незалежно від того, в яко…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP05_VID_042_ACT2_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [08:17 – 08:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 1995 році його система LeNet-5 встановлює промисловий рекорд: банкомати по всій Америці починають автоматично читати до двадцяти відсотків усіх виписаних від ру…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP05_VID_043_ACT2_24FPS_KeyScene_03_Silicon_Light_Refraction.mp4` [08:30 – 08:47 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Це був незаперечний інженерний тріумф.
     - *Veo Prompt:* `Empty conference room in 2002: Yann LeCun standing beside a poster of convolutional networks in a dimly lit hallway while crowds of scientists walk past towards a grand hall labeled "Support Vector Machines", 35mm film grain, 4k.`
044. `EP05_VID_044_ACT2_24FPS_Architectural_Corridor_A2S19_Optical_D.mp4` [08:47 – 09:04 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мільйони чеків щодня проходили крізь нейромережу Лекуна.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP05_VID_045_ACT2_24FPS_Neural_Horizon_Pulse_A2S20_Silhouette.mp4` [09:04 – 09:21 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І саме в цей момент...
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP05_VID_046_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S21_SlowMo.mp4` [09:21 – 09:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Корпорація AT&T розпадається, легендарну лабораторію розформовують.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP05_VID_047_ACT2_24FPS_School_Auditorium_Stage_Macro_Detail.mp4` [09:38 – 09:54 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А в університетах приходить нова мода — метод опорних векторів (SVM), який придумав колега Лекуна по коридору Володимир Вапнік.
     - *Veo Prompt:* `Extreme macro push-in shot of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP05_VID_048_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [09:54 – 10:11 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Математики закохалися в SVM за те, що його формули можна було красиво довести на дошці за п'ять хвилин.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP05_VID_049_ACT2_24FPS_Hyperscale_Compute_Cluster_Tracking_Me.mp4` [10:11 – 10:28 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Настають п'ятнадцять років абсурдної ізоляції: технологія, яка щодня крутить мільярди доларів у банкоматах, вигнана з наукових журналів.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP05_VID_050_ACT2_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [10:28 – 10:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли у 2012 році AlexNet — яка за своєю суттю була прямою масштабованою копією його LeNet-5 на відеокартах NVIDIA — розірвала світ комп'ютерного зору на частини,…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP05_VID_051_ACT3_24FPS_KeyScene_01_Silicon_Light_Refraction.mp4` [10:45 – 10:57 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Грудень 2013 року.
     - *Veo Prompt:* `Dramatic meeting at night in Menlo Park: Mark Zuckerberg and Yann LeCun across a glass table, a glowing open padlock symbol shattering chains of proprietary code into millions of free golden sparks spreading across the globe, 8k.`
052. `EP05_VID_052_ACT3_24FPS_Architectural_Corridor_A3S02_SlowMo_In.mp4` [10:57 – 11:08 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Грудень 2013 року.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP05_VID_053_ACT3_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [11:08 – 11:20 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Марк Цукерберг прилітає до Нью-Йорка, щоб переманити професора NYU Яна Лекуна очолити нову лабораторію штучного інтелекту FAIR.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP05_VID_054_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [11:20 – 11:32 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Лекун висуває ультиматум, від якого у корпоративних юристів холоне в жилах: «Я піду до вас лише за однієї умови — ми нічого не ховаємо під замок.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP05_VID_055_ACT3_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [11:32 – 11:43 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Кожна стаття, кожен фреймворк і кожна модель мають публікуватися у відкритому доступі для всього людства».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP05_VID_056_ACT3_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [11:43 – 11:55 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Кожна стаття, кожен фреймворк і кожна модель мають публікуватися у відкритому доступі для всього людства».
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP05_VID_057_ACT3_24FPS_Architectural_Corridor_A3S07_Optical_D.mp4` [11:55 – 12:07 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Цукерберг погоджується.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP05_VID_058_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [12:07 – 12:18 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме з цього пакту виростає PyTorch — відкрита мова, на якій сьогодні пишуться 90% усіх нейромереж планети, та сімейство відкритих моделей LLaMA, яке зруйнувало м…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP05_VID_059_ACT3_24FPS_Upwind_Atlantic_Sail_SlowMo_Insert.mp4` [12:18 – 12:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли керівники закритих лабораторій почали лякати Конгрес США тим, що відкритий код ШІ треба заборонити й ліцензувати заради «порятунку людства», Лекун вийшов на…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP05_VID_060_ACT3_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [12:30 – 12:47 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Але найголовнішу єресь Ян Лекун кидає сьогодні прямо в обличчя всій індустрії генеративного ШІ.
     - *Veo Prompt:* `Slow motion cinematic shot of a sleek black house cat calculating a complex jump across a cluttered bookshelf, overlaid with glowing green geometric physics vectors (gravity, momentum, trajectory) inside the cat's visual field, 8k 24fps.`
061. `EP05_VID_061_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [12:47 – 13:04 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але найголовнішу єресь Ян Лекун кидає сьогодні прямо в обличчя всій індустрії генеративного ШІ.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP05_VID_062_ACT3_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [13:04 – 13:21 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки світ сходить з розуму від чат-ботів і пророкує появу AGI вже наступного року через просте додавання чіпів до великих мовних моделей (LLM), Лекун заявляє: «Су…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP05_VID_063_ACT3_24FPS_Neural_Horizon_Pulse_A3S13_Overhead_Go.mp4` [13:21 – 13:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Подивіться на математику: щоб навчити сучасну LLM, їй згодовують увесь публічний текст інтернету.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP05_VID_064_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S14_Optica.mp4` [13:38 – 13:54 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це приблизно десять в тринадцятому ступені байтів даних.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP05_VID_065_ACT3_24FPS_Equation_Notebook_Macro_A3S15_Silhouet.mp4` [13:54 – 14:11 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це приблизно десять в тринадцятому ступені байтів даних.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP05_VID_066_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [14:11 – 14:28 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Людині знадобилося б сто сімдесят тисяч років безперервного читання, щоб просто пробігти очима цей текст.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP05_VID_067_ACT3_24FPS_University_Archive_Hall_Macro_Detail.mp4` [14:28 – 14:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І попри це — модель, яка прочитала всю бібліотеку людства, не здатна навчитися водити автомобіль за двадцять годин, як це робить будь-який сімнадцятирічний підліт…
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP05_VID_068_ACT3_24FPS_KeyScene_03_Seoul_Move_37_Go_Stone.mp4` [14:45 – 14:58 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Чотирирічна дитина за перші шістнадцять тисяч годин свого неспання отримує через зорові нерви в п'ятдесят разів більше інформації про реальний тривимірний світ, н…
     - *Veo Prompt:* `Comparison visualization: a narrow dark pipe of text symbols (1D token stream) versus a massive 3D holographic sphere of sensory physics data flowing into a four-year-old child's eyes (World Model JEPA), Octane render, 8k.`
069. `EP05_VID_069_ACT3_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [14:58 – 15:11 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Чотирирічна дитина за перші шістнадцять тисяч годин свого неспання отримує через зорові нерви в п'ятдесят разів більше інформації про реальний тривимірний світ, н…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP05_VID_070_ACT3_24FPS_Equation_Notebook_Macro_A3S20_Overhead.mp4` [15:11 – 15:24 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мова — це лише пласка, стиснута тінь реальності.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP05_VID_071_ACT3_24FPS_Silicon_Light_Refraction_A3S21_Optical.mp4` [15:24 – 15:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мова — це лише пласка, стиснута тінь реальності.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP05_VID_072_ACT3_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [15:38 – 15:51 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Більшість нашого розуму є невербальною.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP05_VID_073_ACT3_24FPS_London_Tournament_Chessboard_SlowMo_In.mp4` [15:51 – 16:04 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли столяр стругає дошку або кішка готується до стрибка на шафу, вони не генерують у голові речення зі слів — у їхньому мозку працює фізичний симулятор реальност…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP05_VID_074_ACT3_24FPS_London_Tournament_Chessboard_Macro_Det.mp4` [16:04 – 16:17 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли столяр стругає дошку або кішка готується до стрибка на шафу, вони не генерують у голові речення зі слів — у їхньому мозку працює фізичний симулятор реальност…
     - *Veo Prompt:* `Extreme macro push-in shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP05_VID_075_ACT3_24FPS_Upwind_Atlantic_Sail_Anamorphic_Wide.mp4` [16:17 – 16:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме над цим Лекун працює сьогодні, створюючи архітектуру JEPA — штучний інтелект, який не вгадує наступне слово в тексті, а вчиться розуміти гравітацію, інерцію,…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP05_VID_076_ACT4_24FPS_KeyScene_01_Upwind_Atlantic_Sail.mp4` [16:30 – 16:40 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли дебати в мережі досягають точки кипіння, шістдесятичотирирічний Лекун закриває ноутбук і виходить у відкритий океан на своїй вітрильній яхті.
     - *Veo Prompt:* `Aerial cinematic shot of a white racing sailboat cutting sharply through deep blue Atlantic waves at sunset, Yann LeCun at the helm adjusting the mainsheet against strong wind, spray catching golden light, 4k 24fps.`
077. `EP05_VID_077_ACT4_24FPS_Upwind_Atlantic_Sail_Optical_DataViz.mp4` [16:40 – 16:50 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли дебати в мережі досягають точки кипіння, шістдесятичотирирічний Лекун закриває ноутбук і виходить у відкритий океан на своїй вітрильній яхті.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP05_VID_078_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [16:50 – 17:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вітрильник — це ідеальна фізична метафора його філософії.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP05_VID_079_ACT4_24FPS_Upwind_Atlantic_Sail_SlowMo_Insert.mp4` [17:00 – 17:10 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ти не можеш змусити вітер дути туди, куди тобі хочеться.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP05_VID_080_ACT4_24FPS_Upwind_Atlantic_Sail_Macro_Detail.mp4` [17:10 – 17:20 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ти не можеш змусити вітер дути туди, куди тобі хочеться.
     - *Veo Prompt:* `Extreme macro push-in shot of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP05_VID_081_ACT4_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [17:20 – 17:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але якщо ти бездоганно знаєш закони аеродинаміки та гідродинаміки, ти можеш поставити косе вітрило під гострим кутом і йти в бейдевінд — прямо проти зустрічного в…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP05_VID_082_ACT4_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [17:30 – 17:40 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на майбутнє без жодного страху: на його переконання, ми не створюємо термінаторів, які захочуть нас поневолити, бо прагнення до домінування — це біол…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP05_VID_083_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [17:40 – 17:50 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на майбутнє без жодного страху: на його переконання, ми не створюємо термінаторів, які захочуть нас поневолити, бо прагнення до домінування — це біол…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP05_VID_084_ACT4_24FPS_Silicon_Light_Refraction_A4S09_Optical.mp4` [17:50 – 18:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми будуємо нову епоху Відродження, де у кожної людини на Землі буде власний штат геніальних цифрових асистентів.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP05_VID_085_ACT4_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [18:00 – 18:13 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які принципи цього незламного французького раціоналіста варто забрати у власний арсенал особистості?
     - *Veo Prompt:* `Macro shot of a brass marine sextant and a modern open-source silicon chip resting on a wooden chart table, warm sunlight reflecting off lenses, symbol of rational navigation, 4k.`
086. `EP05_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [18:13 – 18:26 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо весь натовп біжить в один бік — зупиніться і подивіться в протилежний.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP05_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:26 – 18:39 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Мода в науці, бізнесі та житті — це стадний інстинкт.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP05_VID_088_ACT4_24FPS_Equation_Notebook_Macro_A4S13_Anamorph.mp4` [18:39 – 18:52 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжні прориви завжди чекають у темних кутах, які більшість оголосила «неперспективними».
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP05_VID_089_ACT4_24FPS_Silicon_Light_Refraction_A4S14_Trackin.mp4` [18:52 – 19:06 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ніколи не плутайте красномовство з розумінням суті.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP05_VID_090_ACT4_24FPS_Architectural_Corridor_A4S15_Overhead.mp4` [19:06 – 19:19 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Як мовна модель може гладко генерувати правдоподібну нісенітницю без розуміння фізики, так і люди часто ховають порожнечу за модними словами.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP05_VID_091_ACT4_24FPS_Upwind_Atlantic_Sail_Optical_DataViz.mp4` [19:19 – 19:32 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Діліться знаннями відкрито — секретність є ознакою слабкості.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of crisp white racing yacht sail slicing sharply into dark Atlantic wind spray with geometric airflow vectors, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP05_VID_092_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [19:32 – 19:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Той, хто боїться показати свої напрацювання світу, боїться, що його зупинять.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP05_VID_093_ACT4_24FPS_KeyScene_03_Equation_Notebook_Macro.mp4` [19:45 – 19:54 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Страх перед невідомим народжується лише від темряви в розумі.
     - *Veo Prompt:* `Slow majestic camera pull-back from a lone sailboat slicing through dark blue ocean swells into a vast horizon where clouds and light rays form geometric receptive fields across the sky, IMAX 8k.`
094. `EP05_VID_094_ACT4_24FPS_Silicon_Light_Refraction_A4S19_Macro_D.mp4` [19:54 – 20:04 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Страх перед невідомим народжується лише від темряви в розумі.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP05_VID_095_ACT4_24FPS_Architectural_Corridor_A4S20_Anamorphi.mp4` [20:04 – 20:13 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Страх перед невідомим народжується лише від темряви в розумі.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP05_VID_096_ACT4_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [20:13 – 20:22 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли ви замінюєте містичний трепет холодним світлом інженерного знання, чудовиська зникають.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP05_VID_097_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [20:22 – 20:32 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли ви замінюєте містичний трепет холодним світлом інженерного знання, чудовиська зникають.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP05_VID_098_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [20:32 – 20:41 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли ви замінюєте містичний трепет холодним світлом інженерного знання, чудовиська зникають.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP05_VID_099_ACT4_24FPS_Silicon_Light_Refraction_A4S24_Silhoue.mp4` [20:41 – 20:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тоді найлютіший зустрічний шторм епохи перетворюється просто на попутний потік, який наповнює ваші вітрила.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP05_VID_100_ACT4_24FPS_Architectural_Corridor_A4S25_SlowMo_In.mp4` [20:51 – 21:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І тоді найлютіший зустрічний шторм епохи перетворюється просто на попутний потік, який наповнює ваші вітрила.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring wispy white rosin smoke from soldering iron on green PCB in 1974 Paris, Bell Labs optical scanners, green physics vectors in a cat's visual cortex, white Atlantic sailboat cutting upwind, shot on Angénieux Optimo Anamorphic 42mm & Macro 90mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
