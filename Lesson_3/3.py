#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

n = randint(2, 10)
a = [randint(-30, 30) for x in range(n)]
print(' '.join([str(x) for x in a]))

index_of_min = 0
index_of_max = 0
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
    if a[i] < a[index_of_min]:
        index_of_min = i
a[index_of_min], a[index_of_max] = a[index_of_max], a[index_of_min]

print(' '.join([str(x) for x in a]))
