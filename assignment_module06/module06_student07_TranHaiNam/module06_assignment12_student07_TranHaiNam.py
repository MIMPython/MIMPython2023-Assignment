#a
import numpy as np
def rotate_90degress(matrix):
    row, column = matrix.shape 
    new_matrix = np.zeros(shape=(column,row)) #Tạo ma trận mới (chỉ chứa số 0) với hàng bằng cột, cột bằng hàng của matrix cũ.
    for i in range(row//2):
            matrix[[i]],matrix[[-1-i]] = matrix[[-1-i]],matrix[[i]] #sắp xếp lại hàng ma trận với thứ tự mới (ví dụ: hàng 1 xuống hàng 4, hàng 4 lên hàng)    
    for i in range(column):
        for j in range(row):
            new_matrix[i][j] = matrix[j][i]
    return new_matrix

matrix = np.array([
    
    [6, 5, 4, 3],
    [0, 1, 0, 4],
    [0, 1, 1, 5],
    [1, 2, 3, 6],
    [7, 8, 9, 10]
])
print(rotate_90degress(matrix))

""" Ví dụ theo ma trận trên:
    [6, 5, 4, 3],      [7,8,9,10]       [7,1,0,0,6]
    [0, 1, 0, 4],      [1,2,3,6]        [8,2,1,1,5]
    [0, 1, 1, 5],  --> [0,1,1,5]  -->   [9,3,1,0,4]
    [1, 2, 3, 6],      [0,1,0,4]        [10,6,5,4,3]
    [7, 8, 9, 10]      [6,5,4,3]

"""
#b: Chưa hoàn thành