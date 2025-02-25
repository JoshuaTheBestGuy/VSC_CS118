""" Random Number 
    Author; Mattea Gallon 
"""
from random import randint

print("Creating all integers from 1 to n (inclusive) randomly.")
user_input = input("Please enter a number, or 'q' to quit: ")
if (user_input == 'q'):
    exit()
user_input = int(user_input)

print(f"Creating a random sequence of all integers 1 .. {user_input}", end=" ")
found_numbers = []
past_x = 0
current_times_appeared = 0
number_appeared = 0
times_appeared = 0
count = 0
x = 0

while(len(found_numbers) < user_input):
    x = randint(1, user_input)
    
    if (past_x == x):
        current_times_appeared = current_times_appeared + 1
        if (times_appeared <= current_times_appeared):
            number_appeared = x
            times_appeared = current_times_appeared
    else:
        current_times_appeared = 1

    past_x = x

    if (x not in found_numbers):
        found_numbers.append(x)

    count = count + 1

print(f"required {count} randint(1,{user_input}) calls.")
print(f"The integer that was created last was {x}.")
print(f"The integer that was created the most times in a row, {times_appeared} times, was {number_appeared}.")
print(found_numbers)