init:        
    $ exampoints = 0        #   Переменная ,в которую записывается количество набранных пользователем баллов.       
    $ attempts_counter = 2  # Количество попыток на прохождение теста
    $ les1 = 0              # Пермееные прохождения лекций
    $ les2 = 0
    $ les3 = 0
    $ les4 = 0
    $ les5 = 0
    $ les = les1 + les2 + les3 + les4 + les5
    $ task1 = 0              # Пермееные прохождения тестов
    $ task2= 0
    $ task3 = 0
    $ task4 = 0
    $ task5 = 0
    $ task = task1 + task2 + task3 + task4 + task5
    $ prov = 0
    $ popitka_1 = 0
    $ popitka_2 = 0
    $ popitka_3 = 0
    $ popitka_4 = 0
    $ popitka_5 = 0

    



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
        

    jump  menu_1c

    hide prepod_3

label lecture_1c: 
    menu list_lecture:
        "Начать лекцию"

        "Первая":
            jump professional_1c_lectures_one

        "Вторая":
            jump professional_1c_lectures_two

        "Третья":
            jump professional_1c_training_start

        "Четвертая":
            jump professional_1c_training_start

        "Пятая":
            jump professional_1c_training_start


label tasks_1c:
    menu list_tasks:
        "Начать тест"

        "Первый":
            jump professional_1c_task_one

        "Второй":
            jump professional_1c_task_two

        "Третий":
            jump professional_1c_training_start

        "Четвертый":
            jump professional_1c_training_start

        "Экзамен":
            jump professional_1c_training_start

label menu_1c:
    menu menu_for_1c:
        "Что дальше?"

        "Лекции":
            jump lecture_1c

        "Тесты":
            jump tasks_1c
                
        "Прогресс курса":
            jump  professional_1c_progress

        "Результаты тестов":
            jump res

        "Меню предметов":
            jump choice_direction

label professional_1c_progress:
    show prepod_3 at left with dissolve
    "Давай взглянем на твои успехи"

    $ task1 = 0
    $ prov = 0
    $ popitka_1 = 0
    
    jump menu_1c          


label professional_1c_lectures_one:
    show prepod_3 at left with dissolve
    "Первая лекция курса 1С"
    "Для начала разберемся что такое 1С. Это фирма, разработавшая 1С:Предприятие. Основана она была в 1991 году Борисом и Сергеем Нуралиевым."
    "На данный момент она занимает лидирующие позиции в российском софтверном бизнесе благодаря своему суперпродукту 1С:Предприятие"
    "Система 1С:Предприятие предоставляет в распоряжение разработчику широкий набор объектов:  справочники, документы, регистры и т.д., и инструментов: встроенный язык программирования, механизм запросов, различные визуальные редакторы и конструкторы. "
    "Сама по себе 1С:Предприятие — это специализированная объектно-ориентированная система управления базами данных (СУБД), предназначенная для автоматизации деятельности предприятия."
    "Рассмотрим 1С:Предприятие подробнее. Как уже говорилось ранее, это система управления базами данных. К ним относятся Microsoft SQL Server, PostgreSQL, Oracle Database, IBM DB2 и файловой базой данных. "
    "Состоит «1С:Предприятие» из двух частей: технологической платформы и конфигурации. "
    "Технологическая платформа – это и среда разработки, и среда выполнения. Она содержит все инструменты разработки, а так же осуществляет работу уже готовых продуктов. Разработкой платформы занимается сама компания «1С»."
    "Конфигурация – это прикладные решения, которые работать сами по себе не смогут, для этого им необходима платформа. Фирмой 1С были разработаны типовые конфигурации: бухгалтерия, кадровый учет, управление торговлей и т.д.."
    "Более подробную информацию о конфигурации ты сможешь узнать на второй лекции"

    if  les1 == 0:
        $ les1 += 1
    else:
        $ les1 = les1

    menu choice:
        "Что дальше?"

        "Читать лекции дальше":
            jump  professional_1c_lectures_two

        "Решать тест":
            jump  professional_1c_task_one

        "Выйти в меню":
            jump  menu_1c


label professional_1c_lectures_two:
    pass


label professional_1c_task_one:
    if popitka_1 <= 2:

        if task1 > 0:
            $ prov = task1
            $ task1 = 0
        else:
            menu q1_1:
                "Это твоя [popitka_1] попытка решить тест"
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_2
                
                "Неправильный ответ":
                    jump q1_2

            menu q1_2:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_3
                
                "Неправильный ответ":
                    jump q1_3

            menu q1_3:
                "Вопрос второй"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_4

                "Неправильный ответ":
                    jump q1_4

            menu q1_4:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_5
                
                "Неправильный ответ":
                    jump q1_5

            menu q1_5:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_6
                
                "Неправильный ответ":
                    jump q1_6

            menu q1_6:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_7
                
                "Неправильный ответ":
                    jump q1_7

            menu q1_7:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_8
                
                "Неправильный ответ":
                    jump q1_8

            menu q1_8:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_9
                
                "Неправильный ответ":
                    jump q1_9

            menu q1_9:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1
                    jump q1_10
                
                "Неправильный ответ":
                    jump q1_10

            menu q1_10:
                "Вопрос"

                "Правильный ответ":
                    $ task1 += 1

                    if task1 > prov:
                        jump end_task1
                    
                    elif task1 < prov:
                        $ task1 = prov
                        jump end_task1
                    else: 
                        jump end_task1
                
                "Неправильный ответ":

                    if task1 > prov:
                        jump end_task1
                    elif task1 < prov:
                        $ task1 = prov
                        jump end_task1
                    else: 
                        jump end_task1

    else:
        jump ban

        
label ends_tasks_1c:
    menu end_task1:
        "Первый тест пройден на [task1]"

        "Перепройти тест (сохранится лучшая попытка)":  #багнуто работает, нужно разобратся
            $ popitka_1 += 1
            jump professional_1c_task_one

        "Выйти в меню":
            jump menu_1c    

        
label ban:
        "Вы уже два раза проходили этот тест"
        "Возвращаемся обратно в меню"
        jump menu_1c


label res:
        "Результаты пройденных тестов:"
        "Первый тест пройден на [task1]"
        "Второй тест пройден на [task2]"
        "Третий тест пройден на [task3]"
        "Четвертый тест пройден на [task4]"
        "Экзамен пройден на [task5]"


       
        jump menu_1c

label professional_1c_task_two:
    pass



