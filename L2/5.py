my_list = [6, 4, 4, 3, 2]
for num in my_list:
    n = int(input('Введите новый элемент рейтинга: '))
    my_list.append(n)
    new_list = sorted(my_list)
    new_list.reverse()
    print(new_list)
