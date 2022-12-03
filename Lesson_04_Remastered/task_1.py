"""
File with task 1
"""

from random import randint

def task_1():
    """
    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
    стоящих на нечётной позиции. Пример:
        - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
    """
    print(task_1.__name__)

    size = int(input('Введите размер генерируемого списка: '))
    source_list = [0] * size
    summ = 0
    for i in range(size):
        source_list[i] = randint(0, size * 2)
    print('Сгенерированный список:', source_list)
    for i in range(1, size, 2):
        summ += source_list[i]
    print(f'Сумма элементов, стоящих на нечетных позициях: {summ}')

    print('----------------')


if __name__ == '__main__':
    task_1()
