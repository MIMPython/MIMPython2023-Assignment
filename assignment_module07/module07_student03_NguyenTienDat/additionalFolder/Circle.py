import math 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def caculate_area(self):
        return math.pi*math.pow(self.radius,2)    
    
    def caculate_perimeter(self):
        return 2*math.pi*self.radius    