"""
File with task 2
"""

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


def first_predicate(x_1, y_1, z_1):
    """
    :param x_1: as X in formula
    :param y_1: as Y in formula
    :param z_1: as Z in formula
    :return: ¬(X ⋁ Y ⋁ Z)
    """
    return not(x_1 or y_1 or z_1)


def second_predicate(x_2, y_2, z_2):
    """
    :param x_2: as X in formula
    :param y_2: as Y in formula
    :param z_2: as Z in formula
    :return: ¬X ⋀ ¬Y ⋀ ¬Z
    """
    return (not x_2) and (not y_2) and (not z_2)
