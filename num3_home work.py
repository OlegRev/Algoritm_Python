#3. Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

digital = input("введите натуральное число")
x = 0
a = 1
b = 10
new_digital = ''

while x != len(digital):

    digit = int(digital) // a
    digit = digit % b
    new_digital += str(digit)
    a *= 10
    x +=1

print(f'Развернутое число = {new_digital}')
