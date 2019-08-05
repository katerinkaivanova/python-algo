"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def create_seq(a, n):
    if n == 1:
        return str(a)
    else:
        return str(a) + " " + create_seq(-1 * a / 2, n - 1)


try:
    n = int(input("Введите натуральное число n: "))

    if n > 0:
        my_seq = create_seq(1, n)
        print(f"Ряд: {my_seq}")
        print(f"Сумма элементов: {sum([float(x) for x in my_seq.split()])}")
    else:
        print("Ошибка ввода!")

except Exception:
    print("Некорректные данные!")
