from math import sqrt

# Tìm ước chung lớn nhất
def gcd(a: int, b: int):
    a, b = max(abs(a), abs(b)), min((abs(a), abs(b)))
    if b == 0:
        if a == 0:
            raise Exception('Invalid value gcd(0, 0)')
        else:
            return a
    else:
        while a%b != 0:
            a, b = b, a%b
        return b

# Kiểm tra số nguyên tố
def isPrime(n):
    s = int(sqrt(n))+1
    checked = 1
    for d in range(2, s):
        if n%d == 0:
            return False
        else:
            checked += 1
    if checked == s-1:
        return True

# Phân tích một số nguyên (dương) thành các thừa số nguyên tố
def factorize(n: int):
    primeFactorList = []
    while n>1:
        if isPrime(n):
            primeFactorList.append(n)
            break
        else:
            for d in range(2, n):
                if n%d == 0:
                    primeFactorList.append(d)
                    n = n//d
                    break
    return primeFactorList

if __name__ == '__main__':
    pass