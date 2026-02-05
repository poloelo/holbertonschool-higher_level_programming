#!/usr/bin/python3

"""
Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Shape Abstract class to define geometric shapes interface
    """
    
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class representing a circular shape
    
    Attributes:
        radius: The radius of the circle (must be positive)
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance
        
        Args:
            radius: The radius of the circle
            
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle
        
        Returns:
            float: The area (π * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter of the circle
        
        Returns:
            float: The perimeter (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class representing a rectangular shape
    
    Attributes:
        width: The width of the rectangle
        height: The height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            
        Raises:
            ValueError: If width or height is negative
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle
        
        Returns:
            float: The area (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle
        
        Returns:
            float: The perimeter (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape
    
    Args:
        shape: An object with area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")