#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_results = my_list.copy()
    for i in range(len(list_results)):
        list_results[i] = True if list_results[i] % 2 == 0 else False
    return list_results
