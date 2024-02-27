init:
    $ python_timegame_counter = 0  # Количество набранных за игру очков.
    $ python_timegame_attempts = 2 # Количество попыток 

label python_attempts_checkout:
    if python_timegame_attempts == 2:
        jump python_timegame_intro
    elif python_timegame_attempts == 1:
        jump python_timegame_start
    else:
        "Попытки закончились"
        jump python_training_start

label python_timegame_intro:
    show prepod_2 at left
    prepod_2 "Давай сыграем на время: успей ответить  все вопросы, пока таймер не истек."
    prepod_2 "Обрати внимание на то, что правильный ответ будет прибавлять время на таймере, а неправильный ,наоборот, отнимать."

label python_timegame_start:
    if  gender_male == True:
        "Готов сыграть?"
    else:
        "Готова сыграть?"
    hide prepod_2

label python_timegame_ready_or_not:
    menu python_timegame_ready_or_not_menu:
        "Осталось попыток: [python_timegame_attempts]. Начнем?"

        "Да":
            $ python_timegame_attempts -= 1
            $ python_timegame_counter = 0

        "Нет":
            "Очень жаль. Наверное, испугался?"
            jump python_gamemode_choice
        "Посмотреть последний результат":
            jump python_timegame_lastgame

label python_qte_test_1:   #Тестирование  1
    $ time = 60
    $ numeral_timer_menu = True
    
    scene bg_blackboard

    menu python_qte_test_1_1:
        "Какая команда отвечает за вывод информации на экран?"

        "print":
            $ python_timegame_counter += 1 
            $ time += 10
            pass
        "if":
            $ time -=10
            pass
        "for":
            $ time -=10
            pass
           
    menu python_qte_test_1_2:
        "Какая команда отвечает за ввод числа с клавиатуры?"

        "print()":
            $ time -=10
            pass
        "while":
            $ time -=10
            pass
        "int(input())":
            $ python_timegame_counter += 1
            $ time += 10
            pass

    menu python_qte_test_1_3:
        "Сколько библиотек можно импортировать в один проект?"

        "Не более 3":
            $ time -=10
            pass
        "Неограниченное количество":
            $ time +=10
            $ python_timegame_counter += 1 
            pass
        "Не более 10":
            $ time -=10
            pass

    $ horizontal_menu = False
    
    menu python_qte_test_1_4:
    
        "Какая программа выведет заданное пользователем число в обратном порядке?"

        "{image=content/disciplines/freemode/python/time_game/single/imagetasks/image1.png}":
            
            pass
        "{image=content/disciplines/freemode/python/time_game/single/imagetasks/image2.png}":
            $ python_timegame_counter += 1
            $ time += 10
            pass
        "{image=content/disciplines/freemode/python/time_game/single/imagetasks/image3.png}":  
            pass

if time ==0:
    label timeout_marker:
        "Время вышло."

label end:
    "Тест завершен, вы набрали [python_timegame_counter] баллов из 4."
    $ numeral_timer_menu = False
    
    jump python_training_start

label python_timegame_lastgame:
    "Последний результат: [python_timegame_counter]"
    jump python_timegame_ready_or_not