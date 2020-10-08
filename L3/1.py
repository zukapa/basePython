def first_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "деление на ноль"


print(first_func(int(input('введите a = ')), int(input('введите b = '))))
