# Bài tập 7:

def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n = int(n/factor)
        else:
            factor += 1
    return n

result = largest_prime_factor(600851475143) # output 6857 
print(result)
