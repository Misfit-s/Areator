import math as m

class Circle:
    """A class that represents a circle."""
    def __init__(self, radius):
        self.pi = m.pi
        self.radius = radius
        self.area = 0
        
    def area_of_circle(self):
        """Returns the area of the circle."""
        self.area = self.pi * (self.radius ** 2)
        return self.area