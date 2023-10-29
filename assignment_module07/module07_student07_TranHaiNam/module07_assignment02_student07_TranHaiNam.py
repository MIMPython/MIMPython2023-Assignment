import math
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def __repr__(self):
        return Rectangle({self.length},{self.width})
    
    def Diagonal(self):
        diagonal = math.sqrt(self.width**2 + self.length**2)
        return diagonal
    
    def Perimeter(self):
        perimeter = (self.length + self.width) * 2
        return perimeter

    def Area(self):
        area = self.width * self.width
        return area

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

class Rhombus:
    def __init__(self,main_diagonal,second_diagonal):
        self.main_diagonal = main_diagonal
        self.second_diagonal = second_diagonal
    
    def getSide(self):
        side = math.sqrt( (self.main_diagonal/2)**2 + (self.second_diagonal/2)**2 )  
        return side
    
    def Perimeter(self):
        perimeter = 4 * self.getSide()
        return perimeter
    
    def Area(self):
        area = self.main_diagonal * self.second_diagonal
        return area
    
    def __repr__(self):
        return Rhombus({self.main_diagonal},{self.second_diagonal})

class Ellipse:
    def __init__(self,first_radius,second_radius):
        self.first_radius = first_radius #Bán kính trục dọc
        self.second_radius = second_radius #Bán kính trục ngang
    
    def Perimeter(self):
        perimeter = math.pi * (self.first_radius + self.second_radius)
        return perimeter
    
    def Area(self):
        area = math.pi * self.first_radius * self.second_radius
        return area
    
    def __repr__(self):
        return Ellipse({self.first_radius},{self.second_radius})
    
class Circle(Ellipse):
    def __init__(self, first_radius):
        super().__init__(first_radius,first_radius)





