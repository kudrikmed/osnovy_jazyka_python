my_list = []

while True:
    my_list.append(input("Введите значение: "))
    answer = input("Хотите ввести еще значение (Y/n)? ")
    if answer == "Y" or answer == "y":
        continue
    else:
        break

for i in range(1, len(my_list), 2):
    value_one = my_list[i]
    value_two = my_list[i - 1]
    my_list[i] = value_two
    my_list[i - 1] = value_one

print(my_list)
