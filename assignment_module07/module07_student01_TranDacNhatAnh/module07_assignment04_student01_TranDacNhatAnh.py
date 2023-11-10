# Bài tập yêu cầu xây dựng class Fraction -> Biểu diễn các tỉ số
from additionalFolder.NumberTheory import gcd

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if denominator == 0:
            raise ZeroDivisionError(f'fraction {self} has 0 as denominator')
        self.n = numerator
        self.d = denominator
        # Fraction(f) = f.n / f.d

    def simplify(self):
        d = gcd(self.n, self.d)
        self.n, self.d = self.n//d, self.d//d
        return self

    def getValue(self) -> float:
        return self.n/self.d

    def __add__(self, fractionB):
        numerator = self.n*fractionB.d + self.d*fractionB.n
        denominator = self.d*fractionB.d
        return Fraction(numerator=numerator, denominator=denominator).simplify()
    
    def multiply(self, fractionB):
        return Fraction(self.n*fractionB.n, self.d*fractionB.d).simplify()

    def leq(self, fractionB) -> bool:
        if self.getValue() - fractionB.getValue() > 0:
            return False
        return True

    def __repr__(self) -> str:
        return f'{self.n}/{self.d}'

fracList = [Fraction(1, 2), Fraction(1, 4), Fraction(2, 8)]
print(fracList[0]) # 1/2
print(fracList[2].simplify()) # 1/4
print(fracList[0].getValue()) # 0.5
print(fracList[0].leq(fracList[1])) # False
total = Fraction(0, 1)
for f in fracList:
    total = total.__add__(f)
print(total, total.getValue()) # 1/1, 1.0

# Sau khi cài đặt __add__ cho class Fraction, việc tính tổng một list các Fraction bằng sum(fracList) vẫn không thể thực hiện 
# vì __add__ không tương đương với phép cộng ('+') được mặc định sử dụng với hàm sum().