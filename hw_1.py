# Задача 1
#
# speed = 7
# speed = speed + 7
# speed = speed * 10
# print(speed)
#
# time = 10
# time = 10 ** 2
# time = time / 3
# print(time)
#
# distance = speed * time
# print(distance)
#
# integer_1 = int(input('Введите целое число:'))
# integer_2 = integer_1 * 5
# print(integer_2)
#
# integer_3 = 5
# integer_4 = 1
# print(integer_3 > integer_4)
#
# name = input('Name: ')
# print('Hello, ', name)
#
# my_str_1 = str(input('Введите ваше имя:'))
# my_str_2 = str(input('Хорошего дня!'))
# my_str_3 = my_str_1 + my_str_2
# print(my_str_3)

# Задача 2
#
# enter_value = int(input('Введите время в секундах: '))
# time_in_hours = enter_value // 3600
# time_in_minutes = (enter_value % 3600)//60
# time_in_seconds = enter_value % 3600 % 60
# print('чч: {} мм: {} cc {}'.format(time_in_hours, time_in_minutes, time_in_seconds))
#
# Задача 3
#
# n = str(input('Введите число n: '))
# print(f'{n} + {n +n} + {n + n +n} = {int(n) + int(n + n) + int(n + n + n)}')
# #
# # Задача 4
# a = int(input('Введите положительное число: '))
# b = a % 10
# a = a // 10
# while a > 0:
#     if a % 10 > b:
#         b = a % 10
#     a = a // 10
# print(b)
#
# # Задача 5
# revenue = int(input('Введите значение выручки: '))
# costs = int(input('Введите значение издержек: '))
# financial_result = revenue - costs
# if financial_result > 0 :
#     print('Прибыль')
#     profit_margin = financial_result / revenue
#     print('Рентабельность выручки = ', profit_margin)
#     number_of_staff = int(input('Введите численность персонала: '))
#     profit_per_employee = financial_result / number_of_staff
#     print('Прибыль фирмы в расчете на одного сотрудника', profit_per_employee)
# elif financial_result < 0 :
#     print('Убыль')

# Задача 6
# a = int(input('Введите значение километров для первого дня пробежки: '))
# b = int(input('Введите искомое значение километров: '))
# n = 1
# while a < b :
#     a *= 1.1
#     n += 1
# print(n)











































