"""Module for Square class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
