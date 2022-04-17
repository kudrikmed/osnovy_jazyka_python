given_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def is_unique(val, my_list):
    return my_list.count(val) == 1


print(list(x for x in given_list if is_unique(x, given_list)))
