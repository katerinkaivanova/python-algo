"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def find_num(num, lst):
    counter = 0
    for elem in lst:
        if num == elem:
            counter += 1
    return counter


try:
    user_lst = [float(x) for x in input("Введите последовательность чисел через пробел: ").split()]
    user_num = float(input("Введите число для поиска: "))
    res = find_num(user_num, user_lst)
    if res == 0:
        print("Нет совпадений")
    else:
        print(f"Найдено совпадений: {res}")

except Exception:
    print("Некорректные данные!")
