#!/usr/bin/python3
"""A module that rotates a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """given a square matrix, return a 90 degrees rotated matrix"""

    test_matrix = matrix.copy()
    matrix.clear()

    test_matrix.reverse()

    for idx in range(len(test_matrix)):
        new_row = [element[idx] for element in test_matrix]
        matrix.append(new_row)
