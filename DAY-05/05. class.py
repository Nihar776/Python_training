from math import pi
class Circle:

    def __init__(self, radius:float):
        self.radius =radius
        print(f"You have sucessfully created a Circle with radius {self.radius}")

    def calcArea(self):
        self.area=pi*self.radius**2
        print(f"Area of the circle with radius= {self.radius} is {self.area:.2f}")
    def calcCircumference(self):
        self.circumference=2*pi*self.radius
        print(f"Circumference of circle with Radius= {self.radius}={(self.circumference):.2f}")

circle=Circle(float(input("Enter radius of you desired length to create: ")))
circle.calcArea()
circle.calcCircumference()