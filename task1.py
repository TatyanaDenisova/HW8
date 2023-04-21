def writing_person():
    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(f"{lastname} {name} {surname} {tel}\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)


def print_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
                    data_1.write("\n")

def change_note():
    note = input("введите запись, которую нужно изменить: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if note not in line:
                    data_1.write(line)
                else:
                    ask = input("""что поменять?
                                1 - фамилию,
                                2 - имя, 
                                3 - отчество,
                                4 - телефон
                                : """)
                    while ask not in ("1","2","3","4"):
                        print('ввод некорректный')
                        ask = input("""что поменять?
                                1 - фамилию,
                                2 - имя, 
                                3 - отчество,
                                4 - телефон
                                : """)
                    new_note = input('введите новые данные: ')
                    line_list = line.split()
                    line_list[int(ask)-1]=new_note
                    data_1.write(" ".join(line_list)+"\n")


def delite_note():
    note = input("введите запись, которую нужно удалить: ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        lines = data.readlines()
        with open("phonebook.txt", "w", encoding="utf-8") as data_1:
            for line in lines:
                if note not in line:
                    data_1.write(line)
                else:
                    print(line)
                    ask= input('желаете удалить эту строку? (y/n): ')
                    while ask not in ("y","n"):
                        print('ввод некорректный')
                        ask= input('желаете удалить эту строку? (y/n): ')
                    if ask == 'n':
                        data_1.write(line)


print("""1 - добавление,
2 - поиск,
3 - вывод на экран,
4 - импорт в файл, 
5 - внесение изменений
6 - удаление """)
ask = int(input())
if ask ==1:
    writing_person()
elif ask ==2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    load()
elif ask ==5:
    change_note()
elif ask ==6:
    delite_note()
else:
    print('нет такой команды')

