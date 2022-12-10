define e = Character('Сергиц', color="#15c3e6")
define r = Character('Работодательница', color="#FF8484")
define adm = Character('admin', color="#FF0000")
define zav = Character('Заведующий', color="#F17171")
define rdm = Character('Незнакомец', color="#949292")
define vd = Character('Ведущий', color="#6A3232")
define vdall = Character('Ведущие', color="#6A3232")

#ГЛАВА: КАДРОВЫЙ ОТДЕЛ

label start:
    jump dom
    return


label otdel:

    scene offi

    show sir_normal:
        xalign 0.8

    show misskadr:
        xalign 0.3 yalign 1.1 xzoom -1

    e "Здравствуйте, я хочу работать промоутером"
    
    r "Назовите ваше имя"
    menu:
        "Выберите ваше имя"

        "Сергей Балокин":
            r "Это не ваше настоящее имя."
            "Сергица выгнали из банка и он отправился домой.."
            jump donecard

        "Сергиц":
            r "Сколько вам лет?"
            jump goda

        "Иди нахер":
            "Сергица выгнали из банка и он отправился домой.."
            jump donecard





    return

label goda:
    menu:
        "Выберите ваш возвраст"

        "16 лет":
            r "Отлично, теперь назовите номер своей карты, куда вам будет поступать З/П в размере 500р за один рабочий день"
            jump card
        "13 лет":
            r "Ты слишком мал!"
        "Я передумал!":
            jump donecard

    return

label card:
    menu:
        "Назовите номер своей карты"

        "4130 2561 7890 1025":
            r "Так, секунду...{w=2}А почему карта показывается как сбер кидс?"
            jump poyasn
        "Я передумал!":
            jump donecard
            #возвращается на home
    return
label poyasn:
    show sir_shock:
        xalign 0.8
    menu:
        "Объясните ситуцию сотруднице банка"

        "Я не знаю!":
            r "Просьба отвечать честно!"
            jump otdel
        "Это карта моего брата, хочу сделать ему сюрприз":
            hide sir_shock
            r "Что-ж, хорошо. Вот ваши листовки,\n За день вы должны раздать минимум половину.\n Приступаете уже завтра, до свидания"
            e "До свидания!"
            jump center

    return
label center:
    scene cent
    "На следующий день..."
    jump office
    return
label office:
    scene offi
    "Офис, где принимали на работу был пуст, и наш герой отправился домой"
    jump sklad
    #jump donecard
    return

label donecard:
    scene manga



    return

#ГЛАВА: СКЛАД

label sklad:
    scene skl
    show sir_normal:
        xalign 0.8
    show rbtk:
        xalign 0.3 yalign 1.0
    zav "Что нужно?"
    e "Я хочу устроиться грузчиком в подростковый отдел"
    zav "Как зовут?"
    e "Меня зовут Сергиц"
    zav "Сколько годков тебе?"
    e "13"
    zav "Куда тебе гроши кидать?"
    e "на карту, 4130 2561 7890 1025"
    zav "Хорошо, вот твоя форма, за 1 смену получишь 900р."
    e "Хорошо"
    jump magnit
    return

label magnit:
    scene magn
    show sir_normal:
        xalign 0.8
    show rdmchel:
        xalign 0.3 yalign 1.0
    rdm "Че ты тут делаешь, деньги нужны?"
    menu:
        "Выберите вариант ответа"

        "Да, я пришел подрабатывать":
            rdm "Ясно. А я тут потому, что купил ашкудишку в долг"
            jump ashka
        "Нет, я пришел за продуктами":
            show sir_normal:
                xalign 0.8
            show rdmchel:
                xalign 0.3 yalign 1.0

            rdm "Тогда почему ты в рабочей форме?"
            
            e "Эээ{w=1}, моя куртка в стирке и я взял куртку отца."

            rdm "Ну ладно, иди"

            e "Да ладно, я пошутил. Буду работать тут"

            rdm "Шутник нашелся! Ну окей, работай."

            jump dom

        "Пошел нахуй":
            rdm "Ты чо ахухел бля?"
            show rdmchel:
                xalign 0.3 yalign 1.0

            show rdmchel:
                xalign 0.7 yalign 1.0

            show sir_shock:
                xalign 0.8
            scene boln
            with fade
            "Сергиц был атакован своим коллегой, после чего попал в больницу.\nПосле не очень долгого нахождения в больнице Сергица выписали"
            jump dom
            with fade
    return

label ashka:
    menu:
        "Выберите вариант ответа"

        "Ясно":
            rdm "Ладно, давай пока."
            jump dom
        "Дашь тяжку?":
            rdm "Ну, на"
            "Сергиц начинает затягиваться ашкудишкой рабочего,\n затем начинает задыхаться"
            scene boln
            "Только в больнице выяснилось, что наш герой скончался."
    return
label dom:
    scene home
    show sir_normal
    e "Ура, мне пришла зарплата! Я наконец смогу задонатить и выбить Леона!"
    "Услышав звуки Brawl Talk, Сергиц посмотрел на телевизор"
    hide sir_normal
    scene ved1
    vd "А мы переходим к завершающим новостям!"
    scene ved2
    vdall "..И мы наконец, приняли важнейшее решение: убрать ящики из игры!"
    scene home
    show sir_shock
    e "Что?!.."
    e "О нет! Мне же не хватит денег чтобы купить Леона за гемы"
    show sir_sad
    adm "end"
    return