#!/usr/bin/python3
"""0x0B-python-input_output Module"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
