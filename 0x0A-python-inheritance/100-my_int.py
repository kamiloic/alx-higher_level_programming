#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """
    Class representing a custom integer with inverted == and != operators.
    """

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)
