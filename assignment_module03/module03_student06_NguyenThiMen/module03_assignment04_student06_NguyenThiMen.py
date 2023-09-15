import sympy as sp
import numpy as np
# tinh so fibonacci su dung vong lap
def fibonacci1(n):
    f0 = 0
    f1 = 1
    for i in range(2, n+1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f

# su dung de quy
def fibonacci2(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)

# su dung thu vien numpy va ket qua cua ma tran fibonacci
def fibonacci3(n):
    fib_matrix = np.array([[1, 1], [1, 0]])
    # su dung module np.linalg thuc hien phep tinh dai so tuyen tinh
    result_matrix = np.linalg.matrix_power(fib_matrix, n) # linalg (linear algebra)
    return result_matrix[1][0]

def fibonacci4(n):
    return sp.fibonacci(n)

if __name__ == '__main__':
    print('Tinh so fibonacci thu 10 su dung vong lap:')
    print(fibonacci1(10))
    print('Tinh so fibonacci thu 10 su dung de quy:')
    print(fibonacci2(10))
    print('Tinh so fibonacci thu 10 su dung numpy:')
    print(fibonacci3(10))
    print('Tinh so fibonacci thu n su dung sympy:')
    print(fibonacci4(10))
