given_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


print([b for a, b in zip(given_list, given_list[1:]) if b > a])
