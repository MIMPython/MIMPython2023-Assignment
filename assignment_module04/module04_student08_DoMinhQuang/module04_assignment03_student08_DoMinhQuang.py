'''Bài 3: Xây dựng lớp class Line '''
#a) Phương trình y = ax + b không là phương trình đường thẳng tổng quát vì nó không biểu diễn được đường thẵng x = c'''
#b) Điều kiện để ax + by + c = 0 là phương trình tổng quát của 1 đường thẳng là a và b không đồng thời bằng 0

import math
from module04_assignment02_student08_DoMinhQuang import Point

#Cách cơ bản
def cramer_rule_1(a1, b1, c1, a2, b2, c2) -> tuple: #Thuật toán tìm nghiệm hệ phương trình tuyến tính
    det_A  = a1 * b2 - a2 * b1
    det_A1 = c1 * b2 - c2 * b1
    det_A2 = a1 * c2 - a2 * c1
    if det_A != 0 :
        x = det_A1 / det_A
        y = det_A2 / det_A
        return (x, y)
    else:
        if a1 / a2 == b1 / b2 == c1 / c2:
            return("Infinite roots")
        else :
            return()

def cramer_rule_2(a1, b1, c1, a2, b2, c2) -> tuple: #Thuật toán tìm nghiệm hệ phương trình tuyến tính
    det_A  = a1 * b2 - a2 * b1
    det_A1 = c1 * b2 - c2 * b1
    det_A2 = c1 * a2 - c2 * a1
    try :
        x = det_A1 / det_A
        y = det_A2 / det_A
        return (x, y)
    except ZeroDivisionError:
        if a1 / a2 == b1 / b2 == c1 / c2:
            raise("Infinite roots")
        else :
            raise("No roots")


class Line:
    def __init__(self,a : float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def find_intersect(self, lineB) -> tuple:
        tupe = cramer_rule_1(self.a , self.b, - self.c, lineB.a, lineB.b, - lineB.c)#tìm giao điểm 2 đường thẳng,
        return tupe                                                             #hay là nghiệm của hệ

    import math
    def find_distance(self, pointA: Point) -> float:
        value1 = math.fabs(self.a * pointA.x + self.b * pointA.y + self.c)#công thức tính khoảng cách từ điểm -> đg thẳng
        value2 = math.sqrt(self.a ** 2 + self.b ** 2)
        distance = value1 / value2
        return distance

    @classmethod
    def line_general_equation(cls, pointA: Point, pointB: Point):
        a = pointB.y - pointA.y
        b = pointA.x - pointB.x
        c = a * pointA.x + b * pointA.y
        return cls(a, b, - c)

    @classmethod
    def write_peppendicular_line(cls,pointA: Point, pointB: Point): #Hàm này em viết trong lúc làm bài 6, song cũng không dùng tới :V
        middle_point = Point(0.5 * (pointA.x + pointB.x), 0.5 * (pointA.y + pointB.y))
        vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
        a = vector_AB.x
        b = vector_AB.y
        c = a * middle_point.x + b * middle_point.y
        return cls(a, b, -c)





if __name__ == '__main__':
    #  Vô số nghiệm -> 2 đường thằng trùng nhau
    lineA = Line(1, 1, 1)
    lineB = Line(2, 2, 2)
    print(lineA.find_intersect(lineB))# Infinite roots

    # Nghiem duy nhất -> 2 đường thằng giao nhau
    lineC = Line(2,4,5)
    lineD = Line(2,5,-4)
    print(lineC.find_intersect(lineD))#(- 20.5, 9.0)

    # Vô nghiệm -> 2 đường thẳng song song
    lineE = Line(1,1,1)
    lineF = Line(1,1,2)
    print(lineE.find_intersect(lineF))#()

    #e
    pointA = Point(1,2)
    print('Khoảng cách:',lineA.find_distance(pointA))#2.82842712474619

    #f
    point1 = Point(2, 4)
    point2 = Point(1, 2)
    line = Line.line_general_equation(point1, point2)
    print(f"Phương trình đường thẳng: {line.a}x + {line.b}y + {line.c} = 0")


#Chạy code : python module04_assignment03_student08_DoMinhQuang.py






