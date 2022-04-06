# Задача 1_4 курса "Основы языка Python"

num = int(input("Введите целое положительное число: "))
divider = 1
biggest_number = 0
while num // divider:
    current_number = (num % (divider * 10)) // divider
    if current_number > biggest_number:
        biggest_number = current_number
    divider = divider * 10
print(biggest_number)
