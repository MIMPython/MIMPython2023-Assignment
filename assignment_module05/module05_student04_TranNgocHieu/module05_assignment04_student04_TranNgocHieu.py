import math
from datetime import datetime, timedelta
# Case 1
# def case1(stock, gain, target_price):
#     """
#     Given inital stock value and maximum daily gain, 
#     calculate the number of days for stock price to reach target price.
#     """

begin_date = datetime(2022, 8, 9)
F_price = 7.24

print("Case 1")
# a)
def a1():
    new_price = F_price
    print("Maximum stock price:")
    for day in range(1, 4):
        date = (begin_date + timedelta(days = day)).strftime("%d-%m-%Y")
        new_price *= 1.07
        print(f"{date}: {new_price}")
a1()

# b)
def b1():
    new_price = F_price
    days_taken = 0
    while new_price < 58.69:
        days_taken += 1
        new_price *= 1.07
    end_date = (begin_date + timedelta(days = days_taken)).strftime("%d-%m-%Y")
    return end_date
print(b1())

# Case 2: Lặp lại quá trình ở trên, thêm bước làm tròn giá trị.
print("Case 2")
# a)
def a2():
    new_price = F_price
    print("Maximum stock price:")
    for day in range(1, 5):
        date = (begin_date + timedelta(days = day)).strftime("%d-%m-%Y")
        new_price = round(new_price * 1.07, 2)
        print(f"{date}: {new_price}")
a2()

# b)
def b2():
    new_price = F_price
    days_taken = 0
    while new_price < 58.69:
        days_taken += 1
        new_price = round(new_price * 1.07, 2)
    end_date = (begin_date + timedelta(days = days_taken)).strftime("%d-%m-%Y")
    return end_date
print(b2())