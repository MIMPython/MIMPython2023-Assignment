import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, other , metric):
        if metric == "L1":
            return abs(self.x - other.x) + abs(self.y + other.y)
        if metric == "L2":
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
    def reflec(self):
        return (-self.x, -self.y)
    
    def __repr__(self):
        return f'Point("{self.x}","{self.y}")'
    
if __name__ == '__main__':
    pointa = Point(1,2)
    pointb = Point(12,4)
    print(Point.reflec(pointa)) # (-1,-2
    print(Point.distance(pointa,pointb,"L2")) # xấp xỉ 11,18
