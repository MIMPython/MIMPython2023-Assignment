import getpass
import time

''' Câu a Viết một chương trình sao cho nó dừng lại khi người dùng nhập
vào đúng một chữ số trong khoảng từ 0 đến 9'''
def a():
    boolean = False
    while not boolean:
        number = int(input("Enter number from 0 to 9: "))
        if number >=0 and number <= 9:
            boolean = True

# Câu b Trò chơi kéo - búa - bao 
def player_choice(player_name):
    while True:
        choice = getpass.getpass(f'{player_name},Enter a number from 1 to 3: ')
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                return choice
            else:
                print('Invalid selection. Please choose again.')
        except ValueError: # occurs when a correct argument type but an incorrect value is supplied to a function
            print('Wrong input character. Please choose again.')
        except Exception as e: 
            print(f'Error {e}. Please choose again.')
        

def check_winner(player1, player2):
    if player1 == player2:
        return 0
    elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
        return 1
    else:
        return 2
    

def get_message(result, player1_name, player2_name):
    if result == 0:
        return 'Draw'
    elif result == 1:
        return f'{player1_name} win!'
    else:
        return f'{player2_name} win!'
    

def is_timeout(start_time, time_limit):
    return time.time() - start_time > time_limit


def b():
    time_limit = 5 # Each player only has 5 seconds to choose turn.
    print('This is a rock paper scissors game.')
    player1_name = str(input('Enter player 1 name: '))
    player2_name = str(input('Enter player 2 name:'))
    print('1. scissors')
    print('2. rock')
    print('3. paper')
    print('Let\'s start game.')
    while True:
        player1_choice = player_choice(player1_name)
        start_time = time.time()

        if is_timeout(start_time, time_limit):
            print(f'{player1_name} wasted long time,{player2_name} wins!')
            break
        
        player2_choice = player_choice(player2_name)
        start_time = time.time()

        if is_timeout(start_time, time_limit):
            print(f'{player2_name} wasted long time,{player1_name} wins!')
            break

        result = check_winner(player1_choice, player2_choice)
        print(get_message(result, player1_name, player2_name))
        print(f'{player1_name} chose:{player1_choice} ')
        print(f'{player2_name} chose:{player2_choice}')

        play_again = input('Do you want to play again? (YES/NO):')
        if play_again.upper() != 'YES':
            break   
b()
