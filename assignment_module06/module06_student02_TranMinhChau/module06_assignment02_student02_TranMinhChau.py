# Bài tập 2: (numpy methods)
import numpy as np
import time
#1 ) np.median(): Median (trung vị) là giá trị trung tâm của một dãy số với điều kiện là dãy số đó phải sắp xếp theo thứ tự từ bé đến lớn. 
X = [1, 2, 3, 4, 2, 3, 5, 6, 1]
# Dùng numpy
start_time_numpy_1 = time.time()
for _ in range(10000):
    np.median(X)
end_time_numpy_1 = time.time()
# Cách thủ công
def manual_median(arr):
    sorted_arr = np.sort(arr)
    n = len(arr)
    middle = n // 2
    if n % 2 == 1:
        return sorted_arr[middle]
    else:
        return (sorted_arr[middle - 1] + sorted_arr[middle]) / 2
start_time_manual_1 = time.time()
for _ in range(10000):
    manual_median(X)
end_time_manual_1 = time.time()
# Tính thời gian thực thi
elapsed_time_numpy_1 = end_time_numpy_1 - start_time_numpy_1
elapsed_time_manual_1 = end_time_manual_1 - start_time_manual_1
print("Thời gian thực thi của np.median:", elapsed_time_numpy_1)# Thời gian thực thi của np.mean:  0.07749652862548828
print("Thời gian thực thi của chương trình thủ công:", elapsed_time_manual_1)# Thời gian thực thi của chương trình thủ công: 0.024147510528564453

# 2) np.repeat(): được sử dụng để lặp lại mảng theo một số lần xác định.
# Dùng numpy
start_time_numpy_2 = time.time()
for _ in range(10000):
    np.repeat(X, 3)
end_time_numpy_2 = time.time()
# Cách thủ công
def manual_repeat(arr, repeats):
    repeated_list = []
    for elem in arr:
        repeated_list.extend([elem] * repeats)
    return np.array(repeated_list)
start_time_manual_2 = time.time()
for _ in range(10000):
    manual_repeat(X, 3)
end_time_manual_2 = time.time()
# Tính thời gian thực thi
elapsed_time_numpy_2 = end_time_numpy_2 - start_time_numpy_2
elapsed_time_manual_2 = end_time_manual_2 - start_time_manual_2
print("Thời gian thực thi của np.repeat:", elapsed_time_numpy_2)# Thời gian thực thi của np.mean:  0.027883529663085938
print("Thời gian thực thi của chương trình thủ công:", elapsed_time_manual_2)# Thời gian thực thi của chương trình thủ công: 0.030480146408081055












