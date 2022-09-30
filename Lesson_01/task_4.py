"""
File with task 4
"""

def task_4():
    """Напишите программу, которая по заданному номеру четверти,
    показывает диапазон возможных координат точек в этой четверти
    (x и y).
    """
    print(task_4.__name__)
    _quater_ = int(input('Введите номер четверти: '))
    if 0 < _quater_ < 5:
        if _quater_ in (1, 4):
            print('x > 0 &', end=' ')
        else:
            print('x < 0 &', end=' ')
        if _quater_ in (1, 2):
            print('y > 0')
        else:
            print('y < 0')
    else:
        print('Такого номера четверти не существует!')
    print('----------------')
