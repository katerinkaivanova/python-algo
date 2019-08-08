#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

n = randint(2, 10)
a = [randint(-30, 30) for x in range(n)]
print(' '.join([str(x) for x in a]))

index_of_min = 0
for i in range(1, len(a)):
    if a[i] < a[index_of_min]:
        index_of_min = i

if a[index_of_min] < 0:
    index_of_negative = index_of_min
    for i in range(len(a)):
        if a[index_of_negative] < a[i] < 0:
            index_of_negative = i
    print(f"Максимальный отрицательный элемент: {a[index_of_negative]}, индекс: {index_of_negative}")
else:
    print("Нет отрицательных чисел!")
