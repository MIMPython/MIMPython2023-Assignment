class Datetime:
    def __init__(self, year, month, day, hour = 0, min = 0, sec = 0):
        self.y, self.m, self.d = year, month, day
        self.h, self.min, self.s = hour, min, sec

    def __repr__(self):
        return f"{self.d:02d}-{self.m:02d}-{self.y}"

    def getTime(self):
        """
        Return instance time in usual format.
        """
        my_time = (f"Instance date and time is "
                   f"{self.d:02d}-{self.m:02d}-{self.y} " 
                   f"{self.h:02d}:{self.min:02d}:{self.s:02d}.")
        return my_time
    
    def getWeekDay(self):
        """
        Return day of the week from date.
        """
        import pandas
        day = pandas.Timestamp(f"{self.y}-{self.m:02d}-{self.d:02d}")
        return day.day_name() 
    
    def isLeapYear(num):
        """
        Check whether given number represents a leap year.
        """
        if num % 4 == 0 and num % 100 != 0:
            return True
        elif num % 4 == 0 and num % 100 == 0:
            if num % 400 == 0:
                return True
            else: return False
        else:
            return False
        
    def leapYearCounter(num1, num2):
        """
        Count the number of leap years from 
        year num1 + 1 to year num2 - 1.
        """
        count = 0
        for i in range(num1 + 1, num2):
            if Datetime.isLeapYear(i):
                count += 1
        return count

    def compareDate(d1, d2) -> tuple:
        """
        Return tuple of dates in ascending order.
        """
        pairwise = zip([d1.y, d1.m, d1.d], [d2.y, d2.m, d2.d])
        for pair in pairwise:
            if pair[0] < pair[1]:
                return(d1, d2)
            elif pair[0] > pair[1]:
                return(d2, d1)
            else:
                continue
        return(d1, d2)
    
    def timeBetweenYear(self, date) -> int:
        """
        Return year(s) between two time instances.
        """
        return abs(self.y - date.y)
    
    def timeBetweenMonth(self, date) -> int:
        """
        Return month(s) between two time instances.
        """
        if self.y == date.y:
            return abs(self.m - date.m)
        d1, d2 = Datetime.compareDate(self, date)
        year = Datetime.timeBetweenYear(d1, d2)
        return (year*12 + d2.m - d1.m)
    
    def timeBetweenDaySameYear(d1, d2):
        """
        Calculate the days between two dates of the same year.
        """
        day = 0
        month_day_dictionary = {
            1: 31, 2: 28, 3: 31,
            4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30,
            10: 31, 11: 30, 12: 31
        }
        if Datetime.isLeapYear(d1.y):
            month_day_dictionary[2] += 1
        D1, D2 = Datetime.compareDate(d1, d2)
        if D1.m == D2.m:
            day = D2.d - D1.d
        else:
            for month in range(D1.m + 1, D2.m):
                day += month_day_dictionary[month]
            day += month_day_dictionary[D1.m] - D1.d + D2.d
        if d1.m < d2.m:
            return day
        elif d1.m > d2.m:
            return -day
        else:
            if d1.d <= d2.d:
                return day
            else:
                return -day

    def timeBetweenDay(self, date):
        """
        Return day(s) between two time instances.
        """
        d1, d2 = Datetime.compareDate(self, date)
        year = Datetime.timeBetweenYear(d1, d2)
        day = year * 365
        leap_year = Datetime.leapYearCounter(d1.y, d2.y)
        if Datetime.isLeapYear(d1.y) and not Datetime.isLeapYear(d2.y):
            if d1.m < 2:
                leap_year += 1
            elif d1.m == 2 and d1.d <= 28:
                leap_year += 1
        elif not Datetime.isLeapYear(d1.y) and Datetime.isLeapYear(d2.y):
            if d1.m >= 3:
                leap_year += 1
        elif Datetime.isLeapYear(d1.y) and Datetime.isLeapYear(d2.y) and d1.y != d2.y:
            leap_year += 1
        day += leap_year

        # After this step, if we push [day] days forward, we get the same
        # day and month for d1, but d1's year will match that of d2.
        # Except if d1 is the 29/02 of a leap year and d2 is not a leap 
        # year, it will be sent to 28/02.

        special_case = [
            Datetime.isLeapYear(d1.y),
            d1.m == 2, d1.d == 29,
            not Datetime.isLeapYear(d2.y),
        ]
        if all(special_case):
            new_d1 = Datetime(d2.y, 2, 28)
            day += Datetime.timeBetweenDaySameYear(new_d1, d2)
        else:
            new_d1 = Datetime(d2.y, d1.m, d1.d)
            day += Datetime.timeBetweenDaySameYear(new_d1, d2)
        return day
        
    def timeBetween(self, date, key = "year"):
        """
        Meassage printer for timeBetween-type methods above.
        """
        if key == "year":
            keyword = "year(s)"
            num = Datetime.timeBetweenYear(self, date)
        
        elif key == "month":
            keyword = "month(s)"
            num = Datetime.timeBetweenMonth(self, date)
        
        elif key == "day":
            keyword = "day(s)"
            num = Datetime.timeBetweenDay(self, date)

        message = (
            f"The {keyword} between instance date ({repr(self)}) "
            f"and target date ({repr(date)}) is {num}."
        )
        return message
      
def main():
    my_date = Datetime(2004, 12, 9)
    target_date = Datetime(2004, 10, 27)

    print(my_date.getTime())
    print(target_date.getWeekDay())
    print(my_date.timeBetween(target_date, key = "day"))

if __name__ == "__main__":
    main()
