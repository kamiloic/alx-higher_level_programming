#!/usr/bin/python3
"""0x0B-python-input_output Module"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
