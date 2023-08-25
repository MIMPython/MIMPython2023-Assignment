import math


def solve_quadratic(a, b, c):
    if a == 0:
        print("'a' cannot be zero")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return ()
        elif delta == 0:
            x = -b / (2*a)
            return (x,)
        else: 
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            if x1 < x2:
                return (x1, x2)
            else:
                return (x2, x1)
            

def foo(a, b, c):
    return solve_quadratic(a,b,c)

a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
results = foo(a, b, c)
print(results)
