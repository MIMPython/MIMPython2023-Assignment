# Bài tập yêu cầu viết chương trình sắp xếp các list đã cho theo thứ tự tổng tăng dần, đồng thời đề xuất các phương án khác 
# để sắp xếp các list.

# Phương án 1: Sắp xếp theo tổng các phần tử của list. Khi 2 list có tổng bằng nhau, so sánh theo "thứ tự từ điển"
def arrangeList(manyLists):
    for i in range(len(manyLists)):
        for j in range(i):
            if sum(manyLists[j]) > sum(manyLists[i]):
                temp = manyLists[i]
                manyLists[i] = manyLists[j]
                manyLists[j] = temp
            elif sum(manyLists[i])==sum(manyLists[j]):
                if manyLists[j]>manyLists[i]:
                    temp = manyLists[i]
                    manyLists[i] = manyLists[j]
                    manyLists[j] = temp
    return manyLists
# Test PA1
A = [[1, 2], [3, 0, 4], [2], [4, 5], [7,2], [3,6]]
print(arrangeList(A)) # [[2], [1, 2], [3, 0, 4], [3, 6], [4, 5], [7, 2]]

# Phương án 2: Phương án được sử dụng cho hàm sort.() của Python. Sử dụng "thứ tự từ điển" ngay từ đầu, tức là list có các phần tử ở đầu nhỏ hơn 
# sẽ được xếp lên trước.
B = A
B.sort()
# Test PA2
print(B) # [[1, 2], [2], [3, 0, 4], [3, 6], [4, 5], [7, 2]]

# Phương án 3: list có ít phần tử hơn được xếp lên trước. Khi 2 list dài bằng nhau, so sánh theo "thứ tự từ điển"
def sortLists(manyLists):
    for i in range(len(manyLists)):
        for j in range(i):
            if len(manyLists[j]) > len(manyLists[i]):
                temp = manyLists[i]
                manyLists[i] = manyLists[j]
                manyLists[j] = temp
            elif len(manyLists[i])==len(manyLists[j]):
                if manyLists[j]>manyLists[i]:
                    temp = manyLists[i]
                    manyLists[i] = manyLists[j]
                    manyLists[j] = temp
    return manyLists
C = A
print(sortLists(C)) # [[2], [1, 2], [3, 6], [4, 5], [7, 2], [3, 0, 4]]

# Tóm lại, mặc dù có rất tiêu chí khác nhau để so sánh 2 list, nhưng đa số chúng không tránh khỏi trường hợp điều kiện so sánh của 2 list "bằng nhau"
# Dù trong trường hợp nào, "thứ tự từ điển" vẫn là một tiêu chí hiệu quả để so sánh 2 đối tượng, vì đã "khác nhau" thì sẽ có 1 phần tử mà chúng khác nhau.