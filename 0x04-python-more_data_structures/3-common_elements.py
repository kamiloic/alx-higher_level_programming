#!/usr/bin/python3

def common_elements(set_1, set_2):
    commom = []

    for item_in_set_1 in set_1:
        for item_in_set_2 in set_2:
            if item_in_set_1 == item_in_set_2:
                commom.append(item_in_set_1)
    return commom
