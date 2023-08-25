import math


def getNumberOfDigits(number: int) -> int:
    value = math.log10(number)
    numDigits = int(value)
    return numDigits + 1


def encode(numberOfPages: int) -> int:
    """
        Calculate number of digits needed to point book's pages

        Arguments:
            numberOfPages {int} -- Number of pages

        Returns:
            int -- Number of digits needed to point book's pages
    """
    value = 0
    numDigits = getNumberOfDigits(number=numberOfPages)
    for k in range(1, numDigits):
        value += k * (10 ** k - 10 ** (k - 1))
    value += numDigits * (numberOfPages - 10 ** (numDigits - 1) + 1)
    return value


def decode(numberOfDigits: int) -> int:
    """
        Calculate number of pages used number of digits for numbering
        Arguments:
            numberOfiDigits {int} -- Number of digits

        Returns:
            int -- Number of pages
    """
    def numDigits(index: int) -> int:
        return index * (10 ** index - 10 ** (index - 1))

    index = 1
    while numberOfDigits > numDigits(index=index):
        numberOfDigits -= numDigits(index=index)
        index += 1
    return 10 ** (index - 1) - 1 + (numberOfDigits // index)


if __name__ == "__main__":
    print(encode(numberOfPages=10))
    print(decode(numberOfDigits=11))
