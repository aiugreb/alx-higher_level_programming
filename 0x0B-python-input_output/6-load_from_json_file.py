#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """ func """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
