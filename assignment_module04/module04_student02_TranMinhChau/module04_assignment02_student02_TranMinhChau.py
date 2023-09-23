#Bài tập 2: Xây dựng class Point để biểu diễn các điểm trong mặt phẳng tọa độ Oxy.
#1. Thiết kế phần khởi tạo của class Point (chọn tên thuộc tính phù hợp) và khởi tạo một số instance của class này.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Lấy các điểm 
A = Point(1, 2)
B = Point(3, 4)
C = Point(5, 6)
# In ra các điểm
print(f"A = [{A.x}, {A.y}]") #A = [1, 2]
print(f"B = [{B.x}, {B.y}]") #B = [3, 4]
print(f"C = [{C.x}, {C.y}]") #C = [5, 6] 

#2. Viết hàm distance() thuộc class Point để tính khoảng cách Euclid (hay còn gọi là chuẩn L2) giữa hai instance của class Point.
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(point1, point2):
    d_x = point1.x - point2.x
    d_y = point1.y - point2.y
    return math.sqrt(d_x**2 + d_y**2)

A = Point(1, 2)
B = Point(3, 4)

AB = distance(A, B)
print(f"AB = {AB}") #AB = 2.8284271247461903

#3. Bổ sung tham số metric (nhận giá trị là một str) trong hàm distance() vừa viết để tính khoảng cách giữa hai điểm theo một trong hai metric: khoảng cách Euclid (chuẩn L2) hoặc khoảng cách Manhattan (chuẩn L1). 
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance3(point1, point2, metric='Euclid'):
    dx = abs(point1.x - point2.x)
    dy = abs(point1.y - point2.y)

    if metric == 'Euclid':
        return math.sqrt(dx**2 + dy**2)
    elif metric == 'Manhattan':
        return dx + dy
    else:
        raise ValueError
# Lấy các điểm   
A = Point(1, 2)
C = Point(5, 6)
# Tính khoảng cách 
manhattan_distance = distance3(A, C, metric='Manhattan')
print(f"L1 = {manhattan_distance}") #L1 = 8

euclid_distance = distance3(A, C, metric='Euclid')
print(f"L2 = {euclid_distance}") #L2 = 5.656854249492381

#4.Viết một method để tạo một điểm đối xứng với một điểm cho trước qua gốc tọa độ.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect(self):
        reflected_x = -self.x
        reflected_y = -self.y
        return self.__class__(reflected_x, reflected_y)
# Lấy điểm A
A = Point(2, 3)
# Gọi phương thức reflect
A_reflected = A.reflect()
print(f"Tọa độ của điểm A sau khi được đối xứng qua gốc tọa độ: ({A_reflected.x}, {A_reflected.y})") #Tọa độ của điểm A sau khi được đối xứng qua gốc tọa độ: (-2, -3)

#5. Bổ sung hàm __repr__() cho class Point.
#__repr__(): trả về một chuỗi biểu diễn có thể in được của đối tượng đã cho
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
A = Point(2, 3)
print(repr(A)) #Point(2, 3)


