# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

x1, y1 = map(int, input('Введитe координаты точки A(x1, y1) через пробел: ').split())
x2, y2 = map(int, input('Введитe координаты точки B(x2, y2) через пробел: ').split())

k = int((y1 - y2) / (x1 - x2))
b = int(y1 - k * x1)

print(f'y = {k} * x + {b}')