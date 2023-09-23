# Câu b Trò chơi kéo - búa - bao
import getpass
import time


def player_choice(player_name, time_limit):
    # vượt quá thời gian -> None
    start_time = time.time()
    while True:
        choice = getpass.getpass(f'{player_name},Enter a number from 1 to 3: ')
        end_time = time.time()
        if end_time - start_time > time_limit:
            return None
        else:
            try:
                choice = int(choice)
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print('Invalid selection. Please choose again.')
            except ValueError:  # occurs when a correct argument type but an incorrect value is supplied to a function
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


def b():
    time_limit = 5
    print('This is a rock paper scissors game.')
    print(f'Player has {time_limit} seconds to choose')
    player1_name = str(input('Enter player 1 name: ').title())
    player2_name = str(input('Enter player 2 name: ').title())
    print('1. scissors')
    print('2. rock')
    print('3. paper')
    print('Let\'s start game.')
    count_1, count_2, rounds = 0, 0, 0

    while True:

        player1_choice = player_choice(player1_name, time_limit)

        player2_choice = player_choice(player2_name, time_limit)

        if player1_choice is None or player2_choice is None:
            if player1_choice is None:
                print(
                    f'{player1_name} wasted much time to choose.{player2_name.title()} wins')
                count_2 += 1
                rounds += 1
            else:
                print(
                    f'{player2_name} wasted much time to choose.{player1_name.title()} wins')
                count_1 += 1
                rounds += 1
        else:
            result = check_winner(player1_choice, player2_choice)
            if result == 1:
                count_1 += 1
            elif result == 2:
                count_2 += 1
            rounds += 1
            print(get_message(result, player1_name, player2_name))
            print(f'{player1_name} chose:{player1_choice} ')
            print(f'{player2_name} chose:{player2_choice}')
        # trả lại lựa chọn của người dùng
        play_again = input('Do you want to play again? (YES/NO):')
        if play_again.upper() != 'YES':
            break
    # trả về tỉ số
    print(f'Number of rounds played: {rounds}')
    print(f'{player1_name} wins: {count_1}')
    print(f'{player2_name} wins: {count_2}')
    print('Thanks for playing!')


b()
