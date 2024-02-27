init:
    image python_exam_task_1 =                     "content/disciplines/python/exam/exam_1/task_1/python_exam_task_1.png"
    image python_exam_task_1_blurred =             "content/disciplines/python/exam/exam_1/task_1/python_exam_task_1_blurred.png" # На данный момент, изображения блюрятся извне. 
    $ exampoints = 0    #   Переменная ,в которую записывается количество набранных пользователем баллов.
    $ attempts_counter = 2 # Количество попыток на прохождение теста

label python_exam_start:
    prepod_2 "Пора проходить тестирование"

label choice_exam_variant:  # Выбор типа экзамена
    menu choice_exam_variant_menu:
        "Выберите тип теста:"
        
        "Текстовый тест":
            jump test_1

        "Тест с изображениями":
            jump test_with_images

        "Скрытый режим" if persistent.secret_unlocked:
            jump secretmode

        "Разблокировать скрытый режим":
            $ persistent.secret_unlocked = True

            "Режим разблокирован"
            jump choice_exam_variant_menu

        "Заблокировать скрытый режим":
            $ persistent.secret_unlocked= False

            "Режим заблокирован"
            jump choice_exam_variant_menu

        "Тест с ограничением попыток":
            jump limited_counter_test

label limited_counter_test: # Тест с ограничением попыток
    while attempts_counter >1:
        $attempts_counter -= 1
        "У вас осталось попыток: [attempts_counter]."
        jump choice_exam_variant
    "Попытки закончились."
    jump choice_exam_variant

label secretmode:
    "Поздравляем, вы открыли секретный режим."
    jump choice_exam_variant


# Текстовое тестирование

label test_1:   #Задание 1
    scene bgs blackboard
    menu test_1_1:
        "Вопрос 1"
        
        "Какая из следующих функций преобразует строку в список в Python?"
        
        "List(mystring)":
            $ exampoints +=  0.5 #Количество баллов, выдаваемое пользователю за правильный ответ 
            jump test_1_2
    
        "Eval(mystring)":
            jump test_1_2

        "Repr(mystring)":
            jump test_1_2

        "Tuple(mystring)":
            jump test_1_2

label test_1_2: #Задание 2
    menu test_1_2_1:
        "Вопрос 2"
        
        "Неправильный ответ":
            jump test_1_3

        "Правильный ответ":
            $ exampoints += 1.5
            jump test_1_3
    

label test_1_3: # И т.д до бесконечности
    menu test_1_3_1:
        "Последний Вопрос"

        "Правильный ответ":
            $ exampoints +=1
            pass

        "Неправильный ответ":
            pass
jump scoring


# Тестирование с изображениями
label test_with_images:
if not persistent.imagetest_unlocked: # Ограничение на доступ с параметром.
    scene black with fade
    centered "Чтобы Разблокировать данный режим, завершите текстовый тест "
    jump choice_exam_variant
    scene python_exam_task_1_blurred with fade
else:
    
    "Какой результат выдаст выполнение данного кода"
    menu:
        "{image=content/disciplines/python/exam/exam_1/task_1/python_exam_task_1.png}":
            "Правильный ответ"
            $ exampoints +=1
            pass
            
        "{image=content/disciplines/python/exam/exam_1/task_1/python_exam_task_1.png}":
            "Неправильный ответ"
            pass


#Функция проверки набранных пользователем баллов
label scoring:
    if exampoints <= 1:
        scene  bgs fail with fade
        centered "К сожалению, вы не сдали экзамен"
        $ persistent.imagetest_unlocked = False

    elif exampoints >= 2:
        scene black with fade
        centered "Поздравляем, вы сдали экзамен."
        $ persistent.imagetest_unlocked = True

    else:
        scene black with fade
        centered "Удовлетворительно"
        $ persistent.imagetest_unlocked = True

$ exampoints= 0

jump choice_exam_variant
 
