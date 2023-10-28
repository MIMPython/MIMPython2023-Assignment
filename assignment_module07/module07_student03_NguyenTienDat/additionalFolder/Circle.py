import math 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def caculate_area(self):
        return 2*math.pi*self.radius    
    
    def caculate_perimeter(self):
        return math.pi*math.pow(self.radius,2)