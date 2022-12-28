
# Объявляем персонажей (легче обращаться к сущностям, чем каждый раз прописывать их заново)

define captain = Character('Капитан', color= "#4287f5")
define firstman = Character('Старпом', color="#c8ffc8" )
define secondman = Character('Рулевой', color= "#c8ffc8")
define coordinator = Character('Координатор', color= "#c8ffc8")
define signal = Character('Связист', color= "#c8ffc8")
define secureman = Character('Начальник Охраны', color="#FF0000" )
define medic = Character('Медик', color= "#00FF00")
define cook = Character('Кок', color= "#c8ffc8")
define engineer = Character('Техник', color= "#c8ffc8")
define unknown = Character('???', color="#FF0000" ) #Используется в сценах,где не ясно, кто перед находится перед нами.


init:
# Тут можно объявлять изображения, но никто не мешает делать это прямо в сценах ( даже нужно так делать, особенно актуально для одиночных ивентов, нечего захламлять код)

    # Фоновые изображения (bg= background) .
    image bg port = "Images/background/port.jpeg"
    image bg corridor = "Images/background/corridor.jpg"
    image bg gostinnaya = "Images/background/gostinnaya.jpeg"
    image bg kitchen = "Images/background/kitchen.jpg"
    image bg clinic = "Images/background/clinic.jpg"
    image bg utility = "Images/background/utility.jpg"
    image bg signal_room ="Images/background/signal_room.jpg"
    image bg armory_room="Images/background/armory_room.jpg"

    # Изображения персонажей .
    image captain_img = "Images/characters/captain.png"
    image firstman_img = "Images/characters/firstman.png"
    image secondman_img = "Images/characters/secondman.png"
    image cook_img = "Images/characters/cook.png"
    image medic_img = "Images/characters/medic.png"
    image engineer_img= "Images/characters/engineer.png"
    image signal_img = "Images/characters/signal.png"
    image secureman_img="Images/characters/secureman.png"


#Тут начинается сюжет.

label start:
    stop music 
    scene bg port with dissolve
    "Корабль, пришвартованный у самого края провинциального космопорта, ничем не выделялся на фоне окружающего пейзажа."
    "Потрепанная металлическая обшивка сливалась с серыми панелями стен, пустые иллюминаторы едва отражали тусклый свет."
    "Когда-то эта модель была образцом грузового транспорта, но теперь от её былой славы осталась лишь полуоблупившиеся и поблекшие языки пламени, нарисованные по бокам корабля."
    "И все-таки в иллюминаторах иногда вспыхивали лампы, а обшивка правого борта переливалась серебром в холодном свете звёзд."
    "Человеку достаточно мечтательному этот вид мог бы даже показаться красивым."

    menu before_enter_the_ship:
        "Выберите действие"

        "Посмотреть еще":
            show captain at left
            captain "{i}Как же он хорош.{/i}"
            hide captain
            "Постояв еще какое-то время, капитан вошел внутрь."
        
        "Пойти внутрь":
            "Капитан сразу же направился вглубь корабля"


# Сцена в коридоре/палубе

    scene bg corridor with dissolve
    "Палуба встретила капитана тусклым дежурным освещением."
    "В коридоре его уже ждала старшая помощница."
    "Она барабанила пальцами в нетерпении и казалась весьма бодрой, несмотря на ранний час."

    show captain at left
    captain "Все хорошо?"
    hide captain
    show firstman at right
    firstman "Предполетная подготовка закончена! Склад загружен, документы заполнены. Но лучше загляни в двигательный отсек, Рикке там всё ещё что-то паяет."
    hide firstman

    menu firstman_scene:
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
    

#Сцена в бытовом отсеке

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


#Сцена на кухне
    scene bg kitchen with dissolve
    "Следующей остановкой в списке была кухня."
    "Оттуда уже во всю доносились звуки и запахи готовки."

    show captain at left
    captain " Могу поинтересоваться, как все подготовлено?"
    hide captain
    play sound "audio/ivent_sounds/tableware_drop.mp3"
    show cook at right
    cook " Ох ты ж..."
    hide cook
    "Кок недовольно повернулась лицом к двери, уперев руки в бока, и тут же просияла, увидев капитана."
    show cook at right
    cook "Капитан, ты ко времени! Все готово. Еда на складу, я в мылу."
    hide cook
    
    menu kitchen:
        "Что спросить?"
  
        "Есть что-то вкусненькое?":
            show cook at right
            cook "А шо, готовое уже не годно? Чай, сам сухпайки выбирал."
            hide cook
            show captain at left
            captain "Так это же сухпайки, чего от них ждать. Ну да ладно, я ведь знаю, что ты нас чем-нибудь порадуешь. Не буду отвлекать."
            hide captain
   
        "Есть что-то новое?":
            show cook at right
            cook "А то! Купила себе книжку рецептов с Фольмагаута в увольнении, и вот начала уже готовить."
            hide cook
            show captain at left
            captain "Раз такое дело, пойду-ка. Не буду мешать."
            hide captain
    
    label after_menu_kitchen:
        "Выйдя в коридор, капитан остановился. У него всё ещё оставалось несколько отсеков, которые ему нужно было посетить прежде, чем он отправится на мостик."
        show captain at left
        captain "Нужно еще проверить готовность у остальных, прежде чем идти на мостик."
        hide captain


# Ниже представлен тот самый случай, когда ивенты нельзя прописывать подряд, ибо они являются вариативными, и могут запускаться в произвольном порядке.

    menu Choice_Loop:
        "Куда пойти дальше?"

        "Идти в медпункт":
            jump clinic_ivent

        "Идти к технику":
            jump engineer_ivent

        "Идти в связную":
            jump server_room_ivent

        "Идти в оружейную":
            jump armory_room_event

#Сцена в медотсеке

    label clinic_ivent:
        scene bg clinic with dissolve
        "Из раскрытой двери в медостсек в коридор лился яркий резкий свет."
        "Приблизившись, капитан почувствовал лёгкий запах лекарств."
        "В медостсеке было пусто. Некоторые шкафы были распахнуты, а на одной из кушеток стоял раскрыты ящик."

        show captain at left
        captain "{i}Кажется, мне стоит посмотреть есть ли кто-то за шкафом.{/i}"
        hide captain
        "..."
        medic "Уже иду! Если это срочно, бинты в левом шкафу!"
        "..."
        medic "Почти пришёл!"
        "Из вторых дверей в глубине медотсека наконец-то показался медик."
        show medic at right
        medic "Капитан! Какими судьбами?"
        hide medic
        show captain at left
        captain "Предполетный обход. Все в порядке?"
        hide captain
        show medic at right
        medic "В полном."
        hide medic
        show captain at left
        captain "Лекарств хватает?"
        hide captain
        show medic at right
        medic "Разумеется."
        hide medic
        show captain at left
        captain "Техника в норме?"
        hide captain
        show medic at right
        medic "Еще бы!"
        hide medic
        show captain at left
        captain "Ты как?"
        hide captain
        show medic at right
        medic "Всё никак не дождусь возможности расстаться с твёрдой землёй под ногами."
        hide medic

    menu clinic:
        "Что еще сказать?"
            
        "Как твоя дочка то?":
            show medic at right
            medic "Позвонила вот на той неделе. Разговоры у нас всё не клеятся, но она хоть сама иногда меня проведывает теперь. И рассказывает, чем живёт. Сухо, но рассказывает. Про повышение, про друзей своих, про новые проекты – про них, конечно, больше всего."
            hide medic
            show captain at left
            captain "Вся в тебя, а?"
            hide captain
            show medic at right
            medic "Родная – и та больше похожа не была б."
            hide medic

        
        "Отправимся, как закончу обход" :
            pass
        
    label after_menu_clinic:
        "Капитан кивнул ему и, бросив последний взгляд на ящик на кушетке, отправился дальше"
        jump Choice_Loop

#Сцена в двигательном отсеке.
    
    label engineer_ivent :
        scene bg utility with dissolve
        "Поднимаясь по ступенькам к генератору, капитан почувствовал слабый запах гари."
        "За распахнутыми дверьми в дальнем углу огромного двигательного отсека сгорбилась фигура со сваркой в руках"
        show captain at left
        captain " Я надеюсь, ты не чинишь корабль перед отлетом?"
        hide captain
        "..."

        menu scream:
            "Что делать дальше?" 

            "Крикнуть":
                show captain at left
                captain "Я ГОВОРЮ С ЛЕЙТЕНАНТОМ ФРЕДЕРИККЕ ЭЙНСЛИ!"
                hide captain

            "Подождать":
                pass

        label after_menu_scream:
        "Сварка погасла. Женщина сняла маску, распрямилась и наконец-то обернулась к капитану"
        
        scene bg utility
        show engineer at right
        engineer " О, Кэп. И давно ты тут?"
        hide engineer
        show captain at left
        captain "Да не особо. Ты ведь не чинишь корабль прямо перед вылетом?"
        hide captain
        show engineer at right
        engineer "Что? Конечно, нет."
        hide engineer
        show captain at left 
        captain "Чем ты тогда тут занимаешься?"
        hide captain
        show engineer at right
        engineer "О, я просто решила укрепить двигатель. В прошлый раз мы попали в пространственную дыру, нас нехило потрясло."
        hide engineer
        show captain at left
        captain "Да, я помню."
        hide captain
        show engineer at right
        engineer "вот я и решила укрепить двигатель, что бы он смог вынести и более сильные тряски."
        hide engineer
        show captain at left
        captain " И ты делаешь это сейчас, потому что?.."
        hide captain
        show engineer at right
        engineer "Основные работы были сделаны до этого. Сейчас мне наконец-то доставили нужный каркас, который скроет крепежи."
        hide engineer
        show captain at left
        captain "Так ты просто делаешь красиво?"
        hide captain
        show engineer at right
        engineer "Ну, по сути да. Техника ведь должна быть красивой."
        hide engineer
        show captain at left
        captain "Не опасно? Она не отвалиться?"
        hide captain
        show engineer at right
        engineer "Ну, этот конкретный каркас не так важен. Главное, чтобы двигатель не отлетел. А он теперь не отлетит."
        hide engineer
        show captain at left
        captain "Ладно. Что по состоянию корабля?"
        hide captain
        show engineer at left
        engineer "Отчёт я отправила десять минут назад."
        hide engineer

        "Женщина надела маску, отвернулась и, вновь включив сварку, принялась работать."
        "Капитан отправился к выходу, по пути открыв свой планшет."
        "Он хмыкнул, отметив, что отчёт пришёл лишь несколькими минутами ранее."
        
        "Отчет о состоянии корабля"
        "Внешняя обшивка – 69 процента (сильный износ и множество повреждений. Необходима замена внешних слоев, пока это не привело к критическим значениям)"
        "Готовность к критическим ситуация – 6/10 (на данный момент внешняя обшивка может выдержать несколько средних ударов или пару пролетов через пространственные дыры. Далее передвижение на нем будет критически опасным)"
        "Внутренняя обшивка – 82 процента (в некоторых местах весьма изношена, но вполне пригодна для эксплуатации. Замены в ближайшее время не требуется)"
        "Генераторы – 89 процента (смена нескольких ступеней на современное топливо привела к увеличению мощности, укрепление крепежей привело к более устойчивому состоянию. Неизвестно, как поведет себя смесь двух жидкостей при экстремально высоких или низких температур.)"
        "Внутреннее оборудование – 94 процента (обновленное ПО, смена карт и ИИ модуля привела к улучшению работы внутреннего оборудования. Некоторые компоненты еще состыковываются, от этого происходит задержка общих уведомлений.)"
        "Общее состояние корабля – 79 процентов »"
        "{i}Одобрено к вылету по установленным безопасным маршрутам.{/i}"


        show captain at left
        captain " Вполне сносно для нашего задания."
        hide captain
        "Пояснений к отчёту не требовалось, поэтому капитан вышел из двигательного отсека и отправился дальше."
        jump Choice_Loop


#Сцена в переговорной

    label server_room_ivent:
        
        scene bg signal_room with dissolve
        
        "Переговорная была оборудована самой удобной и современной мебелью."
        "Сейчас, впрочем, и овальный стол, и большинство кресел были уставлены техникой."
        "За дальним концом, отвоевав себе немного свободного места, сидела небольшая девушка."
        "На ней была объёмная гарнитура и она, должно быть, даже не услышала шагов"

        show signal at right
        signal "Код 113. Повторяю, код 113."
        hide signal
        "Капитан сел в единственное свободное кресло, вздохнул, почувствовав невероятный комфорт"
        show signal at right
        signal "Альфа-57, Бета-25, как слышно?"
        signal "Отлично."
        signal "Заканчиваю связь"
        hide signal

        "Связистка сняла гарнитур, откинувшись на спинку кресла."
        show captain at left
        captain " Как дела?"
        hide captain
        show signal at right
        signal "Нейронные сети! Вы чего пугаете?!"
        hide signal

        menu server_room_choice:
            "Что ответить?"

            "Извиниться":
                show captain at left
                " Прости, думал, ты видела меня."
                hide captain
                show signal at right
                signal "Ничего страшного."
                hide signal
                show captain at left
                captain "Так как там подготовка?"
                hide captain

            "Перейти к делу":
                show captain at left
                "Я пришел убедиться в готовности."
                hide captain

        label after_server_menu_choice:
            show signal at right
            "Практически закончена! Осталось наладить связь между командой. А то не дело полагаться на личные частоты для работы."
            hide signal
        show captain at left
        captain "Лучше поторопись. Я почти закончил обход."
        hide captain
        show signal at right
        signal "Да,капитан."
        hide signal
        jump Choice_Loop

#Сцена в оружейной комнате

    label armory_room_event:
        scene bg armory_room with dissolve
        "В гробовой тишине оружейной лишь тихо потрескивала тусклая лампа над входом."
        show captain at left
        captain "Есть тут кто?"
        hide captain
        play music "audio/music/dangerous.mp3" 
        unknown "Какие предположения?"
        hide unknown
        "В самом далеком и темном углу сидел мужчина, протирая рукоятку бластера."
        show captain at left
        captain "От тебя не было сообщений."
        hide captain
        show secureman at right
        secureman "И должно быть, я испарился. Не работал же, в самом деле."
        hide secureman
        "Начальник безопасности повернулся спиной к капитану, убирая на место многочисленные принадлежности для чистки оружия." 
        "Капитан заметил в шкафу рядом с собой бластер."

        menu gun_ewent:
            "Что делать дальше?" 

            "Схватить бластер":
                show captain at left
                captain "Руки вверх!"
                hide captain
                show secureman at right
                secureman "..."
                hide secureman
                "Мичи замер. Повисла тишина."
                "В какую-то долю секунды начальник охраны уже оказался рядом, свободной рукой уведя бластер к потолку. Во второй же был начищенный бластер, который он прижал к голове капитана."
                show secureman at right
                secureman "Все готово капитан. {i}Ко всему{/i}."
                hide secureman
                show captain at left
                captain "Теперь вижу."
                hide captain

            "Не трогать":
                pass

        label after_gun_ewent:
            stop music fadeout 5
            show secureman at right
            secureman "Еще что-то?"
            hide secureman
            show captain at left
            captain " Нет. На этом все."
            captain "До связи."
            hide captain
            jump Choice_Loop