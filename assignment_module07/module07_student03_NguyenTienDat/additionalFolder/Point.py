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

    def symmetry_point_2(self):
        result = (-self.x, -self.y)
        return result
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'