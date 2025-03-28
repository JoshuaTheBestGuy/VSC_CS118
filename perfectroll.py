"""
Rolling a dice... again... and again?
"""

from random import randint
import time

start_time = time.perf_counter()
my_list = []
average_time_list = []
average_attempt_list = []
current_counter = 1
max_roll_counter = 0
attempts = 1
highest_counter = 0
runs_completed = 0

number = input("How high should we go today?: ")
runs_input = input("How many runs should we do?: ")
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
    if runs_input.isnumeric() == True:
        runs_input = int(runs_input)
        break
    else:
        print(f"{runs_input} is not a valid number!")
        runs_input = input("Please enter a number: ")

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

while runs_completed < runs_input:
    start_time_run = time.perf_counter()
    while max_roll_counter != number:
        while len(my_list) < number:
            dice = randint(1,number)
            if dice == current_counter:
                current_counter += 1
                my_list.append(dice)
                max_roll_counter += 1
                if do_print is True:
                    print(f"You rolled {dice}! Size of the set is {len(my_list)}.")
            else:
                if max_roll_counter > highest_counter:
                    highest_counter = max_roll_counter
                if do_print is True:
                    print(f"You rolled {dice}! That is not a perfect combination! You got up to {max_roll_counter}... so close.. or not? The highest you got to was {highest_counter}.")
                attempts += 1
                my_list = []
                current_counter = 1
                max_roll_counter = 0
    end_time_run = time.perf_counter()
    elapsed_time_perrun = end_time_run - start_time_run
    average_time_list.append(elapsed_time_perrun)
    average_attempt_list.append(attempts)
    if do_print is True:
        print(f"It took {attempts} attempts to get a perfect combination of rolls. It took {elapsed_time_perrun:.4f} seconds.")
    current_counter = 1
    max_roll_counter = 0
    my_list = []
    attempts = 1
    highest_counter = 0
    runs_completed += 1

end_time = time.perf_counter()
elapsed_time = end_time - start_time
average_time_list.sort()
average_attempt_list.sort()
print(f"\n{runs_completed} runs completed. It took '{elapsed_time:.4f}' seconds total. The average time for each run was '{sum(average_time_list) / len(average_time_list)}' The average attempt took '{int(sum(average_attempt_list) / len(average_attempt_list))}' attempts to get a perfect roll of up to {number}.")
print(f"The quickest attempt took '{average_time_list[0]}' while the longest attempt took '{average_time_list[-1]}'.")
print(f"The least attempts taken in a run was '{average_attempt_list[0]}' while the most attempts taken was '{average_attempt_list[-1]}'.\n")