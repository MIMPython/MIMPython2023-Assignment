import numpy as np


def get_determinant(matrix):
    n = matrix.shape[0]
    det = 1
    for i in range(n):
        if matrix[i, i] == 0: # nếu Aii ==0, tìm Aji đầu tiên khác 0, nếu có thì tráo hàng i với j, nếu 0 thì detA = 0
            for j in range(i+1, n):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    det *= -1
                    break
            else:
                return 0
        det *= matrix[i, i]
        # nếu Aii != 0, khử các phần tử trên cột i nằm dưới Aii
        for j in range(i+1, n):
            t = matrix[j, i]/matrix[i, i]
            matrix[j, i:] -= t*matrix[i, i:]
    return det


if __name__ == '__main__':
    array = np.random.randint(0, 11, size=(4, 4))
    matrix = np.array(array, dtype=float)
    print(matrix)
    print(get_determinant(matrix))
    result = np.linalg.det(matrix)
    print(result)
