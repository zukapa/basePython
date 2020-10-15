from math import factorial


def fact(n):
    for a in range(1, n + 1):
        yield factorial(a)


for el in fact(int(input('введите n = '))):
    print(el)
