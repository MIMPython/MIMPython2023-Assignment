import numpy as np
import time
from matplotlib import pyplot as plt



def fix_error_NaN(matrix): #mình chuyển tất cả phần tử trong ma trận về dạng float nếu không sẽ có lỗi "cannot convert float nan to integer"
    matrix1 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix1.append(float(matrix[i][j]))
    matrix1 = np.array(matrix1)
    matrix1.resize(len(matrix[0]),len(matrix[0]))
    return matrix1


def Gauss_elimination_det(matrix):
    if np.size(matrix,0) != np.size(matrix,1):
        return f'This matrix is not nxn matrix' 
    matrix = fix_error_NaN(matrix)
    det = 1
    num_row_column = len(matrix[0])
    count = 0
    for i in range(num_row_column):        
        for j in range(num_row_column):
            if matrix[i][i] == 0: #Trường hợp đường chéo chính có phần tử bằng 0, ta cần đổi hàng đó với hàng phần tử đường chéo đó khác 0
                if matrix[j][i] != 0:
                    matrix[[i,j]] = matrix[[j,i]] 
                    count += 1 #Mỗi lần đổi thì ta cần nhân với (-1) mũ tương ứng để được định thức ban đầu
                    det *= (-1)**count
            if i != j: # khử Gauss
                instance = matrix[j][i] / matrix[i][i]
                for k in range(num_row_column):
                    matrix[j][k] = matrix[j][k] - instance * matrix[i][k]

    for i in range(num_row_column): #tính định thức
        det *= matrix[i][i] 
    return det

def Det_Numpy(matrix):
    return np.linalg.det(matrix)    

#statistics
without_numpy = []
numpy = []
count = []
for  i in range(1,30):
    matrix = np.random.randint(10*6, size = (5*i,5*i)).astype("float")
    count.append(i)
    
    start = time.time()
    Gauss_elimination_det(matrix)
    end = time.time()
    timing = end - start
    without_numpy.append(timing)

    start = time.time()
    Det_Numpy(matrix)
    end = time.time()
    time_numpy = end - start
    numpy.append(time_numpy)
plt.plot(count,without_numpy, label = "Det without Numpy", linestyle = ":")
plt.plot(count,numpy, label = "Det with Numpy", linestyle = "--" )
plt.legend()
plt.title("Statistics")
plt.xlabel("X")
plt.ylabel("Time(s)")
plt.grid
plt.savefig("Assignment10.png")
plt.show()