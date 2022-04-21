from translate import Translator
translator = Translator(to_lang="Russian")

my_file = open("text_4.txt", mode="r", encoding="utf-8")
my_f = my_file.readlines()
my_file.close()

my_new_file = open("output_numbers.txt", mode="w", encoding="utf-8")

number = 1
for line in my_f:
    line = line.split()
    my_new_file.write(f"{translator.translate(line[0]).capitalize()} - {number}\n")
    number += 1

my_new_file.close()
