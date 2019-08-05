"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def my_func(a):
    return a[::-1]


def my_recursion(a):
    if len(a) == 1:
        return a
    else:
        return a[-1] + my_recursion(a[:-1])


try:
    num = input("Введите натуральное число: ")
    print(f"{my_func(num)}")
    print(f"{my_recursion(num)}")

except Exception:
    print("Некорректные данные!")
