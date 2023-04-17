#!/usr/bin/python3

"""
  This module returns the list of available
  attributes and methods of an object
"""


def lookup(obj):
    """returns a list object"""
    return dir(obj)
