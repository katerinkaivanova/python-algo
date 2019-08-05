"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

import sys


def check_lst(lst):
    if len(lst) == 0:
        return False
    for elem in lst:
        if elem < 1:
            return False
    return True


def get_sum(a):
    if len(a) == 1:
        return int(a)
    else:
        return int(a[-1]) + get_sum(a[:-1])


def find_max(lst):
    max_elem = 0
    max_res = 0

    for elem in lst:
        elem_res = get_sum(str(elem))
        if elem_res > max_res:
            max_elem = elem
            max_res = elem_res

    return str(max_elem) + ' ' + str(max_res)


try:
    user_lst = [int(x) for x in input("Введите последовательность натуральных чисел: ").split()]
    if not check_lst(user_lst):
        print("Ошибка ввода!")
        sys.exit()

    print(find_max(user_lst))

except Exception:
    print("Некорректные данные")
