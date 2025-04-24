"""
This is pratice for the finale exam
"""

def foo(loi:list) -> set:
    """ This function processes a given list of integer values as follows: it considers only numbers that are divisible by 7 and then squares them. The output is reversely sorted, (i.e., largest item 1st), and does not contain any duplicates. """
    losi = []
    logi = [i for i in loi if i % 7 == 0]
    for i in logi:
        losi.append(i*i)
    result = set(losi)
    final = sorted(result, reverse=True)
    return final

def bar(string:str) -> int:
    """ This function finds the number of case-sensitive vowels that appear only once in the provided string. """
    result = 0
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        if string.count(vowel) == 1:
            result += 1
    return result

def baz(d:dict, v:int) -> tuple[int]:
    """ This function will do a reverse lookup on a provided dictionary, with the provided value. """
    return tuple([i for i in d if d[i] == v])

def qux(number:int) -> int:
    """ This function calculates the sum of the digits of a given integer. """
    result = 0
    son = str(number)
    for number in son:
        result += int(number[-1])
    return result