#3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
#называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
#в другой — не больше медианы.

from random import randint

m = int(input("Введите натуральное число :"))
SIZE = 2 * m + 1
array = [randint(1, 100) for i in range(SIZE)]

def gnome_sort(array):
    """гномья сортировка списка array"""
    i = 1
    while i < len(array):
        if i == 0 or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

def digit_rank_sort(array):
    """поразрядная сортировка списка array"""
    base = 10
    digit_len = len(str(max(array)))
    for i in range(digit_len):
        result = [[] for _ in range(base)]
        for rank in array:
            di_rank = rank // 10**i % 10
            result[di_rank].append(rank)
        array = []
        for j in range(base):
            array = array + result[j]
    return array

print(array)
print(gnome_sort(array))
print(digit_rank_sort(array))
print(f'медианной списка является :{array[len(array)//2]}')
