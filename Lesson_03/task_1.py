"""
File with task 1
"""

import random

def task_1():
    """
    Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
    Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных
    позициях(не индексах).
    """
    print(task_1.__name__)

    k = int(input('Введите количество чисел: '))
    print('Сумма значений на нечетных позициях:', sum_odd_positions(rand_numbers(k)))

    print('----------------')


def rand_numbers(k) -> list:
    """
    Формирование произвольных чисел
    :param k: количество произвольных чисел
    :return: список с произвольными числами
    """
    l = random.sample(range(k * random.randint(1, 10)), k)
    print('Полученный список чисел:', l)
    return l


def sum_odd_positions(some_list) -> int:
    """
    Возврат суммы элементов на нечетных позициях (не индексах)
    :param some_list: список чисел
    :return: сумма
    """
    return sum(some_list[::2])
