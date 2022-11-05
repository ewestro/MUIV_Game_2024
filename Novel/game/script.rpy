
# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)
define captain = Character('Капитан', color= "#FF0000")
define firstman = Character('Рулевой', color= "#c8ffc8")
define coordinator = Character('Координатор', color= "#c8ffc8")
define signal = Character('Связист', color= "#c8ffc8")
define secure = Character('Начальник Охраны', color= "#c8ffc8")
define doctor = Character('Доктор', color= "#00FF00")
define secondman = Character('Старпом', color= "#c8ffc8")
define cook = Character('Кок', color= "#c8ffc8")
define engineer = Character('Техник', color= "#c8ffc8")

#Можно запилить скрипт, чтобы вместо должностей персонажей были их ФИО (При необходимости)



init:
# Тут можно объявлять изображения, но никто не мешает делать это прямо в сценах ( даже нужно так делать, особенно актуально для одиночных ивентов, нечего захламлять код)
    image bg Чуркостан = "Images/Чуркостан.jpg"
    image bg Какой-то бомжара = "Images/Какой-то бомжара.jpg"
    image captain_img = "Images/captain(400x400).png"
    image doctor_img = "Images/doctor(400x400).png"
   # image firstman_img = ""
   # image coordinator_img = ""
   # image signal_img = ""
   # image secure_img = ""
   # image secondman_img = ""
   # image cook_img = ""
   # image engineer_img  = ""

label start:
    scene bg Чуркостан with dissolve 

#Сцена с капитаном
    show captain_img with moveinleft
    captain "Привет,я Капитан"
menu:
    "Ты видишь капитана?"

    "Нет,я его не вижу":
        "Ну ты и слепое существо"

    "Да, вот он , стоит передо мной":
        "Ты красавчик)"

label after_menu:
    "А сейчас посмотрим на Доктора"


#Сцена с доктором
    scene bg Какой-то бомжара with fade
    show doctor_img with moveinright
    doctor "Привет,я Доктор"
menu:
    "Что сказать доктору?"

    "Слыш,Айболит,Чирик есть,гыы?":
        "Вас кинули с прогиба."

    "Давай 0,5 на двоих?":
        "Вы ввязались в драку с чурками. Айболит раскидал их как детей. Вы сделали выводы. Сделали же:? "

    "Промолчать":
        pass

    #firstman "Привет,я Рулевой"
    #coordinator "Привет,я Координатор"
    #signal "Привет,я Связист"
    #secure "Привет,я Начальник Охраны"
    #secondman "Привет,я Старпом"
    #cook "Привет,я Кок"
    #engineer "Привет,я Техник"
