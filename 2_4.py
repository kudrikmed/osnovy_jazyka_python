some_text = input("Введите несколько слов, разделенных пробелами: ")
some_list = some_text.split()

for i in some_list:
    print(f"{some_list.index(i) + 1}. {i[:10]}")
