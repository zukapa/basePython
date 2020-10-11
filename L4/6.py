from itertools import count, cycle

for i in count(int(input('введите целое число: '))):
    print(i)
    if i == 10:
        break

a = 0
my_list = ['Раз', 'Два', 'Три']
for i in cycle(my_list):
    if a == 10:
        break
    print(i)
    a += 1
