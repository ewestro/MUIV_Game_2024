label html_training_start:
    prepod_5 "[first_player],добро пожаловать на курс изучения  html"
    prepod_5 "Пожалуйста, выберите режим игры"
    jump html_game_mode_choice

label  html_game_mode_choice:
    menu  html_choice_gamemode:
        "Режим игры"

        "Блиц-игра":
            jump  html_time_game_start

        "Сборка полноценного кода по кусочкам":
            jump  html_bulding_code_mode
             
        "Экзамен":
            jump  html_exam_start

label  html_bulding_code_mode:
    #pass