default leaderboard_pers =  [(1000,"Ewe"), (750, "Tima")]

screen leaderboars_menu(): # Экран "Список лидеров" в главном меню.
    tag menu
    frame:
        align(0.5, 0.0)
        background None
        text "Список лидеров" size 50

    frame:
        xysize(400,480)
        pos(200,70)
        padding(10,10,10,10)
        vbox:
            text "Список чисто для вида" xalign 0.5 size 30
            hbox:
                vbox:
                    for score in leaderboard_pers:
                        hbox:
                            xsize 380
                            text score[1] xalign 0.0 size 24
                            text str(score[0]) xalign 1.0 size 24
                            