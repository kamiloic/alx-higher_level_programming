#!/usr/bin/python3
"""0x0B-python-input_output Module"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
