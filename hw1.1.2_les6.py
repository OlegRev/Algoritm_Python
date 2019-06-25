#вариант2
import sys
import random
N_2 = 5
M_2 = 4
matrix_2 = []
for i_2 in range(N_2):
    row_2 = []
    summ_2 = 0

    for j_2 in range(M_2 - 1):
        num_2 = int(input(f'{i_2}-я строка, {j_2}-й элемент : '))
        summ_2 += num_2
        row_2.append(num_2)

    row_2.append(summ_2)
    matrix_2.append(row_2)

for line_2 in matrix_2:
    print(line_2)

#key_ = [itm for itm in locals()]
#val_ = [sys.getsizeof(itm) for itm in locals().values()]
#[print(f'{key_[i]:>15} весит {val_[i]}') for i in range(len(key_))]
#print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in val_])}')

[print(f'{itm:>15}', end='|') for itm in locals()]
print(f'\nвеса равны')
[print(f'{sys.getsizeof(itm):>15}', end='|') for itm in locals().values()]
print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in locals().values()])}')
