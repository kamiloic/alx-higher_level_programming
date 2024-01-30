#!/usr/bin/python3
"""Module for matrix operations.

Attributes:
    error_message_type (str): Common error message for matrix operations.

Methods:
    - divide_num_by(num, div): Divide a number by another number.
    - has_same_row_size(matrix): Check if all rows in the matrix have the same size.
    - matrix_divided(matrix, div): Divide each element in the matrix by a divisor.
"""

error_message_type = "matrix must be a matrix (list of lists) of integers/floats"


def divide_num_by(num, div):
    """
    Divide a number by another number.

    Parameters:
    - num: The numerator (an integer or float).
    - div: The divisor (an integer or float).

    Returns:
    - The result of the division, rounded to 2 decimal places.

    Raises:
    - TypeError: If num or div is not an integer or float.
    - ZeroDivisionError: If div is 0.
    """
    if not isinstance(num, int) and not isinstance(num, float):
        raise TypeError(error_message_type)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(error_message_type)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return (num / div).__round__(2)


def has_same_row_size(matrix):
    """
    Check if all rows in the matrix have the same size.

    Parameters:
    - matrix: A matrix (list of lists).

    Returns:
    - True if all rows have the same size, False otherwise.

    Raises:
    - TypeError: If matrix is not a list of lists.
    - TypeError: If any row in the matrix is not a list.
    - TypeError: If the rows have different sizes.
    """
    row_size = 0
    if (len(matrix) > 0 and len(matrix[0]) > 0):
        row_size = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_message_type)
        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    return True


def matrix_divided(matrix, div):
    """
    Divide each element in the matrix by a divisor.

    Parameters:
    - matrix: A matrix (list of lists).
    - div: The divisor (an integer or float).

    Returns:
    - A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
    - TypeError: If matrix is not a list of lists.
    - TypeError: If any row in the matrix is not a list.
    - TypeError: If the rows have different sizes.
    - TypeError: If div is not an integer or float.
    - ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError(error_message_type)

    if has_same_row_size(matrix):
        pass

    result = []
    for row in matrix:
        result.append(list(map(lambda x: divide_num_by(x, div), row)))

    return result
