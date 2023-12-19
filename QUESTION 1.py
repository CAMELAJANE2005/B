QUESTION 1
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_coordinates(self):
        return (self.x, self.y, self.z)
my_point = Point3D(1, 2, 3)
print(my_point.get_coordinates())
(1, 2, 3)



QUESTION 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.wi
my_rectangle = Rectangle(4, 3)
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()

print("Area:", area)
print("Perimeter:", perimeter)
Area: 12
Perimeter: 14

QUESTION 3 AND 4
import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def isInside(self, point_x, point_y):
        distance = math.sqrt((point_x - self.center_x)**2 + (point_y - self.center_y)**2)
        return distance <= self.radius