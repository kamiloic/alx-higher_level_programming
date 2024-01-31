#!/usr/bin/python3
"""Module with Text Indention related functions

Parameters:
    None

Methods:
    lazy_matrix_mul - Multiplies 2 matrices by using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using the module NumPy

    Parameters:
    - m_a: First matrix
    - m_b: Second matrix

    Returns:
    The product of both matrices
    """
    return np.matmul(np.array(m_a), np.array(m_b))
