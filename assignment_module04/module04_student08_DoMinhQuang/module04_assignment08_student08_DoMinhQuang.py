'''Bài 8: Đếm chữ số 0 ở tận cùng của n!, sau khi bỏ các số 0 đi ta được số gì'''


'''Nếu ở cuối n! xuất hiện số 0 nghĩa là trong tích của n! có chứa tích (2.5), nghĩa là ta chỉ cần đi tìm số lượng số
2 và số 5 rồi lấy số nhỏ hơn, nhưng dễ thấy số số 2 trong tích của n! luôn lớn hon số số 5, do đó chỉ cần tìm số lần
xuất hiện của số 5'''

#Cách 1
def count_zero1(n: int) -> int :    #Nếu n! nhỏ hơn bằng 5! thì chưa có số 0 nào
    s = 0
    for i in range(5, n + 1, 5) :   #Nếu n! lơn hơn 5!, ta duyệt các số chia hết cho 5 trong tích của n số đó
        tmp = i
        while tmp % 5 == 0 :        #Ứng với mỗi số chia hết cho 5, ta lại xét xem nó có thể chia hết cho 5
            s = s + 1               #bao nhiêu lần
            tmp = tmp / 5
    return s



def factorial(n: int) -> int :  #Hàm n! để kiểm tra kết quả
    s = 1
    for i in range(1,n + 1) :
        s = s * i
    return s


#Cách 2: Dùng công thức Legendre
#Có thể xem tại https://vi.wikipedia.org/wiki/C%C3%B4ng_th%E1%BB%A9c_Legendre
import math
def count_zero2(n: int) -> int :
    s = 0
    p = 5
    i = 1
    while p ** i <= n :
        s = s + math.floor(n / (p ** i))
        i = i + 1
    return s

n = 1000
print(count_zero1(n))
print(count_zero2(n))
print(factorial(n))

number_of_zero = count_zero2(n)
factorial = factorial(n)

for i in range(1, number_of_zero + 1) :
    factorial = factorial // 10

number = factorial % 10
print(factorial)
print(number)

#Chạy code:  python module04_assignment08_student08_DoMinhQuang.py


