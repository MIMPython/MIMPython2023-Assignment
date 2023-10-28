import math


class Parallelogram:
    def __init__(self, base: int, side: int, angle: int) -> None:
        '''
        Initialize a Parallelogram
        Parameters:
            base, side, angle
        Raises:
            Error if the arguments are invalid
        '''
        assert base > 0 and side > 0 and (
            0 < angle < 180), 'Error: Invalid arguments.'
        self.base = base
        self.side = side
        self.angle = math.radians(angle)
        self.name = 'Parallelogram'

    @property
    def perimeter(self):
        return 2*(self.base + self.side)

    @property
    def area(self):
        return self.base*(self.side*math.sin(self.angle))

    def __repr__(self) -> str:
        return f'{self.name}: base={self.base}, side ={self.side}, angle = {self.angle}'


class Rectangle(Parallelogram):
    def __init__(self, width: int, height: int) -> None:

        super().__init__(width, height, 90)
        self.name = 'Rectangle'


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        super().__init__(side, side)
        self.name = 'Square'


class Rhombus(Parallelogram):
    def __init__(self, side: int, angle: int) -> None:
        super().__init__(side, side, angle)
        self.name = 'Rhombus'


class Ellipse:
    def __init__(self, major_axis: int, minor_axis: int) -> None:
        '''
        Initialize a Ellipse
        Parameters:
            major axis, minor axis
        Raises:
            Error if the arguments are invalid
        '''
        assert major_axis > 0 and minor_axis > 0, 'Error: Invalid arguments.'
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        self.name = 'Ellipse'

    @property
    def perimeter(self):
        return 2*math.pi*math.sqrt((self.major_axis**2 + self.minor_axis**2)/2)

    @property
    def area(self):
        return math.pi*self.major_axis*self.minor_axis

    def __repr__(self):
        return f'{self.name}: major axis = {self.major_axis}, minor axis = {self.minor_axis}'


class Circle(Ellipse):
    def __init__(self, radius: int) -> None:
        super().__init__(radius, radius)
        self.name = 'Circle'


if __name__ == '__main__':
    parallelogram = Parallelogram(4, 5, 60)
    # Parallelogram: base=4, side =5, angle = 1.0471975511965976
    print(parallelogram)
    print(parallelogram.area)  # 17.32050807568877
    print(parallelogram.perimeter)  # 18
    print()
    rect = Rectangle(4, 5)
    print(rect)  # Rectangle: base=4, side =5, angle = 1.5707963267948966
    print(rect.area)  # 20
    print(rect.perimeter)  # 18
    print()
    square = Square(4)
    print(square)  # Square: base=4, side =4, angle = 1.5707963267948966
    print(square.area)  # 16
    print(square.perimeter)  # 16
    print()
    rhombus = Rhombus(4, 60)
    print(rhombus)  # Rhombus: base=4, side =4, angle = 1.0471975511965976
    print(rhombus.area)  # 13.856406460551018
    print(rhombus.perimeter)  # 16
    print()
    ellipse = Ellipse(6, 7)
    print(ellipse)  # Ellipse: major axis = 6, minor axis = 7
    print(ellipse.area)  # 131.94689145077132
    print(ellipse.perimeter)  # 40.9613567668991
    print()
    cir = Circle(4)
    print(cir)  # Circle: major axis = 4, minor axis = 4
    print(cir.area)  # 50.26548245743669
    print(cir.perimeter)  # 25.132741228718345
