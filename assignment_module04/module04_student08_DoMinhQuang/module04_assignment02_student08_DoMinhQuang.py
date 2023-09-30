'''Bài 2
a) Thiết kế phần khởi tạo của class Point (chọn tên thuộc tính phù hợp) và khởi tạo một số instance của class này.
b) Thiết kế hàm distance thuộc class Point để trả về khoảng cách Euclide giữa 2 instance
c) Bổ sung tham số metric, tùy vào tham số đó mà sẽ trả về khoảng cách Euclide hay khoảng cách Manhattan
d) Viết một method tìm điểm đối xứng qua gốc tọa đọ
e) Bổ sung hàm __repr__() cho class'''

from math import fabs, sqrt
#1
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


    def distance1(self, B) -> float:#2
        a = B.x - self.x
        b = B.y - self.y
        return sqrt(a * a + b * b)

    def distance2(self, B, metric: str) -> float:#3
        if metric == 'L1' :
            distance = fabs(self.x - B.x) + fabs(self.x - B.y)
        elif metric == 'L2' :
            distance = pointA.distance1(B)
        return distance

    def find_symmertry2(self, A):# cách 2
        symmetry_point = Point(- A.y, - A.x)
        return symmetry_point

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


def find_symmetry1(A: Point) -> Point: # cách 1
    symmetry_point = Point( - A.y, - A.x)
    return symmetry_point





if __name__ == '__main__':
    pointA = Point(1, 4)
    pointB = Point(4,10)

    distL1 = pointA.distance2(pointB, metric = 'L1') #12
    print(distL1)
    distL2 = pointA.distance2(pointB, metric = 'L2') #6.708203932499369
    print(distL2)

    pointC = find_symmetry1(pointA)
    print(f'({pointC.x}, {pointC.y})')#(-4, -1)

    pointD = pointA.find_symmertry2(pointA)
    print(f'({pointD.x}, {pointD.y})')# (-4, -1)

    print(pointA.__repr__())#(1, 4)
    # pointC = eval(repr(pointA))
    # print(pointC)  ##Point(1, 4)

#Chạy code : python module04_assignment02_student08_DoMinhQuang.py









