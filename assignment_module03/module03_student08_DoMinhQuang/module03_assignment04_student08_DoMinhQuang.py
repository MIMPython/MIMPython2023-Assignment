import math
import numpy as np
import sympy as sp

n=int(input())
def Fibo1(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return Fibo1(n-1)+Fibo1(n-2)

def Fibo2(n):
    a=0.5*(1+math.sqrt(5))
    b=0.5*(1-math.sqrt(5))
    c= 1/math.sqrt(5)*(pow(a,n)-pow(b,n))
    return round(c,1)

def Fibo3(n):
    arr = np.array([1, 1])
    for i in range(2, n):
        arr = np.append(arr, arr[i - 1] + arr[i - 2])
    return arr[- 1]


def Fibo4(n):
    return sp.fibonacci(n)

if __name__ == '__main__':
    print(Fibo1(n))
    print(Fibo2(n))
    print(Fibo3(n))
    print(Fibo4(n))






