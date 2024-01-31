#!/usr/bin/python3
"""
Module for printing squares of a specific size using the '#' character.

Methods:
    print_square: - Prints a square of a specific size using the '#' character.

"""


def print_square(size):
    """
    Prints a square of a specific size using the '#' character.

    Parameters:
    - size (int): The size of the square.

    Raises:
    - TypeError: If the size is not an integer.
    - ValueError: If the size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
