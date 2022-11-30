#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            num = "Fizz"
        elif num % 5 == 0 and num % 3 != 0:
            num = "Buzz"
        elif num % 5 == 0 and num % 3 == 0:
            num = "FizzBuzz"
        print(num, end=" ")

fizzbuzz()
