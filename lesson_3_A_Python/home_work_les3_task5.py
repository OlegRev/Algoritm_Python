import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE) ]
#print(array)

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.
start = 0
#array = [-10, 1, -2, -8, 3, -4, 5, 6]   #тестовый массив
max_negative_element = "dose not exist"           #для случая если в списке отсутствуют отрицательные элементы
index_el_neg_max = "dose not exist"          #для случая если в списке отсутствуют отрицательные элементы

for itm in range(len(array)):
    if array[itm] == MIN_ITEM or array[itm] > MIN_ITEM and array[itm] < 0:
        max_negative_element = start
        max_negative_element = array[itm]
        index_el_neg_max = start
        index_el_neg_max = itm
    itm += 1

print(f'максимальный отрицательный элемент в списке : {max_negative_element} и его индекс : {index_el_neg_max}')
print(f'список {array}')


