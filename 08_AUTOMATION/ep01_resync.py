#!/usr/bin/env python3
"""Синхронізація склейок EP01 (акти II–IV) з реальним мовленням у дублях озвучки.

Кожному кадру — (блок, фраза дослівно з тексту ElevenLabs). Склейка ставиться за LEAD с до першого
слова фрази (час слова — vo_align.phrase_time). Кадри без фрази (None) розподіляються пропорційно між
сусідніми прив'язаними. Титри (v3), наплави і маркери їдуть разом зі своїми кадрами.
"""
import vo_align as V
import vo_words as W

LEAD = 0.15          # с: зображення трохи випереджає слово
MIN_SHOT = 24        # кадрів: найкоротший план

CUES = {
    "Акт I": [
        None,
        (1, "Більшість людей"), (1, "оцінки в табелях"), (1, "Помилка в соціумі"),
        (2, "У 1993 році"), (2, "дістає з коробки"), (2, "Macintosh LC II"), (2, "Через тридцять років"),
        (2, "Ця машина розмила"), (2, "Вона стала продовженням"), (2, "Комп'ютер навчив його"),
        (2, "машина байдужа до авторитетів"), (2, "Вона карає не за спробу"), (2, "баг, який можна"),
        (3, "Джон Берроуз Скул"), (3, "Якщо ти вирізнявся"), (3, "У шістнадцять років"), (3, "він виходить на сцену"),
        (3, "перед християнською шкільною"), (3, "Це був перший стратегічний"), (3, "коли ти сам голосно"),
        (3, "страх розсіюється"), (3, "Автономія здобувається"),
        (4, "Далі був Стенфорд"), (4, "Лекції, семестрові цикли"), (4, "А кремнієвий світ"),
        (4, "У 2005 році, на другому"), (4, "Йому дев'ятнадцять"), (4, "він засновує Loopt"),
        (4, "мобільну соціальну мережу"),
        (5, "Саме тоді Пол Грем"), (5, "Loopt потрапляє"), (5, "Сім років Альтман"), (5, "Він спить на підлозі"),
        (5, "бореться з операторами"), (5, "У 2012 році компанію"), (5, "Для венчурного ринку"),
        (5, "Але для самого Альтмана"), (5, "школа інженерії волі"), (5, "Більшість людей здаються"),
        (6, "Він виходить із Loopt"), (6, "лінійні проекти"), (6, "Справжня сила"),
        None,
    ],
    "Акт II": [
        None,                                   # титр АКТ II
        (7, "У 2014 році"), (7, "Пол Грем передає"), (7, "Хлопцю в джинсах"), (7, "штампувати мобільні додатки"),
        (7, "розвертає штурвал"), (7, "інвестує в термоядерний синтез"), (7, "біотехнології довголіття"),
        (7, "Його логіка викликає"), (7, "Він формулює свій знаменитий"), (7, "Люди катастрофічно"),
        (8, "Він бачить сліпу зону"), (8, "Якщо компанія зростає"), (8, "Але технології обчислень"),
        (8, "Якщо потужність чіпів"), (8, "через тридцять років"), (8, "У 2015 році закрита вечеря"),
        (8, "зводить разом"), (8, "молодого вченого з Торонто"), (8, "Тема розмови"), (8, "Google щойно придбав"),
        (8, "Деміса Гассабіса"), (8, "Концентрація найпотужнішого"),
        (9, "11 грудня 2015"), (9, "Статус — некомерційна"), (9, "Бюджет — 1 мільярд"), (9, "Мета — побудова"),
        (9, "Перші три роки"), (9, "Дослідники вчили роботів"), (9, "тренували моделі грати"), (9, "Традиційна академія глузувала"),
        (9, "OpenAI — це просто піар"), (9, "Але всередині лабораторії"), (9, "Масштаб вирішує все"),
        (10, "Щоб перевірити гіпотезу"), (10, "Один цикл тренування"), (10, "за електроенергію"),
        (10, "Альтман робить хід"), (10, "він реструктуризує"), (10, "домовляється про перший"),
        (10, "Критики кричали"), (10, "Альтман відповів коротко"),
    ],
    "Акт III": [
        None,                                   # титр АКТ III
        (11, "30 листопада 2022"), (11, "Жодних прес-конференцій"), (11, "За п'ять днів"),
        (11, "Це був найшвидший"), (11, "Світ раптом прокинувся"), (11, "студенти писали"),
        (11, "програмісти генерували"), (11, "а уряди скликали"), (11, "від овальних кабінетів"),
        (11, "до слухань у Сенаті"),
        (12, "П'ятниця, 17 листопада"), (12, "Альтман підключається"), (12, "На екрані"),
        (12, "четверо членів ради"), (12, "Ілля Суцкевер, Адам"), (12, "Розмова триває"),
        (12, "Без попереджень"), (12, "його звільнено"), (12, "Прес-реліз уже"),
        (12, "За кілька хвилин новина"), (12, "Акції Microsoft"), (12, "Індустрія застигає"),
        (12, "Головного візіонера"),
        None,  # у записі UA-13 речення «Починаються… сто двадцять годин» відсутнє — годинник у паузі перед блоком
        (13, "Рада директорів була"), (13, "вони вважали, що Альтман"),
        (13, "Вони були впевнені, що співробітники"), (13, "Вони прорахувалися"), (13, "У суботу Сатья"),
        (13, "У неділю ввечері"), (13, "публікує фото"), (13, "Перший і останній"),
        (14, "Понеділок, ранок"), (14, "понад 730"), (14, "Або ви йдете"), (14, "Під листом"),
        (14, "глибоко шкодує"), (14, "У середу, 22 листопада"), (14, "Стару раду"),
        (14, "Ця криза показала"), (14, "не на посадових"), (14, "Вона трималася на спільній"),
        None,                                   # фінальний план акту
    ],
    "Акт IV": [
        None,                                   # титр АКТ IV
        (15, "Пройшовши крізь вогонь"), (15, "Він розуміє"), (15, "Інтелект став фізичним"),
        (15, "тераватів чистої енергії"), (15, "мільйонів спеціалізованих"), (15, "Звідси — проекти"),
        (15, "будівництво обчислювальних"), (15, "переговори з виробниками"), (15, "пряма ставка на ядерну"),
        (15, "Він дивиться на історію"), (15, "якщо зробити вартість"), (15, "матеріальний дефіцит"),
        (16, "Який головний урок"), (16, "1. Не бійтеся"), (16, "Світ влаштований так"),
        (16, "Якщо ви самі не зробите"), (16, "2. Дивіться на проблеми"), (16, "Люди витрачають тонни"),
        (16, "Будь-яка криза"), (16, "Знайдіть рядок"), (16, "3. Обирайте експоненту"),
        (16, "Якщо ваша щоденна"), (16, "Шукайте речі"), (16, "репутація та автономні"),
        (17, "Світ набагато пластичніший"), (17, "Його правила не викарбувані"), (17, "І цей світ піддається"),
        (17, "впертістю сидіти"), (17, "поки система нарешті"), (17, "Майбутнє не настає"),
        (17, "Його створюють"),
        None, None, None,                        # Земля, корпус Mac, фінальна картка
    ],
}


CUES_EN = {
    "Акт I": [
        None,
        (1, "Most people"), (1, "high school hallways"), (1, "In society mistakes"),
        (2, "In 1993"), (2, "unboxes his first computer"), (2, "a Macintosh LC II"), (2, "Thirty years later"),
        (2, "This machine blurred"), (2, "It became an extension"), (2, "The computer taught him"),
        (2, "a machine is indifferent"), (2, "It does not punish effort"), (2, "A bug you can isolate"),
        (3, "John Burroughs School"), (3, "If you stood out"), (3, "At sixteen"), (3, "he stepped onto the assembly stage"),
        (3, "before the entire Christian"), (3, "It was the first strategic"), (3, "when you speak your most"),
        (3, "fear evaporates"), (3, "True autonomy is seized"),
        (4, "Next came Stanford"), (4, "Syllabi semesters exams"), (4, "And the silicon world"),
        (4, "In 2005 during his sophomore"), (4, "He was nineteen"), (4, "he co founded Loopt"),
        (4, "a mobile social network"),
        (5, "Just then Paul Graham"), (5, "Loopt was selected"), (5, "For seven years"), (5, "He slept on the office floor"),
        (5, "fought tooth and nail"), (5, "In 2012 Green Dot"), (5, "In Silicon Valley terms"),
        (5, "Yet for Altman"), (5, "a crucible of willpower"), (5, "Most people do not quit"),
        (6, "He walked away from Loopt"), (6, "linear ventures"), (6, "True leverage lives"),
        None,
    ],
    "Акт II": [
        None,
        (7, "In 2014"), (7, "Paul Graham named"), (7, "A young founder in jeans"), (7, "churning out delivery apps"),
        (7, "Altman steered the juggernaut"), (7, "backed nuclear fusion"), (7, "funded cellular longevity"),
        (7, "His philosophy rattled"), (7, "He articulated his defining"), (7, "People catastrophically"),
        (8, "He identified the blind spot"), (8, "If a company grows"), (8, "But computing power"),
        (8, "If chip capacity doubles"), (8, "thirty years later"), (8, "In July 2015"),
        (8, "brought together Sam Altman"), (8, "a brilliant young scientist from Toronto"), (8, "Their agenda was existential"),
        (8, "Google had just acquired"), (8, "acquired DeepMind"), (8, "Concentrating superintelligent power"),
        (9, "On December 11"), (9, "a non profit research laboratory"), (9, "armed with one billion"), (9, "Its charter"),
        (9, "The first three years"), (9, "Researchers trained robotic hands"), (9, "pitted neural nets against"),
        (9, "Academia dismissed them"), (9, "a billionaire vanity project"), (9, "Yet inside the lab"), (9, "Scale is all you need"),
        (10, "To test the scaling laws"), (10, "A single training run"), (10, "in electricity and GPUs"),
        (10, "Altman made a move"), (10, "he restructured OpenAI"), (10, "secured an initial one billion"),
        (10, "Purists decried"), (10, "Altman's response was blunt"),
    ],
    "Акт III": [
        None,
        (11, "November 30 2022"), (11, "No press conferences"), (11, "Within five days"), (11, "It became the fastest"),
        (11, "Overnight reality shifted"), (11, "students drafted essays"), (11, "engineers architected software"),
        (11, "and governments scrambled"), (11, "moving between Oval Office"), (11, "Capitol Hill hearings"),
        (12, "Friday November 17"), (12, "Altman joins a routine"), (12, "On his screen"), (12, "four OpenAI board members"),
        (12, "Ilya Sutskever Adam"), (12, "The call lasts minutes"), (12, "Without prior warning"), (12, "Altman is dismissed"),
        (12, "The press release"), (12, "Within moments global markets"), (12, "Microsoft loses"),
        (12, "The tech industry freezes"), (12, "The architect of the AI boom"),
        (13, "Thus began"), (13, "The board believed"), (13, "convinced Altman was moving"), (13, "They assumed the research staff"),
        (13, "They misjudged"), (13, "By Saturday"), (13, "By Sunday evening"), (13, "wearing a visitor badge"), (13, "First and last time"),
        (14, "Monday morning"), (14, "more than seven hundred"), (14, "Resign and reinstate"), (14, "Among the signatures"),
        (14, "publicly expressing profound remorse"), (14, "By Wednesday"), (14, "The old board"),
        (14, "The crisis illuminated"), (14, "was not anchored"), (14, "It rested entirely"),
        None,
    ],
    "Акт IV": [
        None,
        (15, "Having survived"), (15, "He recognized a hard truth"), (15, "Intelligence has become"),
        (15, "gigawatts of clean power"), (15, "millions of silicon chips"), (15, "Hence initiatives"),
        (15, "one hundred billion dollar superclusters"), (15, "global semiconductor pacts"), (15, "massive personal bets"),
        (15, "He views civilizational progress"), (15, "if you drive the marginal cost"), (15, "material scarcity"),
        (16, "What core insights"), (16, "First Do not fear"), (16, "The world is calibrated"), (16, "If you do not bet"),
        (16, "Second Treat problems"), (16, "People waste immense"), (16, "A crisis is simply"), (16, "Find the failing line"),
        (16, "Third Choose the exponential"), (16, "If your daily work"), (16, "Dedicate your energy"),
        (16, "uncompromising reputation"),
        (17, "The world is far more malleable"), (17, "Its rules were not etched"), (17, "And reality yields"),
        (17, "possess the grit"), (17, "until the system finally breathes"), (17, "The future does not arrive"),
        (17, "It is forged right now"),
        None, None, None,
    ],
}


def cue_time(n, phrase, lang):
    try:
        t = W.word_time(n, phrase, lang)              # точно за розпізнаними словами
    except FileNotFoundError:
        t = None
    return t if t is not None else V.phrase_time(n, phrase, lang=lang, strict=True)


def resync(act, log=print, lang="UA"):
    key = act["name"].replace(" EN", "")
    cues = (CUES_EN if lang == "EN" else CUES).get(key)
    if not cues:
        return act
    v1 = act["v1"]
    assert len(cues) == len(v1), f"{act['name']}: {len(cues)} фраз на {len(v1)} планів"
    F = 24
    old = [r[0] for r in v1]
    new = list(old)
    anchored = [False] * len(v1)
    for i, c in enumerate(cues):
        if not c:
            continue
        n, phrase = c
        t = cue_time(n, phrase, lang)
        if t is None:
            log(f"  ? {act['name']} план {i}: фразу «{phrase}» не знайдено — лишаю як було")
            continue
        new[i] = act["vo"][n][1] + int(round((t - LEAD) * F))
        anchored[i] = True
    anchored[0] = True                           # перший план акту — з нуля
    new[0] = old[0]
    # кадри без фрази — пропорційно між сусідами
    idx = [i for i, a in enumerate(anchored) if a]
    for a, b in zip(idx, idx[1:]):
        for i in range(a + 1, b):
            new[i] = int(round(new[a] + (old[i] - old[a]) * (new[b] - new[a]) / max(1, old[b] - old[a])))
    last = idx[-1]
    for i in range(last + 1, len(v1)):
        new[i] = old[i] + (new[last] - old[last]) if i < len(v1) else old[i]
    # хвіст акту (Земля/корпус/картка) лишається на своїх місцях, якщо не зачепили
    for i in range(last + 1, len(v1)):
        new[i] = max(old[i], new[i - 1] + MIN_SHOT)
    # мінімальна тривалість і порядок
    for i in range(1, len(v1)):
        if new[i] < new[i - 1] + MIN_SHOT:
            new[i] = new[i - 1] + MIN_SHOT
    end = act["end_f"]
    if new[-1] > end - MIN_SHOT:
        log(f"  ! {act['name']}: останній план вийшов за межі акту — стискаю")
        new[-1] = end - MIN_SHOT
    moved = [(i, (new[i] - old[i]) / F) for i in range(len(v1)) if abs(new[i] - old[i]) > 2]
    log(f"  {act['name']}: зсунуто {len(moved)} з {len(v1)} склейок, найбільше {max((abs(m) for _, m in moved), default=0):.2f} с")
    shift = dict(zip(old, new))

    def remap(f):
        if f in shift:
            return shift[f]
        i = max([k for k in range(len(old)) if old[k] <= f], default=0)
        nxt = old[i + 1] if i + 1 < len(old) else end
        nnx = new[i + 1] if i + 1 < len(new) else end
        return min(new[i] + (f - old[i]), nnx - 1)

    act["v1"] = [(new[i],) + tuple(r[1:]) for i, r in enumerate(v1)]
    act["dissolves"] = {shift.get(c, c): h for c, h in (act.get("dissolves") or {}).items()}
    act["v3"] = [(remap(f0), n, s) for f0, n, s in act.get("v3", [])]
    act["v2"] = [(remap(f0), n, d) for f0, n, d in act.get("v2", [])]
    act["markers"] = [(f if nm.startswith("Д") else remap(f), c, nm, note) for f, c, nm, note in act.get("markers", [])]
    act["resync"] = moved
    return act
