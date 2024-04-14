import unittest
from Areator import Circle
from Areator import Triangle

class TestCircle(unittest.TestCase):
    
    def test_area(self):
        circle  = Circle(5)
        self.assertAlmostEqual(circle.get_area_of_circle(), 78.53981633974483)
        
    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
            
class TestTriangle(unittest.TestCase):
    
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.get_area_of_triangle(), 6.0)
        
    def test_is_right_angled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_triangle_right_angled())
        
if __name__ == '__main__':
    unittest.main()
        
                
        
                