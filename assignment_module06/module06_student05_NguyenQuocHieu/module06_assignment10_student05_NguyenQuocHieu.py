import numpy
import random
import time


def eliminateGaussianJordan(matrix: numpy.ndarray) -> numpy.ndarray:
    numCols, numRows = matrix.shape
    index = 0
    matrix = matrix.astype(numpy.float64)
    while index < numCols:
        pivot = matrix[index]
        if pivot[index] != 0:
            for i in range(index + 1, numCols):
                matrix[i] = numpy.subtract(
                    matrix[i], matrix[i][index] / pivot[index] * pivot, dtype=numpy.float64)
        print("Step by step: \n", matrix)
        index += 1
    return matrix


def getDeterminant(matrix: numpy.ndarray) -> float:
    transformed_matrix = eliminateGaussianJordan(matrix)
    print("Eliminated: \n", transformed_matrix)
    value = 1.0
    for i in range(matrix.shape[0]):
        value *= transformed_matrix[i][i]
    return value


def generateMatrix(size: int) -> numpy.ndarray:
    matrix = numpy.zeros((size, size), dtype=numpy.int64)
    for i in range(size):
        for j in range(size):
            matrix[i][j] = random.randint(0, 10)
    return matrix


def compareTime():
    matrix = generateMatrix(size=100)
    print("Matrix: \n", matrix)
    start = time.time()
    det1 = getDeterminant(matrix.copy())
    end = time.time()
    print("Determinant value: ", det1)
    print("Elapsed time not using module: ", end - start)
    start1 = time.time()
    det2 = numpy.linalg.det(matrix.copy())
    end1 = time.time()
    print("Determinant value: ", det2)
    print("Elapsed time using module: ", end1 - start1)


if __name__ == "__main__":
    compareTime()
    # Thời gian chênh lệch giữa việc dùng thư viện và không dùng thư viện là không đáng kể
