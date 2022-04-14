num_1 = float(input("введите значение 1: "))
num_2 = float(input("введите значение 2: "))


def my_func(arg_1, arg_2):
    try:
        ans = arg_1 / arg_2
        return ans
    except ZeroDivisionError as err:
        return err


print(my_func(num_1, num_2))
