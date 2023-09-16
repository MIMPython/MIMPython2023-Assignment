#Bài tập 6: (probability of coprime integers)
#(a)
print("a.")
def euclid_gcd(n1, n2):
    while n2:
        n1, n2 = n2, n1 % n2
    return n1
num1 = int(input("Số thứ 1 là:"))
num2 = int(input("Số thứ 2 là:"))
gcd = euclid_gcd(num1, num2)
print("Ước chung lớn nhất của", num1, "và", num2, "là", gcd)

#(c)
print("c.")
import math
a = float(input("Nhập vào giá trị của a với a là số dương"))
b = float(input("Nhập vào giá trị của b với b là số dương"))
#Tính xác suất P 
P = a / math.pi**b
# Giá trị π
pi_value = math.pi

print("Giá trị xác suất P:",P )
print("Giá trị π:", pi_value)

# So sánh giá trị P với π
if abs(P - pi_value) < 0.0000001:  
    print("Giá trị P gần bằng π.")
else:
    print("Giá trị P không gần bằng π.")
