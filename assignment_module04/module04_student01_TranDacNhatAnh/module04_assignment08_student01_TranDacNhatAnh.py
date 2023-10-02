def factorial(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product
print(factorial(50)) # 30414093201713378043612608166064768844377641568960512000000000000
# a) Đếm số chữ số ở tận cùng bên phải
def mathCountZeroes(n): 
    # Ý tưởng toán học của hàm là, do số thừa số 2 trong tích n! luôn nhiều hơn so với số thừa số 5, vậy nên ta chỉ cần quan tâm đến
    # các số có chứa lũy thừa của 5, cụ thể là các số chia hết cho 5 (>= 1 thừa số 5), 25 (>= 2 thừa số 5),...
    zeroes = 0
    while n>0:
        n //= 5
        zeroes += n
        return zeroes
print(mathCountZeroes(50)) # 10
# b) Chữ số khác 0 ở ngoài cùng bên phải
def nonZeroRight(n):
    factor = 1
    for i in range(1,n+1):
        factor*=i
        while factor%10 == 0:
            factor //= 10
    return factor%10
print(nonZeroRight(50)) # 2