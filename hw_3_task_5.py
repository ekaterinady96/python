def my_sum ():
    sum_res = 0
    exception = False
    while exception == False:
        my_number = input('Введите число или Q чтобы закончить цикл: ').split()
        res = 0
        for el in range(len(my_number)):
            if (my_number[el]).upper() == 'Q':
                exception = True
                break
            else:
                res = res + int(my_number[el])
        sum_res = sum_res + res
    print(f'Сумма чисел равна {sum_res}')
print(my_sum())