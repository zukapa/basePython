with open('number.txt', 'w+', encoding="utf=8") as my_file:
    num = input('введите числа через пробел: ')
    my_file.write(num)
    my_num = num.split()
    my_sum = sum(map(int, my_num))
    print(my_sum)
