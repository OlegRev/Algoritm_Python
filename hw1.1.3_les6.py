#вариант3
import sys
import random
N_3 = 5
M_3 = 4
matrix_3 = [[random.randint(0, 99) for _ in range(M_3-1)] for _ in range(N_3)]

for line_3 in matrix_3:
    sum_line_3 = 0
    for i_3, item_3 in enumerate(line_3):
        sum_line_3 += item_3
        print(f'{item_3:>5}', end='')

    print(f'   |{sum_line_3}')

#key_ = [itm for itm in locals()]
#val_ = [sys.getsizeof(itm) for itm in locals().values()]
#[print(f'{key_[i]:>15} весит {val_[i]}') for i in range(len(key_))]
#print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in val_])}')

[print(f'{itm:>15}', end='|') for itm in locals()]
print(f'\nвеса равны')
[print(f'{sys.getsizeof(itm):>15}', end='|') for itm in locals().values()]
print(f'\nобщий вес равен :{sum([sys.getsizeof(itm) for itm in locals().values()])}')
