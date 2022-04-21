# my_file = open("staff.txt", mode="a+", encoding="utf-8")
# my_file.truncate(0)
# my_file.write("Иванов 11000.0\n")
# my_file.write("Петров 30000.0\n")
# my_file.write("Сидоров 25000.0\n")
# my_file.write("Кузнецов 10000.0\n")
# my_file.write("Яковлев 35000.0\n")
# my_file.write("Климов 22000.0\n")
# my_file.write("Георгиев 20000.0\n")
# my_file.write("Семенов 30000.0\n")
# my_file.write("Александров 21000.0\n")
# my_file.write("Алексеев 13000.0\n")
# my_file.write("Дмитриев 15000.0\n")
# my_file.write("Егоров 25000.0\n")
# my_file.seek(0)

my_file = open("text_3.txt", mode="r", encoding="utf-8")
my_f = my_file.readlines()

staff_dict = {}
for string in my_f:
    split_string = string.split()
    staff_dict[split_string[0]] = float(split_string[1])


low_salary = []
for emp in staff_dict:
    if staff_dict[emp] < 20000:
        low_salary.append(emp)

print(f"Работники с ЗП меньше 20000: {', '.join(low_salary)}")

total_salary = 0
for emp in staff_dict:
    total_salary += staff_dict[emp]

mean_salary = total_salary / len(staff_dict)
print(f"Средняя зарплата составила {round(mean_salary, 2)}")

my_file.close()
