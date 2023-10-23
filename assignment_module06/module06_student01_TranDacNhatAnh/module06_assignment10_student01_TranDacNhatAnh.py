import numpy as np
import time

# Hàm giúp đổi chỗ 2 phần tử trong 1 list (một np.ndarray có thể coi như một list[list])
def swap(lst: list, p1: int, p2: int):
    lst[p1], lst[p2] = lst[p2], lst[p1]
    return lst 

# Hàm "phương pháp khử Gauss"
def gaussEliminationMethod(matrix: np.ndarray):
    nRow = len(matrix)
    nCol = len(matrix[0])
    m = min(nRow, nCol)
    for col in range(m):
        row = col
        while True:
            if row == nRow:
                break
            elif matrix[row][col] == 0:
                row += 1
            else:
                swap(matrix, col, row)
                row = col
                for i in range(row+1, nRow):
                    const = matrix[i][col]
                    for j in range(col, nCol):
                        matrix[i][j] -= matrix[col][j]*(const/matrix[col][col])
                break
    return matrix
def calMatrixDet(matrix: np.ndarray):
    nRow = len(matrix)
    nCol = len(matrix[0])
    if nRow == nCol:
        det = 1
        matrix = gaussEliminationMethod(matrix)
        for i in range(nRow):
            det *= matrix[i][i]
        return det
    else:
        raise ValueError(f'Undefined determination for non-Square matrices.')

