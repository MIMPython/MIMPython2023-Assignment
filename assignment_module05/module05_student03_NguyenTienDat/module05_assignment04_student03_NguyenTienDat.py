# Bài tập 4:

import datetime

# Case 1: Integer value
 # (a)
 # The largest stock price today is 107% of yesterday's value.
def max_value_during_the_day(input):
    first_value = input
    max_value = first_value
    for i in range(9, 13):
        max_value += max_value*0.07
        print(f"The maximum value for {i}/8/2022 is:", int(max_value))       
 # (b)
 # Time to reach value is 58.69k vnd. 
def time(input):
    first_value = input
    max_value = first_value
    count = 1
    while max_value <= int(58.69):
        max_value += max_value*0.07
        count += 1
    days = count + int(count/5)*2
    # Because it is not traded on two weekends, the number of days it takes for its value to reach 58.69k is days = count + [count/5] 
    return days # output: 44

def day(input):
    a = datetime.datetime(2022, 8, 8)
    b = a + datetime.timedelta(days=input)
    return f"The value to be 58.69k vnd on {b}"

# Case 2: Similar as case 1



    
    
