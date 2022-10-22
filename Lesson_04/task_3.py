"""
File with task 3
"""

from random import randint


def task_3():
    """
    Задайте последовательность чисел. Напишите программу, которая выведет список
    неповторяющихся элементов исходной последовательности в том же порядке.
    """
    print(task_3.__name__)

    k = int(input('Введите количество чисел в исходном списке: '))
    l = []
    for i in range(k):
        l.append(randint(0, 10))
    print('Полученный список случайных чисел: ', l)

    li = []
    for el in l:
        if l.count(el) == 1:
            li.append(el)
    print('Ответ: ' if k > 0 else 'Введено неправильное число!')
    print(li)

    print('----------------')


if __name__ == '__main__':
    task_3()
