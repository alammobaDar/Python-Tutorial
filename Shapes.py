import math


class Shapes:
    def __init__(self, length, width):
        self.length = length
        self.width = width




class Rectangle(Shapes):

    def __init__(self, length, width):
        super().__init__(length,width)
    def Calculate_area(self):
        return self.length*self.width


class Circle(Shapes):
    def __init__(self, radius):
       self.radius = radius

    def Calculate_area(self):
        return math.pi*math.pow(self.radius,2)


rectangle = Rectangle(3,3)
circle = Circle(3)

print(rectangle.Calculate_area())
print(circle.Calculate_area())