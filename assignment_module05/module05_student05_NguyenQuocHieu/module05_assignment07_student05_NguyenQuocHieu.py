import math
import random
def isPalindrome(number : int):
    string_number = str(number)
    x = string_number[::-1]
    return x == string_number

def isSquare(number : int):
    x = int(math.sqrt(number))
    return x * x == number

def find(bound : int) -> int:
    result = -1
    for i in range(bound):
        if isPalindrome(i) and isSquare(i):
            result = i 
    return result

def isInfinite():
    n = random.randint(0, 100)
    result = find(10 ** n)
    print("Number which is satisfied: " + result)

if __name__ == "__main__":
    isInfinite()