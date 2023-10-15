import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self, ax):
        ax.plot(self.x, self.y, marker='o', color='r')


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def plot(self, ax):
        ax.plot([self.point1.x, self.point2.x], [
                self.point1.y, self.point2.y], color='g')


class Circle:
    def __init__(self, center_point, radius):
        self.radius = radius
        self.center_point = center_point

    def plot(self, ax):
        anpha = np.linspace(0, 2*np.pi, 100)
        x = self.center_point.x + self.radius*np.cos(anpha)
        y = self.center_point.y + self.radius*np.sin(anpha)
        ax.plot(x, y, color='b')


if __name__ == '__main__':

    fig, ax = plt.subplots(2, 2)
    fig.suptitle("Point, Line and Circle", fontsize=14)
    point1 = Point(8, 9)
    point1.plot(ax[0, 0])
    point2 = Point(3, 4)
    line1 = Line(point1, point2)
    line1.plot(ax[0, 1])
    circle = Circle(Point(5, 5), radius=3)
    circle.plot(ax[1, 0])
    plt.savefig('additionalFolder/module06_assignment03_student06_NguyenThiMen_result_b3.png', format='png')
    plt.show()
