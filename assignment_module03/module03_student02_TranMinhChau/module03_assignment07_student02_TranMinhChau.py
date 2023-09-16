#Bài tập 7:(largest prime factor)
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

number = 600851475143
result = largest_prime_factor(number)
print("Thừa số nguyên tố lớn nhất của", number, "là", result)
#Thừa số nguyên tố lớn nhất của 600851475143 là 6857