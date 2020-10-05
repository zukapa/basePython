a = input('Введите строку: ')
my_list = a.split()
i = 1
for b in my_list:
    print(f'{i}. {b[:10]}')
    i += 1
