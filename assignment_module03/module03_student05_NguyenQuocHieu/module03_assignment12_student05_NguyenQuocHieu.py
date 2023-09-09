import math
import numpy as np


class EvenSquareDrawer:
    def __init__(self, root: int) -> None:
        self.root = root
        self.matrix = np.zeros((root, root), dtype=np.uint8)

    def drawEachStep(self, n: int) -> np.ndarray:
        paper = np.zeros((n, n), dtype=np.uint8)
        paper[0][0] = n * n - 3 * n + 3
        paper[0][n - 1] = n * n
        paper[n - 1][0] = n * n - 2 * n + 2
        paper[n - 1][n - 1] = n * n - n + 1

        for i in range(1, n - 1):
            paper[i][0] = paper[0][0] + i
        for i in range(1, n - 1):
            paper[n - 1][i] = paper[n - 1][0] + i
        for i in range(1, n - 1):
            paper[i][n - 1] = paper[0][n - 1] - i
        for i in range(1, n - 1):
            paper[0][i] = paper[0][0] - i
        return paper

    def draw(self) -> None:
        index = self.root
        while index > 0:
            gap = (self.root - index) // 2
            paper = self.drawEachStep(n=index)
            for i in range(index):
                for j in range(index):
                    if paper[i][j] != 0:
                        self.matrix[i + gap][j + gap] = paper[i][j]
            index -= 2


class OddSquareDrawer:
    def __init__(self, root: int) -> None:
        self.root = root
        self.matrix = np.zeros((root, root), dtype=np.uint8)

    def drawEachStep(self, n: int) -> np.ndarray:
        paper = np.zeros((n, n), dtype=np.uint8)
        paper[0][0] = n * n - n + 1
        paper[0][n - 1] = n * n - 2 * n + 2
        paper[n - 1][0] = n * n
        paper[n - 1][n - 1] = n * n - 3 * n + 3

        for i in range(1, n - 1):
            paper[i][0] = paper[0][0] + i
        for i in range(1, n - 1):
            paper[0][i] = paper[0][0] - i
        for i in range(1, n - 1):
            paper[i][n - 1] = paper[0][n - 1] - i
        for i in range(1, n - 1):
            paper[n - 1][i] = paper[n - 1][n - 1] - n + 1 + i

        return paper

    def draw(self) -> None:
        index = self.root
        while index > 0:
            gap = (self.root - index) // 2
            paper = self.drawEachStep(n=index)
            for i in range(index):
                for j in range(index):
                    if paper[i][j] != 0:
                        self.matrix[i + gap][j + gap] = paper[i][j]
            index -= 2


def main():
    number = int(input("Input a number: "))
    sqrt = int(math.sqrt(number))
    value = sqrt + 1 if sqrt ** 2 != number else sqrt
    if value % 2 == 0:
        drawer = EvenSquareDrawer(root=value)
    else:
        drawer = OddSquareDrawer(root=value)
    drawer.draw()
    matrix = drawer.matrix
    for i in range(value):
        for j in range(value):
            if matrix[i][j] > number:
                matrix[i][j] = 0
    print(matrix)


if __name__ == "__main__":
    main()

# Mô tả: in ra các số theo hình xoắn ốc
# Chạy code: python module03_assignment12_student05_NguyenQuocHieu.py
# Output:   [[ 7  6  5  0] (với n = 14)
#            [ 8  1  4  0]
#            [ 9  2  3 14]
#            [10 11 12 13]]
