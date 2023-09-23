from module04_assignment02_student07_TranHaiNam import Point
from module04_assignment03_student07_TranHaiNam import Line
import math

def AreaTriangle(pointA, pointB, pointC):
    if Point.distance(pointA,pointB,"L2") + Point.distance(pointA,pointC,"L2") < Point.distance(pointB,pointC,"L2"):
        return f'Area of Triangle is not exist'
    else:
        line0 = Line.creat_line(pointC, pointB)
        BC = Point.distance(pointB,pointC,"L2")
        AB = Point.distance(pointA,pointB,"L2")
        AC = Point.distance(pointA,pointC,"L2")
        p = ( AB + BC + AC ) / 2
        Area = math.sqrt(p*(p-AB)*(p-AC)*(p-BC))
        return Area
    

 
if __name__ == '__main__':
    pointA = Point(1,-5)
    pointB = Point(2,1)
    pointC = Point(13,-8)
    print(AreaTriangle(pointA, pointB, pointC)) # diện tích xấp xỉ 37,5
    
          


