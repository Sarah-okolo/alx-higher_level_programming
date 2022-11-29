#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
numstr = repr(number)
lastNum = numstr[-1:]
lastNum = int(lastNum)
print(f"Last digit of {number:d} is {lastNum:d}", end=" ")

if lastNum > 5:
    print("and is greater than 5")

elif lastNum == 0:
    print("and is 0")

elif lastNum < 6 and lastNum != 0:
    print("and is less than 6 and not 0")
