label python_training_start:
    prepod_2 "[first_player],добро пожаловать на курс изучения python"
    prepod_2 "Пожалуйста, выберите режим игры"
    jump game_mode_choice


label game_mode_choice:
    menu choice_gamemode:
        "Режим игры"

        "Блиц-игра":
            jump speed_game_mode

        "Сборка полноценного кода по кусочкам":
            jump bulding_code_mode
             
        "Не знаю, что выбрать":
            jump i_dont_known



label speed_game_mode:
    pass

label bulding_code_mode:
    #pass

label i_dont_known:
   # pass
