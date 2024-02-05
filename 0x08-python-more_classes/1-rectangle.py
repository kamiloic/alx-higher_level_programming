#!/usr/bin/python3
""" Module representing Rectangle class
Parameters:
None

Classes:
Rectangle
"""


class Rectangle:
    """
    Rectangle class

    Private Attributes:
    __width
    __height
    """

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle instance.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width.

        Parameters:
        - width (int): Width of the rectangle.

        Raises:
        - TypeError: If width is not an integer.
        - ValueError: If width is less than 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height.

        Parameters:
        - height (int): Height of the rectangle.

        Raises:
        - TypeError: If height is not an integer.
        - ValueError: If height is less than 0.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
