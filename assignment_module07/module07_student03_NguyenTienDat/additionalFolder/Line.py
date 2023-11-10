from . import Point
import math

class Line():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        
    def __repr__(self) -> str:
        return f"{self.a}x + {self.b}y + {self.c} = 0"
    
    
    # d:
    def intersection(self, other):
        # Hai đường thẳng giao nhau tại điểm có tọa độ (x, y):
        y = (self.c*other.a - self.a*other.c)/(other.b*self.a - other.a*self.b)
        x = -(other.b*y + other.c)/other.a
        return (x, y)
     
    def check_intersect(self, other):
        # Kiểm tra đường thẳng:
        if math.pow(self.a, 2) + math.pow(self.b, 2) != 0 and math.pow(other.a, 2) + math.pow(other.b, 2) != 0:
            # Kiểm tra sự tương giao giữa 2 đường thẳng:
            # Biểu diễn theo PT: y = mx + n
            m1 = -self.a/self.b
            m2 = -other.a/other.b
            n1 = -self.c/self.b
            n2 = -other.c/other.b
            if m1 == m2 and n1 != n2: return "parallel"
            elif m1 == m2 and n1 == n2: return "coincident"
            else: return "intersect"
        else:
            return None  
        
    def result_intersect(self, other):
        if self.check_intersect(other) == "parallel": return ()
        elif self.check_intersect(other) == "coincident": return "countless"
        else: return self.intersection(other)
    '''  Test:  
    line_1 = Line(3, 2, -1)
    line_2 = Line(1, 2, -3)
    print(line_1.result_intersect(line_2)) # (-1, 2)
    '''    
        
    # e:
    def distance(self, A):
        x = A.x
        y = A.y
        # tính khoảng cách theo công thức:
        result = abs(self.a*x + self.b*y + self.c)/math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))
        return result
    ''' Test:
    line_1 = Line(3, 2, -1)
    line_2 = Line(1, 2, -3)
    A = Point(0, 0)
    print(line_1.distance(A)) # sqr(13)/13
    '''
    
    # f:
    @classmethod
    def from_points(cls, A, B):
        # tính toán dựa trên phương trình: ax + by + c = 0
        a = B.y - A.y
        b = A.x - B.x
        c = -a*A.x - b*A.y
        return cls(a, b, c)