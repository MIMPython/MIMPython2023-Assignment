# Bài tập 1: (documentation/docstrings)
class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        area(): Return the area of the rectangle.
        perimeter(): Return the perimeter of the rectangle.
        is_square(): Return True if the rectangle is a square, False otherwise.
    """

    def __init__(self, length: float, width: float) -> None:
        """
        Initialize a rectangle with the given length and width.

        Arguments:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        """
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Return the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        
        Examples:
            >>> r = Rectangle(2, 3)
            >>> r.area()
            6.0
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """
        Return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.

        Examples:
            >>> r = Rectangle(2, 3)
            >>> r.perimeter()
            10.0
        """
        return 2 * (self.length + self.width)

    def is_square(self) -> bool:
        """
        Return True if the rectangle is a square, False otherwise.

        Returns:
            bool: True if the rectangle is a square, False otherwise.

        Examples:
            >>> r = Rectangle(2, 3)
            >>> r.is_square()
            False
        """
        return self.length == self.width
    

if __name__ == "__main__":
    r = Rectangle(2, 3)
    print(r.area())
    print(r.perimeter())
    print(r.is_square())