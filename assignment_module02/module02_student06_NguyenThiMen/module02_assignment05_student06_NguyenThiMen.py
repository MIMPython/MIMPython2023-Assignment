A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# (a) Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
def a():
    A[2] = A[2]**2
    print(A[2])

# (b) Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau 
def b():
    remove_element = A.pop(2)
    del A[2]
    print(A)

# (c) Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần
#tử cuối cùng của list A.
def c():
    A.append(A[-1]**2)
    print(A)

# (d) Tính số phần tử trong list.
def d():
    print(len(A))

# (e) Tính tổng các phần tử trong list.
def e():
    sum = 0
    for i in range(len(A)):
        sum += i
    print(sum)

# (f) Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
def f():
    print(A[1] +A[2]+A[3]+A[5])

# (g) Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho
#  (bằng ít nhất hai cách khác nhau)
def g1():
    A.reverse()
    print(A)
def g2():
    # slicing list [start:end:index]
    print(A[::-1])

# (h) Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
def h():
    even_list = []
    odd_list = []
    for i in A:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    print(even_list)
    print(odd_list)

# (i) Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
def i():
    B = A.copy()
    B.sort(reverse = True)
    return B 

# (j) So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp,
#  số phần tử của một list không thay đổi.
def j():
    B = i()
    if len(A) == len(B):
        print('Length of list A and list B are equal')
    else:
        print('Length of list A and list B are diferent')

# (k) Ghép hai list A và list B lại với nhau thành list C.
def k():
    C = A.copy()
    B = i()
    C.extend(B)
    print(C)

if __name__ == '__main__':
    print('a)')
    a()
    print('\nb)')
    b()
    print('\nc)')
    c()
    print('\nd)')
    d()
    print('\ne)')
    e()
    print('\nf)')
    f()
    print('\ng1)')
    g1()
    print('\ng2)')
    g2()
    print('\nh)')
    h()
    print('\ni)')
    i()
    print('\nj)')
    j()
    print('\nk)')
    k()



        
    






