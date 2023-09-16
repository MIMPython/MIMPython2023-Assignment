# Bài tập 9

Rules_for_Tic_Tac_Toe = """
1. The game is played on a grid that's 3 squares by 3 squares.
2. You are X , your friend is O. Players take turns putting their marks in
empty squares.
3. The first player to get 3 of her marks in a row (up, down, across, or
diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in
a row, the game ends in a tie."""


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    for i in range(3):
        if (all(board[i][j] == player for j in range(3))) or\
        (all(board[i][j] == player for j in range(3))):
            return True
    if (all(board[i][i] == player for i in range(3))) or\
        (all(board[i][2 - i] == player for i in range(3))):
        return True
    return False

def main(board):
    if (all(board[i][j] == " " for i in range(3) for j in range(3))):
        print("Draw game")
    else:
        if check_win(board, 'X'):
            print("The player X wins the game")
        elif check_win(board, 'O'):
            print("The player O wins the game")


board = [
    ["X", " ", "O"],
    ["O", "X", "X"],
    ["O", "O", "X"]
]
print_board(board)
main(board) # The player X wins the game