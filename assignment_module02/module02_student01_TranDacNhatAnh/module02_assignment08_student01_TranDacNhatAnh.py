def HalfPyramid(n):
    board = []
    for i in range(n):
        lst = []
        for j in range(i+1):
            lst.append('*')
        board.append(''.join(lst))
    return board
def InvertedHalfPyramid(n):
    board = HalfPyramid(n)
    board.reverse()
    return board
def HollowInvertedHalfPyramid(n):
    board = []
    for i in range(n):
        lst = []
        if i==0:
            for j in range(n-1):
                lst.append('*')
        else:
            for j in range(n-i-1):
                if j==0 or j==n-i-2:
                    lst.append('*')
                else:
                    lst.append(' ')
        board.append(''.join(lst))
    return board
def FullPyramid(n):
    board = []
    for i in range(n):
        lst = []
        for j in range(n+i):
            if j<(n-1-i) or (j%2)==(n-i)%2:
                lst.append(' ')
            else:
                lst.append('*')
        board.append(''.join(lst))
    return board
def InvertedFullPyramid(n):
    board = FullPyramid(n)
    board.reverse()
    return board
def HollowFullPyramid(n):
    board = []
    for i in range(n):
        lst = []
        if i==(n-1):
            for j in range(n+i):
                if j<(n-i-1) or (j%2)==(n-i)%2:
                    lst.append(' ')
                else:
                    lst.append("*")
        else:
            for j in range(n+i):
                if j==(n+i-1) or j==(n-i-1):
                    lst.append('*')
                else:
                    lst.append(' ')
        board.append(''.join(lst))
    return board
def BuildPyramid(board):
    for i in range(len(board)):
        print(board[i])
# Test
BuildPyramid(HalfPyramid(7))
BuildPyramid(InvertedHalfPyramid(7))
BuildPyramid(HollowInvertedHalfPyramid(7))
BuildPyramid(FullPyramid(7))
BuildPyramid(InvertedFullPyramid(7))
BuildPyramid(HollowFullPyramid(7))
