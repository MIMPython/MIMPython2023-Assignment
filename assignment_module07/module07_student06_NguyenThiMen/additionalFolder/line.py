from .point import Point


class Line:
    def __init__(self, a: int, b: int, c: int) -> None:
        assert a != 0 or b != 0, 'It\'s not possible for both a and b to be zero.'
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self) -> str:
        return f'Line: {self.a}x + {self.b}y + {self.c} = 0'

    def is_on_line(self, point: Point) -> bool:
        return (self.a*point.x + self.b*point.y + self.c) == 0


if __name__ == '__main__':
    line = Line(1, -1, 0)
    point = Point(0, 0)
    print(line)
    print(line.is_on_line(point))
