import os

"""
Luật chơi: Tic-tac-toe 3*3
Hai người chơi lần lượt điền X hoặc O vào bảng 3*3. Cách điền là toạ độ
theo hàng, cột của ô muốn điền. Người chơi sẽ chiến thắng nếu có 3 ô 
cùng hàng, cùng cột hoặc trên đường chéo giống nhau. Ván hoà nếu sau 9
lượt, không có người chiến thắng.
"""

import terminaltables

def draw_table(table):
    """Vẽ bảng với list n*n đã chọn."""
    my_table = terminaltables.SingleTable(table)
    my_table.inner_row_border = True
    print(my_table.table)

def win_condition(list):
    """
    Đầu vào là một list 3*3 chứa thông tin của bảng X/O, đầu ra là
    kết quả. Thắng ứng với True, còn lại là False.
    """
    # Điều kiện hàng hoặc cột
    for i in range(3):
        if (list[i][0] == list[i][1] == list[i][2] != ' ' or
            list[0][i] == list[1][i] == list[2][i] != ' '):
            return True

    # Điều kiện đường chéo
    if (list[0][0] == list[1][1] == list[2][2] != ' ' or 
        list[0][2] == list[1][1] == list[2][0] != ' '):
        return True
    
    return False

def game():
    ttt_table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Game starts !")
    draw_table(ttt_table)

    # Giao diện bảng, nhập giá trị vào bảng
    turn = 0
    while turn >= 0:
        turn += 1
        while True: 
            a, b = input("Enter position for X: ").split()
            try:
                a = int(a)
                b = int(b)
                break
            except ValueError:
                print('Invalid input: box coordinates must be ' 
                      + 'integers. Try again.')
        while ttt_table[int(a) - 1][int(b) - 1] in ['X', 'O']:
            print("Invalid input, enter a different position")
            a, b = input("Enter position for X: ").split()
        ttt_table[int(a) - 1][int(b) - 1] = 'X'
        draw_table(ttt_table)
        if turn >= 5:
            if win_condition(ttt_table) == True: 
                print("X wins !")
                key = input("Continue ? (y/n): ")
                if key == "y": game()
                else: break
            if turn == 9: 
                print("Draw !")
                key = input("Continue ? (y/n): ")
                if key == "y": game()
                else: os.sys.exit()
        turn += 1
        while True: 
            a, b = input("Enter position for O: ").split()
            try:
                a = int(a)
                b = int(b)
                break
            except ValueError:
                print('Invalid input: box coordinates must be ' 
                      + 'integers. Try again.')
        while ttt_table[int(a) - 1][int(b) - 1] in ['X', 'O']:
            print("Invalid input, enter a different position")
            a, b = input("Enter position for O: ").split()
        ttt_table[int(a) - 1][int(b) - 1] = 'O'
        draw_table(ttt_table)
        if turn >= 6:
            if win_condition(ttt_table) == True:
                print("O wins !")
                key = input("Continue ? (y/n): ")
                if key == "y": game()
                else: os.sys.exit()

game()

"""
Ví dụ:
1. X thắng
Input:
X: 1 1 --- O: 1 2 --- X: 2 2 --- O: 3 3 ---
X: 2 1 --- O: 3 1 --- X: 2 3
Final output:
┌───┬───┬───┐
│ X │ O │   │
├───┼───┼───┤
│ X │ X │ X │
├───┼───┼───┤
│ O │   │ O │
└───┴───┴───┘
X wins !

2. Ván hoà:
Input:
X: 1 1 --- O: 2 2 --- X: 1 2 --- O: 1 3 --- X: 3 1 ---
O: 2 1 --- X: 2 3 --- O: 3 2 --- X: 3 3
Final output:
┌───┬───┬───┐
│ X │ X │ O │
├───┼───┼───┤
│ O │ O │ X │
├───┼───┼───┤
│ X │ O │ X │
└───┴───┴───┘
Draw !
"""
