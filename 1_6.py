# Задача 1_6 курса "Основы языка Python"

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

if a <= b:
    day = 1
    while a < b:
        a = a * 1.1
        day += 1
    print(day)
else:
    print("Введенные значения некорректны!")
