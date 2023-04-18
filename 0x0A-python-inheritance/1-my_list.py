#!/usr/bin/python3

"""
  This module houses a function
  that prints a list of integers
  in ascending sort
"""


class MyList(list):

    """class inherits list of int"""

    def print_sorted(self):
        """prints the list in ascending sort"""
        sorted_list = sorted(self)
        print(sorted_list)
