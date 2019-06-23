#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
from collections import namedtuple, deque

Company = namedtuple('Company', 'name_c profit_q total_profit ')

i = 1
average_profit = 0
enterprises = deque([])
sorted_companies = deque([None])
text = 'больше'

number_of_enterprises = int(input('Введите количество предприятий'))

while i < number_of_enterprises + 1:
    name_c = input(f'Введите наименование {i} компании :')
    profit_q = [float(input(f'Введите прибыль за {j} квартал {i} компании')) for j in range(1, 5)]
    total_profit = 0
    for item in range(len(profit_q)):
        total_profit += profit_q[item]

    company_i = Company(name_c=name_c, profit_q=profit_q, total_profit=total_profit)

    average_profit += total_profit
    enterprises.append(company_i)

    if i == number_of_enterprises:
        average_profit = average_profit / number_of_enterprises
    i += 1

for co in enterprises:
    if co.total_profit > average_profit:
        sorted_companies.appendleft(co)
    elif co.total_profit < average_profit:
        sorted_companies.append(co)

for co in sorted_companies:
    if co is None:
        text = 'меньше'
    else:
        print(f' Компания {co.name_c} заработала {text}, чем средняя прибыль - {average_profit}')



