"""
File with task 2
"""

from math import sqrt, ceil


def task_2():
    """
    Задайте натуральное число N. Напишите программу, которая составит список
    простых множителей числа N.
    """
    print(task_2.__name__)

    number = int(input('Введите натуральное число: '))

    l = []
    while number > 1:
        for i in range(2, number + 1):
            if number % i == 0:
                number //= i
                l.append(i)
                break
    print('Список простых множителей:', l)

    print('----------------')


if __name__ == '__main__':
    task_2()
