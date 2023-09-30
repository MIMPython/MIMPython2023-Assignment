import numpy
import math


def numRightMostDigits(n: int):
    rightMostDigits = 0
    a = int(math.log(n, 5))
    for i in range(1, a + 1):
        rightMostDigits += int(n / 5 ** i)
    return rightMostDigits


def check(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(result)


def lastRightMostDigit(n: int):
    right = numRightMostDigits(n)
    array = numpy.zeros(n + 1, dtype=numpy.uint16)
    for i in range(n + 1):
        array[i] = 1
    array[0] = 0
    array[1] = 0
    for i in range(2, n + 1):
        if array[i] == 1:
            j = 2 * i
            while j < n + 1:
                array[j] = 0
                j += i
    primes = []
    for i in range(n + 1):
        if array[i] == 1:
            primes.append(i)
    expPrime = numpy.zeros(len(primes), dtype=numpy.uint16)
    for i in range(len(primes)):
        if primes[i] != 5:
            value = 0
            limit = int(math.log(n, primes[i]))
            for j in range(1, limit + 1):
                value += int(n / primes[i] ** j)
            if primes[i] != 2:
                expPrime[i] = (primes[i] ** value) % 10
            else:
                expPrime[i] = (primes[i] ** (value - right)) % 10
        else:
            expPrime[i] = 1
    result = 1
    for v in expPrime:
        result *= v
    return result % 10


if __name__ == "__main__":

    """
    Tóm tắt đề bài: Đặt t(n) = n!
    Thực hiện 2 yêu cầu sau:
    1, Cho biết t(n) có bao nhiêu chữ số 0 ở tận cùng bên phải
    2, Bỏ tất cả chữ số 0 ở tận cùng bên phải của t(n) đi, thu được số mớ t'(n).
    Tìm chữ số tận cùng của t'(n)
    """
    print(numRightMostDigits(26))  # Thực hiện yêu cầu 1
    print(lastRightMostDigit(26))  # Thực hiện yêu cầu 2
