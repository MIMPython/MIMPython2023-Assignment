#Số xuôi ngược là một số tự nhiên không thay đổi khi được viết theo chiều ngược lại.
#Có tồn tại vô hạn số xuôi ngược đồng thời là một số chính phương hay không?

import math

def perfect_square(n):
    for i in range(1,n):
        if i ** 2 == n:
            return True
    return False

def reverse_number(n):
    reverse_number = 0
    while n > 0:
        digit = n % 10
        n = math.trunc(n / 10)
        reverse_number = reverse_number * 10 + digit 
    return reverse_number

def palindrome_number(n):
    if n == reverse_number(n):
        return n


def infinity(n):
    n = 1
    while n > 0:
        n += 1
        if perfect_square(n) and palindrome_number(n):
            
            print(n)

print(infinity(1)) 
#4
9
121
484
676
10201
12321
14641
40804
44944
# em chưa thể đi hết các kết quả vì khối lượng số còn lớn nên cá nhân em nghĩ sẽ tồn tại vô hạn số xuôi ngược đồng thời là số chính phương.
