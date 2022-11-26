"""
File with task 1
"""


def task_1():
    """
    Вводим с клавиатуры целое число X и У.
    Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
    """
    X = int(input('Введите X: '))
    Y = int(input('Введите Y: '))
    left = X if X < Y else Y
    right = X if X > Y else Y
    counter = 0
    for x in range(left + 1, right):
        if not (x % 2 or x % 3):
            counter +=1
    print(f'Количество чисел между {left} и {right}: {counter}')


if __name__ == '__main__':
    task_1()