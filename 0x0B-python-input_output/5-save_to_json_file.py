#!/usr/bin/python3
"""0x0B-python-input_output Module"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
