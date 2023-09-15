

def fibonaci(n):
    queue_fib = [0, 1]
    for i in range(2, n):
        next_fib = queue_fib[i-1] + queue_fib[i-2]
        queue_fib.append(next_fib)
    return queue_fib

import numpy as np    
def fibonaci_numpy(n):
    queue_fib = np.array([0,1])
    for i in range(2,n):
        next_fib = queue_fib[i-1] + queue_fib[i-2]
        queue_fib = np.append(next_fib)
    return queue_fib
print(fibonaci_numpy(9))