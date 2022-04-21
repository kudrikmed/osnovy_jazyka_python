import json

my_file = open("text_7.txt", mode="r", encoding="utf-8")
my_firms = my_file.readlines()
successful_firms = 0
total_profit = 0
success_dict = {}
failure_dict = {}
for i in my_firms:
    line = i.split()
    earnings = int(line[2])
    costs = int(line[3])
    if earnings >= costs:
        profit = earnings - costs
        success_dict[line[0]] = profit
        successful_firms += 1
        total_profit += profit
    else:
        lesion = earnings - costs
        failure_dict[line[0]] = lesion
average_profit = total_profit / successful_firms
my_list = [success_dict | failure_dict, {"average_profit": round(average_profit, 2)}]
print(my_list)
my_file. close()

with open("firms.json", mode="w", encoding="utf-8") as w_json:
    json.dump(my_list, w_json, ensure_ascii=False, indent=4, sort_keys=True)
