#!/usr/bin/python3
"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """Return the addition of two numbers."""
    if not (type(a) is float or type(a) is int):
        raise TypeError("a must be an integer")
    elif not (type(b) is float or type(b) is int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
