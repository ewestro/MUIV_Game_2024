# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)
define first_player = Character             ("[first_player]", color= "#00FFFF" )       #Игрок №1. Для пояснений, см. label name_choice
define second_player = Character            ("[second_player]", color= "#00FFFF" )      #Игрок №2. Для пояснений, см. label name_choice_coop
define decan = Character                    ('Декан', color= "#FFA500")  
define prepod_2 = Character                 ('Преподаватель Python', color= "#00FF00")
define prepod_3 = Character                 ('Преподаватель 1С', color= "#00008B")
define prepod_4 = Character                 ('Преподаватель SQL', color= "#00008B")
define unknown = Character                  ('', color="#FF0000" )                     #Используется в сценах,где не ясно, кто находится перед нами.

                                                          
init:                   #Предварительные моменты игры
    # Фоновые изображения помещений (bgs = backgrounds).
        image bgs muiv =                     "content/images/backgrounds/others/muiv.jpeg"
        #image bgs corridor_1=               "content/images/backgrounds/corridors/"
        #image bgs corridor_2=               "content/images/backgrounds/corridors/"
        #image bgs class_1=                  "content/images/backgrounds/classes/"
        #image bgs class_2=                  "content/images/backgrounds/classes/"
        #image bgs class_3=                  "content/images/backgrounds/classes/"
        #image bgs class_4                   "content/images/backgrounds/classes/"

    # Изображения вышеобъявленных персонажей (img = image).
        #image first_player_img =           "content/images/characters/first_player.png"          #Изображение первого игрока
        #image second_player_img =          "content/images/characters/second_player.png"         #Изображение второго игрока
        image decan =                       "content/images/characters/decan.png"
        # image prepod_2_img = ""
        # image prepod_3_img = ""
        # image prepod_4_img = ""



label start:            #Тут начинается движение игры.
    stop music fadeout 5
    scene bgs muiv with dissolve
    unknown "Добро пожаловать в университет. В данной игре вы можете практиковаться и обучаться по различным дисциплинам."
    unknown "Однако, перед началом, выберите количество игроков."
    jump number_of_players

    
label number_of_players:    # Меню выбора количества игроков
    menu players_count:
        "Выберите количество игроков:"

        "1 игрок":
            jump one_player
        "2 игрока":
            jump two_players


label one_player: # Если выбран 1 игрок
    "Вы выбрали режим игры для одного игрока."
    unknown "Теперь, введите, пожалуйста, свое имя."
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
            first_player = "Студент1"

     first_player "Меня зовут [first_player]!"
     unknown "Игрок 2, ваша очередь выбирать имя."
     jump name_choice_second_player_coop

label name_choice_second_player_coop: # Функция input'а  2 имени игрока (для COOP)
     python:
        second_player = renpy.input("Игрок 2, введите своё имя.", length=32)
        second_player= second_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not second_player:
            second_player = "Студент2"

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
