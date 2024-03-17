screen achievements_menu(): # Экран "Достижения" в  главном меню.
    tag menu
    use game_menu(""):
        vbox: 
            frame:
                style "empty"
                xmaximum 1920 ymaximum 920  
                viewport: # окно со скроллингом 
                    yinitial 0
                    scrollbars "vertical"
                    mousewheel True
                    draggable True     
                    frame:
                        style "empty"  
                        vbox:
                            spacing 8

init python: # Данные достижений в формате словаря. id: (иконка, заголовок, текст)
    achievements_data = {
        "achievement_id1": ("content/images/achievements/achievement.png", _("Игра начинается!"), _("За то, что начали игру.")),
        "achievement_id2": ("content/images/achievements/achievement.png", "Я есть грут!", "Теперь мы знаем, как вас зовут!") }

init -3 python: # Переменные для работы ачивок
    achievements_time = 4  # Сколько видна ачивка (в сек.)
    achievements_showtime = achievements_time *.2 # Скорость появления и исчезновения ачивки.
    achievements_height = 10 # Высота окна с ачивкой.
    achievements_width  = 700  # Ширина окна с ачивкой.
    achievements_outline = 10 # Толщина рамки окна ачивки.
    achievements_xspacing = 8 # Расстояние между заголовком и картинкой.
    achievements_yspacing = 2 # Отступ от заголовка до текста.
    achievements_round = 60   # Закругленность окна ачивки.
    achievements_color = "#128b" # Цвет фона окна ачивки.
    achievements_outlinecolor = "#fff" # Цвет рамки окна ачивки.
    achievements_text_color = "#fff" # цвет текста ачивки .
    achievements_caption_color = "#def" # цвет заголовка ачивки.

    if persistent.achievements is None:  # список полученных ачивок.
        persistent.achievements = []

init -2: # Фон окошка с ачивкой. 
 image achievements_background = Frame(Text( "🟢", color=achievements_color, font="DejaVuSans.ttf", size=achievements_round, outlines=[(achievements_outline, achievements_outlinecolor, 0, 0)]), int(achievements_round/2), int(achievements_round/2))

init python:
    def achievement(achievement_id): # Открыть ачивку с идентификатором achievement_id
        if achievement_id in persistent.achievements: # Если ачивка уже открыта, то ничего не делаем.
            return
        
        if not (achievement_id in persistent.achievements): 
            persistent.achievements.append(achievement_id)
           
            # получить данные ачивки
            img, caption, txt = achievements_data[achievement_id]
            # показать сообщение о получении ачивки
            renpy.show_screen("achievements_screen", img, caption, txt)

    Ach = renpy.curry(achievement) # превращаем функцию def в action, чтобы заново не рисовать окна, а просто выводить окно ачивок в виде action.

    def notify(txt, caption=None, img=None, xalign=1., xmaximum = achievements_width): # Функционал нотификаций.
        if renpy.get_screen("achievements_screen"):
            renpy.hide_screen("achievements_screen")
            renpy.pause(achievements_showtime)
        renpy.show_screen("achievements_screen", img, caption, txt, xalign) # показать сообщение
    Notify = renpy.curry(notify)

    def achievements_delete(achievement_id = None): # удаляем полученные ранее ачивки (выполняется при начале новой игры.)
        if achievement_id in persistent.achievements:
            persistent.achievements.remove(achievement_id)
        elif achievement_id is None: # если id == None, то удаляем все.
            persistent.achievements = []

init:
    style achievement_frame is frame: # стиль для окошка ачивки

        background "achievements_background" # фон окошка          
        xmaximum achievements_width  # размеры окошка по x
        yminimum achievements_height # размеры окошка по y
        xpadding achievements_round # внутренние отступы по x оси
        ypadding achievements_round # внутренние отступы по y оси
 
    style achievement_text is text: # стиль для текста ачивки

        bold False # делает текст неподчеркнутым
        size gui.text_size # размер текста (берется такой же размер, как в gui)
        
    style achievement_caption is achievement_text:  # стиль для заголовка ачивки

        bold True # делает текст подчеркнутым
        size gui.name_text_size # размер текста заголовка (берется такой же размер, как в gui).

    transform achievement_showhide_func(time = achievements_showtime): # показать/спрятать ачивку из-за верхнего края экрана (по умолчанию с правой стороны экрана)
        yalign .0 alpha 0 # положение сообщения об ачивке.
        on show: # условия ,выполняемые при появлении.
            yanchor 1.
            ease_back time alpha 1 yanchor .0

        on hide: # условия, выполняемые при исчезновении.
            ease_back time alpha 0 yanchor 1.

screen achievements_screen(img=None, caption=None, txt=". . .", xalign=1., xmaximum=achievements_width): # экран сообщения о получении ачивки
    timer achievements_time action Hide("achievements_screen") # таймер для убирания ачивки с экрана

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


    