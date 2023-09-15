# a).greatest common divisor with Euclid algorithm
# def gcd(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     return a
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd( b, a%b)


# b). Tinh xac suat chon ngau nhien 2 so la 2 cap so nguyen to cung nhau tu tap hop
# cac so nguyen duong khong qua n

# Cach 2: Dem so cap so nguyen to cung nhau trong tat ca cap so co the chon
n = int(input('Enter n: '))
list = []
for i in range(1, n+1):
    tpl = ()
    for j in range(1, n+1):
        tpl = (i, j)
        list.append(tpl)
print(list)
n_A2 = 0
n_omega2 = len(list)
for element in list:
    a = element[0]
    b = element[1]
    if gcd(a, b) == 1:
        n_A2 += 1
print(n_A2)
P = n_A2 / n_omega2
print(P) # 0.63


# c). P*(pi**b) = a
