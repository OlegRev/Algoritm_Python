import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
#print(array)

#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
start = 0

max_element = array[start]
index_el_max = start

min_element = array[start]
index_el_min = start

for itm in range(len(array)):
    if array[itm] > max_element:
        max_element = array[itm]
        index_el_max = itm
    elif array[itm] < min_element:
        min_element = array[itm]
        index_el_min = itm
    itm += 1

print(f'максимальное значение в списке - {max_element} и его индекс - {index_el_max}\n'
      f'минимальное значение в списке - {min_element} и его индекс -  {index_el_min}')

print(f'список выглядит так \n{array}')
array[index_el_min], array[index_el_max] = array[index_el_max], array[index_el_min]

print(f'после смены минимального и максимального элементы в списке \n{array}')

