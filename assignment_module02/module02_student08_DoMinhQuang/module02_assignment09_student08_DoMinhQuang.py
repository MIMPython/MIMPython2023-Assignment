from random import randint
board=[0,1,2,3,4,5,6,7,8]

def check_line(ch, x1, x2, x3):
    if board[x1] == ch and board[x2] == ch and board[x3] == ch:
        return True
    return False


def checkAll(ch):
    if check_line(ch, 0, 1, 2):
        return True
    if check_line(ch, 3, 4, 5):
        return True
    if check_line(ch, 6, 7, 8):
        return True
    if check_line(ch, 0, 4, 8):
        return True
    if check_line(ch, 6, 4, 2):
        return True
    if check_line(ch, 0, 3, 6):
        return True
    if check_line(ch, 1, 4, 7):
        return True
    if check_line(ch, 2, 5, 8):
        return True

    return False


def printBoard():
    for i in range(0,9,3):
        print('|',board[i],'|',board[i+1],'|',board[i+2],'|')
        print("-------------")
printBoard()
def isEmpty():
    for i in range(9):
       if board[i]!="x" and board[i]!="o":
            return True


while isEmpty():
    player=int(input("Your turn"))
    if board[player]=="x" or board[player]=="o":
        print("Choosen")
    else:
        board[player]="x"

    bot=randint(0,8)
    if board[bot]=="x" or board[bot]=="o":
        pass
    else:
        board[bot]="o"
    printBoard()

    if checkAll("x"):
        print("Player win")
        break

    if checkAll("o"):
        print("Bot win")
        break

if isEmpty()==False:
    if checkAll("x")==False and checkAll("o")==False:
        print("Draw")











