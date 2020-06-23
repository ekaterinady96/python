def my_func() :
    global arg_1, arg_2, arg_3
    arg_1 = int(input('Введите число : '))
    arg_2 = int(input('Введите число : '))
    arg_3 = int(input('Введите число : '))
    max_1 = max(arg_1, arg_2, arg_3)
    if max_1 == arg_1:
        max_2 = max(arg_2, arg_3)
    elif max_1 == arg_2:
        max_2 = max(arg_1, arg_3)
    elif max_1 == arg_3:
        max_2 = max(arg_1, arg_2)
    my_sum = max_1 + max_2
    return my_sum
final = my_func()
print(final)


