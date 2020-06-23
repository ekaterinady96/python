from sys import argv
script_name, output, rate, bonus = argv
try:
    output = int(output)
    rate = int(rate)
    bonus = int(bonus)
    salary = output * rate + bonus
    print(f'Заработная плата сотрудника {salary}')
except IndentationError:
    print('Введите число')