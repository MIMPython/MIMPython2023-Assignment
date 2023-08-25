def printHalfPyramid():
    print("Half Pyramid")
    for i in range(6):
        line = ""
        for j in range(i + 1):
            line += "*"
        print(line)


def printInvertedHalfPyramid():
    print("Inverted Half Pyramid")
    for i in range(6):
        line = ""
        for j in range(6 - i):
            line += "*"
        print(line)


def printHollowInvertedHalfPyramid():
    print("HollowInvertedHalfPyramid")
    for i in range(6):
        line = "*"
        if i == 0:
            for j in range(5):
                line += "*"
            print(line)
        elif i == 5:
            print(line)
        else:
            for j in range(6):
                if j != 4 - i:
                    line += " "
                else:
                    line += "*"
            print(line)


def printFullPyramid():
    print("Full Pyramid")
    for i in range(6):
        line = ""
        if i % 2 == 0:
            for j in range(12):
                if 5 - i <= j <= 5 + i and j % 2 != 0:
                    line += "*"
                else:
                    line += " "
            print(line)
        else:
            for j in range(12):
                if 4 - 2 * (i // 2) <= j <= 6 + 2 * (i // 2) and j % 2 == 0:
                    line += "*"
                else:
                    line += " "
            print(line)


def printInvertedFullPyramid():
    print("Inverted Full Pyramid")
    for i in range(6):
        line = ""
        if i % 2 == 0:
            for j in range(12):
                if i - 1 <= j <= 11 - i and j % 2 == 0:
                    line += "*"
                else:
                    line += " "
            print(line)
        else:
            for j in range(12):
                if i <= j <= 10 - i and j % 2 != 0:
                    line += "*"
                else:
                    line += " "
            print(line)


def printHollowFullPyramid():
    print("Hollow Full Pyramid")
    for i in range(6):
        line = ""
        if i != 5:
            for j in range(12):
                if j == 5 - i or j == 5 + i:
                    line += "*"
                else:
                    line += " "
            print(line)
        else:
            for j in range(12):
                if j % 2 == 0:
                    line += "*"
                else:
                    line += " "
            print(line)


if __name__ == "__main__":
    printHalfPyramid()
    printInvertedHalfPyramid()
    printHollowInvertedHalfPyramid()
    printFullPyramid()
    printInvertedFullPyramid()
    printHollowFullPyramid()
