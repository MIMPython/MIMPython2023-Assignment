def gcd(n: int, d: int) -> int:
    n = abs(n)
    d = abs(d)
    while d:
        n, d = d, n % d
    return n


class Fraction:

    def __init__(self, numerator: int, denominator: int) -> None:
        '''
        Initialize a Fraction
        Parameters:
            numerator: int, denominator: int
        Raises:
            error occurs if some conditions aren't met.
        '''
        if isinstance(numerator, int) == False or isinstance(denominator, int) == False:
            raise TypeError(
                'The numerator and denominator must be an integer.')
        self.numerator = int(numerator/gcd(numerator, denominator))
        self.denominator = int(
            denominator/gcd(numerator, denominator))
        if self.denominator < 0:
            self.denominator = abs(self.denominator)
            self.numerator = -1*self.numerator
        elif self.denominator == 0:
            raise ZeroDivisionError(
                'The denominator of a Fraction cannot be a zero.')
        if self.numerator == 0:
            self.numerator = 0
            self.denominator = 1

    def __repr__(self) -> str:
        return f'Fraction({self.numerator}/{self.denominator})'

    def __eq__(self, fraction: 'Fraction') -> bool:
        return self.numerator == fraction.numerator and self.denominator == fraction.denominator

    def __ne__(self, fraction: 'Fraction') -> bool:
        return not (self == fraction)

    def __lt__(self, fraction: 'Fraction') -> bool:
        return self.numerator*fraction.denominator < self.denominator*fraction.numerator

    def __le__(self, fraction: 'Fraction') -> bool:
        return self.numerator*fraction.denominator <= self.denominator*fraction.numerator

    def __gt__(self, fraction: 'Fraction') -> bool:
        return self.numerator*fraction.denominator > self.denominator*fraction.numerator

    def __ge__(self, fraction: 'Fraction') -> bool:
        return self.numerator*fraction.denominator >= self.denominator*fraction.numerator

    def __add__(self, fraction: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator*fraction.denominator + \
            fraction.numerator*self.denominator
        new_denominator = self.denominator*fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, fraction: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator*fraction.denominator - \
            fraction.numerator*self.denominator
        new_denominator = self.denominator*fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, fraction: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator*fraction.numerator
        new_denominator = self.denominator*fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, fraction: 'Fraction') -> 'Fraction':
        new_numerator = self.numerator*fraction.denominator
        new_denominator = self.denominator*fraction.numerator
        return Fraction(new_numerator, new_denominator)


if __name__ == '__main__':
    # fraction = Fraction(-2,0)
    # print(fraction)
    # fraction1 = Fraction(2.4,6)
    # print(fraction1)
    # fraction2 = Fraction(0,4)
    # print(fraction2)
    fraction3 = Fraction(1, 4)
    fraction4 = Fraction(2, 4)
    fraction5 = Fraction(7, 8)
    print(fraction3 == fraction4)
    print(fraction3 != fraction4)
    print(fraction3 < fraction4)
    print(fraction3 <= fraction4)
    print(fraction3 > fraction4)
    print(fraction3 >= fraction4)
    print(fraction3 + fraction4)
    print(fraction3 - fraction4)
    print(fraction3 * fraction4)
    print(fraction3 / fraction4)
    # totalValue = sum([fraction3, fraction4])
    # print(totalValue) -> không dùng hàm sum để cộng Fraction được.
