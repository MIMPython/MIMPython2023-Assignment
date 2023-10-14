import numpy


def eliminateGaussianJordan(matrix: numpy.ndarray):
    numCols, numRows = matrix.shape
    index = 0
    matrix = matrix.astype(numpy.float64)
    while index < numCols:
        pivot = matrix[index]
        if pivot[0] != 0:
            for i in range(index + 1, numCols):
                matrix[i] = numpy.subtract(
                    matrix[i], matrix[i][0] / pivot[0] * pivot, dtype=numpy.float64)
        index += 1
    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [3 / 2, 2, 4],
              [2, 4, 6.5]]
    matrix = numpy.array(matrix, dtype=numpy.float64)
    print("Result: ", eliminateGaussianJordan(matrix))
