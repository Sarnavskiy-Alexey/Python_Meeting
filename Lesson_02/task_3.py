"""
File with task 3
"""

def task_3():
    """
    Задайте список из n чисел, заполненный по формуле
    (1+1/n)**n и выведите на экран их сумму.
    """
    print(task_3.__name__)
    l = []
    N = int(input('Введите число N > 0: '))
    if N > 0:
        for i in range(1, N + 1):
            l.append(round((1 + 1 / i) ** i))
        print(l)
        print(sum(l))
    else:
        print('Вы ввели неправильное число N!')
    print('----------------')
