# Bài tập 2:
import numpy as np
import time
import matplotlib.pyplot as plt
np.random.seed(31)
# Check matrix A
def check_matrix(A):
    # Tính định thức của ma trận A
    A = np.array(A)
    determinant = np.linalg.det(A)

    # Kiểm tra xem ma trận có suy biến hay không
    if determinant == 0:
        raise ValueError("Ma trận là ma trận suy biến, nên không giải được")
    
def swap_rows(M, row1, row2):
    """Hàm hoán đổi hai hàng của ma trận."""
    M[row1], M[row2] = M[row2], M[row1]

def find_max_row(M, col, n):
    """Hàm tìm hàng có giá trị tuyệt đối lớn nhất tại cột col."""
    max_row = col
    for i in range(col+1, n):
        if abs(M[i][col]) > abs(M[max_row][col]):
            max_row = i
    return max_row

# Normal:
# solving linear equations:
# A is a square matrix (A has length is n) and b is the vector (nx1)
# Tóm tắt phương thức này trong additionlFolder
def linear_equation_non_numpy(A, b):
    A = A.tolist()
    n = len(A)
    M = list(map(list, A))
    
    try:
        check_matrix(A)
        # Tạo ma trận M bằng cách ghép ma trận A với b (b đóng vai trò như là một cột của ma trận A)
        for i in range(n):
            M[i].append(b[i])
        
        # Khử Gauss - Jordan
        for i in range(n):
            # Tìm và hoàn đổi vị trí hàng có giá trị đầu tiên lớn nhất
            max_row = find_max_row(M, i, n)
            swap_rows(M, i, max_row)

            # Chia cả hàng đó cho số hạng đứng đầu
            factor = M[i][i]
            for j in range(i, n + 1):
                M[i][j] /= factor

            # Đưa các hàng còn lại trong cột về 0
            for k in range(n):
                if k != i:
                    factor = M[k][i]
                    # Chia cả hàng đó cho số hạng đứng đầu
                    for j in range(i, n + 1):
                        M[k][j] -= factor * M[i][j]
        
        # Get result:
        result = []
        for _ in range(n):
            result.append(M[_][n])
        
        return result
    except ValueError as e:
        return e 


# Numpy:        
def linear_equation_numpy(A, b):
    try:
        A = np.array(A)
        b = np.array(b)
        return np.linalg.solve(A, b)
    except ValueError as e:
        return e
    except np.linalg.LinAlgError as e:
        return e
        
# # Example usage:
# A = [[8, 4, 2, 0], 
#      [4, 10, 5, 4], 
#      [2, 5, 6.5, 4], 
#      [0, 4, 4, 9]]
# b = [24, 32, 26, 21]

# A = np.random.randint(1, 10, (50, 50))
# b = np.random.randint(1, 10, 50)
# # print(f"Solution x = {linear_equation_non_numpy(A, b)}")
# # print(f"Solution x = {linear_equation_numpy(A, b)}")
# output_1 = np.array(linear_equation_non_numpy(A, b))
# output_2 = np.array(linear_equation_numpy(A, b))
# result = abs(output_1 - output_2)
# print(result)
# # print(output_1[1])
# # print(output_2[1])
# # print(abs(output_1[1]-output_2[1]))
# print(np.mean(result))

def status_results():
    time_caculate_linear_equation_non_numpy = []
    time_caculate_linear_equation_numpy = []
    error_methods = []
    for i in range(2,100):
        A = np.random.randint(1, 10, (i,i))
        b = np.random.randint(1, 10, i)
        # caculate the time to run linear_equation_non_numpy function    
        begin_1 = time.time()
        linear_equation_non_numpy(A,b)
        end_1 = time.time()
        
        # caculate the time to run linear_equation_numpy function  
        begin_2 = time.time()
        linear_equation_numpy(A,b)
        end_2 = time.time()
        
        # error calculation
        output_1 = np.array(linear_equation_non_numpy(A, b))
        output_2 = np.array(linear_equation_numpy(A, b))
        result = abs(output_1 - output_2)
        
        time_caculate_linear_equation_non_numpy.append(end_1-begin_1)
        time_caculate_linear_equation_numpy.append(end_2-begin_2)
        error_methods.append(np.mean(result))
    return time_caculate_linear_equation_non_numpy, time_caculate_linear_equation_numpy, error_methods

time_caculate_linear_equation_non_numpy, time_caculate_linear_equation_numpy, error_methods = status_results()
def result_visualization(time_caculate_linear_equation_non_numpy, time_caculate_linear_equation_numpy, error_methods):
    x = np.arange(len(time_caculate_linear_equation_non_numpy))
    y1 = time_caculate_linear_equation_non_numpy
    y1_1 = time_caculate_linear_equation_numpy
    y2 = error_methods
    
        
    # Create a figure and a set of subplots
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # First subplot
    ax1.plot(x, y1, 'r-', label='Non numpy')  
    ax1.plot(x, y1_1, 'b-',label='Numpy')
    ax1.set_title('Compare between numpy and normal')
    ax1.set_xlabel('Index')
    ax1.set_ylabel('Value')
    

    # Second subplot
    ax2.plot(x, y2) 
    ax2.set_title('Error caculation')
    ax2.set_xlabel('Index')
    ax2.set_ylabel('Value')

    plt.legend()
    # Adjust the layout
    plt.tight_layout()

    # Show the plot
    plt.show()
    
result_visualization(time_caculate_linear_equation_non_numpy, time_caculate_linear_equation_numpy, error_methods)
    

        
        
        