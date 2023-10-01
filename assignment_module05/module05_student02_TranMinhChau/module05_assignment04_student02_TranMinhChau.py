# Bài tập 4:
# (a) Tính giá tối đa trong mỗi ngày từ 09/08/2022 đến 12/08/2022
def max_price_each_day(a, b):
    current_price = a
    max_percentage = b
    result = current_price * max_percentage
    return result
#TH1: Giá cổ phiếu nhận giá trị là một số thực.
print(round(max_price_each_day(7.24, 1.07), 0))#8
#TH2: Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân
print(round(max_price_each_day(7.24, 1.07), 2))#7.75

# (b) Tính thời điểm sớm nhất giá đạt mức 58.69 nghìn đồng
# Sử dụng công thức: Thời gian = log(Mức mục tiêu/ Giá hiện tại)/log(Tỉ lệ tăng giá mỗi ngày + 1)
import math
def days_to_target(x, y, z):
    target_price = x
    current_price = y
    max_percentage_increase = z
    result = math.log(target_price / current_price) / math.log(max_percentage_increase + 1)
    return result 
print(days_to_target(58.69, 7.24, 0.07))#30.92949970738051

