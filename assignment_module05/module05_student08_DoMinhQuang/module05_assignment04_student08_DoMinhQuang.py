'''Bài 4: Tính giá cao nhất có thể trong một ngày khi đã biết giá trị cổ phiếu ban đầu và tỉ lệ tăng giảm giá
          Tìm thời điểm giá cổ phiếu chạm một mốc cho trước'''

import math
import datetime

#TH1
#a)
price_at_8 = 7.24 # Giá cổ phiếu F vào ngày 08/08/2022
min_rate = 0.93 # Tỉ lệ tối thiểu so với ngày trước
max_rate = 1.07 # Tỉ lệ tối đa so với ngày trước
target = 58.69 # Giá cổ phiếu mục tiêu

day_08 = datetime.datetime(2022, 8, 8)

# Tính giá tối đa trong mỗi ngày từ 09/08/2022 đến 12/08/2022
list_price = [price_at_8 * (1.07 ** i) for i in range(1, 5)]
print(list_price)
for i in range(9, 13):
    print(f'Giá cổ phiếu ngày {i}/8/2022: {list_price[i - 9]} nghìn đồng ')

#b)
# Tính thời điểm sớm nhất mà giá cổ phiếu chạm mốc mục tiêu
day = 0 # Số ngày cần thiết để chạm mốc mục tiêu
price = price_at_8 # Giá cổ phiếu hiện tại vào ngày 08/08/2022
while price < target:
    day += 1
    price *= max_rate

day_reach_target = day_08 + datetime.timedelta(day)

print(f"Thời điểm sớm nhất mà giá cổ phiếu F chạm mốc {target} nghìn đồng là sau {day} ngày giao dịch, tức là vào ngày {day_reach_target.day}/{day_reach_target.month}/{day_reach_target.year}\n")


#TH2
list_price = [round(price_at_8 * (1.07 ** i), 2) for i in range(1, 5)]
print(list_price)
for i in range(9, 13):
    print(f'Giá cổ phiếu ngày {i}/8/2022: {list_price[i - 9]} nghìn đồng ')

day = 0 # Số ngày cần thiết để chạm mốc mục tiêu
price = price_at_8 # Giá cổ phiếu hiện tại vào ngày 08/08/2022
while price < target:
    day += 1
    price *= max_rate

day_reach_target = day_08 + datetime.timedelta(day)

print(f"Thời điểm sớm nhất mà giá cổ phiếu F chạm mốc {target} nghìn đồng là sau {day} ngày giao dịch, tức là vào ngày {day_reach_target.day}/{day_reach_target.month}/{day_reach_target.year}\n")

#Ban đầu em nghĩ việc làm tròn có thể ảnh hưởng đến kết quả, song kết quả của 2 TH vẫn giống nhau

#Chạy code: python module05_assignment04_student08_DoMinhQuang.py