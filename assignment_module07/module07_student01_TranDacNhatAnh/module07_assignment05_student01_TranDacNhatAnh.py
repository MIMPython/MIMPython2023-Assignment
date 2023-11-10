# Bài tập yêu cầu xây dựng class Polynomial biểu diễn đa thức (hệ số thực) và các phép toán giữa chúng

# Môt đa thức P(x) bậc n được biểu diễn bởi một list [a_0, a_1, ..., a_n] gồm các số thực là hệ số của nó
# P(x) = a_0 + a_1*x + a_2*x^2 + ... + a_n*x^n

class Polynomial:
    def __init__(self, coefficients: list[float]) -> None:
        self.deg = len(coefficients) - 1
        self.coef = coefficients
    
    def standardize(self):
        while self.coef[-1] == 0:
            self.coef.pop(-1)
        self.deg = len(self.coef)
        return self

    def getValue(self, x: float) -> float:
        value = 0
        for i in range(self.deg+1):
            value += self.coef[i] * (x**i)
        return value

    def add(self, polyB):
        coefList = []
        if self.deg > polyB.deg:
            for i in range(self.deg+1):
                if i<=polyB.deg:
                    coefList.append(self.coef[i] + polyB.coef[i])
                else:
                    coefList.append(self.coef[i])
        else:
            for i in range(polyB.deg+1):
                if i<=self.deg:
                    coefList.append(self.coef[i] + polyB.coef[i])
                else:
                    coefList.append(polyB.coef[i])
        return Polynomial(coefficients=coefList)
    
    def getInverse(self):
        coefList = [-coefficient for coefficient in self.coef]
        return Polynomial(coefficients=coefList)
    # Với hàm lấy đa thức âm này, ta có thể tìm hiệu P(x)-Q(x) mà không cần định nghĩa phép trừ đa thức, chỉ cần add(P, Q.getInverse())

    def multiply(self, polyB):
        coefList = []
        for i in range(self.deg + polyB.deg + 1):
            coefficient = 0
            for j in range(0, i+1):
                if j<=self.deg:
                    if i-j <= polyB.deg:
                        coefficient += self.coef[j]*polyB.coef[i-j]
            coefList.append(coefficient)
        return Polynomial(coefficients=coefList)

    # def divide(self, polyB):
    #     self = self.standardize()
    #     polyB = polyB.standardize()
    #     if self.deg < polyB.deg:
    #         return self
    #     else:
    #         remaining = self
    #         coefList = [0 for _ in range(self.deg - polyB.deg+1)]
    #         while remaining.deg >= polyB.deg:
    #             c = remaining.coef[-1] / polyB.coef[-1]
    #             coefList[remaining.deg - polyB.deg] = c
    #             remaining = remaining.add(Polynomial([-c]).multiply(polyB))
    #     return Polynomial(coefficients=coefList), remaining
    
    def __repr__(self) -> str:
        polyString = f'{self.coef[0]}'
        for i in range(self.deg):
            a_i = self.coef[i+1]
            if a_i > 1:
                polyString += f' + {a_i}x^{i+1}'
            elif a_i < -1:
                polyString += f' - {-a_i}x^{i+1}'
            elif a_i == -1:
                polyString += f' - x^{i+1}'
            elif a_i == 1:
                polyString += f' + x^{i+1}'
        return polyString

if __name__ == '__main__':
    P = Polynomial([1, 0, 1]) # 1 + x^2
    Q = Polynomial([1, 0, -1, 0, 1])
    print(Q) # 1 - x^2 + x^4
    print(P.getValue(2)) # 5
    print(P.getInverse()) # -1 - x^2
    print(P.add(Q)) # 2 + x^4
    print(P.multiply(Q)) # 1 + x^6
    print(P.multiply(Polynomial([0]))) # 0