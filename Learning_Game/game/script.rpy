# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)
define first_player = Character             ("[first_player]", color= "#00FFFF" )       #Игрок №1. Для пояснений, см. label name_choice
define second_player = Character            ("[second_player]", color= "#00FFFF" )      #Игрок №2. Для пояснений, см. label name_choice_coop
define decan = Character                    ('Декан', color= "#FFA500")  
define prepod_2 = Character                 ('Преподаватель Python', color= "#00FF00")
define prepod_3 = Character                 ('Преподаватель 1С', color= "#00008B")
define prepod_4 = Character                 ('Преподаватель SQL', color= "#00008B")
define unknown = Character                  ('', color="#FF0000" )                     #Используется в сценах,где не ясно, кто находится перед нами (Проще говоря, рассказчик).

                                                          
init:                   #Предварительные моменты игры
    # Фоновые изображения помещений (bgs = backgrounds).
        image bgs muiv =                     "content/images/backgrounds/others/muiv.jpeg"
        image bgs blackboard =               "content/images/backgrounds/boards/blackboard.jpg"
        image bgs fail =                     "content/images/backgrounds/others/fail.jpg"

 
    # Изображения вышеобъявленных персонажей.
        image decan =                       "content/images/characters/decan.png"


    # Изображения , которые будут использоваться в целях обучения и тестирования (т.е, единоразовые), хранить и объявлять в соответствующих им папкам и файлам. Тут их объявлять нет никакого смысла


label start:            #Тут начинается движение игры.
    stop music fadeout 5
    scene bgs muiv with dissolve
    unknown "Добро пожаловать в виртуальный университет."
    unknown "В данной игре вы можете практиковаться и обучаться по различным дисциплинам."
    unknown "Пожалуйста, выберите стиль игры. На выбор представлены два варианта: Сюжетный и Свободный."


label gamestyle_choice: #Выбор стиля игры
    menu gamestyle_choice_menu:
        "Выберите стиль игры:"

        "Сюжетный режим":
            jump story_mode

        "Свободный режим":
            jump freedom_mode

        "Отладка":
            jump debug_start



label story_mode:
unknown "В сюжетном режиме вы будете постепенно обучаться. Задания, тесты, экзамены и мини-игры будут открываться по мере прохождения игры."

label freedom_mode:
unknown "В свободном режиме весь контент сразу же доступен для воспроизведения."


label number_of_players:    # Меню выбора количества игроков
    menu players_count:
        "Выберите количество игроков:"

        "1 игрок":
            jump one_player
        "2 игрока":
            jump two_players


label one_player: # Если выбран 1 игрок

    jump choice_confirmation


label choice_confirmation:
    menu choice_confirmation_menu:
        "Вы уверены в своем выборе?:"

        "Да, я уверен":
            pass
        "Нет, я передумал":
            jump number_of_players

unknown "Хорошо,теперь, введите, пожалуйста, свое имя."
jump name_choice_first_player



label name_choice_first_player: # Функция input'а имени пользователя (для одичной игры)
    python:
        first_player = renpy.input("Как вас зовут?", length=32)
        first_player= first_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not first_player:
            first_player = "Студент"

    first_player "Меня зовут [first_player]!"
    unknown "Приятно познакомиться, [first_player], меня зовут **, я являюсь деканом факультета информационных технологий."
    show decan at left with dissolve 
    decan "Теперь выберите дисциплину для изучения и практики."
    hide decan
    jump choice_select_direction
 
label two_players: # Если выбрано 2 игрока
    "Вы выбрали режим игры для двух игроков."
    unknown "Игрок 1, введите, пожалуйста, свое имя."
    jump name_choice_first_player_coop

label name_choice_first_player_coop: # Функция input'а  1 имени игрока (для COOP)
     python:
        first_player = renpy.input("Игрок 1, введите своё имя.", length=32)
        first_player= first_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not first_player:
            first_player = "Студент 1"

     first_player "Меня зовут [first_player]!"
     unknown "Игрок 2, ваша очередь вводить свое имя."
     jump name_choice_second_player_coop

label name_choice_second_player_coop: # Функция input'а  2 имени игрока (для COOP)
     python:
        second_player = renpy.input("Игрок 2, введите своё имя.", length=32)
        second_player= second_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not second_player:
            second_player = "Студент 2"

     second_player "Меня зовут [second_player]!"
     "Приятно познакомиться, [second_player]"
     jump decan_first_appear_coop

label decan_first_appear_coop: # Представление декана для COOP
    unknown "Отлично, теперь немного обо мне. Меня зовут ***, я являюсь деканом факультета информационных технологий."
    show decan at left with dissolve
    decan "Теперь выберите дисциплину для изучения и практики."
    jump choice_select_direction_coop

label choice_select_direction: # Меню выбора дисциплины для одиночной игры
   menu choice:
        "Выберите дисциплину для изучения:"

        "Python":
            jump python_training_start

        "1C-Профессионал":
            jump professional_1c_training_start

        "Язык запросов SQL":
             jump sql_training_start


label choice_select_direction_coop: # Меню выбора дисциплины для COOP
   menu choice_coop:
        "Выберите дисциплину для изучения"

        "Python":
            jump python_training_start_coop

        "1C-Профессионал":
            jump professional_1c_training_start_coop

        "Язык запросов SQL":
            jump sql_training_start_coop
