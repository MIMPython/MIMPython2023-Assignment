#a
n=int(input())
while not n in range(0,10):
    print("Invalid")
    n=int(input())


#b
def rock_paper_scissors(p1,p2):
    if p1=="Bua" and p2=="Keo":
        print("P1 win")
    elif p1=="Keo" and p2=="Bua":
        print("P2 win")
    elif p1=="Bao" and p2=="Bua":
        print("P1 win")
    elif p1=="Bua" and p2=="Bao":
        print("P2 win")
    elif p1=="Keo" and p2=="Bao":
        print("P1 win")
    elif p1=="Bao" and p2=="Keo":
        print("P2 win")

try:
    with open("additionalFolder/module03_assignment05_student08_DoMinhQuang_data1.txt", "r") as f:
        p1=str(f.read())
except Exception as e:
    print(e)

try:
    with open("additionalFolder/module03_assignment05_student08_DoMinhQuang_data2.txt", "r") as f:
        p2=str(f.read())
except Exception as e:
    print(e)

print("P1 chose: ",p1)
print("P2 chose: ",p2)

rock_paper_scissors(str(p1),str(p2))


"module03_assignment05_student08_DoMinhQuang_data1.txt"
"module03_assignment05_student08_DoMinhQuang_data2.txt"
