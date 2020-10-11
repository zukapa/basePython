num = range(20, 240)
num_list = [el for el in num if el % 20 == 0 or el % 21 == 0]
print(num_list)
