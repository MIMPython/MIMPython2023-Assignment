import math


def isPrime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def findLargestPrimeFactor(number: int) -> int:
    if isPrime(number):
        return number
    else:
        middle = int(math.sqrt(number))
        index = 1
        maxFactor = 1
        while index <= middle:
            if number % index == 0 and isPrime(index):
                maxFactor = index
            index += 1
        return maxFactor


if __name__ == "__main__":
    maxFactor = findLargestPrimeFactor(number=600851475143)
    print("Largest prime factor is: ", maxFactor)
# Mô tả: Tìm ước số nguyên tố lớn nhất của số 600851475143
# Chạy code: python module03_assignment07_student05_NguyenQuocHieu.py
# Output: 6857
