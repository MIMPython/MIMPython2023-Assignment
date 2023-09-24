# Bài tập 6: (class Circle)
import sympy as sp
import math 
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

        # Biểu diễn đường tròn bằng biến và phương trình
        self.x_var, self.y_var = sp.symbols('x y')
        self.circle_equation = sp.Eq((self.x_var - self.x)**2 + (self.y_var - self.y)**2, self.r**2)
    # Hàm tính diện tích của đường tròn
    def get_area(self):
        return sp.pi * self.r**2
    # Hàm tính chu vi của đường tròn
    def get_circumference(self):
        return 2 * sp.pi * self.r
    # Hàm kiểm tra điểm nằm trong đường tròn
    def is_point_inside(self, x, y):
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        if distance <= self.r:
            return True
        else:
            return False

    def __str__(self):
        return f"Đường tròn tại tâm ({self.x}, {self.y}) và bán kính {self.r}"

# Sử dụng lớp Circle
circle1 = Circle(0, 0, 5)
print(circle1)
print("Diện tích:", circle1.get_area())
print("Chu vi:", circle1.get_circumference())
print("Điểm (3, 4) có nằm trong đường tròn không?", circle1.is_point_inside(3, 4))