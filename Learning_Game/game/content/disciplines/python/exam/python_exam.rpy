label python_exam_start:
    prepod_2 "Пора проходить тесты"
    $ exampoints = 0    #Переменная для сбора количества очков.
    jump test_1

#Само тестирование 
label test_1:
    scene bgs blackboard
    menu test_1_1:
        "Вопрос 1"

        "Правильный ответ":
            $ exampoints += 0.5 #Количество баллов, получаемое пользователем 
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


#Функция проверки набранных пользователем баллов

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