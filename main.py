board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
player = True


def board_print(board: list):
    print(" ", " ", 0, " ", 1, " ", 2, " ")
    print("  " + "-" * 13)
    for i in range(3):
        print(i, "|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("  " + "-" * 13)


def move(board: list, player: bool):
    if player:
        player_sym = "X"
        print("Ходят крестики")
    else:
        player_sym = "0"
        print("Ходят нолики")

    valid_input = False
    while not valid_input:
        i = input("Введите номер строки(0, 1 или 2):")
        j = input("Введите номер столбца(0, 1 или 2):")
        if i.isnumeric() and j.isnumeric() and 0 <= int(i) < 3 and 0 <= int(i) < 3:
            valid_input = True
            i, j = int(i), int(j)
        else:
            print("ОШИБКА. Вы ввели некоректное значение.")

    if board[i][j] != "-":
        print("ОШИБКА")
        print("Данная позиция уже занята")
        return move(board, player)
    else:
        player = not player
        board[i][j] = player_sym
        return board, player


def check_win(board: list, player: bool):
    stop_game = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-" or \
                board[0][i] == board[1][i] == board[2][i] != "-":
            stop_game = True
    if board[0][0] == board[1][1] == board[2][2] != "-" or \
            board[0][2] == board[1][1] == board[2][0] != "-":
        stop_game = True

    end_game = True
    for i in board:
        for j in i:
            if j == "-" or not end_game:
                end_game = False
                break
    if stop_game:
        if player:
            print("Победили крестики!")
        else:
            print("Победили нолики!")
        return True
    elif end_game:
        print("Ничья!")
        return True
    else:
        return False


while True:
    board_print(board)
    board, player = move(board, player)
    print("=" * 20)
    if check_win(board, not player):
        board_print(board)
        break
