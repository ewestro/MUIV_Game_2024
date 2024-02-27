label html_training_start:
    show prepod_5 at right with dissolve 
    prepod_5 "[first_player], Приветствую. Меня зовут Киселев Федор Владимирович. Я буду преподавать курс изучения языка разметки HTML."
    prepod_5 "Пожалуйста, выберите режим игры"
    jump html_game_mode_choice

label  html_game_mode_choice:
    menu  html_choice_gamemode:
        "Режим игры"

        "Блиц-игра":
            jump  html_time_game_start

        "Сборка полноценного кода по кусочкам":
            jump  html_bulding_code_mode
             
        "Тестирование": #готовое тестирование без попыток и сохранения
            jump  html_exam_start

label  html_bulding_code_mode:
    #pass