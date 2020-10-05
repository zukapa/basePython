n = int(input('Введите целое положительное число: '))
m = n % 10
n = n // 10
while n > 0:
    a = n % 10
    if a > m:
        m = a
    n = n // 10
print(m)
