a = 100
def Fibonacci_1(num):
    if num <= 1: return num
    else:
        a, b, c = (0, 1, -1)
        for i in range(num - 1):
            c = a + b
            a = b
            b = c
        return c
# print(Fibonacci_1(a))

def Fibonacci_2(num):
    # Sử dụng công thức Binet. Đúng đến số thứ 70 (so với cách 1).
    import math
    square_five = math.sqrt(5)
    a = (1 + square_five) / 2
    b = (1 - square_five) / 2
    c = round((a ** num - b ** num) / square_five)
    return c
# print(Fibonacci_2(a))

def Fibonacci_3(num):
    # Sử dụng ma trận. Đúng đến số thứ 92 (so với cách 1).
    import numpy
    F_matrix = numpy.matrix([[1, 1], [1, 0]])
    if num == 0: return 0
    else:
        return (F_matrix ** (num - 1))[0, 0]
# print(Fibonacci_3(a))

def Fibonacci_4(num):
    # Sử dụng phương thức có sẵn trong thư viện sympy.
    import sympy
    return sympy.fibonacci(num)
# print(Fibonacci_4(a))