class Shape:
    def __init__(self, color="red"):
        self.color = color

    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def __str__(self):
        return f"Shape(color={self.color})"

class Rectangle(Shape):
    def __init__(self, width=0, height=0, color="red"):
        super().__init__(color)
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side_length):
        """Alternative constructor to create a rectangle from a square"""
        return cls(side_length, side_length)

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"

class Circle(Shape):
    def __init__(self, radius=0, color="red"):
        super().__init__(color)
        self.radius = radius

    def area(self, pi=3.14):  # Method overloading through default arguments
        return pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"


if __name__ == "__main__":
    # Demonstrating the functionality
    # Using the default constructor
    rect1 = Rectangle()
    print(rect1)
    print(f"Area of rect1: {rect1.area()}")

    # Using the primary constructor
    rect2 = Rectangle(5, 10, "blue")
    print(rect2)
    print(f"Area of rect2: {rect2.area()}")

    # Using the alternative constructor
    rect3 = Rectangle.from_square(7)
    print(rect3)
    print(f"Area of rect3: {rect3.area()}")

    # Creating and using a Circle
    circle = Circle(5, "green")
    print(circle)
    print(f"Area of circle: {circle.area()}")

    # Method overriding
    shape = Shape()
    try:
        print(shape.area())
    except NotImplementedError as e:
        print(e)
