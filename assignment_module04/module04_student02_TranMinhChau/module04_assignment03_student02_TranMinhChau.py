# Bài tập 3: Xây dựng class Line để biểu diễn các đường thẳng trong mặt phẳng Oxy
"""
(a). Vì :
+ Nếu a = 0, thì đường thẳng sẽ song song với trục Ox và có phương trình y = b, phương trình 
này không thể biểu diễn dưới dạng y = ax + b với a,b bất kỳ.
+ Nếu y = 0, thì đường thẳng sẽ song song với trục Oy và có phương trình x = c, phương trình
này không thể biểu diễn dưới dang y = ax + b với a, b bất kỳ.
VD: Đường thẳng không thể biểu diễn qua phương trình y = ax + b, với a, b bất kỳ
+ y = b
+ x = c 

(b). Điều kiện của ba tham số a, b, c để phương trình  ax + by + c = 0 phương trình tổng quát
của một đường thẳng trong mặt phẳng Oxy là :
+ a và b không cùng bằng 0: Điều này đảm bảo rằng đường thẳng không song song với cả trục x và
trục y. Nếu cả a và b đều bằng 0, thì phương trình sẽ trở thành c = 0, không còn biểu diễn đường
thẳng mà là một điểm duy nhất tại gốc tọa độ (0, 0).
+ Không có tham số nào bằng 0: Nếu c ≠ 0, thì đường thẳng có thể bất kỳ và không phụ thuộc vào 
giá trị của a, b, c. Nó có thể là một đường thẳng bất kỳ.

(c) Nhận xét về đoạn code
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
- Ưu điểm:
+ Đơn giản dễ hiểu
+ Có thể tái sử dụng bằng các gọi constructor và truyền các giá trị tương ứng
- Nhược điểm:
+ Thiếu kiểm tra đầu vào (b không thể bằng 0 vì đó sẽ là đường thẳng dọc)
+ Không có xử lý ngoại lệ (truyền không đúng số lượng đối số)
+ Có thể gây xung đột về tên 
+ Không có phương thức khác (ví dụ như tính khoảng cách từ một điểm đến đường thẳng)
"""

#(d): Viết một phương thức trong class Line để xác định (những) giao điểm của hai đường thẳng (nếu có).
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_intersection(self, other_line):
        # Trường hợp hai đường thẳng trùng nhau
        if self.a == other_line.a and self.b == other_line.b and self.c == other_line.c:
            return "Infinite roots"  
        # Dùng công thức cramer để kiểm tra hai đường thẳng có giao nhau không
        determinant = self.a * other_line.b - other_line.a * self.b
        # Trường hợp hai đường thẳng song song, không có giao điểm
        if determinant == 0:
            return ()  
        # Trường hợp hai đường thẳng có một điểm giao điểm
        else:
            x = (self.b * other_line.c - other_line.b * self.c) / determinant
            y = (self.c * other_line.a - other_line.c * self.a) / determinant
        return (x, y)  

#(e): Viết một method trong class Line để xác định khoảng cách giữa một điểm và một đường thẳng.
# Khoảng cách từ một điểm (x0, y0) đến đường thẳng Ax + By + C = 0 được tính bằng công thức:|(Ax0 + By0 + C)| / sqrt(A^2 + B^2)
import math

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def distance_to_point(self, x0, y0):
        # Tính khoảng cách từ điểm (x0, y0) đến đường thẳng Ax + By + C = 0
        distance = abs((self.a * x0 + self.b * y0 + self.c) / math.sqrt(self.a**2 + self.b**2))
        return distance
    
# Lấy A=1, B=2, C=3
line = Line(1, 2, 3)
# Tính khoảng cách từ điểm (4, 5) đến đường thẳng
distance = line.distance_to_point(4, 5)
print(f"Khoảng cách từ một điểm (4, 5) đến đường thẳng Ax + By + C = 0 là {distance}") #Khoảng cách từ một điểm (4, 5) đến đường thẳng Ax + By + C = 0 là 7.602631123499284

#(f): Viết một method trong class Line để khởi tạo một đường thẳng (là một instance của class Line) với tham số đầu vào là hai instance của class Point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_points(cls, point1, point2):
        # Tính các hệ số A, B, C từ hai điểm
        a = point2.y - point1.y
        b = point1.x - point2.x
        c = point1.x * point2.y - point2.x * point1.y

        return cls(a, b, c)

# Tạo hai đối tượng Point
point1 = Point(1, 2)
point2 = Point(3, 4)
# Tạo một đường thẳng từ hai điểm
line = Line.from_points(point1, point2)
# Kiểm tra hệ số của đường thẳng đã được khởi tạo từ hai điểm
print(line.a)  
print(line.b)  
print(line.c)  




