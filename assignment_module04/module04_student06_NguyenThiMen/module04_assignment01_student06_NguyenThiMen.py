'''Sắp xếp list theo thứ tự tăng dần của tổng các phần tử trong list con.
Một list được goi là ổn nếu nó chỉ chứa số thực và chứa ít nhất một phần tử
'''
# A = [[1,2], [3,0,4], [2], [4,5]] # input
# B = [[2], [1,2], [3,0,4], [4,5]] # output'''

A = [[1, 2], [3, 0, 4], [2], [4, 5]]
# sd sorted
B = list(sorted(A, key=lambda x: sum(x)))
# sd sort
A.sort(key=sum)
print(A)

# bổ sung thêm tiêu chí để so sánh 2 list ổn
