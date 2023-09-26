from function import (
    delete_line,
    add,
    change,
    printdata,
    clear,
    loading,
    terminate,
    read_file,
)

menu = """\
Выберите действие:
___________________________
1. Удалить запись.
2. Добавить запись.
3. Изменить запись.
4. Вывести данные.
5. Очистить файл.
6. Выход."""

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
delete_confirm_msg = "Данные успешно удалены!"


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
            printdata()
        elif action == 5:
            clear()
        print(menu, underscores, sep="\n")
        action = choose_action()

    print(underscores)
    action = input(delete_prompt)
    print(underscores)

    if action.lower() in ["да", "yes"]:
        terminate()
        print(delete_confirm_msg)

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


def choose_file(prompt):
    print(underscores)
    answer = int(input(prompt))

    while answer < 1 or answer > 3:
        print(underscores, answer_error, sep="\n")
        answer = int(input(file_answer_err))
        loading()

    return answer


def choose_line(line_count):
    line = int(input(f"Выбери номер строки от 1 до {line_count}: "))

    while line < 1 or line > line_count:
        print(answer_error)
        line = int(input(f"Введите номер строки от 1 до {line_count}: "))

    return line


def delete():
    success_msg = "Удаление успешно завершено!"

    printdata()
    file_num = choose_file(file_delete_prompt)
    print(
        underscores,
        f"Отлично! Будем удалять данные из {file_num}-файла.",
        sep="\n",
    )
    line_count = len(read_file(file_num))
    line = choose_line(line_count)
    delete_line(file_num, line)

    print(underscores, success_msg, sep="\n")
