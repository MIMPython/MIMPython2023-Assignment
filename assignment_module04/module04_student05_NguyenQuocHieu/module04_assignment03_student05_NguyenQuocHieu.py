class Line:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.check()

    def check(self):
        if self.a == 0 and self.b == 0:
            print("Input error")
            exit(1)

    def intersect(self, other) -> None:
        if self.a != 0 and other.b != 0:
            if self.a / other.a == self.b / other.b == self.c / other.c:
                print("Infinitive")
            elif self.a / other.a == self.b / other.b:
                print("Two lines are parallel. No intersection")
            else:
                m = other.a * self.c - other.c * self.a
                n = other.a * self.b - self.a * other.b
                y = float(-n / m)
                if self.a == 0:
                    x = - (other.c + other.b * y) / other.a
                else:
                    x = - (self.c + self.b * y) / self.a
                print("Intersection point at x= ", x, ", y= ", y)
        elif self.a == 0:
            y = - self.c / self.b
            x = - (other.c + other.b * y) / other.a
            print("Intersection point at x= ", x, ", y= ", y)
        else:
            x = - (other.c / other.a)
            y = - (self.c + self.a * x) / self.b
            print("Intersection point at x= ", x, ", y= ", y)


if __name__ == "__main__":
    """
    1, Biểu thức y = ax + b không thể biểu diễn được cho những đường thẳng có y = 0, ví dụ đường thẳng x = 1
    2, ax + by + c = 0 là phương trình tổng quát của đường thẳng trong mặt phẳng Oxy với a, b không đồng thời bằng 0
    """
    line1 = Line(1, 1, -2)  # x + y - 2 = 0
    line2 = Line(1, 0, 1)  # x     + 1 = 0
    line1.intersect(line2)
