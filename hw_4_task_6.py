from itertools import count
for el in count(int(input('Введите стартовое число: '))):
     if el > 150:
         break
     else:
         print(el)

from itertools import cycle
с = 0
for el in cycle(str(input("Введите слово: "))):
    if с > 10:
        break
    print(el)
    с += 1
