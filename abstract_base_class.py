from abc import ABC, abstractclassmethod


class Shape(ABC):
    def __init__(self):
        self.name = None

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def fact(self):
        return "I am a two-dimensional shape."


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi*self.radius**2

    def fact(self):
        return "Circles have 2*pi*r circumference"

A = Circle(3)
print(A.fact())
B = Shape()  # this line will result in error