# Bài tập yêu cầu viết hàm tính giá trị trung bình của các phần tử trong một list
def listAverage(lst: list) -> float:
    try:
        return sum(lst)/len(lst)
    
    # Nếu list không có phần tử nào
    except ZeroDivisionError:
        return f'List {lst} has no element'
    
    # Nếu list có các phần tử không phải số thực
    except TypeError:
        return f'Some elements of list {lst} is not a number'
    # Sẽ không có exception khác vì nếu list có ít nhất 1 phần tử và chỉ gồm các số thì luôn tồn tại trung bình cộng.

# Test
testList = [[0, 1, 2, 3, 4], ['s', 2], []]
for lst in testList:
    print(listAverage(lst)) # 2.0 / Some elements of ['s', 2] is not a number / List [] has no element