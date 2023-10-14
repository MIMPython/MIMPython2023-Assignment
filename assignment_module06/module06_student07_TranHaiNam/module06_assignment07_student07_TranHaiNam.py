import numpy as np 

path = 'C:\module06_student07_TranHaiNam\\data.txt'
data = np.loadtxt(path, dtype = int, delimiter= ' ')
data.resize(20,20)

def left_right(data):
    maximum1  = 0   
    for i in range(17):
        for j in range(17):
            left_right = data[i][j] * data[i][j+1] * data[i][j+2] * data[i][j+3]
            maximum1 = max(maximum1, left_right)
    return maximum1

def column(data):
    maximum2 = 0
    for i in range(17):
        for j in range(20):
            column = data[i][j] * data[i+1][j] * data[i+2][j] * data[i+3][j]
            maximum2 = max(maximum2, column)
    return maximum2

def main_diagonally(data):
    maximum3 = 0
    for i in range(17):
        for j in range(17):
            main_diagonally = data[i][j] * data[i+1][j+1] * data[i+2][j+2] * data[i+3][j+3]
            maximum3 = max(maximum3, main_diagonally)
    return maximum3

def secondary_diagonally(data):
    maximum4 = 0
    for i in range(17):
        for j in range(17):
            secondary_diagonally = data[i][-j] * data[i+1][-j-1] * data[i+2][-j-2] * data[i+3][-j-3]
            maximum4 = max(maximum4, secondary_diagonally)
    return maximum4

def theGreatest_product(data):
    return max(left_right(data), column(data), main_diagonally(data), secondary_diagonally(data))


print(theGreatest_product(data)) #70600674