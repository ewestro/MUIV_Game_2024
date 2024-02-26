# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново).
define first_player = Character ("[first_player]", color= "#00FFFF" )   #Игрок №1. Для пояснений, см. label name_choice.
define second_player = Character ("[second_player]", color= "#00FFFF" ) #Игрок №2. Для пояснений, см. label name_choice_coop.
define decan = Character ('Зайцев Сергей Александрович', color= "#FFA500")  
define secretar = Character ('Владимирова Елизавета Олеговна', color= "#FFA5FF") 
define prepod_2 = Character ('Преображенский Максим Владимирович', color= "#00FF00")
define prepod_3 = Character ('Стряпунина Нэля Ильинична', color= "#00008B")
define prepod_4 = Character ('SQL', color= "#00008B")
define prepod_5 = Character ('Киселёв Федор Владимирович', color= "#FF00BB")
define prepod_6 = Character ('Коротков Дмитрий Павлович', color= "#FF550B")
define unknown = Character ('', color="#FF0000" )   #Используется в сценах,где не ясно, кто находится перед нами (Проще говоря, рассказчик).

init -1: # Переключатели и Переменные.
    # Переключатели меню выбора.  Для активации, в нужный момент игры (НЕ ТУТ, А В САМОМ КОДЕ ИГРЫ) перевести необходимую переменную в положение = True.
    $ numeral_timer_menu= False      #  меню с числовым таймером.
    $ graphical_timer_menu = False   #  меню с графическим таймером.
    $ horizontal_menu = False         #  горизонтальное меню. 
    $ vertical_menu = True          # вертикальное меню.

    # Переменные для генератора имени пользователя.
    $ first_player = "" # Поле, в которое вносится имя пользователя.
    $ gender_male = False
    $ firstname_list_male = ["Глеб", "Дональд" , "Севастьян", "Ярослав", "Николай", "Тимур", "Захар", "Клемент", "Виталий", "Адриан"]
    $ lastname_list_male = ["Дроздов", "Носков", "Крылов", "Лихачёв", "Белов", "Овчинников", "Якушев", "Морозов", "Лаврентьев", "Кондратьев"]
    $ firstname_list_female = ["Сара", "Кира" , "Владислава", "Ванесса", "Леся", "Инесса", "Мелитта", "Эвелина", "Полина", "Милена"]
    $ lastname_list_female = ["Александрова", "Петрова" , "Мухина", "Беляева", "Нестерова", "Орехова", "Кулакова", "Мышкина", "Блохина", "Миронова"]

init:   #Предварительные моменты игры
    # Фоновые изображения помещений (bg_ = backgrounds).
    image bg_muiv = "content/images/backgrounds/others/muiv.jpeg"
    image bg_vhod = "content/images/backgrounds/others/vhod.jpg"
    image bg_koridor = "content/images/backgrounds/others/koridor.jpg"
    image bg_koridor2 = "content/images/backgrounds/others/koridor2.jpg"
    image bg_blackboard = "content/images/backgrounds/boards/blackboard.jpg"
    image bg_fail = "content/images/backgrounds/others/fail.jpg"
    image bg_kabinet = "content/images/backgrounds/others/kabinet.jpg"
    image bg_viborka = "content/images/backgrounds/others/viborka.jpg"
    # Изображения вышеобъявленных персонажей.
    image decan = "content/images/characters/decan.png"
    image secretar = "content/images/characters/secretar.png"
    image prepod_2 = "content/images/characters/prepod_2.png"
    image prepod_5 = "content/images/characters/prepod_5.png"
    # Изображения меню
    image menu_1 = "content/images/menu/menu_1.jpg"
    image menu_2 = "content/images/menu/menu_2.jpg"
    # Изображения , которые будут использоваться в целях обучения и тестирования (т.е, единоразовые), хранить и объявлять в соответствующих им папкам и файлам. Объявлять их тут нет никакого смысла.

label splashscreen: # Начальный сплешскрин.
    image muiv ="gui/splashscreen/muiv.jpg"
    image fit = "gui/splashscreen/fit.jpg"
    scene black
    with Pause(2)
    show muiv at truecenter  with dissolve  
    with Pause (3)
    hide muiv with dissolve
    show fit at truecenter  with dissolve 
    with Pause (3)
    hide fit with dissolve
    show text "Данный проект создан в рамках Выпускной Квалификационной Работы и не претендует на звание игры года . Проект находится в стадии активной разработки, поэтому вы можете столкнуться с различными багами, ошибками и недочетами." with dissolve
    with Pause(7)
    hide text with dissolve
    with Pause(1)
    show text "Надеемся, что вам понравится хоть немного. Мы  очень старались." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    return

label start:    # Тут начинается движение игры.
    stop music fadeout 5
    scene bg_muiv with dissolve
    "Добро пожаловать в виртуальный университет им. С.Ю.Витте !"
    "В данной игре вы можете обучаться и практиковаться по различным видам дисциплин."
    "Для начала, пожалуйста, выберите количество игроков."


label players_count:  # Меню выбора количества игроков
    scene bg_vhod with dissolve
    menu players_count_menu:
        "Выберите количество игроков:"

        "1 игрок":
            pass
        "2 игрока":
            jump two_players
        "Online(скоро)":
            jump building_code_mode2
        "Отладка":
            jump debug_start

label pol_choice:
    $ vertical_menu = False
    $ horizontal_menu = True  
    "Сейчас вам будет предложено выбрать пол"
    menu pol_choice_menu:
        "Выберите пол(коряво отображается вертикальное меню, скоро исправим):"
        
        "Мужской":
            $ gender_male = True
        "Женский":
            $ gender_male = False

$ vertical_menu = True
$ horizontal_menu = False


"Отлично. Теперь введите ваше имя."
"Вы можете ввести имя сами, или воспользоваться генератором."

label username_choice:  # Вводит ли пользователь имя сам, или использует генератор.
    menu username_choice_menu:
        "Выберите действие"

        "Я введу имя сам.":
            jump username_choice_first_player

        "Я воспользуюсь генератором имен.":
            pass

        "Вернуться к выбору пола":
            call pol_choice

label username_generator: #Генератор имен пользователя
    python:
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

label use_generator:    # Генерируем рандомное имя пользователя + условия.
    python:
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
    "Вы уверены в своем выборе? Изменить имя можно будет только после окончания обучения."

    menu username_choice_menu_confirm:
        "Подтвердите выбор"

        "Да, мне нравится созданное имя.":
            pass

        "Нет, я хочу изменить имя.":
            $ first_player = ""
            call username_choice

    scene bg_koridor with dissolve
    show decan at left with dissolve  
    decan "Приятно познакомиться, [first_player], меня зовут Зайцев Сергей Александрович, я являюсь деканом факультета информационных технологий."
    show secretar at right with dissolve 
    decan "А это мой секретарь Владимирова Елизавета Олеговна. Она будет вас сопровождать во время игры, и если возникнут вопросы, обращайтесь к ней."
    hide decan
    hide secretar
    scene bg_koridor2 with dissolve
    show secretar at right with dissolve 
    secretar "Привет. Ну что, начнем обучение?"

label players_vibor:  # Меню выбора количества игроков
    menu players_vibor_menu:

        "Да":
            pass
        "Нет":
            secretar "Подумай ещё."
            jump players_vibor
            
scene bg_kabinet with dissolve
"Пора выбрать режим игры."
"На выбор представлены три режима: свободный , сюжетный и режим ознакомительноно тура по университету."
hide secretar

label gamestyle_choice: # Выбор стиля игры
    menu gamestyle_choice_menu:
        "Выберите стиль игры:"

        "Сюжетный режим":
            pass

        "Свободный режим":
            jump freedom_mode

        "Ознакомительный тур":
            jump university_tour_start


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


label choice_direction: # Меню выбора дисциплины для одиночной игры
    scene bg_viborka with dissolve    
    "Теперь пора выбрать дисциплину."
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

        "Разработка ПО для мобильных устройств":
            jump mobilka_training_start
