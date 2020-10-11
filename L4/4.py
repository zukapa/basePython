my_list = [23, 4, 8, 8, 29, 2, 2, 2, 9, 4, 7, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
