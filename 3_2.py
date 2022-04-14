# Вариант 1


def my_func(name, surname, birth, city, email, tel):
    return f"{name} {surname} {birth} {city} {email} {tel}"


data = input("Введите имя, фамилию, год рождения, город проживания, email, телефон в строку через пробел").split()
print(my_func(*data))
# print(my_func(name=data[0], surname=data[1], birth=data[2], city=data[3], email=data[4], tel=data[5]))

# Вариант 2


def my_func_2(**kwargs):
    my_list = []
    for i in kwargs:
        my_list.append(kwargs[i])
    return my_list


print(*my_func_2(name="A", surname="B", birth="123", city="C", email="D", tel="321"))
