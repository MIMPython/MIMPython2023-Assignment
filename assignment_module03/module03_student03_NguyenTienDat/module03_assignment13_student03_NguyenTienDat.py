# Bài tập 13:
# khi viết 2 số nguyên 2^n và 5^n liên nhau ta sẽ được một số có n - 1 chữ số.

def count_digits(n):
    number = int(str(2**n) + str(5**n))
    count = len(number)
    print (count)