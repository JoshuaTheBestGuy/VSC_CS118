"""
This program will create a list of all numbers 7 to 777 (meaning 7 and 777 are included in the interval) that are divisible by 7 and NOT divisible by 10. Print the 10th number, and print the sum of every 7th number in the list.
Author: Joshua Hendrickson
"""

hepta = []
candidates = list(range(7,777+1))

for number in candidates:
    if number % 7 == 0 and number % 10 != 0:
        hepta.append(number)

print(f"The 10th hepta number is {hepta[9]}.")
print(f"The sum of every seventh hepta number is {sum(hepta[::7])}.")