#1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
#[-100; 100). Выведите на экран исходный и отсортированный массивы.
#Примечания:
#● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
#● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии
#сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
from random import randint

def bubble_sort(array):
    """сортировка списка array методом пузырька"""
    spam = True
    eggs = 0
    while spam:
        eggs += 1
        spam = False
        for i in range(len(array) - eggs):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                spam = True
    return array

array = [randint(-100, 99) for i in range(10)]
print(array)
print(bubble_sort(array))

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    array = [-100, -60, -20, -40, -80, 79, 99, 59, 19, 39]
    array_sorted = [99, 79, 59, 39, 19, -20, -40, -60, -80, -100]
    sort_algorithm(array)
    print("Ok" if array == array_sorted else "Fail")

    print("testcase #2: ", end="")
    array = list(range(0, 20)) + list(range(-19, 0))
    array_sorted = list(range(19, -20, -1))
    sort_algorithm(array)
    print("Ok" if array == array_sorted else "Fail")

    print("testcase #3: ", end="")
    array = [-100, -80, -20, -100, -80, 79, 99, 99, 19, 39]
    array_sorted = [99, 99, 79, 39, 19, -20, -80, -80, -100, -100]
    sort_algorithm(array)
    print("Ok" if array == array_sorted else "Fail")

if __name__ == "__main__":
    test_sort(bubble_sort)
