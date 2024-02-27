label python_training_start:
    scene bg_kabinet with dissolve
    show prepod_2 at left
    prepod_2 " Добро пожаловать на курс изучения Python!"
    prepod_2 "Пожалуйста, выберите режим игры."
    jump python_gamemode_choice
    hide prepod_2


label python_gamemode_choice:
    menu python_gamemode_choice_menu:
        "Режим игры:"

        "Блиц-игра":
            jump python_attempts_checkout

        "Экзамен":
            jump python_exam_start

        "Сборка полноценного кода по кусочкам":
            jump building_code_mode
             

label building_code_mode:
    "Этот режим пока недоступен."
    jump python_gamemode_choice

label building_code_mode2:
    "Этот режим пока недоступен."
    jump players_count