class List:
    def __init__(self) -> None:
        self.data = []

    def add(self, element: list) -> None:
        self.data.append(element)

    def print(self) -> None:
        for element in self.data:
            print(element)

    def sortBySum(self) -> None:
        size = len(self.data)
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                if sum(self.data[j]) < sum(self.data[min_index]):
                    min_index = j
            temp = self.data[ind]
            self.data[ind] = self.data[min_index]
            self.data[min_index] = temp


if __name__ == "__main__":
    """
    Tóm tắt đề bài: cho trước mảng lớn A bao gồm các mảng con a. 
    Sắp xếp các phần tử của A theo tổng giá trị các phần từ trong a.
    """
    testList = List()
    testList.add([1, 2])
    testList.add([3, 0, 4])
    testList.add([2])
    testList.add([4, 5])
    print("Input: ")
    testList.print()
    testList.sortBySum()
    print("Output: ")
    testList.print()
