my_list = [x for x in range(2, 1001, 2)]
print(my_list)


def multiplicate_list(some_list):
    multiplication_result = 1
    for i in some_list:
        multiplication_result *= i
    return multiplication_result


print(multiplicate_list(my_list))
