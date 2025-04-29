from collections import Counter

"""
This is the final exam assignment, which requires implementing 4 functions
Author: Joshua Hendrickson with the help of Copilot
"""

def alpha(input: str) -> list:
    """ 
    This function processes a given string, counting vowels (a, e, i, o, u), ignoring case. 
    The output is a list containing the vowel or vowels that appear most frequently in the string. 
    The returned list is sorted, in lowercase, with no duplicates.
    Disclaimer: AI was used in this function.
    """
    lower = input.lower()
    vowels = "aeiou"
    vowel_counts = Counter(char for char in lower if char in vowels)
    if not vowel_counts:
        return []
    max_count = max(vowel_counts.values())
    result = sorted([vowel for vowel, count in vowel_counts.items() if count == max_count])
    return result


def beta(number:int) -> int:
    """ 
    This function processes a given integer, calculates the sum of those digits that are less than the average of its digits. 
    Disclaimer: AI was NOT used in this function.
    """
    result = 0
    average = 0
    son = str(number)
    for number in son:
        average += int(number[-1])
    average = average / len(son)
    for number in son:
        if int(number[-1]) < average:
            result += int(number[-1])
    return result

def gamma(loi: list[int]) -> int | None:
    """
    This function processes a given list of integer values. 
    It finds the 2nd largest of those integers that appear only once in the list.
    Disclaimer: AI was used in this function.
    """
    unique_elements = [num for num, count in Counter(loi).items() if count == 1]
    if len(unique_elements) < 2:
        return None
    return sorted(unique_elements, reverse=True)[1]

def delta(los: list[str]) -> list:
    """
    This function processes a list of strings. 
    It returns a list, containing only those strings that are all uppercase and at least 6 characters long.
    Disclaimer: AI was used in this function.
    """
    return [s for s in los if s.isupper() and len(s) >= 6]
