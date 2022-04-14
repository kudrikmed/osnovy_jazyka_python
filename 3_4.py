def my_cycle_exponentiation(x: float, y: int):
    """Возводит действительное число x в степень y, при этом y - целое отрицательное число"""
    y = abs(y)
    x = 1 / x
    for i in range(1, y):
        x *= x
    return x


def my_func_exponentiation(x: float, y: int):
    return x ** y


print(my_cycle_exponentiation(3, -2))
