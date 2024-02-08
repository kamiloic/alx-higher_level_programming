#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """Inherits from list and adds a method to print a sorted list."""
    def print_sorted(self):
        print(sorted(self))
