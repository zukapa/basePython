import json

my_list = []
profit = {}
no_loss = []
average_prof = {}
with open('firm.txt', 'r', encoding="utf=8") as my_f:
    for line in my_f:
        name, form, revenue, expend = line.split()
        n = int(revenue) - int(expend)
        profit[name] = n
        if n > 0:
            no_loss.append(n)
    average_prof['average_profit'] = int((sum(no_loss)) / len(no_loss))
    my_list.append(profit)
    my_list.append(average_prof)

print(my_list)

with open('firm.json', 'w', encoding="utf=8") as write_f:
    json.dump(my_list, write_f)
