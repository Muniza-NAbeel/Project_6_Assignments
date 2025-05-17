from abc import ABC, abstractmethod

class Shape(ABC):   # Abstract Base Class
    @abstractmethod   # Abstract method 
    def area(self):
        pass           

class Rectangle(Shape):     # Inheriting from Shape
    def __init__(self, length, width):   # Constructor
        self.length = length
        self.width = width

    def area(self):       # Overriding abstract method
        """Calculating area of rectangle"""
        return self.length * self.width
    
rect = Rectangle(10, 5)     # Creating object of Rectangle
print(f"Area of Rectangle : {rect.area()}")