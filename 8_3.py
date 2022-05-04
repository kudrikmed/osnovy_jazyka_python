class NotANumber(Exception):
    pass


my_list = []
while True:
    try:
        a = input("Введите число: ")
        if a == "stop":
            print(my_list)
            break
        elif a.isdigit():
            my_list.append(a)
        else:
            raise NotANumber
            continue
    except NotANumber:
        print("Введите только число!")
