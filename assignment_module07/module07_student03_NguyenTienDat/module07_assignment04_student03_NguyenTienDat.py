# Bài tập 4:
class Fraction:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator

    def result(self) -> float:
        try:
            return self.n / self.d
        except ZeroDivisionError:
            print("Denominator cannot be zero")

    def __repr__(self):
        return f'Fractione({self.n}, {self.d})'

    def __add__(self, other):
        if isinstance(other, Fraction):
            common_denominator = self.d * other.d
            new_numerator = (self.n * other.d) + (other.n * self.d)
            # Tìm gcd của tử và mẫu
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a

            n = new_numerator//gcd(new_numerator, common_denominator)
            d = common_denominator//gcd(new_numerator, common_denominator)
            return Fraction(n, d)
        else:
            raise TypeError("You can only add Fractions together")

# Mặc dù đã tạo method __add__ làm nhiệm vụ tính tổng 2 phân số nhưng nếu viết kiểu: totalValue = sum([fractionA, fractionB, fractionC]) thì vẫn sẽ báo lỗi
# hàm sum khi đó không thể gọi được method __add__, sum chỉ có thể sử dụng với các iterable.
# Nếu muốn tính sum các phân số ta cần tạo 1 method như sau:
def sum_fractions(fractions):
    total = Fraction(0, 1)
    for fraction in fractions:
        total = total + fraction
    return total

fractionA = Fraction(1, 4)
fractionB = Fraction(1, 0)
fractionC = Fraction(3, 4)

totalValue = sum_fractions([fractionA, fractionB, fractionC])
# print(totalValue)  # Kết quả là Fraction(1, 1)
print(fractionB.result())
