import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation
from time import time
import random
import math

def creat_2D_table(m: int, n: int) -> list:#tạo list 2 chiều
    '''This method is used create a 2 dimensional list

            Parameter
            ---------

            m: int
                    the number of rows
            n: int
                    the number of columns


            Return
            ------

            result: list'''
    # table: list = []
    # for i in range(m):
    #     table.append([])
    #     for j in range(n):
    #         table[i].append(random.randint(1,100))
    table = [[random.randint(1, 100) for j in range(n)] for i in range(m)]
    return table


def minor(matrix: list, i: int, j: int) -> list:
    '''This method is used to find the minor matrix of a matrix

        Parameter
        ---------

        matrix: list
                a 2 dimensional list
        i: int
                position of row
        j: int
                position of column


        Return
        ------

        result: list
                a new matrix after deleting ith row and jth column'''


    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

def cofactor(matrix: list, i: int, j: int) -> float:
    '''This method is used to find the confactor of a matrix

    Parameter
    ---------

    matrix: list
            a 2 dimensional list
    i: int
            position of row
    j: int
            position of column


    Return
    ------

    result: list
                    '''

    m: list = minor(matrix, i, j)
    # Tính phần bù đại số bằng cách nhân với (-1)^(i+j)
    return (-1) ** (i + j) * det(m)

def det(matrix: list) -> float:
    '''This method is used to evaluate the determinant of a matrix

    Parameter
    ---------

    matrix: list
            a 2 dimensional list
    i: int
            position of row
    j: int
            position of column


    Return
    ------

    result: float
            the value of the determinant of the matrix'''

    try:
        if len(matrix) != len(matrix[0]):
            raise Exception('Matrix must be a square matrix!')

    except Exception as e:
        return e

    else:
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        s = 0
        for j in range(len(matrix)):
            s += matrix[0][j] * cofactor(matrix, 0, j)
        return s

parameter = count()
index: list = []
y = []

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 0.00000005)
line, = ax.plot(0, 0)

def eval_error() -> float:
    '''This method is used to find the minor matrix of a matrix

            Parameter
            ---------

            None

            Return
            ------

            result: Error value of determinant'''

    matrix = creat_2D_table(4, 4)
    np_matrix = np.array(matrix)
    error = math.fabs(det(matrix) - np.linalg.det(np_matrix))
    return error

def update(i) -> None:
    error = eval_error()

    index.append(next(parameter))
    y.append(error)

    line.set_xdata(index)
    line.set_ydata(y)

animate = FuncAnimation(plt.gcf(), update, interval = 100)

plt.title('Error between using self-defined function and numpy function')
plt.xlabel('Time')
plt.ylabel('Error')
plt.grid('True')
plt.show()

# domain: np.ndarray = np.arange(-50, 50, 0.1)

# fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1)

# ax = plt.axes(projection = '3d')
#
# def update(i) -> None:
#     ax.set_xlim(0, 105)
#     ax.set_ylim(0, 12)
#     y1: np.ndarray = domain
#     y2: np.ndarray = domain
#     X, Y = np.meshgrid(y1, y2)
#     Z = np.cos(next(parameter) / 1000 * X) * np.sin(next(parameter) / 1000 * Y)
#     ax.cla()
#     ax.plot_surface(X, Y, Z, cmap = 'plasma')
#
#
# animate = FuncAnimation(plt.gcf(), update, interval = 0.1)
# plt.show()



# def update(i) -> None:
#     index.append(next(parameter) / 10)
#     y1 = np.sin(np.array(index))
#     y2 = np.cos(np.array(index))
#
#     ax1.cla()
#     ax1.plot(index, y1)
#
#     ax2.cla()
#     ax2.plot(index, y2)






