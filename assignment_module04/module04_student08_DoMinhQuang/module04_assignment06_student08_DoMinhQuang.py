'''Bài 6: Thiết kế class Circle'''

from module04_assignment02_student08_DoMinhQuang import Point
from module04_assignment03_student08_DoMinhQuang import Line
import math
import re

def write_midperpendicular_line(pointA: Point, pointB: Point):#Viết phương trình đường trung trực của 2 điểm
    middle_point = Point(0.5 * (pointA.x + pointB.x), 0.5 * (pointA.y + pointB.y))
    vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
    a = vector_AB.x
    b = vector_AB.y
    c = a * middle_point.x + b * middle_point.y
    mp_line = Line(a, b, -c)
    return mp_line

class Circle:#Có thể nhận vào các tham số  hoặc là 3 điểm, hoặc là tâm và bán kính, hoặc là phương trình tổng quát
    def __init__(self, *args):
        if len(args) == 3 and all(isinstance(arg, Point) for arg in args):
            self.center, self.radius = self.construct_circle_from_points(*args)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], (int, float)):
            self.center, self.radius = args
        elif len(args) == 1 and isinstance(args[0], str):
            self.center, self.radius = self.construct_circle_from_equation(args[0])
        else:
            raise ValueError("Invalid arguments")

    # def construct_circle_from_points(self, p1, p2, p3):#cái này em tìm được song không dùng, vì những bài trước
    #     x1, y1 = p1.x, p1.y                            #đã có nhiều hàm hỗ trợ cho cách ở dưới
    #     x2, y2 = p2.x, p2.y
    #     x3, y3 = p3.x, p3.y
    #
    #     d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    #     ux = ((x1 ** 2 + y1 ** 2) * (y2 - y3) + (x2 ** 2 + y2 ** 2) * (y3 - y1) + (x3 ** 2 + y3 ** 2) * (y1 - y2)) / d
    #     uy = ((x1 ** 2 + y1 ** 2) * (x3 - x2) + (x2 ** 2 + y2 ** 2) * (x1 - x3) + (x3 ** 2 + y3 ** 2) * (x2 - x1)) / d
    #
    #     radius = math.sqrt((ux - x1) ** 2 + (uy - y1) ** 2)
    #     center = Point(ux, uy)
    #
    #     return center, radius

    def construct_circle_from_points(self, A, B, C): #tâm đường tròn ngoại tiếp ABC sẽ là giao 2 đường trung trực
        mpline_1 = write_midperpendicular_line(A, B)#viết pt đường trung trực qua AB và BC
        mpline_2 = write_midperpendicular_line(B, C)
        tup = mpline_1.find_intersect(mpline_2)#tìm giao của 2 đường thẳng trên
        center = Point(tup[0], tup[1])
        radius = center.distance1(A)
        return center, radius

    def construct_circle_from_equation(self, equation):
        match = re.match(r'x\^2 \+ y\^2 ([+-]) (\d+)x ([+-]) (\d+)y ([+-]) (\d+)', equation)
        sign1, a, sign2, b, sign3, c = match.groups()

        x = f"{sign1}{a}" if sign1 == '-' else f"-{a}"
        y = f"{sign2}{b}" if sign2 == '-' else f"-{b}"
        r = math.sqrt(int(a) ** 2 + int(b) ** 2 - int(c))

        center = Point(x, y)

        return center, r

    @property
    def perimeter(self):
        return f'The perimeter of circle is {radius * 2} * pi = {radius * 2 * math.pi}'

    @property
    def area(self):
        return f'The area of circle is {radius ** 2} * pi = {radius ** 2 * math.pi}'

# Example usage
p1 = Point(0, 0)
p2 = Point(0, 4)
p3 = Point(4, 0)
circle_from_points = Circle(p1, p2, p3)
print(f"Center: ({circle_from_points.center.x}, {circle_from_points.center.y}), Radius: {circle_from_points.radius}")

center = Point(0, 0)
radius = 5
circle_from_center_radius = Circle(center, radius)
print(f"Center: ({circle_from_center_radius.center.x}, {circle_from_center_radius.center.y}), Radius: {circle_from_center_radius.radius}")

equation = "x^2 + y^2 - 4x + 6y - 12 = 0"
circle_from_equation = Circle(equation)
print(f"Center: ({circle_from_equation.center.x}, {circle_from_equation.center.y}), Radius: {circle_from_equation.radius}")

print(circle_from_center_radius.perimeter)
print(circle_from_center_radius.area)

#Chạy code:  python module04_assignment06_student08_DoMinhQuang.py







