# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново).
define first_player = Character ("[first_player]", color= "#00FFFF" )   #Игрок №1. Для пояснений, см. label name_choice.
define second_player = Character ("[second_player]", color= "#00FFFF" ) #Игрок №2. Для пояснений, см. label name_choice_coop.
define decan = Character ('Декан', color= "#FFA500")  
define prepod_2 = Character ('Преподаватель Python', color= "#00FF00")
define prepod_3 = Character ('Преподаватель 1С', color= "#00008B")
define prepod_4 = Character ('Преподаватель SQL', color= "#00008B")
define prepod_5 = Character ('Преподаватель HTML', color= "#FF00BB")
define unknown = Character ('', color="#FF0000" )   #Используется в сценах,где не ясно, кто находится перед нами (Проще говоря, рассказчик).

init -1: # Переключатели и Переменные.
    # Переключатели меню выбора.  Для активации, в нужный момент игры (НЕ ТУТ, А В САМОМ КОДЕ ИГРЫ) перевести необходимую переменную в положение = True.
    $ numeral_timer_menu= False      #  меню с числовым таймером.
    $ graphical_timer_menu = False   #  меню с графическим таймером.
    $ horizontal_menu = False        #  вертикальное меню. 

    # Переменные для генератора имени пользователя.
    $ first_player = ""
    $ gender_male = False
    $ firstname_list_male = ["Глеб", "Дональд" , "Севастьян", "Ярослав", "Николай", "Тимур", "Захар", "Клемент", "Виталий", "Адриан"]
    $ lastname_list_male = ["Дроздов", "Носков", "Крылов", "Лихачёв", "Белов", "Овчинников", "Якушев", "Морозов", "Лаврентьев", "Кондратьев"]
    $ firstname_list_female = ["Сара", "Кира" , "Владислава", "Ванесса", "Леся", "Инесса", "Мелитта", "Эвелина", "Полина", "Милена"]
    $ lastname_list_female = ["Александрова", "Петрова" , "Мухина", "Беляева", "Нестерова", "Орехова", "Кулакова", "Мышкина", "Блохина", "Миронова"]

init:   #Предварительные моменты игры
    # Фоновые изображения помещений (bgs = backgrounds).
    image bgs muiv = "content/images/backgrounds/others/muiv.jpeg"
    image bgs blackboard = "content/images/backgrounds/boards/blackboard.jpg"
    image bgs fail = "content/images/backgrounds/others/fail.jpg"

    # Изображения вышеобъявленных персонажей.
    image decan = "content/images/characters/decan.png"

    # Изображения , которые будут использоваться в целях обучения и тестирования (т.е, единоразовые), хранить и объявлять в соответствующих им папкам и файлам. Объявлять их тут нет никакого смысла.

label start:    # Тут начинается движение игры.
    stop music fadeout 5
    scene bgs muiv with dissolve
    "Добро пожаловать в виртуальный университет."
    "В данной игре вы можете обучаться и практиковаться по различным видам дисциплин."
    "Для начала, пожалуйста, выберите количество игроков."

label players_count:  # Меню выбора количества игроков
    menu players_count_menu:
        "Выберите количество игроков:"

        "1 игрок":
            pass
        "2 игрока":
            jump two_players
        "Online(скоро)":
            pass
        "Отладка":
            jump debug_start

label pol_choice:
    $ horizontal_menu = True
    "Сейчас вам будет предложено выбрать пол"
    menu pol_choice_menu:
        "Выберите пол:"
        
        "Женский":
            pass
        "Мужской":
            $ gender_male = True

"Отлично. Теперь введите ваше имя."
$ horizontal_menu = False
label name_choice:  # Вводит ли пользователь имя сам, или использует генератор.
    menu username_choice_menu:
        "Выберите действие"

        "Я введу имя сам.":
            jump username_choice_first_player

        "Я воспользуюсь генератором имен.":
            pass

        "Вернуться назад":
            jump players_count

label username_generator: #Генератор имен пользователя
init python:
        class username_generator_class_male:

            def username_male_generator_func(self):
                generatedfirstnamemale = renpy.random.choice(firstname_list_male) 
                generatedlastnamemale = renpy.random.choice(lastname_list_male) 
                store.first_player = generatedfirstnamemale + " " + generatedlastnamemale 

        class username_generator_class_female:
            def username_female_generator_func(self):
                generatedfirstnamefemale = renpy.random.choice(firstname_list_female) 
                generatedlastnamefemale = renpy.random.choice(lastname_list_female) 
                store.first_player = generatedfirstnamefemale + " " + generatedlastnamefemale 

label use_generator:    # Генерируем рандомное имя пользователя
init python:
    if gender_male == True:
        gen = username_generator_class_male()
        gen.username_male_generator_func() 
    else:
        gen = username_generator_class_female()
        gen.username_female_generator_func() 

    "Сгенерированное имя [first_player]."
jump greetings

label username_choice_first_player: # Функция input'а имени пользователя (для одичной игры).
    python:
        first_player = renpy.input("Меня зовут...\n", length=32)
        first_player = first_player.strip() # Обрезаем имя, чтобы в поле ввода не попадали пробелы и лишние знаки.
        if not first_player:
            first_player = "Студент"

label greetings:    # Функция приветствия. 
    first_player "Меня зовут [first_player]!"
    "Вы уверены в своем выборе? Изменить имя можно будет только после обучения."
    menu username_choice_menu_confirm:
        "Подтвердите выбор"

        "Да, мне нравится созданное имя.":
            pass

        "Нет, я передумал.":
            $ first_player = ""
            jump name_choice
    
    decan "Приятно познакомиться, [first_player], меня зовут **, я являюсь деканом факультета информационных технологий."
    show decan at left with dissolve 
  
"Пора выбрать режим игры."
"На выбор представлены три режима: свободный , сюжетный и режим ознакомительноно тура по университету."
hide decan

label gamestyle_choice: # Выбор стиля игры
    menu gamestyle_choice_menu:
        "Выберите стиль игры:"

        "Сюжетный режим":
            pass

        "Свободный режим":
            jump freedom_mode

        "Ознакомительный тур":
            jump university_tour_mode


label story_mode: # Если выбраен сюжетный режим.
    "В сюжетном режиме вы будете обучаться постепенно. Задания, тесты, экзамены и мини-игры будут открываться по мере прохождения игры."
jump choice_confirmation


label freedom_mode: # Если выбран свободный режим.
    "В свободном режиме весь контент сразу же доступен для воспроизведения."


label choice_confirmation: # Подтверждение выбора пользователя.
    menu choice_confirmation_menu:
        "Вы уверены в своем выборе?"

        "Да, я уверен":
            pass
        "Нет, я передумал":
            jump gamestyle_choice
     
"Теперь пора выбрать дисциплину."
label choice_direction: # Меню выбора дисциплины для одиночной игры
    menu choice_direction_menu:
        "Выберите дисциплину для изучения:"

        "Python":
            jump python_training_start

        "1C-Профессионал":
            jump professional_1c_training_start

        "Язык запросов SQL":
            jump sql_training_start

        "Язык разметки HTML":
            jump html_training_start