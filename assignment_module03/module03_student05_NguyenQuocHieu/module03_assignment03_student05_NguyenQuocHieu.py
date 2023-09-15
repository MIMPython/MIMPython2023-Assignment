def readData(textPath: str) -> list[str]:
    with open(textPath, "r") as text:
        rawData = text.readlines()[0]
    data = rawData.split(",")
    data = [name.strip("\"\"") for name in data]
    data = sorted(data)
    return data


class NamesScoring:
    def __init__(self, namesData: list[str]) -> None:
        self.data = namesData

    def values(self, word: str) -> int:
        score = 0
        for char in word:
            score += ord(char) - 64
        return score

    def calculate(self) -> int:
        totalScore = 0
        for index in range(len(self.data)):
            totalScore += (index + 1) * self.values(self.data[index])
        return totalScore


if __name__ == "__main__":
    path = "./module03_student05_NguyenQuocHieu/additionFolder/module03_assignment03_student05_NguyenQuocHieu_names.txt"
    data = readData(textPath=path)

    namesScoring = NamesScoring(namesData=data)
    totalScore = namesScoring.calculate()
    print(totalScore)

# Mô tả: Tính tổng điểm của các tên trong danh sách cho trước
# Chạy code: python module03_assignment03_student05_NguyenQuocHieu.py
# Output: 871198282
