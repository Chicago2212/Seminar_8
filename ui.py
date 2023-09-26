import sys
import time

import function

menu = """\
Выберите действие:
___________________________
1. Удалить запись.
2. Добавить запись.
3. Изменить запись.
4. Вывести данные.
5. Очистить файл.
6. Выход."""

change_prompt = """\
Отлично! Выбери данные, которые Вы хотите поменять:
1 - Имя,
2 - Фамилия,
3 - Телефон,
4 - Город
Примечание: Если Вы хотите изменить несколько данных одновременно,\
то запишите номера через пробел.
Ввод: """

parameters_prompts = [
    "Введите имя: ",
    "Введите фамилию: ",
    "Введите номер телефона: ",
    "Введите город: ",
    "Введите разделитель(  - . ; ,  ): ",
]

delete_prompt = """\
Желаю всего доброго! \
Не забывай, что все данные, которые ты записал, они сохранились.
Удалить? (ОТВЕТЬТЕ ДА/НЕТ): """

greeting_msg = """\
***************************  \
Добро пожаловать!  \
***************************"""

farewell_msg = "Всего доброго!"

answer_error = "ERROR! Ошибка, скорее всего, Вы указали неправильное число."
action_answer_err = "Введите значение от 1 до 6." ""
file_answer_err = "Введите номер файла от 1 до 3: "

underscores = "___________________________"

action_prompt = "Введите номер действия: "
file_delete_prompt = "Выберите из какого файла Вы хотите удалить данные: "
file_clear_prompt = "Выберите какой файл Вы хотите очистить: "
file_add_prompt = "Выберите файл, в который Вы хотите добавить строку: "
file_change_prompt = "Выберите в каком файле Вы хотите изменить запись: "
file_choice_msg = "Отлично! Будем {action} данные из {file_num}-файла."
line_prompt = "{action} номер строки от 1 до {line_count}: "

success_msg = "Данные успешно {action}!"
del_success_msg = "Удаление успешно завершено!"
file_clear_msg = "Отлично! Происходит очистка файла, подождите :)"
clear_success_msg = "Файл {file_num} успешно очищен!"
print_msg = "Вывожу данные из {i}-го файла:"


def interface():
    print(greeting_msg, menu, underscores, sep="\n")

    action = choose_action()

    while action != 6:
        if action == 1:
            delete()
        elif action == 2:
            add()
        elif action == 3:
            change()
        elif action == 4:
            function.print_data()
        elif action == 5:
            clear()
        print(menu, underscores, sep="\n")
        action = choose_action()

    print(underscores)
    action = input(delete_prompt)
    print(underscores)

    if action.lower() in ["да", "yes"]:
        function.clear_all_files()
        print(success_msg.format(action="удалены"))

    print(farewell_msg)
    exit()


def choose_action():
    answer = int(input(action_prompt))
    loading()

    while answer < 1 or answer > 6:
        print(answer_error, action_answer_err, menu, underscores, sep="\n")
        answer = int(input(action_prompt))
        loading()

    return answer


def choose_file(prompt, action):
    print(underscores)
    answer = int(input(prompt))

    while answer < 1 or answer > 3:
        print(underscores, answer_error, sep="\n")
        answer = int(input(file_answer_err))
        loading()

    if action != "":
        print(
            underscores,
            file_choice_msg.format(action=action, file_num=answer),
            sep="\n",
        )

    return answer


def choose_line(file_num):
    line_count = len(function.read_file(file_num))
    prompt = line_prompt.format(action="Выбери", line_count=line_count)
    line = int(input(prompt))

    while line < 1 or line > line_count:
        prompt = line_prompt.format(action="Введите", line_count=line_count)
        print(answer_error)
        line = int(input(prompt))

    return line


def delete():
    function.print_data()
    file_num = choose_file(file_delete_prompt, "удалять")
    line = choose_line(file_num)
    function.delete_line(file_num, line)

    print(underscores, del_success_msg, sep="\n")


def add():
    function.print_data()
    file_num = choose_file(file_add_prompt, "")
    parameters = choose_add_parameters()
    function.add_to_file(file_num, parameters)

    msg = success_msg.format(action="записаны")
    print(underscores, msg, sep="\n")


def choose_add_parameters():
    print(underscores, "|", sep="\n")

    answers = list()
    for prompt in parameters_prompts:
        print("|")
        answers.append(input("| " + prompt))

    return answers


def change():
    function.print_data()

    file_num = choose_file(file_change_prompt, "изменять")
    line = choose_line(file_num)
    values = choose_new_values()
    function.change_line(file_num, line, values)

    msg = success_msg.format(action="изменены")
    print(underscores, msg, sep="\n")


def choose_new_values():
    values = list()
    fields = [0]

    while min(fields) < 1 or max(fields) > 4:
        print(underscores)
        fields = list(map(int, input(change_prompt).split()))

    for i in range(4):
        if i + 1 in fields:
            answer = input(parameters_prompts[i])
        else:
            answer = ""
        values.append(answer)

    return values


def clear():
    function.print_data()
    file_num = choose_file(file_clear_prompt, "")
    print(underscores, file_clear_msg, sep="\n")
    function.clear_file(file_num)
    loading()
    msg = clear_success_msg.format(file_num=file_num)
    print(underscores, msg, sep="\n")


def loading():
    animation = [
        "■□□□□□□□□□",
        "■■□□□□□□□□",
        "■■■□□□□□□□",
        "■■■■□□□□□□",
        "■■■■■□□□□□",
        "■■■■■■□□□□",
        "■■■■■■■□□□",
        "■■■■■■■■□□",
        "■■■■■■■■■□",
        "■■■■■■■■■■",
    ]

    for i in range(len(animation)):
        sys.stdout.write(animation[i] + f" {(i + 1) * 10}%\r")
        sys.stdout.flush()
        time.sleep(0.01)

    print("\n")


def print_data():
    print(underscores, )
