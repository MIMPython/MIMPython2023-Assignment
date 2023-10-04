
#a

def maximum_of_day(n):
    F_stock = 7.24
    for i in range(1,n+1):
        F_stock += 7/100 * F_stock
        #F_stock = round(F_stock,2) #TH lấy 2 chữ số sau dấu chấm thập phân
        print("maximum stock of day" + str(i) +"is:" + str(F_stock))
        

#b:
import random
from datetime import datetime
from datetime import timedelta

def theEarliest(F_stock):
    days = 0
    while F_stock > 0:
        days += 1
        #F_stock += random.randint(-7,7) / 100 * F_stock # Trường hợp số cổ phiếu mỗi ngày ngẫu nhiên trong khoảng 93-107% so với ngày trước.
        F_stock += 7/100 * F_stock
        #F_stock = round(F_stock,2) #TH lấy 2 chữ số sau dấu chấm thập phân
        if F_stock > 58.69:
            return days
    
def Exact_day(days):
    week = theEarliest(7.24) % 7
    day_real = 2 * week + theEarliest(7.24)
    exact_time = days + timedelta(days = day_real)
    return f'The Earlist day is {exact_time}'


days = datetime(2022,8,9)
print(Exact_day(days))
    