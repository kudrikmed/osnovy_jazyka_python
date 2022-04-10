my_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})
]

while True:
    menu = input("""Выберите 
    1. Добавить товар
    2. Посмотреть аналитику
    3. Завершить работу\n""")
    if menu == "1":
        # создание новой позиции товара
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        amount = int(input("Введите количество товара: "))
        size = input("Введите единицы измерения товара: ")
        my_tuple = (len(my_list) + 1, {"название": name, "цена": price, "количество": amount, "ед": size})
        my_list.append(my_tuple)
        print(my_list)
        continue
    elif menu == "2":
        # вывод аналитики по условияю задачи
        my_names_list = []
        my_prices_list = []
        my_amounts_list = []
        my_sizes_list = []
        for i in my_list:
            my_names_list.append(i[1]["название"])
            my_prices_list.append(i[1]["цена"])
            my_amounts_list.append(i[1]["количество"])
            my_sizes_list.append(i[1]["ед"])
        print({
            "название": my_names_list,
            "цена": my_prices_list,
            "количество": my_amounts_list,
            "ед": my_sizes_list # в условии не указано, что надо выводить только уникальные значения, если надо уникальные (как в примере) - list(set(my_sizes_list))
        })
        continue
    elif menu == "3":
        # выход из программы
        break
    else:
        # в начало цикла при некорректном вводе
        continue
