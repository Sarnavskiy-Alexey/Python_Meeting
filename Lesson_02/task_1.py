"""
File with task 1
"""

def task_1():
    """
    Напишите программу, которая принимает на вход вещественное
    число и показывает сумму его цифр.
    """
    print(task_1.__name__)
    number = float(input('Введите вещественное число: '))
    sum = 0
    for el in str(number):
        sum += int(el) if el.isnumeric() else 0
    print('Сумма цифр:', sum)
    print('----------------')
