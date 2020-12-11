# ReadMe
В данной папке собраны 3 тестовые задачи

Файлы распологаются по адресу: https://github.com/Stanislov/test_tasks/tree/main/test_parsing

## Задача 1. Файл login.py.
Написана функция для проверки выполнения правил вводимого логина.

Остальные примеры так же бы имели 1 цикл и изменялась последовательность действий и условий (тот же while с перебором символов).

Выводы: их отличие в последовательности шагов, сходство в цикле с перебором каждой буквы логина
 
## Задача 2. Файл test.py
В данном файле добавлено два теста. Для большего количества файлов-тестов создана папка test
 
## Задача 3. Файл events_parsing.py
Здесь написан парсер для просмотра мероприятий, опубликованных на сайте.

Текущий и следующий месяц помещены в переменные "m1" и "m2" (это 12 и 1)

Для запуска файла понадобятся библиотеки bs4, lxml

Для просмотра через докер достаочно ввести команду в linux-e:
### docker run stanislov/my_app_parsing