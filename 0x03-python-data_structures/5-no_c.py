#!/usr/bin/python3

def no_c(my_string=""):
    str_arr = list(my_string)
    cfree_string = ""

    for i in range(len(str_arr)):
        char = str_arr[i]
        cfree_string += char if char not in "cC" else ""

    return cfree_string
