# Bài tập 6:

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
    
def find_max(upper_limit):
    max_length = 0
    number_with_max_length = 0
    
    for i in range(1, upper_limit + 1):
        current_length = Longest_Collatz_Sequence(i)
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i

    return number_with_max_length # output: 837799

print(find_max(10**6))