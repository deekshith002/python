import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return self.radius * 2

    def __str__(self):
        return f"CENTRE OF CIRCLE = ({self.x},{self.y}) \n RADIUS = {self.radius}"


c1 = Circle(5, 3, 15)
c2 = Circle(1, 2, 15)
print(c1)
print(f"AREA = {c1.area()}")
print(F"CIRCUMFERENCE = {c1.circumference()}")
print(c2)