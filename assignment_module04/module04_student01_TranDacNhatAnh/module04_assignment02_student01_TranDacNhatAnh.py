# Bài tập yêu cầu xây dựng class Point để biểu diễn các điểm trong mặt phẳng tọa độ Oxy.

# Gọi các thư viện cần thiết cho Class
from math import sqrt

# Note: khi tạo ra class này, ý định của em là dùng nó để xử lí class Line và tính diện tích tam giác ở bài tập sau, 
# tuy nhiên dùng cho class Point cũng tiện lợi nên em  đặt lên trước luôn :v
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    def length(self): # Độ dài của Vector
        return sqrt(self.x**2 +self.y**2)
    def getPerpendicular(self): # Vector vuông góc
        return Vector(-self.y, self.x)
    def vecAdd(self, vectorB): # Phép cộng Vector
        return Vector(self.x+vectorB.x, self.y+vectorB.y)
    def vecMultiply(self, a): # Phép nhân Vector với một vô hướng (số thực)
        return Vector(self.x*a, self.y*a)
    def scalarMultiply(self, vectorB): # Tích vô hướng của 2 Vector
        return self.x*vectorB.x + self.y*vectorB.y
    def area(self, vectorB): # Liên quan đến diện tích tam giác có 2 cạnh là 2 vector (chung gốc) AB và AC
        return self.x*vectorB.y - self.y*vectorB.x
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

class Point:
    def __init__(self, x, y): # Khởi tạo class Point với 2 yếu tố (x, y) - tung độ và hoành độ của điểm.
        self.x = x
        self.y = y
        return None
    def distance(self, pointB, metric: str): # Hàm trả về "khoảng cách" giữa 2 điểm (hay "độ dài" đoạn thẳng AB)
        if metric == 'L1':
            distance = abs(pointB.x - self.x) + abs(pointB.y - self.y)
        elif metric == 'L2':
            distance = sqrt((pointB.x - self.x)**2 + (pointB.y - self.y)**2)
        elif metric == 'Vec':
            distance = Vector(pointB.x - self.x, pointB.y - self.y)
        else:
            raise f'Invalid metric {metric}'
        return distance
    def pointSymetry(self, pointB): # Lấy đối xứng qua một điểm pointB nào đó...
        return Point(2*pointB.x - self.x, 2*pointB.y - self.y)
    def vectorAdd(self, vectorB: Vector): # Point + Vector --> Point
        return Point(self.x + vectorB.x, self.y + vectorB.y)
    def getVector(self, pointB):
        return Vector(pointB.x - self.x, pointB.y - self.y)
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
# test
if __name__ == '__main__':
    print(Vector.vecAdd(Vector.vecMultiply(Vector(1, 0), 3), Vector.vecMultiply(Vector(0, 1), 2))) # (3, 2) --> Tổ hợp tuyến tính :v
    print(Point.__repr__(Point(0, 0))) # Point(0, 0)
    print(Point.pointSymetry(Point(0, 2), Point(1, 3))) # Point(2, 4)
    print(Point.distance(Point(1, 4), Point(2, 0), metric='L1')) # 5