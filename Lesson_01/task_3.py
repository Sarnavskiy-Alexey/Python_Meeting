"""
File with task 3
"""

def task_3():
    """
    Напишите программу, которая принимает на вход координаты точки
    (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    в которой находится эта точка (или на какой оси она находится).
    """
    print(task_3.__name__)
    x_point = int(input('Введите координату X точки: '))
    y_point = int(input('Введите координату Y точки: '))
    _quater_ = 1
    if (x_point != 0) and (y_point != 0):
        if x_point < 0:
            _quater_ += 1
        if y_point < 0:
            _quater_ += 2
        print('Четверть:', _quater_)
    else:
        if x_point == 0:
            print('Точка x лежит на оси!')
        if y_point == 0:
            print('Точка y лежит на оси!')
    print('----------------')
