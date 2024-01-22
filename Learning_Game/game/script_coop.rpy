label two_players: # Если выбрано 2 игрока
    "Вы выбрали режим игры для двух игроков."
    "Игрок 1, введите, пожалуйста, свое имя."


label name_choice_first_player_coop: # Функция input'а  1 имени игрока (для COOP)
    python:
        first_player = renpy.input("Игрок 1, введите своё имя.", length=32)
        first_player= first_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not first_player:
            first_player = "Студент 1"

    first_player "Меня зовут [first_player]!"
    "Игрок 2, ваша очередь вводить свое имя."


label name_choice_second_player_coop: # Функция input'а  2 имени игрока (для COOP)
    python:
        second_player = renpy.input("Игрок 2, введите своё имя.", length=32)
        second_player= second_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not second_player:
            second_player = "Студент 2"

    second_player "Меня зовут [second_player]!"
    "Приятно познакомиться, [second_player]"


label decan_first_appear_coop: # Представление декана для COOP
    "Отлично, теперь немного обо мне" 
    show decan at left with dissolve
    "Меня зовут ***, я являюсь деканом факультета информационных технологий."
    decan "Теперь выберите дисциплину для изучения и практики."
    jump choice_select_direction_coop


label choice_select_direction_coop: # Меню выбора дисциплины для COOP
    menu choice_coop:
        "Выберите дисциплину для изучения"

        "Python":
            jump python_training_start_coop

        "1C-Профессионал":
            jump professional_1c_training_start_coop

        "Язык запросов SQL":
            jump sql_training_start_coop
