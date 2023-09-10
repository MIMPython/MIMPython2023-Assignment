#Bài tập 12:
n = int(input("Nhập số nguyên dương n: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    for i in range(1, n + 1):
        print(i, end=" ")
