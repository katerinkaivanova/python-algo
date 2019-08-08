# 4. Определить, какое число в массиве встречается чаще всего.

from collections import Counter

try:
    a = Counter([int(x) for x in input("Введите последовательность чисел: ").split()])

    max_count = a.most_common(1)[0][1]
    lst = sorted([x for x in a.keys() if a.get(x) == max_count], reverse=True)
    print(lst[0])

except Exception:
    print("Ошибка ввода!")
