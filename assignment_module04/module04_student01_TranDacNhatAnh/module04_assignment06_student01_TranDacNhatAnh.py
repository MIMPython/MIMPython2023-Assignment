# Bài tập yêu cầu xây dựng class Circle để biểu diễn đường tròn trong mặt phẳng Oxy
from module04_assignment02_student01_TranDacNhatAnh import Point
from module04_assignment02_student01_TranDacNhatAnh import Vector
from module04_assignment03_student01_TranDacNhatAnh import Line
# Phục vụ giải các phương trình liên quan đến đường tròn :v
from math import sqrt
def solveQuadratic(a,b,c):
    if a==0:
        if b==0:
            return ()
        else:
            return (-c/b, )
    else:
        delta = b*b-4*a*c
        if delta <0:
            return ()
        elif delta==0:
            return (-b/(2*a), )
        else:
            return (min((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)), max((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)))
def smoothen(object1): # Do giải phương trình bậc 2 có sai số làm tròn, nên hàm này được tạo ra để làm các nghiệm "hợp lí hơn"
    if type(object1) == Line or type(object1) == Point:
        object1.x = round(object1.x, 14)
        object1.y = round(object1.y, 14)
    return object1
class Circle:
    def __init__(self, center: Point, radius):
        self.c = center
        self.r = radius
    def intersection(self, circleB): # Tìm giao điểm của 2 đường tròn
        # Để tìm giao điểm của 2 đường tròn, ta cần tìm nghiệm của hệ phương trình:
        # (1) (x-A.x)**2 + (y-A.y)**2 = A.r**2
        # (2) (x-B.x)**2 + (y-B.y)**2 = B.r**2 ||A(Ax, Ay), B(Bx, By) là tâm đường tròn, Ar và Br là các bán kính||
        # Hướng giải: (1)-(2): x*(A.x-B.x) + y*(A.y-B.y) = (const)
        # --> Biểu diễn y theo x sau đó giải pt bậc 2:
        # y = (const - x*(A.x-B.x)) / (A.y - B.y)
        # --> (x-A.x)**2 + ((const-x*(A.x-B.x)) / (A.y - B.y) - A.y)**2 = A.r**2
        # --> (x**2 - 2*x*A.x + A.x**2) + ((x*(A.x-B.x)/(A.y-B.y))**2 - 2*x*(const/(A.y-B.y)-A.y)+ (const/(A.y-B.y)-A.y)**2) = A.r**2
        # --> x**2*(1+(A.x-B.x)/(A.y-B.y)) - 2*x*(A.y-A.x-const/(A.y-B.y)) + (A.x**2+(const/(A.y-B.y)-A.y)**2-A.r**2) = 0
        # Trên đây là biến đổi đại số, tiếp theo bên dưới sẽ chỉ làm gọn các biến và tìm nghiệm bằng hàm solveQuadratic nói trên.
        vectorAB = Point.distance(self.c, circleB.c, metric='Vec')
        const1 = ((self.c).x**2 + (self.c).y**2 - (circleB.c).x**2 - (circleB.c).y**2 - self.r**2 + circleB.r**2) / 2
        if Vector.length(vectorAB) > (self.r + circleB.r) or Vector.length(vectorAB) < abs(self.r - circleB.r):
            raise 'No intersection' # Hai đường tròn chứa nhau hoặc nằm ngoài nhau
        elif vectorAB.y == 0: # (1)-(2): x*(A.x-B.x) = (const). Trường hợp này cần xử lí riêng vì A.y-B.y=0 thì phép chia sẽ khá phiền.
            x = -const1 / vectorAB.x
            y1 = (self.c).y - sqrt((self.r**2 - (x - (self.c).x)**2))
            y2 = (self.c).y + sqrt((self.r**2 - (x - (self.c).x)**2))
            return smoothen(Point(x, y1)), smoothen(Point(x, y2))
        else:
            const2 = -const1 / (vectorAB.y)
            x1, x2 = solveQuadratic(1+Vector.ratio(vectorAB)**2, 2*((self.c).y - (self.c).x - const2), (self.c).x**2 + (const2 - (self.c).y)**2 - self.r**2)
            y1, y2 = (const2 - x1*Vector.ratio(vectorAB)), (const2 - x2*Vector.ratio(vectorAB))
            return smoothen(Point(x1, y1)), smoothen(Point(x2, y2))
    def tangent(self, pointA: Point): # Vẽ tiếp tuyến từ điểm A tới đường tròn (O)
        vectorOA = Point.getVector(self.c, pointA)
        if Vector.length(vectorOA) < self.r:
            return f'No tangent. Point {pointA} is in Circle {self}.'
        else:
            # Dựng đường tròn đường kính OA
            tangentCircle = Circle(Point.vectorAdd(self.c, Vector.vecMultiply(vectorOA, 0.5)), Vector.length(vectorOA)*0.5)
            # 2 tiếp tuyến sẽ là đường thẳng đi qua A và từng giao điểm của (O) với đường tròn (OA)
            pointB, pointC = Circle.intersection(self, tangentCircle)
            lineAB = Line(smoothen(Point.getVector(pointA, pointB)), pointA)
            lineAC = Line(smoothen(Point.getVector(pointA, pointC)), pointA)
            return lineAB, lineAC
    def __repr__(self):
        return f'Circle({self.c}, {self.r})'
    # Còn nhiều thứ em thấy đáng bỏ công ra định nghĩa nhưng vì thời gian có hạn nên em sẽ bổ sung sau ạ :v
if __name__=='__main__':
    print(Circle.intersection(Circle(Point(-1, 0), 1), Circle(Point(1, 0), 1))) # Point(0.0, 0.0), Point(0.0, 0.0)
    print(Circle.tangent(Circle(Point(0, 0), 2), Point(4, 0))) # Line(Vector(-3, -sqrt(3)), Point(4, 0)), Line(Vector(-3, sqrt(3)), Point(4, 0))
    print(Circle.tangent(Circle(Point(0, 0), 2), Point(2, 2))) # Line(Vector(-2, 0), Point(2, 2)), Line(Vector(0, -2), Point(2, 2))
    # Trường hợp tiếp xúc là trường hợp đặc biệt, tuy nhiên ở đây em vẫn coi như 2 đường tròn có 2 giao điểm trùng nhau 
    # --> trả về 1 điểm 2 lần.