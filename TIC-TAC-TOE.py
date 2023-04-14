PLAYER_SYMBOLS = ".0X"
ROW_INDICES = "ABC"
COLUMN_INDICES = "123"


def welcome_game():  # Приветствие
    print("Добро пожаловать в игру крестики-нолики!")


welcome_game()
game_field = [[0 for _ in range(3)] for _ in range(3)]  # создание списков 3 на 3 для игрового поля


def print_game_field(gf):  # Функция, которая рисует поле
    for row in gf:
        for cell in row:
            print(PLAYER_SYMBOLS[cell], end=" ")  # Для начала игры поле определено точками, далее если игрок №1 - 0,
            # если №2 - X.
        print()


def is_tie(gf):  # Функция, проверяющая ничью
    for row in gf:
        for cell in row:
            if cell == 0:
                return False
    return True


def is_completed(gf):  # Фун-ия определяет: завершена ли партия, выводим номер игрока, который выиграл
    for row in gf:
        cell1, cell2, cell3 = row
        if (cell1 == cell2 == cell3) and cell1 != 0:
            return True, cell1  # если ячейки равны между собой и не равны нулю, то выиграл какой-то игрок

    for j in range(len(gf[0])):  # Проверяем победу
        first = gf[0][j]
        if first != 0:
            for i in range(1, len(gf)):
                if gf[i][j] != first:
                    break
            else:
                return True, first

    diagonal = gf[0][0]  # Проверяем победу в диагонали слева направо
    if diagonal != 0:
        for i in range(len(gf)):
            if gf[i][i] != diagonal:
                break
        else:
            return True, diagonal

    inv_diagonal = gf[0][len(gf) - 1]  # Проверяем победу в диагонали справа налево
    if inv_diagonal != 0:
        for i in range(len(gf)):
            if gf[i][len(gf) - i - 1] != inv_diagonal:
                break
        else:
            return True, inv_diagonal

    return is_tie(gf), 0


current_player = 1  # текущий игрок
completed, who_win = False, 0

while not completed:  # Ввод позиции игроков
    print_game_field(game_field)

    player_input = input(f"Игрок №{current_player}, введите позицию на игровом поле: ")
    if len(player_input) != 2:
        print("Неверное кол-во символов. Введите в формате: А1, где первый символ - ряд из A,B,C, второй - столбец из "
              "1,2,3")
        continue
    player_row, player_column = player_input
    player_row = ROW_INDICES.find(player_row)
    if player_row == -1:
        print("Неверный номер ряда. Укажите ряд:", ",".join(ROW_INDICES))
        continue
    player_column = COLUMN_INDICES.find(player_column)
    if player_column == -1:
        print("Неверный номер строки. Укажите цифру:", ",".join(COLUMN_INDICES))
        continue
    if game_field[player_row][player_column] > 0:
        print("Эта ячейка уже занята. Выберите другую")
        continue
    game_field[player_row][player_column] = current_player

    completed, who_win = is_completed(game_field)

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1
    else:
        print("Неверный номер игрока")

if who_win != 0:
    print(f"Игрок №{who_win} победил!")
else:
    print("Игра завершилась ничьей")

