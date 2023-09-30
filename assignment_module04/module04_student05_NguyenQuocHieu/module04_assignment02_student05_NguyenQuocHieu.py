import numpy


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, other, metric: str) -> float:
        if metric == "L1":
            return numpy.abs(self.x - other.x) + numpy.abs(self.y - other.y)
        else:
            return numpy.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def symetric(self):
        return Point(-self.x, -self.y)

    def __repr__(self) -> str:
        return "(x=" + str(self.x) + ", y=" + str(self.y) + ")"


if __name__ == "__main__":
    """
    Tạo class Point thực hiện các yêu cầu: tìm điểm đối xứng và tính khoảng cách tới một đối tượng Point khác
    """
    pointA = Point(4, 2)
    pointB = Point(0, 0)
    print("A: ", pointA)
    print("B: ", pointB)
    print("Symetric of A: ", pointA.symetric())
    print("AB= ", pointA.distance(pointB, "L2"))
