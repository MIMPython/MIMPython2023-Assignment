# Bài tập 4:


# Sử dụng vòng lặp:
def fibonacci_1(n):
    if n > 1:
        a = 0
        b = 1
        for i in range(2, n + 1):
            temp = b
            b = b + a
            a = temp
        return b  
    elif n <= 0: return 0
    else: return 1
    
    
# Sử dụng đệ quy:
def fibonacci_2(n):
    if n > 1:
        return fibonacci_2(n-1) + fibonacci_2(n-2)
    elif n <= 0: return 0
    else: return 1
         
         
# Sử dụng numpy:import       
import numpy   
def fibonacci_3(n):
    if n > 1:
        fib = numpy.zeros(n+1, dtype = int)
        fib[1] = 1
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[n]
    elif n == 1: return 1
    else: return 0


# Sử dụng sympy:



print(fibonacci_1(6))
print(fibonacci_2(6))
print(fibonacci_3(6))
    