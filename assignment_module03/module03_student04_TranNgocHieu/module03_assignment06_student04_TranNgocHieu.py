# a)
def gcd(a, b):
    # Đầu vào là hai số nguyên, đầu ra là ước chung lơn nhất của chúng.
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return abs(b)

# b)
def prob1(size):
    # Tính xác suất bằng cách chọn ngẫu nhiên cặp số 100.000 lần.
    import numpy
    count = 0
    for i in range(10 ** 5):
        a = numpy.random.randint(1, size)
        b = numpy.random.randint(1, size)
        if gcd(a, b) == 1:
            count += 1
    return count / 10 ** 5
def prob2(size):
    # Tính xác suất bằng cách kiểm tra tất cả các cặp số có thể.
    count = 0
    for i in range(1, size + 1):
        for j in range(i, size + 1):
            if gcd(i, j) == 1:
                count += 1
    return round(count / (size * (size - 1) / 2), 5)
# print(f"{prob1(5000)} {prob2(5000)}")

# c)
# Từ cách 2, câu b), với các số nguyên dương không quá 5000,
# xác suất để chọn ra hai số nguyên tố cùng nhau là khoảng 0.60816
def estimate():
    import math
    P = 0.60816
    pi = math.pi
    list = []
    for i in range(10):
        list.append((P * (pi ** i) - math.floor(P * (pi ** i))))

    min_list = min(list)
    print(f"{round(min_list, 5)} {list.index(min_list)}") # 0.0023 2

# Dự đoán: P = 6/pi^2 

def test(n):
    # Kiểm tra dự đoán bằng cách 1, chạy n lần, in ra khoảng cách bé nhất.
    import math
    pi = math.pi
    guess = 6 / (pi ** 2)
    min_diff = 10
    for i in range(n):
        P = prob1(10 ** 6)
        difference = abs(P - guess)
        if min_diff >= difference: min_diff = difference
    return min_diff

print(test(10))