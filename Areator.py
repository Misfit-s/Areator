import math as m

class Circle:
    """A class that represents a circle."""
    def __init__(self, radius):
        self.pi = m.pi
        """the number of pi"""
        self.radius = float(radius)
        """the radius of the circle"""
        self.area = 0
        """the area of the circle"""
        
    def get_area_of_circle(self):
        """Returns the area of the circle."""
        self.area = self.pi * (self.radius ** 2)
        return self.area

class Triangle:
    """A class that represents a triangle."""
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.sides = {'side_a': self.side_a,'side_b': self.side_b,'side_c': self.side_c}
        self.area = 0
        """the area of the triangle"""
        
    def semiperimeter(self):
        """Returns the semiperimeter."""
        return 1 / 2 * (self.side_a + self.side_b + self.side_c)
    
    def hypotenuse(self):
        """Returns the hypotenuse."""
        hypotenuse_name = max(self.sides, key = self.sides.get)
        return hypotenuse_name
    
    def is_triangle_right_angled(self):
        """"Returns whether or not the triangle is right-angled."""
        hypotenuse_name = self.hypotenuse()
        sides = self.sides
        
        hypotenuse = sides.get(hypotenuse_name)
        sides.pop(hypotenuse_name)
        
        squared_cathets = [value ** 2 for value in sides.values()]
        sum_of_squared_cathets = sum(squared_cathets)
        
        if hypotenuse ** 2 == sum_of_squared_cathets:
            return True
        else:
            return False
        
    def get_area_of_triangle(self):
        """Returns the area of the triangle."""
        semiperimeter = self.semiperimeter()
        return (semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) * (semiperimeter - self.side_c)) ** 0.5