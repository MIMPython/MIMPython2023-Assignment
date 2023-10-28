# Bài tập 2:

class Retangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def caculate_area(self):
        return self.width * self.length
    
    def caculate_perimeter(self):
        return 2*(self.width + self.length)
    
class Square(Retangle):
    def __init__(self, side):
        super().__init__(side, side)
        
class Rhombus(Retangle):
    def __init__(self, side, hight):
        super().__init__(side, hight)
    
# obj_1 = Retangle(10,5)
# print(Retangle.caculate_area(obj_1))
# obj_2 = Square(10)
# print(Retangle.caculate_area(obj_2))
# obj_3 = Rhombus(10,6)
# print(Retangle.caculate_area(obj_3))

import math 
class Elipse:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
    
    # Ramanujan's formula
    def caculate_area(self):
        a = self.hight/2
        b = self.width/2
        return math.pi*(3*(a+b)-math.sqrt((3*a+b)*(a+3*b)))
    
    def caculate_perimeter(self):
        a = self.hight/2
        b = self.width/2
        return math.pi*a*b
    
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def caculate_area(self):
        return 2*math.pi*self.radius    
    
    def caculate_perimeter(self):
        return math.pi*math.pow(self.radius,2)
# obj_4 = Elipse(3, 5)
# print(Elipse.caculate_area(obj_4))
# obj_5 = Circle(3)
# print(Circle.caculate_area(obj_5))
        
    
    