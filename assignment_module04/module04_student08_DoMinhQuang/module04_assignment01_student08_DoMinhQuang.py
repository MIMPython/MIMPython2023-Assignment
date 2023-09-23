'''Bài 1: Sắp xếp lại list sau theo thứ tự tăng dần của tổng các phần tử trong list con
          Một list được gọi là ổn nếu nó chỉ chứa các số thực và có ít nhất một phần tử là số thực
          Đặt thêm tiêu chí để so sánh 2 list ổn'''



A = [[1,2], [3,0,4], [2], [4,5]]
# for i in range(len(A) - 1) :
#    for j in range(i + 1, len(A)) :
#        if sum(A[i]) > sum(A[j]) :
#            A[i], A[j] = A[j], A[i]
# print(A)

A.sort(key = lambda x : sum(x))
print(A)


def check_element(list) :
    for element in list :
        if not type(element) is int and not type(element) is float : #nếu loại phần tử không phải là float hay int, return False
            return False
        return True

'''Bổ sung thêm tiêu chí cho list ổn: không có 2 phần tử nào trùng nhau'''
def check_list(list) :
    if list and check_element(list) : #Kiểm tra điều kiêện list không rỗng và có các phần tử thỏa mãn check_element
        if len(set(list)) < len(list):#Kiểm tra xem có 2 phần tử trùng nhau không
            return False
        return True
    else:
        return False

B = []
C = ['M','I','M']
D = [2,5,2,65,2.5]
E = [1,2,3,4]
print(check_list(B))#False
print(check_list(C))#False
print(check_list(D))#False
print(check_list(E))#True

#Chạy code : python module04_assignment01_student08_DoMinhQuang.py












