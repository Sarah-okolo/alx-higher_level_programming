#!/usr/bin/python3

import sys

n = len(sys.argv)

if n < 1:
    print("{} arguments.".format(n))

elif n == 1:
    print("{} argument:\n{}: {}".format(n, n, sys.argv[0]))

else:
    print("{} arguments:".format(n))
    for i in range(0, n):
        print("{}: {}".format(i+1, sys.argv[i]))
