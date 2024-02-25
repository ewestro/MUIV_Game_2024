init:  
    $ task_1 = 0

label html_exam_start:
    show prepod_5 at right with dissolve 
    prepod_5 "Сейчас будем проходить тестирование по HTML. Надеюсь ты хорошо подготовился."
    hide prepod_5
label mobilka_task_one:

         menu w1:
                "Что такое HTML?"

                "Язык разметки":
                    $ task_1 += 1
                    pass
                
                "Скриптовый язык":
                    pass

                "Библиотека гипертекста":
                    pass

         menu w2:
                "HTML-документ может иметь расширения:"

                ".html или .htm":
                    pass 
                
                ".html или .txt":
                    $ task_1 += 1
                    pass 

                ".html":
                    pass 

         menu w3:
                "В HTML не существует … тэгов."

                "Парных":
                    pass 
                
                "Одиночных":
                    pass 

                "Тройных":
                    $ task_1 += 1
                    pass 

         menu w4:
                "Какие тэги делают шрифт текста жирным?"
                "Пиксели и миллиметры":
                    pass
                "Миллиметры и сантиметры":
                    pass
                "Пиксели и проценты":
                    pass
                    $ task_1 += 1

         menu w5:
                "Выберите код HTML, который бы создавал кнопку отправки заполненной формы. Имя кнопки – ОК."

                "<input type='OK' value='Submit'/>":
                    pass
                
                "<input type='Submit' value='OK'/>":
                    $ task_1 += 1
                    pass

                "<p> input type='Submit' value='OK'< /p>":
                    pass

         menu w6:
                "Какой тэг при создании страницы добавляет имя страницы, которое будет отображаться в строке заголовка в браузере пользователя?"

                "<title> … </title>":
                    $ task_1 += 1
                    pass 
                
                "<header> … </header>":
                    pass 

                "<body> … </body>":
                    pass

         menu w7:
                "Что содержит в себе атрибут href?"

                "URL страницы, на которую произойдет перенаправление":
                    $ task_1 += 1
                    pass
                
                "Имя страницы, на которую произойдет перенаправление":
                    pass 

                "Указание на то, где будет открываться новая страница: в том же или новом окне":
                    pass 

         menu w8:
                "Какие из перечисленных тэгов относятся к созданию таблицы?"

                "<header> <body> <footer>":
                    pass 
                
                "<table> <tr> <td>":
                    $ task_1 += 1
                    pass 

                "<ul> <li> <tr> <td>":
                    pass 

         menu w9:
                "Укажите тэг, который соответствует элементу списка:"

                "<li>":
                    $ task_1 += 1
                    pass 
                
                "<ul>":
                    pass 

                "<ol>":
                    pass 

         menu w10:
                "Какие тэги делают шрифт текста жирным?"
                "<ins> и <del>":
                    pass
                "<li> и <ul>":
                    pass
                "<b> и <strong>":
                    pass
                    $ task_1 += 1

show prepod_5 at right with dissolve 
prepod_5 "Отлично! Первый тест пройден на [task_1] баллов из 10. Теперь можно идти дальше."
hide prepod_5

label ends_tasks_html:
    menu end_task_1:     
        "Выйти в меню":
            jump choice_direction # Меню выбора дисциплины для одиночной игры