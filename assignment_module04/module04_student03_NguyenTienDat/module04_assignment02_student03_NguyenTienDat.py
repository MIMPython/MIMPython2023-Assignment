# Bài tập 2

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def distance(self, other, metric):
        if metric == 'L1':
            return abs(self.x - other.x) + abs(self.y - other.y)
        if metric == 'L2':
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
 
    # cách 2, ý 4:
    def symmetry_point_2(self):
        result = (-self.x, -self.y)
        return result
    
    
    # cách 3, ý 4:
    def symmetry_point_3(self):
        result = self.__class__(-self.x, -self.y)
        return result
    
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
        
# cách 1, ý 4:        
# def symmetry_point_1(point):
#     return Point(-point.x, -point.y)
# pointA = Point(3,4)
# pointB = symmetry_point_1(pointA)
# print(pointB) # (-3, -4)


if __name__ == '__main__':       
    pointA = Point(3, 4)
    pointB = Point(7, 7)
    disL2 = pointA.distance(pointB, 'L2') # output: 5
    disL1 = pointA.distance(pointB, 'L1') # output: 7
    symmetry_point = pointA.symmetry_point_2() # output: (-3, -4)
    