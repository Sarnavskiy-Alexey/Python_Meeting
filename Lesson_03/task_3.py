"""
File with task 3
"""


def task_3():
    """
    Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    Без использования встроенной функции преобразования, без строк.
    """
    print(task_3.__name__)

    number = int(input('Введите десятичное число: '))
    some_list = []
    while number > 0:
        some_list.insert(0, number % 2)
        number = int(number / 2)
    print("".join(map(str, some_list)))

    print('----------------')
