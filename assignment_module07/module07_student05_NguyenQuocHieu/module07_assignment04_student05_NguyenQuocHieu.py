class Fraction:
    """
    A fraction is determined by 2 parameters:
        a : Numerator of the fraction
        b : Denominator of the fraction
    or 1 parameter:
        x : Value of the fraction
    """

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            self.normalize()
        elif len(args) == 1:
            y = args[0]
            m = 0
            while float(int(y)) != y:
                y = y * 10.0
                m += 1
            self.a = int(y)
            self.b = 10 ** m
            self.normalize()
        elif len(args) == 0:
            self.a = 0
            self.b = 1
        else:
            raise TypeError(
                "TypeError: Fraction.__init__() takes no more than 2 positional arguments")

    def normalize(self):
        def gcd(a, b) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)
        c = gcd(self.a, self.b)
        self.a = int(self.a / c)
        self.b = int(self.b / c)

    def __repr__(self) -> str:
        return str(self.a) + "/" + str(self.b)

    def compare(self, fraction):
        value1 = self.a * fraction.b
        value2 = self.b * fraction.a
        if value1 < value2:
            print("Less than " + str(fraction))
        else:
            print("More than " + str(fraction))

    def __lt__(self, fraction) -> bool:
        return True if self.a * fraction.b < self.b * fraction.a else False

    def __eq__(self, fraction) -> bool:
        return True if self.a * fraction.b == self.b * fraction.a else False

    def __le__(self, fraction) -> bool:
        return True if self.a * fraction.b <= self.b * fraction.a else False

    def __ne__(self, fraction) -> bool:
        return True if self.a * fraction.b != self.b * fraction.a else False

    def __gt__(self, fraction) -> bool:
        return True if self.a * fraction.b > self.b * fraction.a else False

    def __ge__(self, fraction) -> bool:
        return True if self.a * fraction.b >= self.b * fraction.a else False

    def __add__(self, fraction) -> None:
        numerator = self.a * fraction.b + self.b * fraction.a
        denominator = self.b * fraction.b
        return Fraction(numerator, denominator)


if __name__ == "__main__":
    fraction = Fraction(1, 5)
    fraction2 = Fraction(4 / 5)
    print(fraction <= fraction2)
    print(fraction > fraction2)
    print(fraction != fraction2)
    print(fraction + fraction2)
