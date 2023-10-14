import numpy as np
import time
from module06_assignment01_student06_NguyenThiMen import create_matrix_2D
'''
numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>): trả về giá trị trung bình các phần tử mảng
np.median(a, axis=None, out=None, overwrite_input=False, keepdims=False): trả về trung vị của các phần tử mảng
np.max(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>):  trả về gtln
np.min(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>): trả về gtnn
numpy.argmax(a, axis=None, out=None, *, keepdims=<no value>): trả về chỉ số của gtln
numpy.argmin(a, axis=None, out=None, *, keepdims=<no value>): trả về chỉ số của gtnn
numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0): tạo mảng chứa giá trị phân bố đều
numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None): tạo mảng chứa các giá trị có bước nhảy cố định
np.random.randint(low, high=None, size=None, dtype=int): tạo mảng có kích thước, hình dạng mong muốn, giá trị ngẫu nhiên trg khoảng thiết lập
numpy.where(condition, [x, y, ]/): tìm vị trí của các phần tử trong mảng thỏa mãn 1 điều kiện cụ thể
numpy.isclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False): kiểm tra 2 mảng(các phần tử trong 2 mảng) có gần nhau 
numpy.roots(p): tính nghiệm của 1 đa thức
'''

# Tính giá trị trung bình các phần tử của ma trận
matrix = create_matrix_2D(7, 8)
print(matrix)

# PP thủ công
start_time = time.perf_counter()
total_sum = 0
total_elements = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        total_sum += matrix[i][j]
        total_elements += 1
mean = total_sum / total_elements
end_time = time.perf_counter()
print(start_time)
print(end_time)
print(
    f'Calculate the average value of the elements in {matrix} using a loop took {end_time - start_time} seconds')

print(mean)
# PP dùng numpy
start_time1 = time.perf_counter()
result = np.mean(matrix)
end_time1 = time.perf_counter()
print(
    f'Calculate the average value of the elements in {matrix} using numpy library {end_time1 - start_time1} seconds')
