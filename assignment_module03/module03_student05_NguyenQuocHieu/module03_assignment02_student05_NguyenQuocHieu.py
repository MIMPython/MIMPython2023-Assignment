def readData(textPath: str):
    with open(textPath, "r") as text:
        data = text.readlines()
    data = [number.rstrip(number[-1])
            for number in data if number.endswith("\n")]
    return data


class BigNumberProcess:
    def __init__(self, data) -> None:
        self.data = data

    def encodeNumber(self, numberString: str) -> list[int]:
        numberString = list(reversed(numberString))
        digitsList = []
        for i in range(len(numberString)):
            digitsList.append(int(numberString[i]))
        return digitsList

    def add2Lists(self, first: list, second: list) -> list:
        index = 0
        firstLimit = len(first)
        secondLimit = len(second)
        if firstLimit < secondLimit:
            for i in range(secondLimit - firstLimit):
                first.append(0)
            limitation = secondLimit
        elif firstLimit > secondLimit:
            for i in range(firstLimit - secondLimit):
                second.append(0)
            limitation = firstLimit
        else:
            first.append(0)
            second.append(0)
            limitation = firstLimit + 1
        while index < limitation:
            if index == len(first) - 1:
                first.append(0)
            first[index] += second[index]
            if first[index] >= 10:
                first[index] -= 10
                first[index + 1] += 1
            index += 1
        return first

    def calculate(self) -> list[int]:
        result = [0]
        for numberString in self.data:
            digitsList = self.encodeNumber(numberString=numberString)
            result = self.add2Lists(result, digitsList)
        output = list(reversed(result))
        index = 0
        while index < len(output):
            if output[index] != 0:
                startIndex = index
                break
            index += 1
        return output[startIndex: startIndex + 10]


if __name__ == "__main__":
    dataPath = "./module03_student05_NguyenQuocHieu/additionFolder/module03_assignment02_student05_NguyenQuocHieu_bignumberdata.txt"
    data = readData(dataPath)

    program = BigNumberProcess(data=data)
    output = program.calculate()
    print(output)

# Mô tả: Tìm 10 chữ số đầu tiên của tổng 100 số 50 chữ số đã cho
# Chạy code: python module03_assignment02_student05_NguyenQuocHieu.py
# Output: [5, 4, 8, 3, 8, 7, 2, 6, 9, 6]
