def factorialNum(n):
    if n == 0:
        return 1
    else:
        return n * factorialNum(n-1)

def HowManyZero(n):        
    a = factorialNum(n)
    count = 0
    while a % 10 == 0:
        count += 1
        a /= 10
    return count, a 

print(HowManyZero(10)) 
# có 2 chữ số 0 ở tận cùng và số mới là: 36288
