'''Bài 7: Tìm ước nguyên tố lớn nhất'''
import math
def isPrime(n):#Hàm kiểm tra số nguyên tố
    if n < 2:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def findMaxPrimeFactor(n):
    list = []
    for i in range(2,math.floor(math.sqrt(n))):
        if n % i == 0 and isPrime(i):
            list.append(i)#tạo một mảng chứa các số nguyên tố là ước của n
    return max(list)#trả về phần tử lớn nhất của mảng

if __name__ == '__main__':
    print(findMaxPrimeFactor(13195))#29
    print(findMaxPrimeFactor(600851475143))#6857

#Chạy code: python module03_assignment07_student08_DoMinhQuang.py
