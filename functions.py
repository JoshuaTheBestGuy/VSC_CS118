"""
My Functions
Author: Joshua Hendrickson
"""

def is_odd(k:int) -> bool:
    """ Returns True if 'k' is odd """
    return k % 2 == 1

def is_even(k:int) -> bool:
    """ Returns True if 'k' is even """
    return not is_odd(k)

def summation(a:int, b:int) -> bool:
    """ Returns the sum of all values 'a' to 'b' """
    result = 0
    for i in range(a,b+1):
        result += i
    return result