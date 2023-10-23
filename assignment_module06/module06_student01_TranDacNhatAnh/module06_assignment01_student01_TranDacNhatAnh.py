# Mục tiêu của bài tập là so sánh tốc độ khi sử dụng các phép toán tính tổng khi sử dụng thư viện Numpy với khi sử dụng các cách 
# cài đặt thủ công.

import random as rd
import numpy as np
import time
import csv


testResults = []
for test in range(100):
    # (a)
    # Tạo một mảng 2 chiều gồm m hàng và n cột, các hàm tính tổng như đề bài yêu cầu sẽ tính toán sử dụng mảng này.
    def generateArray(m: int, n: int):
        someArray = [[rd.randint(0, 10000) for _ in range(n)] for _ in range(m)]
        return someArray

    startTime1 = time.perf_counter()
    arr1 = generateArray(3, 4)
    endTime1 = time.perf_counter()
    generateArrayTime = endTime1 - startTime1

    # (b)
    # Tính tổng các số thuộc cùng một cột (được đánh số 0, 1, ..., n-1)
    def sumInAColumnOfArray(array: list[list[int]]):
        nRow = len(array)
        nCol = len(array[0])
        total = [0 for _ in range(nCol)]
        for row in range(nRow):
            for col in range(nCol):
                total[col] += array[row][col]
        return total

    startTime2 = time.perf_counter()
    total1 = sumInAColumnOfArray(array=arr1)
    endTime2 = time.perf_counter()
    calculateTotal1Time = endTime2 - startTime2

    # (c)
    # Thực hiện các yêu cầu tương tự (a) và (b) sử dụng kiểu dữ liệu np.ndarray
    def generateNumpyArray(m: int, n: int):
        numpyArray = np.array([rd.randint(0, 10000) for _ in range(m*n)]).reshape(m, n)
        return numpyArray

    startTime3 = time.perf_counter()
    arr2 = generateNumpyArray(3, 4)
    endTime3 = time.perf_counter()
    generateNumpyArrayTime = endTime3 - startTime3

    def sumInAColumnOfNumpyArray(array: np.ndarray):
        total = array.sum(axis=0)
        return total

    startTime4 = time.perf_counter()
    total2 = sumInAColumnOfNumpyArray(array=arr2)
    endTime4 = time.perf_counter()
    calculateTotal2Time = endTime4 - startTime4

    startTime5 = time.perf_counter()
    total3 = sumInAColumnOfArray(array=arr2)
    endTime5 = time.perf_counter()
    calculateTotal3Time = endTime5 - startTime5

    result = {
        'Test': test,
        'Generate time without Numpy': generateArrayTime,
        'Generate time by Numpy': generateNumpyArrayTime,
        'Sample array' : arr2,
        'Sum of columns without Numpy': total3,
        'Calculate time without Numpy': calculateTotal3Time,
        'Sum of columns by Numpy': total2,
        'Calculate time by Numpy': calculateTotal2Time
    }
    testResults.append(result)

resultColumns = ['Test', 'Generate time without Numpy', 'Generate time by Numpy', 'Sample array', 'Sum of columns without Numpy', 
                'Calculate time without Numpy', 'Sum of columns by Numpy', 'Calculate time by Numpy']

with open('additionalFolder\module06_assignment01_student01_TranDacNhatAnh.csv', 'w', newline = '\n') as file:
    writer = csv.DictWriter(file, fieldnames = resultColumns)
    writer.writeheader()
    writer.writerows(testResults)

