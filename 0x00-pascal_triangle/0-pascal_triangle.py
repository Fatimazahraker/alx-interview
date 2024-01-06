#!/usr/bin/python3

def pascal_triangle(n):
    """Definition of function"""

    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
        triangle.append(row)

    return triangle

