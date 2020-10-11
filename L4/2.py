my_list = [23, 4, 8, 8, 29, 2, 2, 2, 9, 4, 7, 11]
new_list = [el for i, el in enumerate(my_list) if my_list[i - 1] < my_list[i]]
print(my_list)
print(new_list)
