from function import delete, add, change, printdata, clear, loading, check_numbers, terminate, transfer
import os

def interface():
    print("Текущая деректория:", os.getcwd())
    print("***************************  Добро пожаловать!\t ***************************\n"
          "Выберите действие:\n"
          "___________________________\n"
          "1. Удалить запись.\n"
          "2. Добавить запись.\n"
          "3. Изменить запись.\n"
          "4. Вывести данные.\n"
          "5. Очистить файл.\n"
          "6. Перенос данных.\n"
          "7. Выход.")
    answer = int(input("___________________________\nВведите номер действия: "))
    loading()
    answer = check_numbers(answer)
    while answer != 7:
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
        elif answer == 6:
            transfer()
        print("Выберите действие:\n"
              "___________________________\n"
              "1. Удалить запись.\n"
              "2. Добавить запись.\n"
              "3. Изменить запись.\n"
              "4. Вывести данные.\n"
              "5. Очистить файл.\n"
              "6. Перенос данных.\n"
              "7. Выход.")
        answer = int(input("___________________________\nВведите номер действия: "))
        answer = check_numbers(answer)

    answer = input("___________________________\n"
                   "Желаю всего доброго! Не забывай, что все данные, которые ты записал, они сохранились.\n"
                   "Удалить? (ОТВЕТЬТЕ ДА/НЕТ): ").lower()
    if answer in ['да', 'yes']:
        terminate()
        print("___________________________\n"
              "Данные успешно удалены!"
              "Всего доброго!\n")
    else:
        print("___________________________\n"
              "Всего доброго!")
    exit()