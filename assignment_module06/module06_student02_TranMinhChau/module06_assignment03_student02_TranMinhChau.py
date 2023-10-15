# Bài tập 3:
import matplotlib.pyplot as plt
# Biểu diễn 1 điểm trên mặt phẳng
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, ax, color='black'):
        ax.plot(self.x, self.y, marker='o', markersize=5, color=color)
        ax.text(self.x, self.y, f'({self.x}, {self.y})', fontsize=8, verticalalignment='bottom')
# Biểu diễn một đoạn thẳng trên mặt phẳng
class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def plot(self, ax, color='black'):
        ax.plot([self.start_point.x, self.end_point.x], [self.start_point.y, self.end_point.y], color=color)
# Biểu diễn một đường tròn trên mặt phẳng
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def plot(self, ax, color='black'):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color=color, fill=False)
        ax.add_patch(circle)
# Sử dụng chương trình
fig, ax = plt.subplots()
# Tạo điểm và vẽ
point = Point(1, 2)
point.plot(ax, color='red')
# Tạo đoạn thẳng và vẽ
line = Line(Point(0, 0), Point(3, 4))
line.plot(ax, color='blue')
# Tạo hình tròn và vẽ
circle = Circle(Point(5, 5), 2)
circle.plot(ax, color='green')
# Điều chỉnh trục ox và oy bằng nhau
ax.set_aspect('equal')
# Lưu hình ảnh và hiển thị
plt.show()