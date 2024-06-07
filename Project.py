def print_board(board):

    for row in board:
        print("  | ".join(row))
        print("-" * 12)


def check_winner(board, player):


    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all(
            [board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_full(board):

    return all([cell != " " for row in board for cell in row])


def play_game():


    player1_name = input("Введіть ім'я гравця 1 (гратиме за 'X'): ")
    player2_name = input("Введіть ім'я гравця 2 (гратиме за 'O'): ")

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    current_player_name = player1_name

    while True:
        print_board(board)
        print(f"Хід гравця {current_player_name} ({current_player})")


        try:
            row, col = map(int, input("Введіть рядок і стовпець (через пробіл): ").split())
        except ValueError:
            print("Невірний ввід. Будь ласка, введіть два числа через пробіл.")
            continue

        if row not in range(1, 4) or col not in range(1, 4):
            print("Неправильні координати. Введіть числа від 1 до 3.")
            continue


        row, col = row - 1, col - 1

        if board[row][col] != " ":
            print("Ця клітинка вже зайнята. Оберіть іншу.")
            continue


        board[row][col] = current_player


        if check_winner(board, current_player):
            print_board(board)
            print(f"Гравець {current_player_name} ({current_player}) переміг!")
            break


        if is_full(board):
            print_board(board)
            print("Нічия!")
            break


        if current_player == "X":
            current_player = "O"
            current_player_name = player2_name
        else:
            current_player = "X"
            current_player_name = player1_name



if __name__ == "__main__":
    play_game()
