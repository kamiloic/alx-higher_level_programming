#!/usr/bin/python3
"""0x0B-python-input_output Module"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
