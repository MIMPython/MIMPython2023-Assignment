import random
import time
import numpy


def generateData():
    random.seed(2003)
    width = 10000
    height = 10000
    numbers = [i for i in range(10)]
    selectedNumbers = random.choices(numbers, k=width * height)
    matrix = []
    for i in range(height):
        row = [selectedNumbers[j] for j in range(i * width, (i + 1) * width)]
        matrix.append(row)
    return matrix


def sumNotUsingModule():
    matrix = generateData()
    random.seed(1)
    colIndex = random.randint(0, len(matrix[0]))
    rowIndex = random.randint(0, len(matrix))
    rowSum = 0
    colSum = 0

    start = time.time()
    for term in matrix[rowIndex]:
        rowSum += term
    for subList in matrix:
        colSum += subList[colIndex]
    end = time.time()
    print("Result: rowSum=", rowSum, "colSum=", colSum)
    print("Elapsed time: ", end - start)


def sumUsingModule():
    matrix = generateData()
    random.seed(1)
    colIndex = random.randint(0, len(matrix[0]))
    rowIndex = random.randint(0, len(matrix))
    start = time.time()
    data = numpy.array(matrix)
    rowSums = numpy.sum(data, axis=0)
    colSums = numpy.sum(data, axis=1)
    rowSum = rowSums[rowIndex]
    colSum = colSums[colIndex]
    end = time.time()
    print("Result: rowSum=", rowSum, "colSum=", colSum)
    print("Elapsed time: ", end - start)


if __name__ == "__main__":
    sumUsingModule()
