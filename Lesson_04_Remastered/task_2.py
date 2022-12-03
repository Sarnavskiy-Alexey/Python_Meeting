"""
File with task 2
"""

from random import randint

def task_2():
    """
    Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
    И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
    """
    print(task_2.__name__)

    size_A = int(input('Введите размер A: '))
    size_B = int(input('Введите размер B: '))

    source_list = [0] * size_A
    for i in range(size_A):
        source_list[i] = [0] * size_B
    for i in range(size_A):
        for j in range(size_B):
            source_list[i][j] = randint(0, size_A * size_B * 2)
    print('Сгенерированный список:')
    for i in range(size_A):
        print('', source_list[i], sep='\t')
    for i in range(size_A):
        middle = 0
        for j in range(size_B):
            middle += source_list[i][j]
        middle /= size_B
        print(f'Среднее арифметическое {i}й строки: {middle}')

    print('----------------')


if __name__ == '__main__':
    task_2()
