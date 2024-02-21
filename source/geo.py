## Class based test in pytest

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Square:

    def __init__(self):
        self.name  = 'square'
        self.side = 5

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle:

    def __init__(self, radius) -> None:
        self.name = 'circle'
        self.pi = 3.1415
        self.radius = radius

    def area(self):
        return round((self.radius ** 2) * self.pi,2)

    def perimeter(self):
        return round(self.pi * 2 * self.radius,2)

class Rectangle(Shape):
    # This is for the pytest fixtures example

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return (self.length **2) + (self.breadth**2)
    

# this is for mark and parameterization
class Osquare(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(self.side, self.side)
