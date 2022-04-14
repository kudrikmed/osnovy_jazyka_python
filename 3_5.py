stripped_data = []

while True:
    end_cycle = False
    data = input("Введите слова, разделенные пробелом: ").split()

    for i in data:
        i.strip()
        if i == "q":
            end_cycle = True
            break
        elif i.isdigit():
            stripped_data.append(int(i))
        else:
            continue

    print(sum(stripped_data))
    if end_cycle:
        break
