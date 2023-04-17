#!/usr/bin/python3

"""
  This module returns the list of available
  attributes and methods of an object
"""


def lookup(obj):
    """returns a list of attributes and methods of a given object"""
    return dir(obj)
