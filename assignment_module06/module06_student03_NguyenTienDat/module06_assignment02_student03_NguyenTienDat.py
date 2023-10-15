# Bài tập 2:

# mean, median:
import numpy as np
np.random.seed(31)
input = list(np.random.randint(0, 10, size=10))
def mean_normal(input) -> float:
    sum = 0
    for i in range(len(input)):
        sum += input[i]
    return sum/len(input)

def median_normal(input) -> float:
    input = sorted(input)
    if len(input) % 2 == 0:
        result = (input[int(len(input)/2)] + input[int(len(input)/2) - 1])/2
        return result
    elif len(input) % 2 == 1:
        result = input[int(len(input)/2)]
        return result
    
def mean_numpy(input) -> float:
    return np.mean(input)

def median_numpy(input) -> float:
    return np.median(input)

import time
def static_results():
    time_caculate_mean_non_numpy = []
    time_caculate_median_non_numpy = []
    time_caculate_mean_numpy = []
    time_caculate_median_numpy = []
    for i in range(1000000, 1000010):
        input = list(np.random.randint(0, 10, size=i))
        start_1 = time.time()
        time_mean_normal = mean_normal(input)
        end_1 = time.time()

        start_2 = time.time()
        time_median_normal = median_normal(input)
        end_2 = time.time()

        start_3 = time.time()
        time_mean_numpy = mean_numpy(input)
        end_3 = time.time()

        start_4 = time.time()
        time_median_numpy = median_numpy(input)
        end_4 = time.time()
        time_caculate_mean_non_numpy.append(end_1-start_1)
        time_caculate_median_non_numpy.append(end_2-start_2)
        time_caculate_mean_numpy.append(end_3-start_3)
        time_caculate_median_numpy.append(end_4-start_4)

    print('-'*117)
    print("|{}".format("Time caculate mean normal"), "|{}".format("Time caculate median normal"),\
        "|{}".format("Time caculate mean by numpy"), "|{}".format("Time caculate median by numpy"), "|")
    print('-'*117)
    
    for i in range(len(time_caculate_mean_non_numpy)):
        print("|{: <25f}".format(time_caculate_mean_non_numpy[i]), "|{: <27f}".format(time_caculate_median_non_numpy[i]),\
            "|{: <27f}".format(time_caculate_mean_numpy[i]), "|{: <29f}".format(time_caculate_median_numpy[i]), "|")
        
    print('-'*117)
        
if __name__ == "__main__":
    static_results()