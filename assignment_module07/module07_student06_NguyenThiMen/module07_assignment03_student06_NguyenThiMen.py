from additionalFolder.point import Point
from additionalFolder.circle import Circle
from additionalFolder.line import Line

if __name__ == '__main__':
    point = Point(3, 4)
    line = Line(1, 2, 0)
    print(line)
    print(line.is_on_line(point))
    point = Point(4, 4)
    circle = Circle(point, 4)
    print(circle)
