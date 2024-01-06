#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row_idx in range(len(matrix)):
        row = matrix[row_idx]
        for i in range(len(row)):
            print(
                "{}{}".format(row[i], " " if i != len(row) - 1 else ""),
                end=""
                )
        print()
