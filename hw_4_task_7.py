n = int(input('Введите положительное число: '))
from itertools import count
from math import factorial
def fact():
    for el in count(1):
        yield factorial(el)
g = fact()
el = 0
for i in g:
    if el < n:
        print(i)
        el += 1
    else:
        break