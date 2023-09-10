#Bài tập 4:
import math

#Cách 1:
print("Cách 1:")
def fibonacci(n):
    if n < 0:
        print("n phải là một số tự nhiên")
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhập số tự nhiên n: "))
result = fibonacci(n)
print(f"F_{n} = {result}")

#Cách 2: Sử dụng thư viện numpy
print("Cách 2:")
import numpy as np

def fibonacci_np(n):
    fib = np.zeros(n + 1, dtype=int)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

n = int(input("Nhập số tự nhiên n: "))
result = fibonacci_np(n)
print(f"F_{n} = {result}")

#Cách 3: Sử dụng thư viện sympy
print("Cách 3:")
from sympy import fibonacci

n = int(input("Nhập số tự nhiên n: "))
result = fibonacci(n)
print(f"F_{n} = {result}")



