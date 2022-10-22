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
    l = [(Fib(abs(i)) * (1 if i >= 0 else (-1 if (i + 1) % 2 == 1 else 1))) for i in range(-k, k + 1)]
    print('Полученный список чисел Фибоначчи:', l)

    print('----------------')


def Fib(k) -> int:
    if k in range(2):
        return k
    else:
        return Fib(k - 1) + Fib(k - 2)
