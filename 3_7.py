def int_func(arg: str):
    arg = arg.strip()
    arg = arg.lower()
    return arg.capitalize()


ans = list(map(int_func, input("Введите слова, разделенные пробелом: ").split()))
print(*ans)
