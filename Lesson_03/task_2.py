"""
File with task 2
"""

import task_1

def task_2():
    """
    Напишите программу, которая найдёт произведение пар чисел списка.
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    """
    print(task_2.__name__)

    k = int(input('Введите количество чисел: '))
    some_list = task_1.rand_numbers(k)

    out_list = [some_list[i] * some_list[k - i - 1] for i in range(int(k / 2))]
    if k % 2 == 1:
        out_list.append(some_list[int(k / 2)])
    print('Ответ:', out_list)

    print('----------------')
