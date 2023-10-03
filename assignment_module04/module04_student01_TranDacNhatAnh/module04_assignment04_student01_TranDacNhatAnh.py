from module04_assignment02_student01_TranDacNhatAnh import Point
from module04_assignment02_student01_TranDacNhatAnh import Vector
# Do ở file assignment02 em đã định nghĩa hàm tính diện tích 1 tam giác theo 2 vector cạnh của nó, nên ở đây em chỉ việc lấy ra dùng :v
def triangleArea(pointA: Point, pointB: Point, pointC: Point):
    sideAB = Point.distance(pointA, pointB, metric='Vec')
    sideAC = Point.distance(pointA, pointC, metric='Vec')
    return abs(Vector.area(sideAB, sideAC)/2)
# test
if __name__ == '__main__':
    print(triangleArea(Point(1, 3), Point(3, 5), Point(6, 4))) # 0.5