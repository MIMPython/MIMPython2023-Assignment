from module04_assignment02_student06_NguyenThiMen import Point
import math


def get_triangle_area(A, B, C):
    AB = A.calculate_distances(B)
    AC = A.calculate_distances(C)
    BC = B.calculate_distances(C)
    p = (AB + BC + AC)/2
    return math.sqrt(p*(p-AB)*(p-AC)*(p-BC))


if __name__ == '__main__':
    A = Point(2, 2)
    B = Point(5, 1)
    C = Point(3, 6)
    print(f'The area of the triangle formed by {A}, {B}, {C} is {get_triangle_area(A,B,C)}')
