'''Bài 4: Tính diện tích tam giác bằng ít nhất 3 cách'''

from module04_assignment02_student08_DoMinhQuang import Point
from module04_assignment03_student08_DoMinhQuang import Line
import math

#Cách 1 Dùng tích có hướng
def evaluate_surface1(pointA: Point, pointB: Point, pointC: Point) -> float :
    vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
    vector_AC = Point(pointC.x - pointA.x, pointC.y - pointA.y)
    return 0.5 * math.fabs(vector_AB.x * vector_AC.y - vector_AB.y * vector_AC.x)



def distance(pointA: Point, pointB: Point) -> float :
    vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
    return math.sqrt(vector_AB.x ** 2 + vector_AB.y ** 2)

#Cách 2 dùng công thức Heron
def evaluate_surface2(pointA: Point, pointB: Point, pointC: Point) -> float :
    a = distance(pointA, pointB)
    b = distance(pointB, pointC)
    c = distance(pointA, pointC)
    p = 0.5 * (a + b + c)
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

#Cách 3 dùng công thức 1/2 * cạnh đáy * chiều cao
def evaluate_surface3(pointA: Point, pointB: Point, pointC: Point) -> float :
    vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
    AB = math.sqrt(vector_AB.x ** 2 + vector_AB.y ** 2)
    line = Line.line_general_equation(pointA, pointB)
    distance = line.find_distance(pointC)
    return 0.5 * AB * distance
#Cách 4 dùng công thức 1 / 2 * sqrt ( (AB*AC) ** 2 - ( vector_AB . vector_AC) ** 2 )
def evaluete_surface4(pointA: Point, pointB: Point, pointC: Point) -> float :
    AB = distance(pointA, pointB)
    AC = distance(pointA, pointC)
    vector_AB = Point(pointB.x - pointA.x, pointB.y - pointA.y)
    vector_AC = Point(pointC.x - pointA.x, pointC.y - pointA.y)
    return 0.5 * math.sqrt( (AB ** 2) * (AC ** 2) - (vector_AB.x * vector_AC.x + vector_AB.y * vector_AC.y) ** 2)

A = Point(1, 3)
B = Point(2,10)
C = Point(2,5)
print(round((evaluate_surface2(A, B, C)), 1))
print(evaluate_surface1(A, B, C))
print(evaluate_surface3(A, B, C))
print(round((evaluete_surface4(A, B, C)), 1))

#Chạy code:  python module04_assignment04_student08_DoMinhQuang.py






