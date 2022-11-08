
# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)

define captain = Character('Капитан', color= "#4287f5")
define firstman = Character('Старпом', color= "#FF0000")
define secondman = Character('Рулевой', color= "#c8ffc8")
define coordinator = Character('Координатор', color= "#c8ffc8")
define signal = Character('Связист', color= "#c8ffc8")
define secure = Character('Начальник Охраны', color= "#c8ffc8")
define doctor = Character('Доктор', color= "#00FF00")
define cook = Character('Кок', color= "#c8ffc8")
define engineer = Character('Техник', color= "#c8ffc8")


init:
# Тут можно объявлять изображения, но никто не мешает делать это прямо в сценах ( даже нужно так делать, особенно актуально для одиночных ивентов, нечего захламлять код)

    # Фоновые изображения (bg= background) .
    image bg port = "Images/background/port.jpeg"
    image bg corridor = "Images/background/corridor.jpg"
    image bg gostinnaya = "Images/background/gostinnaya.jpeg"
    image bg kitchen = "Images/background/kitchen.jpg"

    # изображения персонажей .
    image captain_img = "Images/characters/captain.png"
    image firstman_img = "Images/characters/firstman.png"
    image secondman_img = "Images/characters/secondman.png"
    image cook_img = "Images/characters/cook.png"

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
            show captain at left
            captain "{i}Как же он хорош.{/i}"
            hide captain
            "Постояв еще какое-то время, капитан вошел внутрь."
        
        "Пойти внутрь":
            pass



    scene bg corridor with dissolve
    "Палуба встретила капитана тусклым дежурным освещением."
    "Через несколько поворотов он вышел к складу, где его уже ждала старшая помощница."
    "Она барабанила пальцами в нетерпении и казалась весьма бодрой, несмотря на ранний час."

    show captain at left
    captain "Все хорошо?"
    hide captain
    show firstman at right
    firstman "Предполетная подготовка закончена! Склад загружен, документы заполнены. Но лучше загляни в двигательный отсек, Рикке там всё ещё что-то паяет."
    hide firstman

    menu:
        "Что сказать?"

        "А в жизни как? Как дела дома?":
            show firstman at right
            firstman "А как может быть дома у человека, который там не бывает?"
            hide firstman
            "Судя по её улыбке, старпома такой расклад дел вполне устраивал."
            show captain at left
            captain "Ну, бывай. Жду на мостике, как закончу обход."
            hide captain

        "Ну, бывай. Жду на мостике, как закончу обход.":
            pass
    
    
    scene bg gostinnaya with dissolve
    "Первым отсеком на пути капитана был бытовой."
    "Двери в кают-компанию были открыты, и на большом диване у противоположной стены клевал носом рулевой, заложив руки за голову."
    "Он встрепенулся, зевая и щуря глаза, раньше, чем капитан успел его окликнуть."

    show secondman at right
    secondman "Стало быть, пора?"
    hide secondman
    show captain at left
    captain "Скоро. Финальный обход."
    hide captain
    show secondman at right
    secondman "Куда хоть летим? Шеридан там уже на стенку без точных координат лезет."
    hide secondman
    show captain at left
    captain "На стенку, говоришь?"
    hide captain
    "Капитан достал коммуникатор и, не глядя, набрал частоту Координатора."
    show captain at left
    captain " Вега. Путь будет спокойным."
    hide captain
    "Рулевой недовольно скривился, не получив точного ответа."
    show captain at left
    captain "Я уже отправил координаты."
    hide captain
    "Рулевой расслабился, откинувшись на спинку дивана, и махнул рукой."
    show secondman at right
    secondman "Тогда иди, заканчивай свой осмотр."
    hide secondman


    scene bg kitchen with dissolve
    "Следующей остановкой в списке была кухня."
    "Оттуда уже во всю доносились звуки и запахи готовки."

    show captain at left
    captain " Могу поинтересоваться, как все подготовлено?"
    hide captain
    #тут должен быть звук грохота посуды, но пока его нет
    show cook at right
    cook " Ох ты ж!"
    hide cook
    "Кок недовольно повернулась лицом к двери, уперев руки в бока, и тут же просияла, увидев капитана."
    show cook at right
    cook "Капитан, ты ко времени! Все готово. Еда на складу, я в мылу."
    hide cook
    show captain at left
    captain "Есть что-то вкусненькое?"
    hide captain
    show cook at right
    cook "А шо, готовое уже не годно? Чай, сам сухпайки выбирал."
    hide cook
    show captain at left
    captain "Есть что-то новое?"
    hide captain
    show cook
    cook "А то! Купила себе книжку рецептов с Фольмагаута в увольнении, и вот начала уже готовить."
    hide cook
    show captain at left
    captain "Раз такое дело, пойду-ка. Не буду мешать."
