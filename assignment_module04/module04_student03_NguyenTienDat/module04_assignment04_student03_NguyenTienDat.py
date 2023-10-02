# Bài tập 4:

from module04_assignment02_student03_NguyenTienDat import Point
from module04_assignment03_student03_NguyenTienDat import Line
import math

class triangle_area():     
    def triangle_area(A, B, C):
        x_A = A.x
        y_A = A.y
        X_B = B.x
        y_B = B.y
        x_c = C.x
        y_c = C.y
        return 0.5*abs((X_B - x_A)*(y_c - y_A) - (x_c - x_A)*(y_B - y_A))


if __name__ == '__main__':
    A = Point(3, 3)
    B = Point(1, 1)
    C = Point(2, 3)
    result = triangle_area.triangle_area(A, B, C)
    print(result) # output: 1.0