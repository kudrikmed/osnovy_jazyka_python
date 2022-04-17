def fact(n: int):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        yield ans


for x in fact(10):
    print(x)
