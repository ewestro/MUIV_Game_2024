label python_training_start:
    prepod_2 "[first_player],добро пожаловать на курс изучения python"
    prepod_2 "Пожалуйста, выберите режим игры"
    jump game_mode_choice


label game_mode_choice:
    menu choice_gamemode:
        "Режим игры"

        "Блиц-игра":
            jump python_time_game_start

        "Сборка полноценного кода по кусочкам":
            jump bulding_code_mode
             
        "Экзамен":
            jump python_exam_start




label bulding_code_mode:
    #pass
