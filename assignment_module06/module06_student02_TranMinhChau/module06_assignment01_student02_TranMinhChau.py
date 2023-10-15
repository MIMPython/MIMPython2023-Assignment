# Bài tập 1: (numpy)
#(a) Viết một hàm nhận vào hai số nguyên dương m,n và trả về một bảng hai chiều.
import random

def creat_array(m,n):
    table = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(0, 99))
        table.append(row)
    return table
a = creat_array(3,4)
print(a)

#(b) Viết một hàm tính tổng các số thuộc cùng một cột của một bảng số cho trước.
def total_by_column(input_table):
    table_col = []
    nums = len(input_table[0])
    for col in range(nums):
        total_col = 0
        for row  in input_table:
            total_col += row[col]
        table_col.append(total_col)
    return table_col
b = [[97, 11, 29, 79],
     [2, 76, 14, 73], 
     [95, 35, 19, 51]]
result_b = total_by_column(b)
print(result_b)

#(c) Sử dụng kiểu dữ liệu numpy.ndarray.
import numpy as np

#a.
def creat_array_np(m, n):
    arr = np.random.randint(1, 100, size=(m, n))
    return arr
c = creat_array_np(3,4)
check_the_dimension = c.ndim # Kiểm tra số chiều của bảng
print(c)
print("Số chiều của bảng là: ",check_the_dimension)

#b.
def total_by_column_np(table):
    table_col_np = np.sum(table, axis=0)
    return table_col_np
d = total_by_column_np(b)
print(d)

#(d) So sánh tốc độ thực hiện của hai hàm tính tổng các số theo cột.
import time
# Tính thời gian của cách thủ công
start_time_manual = time.time()
for _ in range(10000):
    total_by_column(b)
end_time_manual = time.time()
elapsed_time_manual = end_time_manual - start_time_manual
print("Thời gian tính của cách thủ công là:", elapsed_time_manual) # Thời gian tính của cách thủ công là: 0.013826847076416016
# Tính thời gian khi sử dụng numpy
start_time_numpy_ = time.time()
for _ in range(10000):
    total_by_column_np(b)
end_time_numpy = time.time()
elapsed_time_numpy = end_time_numpy - start_time_numpy_
print("Thời gian tính khi sử dụng numpy là:",elapsed_time_numpy) # Thời gian tính khi sử dụng numpy là: 0.05529356002807617

# Tốc độ cách tính thủ công nhanh hơn

#(e) So sánh tốc độ thực hiện của hai tính tổng các số thuộc cùng một hàng của bảng số.
# 1. Cách tính thủ công
def total_by_row(input_table):
    table_row = []
    for i in range(len(input_table)):
        total_row = 0
        for j in range(len(input_table[i])):
            total_row += input_table[i][j]
        table_row.append(total_row)
    return table_row
start_time_manual_e = time.time()
for _ in range(10000):
    total_by_row(b)
end_time_manual_e = time.time()
elapsed_time_manual_e = end_time_manual_e - start_time_manual_e
print("Thời gian tính thủ công là: ", elapsed_time_manual_e) # 0.004600048065185547

# 2. Tính bằng numpy
def total_by_row_np(table):
    table_row_np = np.sum(table, axis=1)
    return table_row_np
start_time_numpy_e= time.time()
for _ in range(10000):
    total_by_row_np(b)
end_time_numpy_e = time.time()
elapsed_time_numpy_e= end_time_numpy_e - start_time_numpy_e
print("Thời gian tính bằng np là: ", elapsed_time_numpy_e)# 0.05080866813659668

# Tốc độ cách tính thủ công nhanh hơn