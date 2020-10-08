def my_func(a, b):
    b = abs(b)
    result = a
    while b != 1:
        b -= 1
        result *= a
    return 1 / result


print(my_func(10, -1))
