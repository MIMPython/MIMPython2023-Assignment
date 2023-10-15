import random
import numpy as np
import matplotlib.pyplot as plt
import time


def create_matrix_2D(m, n):
    '''
    hàm nhận vào m,n và trả về bảng 2 chiều kiểu list, chứa các số tự nhiên ngẫu nhiên
    từ 0-1000
    '''
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 1000))
        matrix.append(row)
    return matrix


def get_sum_of_column(matrix):
    '''
    tính tổng mỗi cột của ma trận 2 chiều
    '''
    column_sums = []
    for column in range(len(matrix[0])):
        sum = 0
        for row in range(len(matrix)):
            sum += matrix[row][column]
        column_sums.append(sum)
    return column_sums


def create_matrix_2D_np(m, n):
    '''
    sử dụng np.ndarray để tạo ma trận 2 chiều m hàng, n cột
    '''
    # matrix = np.ndarray(shape =(m,n), dtype = np.int32)
    matrix = np.random.randint(0, 1001, size=(m, n))
    return matrix


def get_sum_of_colum_np(matrix):
    '''
    tính tổng cột ma trận 2 chiều sử dụng np.sum()
    '''
    return np.sum(matrix, axis=0)


def test_time_without_numpy():
    '''
    trả về khoảng thời gian của hàm thực thi
    '''
    matrix = create_matrix_2D(m, n)
    start_time = time.perf_counter()
    result = get_sum_of_column(matrix)
    end_time = time.perf_counter()
    return end_time - start_time


def test_time_with_numpy():
    '''
    trả về khoảng thời gian của hàm thực thi
    '''
    matrix = create_matrix_2D_np(m, n)
    start_time = time.perf_counter()
    result = get_sum_of_colum_np(matrix)
    end_time = time.perf_counter()
    return end_time - start_time


if __name__ == '__main__':
    print('Enter m,n >= 1000 to test result')
    m = int(input('Enter the number of rows: '))
    n = int(input('Enter the number of columns: '))
    number_tests = int(input('Enter the number of tests: '))
    # print('*'*10)
    # matrix = create_matrix_2D(m,n)
    # print(matrix)
    # result = get_sum_of_column(matrix)
    # print(result)
    # print('*'*10)
    # matrix_use_np = create_matrix_2D_np(m,n)
    # print(matrix_use_np)
    # result1 = get_sum_of_colum_np(matrix_use_np)
    # print(result1)
    # print('*'*10)
    times_without_numpy = []
    times_with_numpy = []
    # cho 20 lần thử nghiệm
    for i in range(number_tests):
        time_without_using_numpy = test_time_without_numpy()
        times_without_numpy.append(time_without_using_numpy)
        time_with_using_numpy = test_time_with_numpy()
        times_with_numpy.append(time_with_using_numpy)
    # Vẽ biểu đồ so sánh

    fig, ax = plt.subplots()
    kwg1 = {
        'marker': 'o', 'color': 'blue', 'linestyle': '-', 'linewidth': 2, 'markersize': 5, 'label': 'Caculate without numpy'

    }
    kwg2 = {
        'marker': 'D', 'color': 'pink', 'linestyle': '--', 'linewidth': 2, 'markersize': 5, 'label': 'Caculate using numpy'

    }
    ax.plot(range(1, number_tests+1), times_without_numpy, **kwg1)
    ax.plot(range(1, number_tests + 1), times_with_numpy, **kwg2)
    ax.set(title='Compare implement time', xlabel='The number of tests',
           ylabel='Time implement (seconds)', xticks=range(1, number_tests+1))
    ax.legend()
    plt.savefig('additionalFolder/module06_assignment01_student06_NguyenThiMen_result_ex1.jpg', format = 'jpg')
    plt.show()
    # kết quả biểu đồ ở additionFolder chạy với matrix 2D cỡ 1000x1000, test 10 lần
