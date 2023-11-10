# Bài tập yêu cầu xây dựng các class Hình học: Rectangle, Square, Rhombus, Circle, Elipse

from additionalFolder.Geometry import Vector, Point

# class Rectangle, ở đây mặc định các cạnh của hình chữ nhật song song với trục Ox, Oy của mặt phẳng để tránh những tình huống phức tạp
class Rectangle:
    def __init__(self, topleft: Point, botright: Point):
        if topleft.x <= botright.x and topleft.y >= botright.y:
            self.tl = topleft
            self.br = botright
        else: 
            raise ValueError('{topleft} is not the Top Left of the rectangle')
        
    def area(self):
        return (self.br.x - self.tl.x)*(self.tl.y - self.br.y)
    
    def center(self):
        return Point.barycenter(self.tl, 1, self.br, 1)[0]

    def __repr__(self):
        return f'Rectangle({self.tl}, {self.br})'

A = Rectangle(topleft=Point(0, 2), botright=Point(4, 0))
print(A.center())