import math

class Fraction:
    def  __init__(self,numerator,denominator):
        if denominator == 0:
            raise ZeroDivisionError(f'denominator cannot be Zero')
        else:
            if denominator < 0:
                numerator *= -1
                denominator *= -1
            gcd = math.gcd(numerator,denominator)
            self.numerator = numerator//gcd
            self.denominator = denominator//gcd

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'
    @classmethod
    def initializeFromFloat(cls,num_float):
        num = str(num_float).split(".")
        if int(num[0]) == 0:
            numerator = int(num[1])
            denominator = 10**len(num[1])
            return Fraction(numerator,denominator)
        else:
            numerator = int(num[0]+num[1])
            denominator = 10**len(num[1])
            return Fraction(numerator,denominator)
    
    def __add__(self,other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator + other.numerator
            return Fraction(new_numerator,self.denominator)
        else:
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator,new_denominator)
    

    def __sub__(self,other):
        if self.denominator == other.denominator:
            new_numerator = self.numerator - other.numerator
            return Fraction(new_numerator,self.denominator)
        else:
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator,new_denominator)
    
    def __mul__(self,other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator,new_denominator)
    
    def __trdiv__(self,other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator,new_denominator)
    


    def __gt__(self, other):
        return self.numerator/self.denominator > other.numerator/other.denominator
    
    def __ge__(self, other):
        return self.numerator/self.denominator >= other.numerator/other.denominator
    
    def __lt__(self, other):
        return self.numerator/self.denominator < other.numerator/other.denominator
    
    def __le__(self, other):
        return self.numerator/self.denominator <= other.numerator/other.denominator
    
    def __eq__(self, other):
        return self.numerator/self.denominator == other.numerator/other.denominator
    
    def __ne__(self, other):
        return self.numerator/self.denominator != other.numerator/other.denominator
    
    

#totalValue = sum([fractionA, fractionB, fractionC]): không thể sử dụng cách viết này
# Vì hàm sum trả về giá trị bắt đầu ( thường là 0) tới các iterable của số, để sử dụng được cách viết này ta cần định nghĩa giá trị 
# bắt đầu là (0,1)
