"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def my_func(a):
    evens = 0
    odds = 0

    for x in a:
        if int(x) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return [evens, odds]


try:
    num = input("Введите натуральное число: ")
    res = my_func(num)
    evens = res[0]
    odds = res[1]

    print(f"Чётных чисел: {evens}, нечётных чисел: {odds}")

except Exception:
    print("Некорректные данные!")
