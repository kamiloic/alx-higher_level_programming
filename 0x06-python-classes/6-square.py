#!/usr/bin/python3
"""Module representing a Square with size and position.

Attributes:
    None

Classes:
    Square: Represents a square with a given size and position.
"""

class Square:
    """Represents a square with a given size and position.

    Attributes:
    - size (int): The size of the square's side.
    - position (tuple): The position of the square in (x, y) coordinates.

    Methods:
    - __init__: Initializes the square with a given size and position.
    - area: Calculates the area of the square.
    - my_print: Prints the square using '#' characters with the given position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size and position.

        Parameters:
        - size (int): The size of the square's side.
        - position (tuple): The position of the square in (x, y) coordinates.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Parameters:
        - value (int): The size of the square's side.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute.

        Parameters:
        - value (tuple): The position of the square in (x, y) coordinates.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters with the given position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
