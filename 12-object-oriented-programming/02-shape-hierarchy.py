import math

# Create Circle and Rectangle classes with area() method.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this!")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Examples of using the Circle and Rectangle classes
circle = Circle(5)
print(f"Area of the circle with radius 5: {circle.area()}")
rectangle = Rectangle(4, 6)
print(f"Area of the rectangle with width 4 and height 6: {rectangle.area()}")
