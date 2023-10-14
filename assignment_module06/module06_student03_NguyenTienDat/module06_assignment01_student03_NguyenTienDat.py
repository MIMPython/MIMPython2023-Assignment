# Bài tập 1:

# Normal:
import random
random.seed(31)
def create_matrix_normal(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(1, 10))
        matrix.append(row)
    return matrix # output (m=3, n=5, seed=31): [[1, 8, 2, 7, 3], [1, 3, 2, 9, 4], [3, 3, 1, 1, 3]]

def sum_column_normal(input):
    result = []
    for i in range(len(input[0])):
        temp = 0
        for j in range(len(input)):
            temp += input[j][i] 
        result.append(temp)
    return result

def sum_row_normal(input):
    result = []
    for i in range(len(input)):
        temp = 0
        for j in range(len(input[0])):
            temp += input[i][j]
        result.append(temp)
    return result


# Numpy:
import numpy as np
np.random.seed(31)
def create_matrix_numpy(m, n):
    return np.random.randint(1,10, (m,n))
# input(m=3,n=5,seed=31): [[3 8 1 3 8]
#                          [7 7 3 3 2]
#                          [8 2 2 5 7]]

def sum_column_numpy(input):
    return np.sum(input, axis=0) 

def sum_row_numpy(input):
    return np.sum(input, axis=1)
 
 
# statistical comparison results:
import time
def static_results():
    time_create_matrix_normal = []
    time_sum_column_normal = []
    time_sum_row_normal = []

    time_create_matrix_numpy = []
    time_sum_column_numpy= []
    time_sum_row_numpy= []

    for row in range(500, 505):
        for col in range(500, 505):
            start_1 = time.time()
            creat_matrix = create_matrix_normal(row, col)
            end_1 = time.time()

            start_2 = time.time()
            sum_matrix_col = sum_column_normal(creat_matrix)
            end_2 = time.time()

            start_3 = time.time()
            sum_matrix_rows = sum_row_normal(creat_matrix)
            end_3 = time.time()

            start_4 = time.time()
            creat_matrix_by_numpy = create_matrix_numpy(row, col)
            end_4 = time.time()

            start_5 = time.time()
            sum_column_matrix_by_numpy = sum_column_numpy(creat_matrix_by_numpy)
            end_5 = time.time()
            
            start_6 = time.time()
            sum_row_matrix_by_numpy = sum_row_numpy(creat_matrix_by_numpy)
            end_6 = time.time()

            time_create_matrix_normal.append(end_1 - start_1)
            time_sum_column_normal.append(end_2 - start_2)
            time_sum_row_normal.append(end_3 - start_3)

            time_create_matrix_numpy.append(end_4 - start_4)
            time_sum_column_numpy.append(end_5 - start_5)
            time_sum_row_numpy.append(end_6 - start_6)
            
    print("-"*201)
    print("|{}".format("time create matrix normal"), "|{}".format("time caculate sum of column normal"),\
        "|{}".format("time caculate sum of row normal"), "|{}".format("time create matrix by numpy"),\
        "|{}".format("time calculate sum of column by numpy"), "|{}".format("time calculate sum of row by numpy"), "|")
    print("-"*201)
    
    for i in range(len(time_create_matrix_normal)):
        print("|{: <25}".format(time_create_matrix_normal[i]), "|{: <34}".format(time_sum_column_normal[i]),\
            "|{: <31}".format(time_sum_row_normal[i]), "|{: <27}".format(time_create_matrix_numpy[i]),\
            "|{: <37}".format(time_sum_column_numpy[i]), "|{: <34}".format(time_sum_row_numpy[i]), "|")
    
    print("-"*201)
      
if __name__ == "__main__":  
    static_results()
            
