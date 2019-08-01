# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a, b, c = map(int, input('Введитe три числа через пробел: ').split())

if a >= b and a >= c:
    max = a
    if b >= c:
        min = c
        mid = b
    else:
        min = b
        mid = c
elif b >= c:
    max = b
    if a >= c:
        min = c
        mid = a
    else:
        min = a
        mid = c
else:
    max = c
    if a >= b:
        min = b
        mid = a
    else:
        min = a
        mid = b

print(f'{min} - минимум, {mid} - среднее, {max} - максимум')
