#create a class shape with a variable radius. initialise the varible with constructr . create a class circle  which is child of shape class
#define a method cal_area() to cal area using math pckg. 
#create a class shpere which is child of shape class . define cal_volume to find volume of sphere 


import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def cal_area(self):
        area = math.pi * math.pow(self.radius , 2)
        print("Area of Circle =", area)


class Sphere(Shape):
    def cal_volume(self):
        volume = (4 / 3) * math.pi * math.pow(self.radius , 3)
        print("Volume of Sphere =", volume)


c = Circle(5)
c.cal_area()

s = Sphere(5)
s.cal_volume()