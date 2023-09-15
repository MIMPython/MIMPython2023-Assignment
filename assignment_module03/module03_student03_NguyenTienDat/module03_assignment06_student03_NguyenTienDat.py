# Bài tập 6:

# a)
def euclidean_gcd(a, b):
    while b:
        a, b = b, a % b
    if a != 1:
        return a
    else:
        return "coprime integers"
        

# b)
def probability(N):
    result = sum(count_coprime_integers(i) for i in range(2, N))
    P = result*2/(N*(N-1))
    return P 
        
        
        
# check xem có bao nhiêu cặp số nguyên tố cùng nhau có số n là 1 phần tử trong cặp số đó và phần tử còn lại bé hơn n.
def count_coprime_integers(n):
    count = 0
    for i in range(1, n):
        if euclidean_gcd(n, i) == "coprime integers":
            count += 1  
    return count


# c)
# Dò nghiệm: (vì mình biết số a b sẽ đẹp và nhỏ nên mình dò khoảng nhỏ :>)
import math
def find_a_b():
    P = probability(10**4)
    # cho phép sai số epsilon
    epsilon = 0.0001
    for a in range(1, 10):
        for b in range(1, 10):
            if abs(P - a/(math.pi**b)) < epsilon:
                return a, b 


print(probability(10**4)) # output xấp xỉ 60%
print(find_a_b()) # output: 6, 2


# Ngoài ra có một cách tối ưu hơn để tính P đó là dùng hàm Phi Euler (chạy tốt hơn với N lớn):
# Thuật toán tính phi của một số n:
def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def calculate_probability_using_totient(N):
    totient_sum = sum(phi(i) for i in range(1, N + 1))
    probability = totient_sum*2 / (N * (N-1) )
    return probability

# calculate_probability_using_totient(10**6)

# Một cách khác tính P:
def largest_prime_factor(n):
    factor = 2
    prime = [] # list chứa các số nguyên tố thành phần của n
    s_m = [] # list chứa các số mũ lần lượt của các số trong list prime 
    # thuật toán đếm các phần tử của 2 list prime và s_m 
    while factor * factor <= n:
        count = 0
        if n % factor == 0:
            while n % factor == 0 and n != 1:
                count += 1
                n = int(n/factor)
            prime.append(factor)
            s_m.append(count)
        else:
            factor += 1
    if n > 1:  # Đảm bảo rằng n lớn hơn 1 và không phải là số nguyên tố
        prime.append(n)
        s_m.append(1)
    return prime, s_m  # Trả về cả danh sách các ước số nguyên tố và số mũ tương ứng


# tính phi Euclid của n 
def phi(n):
    data = largest_prime_factor(n)
    prime = data[0]
    s_m = data[1]
    result = 1
    for i in range(len(prime)):
        result *= (prime[i]-1)*(prime[i]**(s_m[i]-1))
    return result

# tính P:
def calculate_probability_using_totient(N):
    totient_sum = sum(phi(i) for i in range(1, N + 1))
    probability = totient_sum*2 / (N * (N-1) )
    return probability

calculate_probability_using_totient(10**9) # output xấp xỉ 60%
        