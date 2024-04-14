from Areator import Circle, Triangle

class Interface:
    
    def __init__(self) -> None:
        self.shape_type = input("Enter the shape type:\n1.Circle\n2.Triangle\n")
        
    def circle(self):
        radius = int(input("Enter the radius:"))
        
        c = Circle(radius)
        print(c.get_area_of_circle())
    
    def triangle(self):
        side_a = int(input("Enter the side a: "))
        side_b = int(input("Enter the side b: "))
        side_c = int(input("Enter the side c: "))

        t = Triangle(side_a, side_b, side_c)
        print(t.get_area_of_triangle())
        print(t.is_triangle_right_angled())
        
    def main(self):
        if self.shape_type == '1':
            self.circle()
        elif self.shape_type == '2':
            self.triangle()
        else:
            print("Invalid Input")

if __name__ == "__main__":
    i = Interface()
    i.main()