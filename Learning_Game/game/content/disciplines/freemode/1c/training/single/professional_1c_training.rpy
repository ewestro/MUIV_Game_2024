init:        
    $ exampoints = 0        #   Переменная ,в которую записывается количество набранных пользователем баллов.       
    $ attempts_counter = 2  # Количество попыток на прохождение теста
    $ les = 0              # Пермееные прохождения лекций
 



label professional_1c_training_start:
    show prepod_3 at left with dissolve
    prepod_3 "Добро пожаловать, [first_player]!"
    "Меня зовут ***, я преподователь 1С"
    if  les == 0:
        "Меня зовут ***, я преподователь 1С"
        "Вижу ты тут первый раз."
        "Сейчас я быстро введу тебя в курс дела."
        "Курс 1С расчитан на пять лекций и четыре теста с выпускным экзаменом."
        "Можешь переходить к первой лекции. Удачи!"
        jump professional_1c_lectures_one
    else:
        "Рада снова видеть тебя, [first_player]!"
        "Не буду тебя отвлекать разговорами, можешь продолжать свое обучение."
        menu les_task_menu:
            "Что Вы хотите продолжить?"

            "Лекции":
                jump lecture

            "Тесты":
                jump tasks

    hide prepod_3

label lecture: 
    menu list_lecture:
        "Начать лекцию"

        "Первая":
            jump professional_1c_lectures_one

        "Вторая":
            jump professional_1c_training_start

        "Третья":
            jump professional_1c_training_start

        "Четвертая":
            jump professional_1c_training_start

        "Пятая":
            jump professional_1c_training_start


label tasks:
    menu list_tasks:
        "Начать тест"

        "Первый":
            jump professional_1c_training_start

        "Второй":
            jump professional_1c_training_start

        "Третий":
            jump professional_1c_training_start

        "Четвертый":
            jump professional_1c_training_start

        "Экзамен":
            jump professional_1c_training_start

label professional_1c_lectures_one:
    "Фарту масти, собаке по пасти."
    $ les += 1
    jump  professional_1c_training_start
