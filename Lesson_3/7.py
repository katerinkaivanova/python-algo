"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import randint

n = randint(2, 10)
a = [randint(-10, 10) for x in range(n)]
print(' '.join([str(x) for x in a]))

m1, m2 = float('inf'), float('inf')
for x in a:
    if x <= m1:
        m1, m2 = x, m1
    elif x < m2:
        m2 = x

print(m1, m2)
