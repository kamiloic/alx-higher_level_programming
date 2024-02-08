#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area method
        Throw exception when not implemented
        """
        return self.__height * self.__width

    def __str__(self):
        """Area method
        Throw exception when not implemented
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
