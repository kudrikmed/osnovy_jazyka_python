my_list = [7, 5, 3, 3, 2]

while True:
    new_value = input("Введите натуральное число: ")
    if new_value.isdigit() and int(new_value) != 0:
        new_value = int(new_value)
        break
    else:
        continue

if new_value <= my_list[-1]:
    my_list.append(new_value)
else:
    for i in my_list:
        if new_value > i:
            my_list.insert(my_list.index(i), new_value)
            break
print(my_list)
