from function import (
    delete,
    add,
    change,
    printdata,
    clear,
    loading,
    check_numbers,
    terminate,
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

greeting_message = """\
***************************  \
Добро пожаловать!  \
***************************"""

answer_error = """\
ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n
Введите значение от 1 до 6."""

separator = "___________________________"
input_prompt = "Введите номер действия: "
delete_confirmation_message = "Данные успешно удалены!"
farewell_message = "Всего доброго!"


def interface():
    print(greeting_message)
    print(menu)
    print(separator)

    answer = request_answer()
    loading()

    while answer != 6:
        if answer == 1:
            delete()
        elif answer == 2:
            add()
        elif answer == 3:
            change()
        elif answer == 4:
            printdata()
        elif answer == 5:
            clear()
        print(menu)
        print(separator)
        answer = request_answer()

    print(separator)
    answer = input(delete_prompt)
    print(separator)

    if answer.lower() in ["да", "yes"]:
        terminate()
        print(delete_confirmation_message)

    print(farewell_message)
    exit()


def request_answer():
    answer = int(input(input_prompt))

    while not check_numbers(answer):
        print(answer_error)
        print(menu)
        print(separator)
        answer = int(input(input_prompt))

    return answer
