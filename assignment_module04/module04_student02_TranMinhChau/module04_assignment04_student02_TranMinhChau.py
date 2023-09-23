# Bài tập 4:
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Hàm tính độ dài của đoạn thẳng giữa điểm hiện tại và một điểm khác
    def distance(self, other_point):
        d_x = abs(self.x - other_point.x)
        d_y = abs(self.y - other_point.y)
        return math.sqrt(d_x**2 + d_y**2)

# Tọa độ của các điểm của tam giác
A = Point(1, 2)
B = Point(2, 6)
C = Point(6, 3)
# Tính độ dài các cạnh của tam giác
AB = A.distance(B)
AC = A.distance(C)
BC = B.distance(C)
# Tính nửa chu vi của tam giác
s = (AB + BC + AC) / 2
# Tính diện tích tam giác bằng công thức Heron
area_of_triangle = math.sqrt(s * abs(s - AB) * abs(s - BC) * abs(s - AC))

print(f"Diện tích tam giác ABC là: {area_of_triangle}") #Diện tích tam giác ABC là: 9.500000000000004

    
    
    
