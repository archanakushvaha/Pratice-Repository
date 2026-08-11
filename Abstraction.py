#Abstraction

from abc import ABC , abstractmethod

import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2+self.length*self.width

class Circle(Shape):

    def __init__(self , redius):
        self.redius = redius

    def area(self):
        return math.pi*self.redius*self.redius

    def perimeter(self):
        return 2*math.pi*self.redius
    
try:
    s = Shape()
except TypeError as e:
    print("Shape Error : " , e)
            

r = Rectangle(10 , 20)

print("Rectangle Area : " , r.area())
print("Rectangle Perimeter : " , r.perimeter())


c = Circle(7)

print(f"Circle Area : {c.area():.3f} " , )

print(f"Circle Area : " , round(c.area() , 2) )
print("Circle Area : " , round(c.perimeter() , 2))



    
