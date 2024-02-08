#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Empty class representing a base geometry."""

    def area(self):
        """Area method
        Throw exception when not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
