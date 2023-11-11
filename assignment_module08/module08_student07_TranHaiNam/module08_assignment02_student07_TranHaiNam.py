import numpy as np
import time
import matplotlib.pyplot as plt

def Gauss_Jordan(matrix,B):
    new_matrix = np.hstack((matrix,B),dtype='float')   
    num_column = len(new_matrix[0])
    num_row = len(new_matrix[:,0])
    if num_row + 1 != num_column:
        raise TypeError(f"This matrix can't be solve'")
    elif np.linalg.det(matrix) == 0:
        raise Exception(f'Infinity roots')  
    
    for i in range(num_row):        
        for j in range(num_column):
            if new_matrix[i][i] == 0: #Trường hợp đường chéo chính có phần tử bằng 0, ta cần đổi hàng đó với hàng phần tử đường chéo đó khác 0
                if new_matrix[j][i] != 0:
                    new_matrix[[i,j]] = new_matrix[[j,i]]
        for j in range(num_row):       
            if i != j: # khử Gauss
                instance = new_matrix[j][i] / new_matrix[i][i]
                for k in range(num_column):
                    new_matrix[j][k] = new_matrix[j][k] - instance * new_matrix[i][k]
    for i in range(num_row):
        if new_matrix[i][i] != 1: # đưa về ma trận bậc thang rút gọn
            new_matrix[i,-1] = new_matrix[i,-1] / new_matrix[i,i]
            new_matrix[i][i] *= 1/new_matrix[i][i]
    return new_matrix[:,-1]
            
def solve_np(matrix,B):
    x = np.linalg.solve(matrix, B)
    return x
# matrix = ([[0, 4, 2, 0], 
#       [4, 0, 6, 4], 
#       [2, 7, 0, 4], 
#       [0, 4, 4, 0] ])
# B = [[2], 
#      [3],
#      [6],
#      [8]]
# print(solve_np(matrix,B))
# print(Gauss_Jordan(matrix,B))

def visualization():
    t = np.linspace(1,50,50)
    with_numpy = []
    without_numpy = []
    for i in range(1,51):
        matrix = np.random.randint(50, size=(i,i),dtype= 'int')
        B = np.random.randint(50,size=(i,1),dtype='int')


        start = time.time()
        function = Gauss_Jordan(matrix,B)
        end = time.time()
        values = end - start
        without_numpy.append(values)

        new_start = time.time()
        new_function = solve_np(matrix,B)
        new_end = time.time()
        new_values = new_end - new_start
        with_numpy.append(new_values)

    fig, ax = plt.subplots(1,1)
    ax.plot(t,without_numpy,label = 'Without Numpy',linestyle = '--')
    ax.plot(t,with_numpy,label = 'Ussing Numpy', linestyle = ':')
    ax.set_xlabel('number')
    ax.set_ylabel('Time(s)')
    ax.grid()
    ax.legend()
    plt.tight_layout()
    plt.show()
    # fig.savefig('statistic.png')
visualization()
    
    
    

