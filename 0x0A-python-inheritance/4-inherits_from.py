#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of, or if it inherits from,
    the specified class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
