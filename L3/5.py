def my_func():
    complete_sum = 0
    full_sum = []
    while True:
        us_entry = list(map(str, input('введите числа через пробел, нажмите Q для выхода: ').split()))
        privat_sum = 0
        cut = ''
        for ind, val in enumerate(us_entry):
            if val.upper() == 'Q':
                cut = us_entry.pop(ind)
        for ind in us_entry:
            privat_sum = privat_sum + int(ind)
        full_sum.append(privat_sum)
        for ind in full_sum:
            complete_sum = complete_sum + ind
        print(complete_sum)
        complete_sum = 0
        if cut.upper() == 'Q':
            break
    return 'готово!'


print(my_func())
