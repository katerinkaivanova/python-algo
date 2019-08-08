"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

from random import randint

n = 5
m = 4

a = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    row_sum = 0
    for j in range(0, m - 1):
        a[i][j] = randint(0, 10)
        row_sum = row_sum + a[i][j]
        print(f"{a[i][j]:5}", end=' ')
    a[i][m - 1] = row_sum
    print(f"{a[i][m - 1]:5}")
