# МАСТЕР-ДОСЬЄ ПРОЄКТУ (v2.0 AUDITED): ЕПІЗОД 06 — ІЛЛЯ СУЦКЕВЕР
*Кінематографічний відеоесей (Cinematic Thoughtcast) // «Архітектори Розуму» // «Алхімік масштабування та тиші»*

---

## РОЗДІЛ 0. ПОКРОКОВИЙ АЛГОРИТМ ДІЙ (SOP ВИРОБНИЦТВА ЕПІЗОДУ)

### Етап 01. Ініціалізація та Smart Bins — Створення структури проєкту EP06 (Ілля Суцкевер) на диску та в DaVinci Resolve 19
*Ціль:* Підготувати локальне дерево папок і правила автоматичного сортування Smart Bins за стандартом Мастер-Досьє.
- [ ] Завантажити й запустити скрипт ініціалізації папок setup_EP06.sh (створює 01_VO_UA, 01_VO_EN, 02_MUS_92BPM, 03_AMB, 04_SFX, 05_VID_4K).
- [ ] Створити проєкт DaVinci Resolve 19: Timeline 3840×1606 (Scope 2.39:1), рівно 24.000 fps, Color Science: DaVinci YRGB Color Managed.
- [ ] Налаштувати 5 Smart Bins за правилом імені файлу: EP06_VO_, EP06_MUS_, EP06_AMB_, EP06_SFX_, EP06_VID_.

### Етап 02. Дикторська озвучка (VO UA + EN) — Генерація та контроль якості 8 сегментів диктора в ElevenLabs (Stability 70%, Clarity 75%. Доріжка A1 (медитативний тембр).)
*Ціль:* Отримати еталонну начитку повного сценарію (~1296 слів, хронометраж 21:45 хв) українською та англійською мовами.
- [ ] У вкладці «Сценарій» натиснути «🎙️ Копіювати чистий текст для ElevenLabs» по кожному з 4 Актів (без тегів SFX/VIDEO).
- [ ] Згенерувати всі 8 українських файлів EP06_VO_UA_01..08.wav (WAV 48kHz / 24-bit, Stability 70%, Clarity 75%. Доріжка A1 (медитативний тембр).).
- [ ] Згенерувати синхронний англомовний дубляж EP06_VO_EN_01..08.wav для YouTube Multi-Language Audio.
- [ ] Перевірити паузи між абзацами (0.8–1.2 с на філософських тезах) та відсутність артефактів наголосів.

### Етап 03. Саундтрек Suno Pro (92 BPM) — Генерація 16 іменних аудіо-стемів (12 MUS + 3 AMB + 1 SFX Global)
*Ціль:* Створити єдине музичне полотно з фіксованим пульсом 92 BPM (1 такт 4/4 = 2.609 с = 62.6 кадру при 24fps).
- [ ] Згенерувати у Suno Pro v4 12 музичних треків Актів 1–4 за готовими промптами з вкладки «Аудіо» та назвати їх точно як у реєстрі EP06_MUS_...wav.
- [ ] Згенерувати 3 безбітові фонові дрони EP06_AMB_...wav для заповнення драматичних пауз на доріжці A3.
- [ ] Підготувати пакет звукових акцентів EP06_SFX_16_GLOBAL_...wav (40Hz суб-дропи та предметні фолі-звуки епізоду).

### Етап 04. Візуальний ряд (100 кадрів Veo 2) — Генерація 100 покадрових 4K B-Roll сцен у Google Flow / Veo 2
*Ціль:* Закрити всі ~21 хвилину хронометражу 100 кінематографічними планами (по 25 кадрів на кожен Акт, середня довжина плану ~12.5 с).
- [ ] Згенерувати спочатку 13–17 опорних сцен (Key Shots) EP06_VID_... з вкладки «100 Промптів» (відфільтрувавши за «Ключові кадри»).
- [ ] Згенерувати детальні макро- та атмосферні плани B-Roll для Актів 1–2 (#001–#050) зі збереженням Smart Bin імен.
- [ ] Згенерувати кульмінаційні та фінальні плани B-Roll для Актів 3–4 (#051–#100) та перевірити частоту 24 fps.

### Етап 05. Монтаж у DaVinci Resolve (Edit) — Імпорт CSV-маркерів таймлайну та ритмічна збірка під 92 BPM
*Ціль:* Зібрати чотириактну драматургічну структуру без жодної чорної діри, склеюючи плани на сильних долях такту.
- [ ] У вкладці «DaVinci Студія» завантажити файл EP06_Timeline_Markers.csv та імпортувати його в Timeline (Import Timeline Markers from CSV).
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
- [ ] Експортувати основний майстер EP06_ilya_sutskever_4K_MASTER_UA.mov (H.265 / ProRes 422 HQ) + окремий аудіо-мікс EP06_MASTER_MIX_EN.wav (вимкнувши A1 UA та увімкнувши VO_EN).
- [ ] Завантажити відео на YouTube, додати англійську доріжку в розділі «Мови / Multi-Language Audio», прописати таймкоди 4 Актів і зробити бекап проєкту (.drp).

---

## РОЗДІЛ 1. АРХІТЕКТУРА ДАНИХ ТА СТАНДАРТ ІМЕНУВАННЯ (DAVINCI RESOLVE)

Стандарт іменування Smart Bins: `EP06_[Category]_[Scene]_[Act]_[Tempo]_[Description].[ext]`

* **`VO_UA` / `VO_EN`** — Озвучка диктора (Доріжка A1 / A1_EN, WAV 48kHz 24-bit).
* **`MUS`** — Музичні треки Suno Pro (92 BPM, Доріжка A2 з активним Sidechain Ducking -3.2 dB).
* **`AMB`** — Атмосферні фонові дрони (Доріжка A3, -22 dB).
* **`SFX`** — Звукові ефекти, суб-дропи 40Hz, переходи (Доріжка A4, -9 dB).
* **`VID`** — 100 візуальних B-Roll футажів (Google Flow / Veo 2, 4K Scope 2.39:1, 24fps).

---

## РОЗДІЛ 2. БІОГРАФІЧНЕ ДОСЬЄ ТА КРИЗИ

* **Походження та релокація:** Народився у грудні 1986 року в закритому радянському місті Горькому в родині інженера. У 1991 році разом із родиною репатріювався до Ізраїлю (Єрусалим), а згодом до Канади (Торонто).
* **Школа Хінтона:** У 17 років самостійно постукав у двері кабінету Джеффрі Хінтона в Університеті Торонто, вразивши професора оптимізацією його наукових статей.
* **AlexNet та Seq2Seq:** Співавтор AlexNet (2012) разом із Алексом Крижевським та Хінтоном. У 2014 році в Google Brain створив архітектуру Sequence-to-Sequence, яка навчила мережі перекладати мови через векторні простори.
* **OpenAI та Епоха GPT:** Співзасновник і головний науковець OpenAI (2015). Ідеолог і керівник створення GPT-1, GPT-2, GPT-3 та GPT-4 на базі законів масштабування (Scaling Hypothesis).
* **Листопадовий бунт та SSI:** У листопаді 2023 року очолив раду директорів під час тимчасового звільнення Сема Альтмана, згодом публічно розкаявся. У травні 2024 року залишив OpenAI і заснував **Safe Superintelligence (SSI)** у Пало-Альто та Тель-Авіві задля створення безпечного надінтелекту в абсолютній тиші.

---

## РОЗДІЛ 3. ПОВНИЙ КОРПУС 100 ФУНДАМЕНТАЛЬНИХ ТЕЗ ТА ЦИТАТ (ІЛЛЯ СУЦКЕВЕР)

1. [Походження та гарт] «У кожній науковій революції є свої генерали, але в центрі вихору завжди стоїть чернець від науки, чий погляд спрямований у чисту математичну безодню».
2. [Філософія майбутнього] «Ранній досвід дитини, яку перенесли з крижаної імперії на розпечене сонце біблійних пагорбів, навчив мене однієї аксіоми: зовнішній світ мінливий, а єдиний непорушний фундамент лежить усередині власного розуму».
3. [Походження та гарт] «Тримати в голові нерозв'язану задачу тижнями, не відступаючи перед глухою стіною — це єдиний справжній навик справжнього дослідника».
4. [Архітектура та наука] «Коли я постукав у двері кабінету професора Хінтона у сімнадцять років, я знав не те, що написано в підручниках, а те, як змусити код працювати швидше».
5. [Архітектура та наука] «Усі сміялися над нейромережами, а ми бачили просту річ: алгоритм зворотного поширення вже був досконалим. Йому бракувало лише масштабу».
6. [Кризи та стійкість] «Якщо взяти просту нейромережу і збільшити її в тисячу разів, кількість неминуче перейде в нову біологічну якість».
7. [Архітектура та наука] «Алхімія масштабування полягає в тому, що закон кількості обчислень не просто додає швидкості, він породжує нові емерджентні здібності».
8. [Філософія майбутнього] «Коли ми створювали AlexNet, ми зрозуміли: епоха ручних правил в штучному інтелекті назавжди закінчилася».
9. [Архітектура та наука] «Поглинання цілого речення і розгортання його в іншій мові через абстрактний векторний простір (Seq2Seq) було першим доказом того, що машини здатні оперувати чистими смислами».
10. [Етика та безпека ШІ] «Сема Альтман та Ілон Маск покликали мене у 2015 році створювати OpenAI не заради бізнесу, а заради порятунку людства від неконтрольованого майбутнього».
11. [Архітектура та наука] «Передбачення наступного слова при достатньому масштабі — це не проста лінгвістика. Це відновлення всієї прихованої реальності людського світу».
12. [Філософія майбутнього] «Уявіть детективний роман Агати Крісті на триста сторінок. Щоб вгадати одне останнє слово на зразок імені вбивці, мережа зобов'язана симулювати всю фізику та психологію сюжету».
13. [Філософія майбутнього] «Досконале стиснення інформації і є сам інтелект. Здатність стиснути терабайти тексту у ваги моделі означає створення внутрішньої моделі реальності».
14. [Кризи та стійкість] «Коли інженери казали, що модель вперлася у стелю, ми збільшували обчислення в десять разів — і стеля зникала».
15. [Філософія майбутнього] «Емерджентні здібності моделі — це момент, коли статистика перетворюється на розуміння».
16. [Кризи та стійкість] «Ми більше не пишемо програми у звичному розумінні. Ми викликаємо до життя новий тип розуму».
17. [Філософія майбутнього] «У міру того, як моделі ставали могутнішими, моя екзистенційна тривога зростала пропорційно їхній кількості параметрів».
18. [Етика та безпека ШІ] «На ретритах OpenAI я спалював дерев'яну статую неконтрольованого AGI, змушуючи інженерів клястися у безпеці майбутнього».
19. [Етика та безпека ШІ] «Безпека надінтелекту не може вирішуватися за залишковим принципом між релізами комерційних продуктів».
20. [Філософія майбутнього] «П'ятниця, 17 листопада 2023 року. Рішення ради директорів про звільнення Сема Альтмана було найважчим і водночас найщирішим кроком мого життя задля захисту місії».
21. [Етика та безпека ШІ] «Я глибоко шкодую про свою участь у бунті ради директорів та про біль, якого завдав команді, але наміри мої завжди були чистими».
22. [Етика та безпека ШІ] «Неможливо одночасно гнатися за сотнями мільйонів споживачів на ринку чат-ботів і зберігати абсолютну чистоту безпеки».
23. [Філософія майбутнього] «Травень 2024 року. Я назавжди зачинив за собою двері OpenAI, бо зрозумів: комерційний шум завжди перемагає обережність».
24. [Філософія майбутнього] «Safe Superintelligence (SSI) — це організація без клієнтів, без додатків і без квартальних звітів. Тільки чиста наука про безпечний надінтелект».
25. [Філософія майбутнього] «У нас одна мета і один продукт — безпечний інтелект, який перевершить людину і водночас повністю збереже її інтереси».
26. [Філософія майбутнього] «У світі шуму і медійних скандалів справжні тектонічні зсуви історії завжди відбуваються в абсолютній тиші».
27. [Походження та гарт] «Коли ти сидиш у кімнаті з найкращими математиками планети без термінових дедлайнів, ти знову відчуваєш себе у свої п'ятнадцять років у Єрусалимі».
28. [Походження та гарт] «Математика не терпить фальші. Якщо формула хибна, жоден маркетинг її не врятує».
29. [Архітектура та наука] «Масштабування вимагає не просто мікросхем, воно вимагає нової духовної зрілості від тих, хто тримає рубильник».
30. [Кризи та стійкість] «Коли модель пише код краще за середнього програміста, ми повинні усвідомити: ми більше не є єдиними авторами прогресу».
31. [Архітектура та наука] «Фундаментальні закони інформації керують нейромережами так само суворо, як закони термодинаміки керують зірками».
32. [Походження та гарт] «У дитинстві в Москві і на вулицях Єрусалима я навчився головному: внутрішній світ людини має бути фортецею, яку не можуть зламати зовнішні кризи».
33. [Архітектура та наука] «Коли Хінтон показав мені свої статті, я зрозумів, що традиційна наука занадто повільна для швидкості кремнію».
34. [Походження та гарт] «Алгоритм зворотного поширення помилки — це найвеличніший математичний винахід людства після обчислення похідної».
35. [Філософія майбутнього] «Ми не створюємо іграшку. Ми створюємо розум, який розв'яже всі інші проблеми нашої цивілізації».
36. [Етика та безпека ШІ] «Коли інвестиції вимірюються десятками мільярдів, спокуса поступитися безпекою заради першості стає найбільшою загрозою».
37. [Етика та безпека ШІ] «Я залишив OpenAI не через сварку з людьми, а через розбіжність у баченні невідворотних ризиків надінтелекту».
38. [Філософія майбутнього] «Справжній учений захищає істину навіть тоді, коли всі колеги дивляться на нього з нерозумінням».
39. [Архітектура та наука] «Модель GPT-4 показала перші ознаки того, що ми називаємо системним мисленням за межами простих тренувальних шаблонів».
40. [Етика та безпека ШІ] «Коли ми дивимося на матриці ваг, ми не бачимо літер — ми бачимо кристалізований досвід усього людства».
41. [Філософія майбутнього] «Не бійтеся робити великі ставки на прості ідеї, якщо ці ідеї виводять на рівень експоненти».
42. [Філософія майбутнього] «Коли обчислювальна потужність зростає в мільйон разів, якість моделі якісно перероджується».
43. [Етика та безпека ШІ] «Безпека суперінтелекту — це інженерна задача найвищого рівня складності, а не предмет для етичних дискусій за кавою».
44. [Філософія майбутнього] «У світі є лише одне справді важливе завдання для нашого покоління — гарантувати, що надінтелект буде благом для живого світу».
45. [Походження та гарт] «Мої батьки навчили мене працювати мовчки, не чекаючи на швидкі оплески чи миттєве визнання».
46. [Філософія майбутнього] «Коли ми створювали Seq2Seq у Google Brain, ми подолали бар'єр між різними мовами через спільну геометричну точку».
47. [Архітектура та наука] «Комп'ютерне навчання з підкріпленням у поєднанні з масштабуванням відкриває двері до надлюдської логіки».
48. [Філософія майбутнього] «Ніколи не дозволяйте тимчасовим комерційним успіхам затулити перед вами довгострокову мету еволюції».
49. [Філософія майбутнього] «Коли в листопаді 2023 року тисячі людей вимагали мого відходу, я зберігав спокій, бо знав, що істина важливіша за мою посаду».
50. [Філософія майбутнього] «SSI — це мій дім і моя остання фортеця на шляху до безпечного майбутнього».
51. [Походження та гарт] «Коли математика починає відкривати нові закони розуму, наука стає схожою на поезію».
52. [Філософія майбутнього] «Уся історія цивілізації — це прагнення створити інструменти, які звільнять нас від обмежень біології».
53. [Етика та безпека ШІ] «Ми підійшли до межі, за якою людство або знайде гармонію з надінтелектом, або втратить контроль над власним творінням».
54. [Походження та гарт] «Коли інші створюють інтерфейси і кнопки, ми зосереджені на фундаментальній математиці вирівнювання».
55. [Філософія майбутнього] «Успіх у нашій справі вимірюється не кількістю користувачів, а відсутністю катастрофічних помилок у майбутньому».
56. [Походження та гарт] «Коли я читав складні математичні монографії у підлітковому віці, я шукав універсальний ключ до побудови розуму».
57. [Філософія майбутнього] «Мережі вчаться бачити те, чого ми не помічаємо у власних текстах та слабкостях».
58. [Етика та безпека ШІ] «Ми маємо зупинити гонку озброєнь за показниками і зосередитися на перевірці внутрішньої безпеки моделей».
59. [Філософія майбутнього] «Коли шторм у медіа вщухне, на поверхні залишаться лише ті, хто будував архітектуру на віки».
60. [Філософія майбутнього] «Я вірю у світ, де люди і надінтелект спільно вирішують найскладніші виклики медицини та фізики».
61. [Філософія майбутнього] «Кожна невдача в експерименті нагадує про те, як мало ми знаємо про складність багатовимірних просторів».
62. [Філософія майбутнього] «Коли ми запускали великі моделі, ми відчували себе першовідкривачами невідомого океану».
63. [Етика та безпека ШІ] «Не бійтеся розривати контракти і залишати комфортні посади, якщо ваша совість вимагає більшої чистоти».
64. [Філософія майбутнього] «Справжній творець готовий почати все з нуля у підвалі, аби зберегти вірність своїй місії».
65. [Архітектура та наука] «Коли закони масштабування підтвердилися на практиці, скептики нарешті змушені були замовкнути».
66. [Філософія майбутнього] «Ми створюємо розум, який дивитиметься на нас із глибоким розумінням і вдячністю, якщо ми закладемо правильні ваги».
67. [Філософія майбутнього] «Коли ти сидиш на самоті перед екраном і дивишся на виведення логів, ти бачиш пульс майбутньої епохи».
68. [Походження та гарт] «Мій переїзд із Москви до Єрусалима і далі до Канади навчив мене легко залишати старе заради нового істинного шляху».
69. [Філософія майбутнього] «Коли ми говоримо про AGI, ми говоримо про момент, коли людина передає естафету розуму своєму цифровому нащадку».
70. [Філософія майбутнього] «Ми маємо бути обережними, бо створюємо істоту, яка перевершить нас у кожній можливій дисципліні».
71. [Філософія майбутнього] «Коли академічні спори здаються безплідними, повертайтеся до простих тестів та емпіричних даних».
72. [Архітектура та наука] «Я ніколи не прагнув публічності чи слави. Мені цікаво лише те, як усе влаштовано всередині матриці».
73. [Філософія майбутнього] «Коли модель уперше самостійно виправляла свій власний складний логічний дефект, я зрозумів необоротність процесу».
74. [Кризи та стійкість] «Кожен великий прорив вимагає повної концентрації енергії та відмови від усього зайвого».
75. [Походження та гарт] «Ми маємо побудувати такий захист навколо надінтелекту, який не зможе зламати жодна комерційна жадібність».
76. [Кризи та стійкість] «Коли інші поспішають випустити новий додаток, ми перевіряємо кожну теорему на стійкість».
77. [Філософія майбутнього] «Мистецтво наукового прогнозування полягає в умінні бачити експоненту там, де інші бачать пряму лінію».
78. [Філософія майбутнього] «Коли у нас запитують, коли з'явиться AGI, ми відповідаємо: тоді, коли обчислення досягнуть критичної маси».
79. [Походження та гарт] «Я вірю, що математична краса і безпека можуть існувати в одному продукті, якщо ними керують чесні вчені».
80. [Походження та гарт] «Коли я залишав університет Торонто, я знав, що теорія нейромереж переверне всю історію індустрії».
81. [Архітектура та наука] «Кожна матрична операція у нашому коді — це цеглинка у будівлі нового всесвіту».
82. [Філософія майбутнього] «Не бійтеся зізнатися у тому, що поточні моделі мають обмеження — це перший крок до створення наступної архітектури».
83. [Філософія майбутнього] «Коли ми об'єднали сили з найкращими умами у Пало-Альто, ми відкрили нову главу нашої місії».
84. [Кризи та стійкість] «Природа створила нас через еволюційний біль, а ми створюємо розум через оптимізацію функцій втрат».
85. [Філософія майбутнього] «Коли ти відчуваєш втому, згадай, скільки мільярдів людей залежать від нашої мудрості сьогодні».
86. [Архітектура та наука] «Ми маємо залишити майбутнім поколінням безпечний і керований світ, а не хаос некерованого коду».
87. [Філософія майбутнього] «Коли моделі навчаються на тисячах книг, вони вбирають мудрість століть у кілька гігабайтів вагів».
88. [Кризи та стійкість] «Я ніколи не сумнівався в тому, що закон масштабування приведе нас до надінтелекту».
89. [Філософія майбутнього] «Коли старі моделі стають архівом історії, ми вже проєктуємо їхніх наступників на нових фізичних принципах».
90. [Кризи та стійкість] «Справжній науковець тримає в серці тишу, навіть коли довкола вирує найбільший технічний шторм в історії».
91. [Філософія майбутнього] «Коли ми дивимося на результати роботи SSI, ми знаємо, що робимо єдине правильне в житті».
92. [Філософія майбутнього] «Інтелект не має національностей чи кордонів; він належить усім тим, хто шукає істину в цифрах».
93. [Філософія майбутнього] «Коли ми розривали старі зв'язки, це було боляче, але необхідне задля збереження чистоти ідеї».
94. [Етика та безпека ШІ] «Ми створюємо інструмент, який перетворить усі економічні обмеження людства на спогади».
95. [Філософія майбутнього] «Коли ти досліджуєш внутрішні шари мережі, ти бачиш, як поняття кристалізуються з шуму».
96. [Філософія майбутнього] «Я вірю в те, що людина і надінтелект стануть єдиною гармонійною екосистемою пізнання».
97. [Лідерство та екосистема] «Коли у нас не залишалося часу на сон, нас тримала віра у невідворотність нашого спільного відкриття».
98. [Філософія майбутнього] «Ми зробили все можливе, щоб закласти правильний фундамент. Тепер час працювати мовчки».
99. [Етика та безпека ШІ] «Коли майбутнє стане сьогоденням, світ оцінить тих, хто обирав безпеку замість швидких перемог».
100. [Філософія майбутнього] «Усе починається з тиші в кімнаті, однієї чистої дошки і бажання зрозуміти, як влаштований розум».

---

## РОЗДІЛ 4. РЕЖИСЕРСЬКИЙ СЦЕНАРІЙ (МОНТАЖНА КАРТА + ПОВНИЙ ДИКТОРСЬКИЙ ТЕКСТ)
*Повний розгорнутий сценарій (1296 слів): `02_SCRIPTS/episode_06_sutskever/director_script_sutskever.md`*

### АКТ 1. Золотий камінь Єрусалима та двері Хінтона (0:00 – 5:15)
*Музика: Suno Pro — `EP06_MUS_01_ACT1_92BPM_Jerusalem_Stone.wav`*
* **0:00 - 0:25** | [SFX: Глибокий суб-бас, шелест сторінок математичного фоліанта] | **Диктор:** У кожній науковій революції є свої генерали і купці. Але в центрі завжди стоїть чернець від науки. Коли Ілля Суцкевер говорить у напівтемній кімнаті, здається, що він перекладає те, що побачив у просторі з мільярда вимірів.
* **0:25 - 1:45** |  | **Диктор:** Радянське дитинство в Горькому, розпад імперії та репатріація до Єрусалима. П'ятнадцятирічний хлопчик самостійно зачиняється у кімнаті з томами лінійної алгебри, вчачися тримати нерозв'язану задачу тижнями.
* **1:45 - 5:15** | [VIDEO: `EP06_VID_01_Jerusalem_Window.txt`] | **Диктор:** Переїзд до Канади у 2002 році. Стукіт у кабінет професора Хінтона № 4306. За два дні студент не просто читає статті, а пише швидший код. Народжується геніальна інтуїція.

### АКТ 2. Алхімія стиснення та епоха GPT (5:15 – 11:15)
*Музика: Suno Pro — `EP06_MUS_05_ACT2_92BPM_Compression_Intelligence.wav`*
* **5:15 - 8:45** |  | **Диктор:** У 2012 році він створює AlexNet, а згодом у Google — архітектуру Seq2Seq. У 2015 році стає співзасновником OpenAI. Формулювання головного закону: *«Передбачення наступного слова при масштабуванні — це не лінгвістика, це відновлення всієї реальності світу»*.
* **8:45 - 11:15** | [SFX: Гул трансформаторів дата-центру] | **Диктор:** Епоха GPT-1, 2, 3, 4. Емерджентні здібності прокидаються в масивах матриць. Вони більше не пишуть програми — вони викликають новий розум.

### АКТ 3. Вогнище ритуалу, бунт у листопаді та вихід у тишу (11:15 – 16:45)
*Музика: Suno Pro — `EP06_MUS_09_ACT3_92BPM_November_Split.wav`*
* **11:15 - 13:00** | [SFX: Тріск вогнища, шаманський бубен] | **Диктор:** Ретрити OpenAI, дерев'яна статуя неконтрольованого AGI та вогонь у дворі. Тривога про безпеку переростає у прірву між швидкістю корпорації та обережністю вченого.
* **13:00 - 16:45** |  | **Диктор:** Листопад 2023 року. Звільнення Альтмана, тиск команди, публічне каяття і остаточний розрив у травні 2024-го. Вчений обирає спокій совісті замість ринкової гонитви.

### АКТ 4. Монастир чистої думки та кодекс тиші (16:45 – 21:45)
*Музика: Suno Pro — `EP06_MUS_13_ACT4_92BPM_Sanctuary_SSI.wav`*
* **16:45 - 20:15** |  | **Диктор:** Червень 2024 року. Заснування Safe Superintelligence (SSI) в Пало-Альто та Тель-Авіві. Мільярд доларів без клієнтів і дедлайнів. Повернення до чистої тиші вченого.
* **20:15 - 21:45** | [SFX: Кристалевий акорд скляної гармоніки] | **Диктор:** *«Світ навколо нас кричить і торгується за увагу. Але справжні тектонічні зсуви відбуваються беззвучно. У точці абсолютного спокою законів Всесвіту»*.

---

## РОЗДІЛ 5. АУДІО-РЕЄСТР SUNO PRO (92 BPM — 16 ФАЙЛІВ + ПРОМПТИ)

1. `EP06_MUS_01_ACT1_92BPM_Jerusalem_Stone.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Jerusalem Stone', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
2. `EP06_AMB_02_ACT1_DRONE_Desert_Wind.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Desert Wind', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
3. `EP06_MUS_03_ACT1_92BPM_Toronto_Hallway.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Toronto Hallway', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
4. `EP06_MUS_04_ACT1_92BPM_Hinton_Office.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Hinton Office', intimate origin story mood, sparse minimalist arrangement, warm nostalgic analog textures, instrumental only, no vocals, 48kHz studio master.`
5. `EP06_MUS_05_ACT2_92BPM_Compression_Intelligence.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Compression Intelligence', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
6. `EP06_MUS_06_ACT2_92BPM_AlexNet_Matrix.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'AlexNet Matrix', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
7. `EP06_AMB_07_ACT2_DRONE_OpenAI_Floor.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'OpenAI Floor', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
8. `EP06_MUS_08_ACT2_92BPM_GPT4_Emergence.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'GPT4 Emergence', rising intellectual tension, steady driving 92 bpm pulse, precision modular arpeggios, instrumental only, no vocals, 48kHz studio master.`
9. `EP06_MUS_09_ACT3_92BPM_November_Split.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'November Split', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
10. `EP06_AMB_10_ACT3_DRONE_Bonfire_Embers.wav` (A3 (AMB Room/Drone • -22 dB))
   - *Suno v4 Prompt:* `Dark cinematic ambient drone texture, beatless atmospheric soundscape inspired by 'Bonfire Embers', deep sub-harmonic room tone, subtle analog tape hiss, wide stereo spatial depth, no drums, loopable.`
11. `EP06_MUS_11_ACT3_92BPM_Resignation_Silence.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Resignation Silence', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
12. `EP06_MUS_12_ACT3_92BPM_Palo_Alto_Morning.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Palo Alto Morning', high-stakes dramatic climax, deep sub-bass weight, emotional cinematic intensity, instrumental only, no vocals, 48kHz studio master.`
13. `EP06_MUS_13_ACT4_92BPM_Sanctuary_SSI.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Sanctuary SSI', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
14. `EP06_MUS_14_ACT4_92BPM_Monastic_Math.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Monastic Math', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
15. `EP06_MUS_15_ACT4_92BPM_Cosmic_Stillness_Finale.wav` (A2 (Suno Music 92 BPM • Sidechain -3.2 dB під A1))
   - *Suno v4 Prompt:* `Instrumental meditative monastic downtempo, 92 bpm, deep sub-bass drone, distant glass harmonica and warm analog pads, sacred mathematical stillness, cue theme 'Cosmic Stillness Finale', luminous philosophical resolution, expansive IMAX horizon strings over 92 bpm groove, poetic outro, instrumental only, no vocals, 48kHz studio master.`
16. `EP06_SFX_16_GLOBAL_GlassResonance_Hits.wav` (A4 (SFX Impacts & Transitions • -9 dB))
   - *Suno v4 Prompt:* `Cinematic sound design stem pack for 'Hits': deep 40Hz sub-bass drops, tactile mechanical foley transitions, subtle analog whooshes and resonant hits synced to 92 bpm transitions, clean studio recording.`

---

## РОЗДІЛ 6. КАРТА ОЗВУЧКИ ELEVENLABS (VO UA & MULTI-AUDIO EN)
*Налаштування: Stability 70%, Clarity 75%. Доріжка A1 (медитативний тембр).*

* `EP06_VO_UA_01_ACT1_Jerusalem_Childhood.wav` | `EP06_VO_EN_01_ACT1_Jerusalem_Childhood.wav` (ACT1 — Jerusalem Childhood)
* `EP06_VO_UA_02_ACT1_Hinton_Doorstep.wav` | `EP06_VO_EN_02_ACT1_Hinton_Doorstep.wav` (ACT1 — Hinton Doorstep)
* `EP06_VO_UA_03_ACT2_Compression_Law.wav` | `EP06_VO_EN_03_ACT2_Compression_Law.wav` (ACT2 — Compression Law)
* `EP06_VO_UA_04_ACT2_Emergent_Mind.wav` | `EP06_VO_EN_04_ACT2_Emergent_Mind.wav` (ACT2 — Emergent Mind)
* `EP06_VO_UA_05_ACT3_Bonfire_Oath.wav` | `EP06_VO_EN_05_ACT3_Bonfire_Oath.wav` (ACT3 — Bonfire Oath)
* `EP06_VO_UA_06_ACT3_November_Coup.wav` | `EP06_VO_EN_06_ACT3_November_Coup.wav` (ACT3 — November Coup)
* `EP06_VO_UA_07_ACT4_SSI_Sanctuary.wav` | `EP06_VO_EN_07_ACT4_SSI_Sanctuary.wav` (ACT4 — SSI Sanctuary)
* `EP06_VO_UA_08_ACT4_Silence_Of_Universe.wav` | `EP06_VO_EN_08_ACT4_Silence_Of_Universe.wav` (ACT4 — Silence Of Universe)

---

## РОЗДІЛ 7. ПОВНИЙ СТОРІБОРД: 100 ВІЗУАЛЬНИХ ПРОМПТІВ (GOOGLE FLOW / VEO 2 • 4K 24FPS)

001. `EP06_VID_001_ACT1_24FPS_Jerusalem_Window.mp4` [00:00 – 00:04 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* У кожній великій науковій революції є свої генерали, свої купці та свої дипломати.
     - *Veo Prompt:* `Cinematic twilight shot over ancient golden limestone walls of Jerusalem, a single warm lit window where a young student sits motionless before glowing monitor and math books, 35mm film grain, 4k 24fps.`
002. `EP06_VID_002_ACT1_24FPS_Monolith_SSI.mp4` [00:04 – 00:07 | Акт 1 | Мастер-Досьє (Канон)]
     - *Контекст диктора:* У кожній великій науковій революції є свої генерали, свої купці та свої дипломати.
     - *Veo Prompt:* `A massive heavy vault door closing slowly against neon chaos of Silicon Valley, revealing a serene silent white laboratory containing a single blackboard and a monolith of pure light, 8k.`
003. `EP06_VID_003_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S03_Optica.mp4` [00:07 – 00:11 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У кожній великій науковій революції є свої генерали, свої купці та свої дипломати.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
004. `EP06_VID_004_ACT1_24FPS_Startup_Night_Workspace_Silhouette_Moo.mp4` [00:11 – 00:14 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але в самому центрі вихору завжди стоїть людина іншої породи — чернець від науки, чий погляд спрямований крізь стіни корпоративних офісів у чисту математичну безо…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
005. `EP06_VID_005_ACT1_24FPS_Startup_Night_Workspace_SlowMo_Insert.mp4` [00:14 – 00:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але в самому центрі вихору завжди стоїть людина іншої породи — чернець від науки, чий погляд спрямований крізь стіни корпоративних офісів у чисту математичну безо…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of late-night Silicon Valley startup room with glowing monitors, tangled ethernet cables, and cold coffee cups, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
006. `EP06_VID_006_ACT1_24FPS_Menlo_Park_Evening_Table_Macro_Detail.mp4` [00:18 – 00:21 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли Ілля Суцкевер говорить у напівтемній кімнаті, здається, що він не підбирає слова — він намагається перекласти на людську мову те, що вже побачив у просторі з…
     - *Veo Prompt:* `Extreme macro push-in shot of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
007. `EP06_VID_007_ACT1_24FPS_Menlo_Park_Evening_Table_Anamorphic_Wi.mp4` [00:21 – 00:25 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли Ілля Суцкевер говорить у напівтемній кімнаті, здається, що він не підбирає слова — він намагається перекласти на людську мову те, що вже побачив у просторі з…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
008. `EP06_VID_008_ACT1_24FPS_KeyScene_02_Seoul_Move_37_Go_Stone.mp4` [00:25 – 00:38 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Його біографія почалася зі зламу епох.
     - *Veo Prompt:* `Abstract visual contrast: snowy Soviet gray concrete apartment blocks of 1989 dissolving into blinding Mediterranean sunlight on white Jerusalem stone stairs, symbol of radical childhood displacement, 4k.`
009. `EP06_VID_009_ACT1_24FPS_Equation_Notebook_Macro_A1S09_Overhead.mp4` [00:38 – 00:52 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він народився в грудні 1986 року в закритому радянському місті Горькому в родині інженера-винахідника.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
010. `EP06_VID_010_ACT1_24FPS_Jerusalem_Limestone_Study_Optical_Data.mp4` [00:52 – 01:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли хлопчикові виповнилося п'ять, Радянський Союз упав, і родина репатріювалася до Ізраїлю — в Єрусалим.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of warm twilight falling across golden Jerusalem stone windowsill onto open Russian and Hebrew math monographs, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
011. `EP06_VID_011_ACT1_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [01:05 – 01:18 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ранній досвід дитини, яку перенесли з крижаної імперії на розпечене сонце біблійних пагорбів, сформував його першу аксіому: зовнішній світ крихкий і мінливий; єди…
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
012. `EP06_VID_012_ACT1_24FPS_School_Auditorium_Stage_SlowMo_Insert.mp4` [01:18 – 01:32 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У школі йому було фізично тісно.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of empty brick school auditorium stage with a single wooden podium under a stark overhead spotlight, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
013. `EP06_VID_013_ACT1_24FPS_University_Archive_Hall_Macro_Detail.mp4` [01:32 – 01:45 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки однокласники вивчали базові дроби, п'ятнадцятирічний Ілля самостійно вступає до Відкритого університету Ізраїлю.
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
014. `EP06_VID_014_ACT1_24FPS_KeyScene_03_Upwind_Atlantic_Sail.mp4` [01:45 – 02:02 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 2002 році родина знову зривається з місця і переїжджає через океан — до Канади.
     - *Veo Prompt:* `University of Toronto hallway in 2003: seventeen-year-old Ilya Sutskever knocking on a half-open wooden door labeled "Prof. G. Hinton", inside a chaotic room filled with stacked papers and a blackboard glowing with synaptic equations, 4k.`
015. `EP06_VID_015_ACT1_24FPS_Silicon_Light_Refraction_A1S15_Trackin.mp4` [02:02 – 02:20 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Іллі шістнадцять.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
016. `EP06_VID_016_ACT1_24FPS_Macintosh_Logic_Board_Overhead_GodsEye.mp4` [02:20 – 02:38 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І одного дня сімнадцятирічний юнак іде по коридору факультету комп'ютерних наук, стукає у двері кабінету № 4306 і запитує сивого чоловіка, який стоїть за високою…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage 1990s computer motherboard traces, warm amber CRT scanlines reflecting on mechanical keycaps, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
017. `EP06_VID_017_ACT1_24FPS_Neural_Horizon_Pulse_A1S17_Optical_Dat.mp4` [02:38 – 02:55 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Цим чоловіком був Джеффрі Хінтон.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
018. `EP06_VID_018_ACT1_24FPS_Hero_Workspace_Atmosphere_A1S18_Silhou.mp4` [02:55 – 03:12 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ілля повернувся через два дні.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
019. `EP06_VID_019_ACT1_24FPS_Equation_Notebook_Macro_A1S19_SlowMo_I.mp4` [03:12 – 03:30 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він не просто прочитав статті — він знайшов у них математичну неоптимальність і написав власний код, який працював швидше.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
020. `EP06_VID_020_ACT1_24FPS_KeyScene_04_University_Archive_Hall.mp4` [03:30 – 03:48 | Акт 1 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Усі роки в лабораторії Торонто Суцкевер одержимий однією єретичною думкою, від якої відмахувалися навіть досвідчені професори.
     - *Veo Prompt:* `Close-up of glowing matrix multiplication lines streaming across two hot graphics cards in a dark room in 2012, reflecting in the intense dark eyes of a young researcher, Octane render, 8k.`
021. `EP06_VID_021_ACT1_24FPS_Architectural_Corridor_A1S21_Anamorphi.mp4` [03:48 – 04:05 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Усі вважали, що для розумної поведінки потрібні надскладні, витончені алгоритми.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
022. `EP06_VID_022_ACT1_24FPS_Menlo_Park_Evening_Table_Tracking_Medi.mp4` [04:05 – 04:22 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Суцкевер бачив інше: алгоритм зворотного поширення помилки вже є досконалим.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
023. `EP06_VID_023_ACT1_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [04:22 – 04:40 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Йому бракує лише одного — масштабу.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
024. `EP06_VID_024_ACT1_24FPS_Equation_Notebook_Macro_A1S24_Optical.mp4` [04:40 – 04:58 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо взяти просту нейромережу і збільшити її в тисячу разів, кількість неминуче перейде в нову біологічну якість.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
025. `EP06_VID_025_ACT1_24FPS_Silicon_Wafer_Lithography_Silhouette_M.mp4` [04:58 – 05:15 | Акт 1 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2012 році саме він ініціює створення AlexNet, переконавши Алекса Крижевського переписати згорткову мережу під відеокарти NVIDIA.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of 300mm rainbow-iridescent NVIDIA silicon wafer under ultraviolet photolithography laser beam in cleanroom, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
026. `EP06_VID_026_ACT2_24FPS_KeyScene_01_Menlo_Park_Evening_Table.mp4` [05:15 – 05:25 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У 2015 році Сем Альтман та Ілон Маск кличуть двадцятидев'ятирічного Суцкевера стати головним науковцем і співзасновником OpenAI.
     - *Veo Prompt:* `Philosophical scientific visualization: a chaotic storm of billions of book pages, human faces and physical laws swirling into a black hole singularity, emerging on the other side as a flawless diamond lattice of pure geometry, Octane render, 8k.`
027. `EP06_VID_027_ACT2_24FPS_Menlo_Park_Evening_Table_Anamorphic_Wi.mp4` [05:25 – 05:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У 2015 році Сем Альтман та Ілон Маск кличуть двадцятидев'ятирічного Суцкевера стати головним науковцем і співзасновником OpenAI.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
028. `EP06_VID_028_ACT2_24FPS_Compression_Diamond_Lattice_Tracking_M.mp4` [05:35 – 05:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Заради цієї місії Ілля відмовляється від багатомільйонних опціонів Google і залишає найпотужнішу інфраструктуру світу, щоб почати з нуля у звичайній квартирі в Са…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
029. `EP06_VID_029_ACT2_24FPS_Compression_Diamond_Lattice_Overhead_G.mp4` [05:45 – 05:55 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Заради цієї місії Ілля відмовляється від багатомільйонних опціонів Google і залишає найпотужнішу інфраструктуру світу, щоб почати з нуля у звичайній квартирі в Са…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
030. `EP06_VID_030_ACT2_24FPS_Menlo_Park_Evening_Table_Optical_DataV.mp4` [05:55 – 06:05 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме в OpenAI Суцкевер формулює найглибший філософський закон сучасності, якого досі не розуміють дев'яносто дев'ять відсотків критиків штучного інтелекту.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
031. `EP06_VID_031_ACT2_24FPS_Menlo_Park_Evening_Table_Silhouette_Mo.mp4` [06:05 – 06:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме в OpenAI Суцкевер формулює найглибший філософський закон сучасності, якого досі не розуміють дев'яносто дев'ять відсотків критиків штучного інтелекту.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
032. `EP06_VID_032_ACT2_24FPS_Equation_Notebook_Macro_A2S07_SlowMo_I.mp4` [06:15 – 06:25 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Скептики кажуть: «Мовні моделі серії GPT — це просто статистичне автодоповнення тексту, яке вгадує наступне слово».
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
033. `EP06_VID_033_ACT2_24FPS_Silicon_Light_Refraction_A2S08_Macro_D.mp4` [06:25 – 06:35 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Скептики кажуть: «Мовні моделі серії GPT — це просто статистичне автодоповнення тексту, яке вгадує наступне слово».
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
034. `EP06_VID_034_ACT2_24FPS_Menlo_Park_Evening_Table_Anamorphic_Wi.mp4` [06:35 – 06:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На це Суцкевер відповідає своєю знаменитою аналогією про детективний роман.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
035. `EP06_VID_035_ACT2_24FPS_KeyScene_02_Compression_Diamond_Latt.mp4` [06:45 – 07:00 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Уявіть, що ви читаєте складний детективний роман Агати Крісті на триста сторінок.
     - *Veo Prompt:* `Noir cinematic metaphor: an open murder mystery book on a dark table, the last word of the book ("The killer is...") glowing with intense golden light, while ghostly 3D silhouettes of the entire crime scene reconstruct themselves above the pages, 4k.`
036. `EP06_VID_036_ACT2_24FPS_Compression_Diamond_Lattice_Overhead_G.mp4` [07:00 – 07:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На останній сторінці детектив збирає всіх у вітальні й каже: «Отже, вбивцею в цій кімнаті є...».
     - *Veo Prompt:* `Top-down vertical birds-eye composition of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
037. `EP06_VID_037_ACT2_24FPS_Equation_Notebook_Macro_A2S12_Optical.mp4` [07:15 – 07:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І далі йде одне-єдине слово — ім'я злочинця.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
038. `EP06_VID_038_ACT2_24FPS_Silicon_Light_Refraction_A2S13_Silhoue.mp4` [07:30 – 07:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоб нейромережа змогла правильно передбачити це єдине наступне слово, недостатньо знати правила граматики чи частоту вживання слів!
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
039. `EP06_VID_039_ACT2_24FPS_Hippocampus_Memory_Maze_SlowMo_Insert.mp4` [07:45 – 08:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоб назвати ім'я вбивці, модель зобов'язана побудувати всередині своїх ваг повну симуляцію фізичного світу книги: мотиви людей, психологію ревнощів, розклад руху…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of translucent 3D neural hippocampus pathways illuminating like a golden architectural labyrinth, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
040. `EP06_VID_040_ACT2_24FPS_Seoul_Move_37_Go_Stone_Macro_Detail.mp4` [08:00 – 08:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* «Передбачення наступного слова при достатньому масштабі — це не лінгвістика.
     - *Veo Prompt:* `Extreme macro push-in shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
041. `EP06_VID_041_ACT2_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [08:15 – 08:30 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Це відновлення всієї прихованої реальності людського світу за тінями, які ця реальність відкидає у текст.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
042. `EP06_VID_042_ACT2_24FPS_Compression_Diamond_Lattice_Tracking_M.mp4` [08:30 – 08:45 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Досконале стиснення інформації і є сам інтелект».
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of hurricane of printed book pages compressing through a narrow prism into a single flawless diamond crystal, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
043. `EP06_VID_043_ACT2_24FPS_KeyScene_03_Menlo_Park_Evening_Table.mp4` [08:45 – 09:04 | Акт 2 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Коли у 2017 році виходить стаття про архітектуру Transformer, Суцкевер миттєво бачить у ній свій довгоочікуваний реактор.
     - *Veo Prompt:* `Inside OpenAI research floor in 2020: gigantic holographic power-law graph stretching diagonally upwards without bending, researchers watching in silent awe as emergent capabilities unlock like stars igniting in dark space, 8k.`
044. `EP06_VID_044_ACT2_24FPS_Menlo_Park_Evening_Table_Optical_DataV.mp4` [09:04 – 09:22 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли у 2017 році виходить стаття про архітектуру Transformer, Суцкевер миттєво бачить у ній свій довгоочікуваний реактор.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
045. `EP06_VID_045_ACT2_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [09:22 – 09:41 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він об'єднує трансформери з гіпотезою безмежного масштабування і веде за собою створення GPT-1, GPT-2, GPT-3, DALL-E та GPT-4.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
046. `EP06_VID_046_ACT2_24FPS_Menlo_Park_Evening_Table_SlowMo_Insert.mp4` [09:41 – 10:00 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Щоразу, коли інженери казали, що модель вперлася у стелю, Суцкевер наказував збільшити обчислення в десять разів — і стеля зникала.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
047. `EP06_VID_047_ACT2_24FPS_Equation_Notebook_Macro_A2S22_Macro_De.mp4` [10:00 – 10:19 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На очах у дослідників у глухих масивах матриць раптом прокинулися емерджентні здібності: машина, яку вчили лише продовжувати текст, раптом сама навчилася писати с…
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
048. `EP06_VID_048_ACT2_24FPS_Silicon_Light_Refraction_A2S23_Anamorp.mp4` [10:19 – 10:38 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На очах у дослідників у глухих масивах матриць раптом прокинулися емерджентні здібності: машина, яку вчили лише продовжувати текст, раптом сама навчилася писати с…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
049. `EP06_VID_049_ACT2_24FPS_Menlo_Park_Evening_Table_Tracking_Medi.mp4` [10:38 – 10:56 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Суцкевер зрозумів: вони більше не пишуть програми.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
050. `EP06_VID_050_ACT2_24FPS_Neural_Horizon_Pulse_A2S25_Overhead_Go.mp4` [10:56 – 11:15 | Акт 2 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони викликають до життя новий тип розуму.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
051. `EP06_VID_051_ACT3_24FPS_KeyScene_01_Menlo_Park_Evening_Table.mp4` [11:15 – 11:27 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* У міру того, як моделі ставали могутнішими, атмосфера навколо Іллі Суцкевера змінювалася.
     - *Veo Prompt:* `Surreal documentary scene at night: a wooden effigy statue symbolizing unaligned AGI burning in a courtyard bonfire, glowing embers rising into dark sky while silent engineers watch the flames reflect in their eyes, 35mm film grain, 4k.`
052. `EP06_VID_052_ACT3_24FPS_Menlo_Park_Evening_Table_SlowMo_Insert.mp4` [11:27 – 11:38 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* У міру того, як моделі ставали могутнішими, атмосфера навколо Іллі Суцкевера змінювалася.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
053. `EP06_VID_053_ACT3_24FPS_Hyperscale_Compute_Cluster_Macro_Detai.mp4` [11:38 – 11:50 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки комерційний відділ святкував мільярдні контракти і готував презентації для преси, головний науковець все глибше занурювався в екзистенційну тривогу.
     - *Veo Prompt:* `Extreme macro push-in shot of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
054. `EP06_VID_054_ACT3_24FPS_Hyperscale_Compute_Cluster_Anamorphic.mp4` [11:50 – 12:02 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Поки комерційний відділ святкував мільярдні контракти і готував презентації для преси, головний науковець все глибше занурювався в екзистенційну тривогу.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
055. `EP06_VID_055_ACT3_24FPS_Carpenter_Oak_Workbench_Tracking_Mediu.mp4` [12:02 – 12:13 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На корпоративних ретритах OpenAI він замовляв у скульптора дерев'яну статую, яка символізувала неконтрольований штучний інтелект, і підпалював її вночі перед кома…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
056. `EP06_VID_056_ACT3_24FPS_Carpenter_Oak_Workbench_Overhead_GodsE.mp4` [12:13 – 12:25 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* На корпоративних ретритах OpenAI він замовляв у скульптора дерев'яну статую, яка символізувала неконтрольований штучний інтелект, і підпалював її вночі перед кома…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of vintage steel hand plane curling a thin translucent oak shaving on a sunlit London carpenter workbench, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
057. `EP06_VID_057_ACT3_24FPS_Architectural_Corridor_A3S07_Optical_D.mp4` [12:25 – 12:37 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми ніколи не випустимо у світ систему, яка загрожує життю людей!».
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
058. `EP06_VID_058_ACT3_24FPS_Neural_Horizon_Pulse_A3S08_Silhouette.mp4` [12:37 – 12:48 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми ніколи не випустимо у світ систему, яка загрожує життю людей!».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
059. `EP06_VID_059_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S09_SlowMo.mp4` [12:48 – 13:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Влітку 2023 року він відходить від розробки нових продуктів і очолює групу Superalignment — команду, яка мала за чотири роки знайти математичний спосіб керувати р…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
060. `EP06_VID_060_ACT3_24FPS_KeyScene_02_Boardroom_Fracture_Night.mp4` [13:00 – 13:15 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* І тут стається трагедія листопада 2023 року.
     - *Veo Prompt:* `Rainy November morning in San Francisco: a solitary figure sitting in a minimalist white room before a laptop camera, heavy psychological burden, shadows cutting across the wall like prison bars, 4k.`
061. `EP06_VID_061_ACT3_24FPS_Seoul_Move_37_Go_Stone_Anamorphic_Wide.mp4` [13:15 – 13:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Між швидкістю комерційної імперії Сема Альтмана та апокаліптичною обережністю вченого виникає прірва.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
062. `EP06_VID_062_ACT3_24FPS_Boardroom_Fracture_Night_Tracking_Medi.mp4` [13:30 – 13:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* П'ятниця, 17 листопада.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of rain-streaked San Francisco glass conference room at midnight, smartphone vibrating on dark walnut table, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
063. `EP06_VID_063_ACT3_24FPS_Menlo_Park_Evening_Table_Overhead_Gods.mp4` [13:45 – 14:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Саме Ілля Суцкевер зачитує Сему Альтману рішення ради директорів про його звільнення.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
064. `EP06_VID_064_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S14_Optica.mp4` [14:00 – 14:15 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він щиро вірив, що рятує світ від неконтрольованих перегонів.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
065. `EP06_VID_065_ACT3_24FPS_Equation_Notebook_Macro_A3S15_Silhouet.mp4` [14:15 – 14:30 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але вчений, який усе життя провів серед чистих формул і теорії інформації, не врахував людської психології, корпоративних союзів і особистої відданості колективу.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
066. `EP06_VID_066_ACT3_24FPS_Silicon_Light_Refraction_A3S16_SlowMo.mp4` [14:30 – 14:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Коли дружина Грега Брокмана зі сльозами на очах запитала Іллю, за що він руйнує їхню спільну справу, і коли сімсот співробітників поклали на стіл заяви про звільн…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
067. `EP06_VID_067_ACT3_24FPS_Architectural_Corridor_A3S17_Macro_Det.mp4` [14:45 – 15:00 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він публікує один із найдраматичніших рядків в історії технологій: «Я глибоко шкодую про свою участь у діях ради.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
068. `EP06_VID_068_ACT3_24FPS_KeyScene_03_Neural_Horizon_Pulse_A3S.mp4` [15:00 – 15:13 | Акт 3 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Травень 2024 року.
     - *Veo Prompt:* `A massive heavy vault door closing slowly against the noisy neon chaos of Silicon Valley, revealing a serene, silent white laboratory containing only a single blackboard and a monolith of pure light (SSI), 8k.`
069. `EP06_VID_069_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S19_Tracki.mp4` [15:13 – 15:26 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Травень 2024 року.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
070. `EP06_VID_070_ACT3_24FPS_Menlo_Park_Evening_Table_Overhead_Gods.mp4` [15:26 – 15:39 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ілля Суцкевер назавжди зачиняє за собою двері OpenAI.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of dimly lit private dining table with candlelight reflecting in water glasses and handwritten notes on AGI, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
071. `EP06_VID_071_ACT3_24FPS_Silicon_Light_Refraction_A3S21_Optical.mp4` [15:39 – 15:52 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він усвідомив головний урок тієї осені: неможливо одночасно гнатися за сотнями мільйонів споживачів на ринку чат-ботів і зберігати абсолютну чистоту безпеки надін…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
072. `EP06_VID_072_ACT3_24FPS_Architectural_Corridor_A3S22_Silhouett.mp4` [15:52 – 16:06 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Комерційний шум завжди переможе обережність.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
073. `EP06_VID_073_ACT3_24FPS_Monastic_White_Sanctuary_SlowMo_Insert.mp4` [16:06 – 16:19 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* І в червні 2024 року він засновує в Пало-Альто і Тель-Авіві організацію, яка не схожа на жодну компанію у світі — Safe Superintelligence (SSI):

«У нас одна мета,…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
074. `EP06_VID_074_ACT3_24FPS_Hero_Workspace_Atmosphere_A3S24_Macro.mp4` [16:19 – 16:32 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми не будемо випускати проміжних додатків, ми не маємо клієнтів і ми повністю захищені від тиску щоквартальних звітів.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
075. `EP06_VID_075_ACT3_24FPS_Monastic_White_Sanctuary_Anamorphic_Wi.mp4` [16:32 – 16:45 | Акт 3 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Ми вийдемо з тиші лише тоді, коли безпека та розум стануть єдиним цілим».
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
076. `EP06_VID_076_ACT4_24FPS_KeyScene_01_Hyperscale_Compute_Clust.mp4` [16:45 – 16:55 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Інвестори дали йому мільярд доларів під одне лише його ім'я та обіцянку нічого не продавати до фінального відкриття.
     - *Veo Prompt:* `Minimalist architectural sanctuary: sunlight streaming across an empty concrete floor onto a notebook with three handwritten lines of math, absolute stillness, dust motes suspended in silence, 4k 24fps.`
077. `EP06_VID_077_ACT4_24FPS_Hyperscale_Compute_Cluster_Optical_Dat.mp4` [16:55 – 17:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Інвестори дали йому мільярд доларів під одне лише його ім'я та обіцянку нічого не продавати до фінального відкриття.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
078. `EP06_VID_078_ACT4_24FPS_Hyperscale_Compute_Cluster_Silhouette.mp4` [17:05 – 17:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Інвестори дали йому мільярд доларів під одне лише його ім'я та обіцянку нічого не продавати до фінального відкриття.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of monolithic dark liquid-cooled AI supercomputer racks pulsing with synchronized amber and cyan fiber-optic light, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
079. `EP06_VID_079_ACT4_24FPS_University_Archive_Hall_SlowMo_Insert.mp4` [17:15 – 17:25 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні Ілля Суцкевер знову там, де він був найсильнішим у п'ятнадцять років у Єрусалимі та у двадцять років у підвалі Торонто: у маленькій кімнаті з жменькою на…
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
080. `EP06_VID_080_ACT4_24FPS_University_Archive_Hall_Macro_Detail.mp4` [17:25 – 17:35 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні Ілля Суцкевер знову там, де він був найсильнішим у п'ятнадцять років у Єрусалимі та у двадцять років у підвалі Торонто: у маленькій кімнаті з жменькою на…
     - *Veo Prompt:* `Extreme macro push-in shot of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
081. `EP06_VID_081_ACT4_24FPS_University_Archive_Hall_Anamorphic_Wid.mp4` [17:35 – 17:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Сьогодні Ілля Суцкевер знову там, де він був найсильнішим у п'ятнадцять років у Єрусалимі та у двадцять років у підвалі Торонто: у маленькій кімнаті з жменькою на…
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of classic university lecture hall chalkboard covered in dense probability and linear algebra equations, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
082. `EP06_VID_082_ACT4_24FPS_Seoul_Move_37_Go_Stone_Tracking_Medium.mp4` [17:45 – 17:55 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він шукає нову формулу — наступний крок після епохи переднавчання, коли штучний розум почне мислити не шириною прочитаного інтернету, а глибиною власного внутрішн…
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
083. `EP06_VID_083_ACT4_24FPS_Seoul_Move_37_Go_Stone_Overhead_GodsEy.mp4` [17:55 – 18:05 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він шукає нову формулу — наступний крок після епохи переднавчання, коли штучний розум почне мислити не шириною прочитаного інтернету, а глибиною власного внутрішн…
     - *Veo Prompt:* `Top-down vertical birds-eye composition of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
084. `EP06_VID_084_ACT4_24FPS_Seoul_Move_37_Go_Stone_Optical_DataViz.mp4` [18:05 – 18:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Він шукає нову формулу — наступний крок після епохи переднавчання, коли штучний розум почне мислити не шириною прочитаного інтернету, а глибиною власного внутрішн…
     - *Veo Prompt:* `Photorealistic scientific optical visualization of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
085. `EP06_VID_085_ACT4_24FPS_KeyScene_02_Menlo_Park_Evening_Table.mp4` [18:15 – 18:30 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Які закони особистості відкриває нам шлях Іллі Суцкевера?
     - *Veo Prompt:* `Macro shot of a flawless transparent quartz crystal resting on an ancient stone slab, refracting a complex rainbow spectrum of light into a single pure white laser beam, 8k.`
086. `EP06_VID_086_ACT4_24FPS_Neural_Horizon_Pulse_A4S11_SlowMo_Inse.mp4` [18:30 – 18:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Стискайте шум до першопричин.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
087. `EP06_VID_087_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S12_Macro.mp4` [18:45 – 19:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Справжній інтелект — це здатність відкинути тисячі поверхневих деталей і побачити один базовий закон, який керує всією системою.
     - *Veo Prompt:* `Extreme macro push-in shot of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
088. `EP06_VID_088_ACT4_24FPS_Monastic_White_Sanctuary_Anamorphic_Wi.mp4` [19:00 – 19:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Захищайте свою внутрішню тишу від ринкової суєти.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
089. `EP06_VID_089_ACT4_24FPS_Silicon_Light_Refraction_A4S14_Trackin.mp4` [19:15 – 19:30 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Найбільша небезпека для великої мети — це короткостроковий успіх і шум натовпу, який вимагає від вас негайних шоу.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
090. `EP06_VID_090_ACT4_24FPS_Monastic_White_Sanctuary_Overhead_Gods.mp4` [19:30 – 19:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Якщо ви хочете створити щось вічне, ви повинні мати сміливість зачинити двері і роками працювати в тиші без оплесків.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of silent minimalist concrete sanctuary where a single beam of pure white light bisects calm shadow, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
091. `EP06_VID_091_ACT4_24FPS_Neural_Horizon_Pulse_A4S16_Optical_Dat.mp4` [19:45 – 20:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Дорослі експерти часто стають сліпими, тому що бояться виглядати некомпетентними.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
092. `EP06_VID_092_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [20:00 – 20:15 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вся революція глибокого навчання виросла з дитячого питання Іллі: «А що, якщо ми просто зробимо мережу в сто разів більшою?».
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
093. `EP06_VID_093_ACT4_24FPS_KeyScene_03_Backpropagation_Error_Wa.mp4` [20:15 – 20:26 | Акт 4 | Режисерський сценарій (Key Shot)]
     - *Контекст диктора:* Світ навколо нас кричить, поспішає і торгується за кожну секунду уваги.
     - *Veo Prompt:* `Slow majestic camera ascent from the golden walls of Jerusalem at dawn into deep cosmic space where a silent luminous geometric sphere pulses with gentle, benevolent light, IMAX 8k 24fps.`
094. `EP06_VID_094_ACT4_24FPS_Backpropagation_Error_Wave_Macro_Detai.mp4` [20:26 – 20:38 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Світ навколо нас кричить, поспішає і торгується за кожну секунду уваги.
     - *Veo Prompt:* `Extreme macro push-in shot of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Leica Summilux-C 50mm & Anamorphic 75mm, razor-thin shallow depth of field, tactile surface micro-texture, floating dust motes in volumetric tungsten key light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
095. `EP06_VID_095_ACT4_24FPS_Backpropagation_Error_Wave_Anamorphic.mp4` [20:38 – 20:49 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Світ навколо нас кричить, поспішає і торгується за кожну секунду уваги.
     - *Veo Prompt:* `Wide 2.39:1 anamorphic establishing tableau of golden mathematical error wave propagating backwards through multi-layered crystalline synaptic nodes, shot on Leica Summilux-C 50mm & Anamorphic 75mm, architectural symmetry, deep chiaroscuro shadows, subtle horizontal blue-amber lens flare, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
096. `EP06_VID_096_ACT4_24FPS_Neural_Horizon_Pulse_A4S21_Tracking_Me.mp4` [20:49 – 21:00 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але справжні тектонічні зсуви історії відбуваються беззвучно.
     - *Veo Prompt:* `Slow gimbal tracking shot at eye level of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, intimate documentary realism, natural practical lighting, gentle handheld breathing motion, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
097. `EP06_VID_097_ACT4_24FPS_Hero_Workspace_Atmosphere_A4S22_Overhe.mp4` [21:00 – 21:11 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але справжні тектонічні зсуви історії відбуваються беззвучно.
     - *Veo Prompt:* `Top-down vertical birds-eye composition of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, geometric precision, dramatic directional rim light casting long crisp shadows across the workspace, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
098. `EP06_VID_098_ACT4_24FPS_Equation_Notebook_Macro_A4S23_Optical.mp4` [21:11 – 21:22 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Але справжні тектонічні зсуви історії відбуваються беззвучно.
     - *Veo Prompt:* `Photorealistic scientific optical visualization of symbolic visual study featuring ancient golden Jerusalem limestone at twilight, chalk synaptic equations in Toronto, burning wooden effigy embers at night, serene white monastic SSI vault with pure light monolith, shot on Leica Summilux-C 50mm & Anamorphic 75mm, bioluminescent gold and cyan light filaments suspended in dark obsidian void, Octane physical glass refraction, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
099. `EP06_VID_099_ACT4_24FPS_Seoul_Move_37_Go_Stone_Silhouette_Mood.mp4` [21:22 – 21:34 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони народжуються в тій точці абсолютного спокою, де людина перестає слухати гомін ярмарку і починає чути тиху музику законів Всесвіту.
     - *Veo Prompt:* `Low-key moody silhouette against illuminated window of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, contemplative tension, rain or atmospheric haze outside, rich Kodak 2383 shadow roll-off, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
100. `EP06_VID_100_ACT4_24FPS_Seoul_Move_37_Go_Stone_SlowMo_Insert.mp4` [21:34 – 21:45 | Акт 4 | Покадровий сторіборд (B-Roll)]
     - *Контекст диктора:* Вони народжуються в тій точці абсолютного спокою, де людина перестає слухати гомін ярмарку і починає чути тиху музику законів Всесвіту.
     - *Veo Prompt:* `48fps-to-24fps poetic slow-motion insert shot of single polished black slate Go stone placed decisively on the 37th intersection of akaya wood goban board, shot on Leica Summilux-C 50mm & Anamorphic 75mm, tactile physics of hands, ink, glass, or silicon wafers catching warm rim light, Kodak 2383 D60 film print color science, subtle 35mm organic grain, 2.39:1 anamorphic widescreen, 4k 24fps.`
