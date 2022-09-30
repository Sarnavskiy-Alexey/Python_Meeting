def task_1():
    """
    Напишите программу, которая принимает на вход цифру,
    обозначающую день недели, и проверяет, является ли
    этот день выходным.
    """
    print(task_1.__name__)
    a = int(input('Введите число: '))
    if a == 6 or a == 7:
        print('Выходной день')
    elif (a > 0) and (a < 6):
        print('Рабочий день')
    else:
        print('Число не является номером дня недели')
    print('----------------')


def task_2():
    """
    Напишите программу для. проверки истинности утверждения
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    """
    print(task_2.__name__)
    for i in [0, 1]:
        for j in [0, 1]:
            for k in [0, 1]:
                if first_predicate(i, j, k) == second_predicate(i, j, k):
                    print('+', end=' ')
                else:
                    print('-', end=' ')
    print()
    print('----------------')


def first_predicate(x, y, z):
    return not(x or y or z)


def second_predicate(x, y, z):
    return (not x) and (not y) and (not z)


def task_3():
    """
    Напишите программу, которая принимает на вход координаты точки
    (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    в которой находится эта точка (или на какой оси она находится).
    """
    print(task_3.__name__)
    x = int(input('Введите координату X точки: '))
    y = int(input('Введите координату Y точки: '))
    a = 1
    if (x != 0) and (y != 0):
        if x < 0:
            a += 1
        if y < 0:
            a += 2
        print('Четверть:', a)
    else:
        if x == 0:
            print('Точка x лежит на оси!')
        if y == 0:
            print('Точка y лежит на оси!')
    print('----------------')


def task_4():
    """Напишите программу, которая по заданному номеру четверти,
    показывает диапазон возможных координат точек в этой четверти
    (x и y).
    """
    print(task_4.__name__)
    q = int(input('Введите номер четверти: '))
    if (q > 0) and (q < 5):
        if q == 1 or q == 4:
            print('x > 0 &', end=' ')
        else:
            print('x < 0 &', end=' ')
        if q == 1 or q == 2:
            print('y > 0')
        else:
            print('y < 0')
    else:
        print('Такого номера четверти не существует!')
    print('----------------')


def task_5():
    """
    Напишите программу, которая принимает на вход координаты двух
    точек и находит расстояние между ними в 2D пространстве.
    """
    print(task_4.__name__)
    x1 = float(input('Введите x1: '))
    y1 = float(input('Введите y1: '))
    x2 = float(input('Введите x2: '))
    y2 = float(input('Введите y2: '))
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(round(dist, 3))
    print('----------------')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
