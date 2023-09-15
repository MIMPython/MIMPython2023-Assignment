'''
a)Viết chương trình nhập vào số n, chỉ dừng khi nhập n trong khoảng 0 đến 9
b)Thiết kế chương trình kéo búa bao
'''
import getpass


#a
n=int(input())
while not n in range(0,10):
    print("Invalid")
    n = int(input())


#b
def rock_paper_scissors(p1,p2): #Kiểm tra các truường hợp có thể xảy ra
    if p1 == "Bua" and p2 == "Keo":
        print("P1 win")
    elif p1 == "Keo" and p2 == "Bua":
        print("P2 win")
    elif p1 == "Bao" and p2 == "Bua":
        print("P1 win")
    elif p1 == "Bua" and p2 == "Bao":
        print("P2 win")
    elif p1 == "Keo" and p2 == "Bao":
        print("P1 win")
    elif p1 == "Bao" and p2 == "Keo":
        print("P2 win")

p1 = getpass.getpass("Player 1's turn: ")
p2 = getpass.getpass("Player 2's turn: ")

print("P1 chose: ",p1)#Ẩn đi input của người chơi
print("P2 chose: ",p2)

rock_paper_scissors(str(p1),str(p2))

#Chạy code:  python module03_assignment05_student08_DoMinhQuang.py



