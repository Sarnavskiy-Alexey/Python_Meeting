"""
File with task 3
"""

from random import randint

def task_3():
    """
    Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
    """
    print(task_3.__name__)

    size = 30
    source_list = [0] * size
    for i in range(size):
        source_list[i] = randint(0, size * 2)
    print('Неотсортированный сгенерированный список:', source_list, sep='\n')

    """
    Реализована двухсторонняя сортировка выбором: [https://habr.com/ru/post/422085/]
    Цель сортировки: отыскать позицию максимального и минимального элементов,
    а затем поменять их с пограничными значениями
    Отличие от обычной сортировки выбором: добавлен поиск минимального элемента, а также
    условия с возможными частными случаями:
    а) когда минимальный элемент на правой границе списка, а максимальный - на левой
    б) когда максимальный элемент на правой границе, а минимальный - где-то еще кроме левой границы
    в) остальные случаи (включая нахождение минимального элемента на правой границе)
    """
    left, right = 0, size - 1
    while left < right:
        minn, maxx = left, left
        for i in range(left, right + 1):
            if source_list[minn] > source_list[i]:
                minn = i
            if source_list[maxx] < source_list[i]:
                maxx = i
        if left == maxx and right == minn:
            source_list[left], source_list[right] = source_list[right], source_list[left]
        elif left == maxx:
            source_list[right], source_list[maxx] = source_list[maxx], source_list[right]
            source_list[left], source_list[minn] = source_list[minn], source_list[left]
        else:
            source_list[left], source_list[minn] = source_list[minn], source_list[left]
            source_list[right], source_list[maxx] = source_list[maxx], source_list[right]
        left += 1
        right -= 1

    print('Отсортированный список:', source_list, sep='\n')

    print('----------------')


if __name__ == '__main__':
    task_3()
