
from getpass import getpass

#a
def program_stop():
    str1 = "\nThe program will stop if you choose a right number between one to nine"
    str1 += " \nyour number is:"
    number=""
    while number != "5":
        number=input(str1)
        if number == "5":
            break
program_stop()

#b
choice = {"kéo" : 0, "búa" : 1, "bao" : 2}

def player_choice(): #Nhập lựa chọn người chơi
    player_input = int(getpass("Lựa chọn của bạn là: "))
    while player_input not in choice.values():
            palyer_input = getpass("Lựa chọn không hợp lệ, hãy chọn lại: ")
    return player_input

def check_win(player1,player2): #điều kiện thắng
     check_tie = player1 - player2
     if player1 == 0 and check_tie != 0:
          if player2 ==  2:
               return True #người thứ nhất thắng
          else:
               return False #người thứ hai thắng
     elif player1 == 1 and check_tie != 0:
          if player2 == 0:
               return True
          else:
               return False
     elif player1 == 2 and check_tie != 0:
          if player2 == 1:
               return True
          else:
               return False

def gameplay():
     while True:
          print(f"\n{choice}")
          print("Lựa chọn của người chơi thứ nhất")
          player1 = player_choice()
          print("Lựa chọn của người chơi thứ hai")
          player2 = player_choice()
          if player1 == player2:
               print( "game đấu hòa")
          else:
               if check_win(player1,player2):
                    print("Người chơi nhất thắng")
               else:
                    print("Người chơi thứ hai thắng")
          if input(" Gõ 'yes' nếu muốn chơi lại, gõ 'no' nếu không muốn ") != "yes":
               break
          
gameplay()
               

                                





          
               
     



        