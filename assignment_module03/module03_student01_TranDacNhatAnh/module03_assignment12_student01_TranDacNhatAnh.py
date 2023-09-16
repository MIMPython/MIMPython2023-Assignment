from math import sqrt
import numpy as np
def spiral(n):
    side = int(sqrt(n-1))+1 # Kích thước bảng
    center = int((n-1)/2)   # Tâm bảng: board[center][center] sẽ là vị trí của 1
    board = np.arange(side*side).reshape(side, side) # Tạo 1 mảng để điền số vào
    for i in range(side):   # Mảng hiện tại có dạng [[0 1 ... side-1] [side side+1 ...]...] nên ta thay các số bởi 0 để dễ xử lí 
            for j in range(side):
                board[i][j] = 0
    # Điền các số vào bảng theo lối: quy nạp bảng con cỡ (side-1)*(side-1) (sau đó điền nốt các số còn lại vào 1 hàng 1 cột còn dư)
    if side == 1:
        board[center][center] = 1
        return board 
    else: # Vị trí của "center" tại 2 trường hợp là khác nhau nên ta xét riêng. Nếu n chẵn, 
        adjust = side%2
        m = side-1
        inductiveBoard = spiral(m*m)
        for i in range(m):
            for j in range(m):
                if adjust==0:
                    board[i][j] = inductiveBoard[i][j]
                else:
                    board[i+1][j+1] = inductiveBoard[i][j]
        # Xong bước quy nạp, đến bước điền nốt
        remain = n-(side-1)**2
        for i in range(remain):
            if adjust == 0:
                if i<side:
                    board[side-1][i] = i+(side-1)**2+1
                else:
                    board[side-i-2][side-1] = i+(side-1)**2+1
            else:
                if i<side:
                    board[0][side-i-1] = i+(side-1)**2+1
                else:
                    board[i-side+1][0] = i+(side-1)**2+1
        return board
# Điều chỉnh lại output: các phần tử hiện bằng 0 thì thay bằng ' ', các phần tử có 1 chữ số (d) được in dưới dạng ' d'
def show(row):
    for i in range(len(row)):
        if i+1 == len(row):
            if row[i] == 0:
                print(' ')
            elif row[i]<10:
                d = row[i]
                print(f' {d}')
            else: print(row[i])
        else:
            if row[i] == 0:
                print(' ', end=' ', flush=True)
            elif row[i]<10:
                d = row[i]
                print(f' {d}', end=' ', flush=True)
            else:
                print(row[i], end=' ', flush= True)
board = spiral(14)
for row in board:
    show(row)
#  7  6  5 
#  8  1  4 
#  9  2  3 14
# 10 11 12 13

# Một lời giải mà em cho rằng phức tạp quá mức cần thiết, tuy nhiên hiện em chưa nghĩ ra cách nào để rút ngắn nó.