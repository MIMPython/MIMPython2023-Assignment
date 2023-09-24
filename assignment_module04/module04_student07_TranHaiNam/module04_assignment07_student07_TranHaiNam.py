import pandas as pd

class DateTime:
    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def Time(self):
        time = pd.Timestamp(hour = self.hour, day = self.day, month = self.month, year = self.year)
        return time

    def Day_OfWeek(self):    
        time = self.Time()
        return f'This is day {time.day_of_week} in week ' 
    
    def Day_InMonth(self):
        day = self.Time()
        return f'This month has {day.days_in_month} days  '
    
    def Day_OfYear(self):
        day = self.Time()
        return f'This date is {day.day_of_year} in year'
    
    def isLeap_year(self):
        day = self.Time()
        return f'Is this leap year: {day.is_leap_year}'
        
    
time_01 = DateTime(2023,9,17,5)
print(DateTime.Time(time_01)) #2023-09-17 05:00:00
print(DateTime.Day_OfWeek(time_01)) #This is day 6 in week   
print(DateTime.Day_InMonth(time_01)) #This month has 30 days  
print(DateTime.Day_OfYear(time_01)) #This day is 260th in year
print(DateTime.isLeap_year(time_01)) #Is this leap year: False

