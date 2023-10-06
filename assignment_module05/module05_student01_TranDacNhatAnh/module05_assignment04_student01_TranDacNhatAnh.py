# Do cả hai câu hỏi của bài toán đều hướng đến tình huống giá của cố phiếu tăng tối đa sau mỗi ngày nên ta sẽ coi giá cổ phiếu ngày thứ
# n+1 bằng 1-7% giá cổ phiếu ngày thứ n.

from additionalFolder.module04_assignment07_student01_TranDacNhatAnh import Datetime as dt

#TH1: Giá của cổ phiếu là một số thực.
price = 7.24
date = dt(8, 8, 2022)

# (a)
while 1:
    date = dt.add(date, 1)
    price *= 1.07
    print(f'The maximum price of F in {date} is {price}')
    if date.equal(dt(12, 8, 2022)):
        break
# (b)
def untilThePriceReaches(price, newPrice):
    date = dt(8, 8, 2022)
    while price < newPrice:
        date = dt.add(date, 1)
        price *= 1.07
    return f'The price of F will reach {newPrice} earliest in {date}'
print(untilThePriceReaches(7.24, 58.69))

#TH2: Giá của cổ phiếu là một số có 2 chữ số phần thập phân (đơn vị nghìn đồng)
# (a)
price1 = 7.24
date1 = dt(8, 8, 2022)
while 1:
    date1 = dt.add(date1, 1)
    price1 = round(price1*1.07, 2)
    print(f'The maximum price of F in {date1} is {price1}')
    if date1.equal(dt(12, 8, 2022)):
        break

# (b)
def untilThePriceReaches1(price, newPrice):
    date1 = dt(8, 8, 2022)
    while price < newPrice:
        date1 = dt.add(date1, 1)
        price = round(price*1.07, 2)
    return f'The price of F will reach {newPrice} earliest in {date1}'
print(untilThePriceReaches1(7.24, 58.69))