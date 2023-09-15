# Tìm thừa số nguyên tố lớn nhất
import sys
def largest_prime_factor(n):
    n = int(n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n
print(sys.argv)
print(largest_prime_factor(sys.argv[1]))
# python file.py 600851475143
# ['.\\module03_assignment07_student06_NguyenThiMen.py', '600851475143']
# 6857
