def initialize_board():
    return [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def get_player_move():
    row = int(input("Enter row (0,1,2): "))
    col = int(input("Enter column (0,1,2): "))
    return row, col


def is_move_valid(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def make_move(board, player, row, col):
    board[row][col] = player

def check_winner(board, player):
    return any(all(col == player for col in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2-i] == player for i in range(3))

def is_board_full(board):
    return all(col != ' ' for row in board for col in row)

def play_game():
    current_player = 'X'
    game_board = initialize_board()
    while True:
        print_board(game_board)
        print("Player " + current_player + "'s turn")

        move = get_player_move()
        if is_move_valid(game_board, move[0], move[1]):
            make_move(game_board, current_player, move[0],move[1])

            if check_winner(game_board, current_player):
                print("Player " + current_player + " wins!")
                break
            elif is_board_full(game_board):
                print("Tie!!")
                break
            else:
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
        else:
            print("invalid move!!!!")

play_game()