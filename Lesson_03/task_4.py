"""
File with task 4
"""
import random

def task_4():
    """
    Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
    Напишите программу, которая найдёт разницу между максимальным и минимальным
    значением дробной части элементов.
    """
    print(task_4.__name__)

    k = int(input('Введите количество чисел: '))
    some_list = [round(random.uniform(0.0, k), 2) for i in range(k)]
    print('Полученный список чисел:', some_list)
    for i in range(k):
        some_list[i] = round(some_list[i] - int(some_list[i]), 2)
    print('После округления:', some_list)
    print('Минимальное:  ', min(some_list))
    print('Максимальное: ', max(some_list))
    print('Разница:      ', round(abs(max(some_list) - min(some_list)), 2))

    print('----------------')
