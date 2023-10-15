import numpy as np
import time
from matplotlib import pyplot as plt
#a
def Matrix_2D(m,n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(np.random.randint(0,10**6))
        matrix.append(row)
    return matrix


#b
def sumOFcol(m,n):
    matrix = Matrix_2D(m,n)
    list = []
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += matrix[j][i]
        list.append(sum)
    return list

#e
def sumOFrow(m,n):
    matrix = Matrix_2D(m,n)
    list = []
    print(matrix)
    for i in range(m):
        sum = 0
        for j in range(n):
            sum += matrix[i][j]
        list.append(sum)
    return list


def sumOFrow_Numpy(m,n):
    matrix = Matrix_2D(m,n)
    return np.sum(matrix, axis = 1)
    
    
#c
def Matrix_2D_Numpy(m,n):
    return np.random.randint(10**6, size=(m, n)).astype('float')

def sumOfcol_numpy(m,n):
    matrix = Matrix_2D_Numpy(m,n)
    return np.sum(matrix, axis=0)


#Time run
start = time.time()
Matrix_2D(100,200)
end = time.time()
print(f'Matrix_2D: {end - start }')

start = time.time()
Matrix_2D_Numpy(200,500)
end = time.time()
print(f'Matrix_2D_Numpy: {end - start}')

start = time.time()
sumOFcol(200,500)
end = time.time()
print(f'sumOFcol: {end - start}')

start = time.time()
sumOfcol_numpy(200,500)
end = time.time()
print(f'sumOFcol_Numpy: {end - start}')

#Statistics
Not_Numpy = []
Numpy = []
how_manyTime = []
for i in range(1,30):
    how_manyTime.append(i)    
    start = time.time()
    result_notNumpy =  sumOFcol(100*i,100*i)
    end = time.time()
    Timing = end - start
    Not_Numpy.append(Timing)


    start = time.time()
    result_Numpy = sumOfcol_numpy(100*i,100*i)
    end = time.time()
    Timing_Numpy = end - start
    Numpy.append(Timing_Numpy)
plt.plot(how_manyTime,Not_Numpy,linestyle = '--', label = 'Without Numpy')
plt.plot(how_manyTime, Numpy, linestyle= ':',label = 'Numpy')
plt.title("Statistics")
plt.legend()
plt.savefig('Statistics.png')
plt.show()


        
