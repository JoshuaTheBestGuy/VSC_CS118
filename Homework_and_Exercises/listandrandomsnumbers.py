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
    while True:
        if x.isnumeric() == True:
            break
        else:
            print(f"{x} is not a valid number!")
            x = input("Please enter a number: ")

