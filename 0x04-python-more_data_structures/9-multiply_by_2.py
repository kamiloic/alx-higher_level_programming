#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    rslt = dict()
    for key in a_dictionary:
        rslt[key] = a_dictionary[key] * 2

    return rslt
