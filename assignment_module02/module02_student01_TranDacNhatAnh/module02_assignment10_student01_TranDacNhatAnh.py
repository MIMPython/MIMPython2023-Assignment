# Gọi hàm sqrt để tính toán, gọi thư viện numpy và matplotlib để vẽ hình
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
# Tạo các lớp đối tượng liên quan đến bài toán
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
def midPoint(A: Point, B: Point):
    return Point((A.x+B.x)/2, (A.y+B.y)/2)

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    def perpendicular(self):
        return Vector(self.y, -self.x)
def vector(A: Point, B: Point):
    return Vector(B.x-A.x, B.y-A.y)
# Tạo hàm dựng tam giác đều 
# Có 2 cách dựng tam giác đều về 2 phía của đoạn thẳng AB, tương ứng cho 2 điểm là C_1 và C_2
def completeEquilateralTriangle(A: Point, B: Point):
    AB = vector(A, B)
    M = midPoint(A, B)
    C_1 = Point(M.x+(Vector.perpendicular(AB).x)*sqrt(3)/2, M.y+(Vector.perpendicular(AB).y)*sqrt(3)/2)
    C_2 = Point(M.x-(Vector.perpendicular(AB).x)*sqrt(3)/2, M.y-(Vector.perpendicular(AB).y)*sqrt(3)/2)
    return [C_1, C_2]
# Thể hiện lên hình vẽ
def buildEquilateralTriangle(A: Point, B: Point):
    C_1 = completeEquilateralTriangle(A, B)[0]
    C_2 = completeEquilateralTriangle(A, B)[1]
    # Vẽ tam giác đều thứ nhất
    x = np.array([A.x, B.x, C_1.x, A.x])
    y = np.array([A.y, B.y, C_1.y, A.y])
    plt.subplot(2, 2, 1)
    plt.plot(x,y)
    # Vẽ tam giác đều thứ hai
    x = np.array([A.x, B.x, C_2.x, A.x])
    y = np.array([A.y, B.y, C_2.y, A.y])
    plt.subplot(2, 2, 2)
    plt.plot(x,y)
    return plt.show()
# Test
A = Point(0, 0)
B = Point(0, 2)
buildEquilateralTriangle(A, B)

# Nhược điểm: chưa tìm được cách khắc phục chương trình sao cho có thể đặt tên cho các điểm trong hình vẽ