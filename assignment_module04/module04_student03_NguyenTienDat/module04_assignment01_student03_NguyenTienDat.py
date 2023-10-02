# Bài tập 1:
A = [[1,2], [3,0,4], [2], [4,5]] # input1

# Hàm sắp xếp danh sách danh sách con ổn
def sort(input):
    return sorted(input, key=sum)


print(sort(A))  # output: B = [[2], [1,2], [3,0,4], [4,5]] 

# Hàm so sánh số lượng phần tử của 2 list bất kì
C = [[2], [1,2], [3,0,4], [4,5], [5]] # input2
def compare_list(input1, input2):
    if len(input1) > len(input2):
        return str(input1) + "\n" + str(input2)
    else: return str(input2) + "\n" + str(input1)
    
print(compare_list(A,C))