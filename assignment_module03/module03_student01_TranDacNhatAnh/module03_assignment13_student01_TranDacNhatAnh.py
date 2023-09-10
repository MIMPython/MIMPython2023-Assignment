# Cách 1
def stringOfTwosAndFives(n):
    twos = 2**n
    fives = 5**n
    return len(str(twos)) + len(str(fives))
print(stringOfTwosAndFives(15)) #16
# Cách thủ công, biến các số 2**n và 5**n thành string và cộng độ dài của chúng

def lazy(n):
    if n==0:
        return 2
    else:
        return n+1
print(lazy(15)) #16
# Sử dụng kết quả đã được chứng minh bằng Toán: ghép 2**n và 5**n lại thì sẽ nhận được số có n+1 chữ số

# Kiểm tra tính chính xác của hàm lazy
count = 0
for i in range(6152):
    if stringOfTwosAndFives(i) == lazy(i):
        count += 1
print(count) #6152