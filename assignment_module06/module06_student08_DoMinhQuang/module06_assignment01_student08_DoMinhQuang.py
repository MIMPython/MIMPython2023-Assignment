'''Bài 1: thực hiện các yêu cầu tính tổng các số thuộc một cột hoặc một hàng bằng 2 cách, là tự viết hàm và cách sự dụng numpy'''


import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from itertools import count

#a)
def creat_2D_table(m: int, n: int) -> list:#tạo list 2 chiều
    # table: list = []
    # for i in range(m):
    #     table.append([])
    #     for j in range(n):
    #         table[i].append(random.randint(1,100))
    table = [[random.randint(1, 100) for j in range(n)] for i in range(m)]
    return table

def print_2D_table(table: list) -> None:
    for row in table:
        for element in row:
            print(element, end = ' ')
        print()

def sum_table(table: list) -> int:#hàm tính tổng list 2 chiều bằng phương thức tự viết
    sum: int = 0
    for row in table:
        for element in row:
            sum: int = sum + element
    return sum



table = creat_2D_table(1000,1000)
# print_2D_table(table)
start_time = time.time()
print('Phương thức tính tổng tự viết: ',sum_table(table))#dùng hàm tự viết
end_time = time.time()
run_time = end_time - start_time
print('Thời gian chạy: ',run_time,'\n')



table_2 = np.array(table)
# print(table_2)
start_time = time.time()
print('Phương thức tính tổng có sẵn của numpy: ',np.sum(table_2))#dùng thư viện
end_time = time.time()
run_time = end_time - start_time
print('Thời gian chạy: ',run_time,'\n')


#b)
array = creat_2D_table(500,500)
def sum_of_col(table: list, j: int) -> int:
    sum: int = 0
    for row in table:
        for i in range(len(row)):
            if i == j:
                sum: int = sum + row[i]
    return sum

def list_sum_of_col(table: list) -> list:#hàm tính tổng giá trị của từng cột
    result: list = []
    for i in range(len(table[0])):
        result.append(sum_of_col(table, i))
    return  result


start_time = time.time()
result = list_sum_of_col(array)
end_time = time.time()
run_time = end_time - start_time
# print(result)
print(f'Thời gian chạy của phương thức tính tổng các cột tự viết: {run_time}\n')


another_array = np.array(array)
start_time = time.time()
# print(np.sum(another_array, 0))
end_time = time.time()
run_time = end_time - start_time
print(f'Thời gian chạy của phương thức tính tổng các cột trong thư viện có sẵn: {run_time}\n')



#c)
def list_sum_of_row(table: list) -> list:
    sum_list = [sum(row) for row in table]
    return sum_list


new_array = creat_2D_table(500, 500)
# print_2D_table(new_array)
start_time = time.time()
result = list_sum_of_row(new_array)
# print(result)
end_time = time.time()
run_time = end_time - start_time

print(f'Thời gian chạy của phương thức tính tổng các hàng tự viết: {run_time}\n')



another_new_array = np.array(new_array)
# print(another_new_array)
start_time = time.time()
another_result = np.sum(another_new_array, 1)
end_time = time.time()
run_time = end_time - start_time

print(f'Thời gian chạy của phương thức tính tổng các hàng trong thư viện có sẵn: {run_time}\n')


#So sánh tốc độ bằng hình vẽ
index = count()
x = []
y1 = []
y2 = []

def draw(i):
    # fig, ax = plt.subplots( nrows = 1, ncols = 2)

    plt.style.use('fivethirtyeight')

    table = creat_2D_table(1000, 1000)

    start_time = time.time()
    sum_table(table)
    end_time = time.time()

    numpy_table = np.array(table)#ép lại table kiểu list vừa tạo thành kiểu mảng xong dùng thư viện cho mảng numpy

    start_time1 = time.time()
    np.sum(numpy_table)
    end_time1 = time.time()

    plt.cla()
    plt.title('Speed comparing')

    x.append(next(index))
    y1.append(end_time - start_time)
    plt.plot(x, y1, marker = 'o', linestyle = '--', label = 'Hand_made function')

    y2.append(end_time1 - start_time1)
    plt.plot(x, y2, marker = 'o', linestyle = '-', label = 'Numpy module')
    plt.legend(loc = 'upper left')


ani = FuncAnimation(plt.gcf(), draw, interval = 100)
plt.show()