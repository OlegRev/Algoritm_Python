#1 Найти сумму и произведение цифр
# трехзначного числа, которое вводит пользователь.
print('Введите трехзначное целое число')
number = int(input('number = '))

num1 = number//100
num2 = number//10%10
num3 = number%10
summa = num1 + num2 + num3
mul = num1 * num2 * num3

print(f'Сумма введенных чисел равна:{summa} \n '
      f'Произведенние введеных чисел равно: {mul}')
