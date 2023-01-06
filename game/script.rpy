init python:
    import time

# Определение персонажей игры.
define oleg = Character('Олег', color = "#8280ff")
define oleg_thoughts = Character('Олег', color = "#2a28be")
define boss = Character('Иван Михайлович', color = "#beffbe")
define clown = Character('Толя', color = "#befff1")
define rat = Character('Сергей', color = "#befff1")
define worker = Character('Геннадий', color = "#befff1")
define active = Character('Екатерина', color = "#befff1")
define shelb = Character('shelby', color = "#befff1")
define snop = Character('snop', color = "#befff1")

# "Гифки"
image bossx:
    "boss.png"
    0.5
    "boss_rot.png"
    0.5
    repeat
image clownx:
    "clown.png"
    0.5
    "clown_rot.png"
    0.5
    repeat
image ratx:
    "rat.png"
    0.5
    "rat_rot.png"
    0.5
    repeat
image rat_angryx:
    "rat_angry.png"
    0.5
    "rat_angry_rot.png"
    0.5
    repeat
image activex:
    "active.png"
    0.5
    "active_rot.png"
    0.5
    repeat
image workerx:
    "worker.png"
    0.5
    "worker_rot.png"
    0.5
    repeat

# Игра начинается здесь:
label start:

    # Очки отношений
    $ active_points = 0
    $ rat_points = 0
    $ worker_points = 0
    stop music
    play music chinese
    show text "{size=+20}Fire Balls Presents{/size}" with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve
    $ renpy.pause(0.5)
    show text '{size=+20}"Детективные изыскания Олега Евгеньевича"{/size}' with dissolve
    $ renpy.pause(3.0)
    stop music
    hide text with fade
    $ renpy.pause(1.0)
    play music pechat
    centered "Вы ведущий специалист информационной безопасности в крупной фирме, специализирующейся на перевозке грузов. Сегодня к вам обратилось руководство с поручением выявить виновного в утечке важных данных."
    centered "Вас, под видом обычного сотрудника, внедряют в отдел, где работает подозреваемый. Вы должны, полагаясь на дедуктивный метод, выявить причастного к сливу данных."
    centered "От вас зависит дальнейшая судьба всей компании. Приступайте к расследованию."
    stop music
    play sound pechatdate
    centered "{size=+20}{color=#00ff00}Барнаул, Алтайский край{/size}{/color}"

    jump first_day

label first_day:

    ###
    # DAY 1
    ###

    ### Boss office scene
    play sound pechatdate
    centered "{size=+20}{color=#00ff00} 11 сентября 2002 года, 8:00{/size}{/color}"

    play music fon
    scene boss_office with fade

    show boss at center with dissolve
    show bossx

    boss "Доброе утро, Олег Евгеньевич."
    boss "Меня зовут Иван Михайлович, и я являюсь руководителем этого отдела. Полагаю, Вас уже примерно ввели в курс дела?"
    hide bossx

    oleg "Здравствуйте, Иван Михайлович. Да, меня посвятили в происходящее."
    oleg "Однако перед тем, как приступить к работе, мне хотелось бы узнать побольше об этом месте и работающих здесь людях."

    show bossx
    boss "Да, конечно. Данный отдел занимается логистикой. Как Вы понимаете, информация, к которой есть доступ у моих сотрудников, крайне важна для компании."
    boss "Именно поэтому Вам необходимо найти виновного в утечке в ближайшее время."
    boss "Всего в этом отделе работает 4 человека, у которых есть доступ к слитой информации. Думаю, стоит описать Вам каждого из них."
    hide bossx

    show boss at left with move

    show bossx at left
    show clown at right with dissolve
    boss "Первым в списке подозреваемых находится Анатолий. Довольно весёлый и жизнерадостный человек, лёгок в общении."
    hide bossx
    hide clown

    show bossx at left
    show rat at right with dissolve
    boss "Вторым подозреваемым является Сергей. Имеет весьма неприятный характер, честно говоря."
    boss "Пытается выслужиться любыми возможными способами передо мной, часто жалуется на своих коллег."
    hide bossx
    hide rat

    show bossx at left
    show worker at right with dissolve
    boss "Третьим будет Геннадий. Пожалуй, лучший работник в этом отделе. Крайне продуктивен и трудолюбив."
    hide bossx
    hide worker

    show bossx at left
    show active at right with dissolve
    boss "Далее по списку у нас Екатерина. Её можно назвать самым энергичным и социально активным сотрудником."
    boss "Она ответственна за большинство мероприятий по тимбилдингу. Именно благодаря ей, коллектив у нас, за некоторым исключением, довольно дружный."
    hide bossx
    hide active

    show boss at center with move

    show bossx at center
    boss "Что же, вроде рассказал Вам, Олег Евгеньевич, всё, что знал."
    boss "Я руковожу этим отделом не так давно, и поэтому не настолько хорошо знаю своих людей, чтобы делать какие-то выводы самому."
    boss "Но всё же, если будут какие-то вопросы, - обращайтесь."
    boss "Прошу также держать меня в курсе событий."
    boss "Однако не стоит бегать ко мне по каждому поводу, иначе Вы вызовете подозрения. Просто заходите ко мне время от времени, чтобы доложить обстановку"
    boss "И не забывайте, Олег Евгеньевич: Вас направили сюда, потому что Вы отлично зарекомендовали себя ранее, и высшее руководство рассчитывает на Вас."
    boss "От Вас зависит не только Ваша собственная репутация, но и репутация всей компании. Если вы выдадите себя, второй попытки уже не будет."
    boss "Поэтому я искренне желаю Вам удачи."
    hide bossx

    oleg "Понял, спасибо за наводки, Иван Михайлович. Я понимаю, что время поджимает, поэтому приступлю к работе немедленно."

    show bossx
    boss "Отлично. Тогда вот Вам мой последний совет на сегодня: осмотрите весь отдел, чтобы уметь ориентироваться здесь, и познакомьтесь с каждым из подозреваемых лично."
    hide bossx

    oleg "Вас понял, до свидания."

    scene black_screen with fade
    oleg_thoughts "(По всей видимости, это самое серьезное дело, за которое я брался)"
    oleg_thoughts "(Нужно не ударить в грязь лицом)"

    ### clown Scene
    play sound pechatdate
    centered "{color=#00ff00} 11 сентября 2002 года, 8:30{/color}"

    scene office with fade

    oleg_thoughts "(Ладно, теперь надо осмотреться здесь. Пойду поищу свое рабочее мес...)"

    with vpunch
    with hpunch
    show clown with dissolve

    show clownx
    clown "Ох-ох, ну и больно! , дружище!"
    clown "Тут всё-таки логистический отдел, люди занятые работают. Не чета разгильдяем из главного управления!"
    hide clownx

    oleg "Прошу прощения, призадумался тут немного."

    show clownx
    clown "Ничего, бывает. Ты, похоже, тот самый новый сотрудник, о котором нам недавно говорили."
    clown "Приятно познакомиться, меня Толей звать!"
    hide clownx

    oleg "Взаимно, Меня Олег зовут. Cегодня мой первый день. Вот, Иван Михайлович проводил мне инструктаж."

    show clownx
    clown "Иван Михайлович любит толкать речи. Он тот ещё оратор, этого у него не отнять."
    clown "Ладно, осваивайся тут потихоньку, а я пойду кофе себе сделаю."
    hide clownx

    oleg "Любишь кофе?"

    show clownx
    clown "А кто не любит? Я вообще целый день могу на одном только кофе прожить."
    clown "Ну я пошёл. Ещё увидимся!"
    hide clownx

    hide clown with dissolve

    oleg_thoughts "(Похоже, это был мой первый подозреваемый. И вправду, весьма позитивный человек)"

    ### rat scene

    oleg_thoughts "(Хорошо, вот и первое знакомство. Теперь уже точно мне нужн...)"

    "???" 'Только познакомились, а он уже на "ты". Какое непрофессиональное поведение. Впрочем, как обычно...'

    oleg_thoughts "(Ну кто на этот раз?)"

    show rat at center with moveinright

    show ratx
    rat "Моё имя Сергей, будем знакомы."
    rat "К сожалению, большинство сотрудников здесь придерживаются подобного неформального стиля общения."
    rat "Как по мне, это пагубно влияет на рабочую атмосферу, Вы не согласны?"
    hide ratx

    menu:
        "Полностью согласен":
            oleg "Да, конечно, это крайне непрофессионально, я полностью с Вами согласен."
            show ratx
            rat "Рад это слышать."
            rat "В этом месте наблюдается критическая нехватка адекватных работников."
            rat "Надеюсь, с Вашим приходом, здесь начнутся перемены."
            hide ratx
            oleg "Не переживайте, я не подведу."
            show ratx
            rat "Тогда нам нужно будет как-нибудь обсудить нашу стратегию по повышению профессиональных качеств наших коллег."
            hide ratx
            oleg_thoughts "(Только не это...)"
            show ratx
            rat "Хорошо, не буду больше задерживать, у Вас сегодня много дел."
            rat "До встречи."
            hide ratx
            hide rat
            $ rat_points += 1
        "Не согласен":
            oleg "На самом деле, я не думаю, что это как-то может навредить работе."
            hide rat
            show rat_angry
            rat "..."
            $ renpy.pause(0.5)
            show rat_angryx
            rat "Вы меня несколько разочаровали."
            rat "Смею напомнить: платить Вам будут не за пустую болтовню."
            rat "Очень жаль. Я думал, что с Вашим приходом, здесь начнутся перемены."
            hide rat_angryx
            hide rat_angry
            $ rat_points -= 1

    oleg_thoughts "(Отлично. Первый день, и я уже успел с кем-то поссориться)"

    ### worker scene
    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00} 11 сентября 2002 года, 12:00{/color}"

    scene office2 with fade
    show worker at center with fade

    show workerx
    worker "Да уж, ну и денек сегодня..."
    worker "О, ты тот новенький! Кажется, тебя зовут Олег, да?"
    hide workerx
    oleg "Да, приветствую, Геннадий, начальник мне о тебе рассказывал как о самом старательном сотруднике."
    show workerx
    worker "Ой, да пустяки, я всего то отвечаю за разработку всего корпоративного софта в отделе."
    hide workerx
    menu:
        oleg_thoughts "(Хм, а вот это уже становится интересно)"

        "Разузнать поподробнее о его работе":
            oleg "А что конкретно ты разрабатываешь сейчас?"
            show workerx
            worker "А, да ничего серьезного, думаю над расширением функциональности программы по составлению и расчёту маршрутов."
            hide workerx

        "Спросить его об успехах":
            oleg "Как успехи?"
            show workerx
            worker "Да вот, понемногу дорабатываю свою программу, вот только пока ничего толкового не выходит."
            worker "Эх, как же надоела эта работа, а ещё и платят мало..."
            hide workerx
            $ worker_points += 1

        "Промолчать":
            oleg "..."
            worker "..."

    "Кофемашина" "*бип - бип*"
    show workerx
    worker "Ой, у меня там кофе уже приготовился, надо бы поторопиться, пока не остыл."
    worker "Приятно было пообщаться, до встречи, Олег."
    hide workerx
    oleg "Хорошего дня."
    hide worker with dissolve
    oleg_thoughts "(По нему видно, что ему приходится нелегко. На нем лежит немало ответственности)"

    ### active scene
    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00} 11 сентября 2002 года, 16:00{/color}"

    scene office2 with fade

    oleg_thoughts "(Так, ладно, пора за работу)"

    with vpunch
    with hpunch

    oleg_thoughts "(Стоп, а что мне, собственно говоря, надо делать?)"
    oleg_thoughts "(Кажется, Иван Михайлович забыл сказать, какое именно у меня прикрытие...)"
    oleg_thoughts "(Ладно, надо что-нибудь придумать. Не болтать же мне целый день с коллегами)"

    show active with dissolve
    show activex
    active "Привет! Извини, что отвлекаю от работы."
    active "Меня зовут Катя, я менеджер-логист."
    active "Ты, как я понимаю, наш новый программист, да?"
    hide activex

    menu:
        "Именно":
            oleg_thoughts "(Отлично, вот и узнал, кем я работаю)"
            oleg "Да, это я. Сегодня мой первый день."
            show activex
            active "Так и знала! Нам недавно сообщили о том, что к нашей команде присоединится новый человек."
            active "Жаль, я опоздала немного на работу."
            active "Мы собирались все вместе встретить тебя и отметить пополнение коллектива в столовой!"
            active "Но ты, наверно, уже со всеми успел познакомиться, так что смысла в собрании уже нет."
            hide activex
        "Программист?":
            oleg "Программист? Ты сейчас про кого это?"
            active "..."
            show activex
            active "Ха-ха, ну ты и шутник!"
            active "Если бы ты не был новым программистом, тебя бы просто не пустили сюда."
            active "Кажется, у Толи появился соперник за звание лучшего юмориста отдела логистики!"
            hide activex
            $ active_points += 1

    show activex
    active "Думаю, в скором времени мы точно проведем какое-нибудь мероприятие по укреплению дружественных связей между коллегами."
    hide activex
    oleg_thoughts "(Отличная возможность узнать всех подозреваемых поближе)"
    show activex
    active "Осталось только придумать, что же это будет..."
    active "Ладно, не буду отвлекать тебя. Пока!"
    hide activex

    stop music

    ### home scene
    scene black_screen with fade

    play sound pechatdate
    centered "{color=#00ff00}11 сентября 2002 года, 21:00{/color}"

    scene home with fade

    oleg_thoughts "(Да уж, это был безумный день, но надо двигаться дальше)"
    oleg_thoughts "(Завтра предстоит поставить свою систему безопасности на все компьютеры в офисе, чтобы выявить информатора)"
    oleg_thoughts "(А сейчас стоит немного отдохнуть...)"

    jump second_day

label second_day:

    ###
    # DAY 2
    ###

    ### comp scene 1

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}12 сентября 2002 года, 8:30{/color}"

    play music fon

    scene office2 with fade
    oleg_thoughts "(Так, вот я и в офисе. Сейчас нужно быстро внедрить свою программу на компьютеры всех подозреваемых до того, как они придут на работу)"
    oleg_thoughts "(Начну с рабочих мест Екатерины и Геннадия)"

    scene black_screen with fade
    play sound comp
    "Компьютер" "*звук включения*"
    "Компьютер" "..."
    "Компьютер" "..."
    "Компьютер" "Программа успешно установлена"

    play music fon

    scene office2 with fade
    oleg_thoughts "(Всё, готово, теперь нужно установить программу на компьютеры Анатолия и Сергея)"

    ### comp scene 2

    scene office with fade

    oleg_thoughts "(Время на исходе, скоро начнется рабочий день)"

    with fade

    oleg_thoughts "(Так, остался всего один компьютер...)"

    with vpunch
    with hpunch

    show rat with dissolve
    show ratx
    rat "Что здесь происходит?"
    hide rat
    hide ratx
    show rat_angry with dissolve
    show rat_angryx
    rat "Что Вы делаете на моем рабочем месте? И кто дал Вам право пользоваться моим компьютером?"
    hide rat_angryx
    if rat_points == 1:

        oleg "Иван Михайлович попросил меня проверить работоспособность всех компьютеров в офисе,"
        oleg "Чтобы, в случае поломки чего-либо, запросить новое оборудование."
        hide rat_angry
        show rat with dissolve
        show ratx
        rat "Хм, ладно, теперь понятно. Что ж, продолжайте проверку, не буду отвлекать."
        hide ratx
        $ rat_points += 1
        hide rat
        oleg_thoughts "(Вот это конечно пронесло)"
        oleg_thoughts "(Ещё немного, и он, кажется, устроил бы скандал)"
        oleg_thoughts "(Надо постараться не конфликтовать с подозреваемыми, пока я не буду уверен в чьей-либо вине)"
        "Компьютер" "Программа успешно установлена"

    else:
        oleg "..."
        show rat_angryx
        rat "Отвечайте!"
        hide rat_angryx
        menu:
            "Антивирус":
                oleg "Эм, да я вот проверял просто тут это, ну, антивирус в общем..."
                rat "..."
                show rat_angryx
                rat "Убирайтесь прочь."
                hide rat_angryx
                oleg_thoughts "(Надо успеть поставить программу)"
                "Компьютер" "..."
                show rat_angryx
                rat "Вы издеваетесь?"
                hide rat_angryx
                "Компьютер" "Программа успешно установлена"
                oleg_thoughts "(Всё!)"
                oleg "Уже ухожу."
            "Не то место":
                oleg "Разве это не мой компьютер?"
                oleg "Прошу прощения, я всё ещё плохо ориентируюсь здесь."
                hide rat_angry
                show rat with dissolve
                show ratx
                rat "Ваш компьютер находится в другой части офиса."
                rat "Я, конечно, понимаю, что Вам здесь всё в новинку, но я надеюсь, подобное больше не повториться."
                hide ratx
                $ rat_points += 1
                oleg "Да конечно."
                oleg_thoughts "(Ну давай, грузись быстрее!)"
                "Компьютер" "Программа успешно установлена"
                oleg "До встречи."

    hide rat
    hide rat_angry

    ### conversation scene

    scene black_screen with fade

    play sound pechatdate
    centered "{color=#00ff00}12 сентября 2002 года, 14:00{/color}"
    stop music

    show office2 with fade

    show active at right with dissolve
    show activex at right
    active "Наш коллектив нуждается в этом!"
    hide activex

    show worker at left with dissolve
    show workerx at left
    worker "У нас нет времени на эту чушь!"
    hide workerx

    oleg "Всем здрасьте, что тут происходит?"
    show workerx at left
    worker "Она опять лезет ко всем со своими идиотскими идеями!"
    hide workerx
    show activex at right
    active "Никакие они не идиотские!"
    hide activex
    oleg "Что у вас произошло?"
    show activex at right
    active "Я предлагаю всем вместе поехать на природу в эти выходные."
    active "Мы пообщаемся, узнаем друг друга получше. Короче говоря, укрепим дружеские связи и повысим моральный дух в команде!"
    hide activex
    oleg "Звучит не так плохо."
    show workerx at left
    worker "Ага, только у нас тут завал, ведь кое-кто, вместо того, чтобы работать, рассуждает о каких-то дружеских связях и морали."
    worker "Мой дух был бы на высоте, еслы бы мне не приходилось задерживаться и доделывать чью-то работу."
    hide workerx
    show activex at right
    active "Олег, посмотри на все эти унылые лица! Разве им не нужно немного развеяться?"
    hide activex
    menu:
        "Это пойдет на пользу":
            oleg "Не вижу ничего плохого в этом мероприятии."
            show activex at right
            active "Вот так вот, двое против одного!"
            hide activex
            $ active_points += 1
            show workerx at left
            worker "Помимо нас тут работает ещё куча людей. Их спросить не забыла?"
            hide workerx
            show activex at right
            active "Ой, точно. Пойду поговорю с остальными."
            hide activex
            hide active with moveoutleft
            show workerx at left
            worker "Ну и слава Богу, наконец-то можно спокойно поработать."
            hide workerx

        "Работа важнее":
            oleg "Мне кажется, стоит сначала разобраться с работой, прежде чем задумываться о какой-то сторонней деятельности."
            show workerx at left
            worker "Дело говоришь."
            hide workerx
            show activex at right
            active "Да это ведь только на пользу пойдет всему коллективу!"
            hide activex
            show workerx at left
            worker "Тебе уже два человека сказали, что это чушь. Сделай дело - гуляй смело."
            hide workerx
            show activex at right
            active "Понятно с вами всё!"
            hide activex
            hide active with moveoutleft
            $ worker_points += 1

    oleg_thoughts "(Да уж, не самая приятная беседа получилась)"
    oleg_thoughts '(Ну, всякое бывает. Пожалуй, стоит пойти "поработать", чтобы ни у кого не было вопросов ко мне)'
    hide worker
    ### home scene
    scene black_screen with fade

    play sound pechatdate
    centered "{color=#00ff00}12 сентября 2002 года, 22:00{/color}"
    stop music

    scene home with fade

    oleg_thoughts "(Денек, конечно, не из легких выдался)"
    oleg_thoughts "(Точно, посмотрю-ка я свою программу, может что-нибудь удастся выявить...)"
    scene black_screen with fade
    play sound comp
    "Компьютер" "*Звук включения*"
    "Компьютер" "..."
    oleg_thoughts "А вот это уже интересно, кто-то залез в корпоративную сеть компании буквально полчаса назад."
    scene home with fade
    oleg_thoughts "Черт, кто бы это мог быть?"
    oleg_thoughts "Гадание всё равно ни к чему не приведет. Нужно попросить записи с камер видеонаблюдения в офисе."

    jump third_day

label third_day:

    ###
    # DAY 3
    ###

    ### boss scene
    scene black_screen
    play sound pechatdate
    centered "{color=#00ff00}13 сентября 2002 года, 8:30{/color}"

    play music fon

    scene boss_office with fade

    show boss at center with dissolve

    show bossx
    boss "Доброе утро, Олег Евгеньевич. Я вижу, сегодня вы пришли пораньше. Вам есть что рассказать о ходе расследования?"
    hide bossx

    oleg "Здравствуйте, Иван Михайлович. Да, вчера утром я установил свою программу, которая фиксирует активность в корпоративной сети компании."
    oleg "Дело в том, что вчера поздно вечером она зафиксировала вторжение в сеть с рабочего компьютера Сергея."

    show bossx
    boss "Продолжайте."
    hide bossx

    oleg "Так вот, я считаю, стоит посмотреть записи с камер наблюдения в период с 21:20 до 21:40."

    show bossx
    boss "Хорошо. Запись будет у меня уже вечером. Однако не стоит полагаться на нашу видеокамеру."
    boss "Она у нас далеко не самого лучшего качества. Есть большая вероятность того, что лицо подозреваемого будет невозможно опознать."
    boss "Зайдите ко мне, когда все сотрудники покинут офис."
    hide bossx

    oleg "До встречи."

    hide boss

    scene black_screen with fade

    oleg_thoughts "(Похоже, запись с камеры не сильно поможет мне в расследовании)"
    oleg_thoughts "(Придется выяснить всё самому)"
    oleg_thoughts "(Нужно постараться разузнать, где находился каждый из подозреваемых вчера вечером)"

    ### какая-то сцена в офисе
    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}13 сентября 2002 года, 12:00{/color}"

    scene office with fade

    show worker at left with dissolve
    show workerx at left
    worker "... а потом оказалось, что его сына повысили до ефрейтора!"
    hide workerx

    show rat at right with dissolve
    show ratx at right
    rat "Ничего себе! Жаль, что я пропустил эту серию."
    hide ratx

    oleg_thoughts "(Интересно, что же они так бурно обсуждают?)"

    oleg "Всем доброе утро, кого это повысили до ефрейтора?"

    if worker_points >= 1:
        show workerx at left
        worker "Да мы тут обсуждаем один сериал популярный. Каждый день по новой серии выходит."
        worker "Вот, вчера была очень интересная серия, кульминация всего сериала! А Сергей её пропустил."
        hide workerx

        oleg "Похоже, сериал действительно интересный. Стоит глянуть. Не подскажешь, во сколько начинается?"

        show workerx at left
        worker "В 21:30."
        hide workerx

        oleg "Ладно, заболтался я тут. Пойду вернусь к работе, а то много дел навалилось."
    else:
        show workerx at left
        worker "Пойду-ка я отсюда, а то коллектив тут какой-то неприятный."
        hide workerx
        hide worker

        rat "..."
        show ratx at right
        rat "Без понятия, что на него нашло. Заработался вчера видимо."
        hide ratx

        oleg "Понимаю. Ну а что там по поводу сериала?"

        show ratx at right
        rat "Да мы тут обсуждали один сериал популярный. Каждый день по новой серии выходит."
        rat "Вот, вчера была очень интересная серия, кульминация всего сериала! А Сергей её пропустил."
        hide ratx

        oleg "Похоже, сериал действительно интересный. Стоит глянуть. Не подскажешь, во сколько начинается?"

        $ rat_points += 1

        show ratx at right
        rat "В 21:30."
        hide ratx

        oleg "Ладно, заболтался я тут. Пойду вернусь к работе, а то много дел навалилось."

    hide rat
    $ renpy.pause(1.0)
    rat "Кто оставил кофе на моем столе?!"

    show workerx at left
    worker "Не знаю, это не я."
    hide workerx
    hide worker

    ### ещё одна сцена в офисе
    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}13 сентября 2002 года, 14:00{/color}"

    scene office2 with fade

    oleg_thoughts '(Ладно, мне стоит приступить к "работе")'

    scene black_screen with fade
    show text "Спустя 10 минут"
    $ renpy.pause(1.0)

    scene office2 with fade

    show active at right with dissolve
    show activex at right
    active "Толя, как ты посмел! Я всё знаю!"
    hide activex

    show clown at left with dissolve
    clown "..."
    show clownx at left
    clown "Эм... Что ты имеешь в виду?"
    hide clownx

    show activex at right
    active "Мы же договаривались вчера сыграть в Counter Strike!"
    active "А ты так и не зашел!"
    hide activex

    clown "..."
    show clownx at left
    clown "А, ты про это?"
    clown "Я вчера весь вечер был тут. Разгребал деловые завалы всякие."
    hide clownx

    if active_points >= 1:
        show activex at right
        active "Олег, давай лучше с тобой сыграем в Counter Strike?"
        active "А то Толю никогда не дождешься!"
        hide activex

        oleg "Извини, не могу. Я занятой человек, мне тут ещё крота надо поймать."

        show activex at right
        active "Что? Какого ещё крота?"
        hide activex

        oleg "Да на даче у меня кротов развелось, на игры времени совсем нет."

        show activex at right
        active "А, понятно. Ну, будет желание, присоединяйся. Я обычно в 9-10 часов вечера захожу в Counter Strike."
        hide activex

        clown "..."
        oleg "Понятно. Будет свободное время - обязательно присоединюсь."
    else:
        show activex at right
        active "Ну сегодня-то ты хоть пойдешь в Counter Strike?"
        hide activex

        show clownx at left
        clown "Посмотрим. У меня сегодня тоже куча дел."
        clown "Скорее всего, я снова задержусь допоздна."
        hide clownx

        show activex at right
        active "Понятно всё с тобой. Придется искать кого-нибудь другого, с кем можно будет поиграть."
        hide activex

    scene black_screen with fade
    oleg_thoughts "(Надеюсь, сегодняшний день прошел не зря)"

    ### last scene with boss
    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}13 сентября 2002 года, 19:30{/color}"

    oleg "Это запись с камеры видеонаблюдения?"

    scene boss_office with fade

    show boss with dissolve
    show bossx
    boss "Именно. Вчера в 21:32, кто-то залез в компьютер Сергея."
    boss "Мы решили посмотреть запись с камеры, установленной в офисе, чтобы убедиться в том, что это именно он."
    boss "Однако, как Вы можете видеть, на этой записи видно только как некто подходит к его компьютеру и начинает что-то в нем делать."
    boss "Мы не можем быть на 100 процентов уверены, что это Сергей. Вчера, когда я уходил в 7 вечера, все четверо подозреваемых были в офисе."
    hide bossx
    $ renpy.pause(1.0)
    with fade
    show bossx
    boss "Расследование уже слишком затянулось, Олег Евгеньевич."
    boss "Сами понимаете, в любое время информатор может понять, что он под наблюдением, и тогда операция сорвется."
    boss "Более того, мы не может допустить ещё одну утечку данных, это принесет необратимый ущерб компании."
    boss "Поэтому больше у нас нет времени ждать, вы должны назвать мне имя человека, который, по вашему мнению, является кротом."
    boss "У вас есть время подумать до завтрашнего утра. Надеюсь, у вас достаточно собранных сведений, чтобы сделать правильный выбор."
    boss "Жду вас завтра в моем офисе в 8 утра."
    hide bossx

    hide boss with moveoutleft

    oleg_thoughts "(Да уж... От этого решения будет зависеть моя карьера в этой компании)"

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}13 сентября 2002 года, 20:30{/color}"

    scene home with fade

    oleg_thoughts "(Денек, конечно, не из легких выдался)"
    oleg_thoughts "(Завтра предстоит сделать сложный выбор)"
    oleg_thoughts "(А сейчас стоит немного отдохнуть...)"

    jump fourth_day

label fourth_day:

    ###
    # DAY 4
    ###

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}14 сентября 2002 года, 6:00{/color}"

    scene home with fade

    oleg_thoughts "(Мне так и не удалось спокойно поспать...)"
    oleg_thoughts "(Я всю ночь размышлял о том, кто же стоит за всем этим)"
    oleg_thoughts "(Всё равно заснуть не могу. Пойду на работу, что поделать)"

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}14 сентября 2002 года, 7:00{/color}"

    scene office2 with fade
    $ renpy.pause(1.0)
    scene office with fade
    $ renpy.pause(1.0)

    oleg_thoughts "(Похоже, никто ещё не пришел...)"
    oleg_thoughts "(Пожалуй, подожду Ивана Михайловича около его кабинета)"

    with vpunch
    with hpunch

    show rat with dissolve

    if rat_points >= 1:
        show ratx
        rat "Доброе утро, Олег Евгеньевич. Не ожидал увидеть Вас тут в такое раннее время."
        hide ratx

        oleg "Да вот, решил прийти пораньше."
        oleg "Что-то я сегодня вообще не выспался. Пойду приготовлю себе кофе. Тебе взять?"

        show ratx
        rat "Нет, спасибо. Я не любитель кофе. У меня аллергия на кофеин."
        hide ratx
    else:
        show ratx
        rat "Не ожидал увидеть Вас тут в такое раннее время."
        hide ratx

        oleg "Да вот, решил прийти пораньше."
        oleg "Что-то я сегодня вообще не выспался. Пойду приготовлю себе кофе. Тебе взять?"

        show ratx
        rat "Если я захочу, я сам себе могу взять кофе."
        hide ratx

    oleg "Ух ты, ничего себе. Ну, тогда я пошёл."

    hide rat with dissolve

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}14 сентября 2002 года, 8:00{/color}"

    scene boss_office with fade

    show boss with dissolve

    show bossx
    boss "Доброе утро, Олег Евгеньевич."
    boss "Вы же понимаете, что пришло время делать выбор?"
    boss "Надеюсь, Вы тщательно проанализировали все факты."
    boss "Кто из моих подчиненных является информатором?"
    hide bossx

    oleg "Все улики указывают на:"
    menu:
        "Сергея":
            oleg "Все улики указывают на Сергея!"
            jump fail
        "Анатолия":
            oleg "Все улики указывают на Анатолия!"
            jump success
        "Геннадия":
            oleg "Все улики указывают на Геннадия!"
            jump fail
        "Екатерину":
            oleg "Все улики указывают на Екатерину!"
            jump fail

label fail:
    show bossx
    boss "Я Вас понял."
    boss "Будут приняты все необходимые меры."
    boss "Надеюсь, Вы не ошиблись в своих суждениях."
    hide bossx

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}21 сентября 2002 года, 22:00{/color}"

    scene home with fade
    stop music
    "Телефон" "*бип-бип*"

    oleg_thoughts "(Неизвестный номер... Интересно, кто бы это мог быть?)"
    oleg_thoughts "(Мне обычно никто не звонит на службный телефон в такое позднее время)"

    "Абонент" "Я разговариваю с Олегом Евгеньевичем?"

    oleg "Я слушаю."

    "Абонент" "Можете приходить за своей трудовой книжкой."
    "Абонент" "Думаю, Вы уже поняли, что Вы наделали."

    oleg "..."
    oleg "Я ошибся?"

    "Абонент" "..."

    "Телефон" "*бип-бип*"

    scene black_screen with fade
    $ renpy.pause(2.0)
    jump credits

label success:
    show bossx
    boss "Я Вас понял."
    boss "Будут приняты все необходимые меры."
    boss "Надеюсь, Вы не ошиблись в своих суждениях."
    hide bossx

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}21 сентября 2002 года, 22:00{/color}"

    scene home with fade

    "Телефон" "*бип-бип*"

    oleg_thoughts "(Иван Михайлович? Зачем ему звонить мне в такое позднее время?)"

    "Иван Михайлович" "Добрый вечер, Олег Евгеньевич."

    oleg "Здравствуйте, Иван Михайлович. Как у Вас дела. Утечки данных прекратились?"

    "Иван Михайлович" "Зайдите завтра ко мне в офис. Нам с вами есть что обсудить."

    oleg "Не вопрос."

    oleg_thoughts "(Не уж что я ошибся?!)"

    scene black_screen with fade
    play sound pechatdate
    centered "{color=#00ff00}22 сентября 2002 года, 8:45{/color}"

    scene boss_office with fade

    show boss with dissolve
    show bossx
    boss "Здравствуйте, Олег Евгеньевич."
    hide bossx

    oleg "Иван Михайлович."

    boss "..."
    show bossx
    boss "Ну чего Вы такой хмурый, Олег Евгеньевич!"
    boss "Поздравляю Вас! Вы сумели вычислить информатора."
    hide bossx

    oleg_thoughts "(Сумел?..)"

    show bossx
    boss "Я, честно говоря, вообще не ожидал, что им окажется Анатолий."
    boss "Оказывается, всё это время за маской добродушного весельчака скрывался расчетливый злодей. Никогда бы не подумал на него."
    hide bossx

    $ renpy.pause(1.0)

    show bossx
    boss "Ладно, хватит о плохом. Я уже переговорил с некоторыми представителями высшего руководства."
    boss "За Ваши заслуги перед фирмой Вас в скором времени повысят!"
    boss "Примите мои поздравления!"
    hide bossx

    scene black_screen with fade
    play music chinese
    $ renpy.pause(2.0)
    jump credits

label credits:

    ###
    # CREDITS
    ###

    show text "{size=+20}Fire Balls{/size}" with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve

    show text "{size=+10}Teamlead:   Антон Ковальский\nAnalyse:  Роман Васильев\n Design:   Софья Удовенко{/size}" with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve

    show text "{size=+10}Sound design:   Иван Михайлович Металин{/size}" with dissolve
    $ renpy.pause(3.5)
    hide text with dissolve

    show text "{size=+10}Programming:   Андрей Викторович Кремлев\n                 Антон Павлович Фадеев\n                      Иван Михайлович Металин{/size}" with dissolve
    $ renpy.pause(3.5)
    hide text with dissolve

    show text "{size=+10}Script:   Антон Павлович Фадеев\n                    Андрей Викторович Кремлев{/size}" with dissolve
    $ renpy.pause(3.5)
    hide text with dissolve

    show text "{size=+10}Executive Director:   Антон Павлович Фадеев{/size}" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    show text "{size=+10}Executive Director:   Иван Михайлович Металин{/size}" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    show text "{size=+10}Executive Director:   Андрей Викторович Кремлев{/size}" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    #outro
    show radik with fade
    show shelby at left with dissolve
    show snop at right with dissolve
    shelb "La commedia..."
    snop "...e finita"

    return
