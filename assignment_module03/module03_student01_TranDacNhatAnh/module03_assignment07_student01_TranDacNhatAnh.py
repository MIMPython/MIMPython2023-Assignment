from math import sqrt
def Prime(n):
    Factors = []
    while n>1:
        rng = int(sqrt(n))+2
        count = 0
        p = 2
        for i in range(p,rng):
            if n%i==0:
                p=i
                Factors.append(p)
                n = n//i
                break
            else:
                count += 1
        if count == rng-2:
            Factors.append(n)
            n = 1
    return Factors
print(Prime(600851475143)) # [71, 839, 1471, 6857]
# Mặc dù thừa so với yêu cầu của đề bài nhưng em hứng thú nên đã viết 1 hàm in ra tất cả các ước nguyên tố (kể cả bội)
# Để tìm ước nguyên tố lớn nhất, chỉ cần lấy ra phần tử cuối cùng (phần tử thứ [-1]) của list nói trên
print(Prime(600851475143)[-1]) # 6857