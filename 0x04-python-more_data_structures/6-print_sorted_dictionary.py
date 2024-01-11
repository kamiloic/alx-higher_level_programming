#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []
    for key in a_dictionary:
        keys.append(key)

    sortedKeys = sorted(keys)
    for key in sortedKeys:
        print("{}: {}".format(key, a_dictionary[key]))
