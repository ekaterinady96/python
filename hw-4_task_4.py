my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

# Не поняла почему не сработал вариант ниже

# def generator () :
#     for el in (2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11) :
#         yield el
#
# g = generator()
# print(g)
#
# for el in g if g.count(el) < 2 :
#     print(el)