
import math
def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,math.floor(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
def findPrimeFactor(n):
    list = []
    for i in range(2,math.floor(math.sqrt(n))):
        if n%i == 0 and isPrime(i):
            list.append(i)
    return max(list)

if __name__ == '__main__':
    print(findPrimeFactor(13195))#29
    print(findPrimeFactor(600851475143))#6857
