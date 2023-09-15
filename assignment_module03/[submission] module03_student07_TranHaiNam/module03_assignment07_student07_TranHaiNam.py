#Kiểm tra số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    elif n >= 2:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True

#print(isPrime(2))

#phân tích 1 số bằng tích các số nguyên tố        
def analyze_number(n):
    list_prime = []
    i = 2
    while n > 1:
        if (isPrime(i)):
            if n % i == 0:
                list_prime.append(i)
                n = n / i
            else:
                i += 1
        else:
            i += 1
    return list_prime

a = analyze_number(600851475143)
print(a)
print(max(a)) #6857