n = int(input('Введите номер месяца с 1 по 12: '))
month_dict = {1: 'январь',
              2: 'февраль',
              3: 'март',
              4: 'апрель',
              5: 'май',
              6: 'июнь',
              7: 'июль',
              8: 'август',
              9: 'сентябрь',
              10: 'октябрь',
              11: 'ноябрь',
              12: 'декабрь'}
season = ['зима', 'весна', 'лето', 'осень']
if n == 1 or n == 2 or n == 12:
    print(f'{month_dict[n]} - зто {season[0]}')
elif n == 3 or n == 4 or n == 5:
    print(f'{month_dict[n]} - зто {season[1]}')
elif n == 6 or n == 7 or n == 8:
    print(f'{month_dict[n]} - зто {season[2]}')
elif n == 9 or n == 10 or n == 11:
    print(f'{month_dict[n]} - зто {season[3]}')
else:
    print('Неправильный ввод номера')
