from matplotlib import pyplot as plt
import numpy as np


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x},{self.y})'
    
    def plot(self):
        plt.plot(self.x, self.y,'go', color = "r" )
        plt.show()

    
class Line:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def isValid(self):
        if self.a != 0 and self.b != 0:
            return True
        return False
    
    def __repr__(self):
        return f'{self.a}x + {self.b}y + {self.c}'
    
    @classmethod
    def creat_line(cls, PointA, PointB):
        a = PointB.y - PointA.y
        b = PointA.x - PointB.x
        c = -a*PointA.x - b*PointA.y
        return Line(a,b,c)
    
    def draw_line(self):
        list_x = []
        list_y = []
        if self.isValid():  
            for i in range(1,20,2):
                x = i
                list_x.append(i)
                y = (-self.c - self.a * x ) / self.b
                list_y.append(y)
            plt.plot(list_x, list_y, linestyle = ':', label = f'{self}')
            plt.legend()
            plt.grid()
            plt.show()
            
            
        else:
            return f'Unvalid Line'

class Circle:
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = radius

    def isValid(self):
        if self.x**2 + self.y**2 - self.radius > 0:
            return True
        else:
            return False 
    
    def __repr__(self):
        return f'(x-{self.x})**2 + (y-{self.y})**2 = {self.radius}**2'
    
    def draw_cricle(self):
        if  Circle.isValid(self):
            x = np.linspace(-20, 20,1000000)
            y1 = np.sqrt(self.radius**2 - (x - self.x)**2) + self.y
            y2 = -np.sqrt(self.radius**2 - (x - self.x)**2) + self.y
            plt.plot(x,y1, color = 'k')
            plt.plot(x,y2, color = 'k')
            plt.grid()
            plt.title(f"{self}")
            plt.show()
        else:
            return f' Unvalid '

# cir = Circle(2,3,5)
# print(Circle.draw_cricle(cir))


