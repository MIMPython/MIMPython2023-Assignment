# viết hai số nguyên 2^n và 5^n liền nhau ta được một số có bao nhiêu chữ số?
import math
import sys
def calculate_the_number_of_digits(n):
    n = int(n)
    two_power_n = int(math.pow(2, n))
    five_power_n = int(math.pow(5, n))
    two_power_n_str = str(two_power_n)
    five_power_n_str = str(five_power_n)
    number_of_digits_in_2_power_n = len(two_power_n_str)
    number_of_digits_in_5_power_n = len(five_power_n_str)
    return number_of_digits_in_2_power_n + number_of_digits_in_5_power_n
print(calculate_the_number_of_digits(sys.argv[1]))
print(calculate_the_number_of_digits(sys.argv[2]))
print(calculate_the_number_of_digits(sys.argv[3]))
# python file.py 3 9 12
# 4
# 10
# 13
