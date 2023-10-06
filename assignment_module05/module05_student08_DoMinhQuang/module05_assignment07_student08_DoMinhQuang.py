'''Bài 7: Liệu có tồn tại vô hạn số vừa đối xứng vừa chính phương?'''

import math
def check_palindrome(n: int) -> bool:
    temp = str(n)
    if temp[::-1] == temp:
        return True
    else:
        return False

def check_square(n: int) -> bool:
    x = math.sqrt(n)
    if x * x == n:
        return True
    else:
        return False

def check_both_condition(n: int) -> bool:
    while n >= 0:
        if check_palindrome(n) and check_square(n):
            return True
        else:
            return False


if __name__ == '__main__':
    n = 0
    while True:
        if check_both_condition(n):
            print('This is a number!')#Dự đoán là có thể tồn tại vô hạn số thỏa mãn vì voòng lặp chạy liên tục
        else:                         #Hiện em chưa tìm được lời giải thích nào rõ ràng hơn
            n += 1


#Chạy code: python module05_assignment07_student08_DoMinhQuang.py



