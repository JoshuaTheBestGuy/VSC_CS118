"""
This program will define a function which will find all numbers less than 1000 and divisible by 11, then determine which of those numbers contain the most '1' digits.
Author: Joshua Hendrickson with the help of Copilot
"""

def the_11_numbers() -> list[int]:
    result = []
    for i in range(1,1000):
        if i % 11 == 0:
            result.append(i)
    return result

numbers = the_11_numbers()

print(f"There are '{len(the_11_numbers())}' '11' numbers.")\

max_count_of_ones = max(str(num).count('1') for num in numbers)
numbers_with_most_ones = [num for num in numbers if str(num).count('1') == max_count_of_ones]

print(f"The 11-numbers with the most '1's are: {numbers_with_most_ones}.")