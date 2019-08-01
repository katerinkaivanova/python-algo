"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

a, b, c = map(int, input('Введитe длины трех отрезков через пробел: ').split())

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('Равносторонний треугольник')
    else:
        if a != b != c:
            print('Разносторонний треугольник')
        else:
            print('Равнобедренный треугольник')
else:
    print('Не треугольник')