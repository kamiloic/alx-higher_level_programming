#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    return list(map(mapRowToSqaure, matrix))


def square(x):
    return x * x


def mapRowToSqaure(row=[]):
    return list(map(square, row))
