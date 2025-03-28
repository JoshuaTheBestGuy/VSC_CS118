"""
Rolling a dice... again... and again?
"""

from random import randint
import time

start_time = time.perf_counter()
my_list = list()
current_counter = 1
max_roll_counter = 0
attempts = 1
print_attempt = int(1)
highest_counter = 0

number = input("How high should we go today?: ")
do_print = input("Should we include print statements on every attempt? (not recommended for high input!) Please select True or False: ")
do_print = do_print.lower()

while True:
    if number.isnumeric() == True:
        number = int(number)
        break
    else:
        print(f"{number} is not a valid number!")
        number = input("Please enter a number: ")

while True:
    if do_print == "true":
        do_print = True
        break
    elif do_print == "false":
        do_print == False
        break
    else: 
        print(f"{do_print} is not a valid boolean statement.")
        do_print = input("Please select True or False: (not recommended for high input!): ")
        do_print = do_print.lower()

while max_roll_counter != number:
    while len(my_list) < number:
        dice = randint(1,number)
        if dice == current_counter:
            current_counter += 1
            my_list.append(dice)
            max_roll_counter += 1
            if do_print is True and print_attempt == 1_000_000:
                print(f"You rolled {dice}! Size of the set is {len(my_list)}.")
        else:
            if max_roll_counter > highest_counter:
                highest_counter = max_roll_counter
            if do_print is True and print_attempt == 1_000_000:
                print(f"You rolled {dice}! That is not a perfect combination! I have completed {attempts} attempts. The highest you got to was {highest_counter}.")
            if print_attempt == 1_000_000:
                print_attempt = 0
            attempts += 1
            print_attempt += 1
            my_list = list()
            current_counter = 1
            max_roll_counter = 0
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"It took {attempts} attempts to get a perfect combination of rolls. It took {elapsed_time:.4f} seconds.")