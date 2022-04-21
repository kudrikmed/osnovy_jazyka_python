my_file = open("text.txt", mode="a", encoding="utf-8")


while True:
    input_string = input("Введите текст, для завершения работы нажмите Enter: ")
    if input_string != "":
        my_file.write(f"{input_string}\n")
    else:
        my_file.close()
        break
