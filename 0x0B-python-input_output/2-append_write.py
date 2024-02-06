#!/usr/bin/python3
"""Def a write_file function."""

def append_write(filename="", text=""):
    """ func """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
