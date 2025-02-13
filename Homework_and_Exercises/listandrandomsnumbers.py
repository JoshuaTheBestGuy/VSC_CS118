"""
This program will generate random numbers from 1 to n, until all intergers 1 to n have been generated at least once. 
Written by Joshua Hendrickson
"""

from random import randint

print("Creating all integers from 1 to n (inclusive) randomly.")

x = input("Enter the first number, or 'q' to quit: ")

if x == "q":
    quit
else:
    try:
        x = int(x)
    except ValueError:
        print("You did not enter a number.")
        while True:
            x = input("Enter another number: ")
            try:
                x = int(x)
                break
            except ValueError:
                print("You did not enter a number.")
