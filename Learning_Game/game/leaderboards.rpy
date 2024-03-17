screen leaderboars_menu(): # Экран "Достижения" в  главном меню.
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