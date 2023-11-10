from .Algebra import solveQuadratic

from math import sqrt
from numpy import Infinity

def smoothen(object1): # Do giải phương trình bậc 2 có sai số làm tròn, nên hàm này được tạo ra để làm các nghiệm "hợp lí hơn"
    if type(object1) == Line or type(object1) == Point:
        object1.x = round(object1.x, 14)
        object1.y = round(object1.y, 14)
    return object1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        return None
    
    def length(self): # Độ dài của Vector
        return sqrt(self.x**2 +self.y**2)
    
    def ratio(self):
        if self.y == 0:
            if self.x == 0:
                raise Exception('Vector(0, 0) has no ratio.')
            else:
                return Infinity
        else:
            return self.x / self.y
    
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
            raise TypeError(f'Invalid metric {metric}')
        return distance
    
    def pointSymetry(self, pointB): # Lấy đối xứng qua một điểm pointB nào đó...
        return Point(2*pointB.x - self.x, 2*pointB.y - self.y)
    
    def vectorAdd(self, vectorB: Vector): # Point + Vector --> Point
        return Point(self.x + vectorB.x, self.y + vectorB.y)
    
    def getVector(self, pointB):
        return Vector(pointB.x - self.x, pointB.y - self.y)
    def barycenter(self, w1, pointB, w2):
        x = (self.x*w1 + pointB.x*w2) / (w1+w2)
        y = (self.y*w1 + pointB.y*w2) / (w1+w2)
        return Point(x, y), w1+w2
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class Line:
    def __init__(self, vec: Vector, pt: Point): # Định nghĩa đường thẳng bằng Vector chỉ phương và một điểm trong Oxy mà nó đi qua
        self.v = vec
        self.p = pt
    
    def intersection(self, lineB):
        # Việc tìm giao điểm của 2 đường thẳng vẫn luôn gắn liền với giải hệ phương trình (trong chương trình phổ thông, đó là việc giải 
        # hệ gồm phương trình của 2 đường thẳng). Để thực hiện việc đó, em cần tạo ra một hàm giải 2 hệ pt tuyến tính.
        # Mỗi điểm trên đường thẳng có dạng Point(x, y) + Vector(a, b)*t, giải hệ sau:
        #   lineA.p + lineA.v*t1 = lineB.p + lineB.v*t2
        if Vector.ratio(self.v) == Vector.ratio(lineB.v): 
            if self.p == lineB.p: 
                raise Exception(f'{self} and {lineB} are the same line.')
            elif Vector.ratio(Point.getVector(self.p, lineB.p)) == Vector.ratio(self.v):
                raise Exception(f'{self} and {lineB} are the same line.')
            else: # Hai đường thẳng có cùng "hệ số góc" thì song song với nhau
                raise Exception(f'{self} and {lineB} are parallel lines.')
        else: # Để lấy được giao điểm, ta chỉ cần tìm t1 hoặc t2 trong hệ phương trình trên
            vec = Point.getVector(self.p, lineB.p) 
            t = Vector.area(vec, lineB.v) / Vector.area(self.v, lineB.v)
            return Point.vectorAdd(self.p, Vector.vecMultiply(self.v, t))
    
    def getParrallel(self, pointA: Point): # Lấy đường thẳng đi qua điểm pointA và song song với đường thẳng đã cho
        return Line(self.v, pointA)
    
    def getPerpendicular(self, pointA: Point): # Lấy đường thẳng đi qua điểm pointA và vuông góc với đường thẳng đã cho
        return Line(Vector.getPerpendicular(self.v), pointA)
    
    def __eq__(self, lineB) -> bool:
        if self.v.ratio() == lineB.v.ratio():
            if (self.p.getVector(lineB.v)).ratio == self.v.ratio():
                return True
        return False

    def __repr__(self):
        return f'Line({self.v}, {self.p})'

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



if __name__ == '__main__':
    pass