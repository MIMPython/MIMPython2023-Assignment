from math import sqrt
import numpy as np

def solveQuadratic(a,b,c):
    #TH1: a==0, bài toán trở thành giải phương trình bậc nhất.
    if a==0:
        if b==0:
            raise Exception("No variable")
        else:
            return (-c/b, )
    #TH2: a!=0, phương trình có 2 nghiệm phân biệt nếu delta>0, có nghiệm duy nhất nếu delta==0, vô nghiệm nếu delta<0
    else:
        delta = b*b-4*a*c
        if delta <0:
            raise ValueError("Math domain error")
        elif delta==0:
            return (-b/(2*a), -b/(2*a))
        else:
            return (min((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)), max((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)))
