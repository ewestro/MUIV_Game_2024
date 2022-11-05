
# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)
define captain = Character('Капитан', color="#c8ffc8")
define firstman = Character('Рулевой', color="#c8ffc8")
define coordinator = Character('Координатор', color="#c8ffc8")
define signal = Character('Связист', color="#c8ffc8")
define secure = Character('Начальник Охраны', color="#c8ffc8")
define doctor = Character('Доктор', color="#c8ffc8")
define secondman = Character('Старпом', color="#c8ffc8")
define cook = Character('Кок', color="#c8ffc8")
define engineer = Character('Техник', color="#c8ffc8")

#Можно запилить скрипт, чтобы вместо должностей персонажей были их ФИО (При необходимости)



init:
    # Тут можно объявлять изображения, но никто не мешает делать это прямо в сценах ( даже нужно так делать, особенно актуально для одиночных ивентов, нечего захламлять код)
    image bg Чуркостан = "Images/Чуркостан.jpg"
    image bg Какой-то бомжара = "Images/Какой-то бомжара.jpg"
    image captain_img = "Images/captain(400x400).png"
   # image firstman = ""
   # image coordinator = ""
   # image signal = ""
   # image secure = ""
   # image doctor = ""
   # image secondman = ""
   # image cook = ""
   # image engineer = ""

label start:
    scene bg Чуркостан with dissolve 
    show captain_img at left
    captain "Привет,я Капитан"
    #firstman "Привет,я Рулевой"
    #coordinator "Привет,я Координатор"
    #signal "Привет,я Связист"
    #secure "Привет,я Начальник Охраны"
    #doctor "Привет,я Доктор"
    #secondman "Привет,я Старпом"
    #cook "Привет,я Кок"
    #engineer "Привет,я Техник"

    scene bg Какой-то бомжара with fade
    "А это какой-то хрен, добавил его для теста переходов между экранами."
    "Больше тут ничего смотреть, ливай отсюда"
