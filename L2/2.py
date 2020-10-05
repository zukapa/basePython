a = input('Введите элементы списка через пробел: ')
my_list = a.split()
print(my_list)
i = 0
while i < len(my_list):
    cutted = my_list.pop(i)
    past = my_list.insert(i+1, cutted)
    i += 2
print(my_list)
