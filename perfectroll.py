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
highest_counter = 0

while max_roll_counter != 8:
    while len(my_list) < 8:
        dice = randint(1,8)
        if dice == current_counter:
            current_counter += 1
            my_list.append(dice)
            max_roll_counter += 1
            print(f"You rolled {dice}! Size of the set is {len(my_list)}.")
        else:
            if max_roll_counter > highest_counter:
                highest_counter = max_roll_counter
            print(f"You rolled {dice}! That is not a perfect combination! You got up to {max_roll_counter}... so close.. or not? The highest you got to was {highest_counter}.")
            attempts += 1
            my_list = list()
            current_counter = 1
            max_roll_counter = 0
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"It took {attempts} attempts to get a perfect combination of rolls. It took {elapsed_time:.4f} seconds.")
