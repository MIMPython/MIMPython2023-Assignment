with open('additionalFolder\module06_assignment07_student01_TranDacNhatAnh.txt', 'r') as file:
    board = file.read().splitlines()
    for row in range(len(board)):
        board[row] = board[row].split()
productsSet = set()
nRow = len(board)
nCol = len(board[0])

for i in range(nRow):
    for j in range(nCol-3):
        lineProduct = int(board[i][j])*int(board[i][j+1])*int(board[i][j+2])*int(board[i][j+3])
        productsSet.add(lineProduct)

for i in range(nRow-3):
    for j in range(nCol):
        lineProduct = int(board[i][j])*int(board[i+1][j])*int(board[i+2][j])*int(board[i+3][j])
        productsSet.add(lineProduct)

for i in range(nRow-3):
    for j in range(nCol-3):
        lineProduct = int(board[i][j])*int(board[i][j+1])*int(board[i][j+2])*int(board[i][j+3])
        productsSet.add(lineProduct)

for i in range(3, nRow):
    for j in range(nCol-3):
        lineProduct = int(board[i][j])*int(board[i-1][j+1])*int(board[i-2][j+2])*int(board[i-3][j+3])
        productsSet.add(lineProduct)

print(max(productsSet)) # 70600674