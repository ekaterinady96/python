# Задание 1
# el_1 = 2
# el_2 = 59.18
# el_3 = True
# el_4 = None
# el_5 = 'Text'
# my_list = [el_1, el_2, el_3, el_4, el_5] # Вопрос: почему тип не определяется если не задавать каждый элемент отдельно, а сразу списком?
# for el in my_list:
#    print(type(el))
# Задание 2
# el_1 = input('Введите значение: ')
# el_2 = input('Введите значение: ')
# el_3 = input('Введите значение: ')
# el_4 = input('Введите значение: ')
# el_5 = input('Введите значение: ')
# my_list = [el_1, el_2, el_3, el_4, el_5]
# if len(my_list) % 2 == 0 :
#     i = 0
#     while i < len(my_list):
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i +=2
# else:
#     i = 0
#     while i < len(my_list) -1:
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i += 2
# print(my_list)
# Задание 3 (список)
# month = int(input('Введите целое число: '))
# seasons = ['Весна', 'Лето', 'Осень', 'Зима']
# if month == 3 or month == 4 or month == 5:
        # print(seasons[0])
# elif month == 6 or month == 7 or month == 8:
        # print(seasons[1])
# elif month == 9 or month == 10 or month == 11:
        # print(seasons[2])
# elif month == 12 or month == 1 or month == 2:
        # print(seasons[3])
# else:
    # print('Введите число от 1 до 12')
# Задание 3 (словарь)
# month = int(input('Введите целое число: '))
# seasons = {1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
# if month == 3 or month == 4 or month == 5:
#     print(seasons.get(1))
# elif month == 6 or month == 7 or month == 8:
#     print(seasons.get(2))
# elif month == 9 or month == 10 or month == 11:
#     print(seasons.get(3))
# elif month == 12 or month == 1 or month == 2:
#     print(seasons.get(4))
# else:
#     print('Введите число от 1 до 12')
# Задание 4
# sentence = str(input('Введите предложение: '))
# sentence_part = sentence.split(' ')
# for ind, el in enumerate(sentence_part):
#     if len(el) < 10:
#         print(ind, el)
#     else:
#          el = el[0:10]
#          print(ind, el)
# Задание 5
# i = int(input("Enter number: "))
# my_list = [7, 5, 3, 3, 2]
# duplicates = my_list.count(i)
# for el in my_list:
#     if duplicates > 0:
#         position_1 = my_list.index(i)
#         print(my_list.insert(duplicates + position_1, i))
#     elif i > el:
#         position_2 = my_list.index(el)
#         print(my_list.insert(position_2, i))
#     elif i < my_list[len(my_list) - 1]:
#         print(my_list.append(i))
# Задание 6 - не успела :(






