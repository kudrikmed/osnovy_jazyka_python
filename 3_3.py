def sum_of_biggest(arg_1, arg_2, arg_3):
    """Функция возвращает сумму двух наибольших аргументов"""
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(my_list))
    return sum(my_list)


my_data = list(map(lambda x: int(x), input("Введите 3 числа через пробел: ").split()))
print(sum_of_biggest(*my_data))
