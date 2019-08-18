"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict


class HexOperation:
    def __init__(self, num_dict):
        self.num_first = num_dict[0]
        self.num_second = num_dict[1]

    def __add__(self, other):
        return list(hex(int(''.join(self.num_first), 16) + int(''.join(self.num_second), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num_first), 16) * int(''.join(self.num_second), 16)))[2:]


def_dict = defaultdict(list)
def_dict[0].append(input("Введите первое шестнадцатиричное число: "))
def_dict[1].append(input("Введите второе шестнадцатиричное число: "))

res_sum = HexOperation(def_dict).__add__(other=0)
res_mul = HexOperation(def_dict).__mul__(other=0)

print(res_sum, res_mul)
