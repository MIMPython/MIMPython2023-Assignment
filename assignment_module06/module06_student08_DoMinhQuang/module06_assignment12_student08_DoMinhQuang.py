import numpy as np

inputArr = np.array([
    [0, 1, 0],
    [0, 1, 1],
])

def rotate_90_degree(arr):
    ls = list(arr)#biến đổi kiểu mảng số thành kiểu list để dùng được hàm reverse()
    ls.reverse()
    rotated = np.array(ls)
    print(rotated.T)#chuyển vị

rotate_90_degree(inputArr)




