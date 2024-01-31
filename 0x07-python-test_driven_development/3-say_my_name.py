#!/usr/bin/python3
"""
Module for printing names with optional last names.

Methods:
    say_my_name - Prints the provided name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the provided name.

    Parameters:
    - first_name (str): First name.
    - last_name (str, optional): Last name. Defaults to an empty string.

    Raises:
    - TypeError: If either first_name or last_name is not a string.

    Example:
    ::

        >>> say_my_name("John", "Doe")
        My name is John Doe

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
