#Bài tập 5: (rock-paper-scissors game)
#(a) 
while True:
    try:
        user_input = int(input("Bạn hãy nhập số trong khoảng từ 0 đến 9: "))
        if 0 <= user_input <= 9:
            print("Bạn đã nhập đúng chữ số trong khoảng từ 0 đến 9.")
            break
        else:
            print("Vui lòng chỉ nhập số từ 0 đến 9.")
    except ValueError:
      print("Vui lòng chỉ nhập số nguyên từ 0 đến 9.")
    
#(b)
def determine_winner(player1, player2):
    if player1 == player2:
        return "Hòa"
    elif (player1 == "kéo" and player2 == "bao") or \
         (player1 == "búa" and player2 == "kéo") or \
         (player1 == "bao" and player2 == "búa"):
        return "Người chơi 1 thắng"
    else:
        return "Người chơi 2 thắng"

while True:
    print("Chào mừng bạn đến với trò chơi kéo - búa - bao!")
    print("Lựa chọn của người chơi 1: kéo, búa, bao")
    player1_choice = input().lower()

    print("Lựa chọn của người chơi 2: kéo, búa, bao")
    player2_choice = input().lower()

    if player1_choice not in ["kéo", "búa", "bao"] or \
       player2_choice not in ["kéo", "búa", "bao"]:
        print("Vui lòng chỉ chọn từ 'kéo', 'búa', hoặc 'bao'.")
    else:
        result = determine_winner(player1_choice, player2_choice)
        print("Kết quả:", result)

    play_again = input("Bạn có muốn chơi lại không? (yes/no): ")
    if play_again.lower() != "yes":
        break

#(c)
import random 

def determine_winner(playerA, playerB):
    if playerA == playerB:
        return "Hòa"
    elif (playerA == "kéo" and playerB == "bao") or \
         (playerA == "búa" and playerB == "kéo") or \
         (playerA == "bao" and playerB == "búa"):
        return "Người chơi A thắng"
    else:
        return "Người chơi B thắng"
    
choices = ["kéo", "búa", "bao"]

while True:
    print("Chào mừng bạn đến với trò chơi kéo - búa - bao!")

    # Người chơi A lựa chọn một lựa chọn ngẫu nhiên
    playerA_choice = random.choice(choices)
    print("Lựa chọn của người chơi B: kéo, búa, bao")
    playerB_choice = input().lower()

    if playerB_choice not in ["kéo", "búa", "bao"]:
        print("Vui lòng chỉ chọn từ 'kéo', 'búa', hoặc 'bao'.")
    else:
        print("Người chơi A đã lựa chọn:", playerA_choice)
        result = determine_winner(playerA_choice, playerB_choice)
        print("Kết quả:", result)

    play_again = input("Bạn có muốn chơi lại không? (yes/no): ")
    if play_again.lower() != "yes":
        break

"""
(d):Có thể hiểu tính công bằng với những cách khác nhau là:
+ Tính công bằng có thể đảm bảo bằng cách không để người chơi B biết lựa chọn của người chơi A trước khi đưa 
ra lựa chọn của mình. Điều này ngăn người chơi B khai thác thông tin này để thay đổi quyết định của mình.
+ Sử dụng yếu tố ngẫu nhiên, ví dụ như hệ thống chọn ngẫu nhiên lựa chọn của người chơi A và không cho phép
người chơi B biết trước. Điều này giúp đảm bảo tính công bằng bởi vì không ai có thể dự đoán trước lựa chọn 
của người chơi A.
+ Cho cả hai người chơi cùng đưa ra lựa chọn cùng một lúc mà không biết lựa chọn của đối phương. Sau đó, kết 
quả sẽ được tiết lộ. Điều này đảm bảo tính công bằng bởi vì không có ai biết trước lựa chọn của đối phương.
"""