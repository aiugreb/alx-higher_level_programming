#!/usr/bin/python3
"""Defines a pascal_triangle function."""


def pascal_triangle(n):
    """ def """
    if n <= 0:
        return []
    triangles = []
    for i in range(n):
        triangles.append([])
        for j in range(i):
            if len(triangles[i]) == 0:
                triangles[i].append(1)
                continue
            value = triangles[i-1][j-1] + triangles[i-1][j]
            triangles[i].append(value)
        triangles[i].append(1)
    return triangles
