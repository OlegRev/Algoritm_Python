import random

SIZE = 30
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

#2.	Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5,
# т.к. именно в этих позициях первого массива стоят четные числа.

massiv = [i for i, vol in enumerate(array) if vol % 2 == 0]
print(massiv)
