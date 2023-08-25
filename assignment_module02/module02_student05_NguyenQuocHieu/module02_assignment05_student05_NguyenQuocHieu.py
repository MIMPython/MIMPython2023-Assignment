class ListEditor:
    def __init__(self, content: list) -> None:
        self.list = content

    def show(self):
        print(self.list)

    def square(self, index: int) -> None:
        """
        Square index-element in the list
        Args:
            index {int} -- index of the element

        """
        if index < 0 or index >= len(self.list):
            raise IndexError("Index out of bound")
        else:
            self.list[index] = self.list[index] ** 2

    def delete(self, index: int, usingMethod=True) -> None:
        """
        Delete the index-element of the list 
        Args:
            index {int} -- Index of the element
            usingMethod {bool} -- if True, use an available method
        """
        if index < 0 or index >= len(self.list):
            raise IndexError("Index out of bound")
        else:
            if usingMethod:
                self.list.pop(index)
            else:
                head = self.list[0: index - 1]
                foot = self.list[index + 1: len(self.list)]
                head.extend(foot)
                self.list = head

    def appendSquare(self) -> None:
        """
        Append new value to list which equals to last value's square
        """
        lastValue = self.list[len(self.list) - 1]
        self.list.append(lastValue ** 2)

    def count(self) -> int:
        """
        Count the number of elements in the list

        Returns:
            int -- Number of elements in the list
        """
        return len(self.list)

    def sum(self) -> int:
        """
        Calculate the sum of all elements in the list

        Returns:
            int -- Sum of all elements in the list
        """
        return sum(self.list)

    def sumIf(self) -> int:
        """
        Calculate the sum of elements which has indexes at 1, 2, 3 and 5

        Returns:
            int -- Sum of above elements
        """
        indexes = [1, 2, 3, 5]
        value = 0
        for index in indexes:
            if index in range(len(self.list)):
                value += self.list[index]
        return value

    def reverse(self, usingBuiltInMethod=True) -> list:
        """
        Reverse the list

        Args:
            usingBuiltInMethod {bool} -- If True: use built-in method reverse()

        Returns:
            list -- A list which has elements reversed from the above list    
        """
        if usingBuiltInMethod:
            reversedList = list(reversed(self.list))
            return reversedList
        else:
            return self.list[::-1]

    def split(self) -> (list, list):
        """
        Split the list into two new lists: a list contains all odd elements and a list contains all even elements

        Returns:
            (list, list) -- List contains odd elements and list contains even elements
        """
        oddList = []
        evenList = []
        for element in self.list:
            if element % 2 == 0:
                evenList.append(element)
            else:
                oddList.append(element)

        return (oddList, evenList)

    def sortDescending(self) -> list:
        """
        Sort the list in descending order

        Returns:
            list -- Sorted list
        """
        return sorted(self.list, reverse=True)

    def compare(self, otherList: list) -> None:
        """
        Compare two number of elements in two lists
        """
        if len(self.list) == len(otherList):
            print("Same length")
        elif len(self.list) > len(otherList):
            print("Above list has more elements than other list")
        else:
            print("Above list has fewer elements than other list")

    def merge(self, otherList: list) -> None:
        """
        Merge two list
        """
        self.list.extend(otherList)


if __name__ == "__main__":
    A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

    editor = ListEditor(content=A)
    print("a)")
    editor.square(index=3)
    editor.show()
    print("b)")
    editor.delete(index=3, usingMethod=True)
    editor.show()
    editor.delete(index=3, usingMethod=False)
    editor.show()
    print("c)")
    editor.appendSquare()
    editor.show()
    print("d)")
    print(editor.count())
    print("e)")
    print(editor.sum())
    print("f)")
    print(editor.sumIf())
    print("g)")
    print(editor.reverse(usingBuiltInMethod=True))
    print(editor.reverse(usingBuiltInMethod=False))
    print("h)")
    (odd, even) = editor.split()
    print(odd)
    print(even)
    print("i)")
    sortedList = editor.sortDescending()
    print(sortedList)
    print("j)")
    editor.compare(sortedList)
    print("k)")
    editor.merge(sortedList)
    editor.show()
