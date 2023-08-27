#Bài tập 5: Cho list A với các giá trị dưới đây
A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]
#a.Thay giá trị tại vị trí thứ 3 của list A bởi bình phương của chính giá trị đó.
A[2] = A[2] ** 2
print("List A mới là:", A)

#b.Xóa phần tử thứ 3 của list A bằng ít nhất hai cách khác nhau (gợi ý: sử dụng hàm pop hoặc hàm delete).
# Cách 1: Sử dụng hàm pop() để xóa và trả về phần tử ở vị trí thứ 3 (index = 2)
element = A.pop(2)
print("Phần tử đã xóa là:", element)
print("List A mới là:", A)

# Cách 2: Sử dụng hàm del để xóa phần tử ở vị trí thứ 3 (index = 2)
del A[2]
print("List A mới là:", A)

#c.Thêm vào phía cuối list A một phần tử có giá trị bằng với bình phương của phần tử cuối cùng của list A.
last_element = A[-1]
square = last_element ** 2
A.append(square)
print("List A mới là:", A)
 
#d.Tính số phần tử trong list.
print("Số phần tử trong list A là:", len(A))

#e.Tính tổng các phần tử trong list
print("Tổng số phần tử trong list A là:", sum(A))

#f.Tính tổng của các phần tử có chỉ số (index) 1, 2, 3, 5 trong list.
tong = 0
index = [1, 2, 3, 5]
for i in index:
    tong = tong + A[i]
print("Tổng của các phần tử có chỉ số ", index, "là:", tong)

#g.Tạo ra một list mới có thứ tự các phần tử đảo ngược với một list đã cho (bằng ít nhất hai cách khác nhau).
# cách 1: Sử dụng hàm reversed() để trả về một đối tượng reversed có thứ tự ngược lại của list ban đầu, sau đó chuyển đổi đối tượng đó thành list bằng hàm list().
reversed_object = reversed(A)
reverse_list = list(reversed_object)
print(reverse_list)

# Cách 2: Sử dụng toán tử cắt lát (slicing) với bước nhảy âm để lấy các phần tử của list ban đầu theo thứ tự ngược lại và gán cho một list mới. 
reverse_list = A[::-1]
print(reverse_list)

#h. Tách list ban đầu thành hai list, một chỉ chứa các số chẵn, một chỉ chứa các số lẻ.
list_chan = []
list_le = []
for x in A:
    if x % 2 == 0:
        list_chan.append(x)
    else:
        list_le.append(x)
print("List chẵn là:", list_chan)
print("List lẻ là:", list_le)

#i. Tạo một list B gồm các phần tử của list A được sắp xếp theo thứ tự giảm dần từ trái qua phải.
B = sorted(A, reverse = True)
print("List B là:", B)

#j. So sánh độ dài của hai list A và list B để thấy rằng sau khi sắp xếp, số phần tử của một list không thay đổi.
print("Số phần tử của list A trước khi sắp xếp là:", len(A))#14
A.sort(reverse = True)
print("Số phần tử của list A sau khi sắp xếp là:", len(A))#14
print("Số phần tử của list B trước khi sắp xếp là:", len(B))#14
B.sort()
print("Số phần tử của list B sau khi sắp xếp là:", len(B))#14
#Khi chạy code trên, sẽ thấy rằng độ dài của cả hai list không thay đổi sau khi sắp xếp. Điều này cho thấy việc sắp xếp chỉ thay đổi thứ tự của các phần tử trong list.

#k. Ghép hai list A và list B lại với nhau thành list C
C = A + B
print("List C là:", C)

