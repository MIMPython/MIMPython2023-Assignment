# Bài tập 5:
# rock-paper-scissors game.

def main():
    # "R" = Rock
    # "P" = Paper
    # "S" = Scissors
    print("In case you choose Rock, please type 'R'. If it's Paper, type 'P'. If it's Scissors, type 'S'")
    player1 = input().upper()
    player2 = input().upper()
    data_check_1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check_1 = any(player1 == i for i in data_check_1) and any(player2 == i for i in data_check_1)
    if  check_1 == False:
        if player1 == "R" and player2 == "P":
            print ("player2 is win")
        elif player1 == "P" and player2 == "S":
            print ("player2 is win")
        elif player1 == "S" and player2 == "R":
            print ("player2 is win")
        elif player1 == "P" and player2 == "R":
            print ("player1 is win")
        elif player1 == "S" and player2 == "P":
            print ("player1 is win")
        elif player1 == "R" and player2 == "S":
            print ("player1 is win")
        elif player1 == player2:
            print ("Hòa !")
        else:
            print("please enter in the correct format.")
    else:
        return None
    
if __name__ == "__main__":
    main()
# Cách tiếp cận trên sẽ phải cần đảm bảo sự bí mật chủ động từ 2 người chơi,
# nếu không người chơi sau đã biết người chơi trước chọn cách chơi gì.


# Ngoài ra nếu muốn bảo mật hơn thì ta có thể cho 2 bạn chơi trò này theo cách ẩn danh như sau:
import random
def main_1():
    choices = ["R", "P", "S"]
    player1 = random.choice(choices)
    player2 = random.choice(choices)
    data_check_1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check_1 = any(player1 == i for i in data_check_1) and any(player2 == i for i in data_check_1)
    if  check_1 == False:
        if player1 == "R" and player2 == "P":
            print ("player2 is win")
        elif player1 == "P" and player2 == "S":
            print ("player2 is win")
        elif player1 == "S" and player2 == "R":
            print ("player2 is win")
        elif player1 == "P" and player2 == "R":
            print ("player1 is win")
        elif player1 == "S" and player2 == "P":
            print ("player1 is win")
        elif player1 == "R" and player2 == "S":
            print ("player1 is win")
        elif player1 == player2:
            print ("Draw game!")
        else:
            print("please enter in the correct format.")
    else:
        return None
    
if __name__ == "__main__":
    main_1()