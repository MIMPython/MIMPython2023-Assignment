from module04_assignment02_student04_TranNgocHieu import Point
from module04_assignment03_student04_TranNgocHieu import Line

class Triangle():
    def __init__(self, A: Point, B: Point, C: Point):
        self.A = A
        self.B = B
        self.C = C
    
    def area1(self):
        """
        First area formula using coordinates. Definitive answer.
        """
        return 0.5 * abs((self.B.x - self.A.x)*(self.C.y - self.A.y) - (self.C.x - self.A.x)*(self.B.y - self.A.y))
    
    def area2(self):
        """
        Second area formula: Area = 0.5 * height * base.
        Must refine result because of error.
        """
        # Area approximation
        AB = Line.lineThroughTwoPoints(self.A, self.B)
        distance = AB.distanceToPoint(self.C)
        area = 0.5 * distance * self.A.distance(self.B)

        # Refinement
        num = int(area)
        candidates = [num, num + 0.5, num + 1]
        min_num = min(abs(i - area) for i in candidates)
        for i in candidates:
            if abs(i - area) == min_num:
                return i

A = Point(0, 0)
B = Point(2, 1)
C = Point(3, -2)
triangle = Triangle(A, B, C)
print(triangle.area1())
print(triangle.area2())