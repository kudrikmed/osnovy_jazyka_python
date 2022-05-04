class ZeroDivision(Exception):
    pass


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

try:
    if b == 0:
        raise ZeroDivision
    else:
        print(a / b)
except ZeroDivision:
    print("Деление на ноль")
