def countDigits(numPages):
    digits = 0
    for i in range(1, numPages+ 1):
        digits += len(str(i))
    return digits

print(countDigits(10))#11
print(countDigits(20))#31
print(countDigits(125))#267

def countPages(numDigits):
    if numDigits <= 9:
        return 1
    elif numDigits <= 189:
        return (numDigits - 9) // 2 + 9
    else:
        return (numDigits - 189) // 3 + 99

print(countPages(267)) # 125
print(countPages(31))  #20