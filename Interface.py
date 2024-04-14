from Areator import Circle, Triangle

shape_type = input("Enter the shape type:\n1.Circle\n2.Triangle")

if shape_type == '1':
    radius = int(input("Enter the radius:"))
    c = Circle(radius)
    print(c.get_area_of_circle())
    
elif shape_type == '2':
    side_a = int(input("Enter the side a:"))
    side_b = int(input("Enter the side b:"))
    side_c = int(input("Enter the side c:"))
    
    t = Triangle(side_a, side_b, side_c)
    print(t.get_area_of_triangle())
    print(t.is_triangle_right_angled())