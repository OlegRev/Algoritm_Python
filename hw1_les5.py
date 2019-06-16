#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
from collections import namedtuple, deque                                                                                   # импорт нужных модулей

Company = namedtuple('Company', 'name profit_1_quarter profit_2_quarter profit_3_quarter profit_4_quarter ')                # инициализация namedtuple

number_of_enterprises = int(input('Введите количество предприятий'))                                                        # модуль ввода количеста предприятий

i=1                                                                                                                         # инициализация констант :для счетчика
sum_annual_profit_all_company = 0                                                                                           # для суммы общей прибыли всех компаний

enterprises = deque([])                                                                                                     # инициализация deque
annual_profit_company = deque([])                                                                                           #

while i < number_of_enterprises + 1:                                                                                        # вход в цикл с условием: пока значение{i} меньше"<" количеста предприятий{number_of_enterprises}

    company_i = Company(input(f'Введите наименование {i} компании :'),                                                      # модуль ввода дданных о компаниях
                        float(input(f'Введите прибыль за первый квартал {i} компании :')),                                  #
                        float(input(f'Введите прибыль за второй квартал {i} компании :')),                                  #
                        float(input(f'Введите прибыль за третий квартал {i} компании :')),                                  #
                        float(input(f'Введите прибыль за четвертый квартал {i} компании :')))                               #

    annual_profit_company_i = (company_i.profit_1_quarter + company_i.profit_2_quarter                                      # вычесление годовой прыбыли для компании
                               + company_i.profit_3_quarter + company_i.profit_4_quarter)                                   #

    annual_profit_company.append(annual_profit_company_i)                                                                   # добавление годовой прыбыли компании в "annual_profit_company = deque([])"

    enterprises.append(company_i)                                                                                           # добавление экземпляра компании в "enterprises = deque([])"

    sum_annual_profit_all_company += annual_profit_company_i                                                                # суммирование средне-квартальной прибыли всех компаний

    i += 1                                                                                                                  # счетчик

for idx, annual_profit_company_i in enumerate(annual_profit_company):                                                       # модуль условий вывода компаний:
    if annual_profit_company_i > sum_annual_profit_all_company/number_of_enterprises:                                       # если годовая прибыль компании больше средне-годовой прибыли среди всех компаний
        print(f'У компании {enterprises[idx].name} годовая прибыль ВЫШЕ :) среднего, среди введенных компаний')             # то вывести наименование этой компании
    else:                                                                                                                   # иначе
        print(f'У компании {enterprises[idx].name} годовая прибыль ниже :( среднего, среди введенных компаний')             # вывести наименование компаний с годовой прибылью меньше и равной средне-годовой прибыли среди компаний





