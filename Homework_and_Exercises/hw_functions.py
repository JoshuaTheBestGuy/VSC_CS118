"""
This program will define two functions one being the mode of a list, and the other function will do a reverse lookup on a provided dictionary, with the provided value. 
Author: Joshua Hendrickson
"""

def rev_lookup(d:dict, v:int) -> tuple[int]:
    """ This function will do a reverse lookup on a provided dictionary, with the provided value. """
    result = []
    for i in d:
        if d[i] == v:
            result.append(i)
    return tuple(result) 

def mode(x:list[int]) -> tuple[int]:
    """ This function will accept a list of integers as input and return a tuple, containing the mode of the list. """
    tally = {}
    result = []
    for number in x:
        tally[number] = tally.get(number, 0) + 1
    frequencies = list(tally.values())
    frequencies.sort()
    max_frequency = max(frequencies)
    result = rev_lookup(tally, max_frequency)
    return tuple(result)