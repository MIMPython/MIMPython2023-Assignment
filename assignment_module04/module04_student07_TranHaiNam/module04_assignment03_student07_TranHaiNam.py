#a: y = ax+b không biểu diễn được đường thẳng x = c (c là tham số bất kì).
#b: pt ax + by + c = 0 là pt tổng quát của mp Oxy khi a**2 + b**2 != 0 hay a và b không đồng thời bằng 0.
from module04_assignment02_student07_TranHaiNam import Point
import math

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_condition(self):
        if self.a != 0 and self.b != 0:
            return True
        else:
            return False
    
    def __repr__(self):
        return f'{self.a}x +{self.b}y + {self.c} = 0'

    def make_line(self):
        if Line.check_condition(self) == False:
            rep = "It's not a line "
        else:
            rep = "{self.x}x + {self.b}y + {self.c} = 0 "
        return rep

    def intersection(self, other):
        if ( other.a / self.a ) - ( other.b / self.b ) == 0:
            if ( other.c / self.c ) != ( other.a / self.a ):
                return " Two line are parallel"
            else:
                return " infinity common point "
        else:
            x = ( -self.c - ( self.b*(self.a * other.c - other.a * self.c) ) / ( other.a * self.b - self.a * other.b ) ) / self.a
            y =( self.a * other.c - other.a * self.c ) / ( other.a * self.b - self.a * other.b )
            return f' Giao điểm là: {(x,y)} ' 
    
    def dist_PointToLine(self, Point):
        return abs( self.a * Point.x + self.b * Point.y + self.c) / math.sqrt(self.a**2 + self.b**2)
    
    @classmethod
    def creat_line(cls, PointA, PointB):
        a = PointB.y - PointA.y
        b = PointA.x - PointB.x
        c = -a*PointA.x - b*PointA.y
        return cls(a,b,c)
    
if __name__ == '__main__':
    pointA = Point(3,4)
    pointB = Point(4,9)
    print(Line.creat_line(pointA,pointB)) #5x +-1y + -11 = 0

    line1 = Line(1,2,3)
    line2 = Line(7,8,9)
    print(Line.intersection(line1,line2)) #giao điểm là: (1,2)

    print(Line.dist_PointToLine(line1,pointA)) #Khoảng cách xấp xỉ là: 6,2