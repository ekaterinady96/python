arg_1 = int(input('Введите число : '))
arg_2 = int(input('Введите число : '))
def my_func(arg_1, arg_2):
    return arg_1 / arg_2
if arg_2 == 0 :
    print('Ошибка! Деление на ноль невозможно')
else :
    print(my_func(20, 30))
