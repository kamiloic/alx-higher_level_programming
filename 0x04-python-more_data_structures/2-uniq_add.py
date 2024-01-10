#!/usr/bin/python3

def uniq_add(my_list=[]):
    sorted_list = sorted(my_list)
    sum = 0
    for i in range(len(my_list)):
        if i == 0:
            sum += sorted_list[i]
        if i > 0 and sorted_list[i - 1] != sorted_list[i]:
            sum += sorted_list[i]

    return sum
