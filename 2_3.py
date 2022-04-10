month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
month_dict = {1: ("январь", "зима"),
              2: ("февраль", "зима"),
              3: ("март", "весна"),
              4: ("апрель", "весна"),
              5: ("май", "весна"),
              6: ("июнь", "лето"),
              7: ("июль", "лето"),
              8: ("август", "лето"),
              9: ("сентябрь", "осень"),
              10: ("октябрь", "осень"),
              11: ("ноябрь", "осень"),
              12: ("декабрь", "зима")}

while True:
    month = input("Введите номер месяца: ")
    if month.isdigit():
        month = int(month)
        if 0 < month <= 12:
            break
        else:
            continue
    else:
        continue

# решение через dict
print(f"{month_dict[month][0]} - это {month_dict[month][1]}")

# решение через list
winter = ("декабрь", "январь", "февраль")
spring = ("март", "апрель", "май")
summer = ("июнь", "июль", "август")
autumn = ("сентябрь", "октябрь", "ноябрь")
month -= 1

if month_list[month] in winter:
    print(f"{month_list[month]} - это зима")
elif month_list[month] in spring:
    print(f"{month_list[month]} - это весна")
elif month_list[month] in summer:
    print(f"{month_list[month]} - это лето")
else:
    print(f"{month_list[month]} - это осень")
