
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
    image bg port = "Images/background/port.jpg"
    #image bg 2 = "Images/background/2.jpg"
    #image bg 3 = "Images/background/3.jpg"
    #image bg 4 = "Images/background/4.jpg"
    #image bg 5 = "Images/background/5.jpg"
    #image bg 6 = "Images/background/6.jpg"
    #image bg 7 = "Images/background/7.jpg"
    #image bg 8 = "Images/background/8.jpg"
    #image bg 9 = "Images/background/9.jpg"
    #image captain_img = "Images/characters/captain(400x400).png"
    #image doctor_img = "Images/characters/doctor(400x400).png"
   # image firstman_img = ""
   # image coordinator_img = ""
   # image signal_img = ""
   # image secure_img = ""
   # image secondman_img = ""
   # image cook_img = ""
   # image engineer_img  = ""

label start:
    scene bg port with dissolve
    "Корабль, пришвартованный у самого края провинциального космопорта, ничем не выделялся на фоне окружающего пейзажа."
    "Потрепанная металлическая обшивка сливалась с серыми панелями стен, пустые иллюминаторы едва отражали тусклый свет."
    "Когда-то эта модель была образцом грузового транспорта, но теперь от её былой славы осталась лишь полуоблупившиеся и поблекшие языки пламени, нарисованные по бокам корабля."
    "И все-таки в иллюминаторах иногда вспыхивали лампы, а обшивка правого борта переливалась серебром в холодном свете звёзд."
    "Человеку достаточно мечтательному этот вид мог бы даже показаться красивым."

menu:
    "Выберите действие"

    "Посмотреть еще":
        captain "Как же он хорош."
        "Постояв еще какое-то время, капитан вошел внутрь"
        
    "Пойти внутрь":
        pass

label after_menu:
    "Палуба встретила капитана тусклым дежурным освещением."