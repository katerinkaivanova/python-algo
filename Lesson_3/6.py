"""
6. В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

n = randint(2, 10)
a = [randint(-10, 10) for x in range(n)]
print(' '.join([str(x) for x in a]))

index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i

if index_of_max > index_of_min:
    print(f"Ряд: {a[index_of_min + 1:index_of_max]}, сумма: {sum(a[index_of_min + 1:index_of_max])}")
else:
    print(f"Ряд: {a[index_of_max + 1:index_of_min]}, сумма: {sum(a[index_of_max + 1:index_of_min])}")
