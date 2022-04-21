# my_file = open("text.txt", mode="a+", encoding="utf-8")
# my_file.write("first line\n")
# my_file.write("second line\n")
# my_file.write("third line\n")
# my_file.seek(0)

my_file = open("text_4.txt", mode="r", encoding="utf-8")

data = my_file.read().split("\n")
print(f"В файле {len(data)} строк(и)")

i = 1
for string in data:
    words = string.split()
    print(f"В строке {i} всего {len(words)} слов(а)")
    i += 1

my_file.close()
