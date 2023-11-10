import numpy
import sympy
import matplotlib.pyplot as plot


class Polynomial:
    """
    Polynomial P(x) = a0 + a1 * x + a2 * x^2 + a3 * x^3 + ... + an * x^n
    Coefficients of object will be saved as [a0, a1, a2,..., an]
    You can initialize Polynomial object by using 2 ways:
        - Initialize by list of coefficients of the polynomial
        - Initialize by string of polynomial 
    """

    def __init__(self, *args) -> None:
        self.p = []
        coeffs = list(args)
        if len(args) > 0:
            for coeff in coeffs:
                self.p.append(coeff)
            self.p = self.removeZeros(self.p)

    def initFromString(self, string: str) -> None:
        string = string.replace(" ", "")
        string = string.replace("^", "**")
        x = sympy.Symbol('x')
        poly = sympy.polys.polytools.poly_from_expr(string)[0]
        p = []
        for coef in reversed(list(poly.coeffs())):
            p.append(coef)
        p = self.removeZeros(p)
        return Polynomial(*p)

    def deg(self) -> int:
        return len(self.p) - 1

    def removeZeros(self, array):
        while array[-1] == 0:
            array = array[0: len(array) - 1]
        return array

    def __add__(self, polynomial):
        firstCoeffs = self.p
        secondCoeffs = polynomial.p
        if self.deg() < polynomial.deg():
            for i in range(self.deg(), polynomial.deg()):
                firstCoeffs.append(0)
        elif self.deg() > polynomial.deg():
            for i in range(polynomial.deg(), self.deg()):
                secondCoeffs.append(0)
        newCoeffs = []
        for i in range(len(firstCoeffs)):
            newCoeffs.append(firstCoeffs[i] + secondCoeffs[i])
        newCoeffs = self.removeZeros(newCoeffs)
        return Polynomial(*newCoeffs)

    def __sub__(self, polynomial):
        firstCoeffs = self.p
        secondCoeffs = polynomial.p
        if self.deg() < polynomial.deg():
            for i in range(self.deg(), polynomial.deg()):
                firstCoeffs.append(0)
        elif self.deg() > polynomial.deg():
            for i in range(polynomial.deg(), self.deg()):
                secondCoeffs.append(0)
        newCoeffs = []
        for i in range(len(firstCoeffs)):
            newCoeffs.append(firstCoeffs[i] - secondCoeffs[i])
        newCoeffs = self.removeZeros(newCoeffs)
        return Polynomial(*newCoeffs)

    def __neg__(self):
        array = []
        for p in self.p:
            array.append(-p)
        return Polynomial(*array)

    def __mul__(self, polynomial):
        newCoeffs = numpy.zeros(
            (polynomial.deg() + 1, self.deg() + polynomial.deg() + 1), dtype=numpy.int64)
        for i in range(polynomial.deg() + 1):
            for j in range(i, i + self.deg() + 1):
                newCoeffs[i, j] = self.p[j - i] * polynomial.p[i]
        newCoeffs = numpy.sum(newCoeffs, axis=0)
        return Polynomial(*newCoeffs)

    def __repr__(self) -> str:
        expression = ""
        for i in range(len(self.p)):
            if self.p[i] > 0:
                expression += "+" + str(self.p[i]) + "*x^" + str(i)
            if self.p[i] < 0:
                expression += str(self.p[i]) + "*x^" + str(i)
        expression = expression.replace("*x^0", "")
        expression = expression.replace("*x^1", "*x")
        expression = expression[1::] if expression[0] == "+" else expression
        return expression

    def solve(self) -> list:
        roots = numpy.roots(self.p)
        return list(roots)

    def evaluate(self, x: int) -> float:
        coeffs = list(reversed(self.p))
        value = numpy.polyval(coeffs, x)
        return value

    def visualize(self):
        x_points = numpy.linspace(start=0, stop=100, num=10000)
        y_points = numpy.apply_along_axis(
            func1d=self.evaluate, axis=0, arr=x_points)
        plot.plot(x_points, y_points)
        plot.show()


if __name__ == "__main__":
    A = Polynomial(1, 2)
    B = Polynomial().initFromString("1-x^2")
    print("A: ", A)
    print("B: ", B)
    print("-A: ", -A)
    print("A + B: ", A + B)
    print("A - B: ", A - B)
    print("A * B: ", A * B)
    print("Root of A: ", A.solve())
    print(A.evaluate(1))
    B.visualize()
