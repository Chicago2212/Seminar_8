def read_file(file_num):
    with open(f"db/data{file_num}.txt", "r", encoding="utf-8") as file_object:
        data = file_object.readlines()
    return data


def write_file(file_num, data_list):
    with open(f"db/data{file_num}.txt", "w", encoding="utf-8") as file_object:
        for i in range(len(data_list)):
            line_separator = data_list[i][-1]
            file_object.write(
                line_separator.join(
                    data_list[i][j] for j in range(len(data_list[i]) - 1)
                )
            )


def get_separator(data):
    separators = [".", ";", ",", "-"]

    for separator in separators:
        if separator in data:
            return separator

    return None


def get_data_list(data):
    data_list = list()
    for line in data:
        separator = get_separator(line)
        if separator is not None:
            line_list = line.split(separator)
            line_list.append(separator)
            data_list.append(line_list)
        else:
            data_list.append(line)
    return data_list


def delete_line(file_num, line):
    data = read_file(file_num)
    data_list = get_data_list(data)

    del data_list[line - 1]

    for i in range(line - 1, len(data_list)):
        data_list[i][0] = str(i + 1)

    write_file(file_num, data_list)


def add_to_file(file_num, parameters):
    data = read_file(file_num)
    data_list = get_data_list(data)
    parameters.insert(0, str(int(data_list[-1][0]) + 1))
    data_list.append(parameters)
    write_file(file_num, data_list)


def change_line(file_num, line, parameters):
    data = read_file(file_num)
    data_list = get_data_list(data)

    for i in range(len(parameters)):
        if parameters[i] != "":
            data_list[line - 1][i + 1] = parameters[i]

    write_file(file_num, data_list)


def clear_file(file_num):
    open(f"db/data{file_num}.txt", "w").close()


def clear_all_files():
    for i in range(1, 4):
        clear_file(i)


def printdata():
    for i in range(1, 4):
        with open(f"db/data{i}.txt", "r", encoding="utf-8") as file:
            print("___________________________\n" f"Вывожу данные из {i}-го файла:")
            data = [
                [
                    j if "\n" not in j else j.split("\n")[0]
                    for j in i.split(get_separator(i))
                ]
                for i in file.readlines()
            ]
            if len(data) == 0:
                print("Файл пустой!")
            else:
                columns = ["Номер", "Имя", "Фамилия", "Телефон", "Город"]
                max_columns = []
                for col in zip(*data):
                    len_el = []
                    [len_el.append(len(el)) for el in col]
                    max_columns.append(max(len_el))
                for column in columns:
                    print(f"{column:{max(max_columns) + 1}}", end="")
                print()
                print(f'{"=" * max(max_columns) * 5}')
                for el in data:
                    for col in el:
                        print(f"{col:{max(max_columns) + 1}}", end="")
                    print()
                print("\n")
