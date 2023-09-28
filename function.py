separator = ['.', ';', ',', '-']


def data_transfer():
    printdata()
    answer_from = int(input('___________________________\n'
                            'Выберите из какого файла Вы хотите перенести данные данные: '))

    flag = True
    while flag:
        while answer_from < 1 or answer_from > 3:
            answer_from = int(input('___________________________\n'
                                    'ERROR! Ошибка, скорее всего, Вы указали неправильное число или файл пустой.\n'
                                    'Введите номер файла от 1 до 3: '))
        with open(f'db/data{answer_from}.txt', 'r') as from_file:
            data = from_file.readlines()
        if not data:
            answer_from = int(input('___________________________\n'
                                    'ERROR! Ошибка, скорее всего, Вы указали пустой файл.\n'
                                    'Введите номер файла от 1 до 3: '))
        else:
            flag = False
    answer_in = int(input('___________________________\n'
                          'Выберите в какой файл Вы хотите перенести данные: '))
    while answer_in < 1 or answer_in > 3 or answer_in == answer_from:
        answer_in = int(input('___________________________\n'
                              'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                              f'Введите номер файла от 1 до 3 кроме {answer_from}: '))
        loading()

    for i in range(len(data)):
        add(answer_in, data[i])
    delete(answer_in)
    clear(answer_from)
    loading()
    print('___________________________\n'
          'Данные успешно перенесены!')


def data_remake(data):
    global separator
    index_separator = data.split(separator[[i in data for i in separator].index(True)])
    return index_separator


def delete(answer=None):
    if not answer:
        printdata()
        answer = int(input('___________________________\n'
                           'Выберите из какого файла Вы хотите удалить данные: '))
        while answer < 1 or answer > 3:
            answer = int(input('___________________________\n'
                               'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                               'Введите номер файла от 1 до 3: '))
            loading()

        with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            number = int(data_remake(data[-1])[0])

        number_row = int(input("___________________________\n"
                               f"Отлично! Будем удалять данные из {answer}-файла.\n"
                               f"Выбери номер строки от 1 до {number}: "))
        while number_row < 1 or number_row > number:
            number_row = int(input('___________________________\n'
                                   'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                                   f'Введите номер строки от 1 до {number}: '))
        print('___________________________\n'
              'Удаление успешно завершено!')

        del data[number_row - 1]
    else:
        with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            number = int(data_remake(data[-1])[0])

    result = list()
    for i in range(len(data)):
        row = f'{i + 1}' + data[i][[i in separator for i in [i for i in data[i]]].index(True):]
        result.append(row)
    with open(f'db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines(result)


razdelitel = ''


def add(file_num=None, list_data=None):
    if not file_num:
        global razdelitel
        printdata()
        answer = int(input('___________________________\n'
                           'Выберите файла, в который Вы хотите добавить строку: '))
        while answer < 1 or answer > 3:
            answer = int(input('___________________________\n'
                               'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                               'Введите номер файла от 1 до 3: '))
            loading()

        print('___________________________\n'
              '|')
        name = input("|\n| Введите имя: ")
        surname = input("|\n| Введите фамилию: ")
        phone = input(
            "|\n| Введите номер телефона: ")  # При необходимости можно добавить проверку на телефон с помощью регулярных выражений
        city = input("|\n| Введите город: ")
        razdelitel = input("|\n| Введите разделитель(  - . ; ,  ): ")
        print('___________________________\n'
              'Данные успешно записаны!')
        with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            if data:
                number = int(data_remake(data[-1])[0])
            else:
                number = 0
        add_list = f'{number + 1}{razdelitel}{name}{razdelitel}{surname}{razdelitel}{phone}{razdelitel}{city}\n'
    else:
        answer = file_num
        add_list = list_data
        with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
    result = list()
    for i in range(len(data)):
        if list(data[i][-1]) != ['\n']:
            result.append(data[i] + '\n')
        else:
            result.append(data[i])
    result.append(add_list)
    with open(f'db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines(result)


def change():
    printdata()
    answer = int(input('___________________________\n'
                       'Выберите в каком файле Вы хотите изменить запись: '))
    while answer < 1 or answer > 3:
        answer = int(input('___________________________\n'
                           'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                           'Введите номер файла от 1 до 3: '))
        loading()
    with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        number = int(data_remake(data[-1])[0])

    number_row = int(input("___________________________\n"
                           f"Отлично! Будем изменять данные из {answer}-файла.\n"
                           f"Выбери номер строки от 1 до {number}: "))
    while number_row < 1 or number_row > number:
        number_row = int(input('___________________________\n'
                               'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                               f'Введите номер строки от 1 до {number}: '))
        loading()
    answer_list = list(map(int, input("___________________________\n"
                                      "Отлично! Выбери данные, которые Вы хотите поменять:\n"
                                      "1 - Имя,\n"
                                      "2 - Фамилия,\n"
                                      "3 - Телефон,\n"
                                      "4 - Город\n"
                                      "Примечание: Если Вы хотите изменить несколько данных одновременно, "
                                      "то запишите номера через пробел.\n"
                                      "Ввод: ").split()))
    while sum([int(1 <= i <= 4) for i in answer_list]) != len(set(answer_list)):
        answer_list = list(map(int, input("___________________________\n"
                                          "Отлично! Выбери данные, которые Вы хотите поменять:\n"
                                          "1 - Имя,\n"
                                          "2 - Фамилия,\n"
                                          "3 - Телефон,\n"
                                          "4 - Город\n"
                                          "Примечание: Если Вы хотите изменить несколько данных одновременно, "
                                          "то запишите номера через пробел.\n"
                                          "Ввод: ").split()))
        loading()
    name = None
    surname = None
    phone = None
    city = None
    for i in answer_list:
        if i == 1:
            name = input("Введите имя: ")
        elif i == 2:
            surname = input("Введите фамилию: ")
        elif i == 3:
            phone = input("Введите номер телефона: ")
        else:
            city = input("Введите город: ")

    with open(f'db/data{answer}.txt', 'r', encoding='utf-8') as file:
        database = file.readlines()
        data = database[number_row - 1]
    print(data)
    if name is None:
        name = data.split(separator[[i in data for i in separator].index(True)])[1]
    if surname is None:
        surname = data.split(separator[[i in data for i in separator].index(True)])[2]
    if phone is None:
        phone = data.split(separator[[i in data for i in separator].index(True)])[3]
    if city is None:
        city = data.split(separator[[i in data for i in separator].index(True)])[4]

    with open(f'db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines(database[:number_row - 1] +
                        [
                            f"{data.split(separator[[i in data for i in separator].index(True)])[0]}{razdelitel}{name}{razdelitel}{surname}{razdelitel}{phone}{razdelitel}{city}"] +
                        database[number_row + 1:])

    print('___________________________\n'
          'Данные успешно изменены!')


def clear(answer=None):
    if not answer:
        printdata()
        answer = int(input('___________________________\n'
                           'Выберите какой файл Вы хотите очистить: '))
        while answer < 1 or answer > 3:
            answer = int(input('___________________________\n'
                               'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                               'Введите номер файла от 1 до 3: '))
            loading()

        print("___________________________\n"
              "Отлично! Происходит очистка файла, подождите :)")
        loading()
        print('___________________________\n'
              f'Файл {answer} успешно очищен!')
    open(f'db/data{answer}.txt', 'w').close()


def loading():
    import time
    import sys

    animationproc = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□",
                 "■■■■■■□□□□",
                 "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)] + f" {animationproc[i]}")
        sys.stdout.flush()

    print("\n")


def terminate():
    for i in range(1, 4):
        open(f'db/data{i}.txt', 'w').close()


def printdata():
    for i in range(1, 4):
        with open(f'db/data{i}.txt', 'r', encoding='utf-8') as file:
            print("___________________________\n"
                  f"Вывожу данные из {i}-го файла:")
            data = [[j if '\n' not in j else j.split('\n')[0] for j in
                     i.split(separator[[k in i for k in separator].index(True)])] for i in file.readlines()]
            if len(data) == 0:
                print("Файл пустой!")
            else:
                columns = ['Номер', 'Имя', 'Фамилия', 'Телефон', 'Город']
                max_columns = []
                for col in zip(*data):
                    len_el = []
                    [len_el.append(len(el)) for el in col]
                    max_columns.append(max(len_el))
                for column in columns:
                    print(f'{column:{max(max_columns) + 1}}', end='')
                print()
                print(f'{"=" * max(max_columns) * 5}')
                for el in data:
                    for col in el:
                        print(f'{col:{max(max_columns) + 1}}', end='')
                    print()
                print('\n')
        loading()


def check_numbers(answer):
    while answer < 1 or answer > 7:
        print("ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n"
              "Введите значение от 1 до 6.\n"
              "Выберите действие:\n"
              "___________________________\n"
              "1. Удалить запись.\n"
              "2. Добавить запись.\n"
              "3. Изменить запись.\n"
              "4. Вывести данные.\n"
              "5. Очистить файл.\n"
              "6. Перенести данные.\n"
              "7. Выход.")
        answer = int(input("___________________________\nВведите номер действия: "))
        loading()
    return answer
