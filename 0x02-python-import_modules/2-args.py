#!/usr/bin/python3

import sys

n = len(sys.argv) - 1

if n < 1:
    print("{} arguments.".format(n))

elif n == 1:
    print("{} argument:\n{}: {}".format(n, n, sys.argv[1]))

else:
    print("{} arguments:".format(n))
    for i in range(1, n+1):
        print("{}: {}".format(i, sys.argv[i]))

    print()
