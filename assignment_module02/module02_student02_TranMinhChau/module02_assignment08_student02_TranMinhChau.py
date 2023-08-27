#Bài tập 8:
#Hình 1: Half Pyramid 
height = 6
symbol = "*"
for row in range(1, height + 1):
    for col in range(1, row + 1):
        print(symbol, end="")
    print()

#Hình 2: Inverted Half Pyramid 
height = 6
symbol = "*"
for row in range(height, 0, -1):
    for col in range(1, row + 1):
        print(symbol, end="")
    print()

#Hình 3: Hollow Inverted Half Pyramid 
height = 6
symbol = "*"
space = " "
for row in range(height, 0, -1):
    for col in range(1, row + 1):
        if row == height or col == 1 or col == row:
            print(symbol, end="")
        else:
            print(space, end="")
    print()

#Hình 4: Full Pyramid
height = 6
symbol = "*"
space = " "   
for row in range(1, height + 1):
    for col in range(1, height * 2):
        if col >= height - row + 1 and col <= height + row - 1:
            print(symbol, end="")
        else:
            print(space, end="")
    print()

#Hình 5: Inverted Full Pyramid
height = 6
symbol = "*"
space = " "
for row in range(height, 0, -1):
    for col in range(1, height * 2):
        if col >= height - row + 1 and col <= height + row - 1:
            print(symbol, end="")
        else:
            print(space, end="")
    print()

#Hình 6:  Hollow Inverted Full Pyramid 
height = 6
symbol = "*"
space = " "
for row in range(1, height + 1):
    for col in range(1, height * 2):
        if row == height or col == height - row + 1 or col == height + row - 1:
            print(symbol, end="")
        else:
            print(space, end="")
    print()
    

