#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    numerator = 0
    denomenator = 0

    for pair in my_list:
        numerator += pair[0] * pair[1]
        denomenator += pair[1]

    return numerator / denomenator
