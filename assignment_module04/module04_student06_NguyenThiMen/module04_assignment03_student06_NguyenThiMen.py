'''
Phương trình ax+by+c=0 là phương trình tổng quát của một đường thẳng trong mặt phẳng Oxy với điều kiện a^2+b^2 != 0.
Điều kiện này đảm bảo rằng đường thẳng không song song với trục tọa độ và không trùng với trục tọa độ. Nếu a^2+b^2==0,
thì đường thẳng sẽ không tồn tại.
'''
# class Line
from module04_assignment02_student06_NguyenThiMen import Point
import numpy as np
import math


class Line:
    '''
    biểu diễn các đường thẳng trong mặt phẳng Oxy
    '''

    def __init__(self, a, b, c):
        if a**2 + b**2 == 0:
            raise ValueError(
                'The condition for a straight line: a^2 + b^2 must not equal 0')
        else:
            self._a = a
            self._b = b
            self._c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.getter
    def b(self, b):
        self._b = b

    @property
    def c(self):
        return self._c

    @c.getter
    def c(self, c):
        self._c = c

    def __repr__(self):
        return f'Line: {self._a}*x + {self._b}*y + {self._c} = 0'

    def get_intersection(line1, line2):
        '''
        Xác định giao điểm của 2 đường thẳng
        TH1: hai đường thẳng không có giao điểm -> (,)
        TH2: hai đường thẳng có duy nhất một giao điểm -> (x,y)
        TH3: hai đường thẳng trùng nhau, vô số giao điểm -> ???
        '''
        condition = (line1._a == line2._a) and (line1._b == line2._b)
        if condition:
            if line1._c == line2._c:
                return None
            else:
                return ()
        else:
            A = np.array([[line1._a, line1._b],
                          [line2._a, line2._b]])
            b = np.array([-line1._c, -line2._c])

            x, y = np.linalg.solve(A, b)
            return (x, y)

    def get_distance_from_point_to_line(point, line):
        '''
        tính khoảng cách từ 1 điểm đến đường thẳng 
        '''
        distance = math.fabs(line._a*point._x + line._b*point._y +
                             line._c) / (math.sqrt(line._a ** 2 + line._b ** 2))

        return distance

    @classmethod
    def create_line_by_two_points(cls, point1, point2):
        '''
        tìm phương trình đường thẳng biết 2 điểm cho trước
        '''
        x1, y1 = point1._x, point1._y
        x2, y2 = point2._x, point2._y
        if x1 == x2:
            return cls(1, 0, -x1)
        elif y1 == y2:
            return cls(0, -1, -y1)
        a = y1 - y2
        b = x2 - x1
        c = x1*y2 - x2*y1
        return cls(a, b, c)


if __name__ == '__main__':
    line1 = Line(2, -3, -6)
    line2 = Line(2, -3, -6)
    result1 = Line.get_intersection(line1, line2)
    print(f'Solution of the {line1} and the {line2} is: {result1}')
    print(f'{line1} and{line2} are coincident')
    line3 = Line(3, 2, -8)
    result2 = Line.get_intersection(line1, line3)
    print(f'Solution of the {line1} and the {line3} is: {result2}')
    print(f'{line1} and {line3} are intersect at point {result2}')
    line6 = Line(2, -3, 12)
    result3 = Line.get_intersection(line1, line6)
    print(f'Solution of the {line1} and the {line6} is: {result3}')
    print(f'{line1} and {line6} are parallel')
    point1 = Point(1, 2)
    print(point1)
    distance = Line.get_distance_from_point_to_line(point1, line1)
    print(f'The distance from {point1} to {line1} is: {distance}')
    point2 = Point(3, 4)
    result4 = Line.create_line_by_two_points(point1, point2)
    print(f'The line is created by {point1} and {point2} is: {result4}')
