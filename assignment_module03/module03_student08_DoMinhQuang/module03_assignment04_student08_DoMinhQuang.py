#Tính số Fibonacci thứ n bằng nhiều cách khác nhau, trong đó có cách sử dụng numpy và sympy'''

import math
import numpy as np
import sympy as sp
import sys

n = int(sys.argv[1])

'''Cách 1 sử dụng đệ quy'''
def Fibo1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibo1(n - 1) + Fibo1(n - 2)

''' Cách 2 sử dụng công thức số hạng tổng quát của dãy, có thể xem tại 
    https://svnckh.edu.vn/fibonacci-la-gi/'''
def Fibo2(n):
    a=0.5 * (1 + math.sqrt(5))
    b=0.5 * (1 - math.sqrt(5))
    c= 1 / math.sqrt(5) * (pow(a,n) - pow(b,n))
    return round(c,1)

'''Cách 3'''
def Fibo3(n):
    arr = np.array([1, 1]) #Khởi tạo mảng với 2 phần tử là 2 số hạng đầu tiên của dãy
    for i in range(2, n):
        arr = np.append(arr, arr[i - 1] + arr[i - 2])#lần lượt thêm vào các số hạng bằng tổng của 2 số gần nhất
    return arr[- 1] #Sau khi kết thúc vòng lặp ta được 1 mảng gồm các n số fibonacci, lấy ra số cuối cùng là số thứ n


def Fibo4(n):
    return sp.fibonacci(n)

if __name__ == '__main__':
    print("Cách 1: ",Fibo1(n)) #5
    print("Cách 2: ",Fibo2(n)) #5
    print("Cách 3: ", Fibo3(n)) #5
    print("Cách 4: ",Fibo4(n)) #5

#Chạy code : python module03_assignment04_student08_DoMinhQuang.py 5#   Output:5
#Chạy code : python module03_assignment04_student08_DoMinhQuang.py 9#   Output:34






