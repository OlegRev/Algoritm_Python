#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как
# [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

def digit_hex(d):
    """Замена литерал в данной очереди на значения в 10-ой системе счисления"""
    for idx, item in enumerate(d):
        if item == 'A':
            d[idx] = 10
        elif item == 'B':
            d[idx] = 11
        elif item == 'C':
            d[idx] = 12
        elif item == 'D':
            d[idx] = 13
        elif item == 'E':
            d[idx] = 14
        elif item == 'F':
            d[idx] = 15

def hex_dec(d,a):
    """Преобразование из 16-ричной системы счисления в 10-ичную для очереди и получении суммы по всем элементам"""
    for i in range(len(d)):
        a.append(int(d[i])*16**i)
    return sum([i for i in a])
                                                                                                                         #(digit_hex() и hex_dec()) - преобразование из 16- рично1 в 10-ую систему с выходом суммы
def dec_hex(d):
    """Преобразование числа в 10-ой системе счисления в число 16-ричной системы счисления"""
    alphabet = "0123456789ABCDEF"
    n = int(d)
    if n < 16:
        return alphabet[n]
    else:
        return dec_hex(n // 16) + alphabet[n % 16]

digital_1 = deque(input('введите первое число').upper())                                                                 # ввод первого числа и перевод его в верхний регистр
#print(digital_1)
digital_2 = deque(input('введите второе число').upper())                                                                 # ввод второго числа и перевод его в верхний регистр
#print(digital_2)
sumbol = input('введите символ операции над числами ("+" "*" "-" "/")\n'                                                 # ввод символа операции над числами
               'для операций "-" и "/" вычесляется абсалютное значение')                                                 #
res1 = deque()                                                                                                           # инициализация очереди для res1
res2 = deque()                                                                                                           # инициализация очереди для res2

if len(digital_1) > len(digital_2):                                                                                      # условия несовпадения длины введеных чиселесли длина певого больше чторого то:
    digital_2.appendleft(0)                                                                                              # добавить "0" слева во второе число
elif len(digital_1) < len(digital_2):                                                                                    # если первое меньше второго то:
    digital_1.appendleft(0)                                                                                              # добавить "0" слева в первое число

digit_hex(digital_1)                                                                                                     # замена литерал в первом числе
digit_hex(digital_2)                                                                                                     # замена литерал во втором числе
digital_1.reverse()                                                                                                      # разворот очередей
digital_2.reverse()                                                                                                      # разворот очередей

hex_dec(digital_1, res1)                                                                                                 # сумирование элементов в очередях и добавление в res1
hex_dec(digital_2, res2)                                                                                                 # сумирование элементов в очередях и добавление в res2

if sumbol == '+':                                                                                                        #
    print(dec_hex(sum([i for i in res1]) + sum([i for i in res2])))                                                      # вывод для +
elif sumbol == '*':                                                                                                      #
    print(dec_hex(sum([i for i in res1]) * sum([i for i in res2])))                                                      # вывод для *
elif sumbol == '-':                                                                                                      #
    print(dec_hex(abs(sum([i for i in res1]) - sum([i for i in res2]))))                                                 # вывод для -  абсолютное значение
elif sumbol == '/':                                                                                                      #
    print(dec_hex(abs(sum([i for i in res1]) / sum([i for i in res2]))))                                                 # вывод для /  абсолютное значение



