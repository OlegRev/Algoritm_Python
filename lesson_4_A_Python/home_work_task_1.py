"""
1)Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import time
import timeit

# 1 вариант
first_ex = """
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
start = 0
array = [-10, 1, -2, -8, 3, -4, 5, -2]
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

array[index_el_min], array[index_el_max] = array[index_el_max], array[index_el_min]

"""
print(timeit.timeit(first_ex, number=100000))
#0.0325612 (n=1000)0.012785999999999999(для тестового массива)/   0.06523999999999999(n=2000)     0.1055845(n=4000)      |увеличение n на  1 порядок ведет к увеличению времени на  1порядок
#0.2547062 (n=10000)0.031071500000000002(для тестового массива)/                        |соответственно линейная зависимость O(n)
#2.4976191 (n = 100000)0.25449679999999997(для тестового массива)/                     |

#2
second_ex = """ 
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]      
array = [-10, 1, -2, -8, 3, -4, 5, -2]
idx_min = 0
idx_max = 0
for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]

"""
print(timeit.timeit(second_ex, number=100000))
#0.02450170000000007  (n=1000)0.002347000000000002(для тестового массива)/    0.049181(n=2000)  0.09766050000000001(n=4000)                  |O(n)
#0.2448672  (n=10000)0.022519900000000002(для тестового массива)/                               |O(n)
#2.5012068999999997 (n=100000)0.23819369999999995(для тестового массива)/                      |O(n)


# 3 вариант 
third_ex = """ 
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]  
array = [-10, 1, -2, -8, 3, -4, 5, -2]  
min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
"""
print(timeit.timeit(third_ex, number=100000))
#0.0243149 (n=1000)0.0020283000000000037(для тестового массива)  / 0.0476713(n=2000) 0.09618120000000001(n=4000)
#0.25011570000000005 (n=10000)0.01835189999999999(для тестового массива) /0.5174806999999999(n=20000)
#2.4098794000000003 (n=100000)0.18210179999999998(для тестового массива)/

#вывод : третий вариант наилучший по показателям времени с тестовым массивом, использование list comprehension
#приводит время к примерно одному времени

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.

next_ex4 = """
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
start = 0
array = [-10, 1, -2, -8, 3, -4, 5, -2]   #тестовый массив
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]    
max_negative_element = "dose not exist"           #для случая если в списке отсутствуют отрицательные элементы
index_el_neg_max = "dose not exist"          #для случая если в списке отсутствуют отрицательные элементы

for itm in range(len(array)):
    if array[itm] == MIN_ITEM or array[itm] > MIN_ITEM and array[itm] < 0:
        max_negative_element = start
        max_negative_element = array[itm]
        index_el_neg_max = start
        index_el_neg_max = itm
    itm += 1


"""
print(timeit.timeit(next_ex4, number=1000))
#0.0022524000000000016(n=1000 + тестовый массив)  0.024634199999999995(n=1000 + list comprehension)        |  list comprehension увеличивает время в 10 раз
#0.024114999999999998(n=10000 + тестовый массив)            0.2487123(n=10000 + list comprehension)        |
#0.2380367(n=100000 + тестовый массив)    2.4819401(n=100000 + list comprehension)                         |

# вариант 2
next_ex5 = """
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
#array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
array = [-10, 1, -2, -8, 3, -4, 5, -2]   #тестовый массив 
num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if num != float('-inf'):
    num
    index
"""
print(timeit.timeit(next_ex5, number=100000))
#0.0018447000000000047(n=1000)    0.024616100000000002(n=1000 + list comprehension)
#0.019203299999999993 (n=10000)    0.2424808(n=10000 + list comprehension)
#0.19036029999999998  (n=100000)    2.4222567(n=100000 + list comprehension)

import cProfile

def first_ex(array):




    #3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
    start = 0
    #array = [-10, 1, -10, 8, 3, 4, 8, 6, -10]   #тестовый массив

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

    #return max_element, index_el_max
    #return min_element,index_el_min
    #
    #return array
    array[index_el_min], array[index_el_max] = array[index_el_max], array[index_el_min]

    return array

cProfile.run('')

def second_ex(array):
    idx_min = 0
    idx_max = 0
    for i in range(len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
    return array

def main():
    import random

    SIZE = 100000
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
    first_ = first_ex(array)
    second_ = second_ex(array)

cProfile.run('main()')
# SIZE =1000
#        1    0.000    0.000    0.000    0.000 home_work_task_1.py:150(first_ex)
#        1    0.000    0.000    0.000    0.000 home_work_task_1.py:184(second_ex)
#        1    0.000    0.000    0.003    0.003 home_work_task_1.py:196(main)
#        1    0.000    0.000    0.003    0.003 home_work_task_1.py:202(<listcomp>)
# SIZE =10000
#        1    0.002    0.002    0.002    0.002 home_work_task_1.py:150(first_ex)
#        1    0.002    0.002    0.002    0.002 home_work_task_1.py:184(second_ex)
#        1    0.000    0.000    0.041    0.041 home_work_task_1.py:196(main)
#        1    0.006    0.006    0.037    0.037 home_work_task_1.py:202(<listcomp>)
# SIZE =100000
#        1    0.017    0.017    0.017    0.017 home_work_task_1.py:150(first_ex)
#        1    0.018    0.018    0.018    0.018 home_work_task_1.py:184(second_ex)
#        1    0.000    0.000    0.442    0.442 home_work_task_1.py:196(main)
#        1    0.057    0.057    0.407    0.407 home_work_task_1.py:202(<listcomp>)
