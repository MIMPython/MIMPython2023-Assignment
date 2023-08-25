import math


class QuadraticEquation:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def solve(self) -> tuple:
        delta = self.b ** 2 - 4.0 * self.a * self.c
        if delta < 0:
            return ()
        elif delta == 0:
            root = - self.b / (2.0 * self.a)
            return (root, )
        else:
            firstRoot = (- self.b + math.sqrt(delta)) / (2.0 * self.a)
            secondRoot = (- self.b - math.sqrt(delta)) / (2.0 * self.a)
            return (firstRoot, secondRoot)


if __name__ == "__main__":
    coefficients = [(1, 1, -2), (1, 2, 1), (1, 0, 1)]
    for coefficient in coefficients:
        equation = QuadraticEquation(
            a=coefficient[0], b=coefficient[1], c=coefficient[2])
        print(equation.solve())
