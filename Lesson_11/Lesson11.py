"""
Создать 2 массива NumPy
Один из случайных чисел, второй - используя arange Или linspace
После этого выполнить математические операции- сложить, перемножить, делить
Найти максимальный элемент в каждой строчке и столбце первого массива (из случайных чисел)
Найти максимальный элемент в из 2 массивов
Изменить форму массива
"""

import numpy as np


if __name__ == '__main__':
    size = 5
    array_1 = np.random.random([size - 2, size])
    array_2 = np.linspace(1, 2, size)

    print('\tСоздание массивов')
    print('array1 =', array_1, sep='\n')
    print('array2 =', array_2)

    print('\n\tАрифметические действия над массивами')
    print('array1 + array2 =', array_1 + array_2, sep='\n')
    print('array1 * array2 =', array_1 * array_2, sep='\n')
    print('array1 / array2 =', array_1 / array_2, sep='\n')

    print('\n\tМаксимальные элементы')
    print('Максимальные элементы в столбцах array1:', array_1.max(axis=0), sep='\n')
    print('Максимальные элементы в строках array1:', array_1.max(axis=1), sep='\n')
    print('Максимальный элемент в array2:', array_2.max(), sep='\n')

    print('\n\tИзменение формы массива')
    print('Старая форма:', array_1.shape)
    array_1 = array_1.reshape(array_1.shape[0] * array_1.shape[1])
    print('Измененная форма array1:', array_1, sep='\n')
    print('Новая форма:', array_1.shape)
