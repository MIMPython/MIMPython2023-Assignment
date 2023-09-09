'''Bài 6: tính xác suất P để chọn được 2 số nguyên tố cùng nhau, tìm mối quan hệ
với số PI'''

import itertools

#a
def GCD(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        while a != b:
            if(a>b):
                a = a - b
            else:
                b = b - a
    return a





#b
def P(n):
    numberList = list(range(1,n+1))
    total = 0.5 * n * (n - 1)# Đếm số tập con có 2 phần tử trong n phần tử
    cList = itertools.combinations(numberList,2)#list gồm các tập con có 2 phần tử
    count = 0
    for i,d in cList:
        if GCD(i,d) == 1:
            count+= 1
    print("Số cặp số nguyên tố cùng nhau là: ",count)
    print("Xác suất P là: ",count/total)

if __name__ == '__main__':
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print(f"UCLN của {a} và {b} là: ",GCD(3, 3))  # 3
    print("UCLN của 16 và 4 là: ",GCD(16, 4))  # 4
    n = int(input("Nhập số N: "))
    P(1000)#0.608990990990991


#Chạy code: python module03_assignment06_student08_DoMinhQuang.py


