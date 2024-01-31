#!/usr/bin/python3
"""Module representing a function add_interger.

Attributes:
    None

Mathods:
    add_integer: Add integers a and b.
"""


def add_integer(a, b=98):
    """
    Add integers a and b.

    Parameters:
    - a: an integer
    - b: an integer (default is 98)

    Returns:
    - The sum of a and b (integer)

    Raises:
    - TypeError if a or b is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
