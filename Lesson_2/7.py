"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def create_seq(a, n):
    if n == 1:
        return str(a)
    else:
        return str(a) + " " + create_seq(a + 1, n - 1)


def check_seq(s):
    lst = s.split()
    left_side = sum([float(elem) for elem in lst])
    right_side = (lst[-1] * (lst[-1] + 1)) / 2
    return left_side == right_side


try:
    n = int(input("Введите натуральное число n: "))

    if n > 0:
        my_seq = create_seq(1, n)

        print(f"Множество натуральных чисел: {my_seq}")
        if check_seq:
            print("Равенство выполняется")
        else:
            print("Равенство не выполняется")
    else:
        print("Ошибка ввода!")

except Exception:
    print("Некорректные данные!")
