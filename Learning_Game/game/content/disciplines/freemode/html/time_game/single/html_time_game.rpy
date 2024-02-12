label html_time_game_start:
    prepod_5 "Давай сыграем на время: успей ответить  все вопросы, пока таймер не истек."

    label html_QTE_test_1:   #Задание 1
    $ time = 10
    $ menu_timer_graphical = True
    scene bgs blackboard
    menu html_QTE_test_1_1:
        "Это тест QTE c графическим таймером."
        "Выбор 1":
            jump html_QTE_test_2
        "Выбор 2":
            jump html_QTE_test_2
           
label html_QTE_test_2:
    $ time = 10
    $ menu_timer_numeral = True
    scene bgs blackboard
    menu html_QTE_test_2_1:
        "А это тест с текстовым таймером."
        "Выбор 1":
            pass
        "Выбор 2":
            pass

label html_timeout_marker:
"Время вышло."