number = 600851475143
def largest_prime_factor(n):
    # Đầu vào là một số nguyên dương lớn hơn 1, 
    # đầu ra là ước nguyên tố lớn nhất của nó.
    p = 1
    while n != 1:
        p += 1
        while n % p == 0:
            n = n / p
    return p

print(largest_prime_factor(13195)) # 29
print(largest_prime_factor(number)) # 6857