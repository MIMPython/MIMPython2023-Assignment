"""
(a): Phương trình y = ax + b không biểu diễn được các đường thẳng dạng
x = c, với c là một hằng số tuỳ ý.
(b): Điều kiện để phương trình ax + by + c = 0 là phương trình của một
đường thẳng là hai số a, b không đồng thời bằng 0.
"""
from module04_assignment02_student04_TranNgocHieu import Point

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check()

    def check(self):
        """
        Prints error message if instance does not represent a line.
        Credits to @ntqqhuiiunn.
        """
        if self.a == self.b == 0:
            print("Instance error.")
            exit(1)
            # Or raise ValueError("Invalid line.")

    def normalizeLines(self):
        """
        Optional: reduce equation to the form ax + y + c = 0 or x + c = 0,
        and convert -0.0 to 0.0
        Return a new Line object.
        """
        if self.b != 0:
            self.a, self.b, self.c = self.a / self.b, 1.0, self.c / self.b 
        else:
            self.a, self.c = 1.0, self.c / self.a
        if self.a == 0: self.a = 0.0
        if self.b == 0: self.b = 0.0
        if self.c == 0: self.c = 0.0
        return Line(self.a, self.b, self.c)

    def __repr__(self):
        string = (f"Equation type ax + by + c = 0\n"
                    f"a: {self.a}\n"
                    f"b: {self.b}\n"
                    f"c: {self.c}")
        return string

    def getIntersection(self, line):
        """
        Return the point of intersection as an instance of Point class.
        If there is no root, or infinite roots, raise error.
        """
        det = self.a * line.b - line.a * self.b
        detx = line.c * self.b - self.c * line.b
        dety = line.a * self.c - self.a * line.c
        try:
            x = detx / det
        except ZeroDivisionError:
            if self.c != line.c:
                raise ValueError("No root.")
            else:
                raise ValueError("Infinite roots.")
        return Point(detx / det, dety / det)
    
    def distanceToPoint(self, point):
        """
        Return distance from an input point to line.
        """
        import math
        return abs(self.a * point.x + self.b * point.y + self.c) / math.sqrt(self.a**2 + self.b**2)

    def lineThroughTwoPoints(point1: Point, point2: Point):
        """
        Return a line object passing through two given points.
        """
        a1, a2 = point1.x, point1.y
        b1, b2 = point2.x, point2.y
        if a1 == b1 and a2 == b2:
            raise ValueError("Points must be different.")
        else:
            object = Line(a2 - b2, b1 - a1, b1 * (b2 - a2) - b2 * (b1 - a1))
            return object.normalizeLines()
        
    def getPerpendicularBisector(point1: Point, point2: Point):
        """
        Return the perpendicular bisector of a segment connecting two 
        points as a Line object.
        """
        a1, a2 = point1.x, point1.y
        b1, b2 = point2.x, point2.y
        midpoint = Point((a1 + b1) / 2, (a2 + b2) / 2)
        normal_vect = (float(b1 - a1), float(b2 - a2))
        return Line(
            normal_vect[0], 
            normal_vect[1], 
            -(normal_vect[0] * midpoint.x + normal_vect[1] * midpoint.y)
            ).normalizeLines(), midpoint
            
def main():
    # Initiate two lines
    line1 = Line(1, 1, -1)
    line2 = Line(1, -1, 0)

    # Get intersection
    point1 = line1.getIntersection(line2)
    print(repr(point1))

    # Get distance
    point2 = Point(0, 0)
    print(line1.distanceToPoint(point2))

    # Get line through two points
    C = Line.lineThroughTwoPoints(point1, point2)
    print(repr(C))

    # Get perpendicular bisector
    print(Line.getPerpendicularBisector(point2, Point(3, 4)))

if __name__ == "__main__":
    main()