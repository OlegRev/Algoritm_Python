#8.	Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов
# каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import random
matrix = [[int(input('Введите натуральные числа')) for _ in range(4)] for _ in range(4)]

for line in matrix:
    line += [random.randint(0,99)]
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        print(f'{item:>5}', end='')

    print(f'   |сумма элементов строки = {sum_line}')
