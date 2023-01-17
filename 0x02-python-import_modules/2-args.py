#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print(f"{num_args} argument:")
    elif num_args > 1:
        print(f"{num_args} arguments:")
    else:
        print("0 arguments.")
    for i, arg in enumerate(sys.argv[1:]):
        print(f"{i+1}: {arg}")
