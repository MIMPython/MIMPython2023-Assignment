# Bài tập 2: (solving linear equations)
import numpy as np
import time
def solve_linear_equation(A: list, b: list) -> list:
    n = len(A)
    if any(len(row) != n for row in A):
        raise ValueError("A must be a square matrix")
    if len(b) != n:
        raise ValueError("b must have the same length as A")
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Perform Gaussian elimination
    for i in range(n):
        pivot = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[pivot][i]):
                pivot = j
        if pivot != i:
            A[[i, pivot]] = A[[pivot, i]]
            b[[i, pivot]] = b[[pivot, i]]
        factor = A[i][i]
        if factor == 0:
            raise ValueError("A is singular")
        A[i] /= factor
        b[i] /= factor
        for j in range(i + 1, n):
            factor = A[j][i]
            A[j] -= factor * A[i]
            b[j] -= factor * b[i]

    # Perform back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x.tolist()

A = [[1, 2], [3, 4]]
b = [5, 6]

# Solve the linear equation using the custom function
start = time.time() 
x1 = solve_linear_equation(A, b) 
end = time.time()
time1 = end - start
print(f"The solution using the custom function is {x1}")
print(f"The execution time using the custom function is {time1} seconds")

# Solve the linear equation using the numpy function
start = time.time()
x2 = np.linalg.solve(A, b) 
end = time.time() 
time2 = end - start
print(f"The solution using the numpy function is {x2}")
print(f"The execution time using the numpy function is {time2} seconds")