class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def getX(self) -> int:
        return self.x

    def getY(self) -> int:
        return self.y

    def equals(self, other) -> bool:
        return self.x == other.getX() and self.y == other.getY()


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.check()

    def check(self) -> None:
        if self.a.equals(self.b) or self.a.equals(self.c) or self.b.equals(self.c):
            print("Input error")
            exit(1)

    def getArea(self) -> float:
        value = (self.b.getX() - self.a.getX()) * (self.c.getY() - self.a.getY()) - \
            (self.c.getX() - self.a.getX()) * (self.b.getY() - self.a.getY())
        return abs(value) * 0.5


if __name__ == "__main__":
    """
    Tóm tắt đề bài: tạo class Triange thực hiện tính diện tích tam giác với tọa độ 3 đỉnh cho trước
    """
    triangle = Triangle(Point(0, 0), Point(0, 1), Point(2, 0))
    print(triangle.getArea())
