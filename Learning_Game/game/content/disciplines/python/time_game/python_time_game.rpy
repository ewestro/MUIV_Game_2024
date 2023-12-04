label python_time_game_start:
    prepod_2 "[first_player],Давай сыграем на время: успей ответить на все вопросы, пока таймер не истек."

label QTE_test_1:   #Задание 1
    $ time = 5
    $ menu_timer_graphical = True

    scene bgs blackboard
    menu QTE_test_1_1:
        "Это тест QTE c графическим таймером."

        "Выбор 1":
            jump QTE_test_2
        "Выбор 2":
            jump QTE_test_2
           

label QTE_test_2:
    $ time = 5
    $ menu_timer_numeral = True
    scene bgs blackboard
    menu QTE_test_2_1:
        "А это тест с текстовым таймером."

        "Выбор 1":
            pass
        "Выбор 2":
            pass


label timeout_marker:
"Время вышло."