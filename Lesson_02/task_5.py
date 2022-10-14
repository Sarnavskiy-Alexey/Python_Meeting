"""
File with task 5
"""

import random as r

def task_5():
    """
    ** Реализуйте алгоритм перемешивания списка.
    Без функции shuffle из модуля random.
    """
    print(task_5.__name__)
    N = int(input('Введите количество чисел в списке: '))
    l = []
    for i in range(N):
        l.append(i)
    print(l)
    for i in range(len(l)):
        k = r.randint(0, N - 1)
        t = l[i]
        l[i] = l[k]
        l[k] = t
    print(l)
    print('----------------')
