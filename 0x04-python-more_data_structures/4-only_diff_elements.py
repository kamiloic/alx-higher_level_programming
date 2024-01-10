#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = set_1.copy()

    for item in set_2:
        if (item in set_1):
            diff.remove(item)
        else:
            diff.add(item)

    return diff
