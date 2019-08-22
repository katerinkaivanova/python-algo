import random
import cProfile

from Lesson_7.sorting import bubble_sort

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


def main():
    orig_list = [random.randint(-100, 100) for _ in range(100)]
    copy_list = orig_list.copy()

    ordered_list = bubble_sort(copy_list, asc=False)

    del copy_list

    print(orig_list)
    print(ordered_list)


cProfile.run('main()')
