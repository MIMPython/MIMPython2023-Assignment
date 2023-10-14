'''Bài 2: Viết lại các hàm có trong thư viện numpy mà không sử dụng numpy'''



import numpy
import numpy as np

'''Trong các phương thức dưới đây, em gặp khó khăn trong việc thiết kế hàm cho các mảng có chiều lớn hơn 2'''

#mean

arr = np.array([
                  [2, 7, 3, 0, 0],
                  [6, 4, 4, 3, 1],
                  [0, 0, 9, 1, 2],
                ])
print(arr,'\n')
# print(np.mean(arr, 1))  #axis = 1 tính theo hàng ngang, 0  tính theo cột dọc

def find_mean(arr: numpy.ndarray, axis: int = None):#hàm mean() trong numpy, nhận vào một mảng và trả về giá trị trung bình tùy theo tham số axis
    list_arr = list(arr)                            #nếu axis = 1 thì sẽ trả về list gồm giá trị trung bình của hàng, còn axis = 0 là cột
    value: int = 0
    mean_list: list = []
    if axis == None:
        for subarr1 in list_arr:
            # for subarr2 in subarr1:
            value: int = value + sum(subarr1)
        return value / (len(list_arr) * len(subarr1))

    elif axis == 1:
        mean_list = [sum(subarr) / len(subarr) for subarr in list_arr]
        return mean_list

    elif axis == 0:
        for i in range(len(list_arr[0])):
            s: int = 0
            for subarr in list_arr:
                s = s + subarr[i]
            mean_list.append(s / len(list_arr))
        return mean_list

    #Trường hợp axis = 0 có thể được viết gọn hơn như sau dùng hàm zip()
        #mean_list = [sum(x) / len(arr) for x in zip(*arr)]
        #return mean_list



print("Hàm mean tự viết: ",find_mean(arr, 0))
print('Hàm mean trong thư viện: ',np.mean(arr,0))


#max

def find_max(arr: list) -> int:# tìm max trong mảng
    max: int = -1
    for row in arr:
        for elem in row:
            if elem > max:
                max: int = elem
    return max

#min

def find_min(arr: list) -> int: #tìm min trong mảng
    min: int = 100000000000
    for row in arr:
        for elem in row:
            if elem < min:
                min: int = elem
    return min

#ones
def construct_ones(tup: tuple) -> numpy.ndarray: #hàm np.ones() trong numpy tạo ra 1 mảng gồm toàn số 1 với size cho trước
    # for i in range(tup[0]):
    #     matrix.append([])
    #     for j in range(tup[1]):
    #         matrix[i].append(1)
    matrix = [[1 for j in range(tup[1])] for i in range(tup[0])]
    ones = np.array(matrix)
    return ones

ones = construct_ones((4,3))
print(ones)

#zero
def construc_zeros(tup: tuple) -> numpy.ndarray: #hàm np.zeros() khởi tạo 1 mảng gồm toàn số 0
    matrix = [[0 for j in range(tup[1])] for i in range(tup[0])]
    zeros = np.array(matrix)
    return zeros

zeros = construc_zeros((4,3))
print(zeros)

#argmax
def find_argmax(arr: numpy.ndarray, axis: int = None):#hàm np.argmax() trả về một list là các giá trị lớn nhất tùy theo tham số axis
    arr_list = list(arr)                              #nếu axis = 1 thì sẽ trả về list gồm max của các hàng, nếu axis = 0 thì sẽ trả
    max_pos_list: list = []

    if axis == 0:
        for tup in zip(*arr_list):
            for j in range(len(tup)):
                if tup[j] == max(tup):
                    max_pos_list.append(j)
            # max_pos_list = [j for j in range(len(tup)) #if tup[j] == max(tup)] #Dòng này em comment vì sai kết quả
        return max_pos_list                              #em vẫn chưa tìm được lí do

    elif axis == 1:
        max_pos_list = [list(subarr).index(max(list(subarr))) for subarr in arr_list] #ở ngay dòng đầu em đã ép thành kiểu list
        return  max_pos_list                                                          #nhưng xuống đây em lại phải ép laại nếu ko sẽ lỗi

    elif axis == None:
        for subarr in arr_list:
            for i in subarr:
                max_pos_list.append(i)
        return max_pos_list.index(find_max(arr_list))


#argmin

def find_argmin(arr: numpy.ndarray, axis: int = None):
    arr_list = list(arr)
    min_pos_list: list = []

    if axis == 0:
        for tup in zip(*arr_list):
            for j in range(len(tup)):
                if tup[j] == min(tup):
                    min_pos_list.append(j)
            # min_pos_list = [j for j in range(len(tup)) #if tup[j] == max(tup)] #Dòng này em comment vì sai kết quả
        return min_pos_list                              #em vẫn chưa tìm được lí do

    elif axis == 1:
        min_pos_list = [list(subarr).index(min(list(subarr))) for subarr in arr_list] #ở ngay dòng đầu em đã ép thành kiểu list
        return  min_pos_list                                                          #nhưng xuống đây em lại phải ép laại nếu ko sẽ lỗi

    elif axis == None:
        for subarr in arr_list:
            for i in subarr:
                min_pos_list.append(i)
        return min_pos_list.index(find_min(arr_list))




def find_linspace(start: float, stop: float, num: int, endpoint: bool = True):# hàm linspace() khởi tạo 1 mảng với độ dài cho trước và khoảng giá trị cho trước
    step = (stop - start) / (num - 1)                                         #nếu endpoint = False thì sẽ ko tính giá trị stop vào mảng, mặc định là True
    if endpoint == True:
        arr = [start + i * step for i in range(num)]
        return arr

    elif endpoint == False:
        step = (stop - start) / (num)
        arr = [start + i * step for i in range(num)]
        return arr

def find_arrange(start: float, stop: float, step: float):#hàm arrange() khởi tạo mảng với điểm bắt đầu và điểm dừng và bước nhảy nhưng ko biết trước độ dài
    i = 0
    arr = []
    while start + i * step <= stop:
        arr.append(start + i * step)
        i += 1
    return arr


l = find_argmin(arr,1)
print('Hàm argmax tự viết: ',l)
print('Hàm argmax trong thư viện: ',np.argmin(arr, 1))

# b = np.array([[1,2,3]])
# print(find_argmax(b,0))

# ls = list(arr)
# # print(type(ls))
# # print(ls.index(9))

print(find_linspace(2, 3, 5, False))
print(np.linspace(2,3,5,False))

print(find_arrange(1,9,2))
print(np.arange(1,9, 2))



