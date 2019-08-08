# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

n = 5
m = 4

a = [[0 for j in range(m)] for i in range(n)]
b = [0 for j in range(m)]

print("\nМатрица: ")

for i in range(n):
    for j in range(m):
        a[i][j] = randint(0, 10)

for i in range(n):
    for j in range(0, m - 1):
        print(f"{a[i][j]:5}", end=' ')
    print(f"{a[i][m - 1]:5}")

max_num = 0
for j in range(m):
    min_num = float('inf')
    for i in range(n):
        if a[i][j] < min_num:
            min_num = a[i][j]
        b[j] = min_num
    if b[j] > max_num:
        max_num = b[j]

print(f"\nМинимальные элементы по столбцам: {b}, максимальный среди них: {max_num}")
