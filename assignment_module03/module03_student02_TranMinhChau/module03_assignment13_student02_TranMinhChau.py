#Bài tập 13:
n = int(input("Nhập giá trị của n"))
two_to_the_n = 2**n
five_to_the_n = 5**n
result = int(str(two_to_the_n) + str(five_to_the_n))
num_digits = len(str(result))
print(f"Với n = {n}, ta được 1 số có {num_digits} số")