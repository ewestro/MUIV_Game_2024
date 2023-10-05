# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)

define prepod_1 = Character('Преподаватель 1', color= "#4287f5")
define unknown = Character('???', color="#FF0000" ) #Используется в сценах,где не ясно, кто перед находится перед нами.



init:
# Тут можно объявлять изображения, но никто не мешает делать это прямо в сценах ( даже нужно так делать, особенно актуально для одиночных ивентов, нечего захламлять код)

    # Фоновые изображения (bg= background) .
    image bg muiv = "images/backgrounds/muiv.jpeg"
    
    # Изображения персонажей .
    image prepod_1_img = "images/characters/prepod_1.png"



#Тут начинается сюжет.

label start:
    stop music fadeout 5
    scene bg muiv with dissolve
    show prepod_1 at left with dissolve
    prepod_1 "Добро пожаловать в университет."
    hide prepod_1

    menu choice_select_direction:
        "Выберите дисциплину для изучения"

        "Python":
            jump python_training_start

        "1C-Профессионал":
            jump professional_1c_training_start

        "Placeholder":
             pass
