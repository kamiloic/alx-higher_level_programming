#!/usr/bin/python3

def best_score(a_dictionary):
    bestKey = ""
    bestValue = 0
    if (not a_dictionary):
        return None

    for name in a_dictionary:
        if (a_dictionary[name] > bestValue):
            bestKey = name
            bestValue = a_dictionary[name]

    return bestKey
