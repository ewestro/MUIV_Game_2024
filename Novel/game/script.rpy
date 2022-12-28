
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
    stop music fadeout 5
    scene bg port with dissolve
    "Корабль, пришвартованный у самого края провинциального космопорта, ничем не выделялся на фоне окружающего пейзажа."
    "Потрепанная металлическая обшивка сливалась с серыми панелями стен, пустые иллюминаторы едва отражали тусклый свет."
    "Когда-то эта модель была образцом грузового транспорта, но теперь от её былой славы остались лишь полуоблупившиеся и поблекшие языки пламени, нарисованные по бокам корабля."
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
            "Капитан сразу же направился вглубь корабля."


# Сцена в коридоре/палубе
    play sound "audio/ivent_sounds/step_metal_slow.wav"
    scene bg corridor with dissolve
    "Палуба встретила капитана тусклым дежурным освещением. В коридоре его уже ждала старшая помощница."
    "Она барабанила пальцами по планшету в нетерпении и казалась весьма бодрой, несмотря на ранний час."
    show captain at left
    captain "Все хорошо?"
    hide captain
    show firstman at right
    stop sound
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
    "Он встрепенулся раньше, чем капитан успел его окликнуть."

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
    "Капитан достал коммуникатор и, не глядя, набрал частоту координатора."
    show captain at left
    captain " Вега. Путь будет спокойным."
    hide captain
    "Не получив точного ответа на свой вопрос, рулевой недовольно скривился."
    show captain at left
    captain "Я уже отправил координаты."
    hide captain
    show secondman at right
    secondman "Тогда иди, заканчивай свой осмотр."
    hide secondman
    "Рулевой расслабился, откинувшись на спинку дивана, и махнул рукой."


#Сцена на кухне
    scene bg kitchen with dissolve
    "Следующей остановкой в списке была кухня."
    play sound "audio/ivent_sounds/tableware_move.wav"
    "При приближении доносились звуки посуды. Видимо, кок принялся разбирать ящики."

    show captain at left
    captain " Могу поинтересоваться, как все подготовлено?"
    hide captain
    play sound "audio/ivent_sounds/tableware_drop.wav"
    show cook at right
    cook " Ох ты ж!"
    hide cook
    "Кок недовольно повернулась лицом к двери, уперев руки в бока, и тут же просияла, увидев капитана."
    show cook at right
    cook "Капитан, ты ко времени! Все готово.. Провиант в кладовой иль холодной. А я уж в мылу, разбираю утварь."
    hide cook
    
    menu kitchen:
        "Что спросить?"
  
        "Будет что-то вкусненькое?":
            show cook at right
            cook "А что, старое было не по нраву? "
            hide cook
            show captain at left
            captain "Да я не то имел ввиду…"
            hide captain
            show cook at right
            cook "Шучу-шучу. Все будет, но позже."
            hide cook
   
        "Есть что-то новенькое?":
            show cook at right
            play sound "audio/ivent_sounds/tableware_stand.wav"
            cook "А как же! Смотри, какие новые тарелки прикупила! Будет в них горячее!"
            hide cook
            show captain at left
            captain "Да в такой красоте и кушать жалко. "
            hide captain
            show cook at right
            cook "Ничего, за две щеки уплетать будете."
            hide cook
    
    label after_menu_kitchen:
        show captain at left
        captain "Ну ладно, не буду мешать, пойду дальше. "
        hide captain
        "Выйдя в коридор, капитан остановился. У него всё ещё оставалось несколько отсеков, которые нужно было посетить прежде, чем корабль можно будет объявить готовым к отлёту."
        show captain at left
        captain "{i} Нужно еще проверить готовность у остальных, прежде чем идти на мостик. {/i}" 
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
        "Из раскрытой двери в медотсек в коридор лился яркий резкий свет."
        "Приблизившись, капитан почувствовал лёгкий запах лекарств и стерильности."
        "В медотсеке было пусто. Некоторые шкафы были распахнуты, а на одной из кушеток стоял раскрытый ящик."
        show captain at left
        captain "{i}Кажется, мне стоит посмотреть, есть ли кто-то за шкафом.{/i}"
        hide captain
        "..."
        play sound "audio/ivent_sounds/step_metal_medium.wav"
        medic "Уже иду! Если это срочно, бинты в левом шкафу!"
        "..."
        medic "Почти пришёл!"
        stop sound fadeout 5
        "Из вторых дверей в глубине медотсека наконец-то показался медик."
        show medic at right
        medic "Капитан! Какими судьбами?"
        hide medic
        show captain at left
        captain "Предполетный обход."
        hide captain
        show medic at right
        medic "Каждый раз одно и тоже."
        hide medic
        show captain at left
        captain "Так спокойнее. Все в порядке?"
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
        medic "Еще бы! Я сразу же сообщаю, если что-то не так. И рапортов я давно не отправлял."
        hide medic
        show captain at left
        captain "Знаю-знаю. Сам-то как?"
        hide captain
        show medic at right
        medic "Жду отлета. Хочу поскорее расстаться с твёрдой землёй под ногами."
        hide medic

    menu clinic:
        "Что еще сказать?"
            
        "А дочка твоя как?":
            show medic at right
            medic "Позвонила на той неделе. Разговоры с трудом клеятся."
            medic "Но теперь сама иногда меня проведывает. Рассказывает, чем живёт. Суховато, правда."
            hide medic
            "Медик криво усмехнулся."
            show captain at left
            captain "Кого-то мне это напоминает."
            hide captain
            show medic at right
            medic "Сам знаю. Да ты иди, еще дел полно. Чай, не весь корабль обошел."
            hide medic
            show captain at left
            captain "Друга проведать есть пару минут. Я ж вижу, что ты о малой поговорить хочешь."
            hide captain
            show medic at right
            medic "Малая… Да какая она уже малая."
            medic " А про что она может со мной поговорить? Про коллег, про повышение. У нее теперь новые проекты. Про них она больше всего и говорила."
            hide medic
            show captain at left
            captain "Вся в тебя…"
            hide captain
            show medic at right
            medic "Ну а как иначе? Кровь-то одна. Третья положительная. Хех."
            hide medic
        "Отправимся, как закончу обход" :
            pass
        
    label after_menu_clinic:
        show captain at left
        captain "Ну да ладно, не буду задерживаться. Быстрее обойду, быстрее полетим."
        hide captain
        "Капитан кивнул ему и, бросив последний взгляд на ящик на кушетке, отправился дальше."
        jump Choice_Loop

#Сцена в двигательном отсеке.
    
    label engineer_ivent :
        scene bg utility with dissolve
        "Поднимаясь по ступенькам к генератору, капитан почувствовал слабый запах гари."
        "За распахнутыми дверьми в дальнем углу огромного двигательного отсека сгорбилась фигура со сваркой в руках."
        show captain at left
        captain " Я надеюсь, ты не чинишь корабль перед отлетом?"
        hide captain
        play sound "audio/ivent_sounds/welding.wav"
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
        "Сварка погасла. Женщина сняла маску, распрямилась и наконец-то обернулась к капитану."
        
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
        captain "Тогда чем ты тут занимаешься?"
        hide captain
        show engineer at right
        engineer "О, я просто решила укрепить двигатель. В прошлый раз мы попали в пространственную дыру, нас нехило потрясло."
        hide engineer
        show captain at left
        captain "Да, я помню."
        hide captain
        show engineer at right
        engineer "Вот я и решила укрепить двигатель, чтобы он смог вынести и более сильные тряски."
        hide engineer
        show captain at left
        captain " И ты делаешь это сейчас, потому что?..."
        hide captain
        show engineer at right
        engineer "Основные работы уже были сделаны до этого. Сейчас мне наконец-то доставили нужный каркас, который скроет крепежи."
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
        show engineer at right
        engineer "Отчёт я отправила десять минут назад."
        hide engineer
        show captain at left 
        captain "Тогда не буду отвлекать."
        hide captain
        show engineer at right
        engineer "Говоря об отчёте…"
        hide engineer
        show captain at left 
        captain "Что там?"
        hide captain
        show engineer at right
        engineer "Корабль уже плох."
        hide engineer
        show captain at left 
        captain "Цифры плохие?"
        hide captain
        show engineer at right
        engineer "Да нет. Цифры-то в норме. Но я бы не была столь оптимистична."
        hide engineer
        "Техник замолкла и только сильнее нахмурилась."
        show captain at left 
        captain "Говорите, лейтенант. "
        hide captain
        show engineer at right
        engineer " Он уже давно летает. Много переделок и починок пережил."
        hide engineer
        show captain at left 
        captain "И мы знаем его сильные и слабые стороны."
        hide captain
        show engineer at right
        engineer "Только слабостей теперь больше. Посмотрим, как приживутся последние новшества…"
        hide engineer
        show captain at left
        captain "И о каком-то конкретном «но» хочешь сообщить? "
        hide captain
        show engineer at right
        engineer "Да о таком, что всему старому пора на покой. Рано или поздно. И уж лучше рано,чем..."
        hide engineer
        "Капитан заметно помрачнел."
        show engineer at right
        engineer "Я залатала внешнюю оболочку, но этого недостаточно. Ее надо менять. Да только каркас может не выдержать."
        hide engineer
        show captain at left
        captain "Уверен, все не так плачевно. Ты любишь все драматизировать."
        hide captain
        show engineer at right
        engineer "Ну, капитан, тебе виднее."
        hide engineer

        "Женщина надела маску, отвернулась и, вновь включив сварку, принялась работать."
        "Капитан отправился к выходу, по пути открыв свой планшет."
        "Он хмыкнул, отметив, что отчёт пришёл лишь несколькими минутами ранее."
        
        "Отчет о состоянии корабля"
        "Внешняя обшивка – 69 процентов (сильный износ и множество повреждений. Необходима замена внешних слоев, пока это не привело к критическим значениям)"
        "Готовность к критическим ситуация – 6/10 (на данный момент внешняя обшивка может выдержать несколько средних ударов или пару пролетов через пространственные дыры. Далее передвижение на нем будет критически опасным)"
        "Внутренняя обшивка – 82 процента (в некоторых местах весьма изношена, но вполне пригодна для эксплуатации. Замены в ближайшее время не требуется)"
        "Генераторы – 89 процентов (смена нескольких ступеней на современное топливо привела к увеличению мощности, укрепление крепежей привело к более устойчивому состоянию... "
        "Неизвестно, как поведет себя смесь двух жидкостей при экстремально высоких или низких температурах."
        "Внутреннее оборудование – 94 процента (обновленное ПО, смена карт и ИИ модуля привела к улучшению работы внутреннего оборудования..."
        "Некоторые компоненты еще состыковываются, от этого происходит задержка общих уведомлений."
        "Общее состояние корабля – 79 процентов"
        "{i}Одобрено к вылету по установленным безопасным маршрутам.{/i}"
        show captain at left
        captain " Вполне сносно для нашего задания."
        hide captain
        "Пояснений к отчёту не требовалось, поэтому капитан вышел из двигательного отсека и отправился дальше."
        jump Choice_Loop


#Сцена в переговорной

    label server_room_ivent:
        
        scene bg signal_room with dissolve
        
        "Переговорная представляла собой узкую длинную комнату, вдоль стен которой висела техника."
        "На противоположном её конце, отвоевав себе немного свободного места, сидела молодая девушка."
        "На ней была объёмная гарнитура и она, должно быть, даже не услышала шагов"

        show signal at right
        signal "Код 113. Повторяю, код 113."
        hide signal
        "Капитан сел в единственное свободное кресло, вздохнул, почувствовав невероятный комфорт."
        show signal at right
        signal "Альфа-57, Бета-25, как слышно?"
        signal "Отлично."
        signal "Омега-13, как слышно?"
        signal "Отлично."
        signal "Заканчиваю связь."
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
            "Практически закончила. Осталось наладить связь между командой. А то не дело полагаться на личные частоты для работы."
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
        play music "audio/music/dangerous.wav" 
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
                play audio "audio/ivent_sounds/gun_ready.wav" 
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