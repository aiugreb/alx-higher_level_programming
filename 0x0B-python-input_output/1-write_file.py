#!/usr/bin/python3
"""Def a write_file function."""


def write_file(filename="", text=""):
    """ func """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
