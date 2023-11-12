init:
    image python_exam_task_1 =                     "content/disciplines/python/exam/exam_1/task_1/python_exam_task_1.png"
    image python_exam_task_1_blurred =             "content/disciplines/python/exam/exam_1/task_1/python_exam_task_1_blurred.png" # На данный момент, изображения блюрятся извне. 

label python_exam_start:
    prepod_2 "Пора проходить тесты"

    $ exampoints = 0    #Переменная ,в которую записывается количество набранных пользователем баллов.

label choice_exam_variant:
    menu choice_exam_variant_menu:
        "Выберите тип теста"
        
        "Текстовый тест":
            jump test_1

        "Тест с изображениями":
            jump test_with_images

# Текстовое тестирование

label test_1:
    scene bgs blackboard
    menu test_1_1:
        "Вопрос 1"

        "Правильный ответ":
            $ exampoints +=  0.5 #Количество баллов, выдаваемое пользователю за правильный ответ 
            jump test_1_2
    
        "Неправильный ответ":
            jump test_1_2

label test_1_2:
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

    scene python_exam_task_1_blurred with fade
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
    if exampoints < 1:
        scene  bgs fail with fade
        centered "К сожалению, вы не сдали экзамен"
    elif exampoints >= 2:
        scene black with fade
        centered "Поздравляем, вы сдали экзамен."
    else:
        scene black with fade
        centered "50/50"
return
  