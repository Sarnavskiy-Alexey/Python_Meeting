"""
File with task 5
"""


def task_5():
    """
    Задайте число. Составьте список чисел Фибоначчи, в том числе для
    отрицательных индексов. Негафибоначчи
    """
    print(task_5.__name__)

    k = int(input('Введите индекс числа Фибоначчи: '))
    print('Число Фибоначчи:', Fib(abs(k)) * (1 if k >= 0 else (-1 if (k + 1) % 2 == 1 else 1)))

    print('----------------')


def Fib(k) -> int:
    if k in range(2):
        return k
    else:
        return Fib(k - 1) + Fib(k - 2)
