# Задача 1_2 курса "Основы языка Python"

time_in_seconds = int(input("Введите время в секундах: "))
hours = time_in_seconds // 3600
if hours < 10:
    hours = '0' + f'{hours}'
hours_rem = time_in_seconds % 3600
minutes = hours_rem // 60
if minutes < 10:
    minutes = '0' + f'{minutes}'
minutes_rem = hours_rem % 60
seconds = minutes_rem
if seconds < 10:
    seconds = '0' + f'{seconds}'
print(f'{hours}' + ':' + f'{minutes}' + ':' + f'{seconds}')
