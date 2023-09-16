#a)
# Thuật toán tìm Ước chung lớn nhất của 2 số a, b (với giả sử a>=b)
def gcd(a, b):
    if b==0:
        return abs(a)
    else: # Thuật chia Euclid
        while a%b!=0:
            temp = a
            a = b
            b = temp%a
        return abs(b)
#b)
# Cách thứ nhất
import random as rd
def probOfCroprime(N, test):
    count = 0
    for i in range(test):
        a = rd.randint(0, N)
        b = rd.randint(0, N)
        if gcd(a, b) == 1:
            count += 1
    return count / test
print(probOfCroprime(100000, 1000000)) # Tuy kết quả không cố định, những cũng ổn định quanh 0.608
# Cách thứ hai
def probabilityOfCoprime(N):
    count = 0
    for i in range(N+1):
        for j in range(i+1):
            if gcd(i, j)==1:
                count +=1
    return count*2/(N*(N-1)) # Nhân 2 vì gcd(a,b) <=> gcd(b,a)=1
#print(probabilityOfCoprime(10000)) # 0.6080105410541055

#c)
from math import pi
print(6 / (pi*pi)) #0.6079271018540267
# Kết quả này Có lẽ sẽ nhỏ hơn P thực tế vì Python chỉ lấy pi tới 15 chữ số sau "dấu phẩy"
# Đây cũng là nghịch đảo của một giới hạn quen thuộc: 1/1^2 +1/2^2 +...
# Em chưa tự kiểm tra nhưng có lẽ sẽ có 1 chứng minh toán học cho điều này :v