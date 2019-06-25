#вариант1
import sys
import random
N_1 = 5
M_1 = 4
matrix_1 = [[int(input(f'Введите натуральные числа  {j_1}-ая строка {i_1} - ый элемент'))
           for i_1 in range(M_1-1)] for j_1 in range(N_1)]

for line_1 in matrix_1:
    sum_line_1 = 0
    for idx_1, item_1 in enumerate(line_1):
        sum_line_1 += item_1
        print(f'{item_1:>4}', end='')

    print(f'   |{sum_line_1}')

#key_ = [itm for itm in locals()]
#val_ = [sys.getsizeof(itm) for itm in locals().values()]
#[print(f'{key_[i]:>15} весит {val_[i]}') for i in range(len(key_))]
#print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in val_])}')

[print(f'{itm:>15}', end='|') for itm in locals()]
print(f'\nвеса равны')
[print(f'{sys.getsizeof(itm):>15}', end='|') for itm in locals().values()]
print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in locals().values()])}')
