# Задача 1_5 курса "Основы языка Python"

income = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = income - costs
if profit > 0:
    print("Поздравляю! Вы закончили отчетный период с прибылью!")
    ros = profit / income
    print(f"При этом, рентабельность продаж (Return on Sales, ROS) составила {ros}")
    employees = int(input("Какова численность сотрудников Вашего предприятия?: "))
    ppe = profit / employees
    print(f"Для вашей компании прибыль на сотрудника (Profit per Employee) составляет {ppe}")
elif profit == 0:
    print("В данном отчетном периоде значение прибыли равно нулю.")
elif profit < 0:
    print("В данном отчетном периоде Вы сработали в убыток.")
