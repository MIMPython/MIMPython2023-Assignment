import numpy
import random
import time
import pandas
import matplotlib.pyplot as plt

# Method 1
def make_table(m, n):
    """
    Make a m*n table (list of lists) of random numbers.
    """
    myList = [
        [round(random.uniform(0, 1), 5) for j in range (n)]
        for i in range(m)
    ]
    return myList

def get_sum_of_column(table):
    """
    Get sum of numbers in the columns of a table (list of lists).
    Return a list of the sum of each column.
    """
    column_size = len(table[0])
    sum_list = []
    for column in range(column_size):
        sum = 0
        for row in range(len(table)):
            sum += table[row][column]
        sum_list.append(sum)
    return sum_list

# Method 2
def make_numpy_array(m, n):
    """
    Make a numpy array of random floats of size m*n.
    """
    num_arr = numpy.random.rand(m, n)
    return num_arr

def get_sum_of_array_column(arr):
    """
    Return an array of the sums of array columns.
    """
    return arr.sum(axis = 0)

# Get runtime data
def check_runtime_table_method1():
    """
    Return a dataframe of runtime, according to table size, 
    of "make_table" method.
    """
    size_list = []
    runtime_list = []
    for n in range(1, 1001):
        size_list.append(n)
        start_time = time.time()
        # for _ in range(n):
        myList = make_table(n, n)
        runtime = time.time() - start_time
        runtime_list.append(runtime)
    method1_get_table_df = pandas.DataFrame({
        "Size (n*n)": size_list,
        "Runtime": runtime_list,
        })
    return method1_get_table_df
# Current directory: ./module06_student04_TranNgocHieu
# method1_get_table_df = check_runtime_table_method1()
# method1_get_table_df.to_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getTableRuntime1.csv", index = False)

def check_runtime_table_method2():
    """
    Return a dataframe of runtime, according to table size, 
    of "make_numpy_array" method.
    """
    size_list = []
    runtime_list = []
    for n in range(1, 1001):
        size_list.append(n)
        start_time = time.time()
        # for _ in range(n):
        myList = make_numpy_array(n, n)
        runtime = time.time() - start_time
        runtime_list.append(runtime)
    method2_get_table_df = pandas.DataFrame({
        "Size (n*n)": size_list,
        "Runtime": runtime_list,
        })
    return method2_get_table_df
# Current directory: ./module06_student04_TranNgocHieu
# method2_get_table_df = check_runtime_table_method2()
# method2_get_table_df.to_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getTableRuntime2.csv", index = False)

def column_sum_data():
    """
    Includes all the methods used to collect data for sum runtime.
    (This is only done so that "table_list1" in "table_data" method 
    won't re-create each time the file is run.)
    """
    def create_table_data():
        """
        Create table data for column sum tests. Saved as a text file.
        To read file back to a list of tables, refer to the next two methods.
        """
        table_list = []
        for n in range(1, 31):
            table = make_table(n, n)
            table_list.append(table)
        f = open("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getATable.txt", "w")
        counter = 1
        for table in table_list:
            f.write(f"Table {counter}" + "\n")
            for row in range(len(table)):
                f.write(str(table[row]) + "\n")
            counter += 1
        f.close()
    # create_table_data()

    def convert_str_to_list(string):
        """
        (For reading from a file) Convert a list of numbers,
        represented as a string (e.g: "[1, 2, 3]") to the actual 
        list of numbers ([1, 2, 3]).
        """
        string = string.strip()[1:len(string) - 2]
        character_list = string.split(", ")
        num_list = []
        for char in character_list:
            num_list.append(float(char))
        return num_list
    # print(convert_str_to_list("[1, 2, 3]")) 
    # [1.0, 2.0, 3.0]

    def table_data():
        """
        Return module06_assignment01_student04_TranNgocHieu_getTable.txt
        as a list of tables.
        """
        file = open("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getATable.txt", "r")
        lines = file.readlines()
        lines = lines[1:]
        table_list = []
        table = []
        for line in lines:
            if line.startswith("Table"):
                table_list.append(table)
                table = []
                continue
            table.append(convert_str_to_list(line))
        table_list.append(table)   
        return table_list
    table_list1 = table_data()

    def check_runtime_column_sum_method1():
        """
        Test runtime for "get_sum_of_column" method using
        existing data (table_list1).
        """
        size_list = []
        runtime_list = []
        size = 0
        for table in table_list1:
            size += 1
            size_list.append(size)
            start_time = time.time()
            get_sum_of_column(table)
            runtime = time.time() - start_time
            runtime_list.append(runtime)
        method1_get_sum_df = pandas.DataFrame({
            "Size (n*n)": size_list,
            "Runtime": runtime_list,
            })
        return method1_get_sum_df
    # Current directory: ./module06_student04_TranNgocHieu
    # method1_get_sum_df = check_runtime_column_sum_method1()
    # method1_get_sum_df.to_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getSumRuntime1.csv", index = False)
    
    def check_runtime_column_sum_method2():
        """
        Turn data in "table_list1" to numpy arrays, then check
        runtime of "get_sum_of_array_column".
        """
        size_list, runtime_list = [], []
        size = 0
        for table in table_list1:
            size += 1
            size_list.append(size)
            as_arr = numpy.asarray(table, dtype = numpy.float32)
            start_time = time.time()
            get_sum_of_array_column(as_arr)
            runtime = time.time() - start_time
            runtime_list.append(runtime)
        method2_get_sum_df = pandas.DataFrame({
            "Size (n*n)": size_list,
            "Runtime": runtime_list,
        })
        return method2_get_sum_df
    # Current directory: ./module06_student04_TranNgocHieu
    # method2_get_table_df = check_runtime_column_sum_method2()
    # method2_get_table_df.to_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getSumRuntime2.csv", index = False)

# Comparing & plotting the data
def compare_table_generation():
    get_table_runtime1 = pandas.read_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getTableRuntime1.csv")
    get_table_runtime2 = pandas.read_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getTableRuntime2.csv")

    step = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    data1 = [get_table_runtime1["Runtime"][i - 1] for i in step]
    data2 = [get_table_runtime2["Runtime"][i - 1] for i in step]
    get_table_ratio = [data1[i] / data2[i] for i in range(len(data1))]

    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

    ax1.plot(step, data1, label = "Method 1: Self-taught")
    ax1.plot(step, data2, label = "Method 2: Numpy")
    ax1.set(ylabel = "Runtime", xticks = step, 
            title = "Table generator speed")
    ax1.legend()

    ax2.plot(step, get_table_ratio, "tab:green")
    ax2.set(xlabel = "Table size", ylabel = "Ratio", 
            title = "Ratio comparison: Method 1 vs Method 2")
    
    plt.show()
# compare_table_generation()

def compare_sum_calculation():
    get_sum_runtime1 = pandas.read_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getSumRuntime1.csv")
    get_sum_runtime2 = pandas.read_csv("./additionalFolder/module06_assignment01_student04_TranNgocHieu_getSumRuntime2.csv")

    step = [5, 10, 15, 20, 25, 30]
    data1 = [get_sum_runtime1["Runtime"][i - 1] for i in step]
    data2 = [get_sum_runtime2["Runtime"][i - 1] for i in step]
    get_table_ratio = [data1[i] / data2[i] for i in range(len(data1))]

    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

    ax1.plot(step, data1, label = "Method 1: Self-taught")
    ax1.plot(step, data2, label = "Method 2: Numpy")
    ax1.set(ylabel = "Runtime", xticks = step, 
            title = "Sum calculation speed")
    ax1.legend()


    ax2.plot(step, get_table_ratio, "tab:pink")
    ax2.set(xlabel = "Table size", ylabel = "Ratio", 
            title = "Ratio comparison: Method 1 vs Method 2")

    plt.show()
# compare_sum_calculation()





