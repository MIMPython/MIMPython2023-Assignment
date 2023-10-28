from scipy.integrate import quad
import numpy


class Rectangle:
    """
    A rectangle object is determined by 4 parameters:
        x : Horizontal coordinate of center of the rectangle
        y : Vertical coordinate of center of the rectangle
        w : Width of the rectangle
        h : Height of the rectangle
    """

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def getArea(self) -> int:
        return self.w * self.h

    def getPerimeter(self) -> int:
        return 2 * (self.w + self.h)

    def getDiagonal(self) -> float:
        return numpy.sqrt(self.w ** 2 + self.h ** 2)


class Square(Rectangle):
    """
    A square object is determined by 3 parameters:
        x : Horizontal coordinate of center of the square
        y : Vertical coordinate of center of the square
        e : Length of an edge of the square
    """

    def __init__(self, x: int, y: int, e: int) -> None:
        super().__init__(x, y, e, e)


class Rhombus:
    """
    A rhombus object is determined by 4 parameters:
        x : Horizontal coordinate of center of the rhombus
        y : Vertical coordinate of center of the rhombus
        w : Length of the horizontal diagonal of the rhombus
        h : Length of the vertical diagonal of the rhombus
    """

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def getArea(self) -> int:
        return self.w * self.h / 2

    def getPerimeter(self) -> float:
        egde = numpy.sqrt((self.w / 2) ** 2 + (self.h / 2) ** 2)
        return 4 * egde


class Ellipse(Rhombus):
    """
    An ellipse object is determined by 4 parameters:
        x : Horizontal coordinate of center of the ellipse
        y : Vertical coordinate of center of the ellipse
        w : Length of the major axis of the rhombus
        h : Length of the minor axis of the rhombus
    """

    def __init__(self, x: int, y: int, w: int, h: int) -> None:
        super(self).__init__(x, y, w, h)

    def getPerimeter(self):
        def f(x):
            term = 1 - (e ** 2) * (numpy.sin(x) ** 2)
            return numpy.sqrt(term)
        a = self.w / 2
        b = self.h / 2
        e = numpy.sqrt(a ** 2 - b ** 2) / a
        term = quad(lambda x: f(x), 0, numpy.pi / 2)
        return 4 * a * term

    def getArea(self) -> float:
        return numpy.pi * self.w / 2 * self.h / 2



    
