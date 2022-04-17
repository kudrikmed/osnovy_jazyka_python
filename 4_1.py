from sys import argv


def count_salary(work_time, pay, bonus):
    work_time = float(work_time)
    pay = float(pay)
    bonus = float(bonus)
    salary = work_time * pay + bonus
    return round(salary, 2)


print(count_salary(argv[1], argv[2], argv[3]))
