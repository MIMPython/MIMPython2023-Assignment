'''Bài 3: Xây dựng các class hình học rồi vẽ hình'''

import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def draw(self, ax):
        ax.scatter(self.x, self.y)
        ax.set_title('Điểm')
        plt.gca().set_aspect('equal', adjustable = 'box')

class Circle:
    def __init__(self, center: Point, radius: float):
        self.radius = radius
        self.center = center

    def draw(self, ax):
        # circle = plt.Circle((0, 0), self.radius, color = 'k', fill=False)
        # ax.add_artist(circle)

        ax.add_artist(plt.Circle((self.center.x, self.center.y), 0.25))
        ax.set_title('Hình tròn')
        plt.gca().set_aspect('equal', adjustable = 'box')

class Line:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def draw(self, ax):
        if self.b != 0:
            x = np.linspace(- 5, 5, 1000)
            f = lambda x: (self.a * x + self.c) / (- self.b)
            y = f(x)
            ax.plot(x, f(x))
        else:
            ax.axvline(x = - self.c / self.a)#nếu b trong ax + by + c = 0 thì x = -c/a do a, b không đồng thời = 0

        ax.set_title('Đường thẳng')
        plt.gca().set_aspect('equal', adjustable = 'box')



fig, axs = plt.subplots(figsize = (15, 5), nrows = 1, ncols = 3)

center = Point(0.5, 0.5) # nếu em thay đổi tọa độ tâm thì sẽ có thể mất hình
circle = Circle(center,1)
circle.draw(axs[0])

point = Point(3, 4)
point.draw(axs[1])

line = Line(1,0,3)
line.draw(axs[2])

plt.gca().set_aspect('equal', adjustable = 'box')
plt.tight_layout()

plt.show()


