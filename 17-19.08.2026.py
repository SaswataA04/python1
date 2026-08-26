

#create a class triangle with 3 variables side1, side2, side3. initialise the variables with constructor .
#it also has angle1, , angle2 , angle3 . all sides and angles will be initialised with constructor
#create a class equilateral triangle and find the area of triangle with cal_area func . find the tangent of all angles using  find_ angle() 
#create scalene class which is child of triangle class . find perimeter of trianlge with cal_perimeter() 
#print area  as a whole no . NO TYPECASTING . USE MATH PCKG



import math


class Triangle:

    def __init__(self, side1, side2, side3, angle1, angle2, angle3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3


class EquilateralTriangle(Triangle):

    def __init__(self, side1, side2, side3, angle1, angle2, angle3):

        super().__init__(side1, side2, side3, angle1, angle2, angle3)

    def cal_area(self):

        area = (math.sqrt(3) / 4) * math.pow(self.side1, 2)

        return area

    def find_angle(self):

        tan1 = math.tan(math.radians(self.angle1))
        tan2 = math.tan(math.radians(self.angle2))
        tan3 = math.tan(math.radians(self.angle3))

        print("Tangent of angle 1 =", tan1)
        print("Tangent of angle 2 =", tan2)
        print("Tangent of angle 3 =", tan3)


class ScaleneTriangle(Triangle):

    def __init__(self, side1, side2, side3, angle1, angle2, angle3):

        super().__init__(side1, side2, side3, angle1, angle2, angle3)

    def cal_perimeter(self):

        perimeter = self.side1 + self.side2 + self.side3

        return perimeter


equilateral = EquilateralTriangle(6, 6, 6, 60, 60, 60)

area = equilateral.cal_area()

print("Area of equilateral triangle =", f"{area:.0f}")

equilateral.find_angle()


scalene = ScaleneTriangle(5, 6, 7, 50, 60, 70)

perimeter = scalene.cal_perimeter()

print("Perimeter of scalene triangle =", perimeter)