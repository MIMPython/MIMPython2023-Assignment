import numpy
import matplotlib.pyplot as plt

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def plot_point(self):
        plt.plot(self.x, self.y, "bo")
        plt.show()

    def segment(self, point):
        fig, ax = plt.subplots()
        max_x = 1 + max([abs(self.x), abs(point.x)])
        max_y = 1 + max([abs(self.y), abs(point.y)])
        
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        ax.set(
            xlim = (-max_x, max_x),
            ylim = (-max_y, max_y),
        )

        ax.plot(
            [self.x, point.x], 
            [self.y, point.y],
        )
        ax.plot(self.x, self.y, "bo")
        ax.plot(point.x, point.y, "bo")
        
        plt.show()

A = Point(1, 2)
B = Point(-3, 4)
# A.plot_point()
# A.segment(B)

class Circle():
    def __init__(self, center, radius):
        self.o = center
        self.r = radius
    
    def plot_circle(self):
        pi = numpy.pi
        step = 0.002
        param_range = numpy.arange(0, 1 + step, step)
        fig, ax = plt.subplots()
        for param in param_range:
            plt.scatter(
                numpy.cos(2*pi*param) + self.o.x, 
                numpy.sin(2*pi*param) + self.o.y, 
                marker = "o",
                color = "green",
                s = 1.5,
            )
        
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        max_x = abs(self.o.x) + self.r + 1
        max_y = abs(self.o.y) + self.r + 1
        ax.set(
            xlim = (-max_x, max_x),
            ylim = (-max_y, max_y),
            aspect = "equal",
        )
        
        plt.show()
        
circle = Circle(Point(1, 2), 2)
# circle.plot_circle()