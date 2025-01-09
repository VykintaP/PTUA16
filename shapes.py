class Shape:
    def __init__(self, name: str, sides: int):
        self.name = name
        self.sides = sides


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle", 4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length: float):
        self.side_length = side_length
        super().__init__(side_length, side_length)


square = Square(5)
print(square.name)
print(square.sides)
print(square.side_length)
print(square.width)
print(square.height)
print(square.area())
