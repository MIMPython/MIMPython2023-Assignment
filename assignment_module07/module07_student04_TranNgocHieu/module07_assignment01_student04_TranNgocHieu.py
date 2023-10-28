"""
Viết một hàm tính giá trị trung bình của một danh sách các số.
Bắt các lỗi liên quan đến đầu vào.
"""
def listAverage(list):
    try:
        empty_check = list[0]
        num_check = sum(list)
    except IndexError: 
        raise IndexError("List is empty.")
    except TypeError: 
        raise TypeError("List must only contain numbers.")
    return sum(list) / len(list)

a = []
b = [1, 'a']
c = [1, 2, 3]
print(listAverage(a)) # IndexError: List is empty.
print(listAverage(b)) # TypeError: List must only contain numbers.
print(listAverage(c)) # 2.0