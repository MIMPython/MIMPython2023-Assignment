from .point import Point

import math


class Circle:
    def __init__(self, center: Point, radius: int) -> None:
        self.center = center
        self.radius = radius

    def __repr__(self) -> str:
        return f'Circle: center={self.center},radius = {self.radius} '

    @property
    def area(self) -> float:
        return math.pi*(self.radius**2)

    @property
    def perimeter(self) -> float:
        return 2*math.pi*self.radius


if __name__ == '__main__':
    point = Point(1, 1)
    cir = Circle(point, 4)
    print(cir)
    print(cir.area)
    print(cir.perimeter)
