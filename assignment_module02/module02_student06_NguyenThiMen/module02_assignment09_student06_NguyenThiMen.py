# print board
board = [0,1,2,3,4,5,6,7,8,9]
def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        print('-'*9)
print_board()

# check winner
def check_winner():
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2]:
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            return True
    # check diagonals
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    return False
        
# change turn
def play_turn(current_player, player1, player2):
    while True:
        print(f'{current_player}, enter your move in [0,8]: ')
        move = int(input())
        if 0<= move  <= 8: 
            if board[move] != 'X' and board[move] != 'O' :
                if current_player == player1:
                    board[move] = 'X'
                elif current_player == player2:
                    board[move] = 'O'
                break
            else:
                print("\nCell is selected. Choose a different cell.")
                continue
        else:
            print('Invalid move. Choose a number between 0 and 8.')
            continue
    return move
    
def main():
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    # print(instruction)
    print(f'{player1}\'s sign is - X')
    print(f'{player2}\'s sign is - O')
    print("Let's start game")
    print_board()
    current_player = player1
    moves=0
    while moves<9:
        move = play_turn(current_player, player1, player2)
        print_board()
        moves += 1
        if check_winner():
            print(f'Congratulations! {current_player} wins!')
            break
        # change turn
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    if check_winner() == False:
        print_board()
        print("It's a draw!")
main()


        



    










