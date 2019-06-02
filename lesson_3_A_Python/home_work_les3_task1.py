import random

SIZE = 50
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
print(array)

#1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

list_ = [0]*len(array)
for i in array:#range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            list_[j-2] += 1
[print(f'{k} - {list_[k]}') for k in range(2, 10)]
