# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 02 — ДЖЕНСЕН ХУАНГ
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Алхімія страждання та кремнію»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP02 (Дженсен Хуанг) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP02.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP02_VO_, EP02_MUS_, EP02_AMB_, EP02_SFX_, EP02_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 60%, Clarity 85%. Доріжка A1.)
*Ціль:* Отримати еталонну начитку повного сценарію (~1444 слів, хронометраж 21:00 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP02_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 60%, Clarity 85%. Доріжка A1.).
- [ ] Згенерувати синхронний англомовний дубляж EP02_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP02_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP02_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP02_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP02_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP02_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP02_jensen_huang_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP02_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP02_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження:** Народився 17 лютого 1963 року в Тайбеї (Тайвань). У дитинстві мешкав у Таїланді, у 9 років разом із братом емігрував до США.
* **Реформаторій в Кентуккі:** Помилково поселений у баптистський реформаторій Oneida Baptist Institute для важких підлітків замість елітного пансіону. Чистив усі туалети хлопчачого корпусу протягом двох років.
* **Denny's та Орегон:** Робота нічним посудомийником у придорожній закусочній Denny's, де він опанував інженерну оптимізацію процесів і подолав патологічну сором'язливість.
* **Заснування NVIDIA (1993):** Створення компанії разом із Крісом Малаховськи та Кертісом Премом у Denny's на тлі пострілів на вулиці.
* **30 днів до банкрутства (1995–1996):** Провал першого чіпа NV1 через перехід ринку на трикутники. Відчайдушний крок: чесна розмова з президентом Sega, отримання $5 млн авансу за невиконану роботу та створення врятуючого чіпа RIVA 128.
* **Велика єресь CUDA (2006):** Наказ інженерам вбудувати універсальну обчислювальну архітектуру в кожен чіп, попри фінансові збитки та обвал акцій у 2008 році. Ставка окупилася в 2012 році з появою AlexNet.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ДЖЕНСЕН ХУАНГ)

1. [Походження та гарт] «Ви не уявляєте, як ретельно я чистив ті туалети. Це назавжди випалило з моєї душі пиху. Не буває низької праці — буває лише ліниве виконання».
2. [Кризи та стійкість] «Панове, не забувайте: до нашого банкрутства завжди залишається рівно тридцять днів».
3. [Лідерство та екосистема] «Ми не орієнтуємося на поточний ринок. Ми будуємо ринок, розмір якого сьогодні дорівнює нулю мільярдів доларів, але завтра дорівнюватиме всій світовій економіці».
4. [Кризи та стійкість] «Ви маєте надто високі очікування і надто низьку стійкість. А тому я від щирого серця бажаю вам великих порцій болю і страждань».
5. [Філософія майбутнього] «Велич народжується не з інтелекту чи червоного диплома. Велич народжується з характеру, який кується тоді, коли ваші плани летять у прірву».
6. [Філософія майбутнього] «Не бійтеся зізнатися партнерам у тому, що ваш продукт хибний, якщо це збереже головне — абсолютну чесність і довіру».
7. [Філософія майбутнього] «Будь-яку рутинну роботу можна перетворити на високе ремесло, якщо підійти до неї з інженерною точністю».
8. [Філософія майбутнього] «Складність і опір середовища — це ваш єдиний надійний захисний рів від ледачих конкурентів».
9. [Лідерство та екосистема] «Якщо інформація в компанії проходить через п'ять поверхів начальників — правда вмирає по дорозі».
10. [Лідерство та екосистема] «Справжній лідер не ховається в кабінеті. Він сидить за загальним столом поруч із командою біля брудної білої дошки».
11. [Філософія страждання] «Я бажаю вам достатньо болю і страждань. Тому що саме страждання формують характер, а характер формує долю величних компаній».
12. [Школа Denny's] «У 15 років я працював посудомийником у закусочній Denny's у Портленді. Я чистив туалети і мив посуд краще за всіх у світі. Це навчило мене гідності ремесла».
13. [Баптистський інтернат] Oneida Baptist Institute у Кентуккі загартував мене: коли ти 9-річний іммігрант без знання мови чистиш вбиральні, ти вчишся виживати за будь-яких умов.
14. [Постійний страх краху] «Ми завжди були за 30 днів до банкрутства. Цей щоденний страх — найкраще паливо для інновацій та захисту від закостеніння».
15. [Витривалість (Grit)] Інтелект переоцінений; витривалість (grit) — це головний предиктор довгострокового тріумфу в інженерії та бізнесі.
16. [Ставлення до праці] «Байдуже, чи миєте ви посуд у нічній забігайлівці, чи проектуєте чіп на 200 мільярдів транзисторів — робіть це так, ніби від кожної дії залежить всесвіт».
17. [Стійкість до невдач] Помилки — це не привід для сорому. Це просто безкоштовні уроки фізики та ринку.
18. [Культура прямоти] В NVIDIA немає кабінетної бюрократії. Я можу зайти в будь-яку лабораторію і поговорити з молодшим інженером напряму.
19. [Пласка структура] У мене 50 прямих підлеглих. Що менше рівнів менеджменту між лідером та інженером, то чистіший сигнал.
20. [Біжи, а не йди] «Біжи, не йди. Або ти біжиш за їжею, або біжиш, щоб самому не стати чиєюсь їжею».
21. [Настільний теніс] Третє місце на юніорському чемпіонаті США з пінг-понгу навчило мене мікросекундній реакції та нещадному фокусу на м'ячі.
22. [Шкіряна куртка як форма] Я ношу однаковий чорний одяг і шкіряну куртку, щоб не витрачати ані секунди ранкової енергії на вибір гардеробу.
23. [Смирення лідера] Генеральний директор не повинен бути вельможею. Він повинен бути головним розв'язувачем проблем у компанії.
24. [Здатність терпіти біль] Успіх вимірюється не тим, скільки грошей ви заробили, а тим, скільки агонії ви змогли витримати на шляху до мети.
25. [Відмова від консенсусу] Якщо аналітики Уолл-стріт хвалять вашу стратегію, ви робите щось очевидне і банальне.
26. [Гартування кризами] Криза 1995 року, коли чіп NV1 провалився, навчила мене дивитися смерті компанії в очі без паніки.
27. [Рятівний дзвінок Sega] Я чесно зізнався генеральному директору Sega у провалі архітектури NV1, і він дав нам $5 млн авансу на RIVA 128 за нашу чесність.
28. [Уроки Denny's 1993] NVIDIA народилася за столиком Denny's за чашкою безкоштовної кави. Справжні революції починаються в скромних місцях.
29. [Чесність перед клієнтом] Ніколи не продавайте клієнту те, у що самі не вірите всім серцем.
30. [Сила оптимізму] Песимісти мають рацію у деталях, але оптимісти будують нові галактики.
31. [Ціна компромісу] Краще зазнати чистої інженерної поразки, ніж випустити посередній компромісний продукт.
32. [Щоденний перезапуск] Щоранку я прокидаюся з думкою, що компанію треба рятувати знову з чистого аркуша.
33. [Свобода від его] Визнати, що ти витратив три роки на хибну архітектуру і спалити її — це найвища форма мужності.
34. [Довіра до команди] Якщо ви наймаєте найкращих у світі людей, не вказуйте їм кожен крок — дайте їм свободу творити дива.
35. [Інженерний стоїцизм] Закони термодинаміки неможливо підкупити маркетингом. Будуйте на фундаментальній фізиці.
36. [Винахід GPU] У 1999 році ми винайшли GeForce 256 — перший у світі графічний процесор, який звільнив комп'ютер від рамок 2D.
37. [Паралельна парадигма] Центральний процесор (CPU) — це швидкий літак, а графічний процесор (GPU) — це армія з мільйона мурах, здатних зрушити гори.
38. [Фізика 3D графіки] Тривимірна графіка вимагала мільярдів обчислень матриць одночасно; це був ідеальний тренажер для майбутнього ШІ.
39. [Тріумф RIVA 128] У 1997 році чіп RIVA 128 врятував компанію від банкрутства і встановив стандарт швидкості для всієї індустрії ПК.
40. [Смерть 3dfx] Купівля активів 3dfx Voodoo довела: перемагає не культовий бренд, а безжальна інженерна дисципліна випуску чіпів кожні 6 місяців.
41. [Ставка на DirectX] Ми тісно співпрацювали з Microsoft, щоб зробити апаратне 3D-прискорення серцем кожної операційної системи Windows.
42. [Термодинамічний бар'єр] Закон Деннарда помер 15 років тому: центральні процесори вперлися у перегрів, і єдиним виходом став паралелізм.
43. [Шейдерна революція] Програмовані шейдери в GeForce 3 перетворили GPU з фіксованого конвеєра на універсальний математичний інструмент.
44. [Кремнієвий закон] Чим більше транзисторів ви можете ефективно змусити працювати паралельно, тим ближче ви до імітації нейронів мозку.
45. [Інтеграція пам'яті] Обчислення без пропускної здатності пам'яті марні; HBM пам'ять стала такою ж важливою, як і самі ядра.
46. [Швидкість як конкурентна перевага] Ми скоротили цикл проектування суперчіпів з чотирьох років до вісімнадцяти місяців.
47. [Фізика світла (Ray Tracing)] У 2018 році з запуском RTX ми поставили на апаратне трасування променів у реальному часі, коли всі казали, що це неможливо ще 10 років.
48. [Нейрорендерінг DLSS] Традиційний рендеринг пікселів мертвий; тепер ми генеруємо картинку за допомогою нейромереж у реальному часі.
49. [Співпраця з TSMC] Морріс Чанг став моїм наставником і братом по зброї. Без літографії TSMC революція NVIDIA була б неможливою.
50. [Упаковка чіпів CoWoS] Передова упаковка кремнію (Chip-on-Wafer-on-Substrate) стала новим полем битви за продуктивність.
51. [Оптимізація інженерного стеку] Ми проектуємо не просто чіп — ми проектуємо транзистори, підкладку, оптоволокно, сервери та софт як єдине ціле.
52. [Подолання фізичних меж] Коли довжина хвилі світла стала більшою за елементи чіпа, ми застосували обчислювальну літографію на GPU.
53. [Кремній як мистецтво] Погляньте на кристал Blackwell під мікроскопом: 208 мільярдів транзисторів рухаються в ідеальному танці зі швидкістю світла.
54. [Справжня ціна кремнію] Кожна пластина коштує десятки тисяч доларів, і одна порошинка може знищити чіп; тут немає місця недбалості.
55. [Перегони мікронів] Перехід від мікронів до нанометрів вимагав мільярдних ставок на обладнання ASML Extreme Ultraviolet.
56. [Енергоефективність архітектури] Продуктивність на ват — це єдина метрика, яка має значення для суперкомп'ютерів наступного століття.
57. [Провал NV1 як благословення] Якби наш перший чіп був успішним, ми б ніколи не створили GPU. Невдача змусила нас переосмислити все.
58. [Партнерство з геймерами] Геймери всього світу фінансували наші дослідження протягом 20 років, перш ніж з'явився штучний інтелект.
59. [Гідність інженера] Інженер — це людина, яка змушує пісок (кремній) думати і розмовляти.
60. [Вірність парадигмі] Ми трималися за ідею прискорених обчислень тридцять років, коли весь ринок вважав це нішевою забавкою.
61. [Запуск CUDA 2006] «У 2006 році ми інтегрували CUDA в кожен наш чіп безкоштовно. Це коштувало нам мільярдів доларів і обвалило акції, але створило сучасний ШІ».
62. [Zero-Billion-Dollar Markets] «Ніколи не йдіть туди, де вже штовхаються конкуренти. Шукайте ринки, які оцінюються у нуль доларів, і створюйте нові галузі з нуля».
63. [Уолл-стріт проти CUDA] Аналітики благали мене вилучити блоки CUDA і знизити собівартість. Якби я їх послухав, ШІ-революція затрималася б на 15 років.
64. [DGX-1 для OpenAI] У 2016 році я особисто привіз у Сан-Франциско перший суперкомп'ютер DGX-1 і підписав його для Ілона Маска та Сема Альтмана.
65. [Апаратний симбіоз з AlexNet] Коли Хінтон і Суцкевер запустили AlexNet на двох геймерських картах GTX 580, ми зрозуміли: настав наш зоряний час.
66. [Швидкість як екосистема] CUDA — це не просто мова програмування. Це мільйони бібліотек (cuDNN, TensorRT), які неможливо скопіювати за один день.
67. [Монополія користі] Конкуренти намагаються скопіювати наше залізо, але вони не розуміють: справжня цінність полягає в екосистемі програмного забезпечення.
68. [Математика матричного множення] Штучний інтелект у своїй основі — це гігантське множення матриць. Ми оптимізували Tensor Cores саме під цю операцію.
69. [Інвестиції у збиткові роки] Десять років поспіль інвестори карали наші акції за інвестиції в наукові обчислення. Ми вистояли завдяки вірі у фізику.
70. [Перетворення GPU на AI суперкомп'ютер] Один сервер більше не є одиницею обчислень; одиницею став дата-центр з 100 000 з'єднаних чіпів.
71. [Культура відкритості для вчених] Ми роздавали плати університетам безкоштовно, щоб виростити покоління дослідників, які вміють писати код для GPU.
72. [Перехід від графіки до науки] Моделювання згортання білків, астрофізика, прогноз клімату — все це перейшло на CUDA задовго до появи ChatGPT.
73. [Захисний рів екосистеми] Справжній рів (moat) — це не патенти. Це чотири мільйони розробників, які звикли думати в термінах нашої платформи.
74. [Сміливість створювати попит] Ми створили обчислювальну потужність для генеративного ШІ ще до того, як світ зрозумів, що йому потрібен генеративний ШІ.
75. [Сила стандартизації] Той самий код, написаний для ноутбука розробника, працює на кластері з десяти тисяч GPU в дата-центрі.
76. [Створення платформи Omniverse] Omniverse — це цифровий двійник реальності для навчання роботів і тестування автономних фабрик.
77. [Смерть CPU у навчанні ШІ] Використовувати CPU для навчання сучасних LLM — це те саме, що намагатися викопати тунель чайною ложкою.
78. [Трансформація компанії] Ми перестали бути компанією чіпів і стали компанією інфраструктури обчислювальних платформ.
79. [Мережевий комутатор Quantum InfiniBand] Купівля Mellanox за $6.9 млрд була геніальним кроком: передача даних між GPU стала швидшою за шини материнської плати.
80. [Ціна терпіння] Терпіння в інженерії — це здатність щодня копати колодязь, навіть коли перші краплі води з'являться через десять років.
81. [Закон масштабування інфраструктури] Подвоєння кількості чіпів у кластері повинно давати лінійне прискорення навчання без втрат на синхронізацію.
82. [Довіра наукової спільноти] Вчені обирають NVIDIA, тому що наш код не підводить у критичний момент багатомісячного тренування моделей.
83. [Сміливість великих ставок] Ми поставили все майбутнє компанії на CUDA у 2006 році. Це був найбільший ва-банк в історії кремнієвої долини.
84. [Магія паралелізму] Коли тисячі ядер одночасно оновлюють ваги нейромережі, ви чуєте гул народження нової цифрової свідомості.
85. [Служіння науковому прогресу] NVIDIA існує для того, щоб розв'язувати задачі, які звичайні комп'ютери не здатні вирішити в принципі.
86. [Закон Хуанга] «Закон Мура помер. Закон Хуанга доводить: синергія чіпів, софту, мереж та охолодження збільшує продуктивність у 1000 разів за 8 років».
87. [ШІ як промислова революція] «Штучний інтелект — це не програмне забезпечення. Це нова промислова епоха, де дата-центри перетворюють енергію на токени інтелекту».
88. [ШІ-фабрики майбутнього] У 19 столітті фабрики виробляли текстиль і сталь завдяки паровим двигунам. Сьогодні ШІ-фабрики виробляють знання.
89. [Суверенний ШІ] «Кожна суверенна нація зобов'язана володіти власним ШІ, який береже її мову, культуру, історію та національні дані».
90. [Смерть мов програмування] «Комп'ютер тепер розуміє людську мову. Найкращою мовою програмування у світі стала англійська, українська чи китайська».
91. [Демократизація кодингу] Тепер кожен фермер, лікар чи вчитель є програмістом, тому що він може пояснити завдання штучному інтелекту словами.
92. [Чіп Blackwell B200] Blackwell — це не просто чіп; це двигун нової промислової революції, що виконує 20 квадрильйонів операцій на секунду.
93. [Рідкісне охолодження] Ми більше не можемо охолоджувати дата-центри повітрям; рідке охолодження стало обов'язковим інженерним стандартом.
94. [Енергетична ефективність токенів] Наша мета — зменшити споживання енергії на один згенерований токен у тисячі разів.
95. [Автономні роботи (Physical AI)] Наступна велика хвиля ШІ — це фізичний інтелект: гуманоїдні роботи, автономні трактори та автоматизовані заводи.
96. [Платформа Isaac для роботів] Роботи повинні спочатку прожити мільйони годин у віртуальному симуляторі Omniverse, перш ніж вийти на реальні вулиці.
97. [ШІ для проектування чіпів] Ми використовуємо моделі ШІ для розведення доріжок нових чіпів NVIDIA; людина вже не здатна вручну оптимізувати 200 млрд транзисторів.
98. [Капіталізація у $3 трильйони] Ринкова капіталізація — це просто оцінка довіри інвесторів. Головне — продовжувати працювати так, ніби ми за 30 днів до краху.
99. [Перегони інфраструктури] Той, хто першим збудує кластери на 1 000 000 GPU, отримає вирішальну технологічну перевагу в XXI столітті.
100. [Економіка знань] Генерація токенів стане найбільшим бізнесом на планеті, більшим за нафту, автомобілебудування та авіацію.

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1444 слів): `02_SCRIPTS/episode_02_huang/director_script_huang.md`*

### АКТ 1. Іржа, порцеляна та холод Кентуккі (0:00 – 5:15)
*Музика: Suno Pro — `EP02_MUS_01_ACT1_92BPM_Rust_Porcelain.wav`*
* **0:00 - 0:20** | [SFX: Важкий звук краплі води у кахельному приміщенні] | **Диктор:** Сучасний світ технологій любить стерильні легенди. Але справжня імперія кремнію народилася не в сонячному гаражі, а на холодній кахельній підлозі громадського туалету в глушині Кентуккі.
* **0:20 - 2:15** |  | **Диктор:** Дев'ятирічний емігрант із Тайваню потрапляє до баптистського реформаторію для важких підлітків. Він вчить старшого бійця читати, а той — віджиматися. А вдень — щоденне чищення туалетів протягом двох років. *«Це назавжди випалило з моєї душі пиху»*.
* **2:15 - 5:15** | [VIDEO: `EP02_VID_01_Denny_Diner.txt`] | **Диктор:** Нічна зміна посудомийника в закусочній Denny's. Перетворення хаосу посуду на інженерний конвеєр. За цим самим столиком через 15 років він намалює план заснування NVIDIA.

### АКТ 2. Тридцять днів до темряви (5:15 – 10:45)
*Музика: Suno Pro — `EP02_MUS_05_ACT2_92BPM_Thirty_Days_Zero.wav`*
* **5:15 - 8:00** |  | **Диктор:** Квітень 1993 року. Під кулями в Сан-Хосе троє засновників створюють NVIDIA. Фатальна ставка на квадратичні поверхні в чіпі NV1 і вихід Direct3D з трикутниками. Компанія за 30 днів від банкрутства.
* **8:00 - 10:45** |  | **Диктор:** Відчайдушний політ Хуанга до Токіо. Абсолютна чесність перед президентом Sega: *«Наш чіп не підходить, але ви маєте заплатити нам 5 мільйонів, інакше ми помремо завтра»*. Самурайський порятунок і віртуальне проєктування RIVA 128. Правило трьох цілих десятиліть: *«До нашого банкрутства залишилося рівно 30 днів»*.

### АКТ 3. Велика єресь CUDA та кузня інтелекту (10:45 – 16:15)
*Музика: Suno Pro — `EP02_MUS_09_ACT3_92BPM_CUDA_Bet.wav`*
* **10:45 - 13:45** |  | **Диктор:** 2006 рік. Фінансове самогубство Уолл-стріт: вимога вбудувати програмну архітектуру CUDA у кожен чіп. Десять років збитків, обвал акцій на 80% у 2008-му. Хуанг непохитний: *«Ми будуємо ринок, який дорівнюватиме всій світовій економіці»*.
* **13:45 - 16:15** |  | **Диктор:** 2012 рік. Торонто. AlexNet на відеокартах GeForce GTX 580 відкриває ворота глибокого навчання. У 2016 році Хуанг особисто везе перший суперкомп'ютер DGX-1 до лабораторії OpenAI зі словами: *«Заради майбутнього людства»*.

### АКТ 4. Анатомія лідера без кабінету та кодекс болю (16:15 – 21:00)
*Музика: Suno Pro — `EP02_MUS_13_ACT4_92BPM_Silicon_Forge.wav`*
* **16:15 - 19:30** |  | **Диктор:** Відсутність кабінету, 50 прямих підпорядкованих, скасування звітів. Філософія зі Стенфорду: *«Я бажаю вам великих порцій болю і страждань, бо велич кується лише через труднощі»*.
* **19:30 - 21:00** | [SFX: Глибокий удар індустріального молота] | **Диктор:** Татуювання логотипа на плечі. О п'ятій ранку наймогутніший інженер планети дивиться у дзеркало і знає: розслаблятися не можна.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP02_MUS_01_ACT1_92BPM_Rust_Porcelain.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Rust Porcelain', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP02_AMB_02_ACT1_DRONE_Bathroom_Echo.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Bathroom Echo', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP02_MUS_03_ACT1_92BPM_Appalachian_Forest.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Appalachian Forest', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP02_MUS_04_ACT1_92BPM_Dennys_Dishwasher.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Dennys Dishwasher', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP02_MUS_05_ACT2_92BPM_Thirty_Days_Zero.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Thirty Days Zero', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP02_MUS_06_ACT2_92BPM_Sega_Tokyo_Meeting.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Sega Tokyo Meeting', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP02_AMB_07_ACT2_DRONE_Silicon_Failure.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Silicon Failure', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP02_MUS_08_ACT2_92BPM_Riva_Resurrection.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Riva Resurrection', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP02_MUS_09_ACT3_92BPM_CUDA_Bet.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'CUDA Bet', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP02_AMB_10_ACT3_DRONE_WallStreet_Crash.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'WallStreet Crash', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP02_MUS_11_ACT3_92BPM_Toronto_2012.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Toronto 2012', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP02_MUS_12_ACT3_92BPM_DGX1_Delivery.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'DGX1 Delivery', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP02_MUS_13_ACT4_92BPM_Silicon_Forge.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Silicon Forge', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP02_MUS_14_ACT4_92BPM_Endeavor_HQ.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Endeavor HQ', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP02_MUS_15_ACT4_92BPM_Blackwell_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental industrial dark downtempo, 92 bpm, heavy sub-bass pulse, metallic foundry reverb, melancholic tremolo guitar notes, ticking survival metronome, cue theme 'Blackwell Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP02_SFX_16_GLOBAL_Industrial_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 60%, Clarity 85%. Доріжка A1.*

* `EP02_VO_UA_01_ACT1_Reformatory.wav` | `EP02_VO_EN_01_ACT1_Reformatory.wav` (ACT1 — Reformatory)
* `EP02_VO_UA_02_ACT1_Dennys_Conveyor.wav` | `EP02_VO_EN_02_ACT1_Dennys_Conveyor.wav` (ACT1 — Dennys Conveyor)
* `EP02_VO_UA_03_ACT2_Silicon_Valley_1993.wav` | `EP02_VO_EN_03_ACT2_Silicon_Valley_1993.wav` (ACT2 — Silicon Valley 1993)
* `EP02_VO_UA_04_ACT2_Tokyo_Samurai.wav` | `EP02_VO_EN_04_ACT2_Tokyo_Samurai.wav` (ACT2 — Tokyo Samurai)
* `EP02_VO_UA_05_ACT3_CUDA_Heresy.wav` | `EP02_VO_EN_05_ACT3_CUDA_Heresy.wav` (ACT3 — CUDA Heresy)
* `EP02_VO_UA_06_ACT3_Toronto_Awakening.wav` | `EP02_VO_EN_06_ACT3_Toronto_Awakening.wav` (ACT3 — Toronto Awakening)
* `EP02_VO_UA_07_ACT4_Pain_And_Character.wav` | `EP02_VO_EN_07_ACT4_Pain_And_Character.wav` (ACT4 — Pain And Character)
* `EP02_VO_UA_08_ACT4_Thirty_Days_Left.wav` | `EP02_VO_EN_08_ACT4_Thirty_Days_Left.wav` (ACT4 — Thirty Days Left)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP02_VID_001_ACT1_24FPS_Porcelain_Tile.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Сучасний світ технологій любить стерильні легенди.
     - *Veo Prompt:* `Extreme macro cinematic shot of cold water droplets sliding down cracked white porcelain tile in a dark 1970s dormitory bathroom, rusty iron pipe in foreground, moody desaturated cyan and amber lighting, heavy 35mm film grain, 4k 24fps.`
002. `EP02_VID_002_ACT1_24FPS_Dennys_Neon.mp4` [00:04 – 00:08 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Сучасний світ технологій любить стерильні легенди.
     - *Veo Prompt:* `Cinematic night shot through rain-streaked glass of a 1978 American roadside diner "Denny's", warm neon sign reflecting on wet asphalt, inside steam rising from a commercial kitchen dishwashing station, 35mm Kodak film look, 4k.`
003. `EP02_VID_003_ACT1_24FPS_Silicon_Wafer.mp4` [00:08 – 00:12 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* Нам розповідають про геніїв у сонячних каліфорнійських гаражах, про золотих дітей престижних університетів, яким доля з пелюшок вклала в руки акції майбутніх моно…
     - *Veo Prompt:* `Microscopic golden wire bonding machine firing at supersonic speed on a microchip die, sparks of pure light in macro, precision engineering triumph, 8k.`
004. `EP02_VID_004_ACT1_24FPS_University_Archive_Hall_Silhouette_Moo.mp4` [00:12 – 00:16 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але справжня імперія, на чиїх плечах сьогодні тримається весь штучний інтелект планети, народилася не в університетському клубі.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP02_VID_005_ACT1_24FPS_Startup_Night_Workspace_SlowMo_Insert.mp4` [00:16 – 00:20 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вона народилася на холодній кахельній підлозі громадського туалету в глушині штату Кентуккі.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP02_VID_006_ACT1_24FPS_KeyScene_02_Architectural_Corridor_A.mp4` [00:20 – 00:31 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Дев'ятирічний хлопчик із Тайваню на ім'я Дженсен Хуанг разом зі старшим братом прилітає до Сполучених Штатів.
     - *Veo Prompt:* `Atmospheric slow tracking shot through a foggy Appalachian mountain forest at dusk, 1973 aesthetic, a lonely brick reformatory building in the distance with dim yellow windows, cinematic anamorphic lens, melancholic mood, 4k.`
007. `EP02_VID_007_ACT1_24FPS_Neural_Horizon_Pulse_A1S07_Anamorphic.mp4` [00:31 – 00:42 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Батьки відправили їх уперед — до дядька, сподіваючись дати дітям елітну американську освіту.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP02_VID_008_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S08_Tracki.mp4` [00:42 – 00:53 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Йому здається, що це закритий пансіон для обдарованих юнаків.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
009. `EP02_VID_009_ACT1_24FPS_Equation_Notebook_Macro_A1S09_Overhead.mp4` [00:53 – 01:04 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Дженсену дев'ять.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP02_VID_010_ACT1_24FPS_Silicon_Wafer_Lithography_Optical_Data.mp4` [01:04 – 01:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його селять у кімнату із сімнадцятирічним хлопцем, чиє тіло вкрите татуюваннями та свіжими шрамами від ножових поранень.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP02_VID_011_ACT1_24FPS_KeyScene_03_Architectural_Corridor_A.mp4` [01:15 – 01:27 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У такому місці слабкість — це вирок.
     - *Veo Prompt:* `Macro shot of an old English paperback dictionary lying on a scratched wooden desk, a small child's finger tracing printed words under a single dim tungsten bulb, floating dust motes, tactile texture, 4k.`
012. `EP02_VID_012_ACT1_24FPS_Hippocampus_Memory_Maze_SlowMo_Insert.mp4` [01:27 – 01:39 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Маленький емігрант робить свій перший дорослий розрахунок.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP02_VID_013_ACT1_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [01:39 – 01:51 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він укладає пакт із ватажком гуртожитку: щовечора при світлі тьмяної лампи дев'ятирічний Дженсен вчить сімнадцятирічного бійця читати по складах.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP02_VID_014_ACT1_24FPS_Equation_Notebook_Macro_A1S14_Anamorph.mp4` [01:51 – 02:03 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А вдень починається трудова повинність.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
015. `EP02_VID_015_ACT1_24FPS_Silicon_Light_Refraction_A1S15_Trackin.mp4` [02:03 – 02:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Старшим дістається кухня чи двір.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP02_VID_016_ACT1_24FPS_KeyScene_04_Kentucky_Porcelain_Grit.mp4` [02:15 – 02:30 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Він миє унітази щодня протягом двох років.
     - *Veo Prompt:* `Abstract visual transition: swirling soapy water in a dark sink slowly morphing into a glowing constellation of liquid silver particles, hypnotic slow motion, Octane render, 8k.`
017. `EP02_VID_017_ACT1_24FPS_School_Auditorium_Stage_Optical_DataVi.mp4` [02:30 – 02:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Через пів століття, стоячи на сцені перед елітою Стенфорду в чорній шкіряній куртці людини, чия компанія коштує трильйони доларів, він скаже фразу, від якої в зал…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP02_VID_018_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S18_Silhou.mp4` [02:45 – 03:00 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І знаєте, що це мені дало?
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP02_VID_019_ACT1_24FPS_Equation_Notebook_Macro_A1S19_SlowMo_I.mp4` [03:00 – 03:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це назавжди випалило з моєї душі пиху.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP02_VID_020_ACT1_24FPS_Silicon_Light_Refraction_A1S20_Macro_D.mp4` [03:15 – 03:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Не буває низької праці.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
021. `EP02_VID_021_ACT1_24FPS_KeyScene_05_Dennys_Midnight_Booth.mp4` [03:30 – 03:51 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли батьки нарешті переїжджають до Орегону, п'ятнадцятирічний Дженсен влаштовується на свою першу офіційну роботу — нічним посудомийником у придорожню закусочну…
     - *Veo Prompt:* `Cinematic night shot through rain-streaked glass of a 1978 American roadside diner "Denny's", warm neon sign reflecting on wet asphalt, inside steam rising from a commercial kitchen dishwashing station, 35mm Kodak film look, 4k.`
022. `EP02_VID_022_ACT1_24FPS_Neural_Horizon_Pulse_A1S22_Tracking_Me.mp4` [03:51 – 04:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він був патологічно сором'язливим підлітком.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP02_VID_023_ACT1_24FPS_Dennys_Midnight_Booth_Overhead_GodsEye.mp4` [04:12 – 04:33 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але біля мийки з гарячою парою він перетворює хаос брудного посуду на інженерний конвеєр: він сортує тарілки за геометрією, оптимізує кут нахилу струменя води, ск…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP02_VID_024_ACT1_24FPS_Dennys_Midnight_Booth_Optical_DataViz.mp4` [04:33 – 04:54 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він стає найшвидшим посудомийником зміни.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP02_VID_025_ACT1_24FPS_Silicon_Light_Refraction_A1S25_Silhoue.mp4` [04:54 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ти не можеш боятися світу, коли щоночі обслуговуєш десятки втомлених далекобійників.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP02_VID_026_ACT2_24FPS_KeyScene_01_Hero_Workspace_Atmospher.mp4` [05:15 – 05:26 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Квітень 1993 року.
     - *Veo Prompt:* `Macro close-up of a steaming cup of black coffee on a green laminate diner table, next to a paper napkin with hand-drawn microprocessor architecture diagrams in blue ink, moody morning light, 4k.`
027. `EP02_VID_027_ACT2_24FPS_Dennys_Midnight_Booth_Anamorphic_Wide.mp4` [05:26 – 05:36 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Та сама мережа закусочних Denny's на перехресті Берріесса-роуд.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP02_VID_028_ACT2_24FPS_Dennys_Midnight_Booth_Tracking_Medium.mp4` [05:36 – 05:47 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Троє інженерів — Дженсен Хуанг, Кріс Малаховськи та Кертіс Прем — годинами п'ють дешеву каву з безкоштовним доливанням.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP02_VID_029_ACT2_24FPS_Architectural_Corridor_A2S04_Overhead.mp4` [05:47 – 05:58 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На вулиці стріляють — вікна ресторану пробиті кулями місцевих банд, але вони навіть не повертають голови.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP02_VID_030_ACT2_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [05:58 – 06:09 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони бачать те, чого не бачить Intel.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP02_VID_031_ACT2_24FPS_Hero_Workspace_Atmosphere_A2S06_Silhou.mp4` [06:09 – 06:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Весь світ будує універсальні процесори CPU, які виконують операції послідовно — крок за кроком, як бухгалтер з рахівницею.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP02_VID_032_ACT2_24FPS_Hippocampus_Memory_Maze_SlowMo_Insert.mp4` [06:19 – 06:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але майбутнє — це тривимірні симуляції, відеоігри та візуальні світи, де мільйони пікселів потрібно обчислювати одночасно.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP02_VID_033_ACT2_24FPS_KeyScene_02_Backpropagation_Error_Wa.mp4` [06:30 – 06:45 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* І вони роблять фатальну помилку.
     - *Veo Prompt:* `A shattered silicon wafer in extreme macro on a dark steel table, cold blue laboratory light, sharp metallic fragments, symbol of technological failure, Octane render, 4k.`
034. `EP02_VID_034_ACT2_24FPS_Architectural_Corridor_A2S09_Anamorphi.mp4` [06:45 – 07:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Два роки праці.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP02_VID_035_ACT2_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [07:00 – 07:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хуанг та його команда вирішують будувати тривимірну графіку на основі квадратичних поверхонь.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
036. `EP02_VID_036_ACT2_24FPS_Hyperscale_Compute_Cluster_Overhead_Go.mp4` [07:15 – 07:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але в той самий момент корпорація Microsoft випускає стандарт Direct3D, який наказує всій індустрії будувати графіку виключно з трикутників.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP02_VID_037_ACT2_24FPS_Startup_Night_Workspace_Optical_DataVi.mp4` [07:30 – 07:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І водночас на ринок виходять тридцять вісім інших стартапів із виробництва графічних чіпів.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP02_VID_038_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [07:45 – 08:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Його ніхто не купує.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP02_VID_039_ACT2_24FPS_KeyScene_03_Architectural_Corridor_A.mp4` [08:00 – 08:15 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Це точка, де ламаються 99% підприємців.
     - *Veo Prompt:* `Solitary silhouette of a man standing in a dark empty office floor at 3 AM, looking out at distant city lights, rain on window, extreme cinematic contrast, 35mm film grain, 4k.`
040. `EP02_VID_040_ACT2_24FPS_Neural_Horizon_Pulse_A2S15_Macro_Detai.mp4` [08:15 – 08:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хуанг збирає всіх працівників у головному залі і звільняє половину компанії.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP02_VID_041_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [08:30 – 08:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У нього залишається один відчайдушний хід.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP02_VID_042_ACT2_24FPS_Thirty_Days_Wireframe_Chip_Tracking_Me.mp4` [08:45 – 09:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо Хуанг продовжить виконувати контракт — Sega отримає провальний продукт, а NVIDIA помре за пів року.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of 3D wireframe polygon mesh snapping into razor-sharp silicon die blueprint on a 1996 engineering workstation, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP02_VID_043_ACT2_24FPS_Thirty_Days_Wireframe_Chip_Overhead_Go.mp4` [09:00 – 09:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хуанг летить у Токіо до президента Sega Ірімадзірі-сана.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of 3D wireframe polygon mesh snapping into razor-sharp silicon die blueprint on a 1996 engineering workstation, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
044. `EP02_VID_044_ACT2_24FPS_Constitutional_Crystal_Box_Optical_Dat.mp4` [09:15 – 09:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ви повинні негайно розірвати з нами контракт.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dark opaque cube turning into transparent optical quartz revealing ordered golden ethical compass vectors, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP02_VID_045_ACT2_24FPS_KeyScene_04_Seoul_Move_37_Go_Stone.mp4` [09:30 – 09:42 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Абсолютна, оголена чесність перед лицем смерті обеззброїла самурая старого гарту.
     - *Veo Prompt:* `Microscopic golden wire bonding machine firing at supersonic speed on a microchip die, sparks of pure light in macro, precision engineering triumph, 8k.`
046. `EP02_VID_046_ACT2_24FPS_Thirty_Days_Wireframe_Chip_SlowMo_Inse.mp4` [09:42 – 09:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Sega перераховує 5 мільйонів доларів в обмін на частку в напівмертвій компанії.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of 3D wireframe polygon mesh snapping into razor-sharp silicon die blueprint on a 1996 engineering workstation, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP02_VID_047_ACT2_24FPS_Equation_Notebook_Macro_A2S22_Macro_De.mp4` [09:55 – 10:08 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ці гроші дають NVIDIA шість місяців кисню.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP02_VID_048_ACT2_24FPS_DryCleaner_Steam_Window_Anamorphic_Wid.mp4` [10:08 – 10:20 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли перша партія кремнію виходить із печей на Тайвані, чіп заводиться з першої секунди.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of clouds of backlit white steam rising from a heavy garment press against a rain-streaked New Jersey shopfront, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP02_VID_049_ACT2_24FPS_Architectural_Corridor_A2S24_Tracking.mp4` [10:20 – 10:32 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* За чотири місяці продано мільйон екземплярів.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP02_VID_050_ACT2_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [10:32 – 10:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* NVIDIA повертається з того світу.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP02_VID_051_ACT3_24FPS_KeyScene_01_Silicon_Light_Refraction.mp4` [10:45 – 10:55 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 1999 році NVIDIA випускає GeForce 256 і дарує світові саме поняття — GPU (графічний процесор).
     - *Veo Prompt:* `Comparison visual in 3D space: a single bright beam moving slowly in a straight line (CPU) versus a massive tidal wave of millions of synchronized glowing particles crashing forward simultaneously (GPU), Octane render, 8k.`
052. `EP02_VID_052_ACT3_24FPS_Architectural_Corridor_A3S02_SlowMo_In.mp4` [10:55 – 11:05 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 1999 році NVIDIA випускає GeForce 256 і дарує світові саме поняття — GPU (графічний процесор).
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP02_VID_053_ACT3_24FPS_Silicon_Wafer_Lithography_Macro_Detail.mp4` [11:05 – 11:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Компанія виходить на біржу, акції летять угору.
     - *Veo Prompt:* `Extreme macro push-in shot of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP02_VID_054_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S04_Anamor.mp4` [11:15 – 11:25 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Здавалося б — живи і насолоджуйся монополією у світі відеоігор.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP02_VID_055_ACT3_24FPS_Equation_Notebook_Macro_A3S05_Tracking.mp4` [11:25 – 11:35 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Здавалося б — живи і насолоджуйся монополією у світі відеоігор.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP02_VID_056_ACT3_24FPS_Silicon_Wafer_Lithography_Overhead_God.mp4` [11:35 – 11:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але у 2006 році Дженсен Хуанг робить крок, який Уолл-стріт назове «фінансовим самогубством».
     - *Veo Prompt:* `Top-down vertical birds-eye composition of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP02_VID_057_ACT3_24FPS_Macintosh_Logic_Board_Optical_DataViz.mp4` [11:45 – 11:55 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на свої відеокарти і бачить у них сплячий суперкомп'ютер.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP02_VID_058_ACT3_24FPS_Macintosh_Logic_Board_Silhouette_Mood.mp4` [11:55 – 12:05 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він дивиться на свої відеокарти і бачить у них сплячий суперкомп'ютер.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP02_VID_059_ACT3_24FPS_Hyperscale_Compute_Cluster_SlowMo_Inse.mp4` [12:05 – 12:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він наказує інженерам створити CUDA — програмну архітектуру, яка перетворює графічний чіп на універсальну матрицю для важких наукових обчислень.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP02_VID_060_ACT3_24FPS_KeyScene_02_Silicon_Wafer_Lithograph.mp4` [12:15 – 12:26 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Хуанг вимагає вбудовувати апаратну підтримку CUDA у кожен без винятку чіп NVIDIA.
     - *Veo Prompt:* `Dark Wall Street stock ticker boards showing red falling numbers reflected in a pair of glasses, cold cynical atmosphere, slow motion, 4k.`
061. `EP02_VID_061_ACT3_24FPS_Silicon_Wafer_Lithography_Anamorphic_W.mp4` [12:26 – 12:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Хуанг вимагає вбудовувати апаратну підтримку CUDA у кожен без винятку чіп NVIDIA.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP02_VID_062_ACT3_24FPS_Hyperscale_Compute_Cluster_Tracking_Me.mp4` [12:38 – 12:49 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це коштує компанії мільярди доларів.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP02_VID_063_ACT3_24FPS_Neural_Horizon_Pulse_A3S13_Overhead_Go.mp4` [12:49 – 13:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Площа кристала зростає, собівартість летить угору, а попиту немає.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP02_VID_064_ACT3_24FPS_Silicon_Wafer_Lithography_Optical_Data.mp4` [13:00 – 13:11 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Протягом десяти довгих років акціонери на кожному квартальному звіті вимагають від Хуанга припинити спалювати гроші на нікому не потрібну CUDA.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP02_VID_065_ACT3_24FPS_Equation_Notebook_Macro_A3S15_Silhouet.mp4` [13:11 – 13:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2008 році капіталізація NVIDIA обвалюється на 80%.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP02_VID_066_ACT3_24FPS_Silicon_Light_Refraction_A3S16_SlowMo.mp4` [13:22 – 13:34 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але Хуанг стоїть як скеля:

«Ми не орієнтуємося на поточний ринок.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP02_VID_067_ACT3_24FPS_Hyperscale_Compute_Cluster_Macro_Detai.mp4` [13:34 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми будуємо ринок, розмір якого сьогодні дорівнює нулю мільярдів доларів, але завтра дорівнюватиме всій світовій економіці».
     - *Veo Prompt:* `Extreme macro push-in shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP02_VID_068_ACT3_24FPS_KeyScene_03_Neural_Horizon_Pulse_A3S.mp4` [13:45 – 14:04 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* І ось настає 2012 рік.
     - *Veo Prompt:* `A dimly lit bedroom in Toronto, 2012: two gaming graphics cards connected inside an open PC case, cooling fans spinning, green LED light illuminating equations on a whiteboard, cinematic documentary reconstruction, 4k.`
069. `EP02_VID_069_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S19_Tracki.mp4` [14:04 – 14:22 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І ось настає 2012 рік.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP02_VID_070_ACT3_24FPS_University_Archive_Hall_Overhead_GodsE.mp4` [14:22 – 14:41 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У холодній кімнаті в Торонто двоє аспірантів Джеффрі Хінтона — Алекс Крижевський та Ілля Суцкевер — купують у звичайному магазині дві ігрові відеокарти GeForce GT…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP02_VID_071_ACT3_24FPS_Silicon_Wafer_Lithography_Optical_Data.mp4` [14:41 – 15:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Завдяки вшитій туди системі CUDA вони запускають навчання глибокої нейромережі AlexNet.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP02_VID_072_ACT3_24FPS_Architectural_Corridor_A3S22_Silhouett.mp4` [15:00 – 15:19 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Те, на що звичайним процесорам знадобилися б роки, відеокарти Хуанга прораховують за шість днів.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP02_VID_073_ACT3_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [15:19 – 15:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Десять років впертого очікування у темряві окупаються в одну історичну секунду.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP02_VID_074_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S24_Macro.mp4` [15:38 – 15:56 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки інші корпорації ще тільки читають наукові звіти, Хуанг ставить усе існування NVIDIA на єдину карту — глибоке навчання.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP02_VID_075_ACT3_24FPS_Macintosh_Logic_Board_Anamorphic_Wide.mp4` [15:56 – 16:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2016 році він особисто привозить у скромний офіс лабораторії OpenAI важкий сталевий ящик — перший у світі суперкомп'ютер для штучного інтелекту DGX-1, розписуєт…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP02_VID_076_ACT4_24FPS_KeyScene_01_Neural_Horizon_Pulse_A4S.mp4` [16:15 – 16:25 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Сьогодні NVIDIA — це серцевина нової промислової революції.
     - *Veo Prompt:* `Architectural shot of NVIDIA Endeavor headquarters: vast open triangular space filled with natural light and whiteboards, no walls, no private offices, engineers working together at long tables, 4k.`
077. `EP02_VID_077_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S02_Optica.mp4` [16:25 – 16:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні NVIDIA — це серцевина нової промислової революції.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP02_VID_078_ACT4_24FPS_Equation_Notebook_Macro_A4S03_Silhouet.mp4` [16:35 – 16:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Проте всередині цієї трильйонної імперії панують закони, які ламають усі підручники з менеджменту.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP02_VID_079_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [16:45 – 16:55 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У Дженсена Хуанга немає власного кабінету.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP02_VID_080_ACT4_24FPS_London_Tournament_Chessboard_Macro_Det.mp4` [16:55 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він працює за звичайним столом посеред загального залу або в переговорних кімнатах біля білої дошки.
     - *Veo Prompt:* `Extreme macro push-in shot of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP02_VID_081_ACT4_24FPS_London_Tournament_Chessboard_Anamorphi.mp4` [17:05 – 17:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він працює за звичайним столом посеред загального залу або в переговорних кімнатах біля білої дошки.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of hand-carved Staunton chess knight poised above a worn tournament wooden board with analog chess clock ticking, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP02_VID_082_ACT4_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [17:15 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У нього в прямому підпорядкуванні перебуває понад п'ятдесят керівників одночасно.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP02_VID_083_ACT4_24FPS_Monastic_White_Sanctuary_Overhead_Gods.mp4` [17:25 – 17:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він скасував звіти про статус проектів і особисті наради сам на сам:

«Якщо інформація проходить через п'ять поверхів начальників — правда вмирає по дорозі.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP02_VID_084_ACT4_24FPS_Silicon_Light_Refraction_A4S09_Optical.mp4` [17:35 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Будь-який молодший інженер у компанії має право написати мені напряму о третій ночі, якщо він знайшов фундаментальну проблему».
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP02_VID_085_ACT4_24FPS_KeyScene_02_Kentucky_Porcelain_Grit.mp4` [17:45 – 17:58 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Який головний кодекс життя залишає нам хлопець, який пройшов шлях від йоржика в реформаторії до кузні світового розуму?
     - *Veo Prompt:* `Close-up of a rough piece of raw volcanic rock slowly transforming under extreme heat and pressure into a flawless reflective silicon crystal wafer, macro thermodynamics, Octane render, 8k.`
086. `EP02_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [17:58 – 18:11 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Полюбіть біль і страждання.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP02_VID_087_ACT4_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [18:11 – 18:24 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* А тому я від щирого серця бажаю вам великих порцій болю і страждань».
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP02_VID_088_ACT4_24FPS_Equation_Notebook_Macro_A4S13_Anamorph.mp4` [18:24 – 18:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Велич народжується не з інтелекту.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP02_VID_089_ACT4_24FPS_Silicon_Light_Refraction_A4S14_Trackin.mp4` [18:38 – 18:51 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Перетворіть будь-яку працю на високе ремесло.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP02_VID_090_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [18:51 – 19:04 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Робіть це з такою інженерною точністю, ніби від цього залежить доля всесвіту.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP02_VID_091_ACT4_24FPS_Neural_Horizon_Pulse_A4S16_Optical_Dat.mp4` [19:04 – 19:17 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Створюйте нульові ринки.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP02_VID_092_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S17_Silhou.mp4` [19:17 – 19:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Шукайте завдання, які здаються іншим божевільними або надто важкими.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP02_VID_093_ACT4_24FPS_KeyScene_03_Silicon_Wafer_Lithograph.mp4` [19:30 – 19:41 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* На лівому плечі Дженсена Хуанга під чорною шкіряною курткою набите татуювання — логотип NVIDIA.
     - *Veo Prompt:* `Slow camera pull-back from a glowing wafer of Blackwell GPU architecture into a vast digital twin of Earth (Omniverse), cities, weather patterns and neural pathways glowing in harmony, IMAX scale, 8k 24fps.`
094. `EP02_VID_094_ACT4_24FPS_Silicon_Wafer_Lithography_Macro_Detail.mp4` [19:41 – 19:52 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На лівому плечі Дженсена Хуанга під чорною шкіряною курткою набите татуювання — логотип NVIDIA.
     - *Veo Prompt:* `Extreme macro push-in shot of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP02_VID_095_ACT4_24FPS_Dennys_Midnight_Booth_Anamorphic_Wide.mp4` [19:52 – 20:04 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли вони робили це татуювання тридцять років тому, він плакав від болю в кріслі майстра.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of steaming diner coffee mug beside a blue-ink microchip sketch on a paper napkin under red-and-yellow neon, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP02_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:04 – 20:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні цей знак викарбуваний у фундаменті всієї людської цивілізації.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP02_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [20:15 – 20:26 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І щоранку, прокидаючись о п'ятій годині, наймогутніший інженер планети дивиться у дзеркало не як переможець.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP02_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [20:26 – 20:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І щоранку, прокидаючись о п'ятій годині, наймогутніший інженер планети дивиться у дзеркало не як переможець.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring cold cracked white porcelain tile, warm rainy Denny's neon reflections on wet asphalt, microscopic gold wire-bonding sparks on silicon wafers, dark industrial Blackwell forge, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP02_VID_099_ACT4_24FPS_Kentucky_Porcelain_Grit_Silhouette_Moo.mp4` [20:38 – 20:49 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У глибині його очей все ще стоїть той дев'ятирічний хлопчик із Кентуккі, який знає: розслаблятися не можна.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of wet white porcelain tile and worn wooden scrub brush under cold fluorescent dormitory light in 1970s Kentucky, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP02_VID_100_ACT4_24FPS_Thirty_Days_Wireframe_Chip_SlowMo_Inse.mp4` [20:49 – 21:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* До банкрутства залишилося рівно тридцять днів.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of 3D wireframe polygon mesh snapping into razor-sharp silicon die blueprint on a 1996 engineering workstation, shot on Cooke Anamorphic/i 40mm & Laowa 24mm Probe Macro, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
