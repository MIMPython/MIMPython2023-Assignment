# Bài tập 2: (class inheritance)
import math
import turtle

class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(5)
        for i in range(2):
            t.forward(self.length)
            t.left(90)
            t.forward(self.width)
            t.left(90)
        turtle.done()

    def print_info(self):
        print(f"A {self.color} rectangle with length {self.length} and width {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)

    def print_info(self):
        print(f"A {self.color} square with side {self.length}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Rhombus(Rectangle):
    def __init__(self, side, angle, color):
        self.side = side
        self.angle = angle
        self.color = color

    def area(self):
        import math
        return self.side ** 2 * math.sin(math.radians(self.angle))

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(5)
        for i in range(2):
            t.forward(self.side)
            t.left(180 - self.angle)
            t.forward(self.side)
            t.left(self.angle)
        turtle.done()

    def print_info(self):
        print(f"A {self.color} rhombus with side {self.side} and angle {self.angle}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Ellipse:
    def __init__(self, major_axis, minor_axis, color):
        self.major_axis = major_axis
        self.minor_axis = minor_axis
        self.color = color

    def area(self):
        return math.pi * self.major_axis * self.minor_axis

    def perimeter(self):
        # Sử dụng công thức Ramanujan để tính gần đúng chu vi hình ellipse
        a = self.major_axis / 2
        b = self.minor_axis / 2
        h = ((a - b) / (a + b)) ** 2
        return math.pi * (a + b) * (1 + 3 * h / (10 + math.sqrt(4 - 3 * h)))

    def draw(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.pensize(5)
        # Sử dụng công thức parametric để vẽ hình ellipse
        t.penup()
        t.goto(self.major_axis / 2, 0)
        t.pendown()
        for angle in range(360):
            x = self.major_axis / 2 * math.cos(math.radians(angle))
            y = self.minor_axis / 2 * math.sin(math.radians(angle))
            t.goto(x, y)
        turtle.done()

    def print_info(self):
        print(f"A {self.color} ellipse with major axis {self.major_axis} and minor axis {self.minor_axis}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Circle(Ellipse):
    def __init__(self, radius, color):
        super().__init__(2 * radius, 2 * radius, color)

    def perimeter(self):
        return 2 * math.pi * self.major_axis / 2

    def print_info(self):
        print(f"A {self.color} circle with radius {self.major_axis / 2}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

# Vẽ ra các hình
rect = Rectangle(200, 150, "blue")
square = Square(150, "yellow")
rhombus = Rhombus(200, 100, "orange")
elip = Ellipse(200, 250, "brown")
circle = Circle(200, "green")
rect.print_info()
square.print_info()
rhombus.print_info()
elip.print_info()
circle.print_info()
rect.draw()
square.draw()
rhombus.draw()
elip.draw()
circle.draw()