"""
File with task 1
"""

import decimal

def task_1():
    """
    Вычислить число c заданной точностью d
    """
    print(task_1.__name__)

    number = decimal.Decimal(input('Введите число: '))
    d = decimal.Decimal(input("Введите точность '0.0001': "))
    print(number.quantize(d))

    print('----------------')
