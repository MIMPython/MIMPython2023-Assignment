#Bài tập 1: Viết một chương trình sắp xếp list này theo thứ tự tăng dẫn của tổng các số trong mỗi list con.
# Hàm tính tổng của một list con
def total_list(n):
    return sum(n)
# Danh sách các list con
A = [[1,2], [3,0,4], [2], [4,5]]
# Sắp xếp danh sách các list con theo tổng các số trong mỗi list con
sort = sorted(A, key=total_list)
# In ra danh sách đã sắp xếp 
B = [n for n in sort] 
print(f"B = {B}") # B = [[2], [1, 2], [3, 0, 4], [4, 5]]

# Yêu cầu bổ sung: sẽ sắp xếp list các list con dựa trên hai tiêu chí:
# tổng các số trong list con và độ dài của list con.

def length_list(n):
    return len(n)
# So sánh hai list con
def compare_the_list(list1, list2):
    total_list1 = total_list(list1)
    total_list2 = total_list(list2)

    if total_list1 > total_list2:
        return 1
    elif total_list1 < total_list2:
        return -1
    else:
        length_list1 = length_list(list1)
        length_list2 = length_list(list2)
    
        if length_list1 > length_list2:
            return 1
        elif length_list1 < length_list2:
            return -1
        else: 
            return 0
# Sắp xếp danh sách các list con theo 2 tiêu chí trên
sorted_lists = sorted(A , key=lambda x: (total_list(x), length_list(x)))
# In ra danh sách đã sắp xếp
C = [n for n in sorted_lists]
print(f"C = {C}")




