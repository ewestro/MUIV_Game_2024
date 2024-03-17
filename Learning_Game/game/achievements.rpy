screen achievements_menu(): # Экран "Достижения" в  главном меню.
    tag menu # если не использовать этот тэг, то после открытия окна достижений, с него невозможно будет переключиться на другие окна!
    use game_menu(""): # этот тэг подсказывает движку, что мы создаем элемент игрового меню.
        vbox: # создаем вертикальную "коробку".
            text "Достижения" size 50 # текст, отображаемый в коробке.
            frame: # создаем рамку.
                style "empty" # использовать пустую заготовку.
                xmaximum 1920 ymaximum 920  # максимальные размеры рамки.
                viewport: # окно со скроллингом 
                    mousewheel True # Делает страницу прокручиваемой.
                    scrollbars "vertical" # делает прокрутку вертикальной.   
                    draggable True # позволяет делать прокрутку, нажимая на саму рамку.
                    frame:
                        style "empty"
                        vbox:
                            spacing 10  # расстояние между достижениями.
                            for achievement_id in achievements_data.keys(): # условия для каждого достижения.
                                $ img, caption, txt = achievements_data[achievement_id]
                                button:
                                    style "achievement_frame"
                                    hbox: # горизонтальная "коробочка".
                                        yalign .5
                                        spacing achievements_xspacing
                                        null width achievements_xspacing
                                        if img:   # условия добавления картинки (если достижение изначально было с ним).      
                                            add img yalign .5
                                        # заголовок с текстом
                                        vbox:
                                            align (.5, .5)
                                            xfill True
                                            spacing achievements_yspacing
                                            if caption: # условия для заголовка
                                                text caption style "achievement_caption" color achievements_caption_color
                                           
                                            if txt: # условия для текста
                                                text txt style "achievement_text" color achievements_text_color
                                        
                                        null width achievements_xspacing  # отступ от правого края
                                    if not achievement_id in persistent.achievements: # если достижение не открыто, то оно будет прозрачным.
                                        at alpha(.10)


init python: # Данные достижений в формате словаря. id: (иконка, заголовок, текст)
    achievements_data = {
        "achievement_id1": ("content/images/achievements/achievement.png", _("Игра начинается!"), _("За то, что начали игру.")),
        "achievement_id2": ("content/images/achievements/achievement.png", _("Я есть грут!"), _("Теперь мы знаем, как вас зовут!")),
        "achievement_id3": ("content/images/achievements/achievement.png", _("Ух ты! Генераторы!"), _("За то, воспользовались генератором имен.")),}

init -3 python: # Переменные для работы достижений.
    achievements_time = 4  # Время показа Достижения (в сек.)
    achievements_showtime = achievements_time *.2 # Скорость появления и исчезновения достижения.
    achievements_height = 10 # Высота окна достижений.
    achievements_width  = 700  # Ширина окна достижений.
    achievements_outline = 10 # Толщина рамки окна достижений.
    achievements_xspacing = 8 # Расстояние между заголовком и картинкой.
    achievements_yspacing = 2 # Отступ от заголовка до текста.
    achievements_round = 60   # Закругленность окна достижений.
    achievements_color = "#128b" # Цвет фона окна достижений.
    notification_color = "#ffffe0"  #Цвет фона окна для оповещений.
    achievements_outlinecolor = "#fff" # Цвет рамки окна оповещений.
    achievements_text_color = "#fff" # цвет текста достижений .
    achievements_caption_color = "#def" # цвет заголовка достижений.

    if persistent.achievements is None:  # список полученных достижений.
        persistent.achievements = []

init -2: # Фоны окошка с достижениями и фон окна с уведомлениями.
 image achievements_background = Frame(Text( "🟢", color=achievements_color, font="DejaVuSans.ttf", size=achievements_round, outlines=[(achievements_outline, achievements_outlinecolor, 0, 0)]), int(achievements_round/2), int(achievements_round/2))

init python:
    def achievement(achievement_id): # Открыть достижение с идентификатором achievement_id
        if achievement_id in persistent.achievements: # Если достижение уже открыто, то ничего не делаем.
            return
        
        if not (achievement_id in persistent.achievements): # если достижение не открыто, добавляем его в список.
            persistent.achievements.append(achievement_id)
            img, caption, txt = achievements_data[achievement_id] # получить данные достижения.
            renpy.show_screen("achievements_screen", img, caption, txt) # показать сообщение о получении достижения

    Ach = renpy.curry(achievement) # превращаем функцию def в action, чтобы заново не рисовать окна, а просто выводить окно достижений в виде action.

    def notify(txt, caption=None, img=None, xalign=10, xmaximum = achievements_width): # Функционал уведомлений.
        if renpy.get_screen("achievements_screen"):
            renpy.hide_screen("achievements_screen")
            renpy.pause(achievements_showtime)
        renpy.show_screen("achievements_screen", img, caption, txt, xalign) # показать уведомление.
    Notify = renpy.curry(notify)

    def achievements_delete(achievement_id = None): # удаляем полученные ранее достижения (выполняется при начале новой игры.)
        if achievement_id in persistent.achievements:
            persistent.achievements.remove(achievement_id)
        elif achievement_id is None: # если id == None, то удаляем все.
            persistent.achievements = []

init: # Стили
    style achievement_frame is frame: # стиль для окошка достижений.

        background "achievements_background" # фон окошка          
        xmaximum achievements_width  # размеры окошка по x
        yminimum achievements_height # размеры окошка по y
        xpadding achievements_round # внутренние отступы по x оси
        ypadding achievements_round # внутренние отступы по y оси
 
    style achievement_text is text: # стиль для текста достижений.

        bold False # делает текст неподчеркнутым
        size gui.text_size # размер текста (берется такой же размер, как в gui)
        
    style achievement_caption is achievement_text:  # стиль для заголовка достижений.

        bold True # делает текст подчеркнутым
        size gui.name_text_size # размер текста заголовка (берется такой же размер, как в gui).

        
    transform alpha(alpha=.75): # прозрачность
        alpha alpha

    transform achievement_showhide_func(time = achievements_showtime): # показать/спрятать достижение с/в верхнего края экрана (по умолчанию с правой стороны экрана)
        yalign .0 alpha 0 # положение сообщения об достижении.
        on show: # условия ,выполняемые при появлении.
            yanchor 1.
            ease_back time alpha 1 yanchor .0

        on hide: # условия, выполняемые при исчезновении.
            ease_back time alpha 0 yanchor 1.

screen achievements_screen(img=None, caption=None, txt=". . .", xalign=1., xmaximum=achievements_width): # экран сообщения о получении достижения
    timer achievements_time action Hide("achievements_screen") # таймер для убирания достижения с экрана.

    window:
        style "empty" # пустое окно
        xalign xalign
        at achievement_showhide_func() # анимация срабатывает при появлении или исчезновении окна.
        frame:
            style "achievement_frame"
            xmaximum xmaximum
            hbox:
                yalign .5
                spacing achievements_xspacing # отступ по x
                null width achievements_xspacing # отступ по y
                if img:  # если была использована картинка, то добавить ее в угол.
                    add img yalign .5 
                
                vbox:  # заголовок с текстом
                    align (.5, .5)
                    xfill True
                    spacing achievements_yspacing
                    
                    if caption: # если заголовок
                        text caption style "achievement_caption" xalign .5 color achievements_caption_color
                    
                    if txt: # если текст
                        text txt style "achievement_text" xalign .5 color achievements_text_color
                
                null width achievements_xspacing # отступ от правого края


    