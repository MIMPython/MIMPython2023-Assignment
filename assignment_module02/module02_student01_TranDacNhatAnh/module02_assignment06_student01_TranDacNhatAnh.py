from math import sqrt
def solveQuadratic(a,b,c):
    #TH1: a==0, bài toán trở thành giải phương trình bậc nhất.
    if a==0:
        if b==0:
            return ()
        else:
            return (-c/b, )
    #TH2: a!=0, phương trình có 2 nghiệm phân biệt nếu delta>0, có nghiệm duy nhất nếu delta==0, vô nghiệm nếu delta<0
    else:
        delta = b*b-4*a*c
        if delta <0:
            return ()
        elif delta==0:
            return (-b/(2*a), )
        else:
            return (min((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)), max((-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)))
# Nếu bỏ điều kiện a, b, c đồng thời bằng 0 thì tập nghiệm phương trình là toàn bộ tập số thực, vậy ở TH a=b=0, 
# thêm if c=0: return (all, ) là được.

#Test
print(solveQuadratic(1,-3,2)) #(1.0, 2.0)
print(solveQuadratic(1,-6,9)) #(3.0,)
print(solveQuadratic(4,0,7)) #()