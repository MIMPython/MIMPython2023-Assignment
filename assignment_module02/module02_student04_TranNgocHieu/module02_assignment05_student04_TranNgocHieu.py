# Đối với câu a) đến f), i), j), k), list A sẽ được tác động lần lượt
# qua từng câu và sẽ không thiết lập lại

A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
# list chính

# a)
A[2] = A[2]**2
print(A)    
# [70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# b)
A_copy = A[:]    # List dùng cho delete, pop

# Cách 1: dùng pop
A_copy.pop(2)    # 49
print(A_copy)    
# [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# Cách 2: dùng del (Chạy lại "A_copy = A")
A_copy = A[:]
del A_copy[2]
print(A_copy)    
# Tương tự kết quả ở cách 1

# c)
# List A đã bị xoá phần tử thứ 3 (từ câu trên)
del A[2]
A.append(A[-1]**2)
print(A)    
# [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

# d)
A_length = len(A)
print(A_length)    # 15

# e)
print(sum(A))    # 3361

# f)
print(sum((A[1], A[2], A[3], A[5])))    
# 203 (sum of elements of a tuple)

# g)
# Cách 1:
def swap_position(list, pos1, pos2):
    # Đổi chỗ phần tử ở vị trí pos1 và pos2 trong list.
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def list_inverse1(list):
    # Trả về một list mới ngược lại với list cũ.
    list_copy = list[:]
    list_length = len(list)
    for i in range(0, list_length//2):
        list_copy = swap_position(list_copy, i, list_length - i - 1)
    return list_copy

print(list_inverse1([1, 3, 5, 2, 4, 6]))
# [6, 4, 2, 5, 3, 1]

# Cách 2:
def list_inverse2(list):
    # Trả về một list mới ngược lại với list cũ.
    list_inverse = list[:]
    list_length = len(list)
    for i in range(0, list_length):
        list_inverse[i] = list[list_length - i - 1]
    return list_inverse

print(list_inverse2([1, 3, 5, 2, 4, 6]))
# [6, 4, 2, 5, 3, 1]

# h)
def split_list(list):
    # Chia một list thành hai list chứa số chẵn, lẻ.
    even_list, odd_list = [], []
    list_length = len(list)
    for i in range(0, list_length):
        if list[i]%2 == 0:
            even_list.append(list[i])
        else:
            odd_list.append(list[i])
    return even_list, odd_list

splitted_list = split_list([1, 2, 3, 4, 5, 6])
print(f'Even list: {splitted_list[0]}')
print(f'Odd list: {splitted_list[1]}')
# Even list: [2, 4, 6]
# Odd list: [1, 3, 5]

# i)
B = A[:]
B.sort(reverse = True)
print(B)
# [2809, 80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 5, 3, 3, 1]

# j)
print(len(A) == len(B))    # True

# k)
C = A + B
print(C)
# [70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809, 
#  2809, 80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 5, 3, 3, 1]


