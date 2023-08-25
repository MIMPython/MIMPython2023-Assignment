import timeit
import math

page_list = [
    1, 10, 100, 1000, 10000, 10**5, 10**6, 10**7, 10**8
]

def page_to_num_1(page):
    """
    Đầu vào là số trang của một cuốn sách. 
    Đầu ra là số chữ số cần dùng để đánh số từng ấy trang sách.
    Cách 1: Cho chỉ số chạy từ 1 đến page, cộng dần số chữ số trong
    từng lượt (lâu).
    """
    num = 0
    for i in range(1, page + 1):
        num += len(str(i))
    return num
def page_to_num_1_test():
    """
    Test hàm trên với dữ liệu page_list đã tạo.
    """
    for i in page_list:
        print(page_to_num_1(i))

# print(f'Runtime: {timeit.timeit(page_to_num_1_test, number = 1)} seconds')
"""
Output:
1
11
192
2893
38894
488895
5888896
68888897
788888898
Runtime: 26.281787176000307 seconds
"""

def page_to_num_2(page):
    """
    Cách 2: Như bài toán tiểu học
    """
    pow = len(str(page))
    if pow == 1: 
        return page
    else:
        num = 9 # Bắt đầu đếm từ trang 10.
    for i in range(1, pow - 1):
        num += (10**(i + 1) - 10**i) * (i + 1)
    num += (int(page) - 10**(pow - 1) + 1) * pow
    return num
def page_to_num_2_test():
    for i in page_list:
        print(page_to_num_2(i))

# print(f'Runtime: {timeit.timeit(page_to_num_2_test, number = 1)} seconds')
"""
Output:
1
11
192
2893
38894
488895
5888896
68888897
788888898
Runtime: 0.00015004399938334245 seconds
"""

# Đừng thử !
# print(page_to_num_2(10**1000))

def num_to_page(num):
    """
    Hàm ngược của page_to_num, sử dụng cách 2
    """
    if num <= 9:
        return num
    else:
        pow = 0
        num_copy = int(num) - 9
        while (num_copy > 0):
            pow += 1
            num_copy -= (10**(pow + 1) - 10**pow) * (pow + 1)
        # Sau bước này, pow + 1 là số chữ số của số trang.
        # Đếm số trang còn lại cần thiết 
        # trong khoảng 10^pow đến 10^(pow + 1) - 1.
        num_copy += (10**(pow + 1) - 10**pow) * (pow + 1)
        page = math.ceil(num_copy / (pow + 1)) + 10**pow - 1
        return page
    
# for i in page_list:
#     print(num_to_page(page_to_num_2(i)))
"""
Output:
1
10
100
1000
10000
100000
1000000
10000000
100000000
"""