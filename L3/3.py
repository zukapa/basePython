def my_func(arg1, arg2, arg3):
    a = [arg1, arg2, arg3]
    a.remove(min(a))
    return sum(a)


print(my_func(10, 10, 10))
