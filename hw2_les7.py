#2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
#[0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform

def merge_sort(array):
    """сортировка списка array методом слияния"""
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

array = [uniform(0, 49) for i in range(11)]
print(array)
print(merge_sort(array))

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    array = [-100.1, -60.2, -20.3, -40.4, -80.5, 79.6, 99.7, 59.8, 19.9, 39.11]
    array_sorted = [-100.1, -80.5, -60.2, -40.4, -20.3, 19.9, 39.11, 59.8, 79.6, 99.7]
    sort_algorithm(array)
    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #2: ", end="")
    array = list(range(0, 20)) + list(range(-19, 0))
    array_sorted = list(range(-19, 20, 1))
    sort_algorithm(array)
    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #3: ", end="")
    array = [-100.123, -80.124, -20.24, -100.123, -80.124, 79.4567, 99.3456, 99.3456, 19.456, 39.2354]
    array_sorted = [-100.123, -100.123, -80.124, -80.124, -20.24, 19.456, 39.2354, 79.4567, 99.3456, 99.3456]
    sort_algorithm(array)
    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

    print("testcase #4: ", end="")
    array = [uniform(0, 49) for i in range(10)]
    array_sorted = sorted(array)
    sort_algorithm(array)
    print("Ok" if sort_algorithm(array) == array_sorted else "Fail")

if __name__ == "__main__":
    test_sort(merge_sort)
