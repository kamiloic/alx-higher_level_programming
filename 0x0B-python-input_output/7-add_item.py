#!/usr/bin/python3
"""0x0B-python-input_output Module"""


import sys
import os.path

from_file = "add_item.json"

if not os.path.exists(from_file):
    with open(from_file, mode='w', encoding='utf-8') as file:
        file.write("[]")

with open(from_file, mode='r', encoding='utf-8') as file:
    data = json.load(file)

data.extend(sys.argv[1:])

with open(from_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file)
