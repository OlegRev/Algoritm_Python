"""
2)Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""
import cProfile

#first
n = int(input('номер простого числа которое хотим вывести: '))
def eratosthenes(numbers):
    sieve = [i for i in range(numbers)]
    sieve[1] = 0

    for i in range(2, numbers):
        if sieve[i] != 0:
            j = i + i
            while j < numbers:
                sieve[j] = 0
                j += i


    res = [i for i in sieve if i != 0]
    #print(res)
    print(res[n-1])

    # numbers - число, до которого хотим найти простые числа
    # n номер простого числа которое хотим вывести
#second

def div_r(numbers):
    res = []
    for k in range(2, numbers+1):

        prime = True

        for i in range(2, k):
            if k%i == 0:
                prime = False
                break

        if prime:
            res.append(k)
    print(res[n-1])


def main():
    numbers = 1000
    first_ = eratosthenes(numbers)
    second = div_r(numbers)


#cProfile.run('main()')
cProfile.run('eratosthenes(100000 )')
cProfile.run('div_r(10000 )')
#number=1000
#        1    0.000    0.000    0.001    0.001 home_work_task_2.py:11(eratosthenes)
#        1    0.008    0.008    0.008    0.008 home_work_task_2.py:31(div_r)             O(n**2)
#####
#number=2000
#        1    0.001    0.001    0.001    0.001 home_work_task_2.py:11(eratosthenes)
#        1    0.024    0.024    0.024    0.024 home_work_task_2.py:31(div_r)             O(n**2)
#number(4000)
#        1    0.001    0.001    0.002    0.002 home_work_task_2.py:11(eratosthenes)
#        1    0.106    0.106    0.106    0.106 home_work_task_2.py:31(div_r)             O(n**2)  
#number(10000)
#        1    0.004    0.004    0.006    0.006 home_work_task_2.py:11(eratosthenes)
#        1    0.576    0.576    0.576    0.576 home_work_task_2.py:31(div_r)
#number(100000)
#        1    0.067    0.067    0.093    0.093 home_work_task_2.py:11(eratosthenes)
