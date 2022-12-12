"""
File with task 1
"""

from random import randint


# игровое поле первого игрока
game_field_pl1 = []
# игровое поле второго игрока
game_field_pl2 = []


def check_possibility(gf, pos, orientation, size):
    """компаратор возможности вставки корабля на заданное место"""
    for i in range(size):
        if orientation == 0 and (pos % 10 <= size - 1 or gf[pos // 10][pos % 10 - i] != '~'):
            return False
        elif orientation == 1 and (pos % 10 >= 10 - size or gf[pos // 10][pos % 10 + i] != '~'):
            return False
        elif orientation == 2 and (pos // 10 <= size - 1 or gf[pos // 10 - i][pos % 10] != '~'):
            return False
        elif orientation == 3 and (pos // 10 >= 10 - size or gf[pos // 10 + i][pos % 10] != '~'):
            return False
    return True


def generate_ship(gf, counter, size, mark):
    """Генерация кораблей количеством counter на игровом поле"""
    for i in range(counter):
        orientation = randint(0, 3) # 0 - влево, 1 - вправо, 2 - вверх, 3 - вниз
        n = -1
        while n == -1:
            n = randint(0, 99)
            if check_possibility(gf, n, orientation, size):
                for j in range(size):
                    if orientation == 0:
                        gf[n // 10][n % 10 - j] = mark
                    elif orientation == 1:
                        gf[n // 10][n % 10 + j] = mark
                    elif orientation == 2:
                        gf[n // 10 - j][n % 10] = mark
                    elif orientation == 3:
                        gf[n // 10 + j][n % 10] = mark
            else:
                n = -1


def print_game_field(gf1, gf2):
    """вывод на экран двух игровых полей"""
    print('   ', end='')
    for i in range(0, 10):
        print(f'  {i}  ', end='')
    print('     ', end='')
    print('   ', end='')
    for i in range(0, 10):
        print(f'  {i}  ', end='')
    print()
    for i, el in enumerate(zip(gf1, gf2)):
        print(f' {i} {el[0]}      {i} {el[1]}')
    print()


def generate_field(gf):
    """Генерация игрового поля с кораблями"""
    generate_ship(gf, 4, 1, 'B')
    generate_ship(gf, 3, 2, 'D')
    generate_ship(gf, 2, 3, 'C')
    generate_ship(gf, 1, 4, 'L')


def check_end_of_game():
    field_1_ends = field_2_ends = True
    for el in game_field_pl1:
        for item in el:
            if item not in '~X:':
                field_1_ends = False
    if field_1_ends:
        return 2

    for el in game_field_pl2:
        for item in el:
            if item not in '~X:':
                field_2_ends = False
    if field_2_ends:
        return 1
    return 0


def beat_by_pos(gf_beated, pos):
    if gf_beated[pos // 10][pos % 10] == '~':
        gf_beated[pos // 10][pos % 10] = ':'
        return True
    elif gf_beated[pos // 10][pos % 10] in 'X:':
        print('Вы уже били в эту клетку! Выберите другую!')
        return False
    else:
        gf_beated[pos // 10][pos % 10] = 'X'
        return False


def start_sea_battle():
    """Начало игры после инициализации"""
    pl_turn = randint(1, 2) # 1 - первый игрок, # 2 - второй игрок
    the_end = False
    while not the_end:
        print(f'Ход игрока {pl_turn}')
        pos = int(input('Введите число от 0 до 99: '))
        if pos < 0 or pos > 99:
            print('Введено неправильное число!')
            continue
        if beat_by_pos(game_field_pl2 if pl_turn == 1 else game_field_pl1, pos):
            pl_turn = pl_turn % 2 + 1
        else:
            continue

        print_game_field(game_field_pl1, game_field_pl2)
        the_end = check_end_of_game()
    print(f'Выиграл игрок {the_end}! Поздравления!!!')


def start_game():
    """Инициализация игры"""
    print("""Вас приветствует игра "Морской бой"!
Поля каждого из игроков сгенерированы автоматически.
Для выполнения хода напишите число от 0 до 99, где
единицы означают координату по столбцам,
а десятки - по строкам.
Выбор игрока, бьющего первым, осуществляется автоматически.""")
    global game_field_pl1, game_field_pl2
    game_field_pl1 = [['~' for _ in range(10)] for _ in range(10)]
    game_field_pl2 = [['~' for _ in range(10)] for _ in range(10)]
    generate_field(game_field_pl1)
    generate_field(game_field_pl2)
    print_game_field(game_field_pl1, game_field_pl2)
    start_sea_battle()


if __name__ == "__main__":
    """
    Сделать игру морской бой
    """
    start_game()
