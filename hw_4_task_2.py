my_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')

# Не поняла почему не работает вариант ниже
my_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]]
print(f'Исходный список {my_list}')
print(f'Новый список {new_list}')