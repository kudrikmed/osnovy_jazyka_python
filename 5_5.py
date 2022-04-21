from random import randint
my_file = open("numbers.txt", mode="w+", encoding="utf-8")
my_numbers = [str(randint(-100, 100)) for _ in range(100)]
my_file.write(" ".join(my_numbers))
my_file.seek(0)

from_file = my_file.read().split()

my_sum = 0
for num in from_file:
    my_sum += int(num)
print(f"Сумма чисел равна {my_sum}")

my_file.close()
