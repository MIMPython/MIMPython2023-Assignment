# Bài tập 3:

def Longest_Collatz_Sequence(n):
    count = 1
    while (n != 1):
        if n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3*n + 1
            count += 1
    return count
    
def find_max():
    max_temp = 0
    for i in range(1, 10**6 + 1):
        if Longest_Collatz_Sequence(i) > max_temp:
            max_temp = Longest_Collatz_Sequence(i)
            
    for i in range(1, 10**6 + 1):
        if Longest_Collatz_Sequence(i) == max_temp:
            return i # 837799

print(find_max())