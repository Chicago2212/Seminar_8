def delete():
    printdata()
    answer = int(input('___________________________\n'
                       'Выберите из какого файла Вы хотите удалить данные: '))
    while answer < 1 or answer > 3:
        answer = int(input('___________________________\n'
                           'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                           'Введите номер файла от 1 до 3: '))
        loading()

    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        number = int(data[-1].split(';')[0])

    number_row = int(input("___________________________\n"
                           f"Отлично! Будем удалять данные из {answer}-файла.\n"
                           f"Выбери номер строки от 1 до {number}: "))
    while number_row < 1 or number_row > number:
        number_row = int(input('___________________________\n'
                               'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                               f'Введите номер строки от 1 до {number}: '))

    del data[number_row]
    count = 1
    result = list()
    for i in range(number - 1):
        row = f'{count};' + data[i][data[i].index(';') + 1:]
        count += 1
        result.append(row)
    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines(result)

    print('___________________________\n'
          'Удаление успешно завершено!')


def add():
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
    phone = input("|\n| Введите номер телефона: ")  # При необходимости можно добавить проверку на телефон с помощью регулярных выражений
    city = input("|\n| Введите город: ")
    ans = str(input("Ведите знак через которой сохранять"))
    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        if data:
            number = int(data[-1].split(';')[0])
        else:
            number = 0
    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines (data + [f'{number + 1}{ans}{name}{ans}{surname}{ans}{phone}{ans}{city}'])

    print('___________________________\n'
          'Данные успешно записаны!')


def change():
    printdata()
    answer = int(input('___________________________\n'
                       'Выберите в каком файле Вы хотите изменить запись: '))
    while answer < 1 or answer > 3:
        answer = int(input('___________________________\n'
                           'ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n'
                           'Введите номер файла от 1 до 3: '))
        loading()
    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        number = int(data[-1].split(';')[0])

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

    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'r', encoding='utf-8') as file:
        database = file.readlines()
        data = database[number_row - 1]
    print(data)
    if name is None:
        name = data.split(';')[1]
    if surname is None:
        surname = data.split(';')[2]
    if phone is None:
        phone = data.split(';')[3]
    if city is None:
        city = data.split(';')[4]

    with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'w', encoding='utf-8') as file:
        file.writelines(database[:number_row - 1] + [f"{data.split(';')[0]};{name};{surname};{phone};{city}"] +
                        database[number_row + 1:])

    print('___________________________\n'
          'Данные успешно изменены!')


def clear():
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
    open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{answer}.txt', 'w').close()
    loading()
    print('___________________________\n'
          f'Файл {answer} успешно очищен!')


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
        open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{i}.txt', 'w').close()


def printdata():
    for i in range(1, 4):
        with open(f'C:/Users/Sergei/Desktop//Python(seminar)/Seminar_8/db/data{i}.txt', 'r', encoding='utf-8') as file:
            print("___________________________\n"
                  f"Вывожу данные из {i}-го файла:")
            data = [[j if '\n' not in j else j.split('\n')[0] for j in i.split(';')] for i in file.readlines()]
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
    while answer < 1 or answer > 6:
        print("ERROR! Ошибка, скорее всего, Вы указали неправильное число.\n"
              "Введите значение от 1 до 6.\n"
              "Выберите действие:\n"
              "___________________________\n"
              "1. Удалить запись.\n"
              "2. Добавить запись.\n"
              "3. Изменить запись.\n"
              "4. Вывести данные.\n"
              "5. Очистить файл.\n"
              "6. Выход.")
        answer = int(input("___________________________\nВведите номер действия: "))
        loading()
    return answer
