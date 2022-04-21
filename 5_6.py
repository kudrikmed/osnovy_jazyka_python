import re
my_file = open("text_6.txt", mode="r", encoding="utf-8")
my_f = my_file.readlines()

my_dict = {}
for lesson in my_f:
    my_string = re.split(':|\s|\(|\)', lesson)
    my_dict[my_string[0]] = sum([int(s) for s in my_string if s.isdigit()])

print(my_dict)
my_file.close()
