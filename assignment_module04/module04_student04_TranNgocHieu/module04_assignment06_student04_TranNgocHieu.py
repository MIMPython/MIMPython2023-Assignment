from module04_assignment02_student04_TranNgocHieu import Point
from module04_assignment03_student04_TranNgocHieu import Line

class Circle:
    def __init__(self, *args):
        """
        Initialize a circle using two methods:
        1) Through its center an radius
        2) Through 3 non-collinear points
        """
        if len(args) == 2:
            self.o = args[0]
            self._radius = args[1]
        else:
            self.A = args[0]
            self.B = args[1]
            self.C = args[2]
            self.checkInput()
            self.o = None
            self._radius = None

    def checkInput(self):
        if self.A.isCollinear(self.B, self.C):
            raise ValueError("Three points must not be collinear.")

    def __repr__(self) -> str:
        string = (f"Class: Circle\n"
                  f"Center:\n{self.center}\n"
                  f"Radius: {self.radius}")
        return string

    def findCenter(self):
        pb_AB = Line.getPerpendicularBisector(self.A, self.B)[0]
        pb_BC = Line.getPerpendicularBisector(self.B, self.C)[0]
        self.o = pb_AB.getIntersection(pb_BC)
        return self.o
    
    def findRadius(self):
        self._radius = self.o.distance(self.A)
        return self._radius
    
    @property
    def radius(self):
        """
        Circle's radius
        """
        if self._radius == None:
            self.findRadius()
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        self._radius = value
        return self._radius

    @property
    def center(self):
        """
        Circle's center
        """
        if self.o == None:
            self.findCenter()
        return self.o
    
    @center.setter
    def center(self, point: Point):
        self.o = point
        return self.o

def main():
    circle1 = Circle(Point(0, 0), Point(1, -1), Point(2, 3))
    print(repr(circle1))
    print(circle1.center.distance(circle1.A))
    print(circle1.center.distance(circle1.B))
    print(circle1.center.distance(circle1.C))

    circle2 = Circle(Point(3, 4), 2)
    print(repr(circle2))

    circle2.radius = 2.5
    circle2.center = Point(-1, 3)
    print(repr(circle2))

if __name__ == "__main__":
    main()

"""
Đề xuất: Có thể thêm phương thức biện luận giao điểm của một đường
tròn và một đường thẳng, hoặc của hai đường tròn. Nếu thuần tuý giải hệ
phương trình (cho đường thẳng và đường tròn), thì kết quả sẽ chính xác
hơn, nhưng khó làm (đặc biệt với hai đường tròn). Một cách khác là thông
qua đặc trưng hình học của chúng, nhưng sẽ có nhiều bước làm việc với 
số thực và có sai số lớn hơn.
"""