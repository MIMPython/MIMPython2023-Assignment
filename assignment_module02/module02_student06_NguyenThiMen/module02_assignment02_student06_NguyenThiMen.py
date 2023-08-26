# Bài tập 2. Viết một hàm tính bình phương của một số nguyên.
def getSquareNumber(x):
    return x**2


b = int(input("Enter integer number:"))
print(f'The square of {b} is {getSquareNumber(b)}')
if __name__ == '__main__':
    print(getSquareNumber(-2))
    print(getSquareNumber(5))
    print(getSquareNumber(0))
