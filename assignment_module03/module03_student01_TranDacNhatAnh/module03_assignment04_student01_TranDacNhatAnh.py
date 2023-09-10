# 0
import sympy
print(sympy.fibonacci(7)) #13
# Đây là một "cách" để chúng ta lấy được dãy fibonacci, dù không thuyết phục lắm...

# Cách 1
def fibonacci(n):
    if n<2:
        return n
    else:
        a = 0
        b = 1
        for i in range(n-1):
            temp = b
            b = a + b
            a = temp
        return b
print(fibonacci(7)) #13
# Đây là cách tính trực tiếp nhất. Vòng lặp for có tác dụng: sau lần thứ k-1 thì a và b lần lượt là Fibonacci(k-1) và Fibonacci(k)
# 2 cách tiếp theo trình bày một số hàm có cùng cách tính nhưng "đẹp" hơn về mặt hình thức

# Cách 2
def computeFibonacci(n: int):
    if n<2:
        return n
    else:
        return computeFibonacci(n-1) + computeFibonacci(n-2)
print(computeFibonacci(7)) #13
# Cách làm này nhanh gọn và đẹp mắt về mặt hình thức, tuy nhiên với n rất lớn thì sẽ xuất hiện nhược điểm, ví dụ ta cần tìm số Fibonacci thứ 9000 và 10000
# thì sẽ phải thực hiện lần lượt computeFibonacci(9000) và computeFibonacci(10000), tức gần 19000 phép tính.
# Lí do là bởi hàm trên chỉ "tính ra kết quả cuối cùng" mà không "lưu lại quá trình thực hiện".

# Cách 3
listOfFibonacci = [0, 1]
def numberFibonacci(n):
    while len(listOfFibonacci) < n+1:
        listOfFibonacci.append(listOfFibonacci[-1] + listOfFibonacci[-2])
    return listOfFibonacci[n]
print(numberFibonacci(7)) #13
print(listOfFibonacci[5]) #5
# Cách này rõ ràng khắc phục được nhược điểm của 2 cách trên: sau khi tính được số Fibonacci thứ n, ta hoàn toàn có thể lấy ra các số Fibonacci nhỏ hơn
# mà không cần sử dụng hàm để tính

# Cách 4
import functools as f
Fibonacci = lambda n:f.reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
# Code 1 dòng! Cách trên được tìm thấy ở stackoverflow, trong một nỗ lực tìm cách sử dụng numpy.array để giải bài
# Em có ý tưởng sử dụng phép cộng các array có sẵn trong numpy nhưng không tìm được cách thêm vào array 1 phần tử nên 
# chưa thể triển khai được.

# Cách 5
import numpy as np
def fibonacciMatrix(n):
    fiboMatrix = np.matrix([[0,1],[1,1]])
    vec = np.array([[0],[1]])
    return int(np.matmul(fiboMatrix**n,vec)[0])
print(fibonacciMatrix(7)) #13
# Cách tính này cũng xuất hiện trong các bài giảng môn Đại số tuyến tính