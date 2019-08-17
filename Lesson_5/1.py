"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

class_name = 'Company'
fields = ['name', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4', 'year']

Company = namedtuple(class_name, fields)
res = []

try:
    num = int(input("Введите количество предприятий: "))
    for i in range(num):
        name = input(f"Введите название предприятия #{i + 1}: ")
        q1, q2, q3, q4 = map(int, input(f"Введите прибыль предприятия --{name}-- за каждый квартал через пробел: ").split())
        y = sum([q1, q2, q3, q4])
        res.append(Company(name, q1, q2, q3, q4, y))

    average_profit = sum([elem.year for elem in res]) / num

    print(f"Средняя прибыль за год для всех предприятий: {average_profit:.2f}")
    print(f"Прибыль ниже средней: {[elem.name for elem in res if elem.year < average_profit]}")
    print(f"Прибыль равна или выше средней: {[elem.name for elem in res if elem.year >= average_profit]}")

except Exception:
    print("Ошибка ввода!")
