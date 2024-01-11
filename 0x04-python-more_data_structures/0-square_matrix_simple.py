#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_matrix.append(list(map(lambda x: x * x, row)))
    return result_matrix
