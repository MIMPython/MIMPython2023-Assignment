from .module07_assignment03_student04_TranNgocHieu_Point import Point
from .module07_assignment03_student04_TranNgocHieu_Line import Line

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