"""
This program will generate random numbers from 1 to n, until all intergers 1 to n have been generated at least once. 
Written by Joshua Hendrickson with the help of Copilot.
"""

from random import randint

print("Creating all integers from 1 to n (inclusive) randomly.")

x = input("Enter the first number, or 'q' to quit: ") # asks the user for their number

# lines 13 through 23 check if the user has entered a valid number, if they have not, the loop will contiune until they have. Or the program will quit if the user enters 'q'.
if x == "q":
    quit()
else:
    while True:
        if x.isnumeric() == True:
            x = int(x)
            check_list_digit = x
            break
        else:
            print(f"{x} is not a valid number!")
            x = input("Please enter a number: ")

# needed vars
list = list()
ran_counter = 1
check_list = []
most_frequent_number = None
previous_number = None
current_streak = 0
max_streak = 0

# this while loop is fundamental to the sucesful use of the program. It will create a list of all the digits from 1 to x, serving as a "check list" that the program can use to check if the list that is used to store the random numbers includes all of the numbers from 1 to x. 
while True:
    check_list_digit = int(check_list_digit)
    check_list.append(check_list_digit)
    check_list_digit -= 1
    if check_list[-1] == 1:
        break
    else:
        continue

# this is the core of the program, first getting a random number from 1 to x, then putting that number in the list. Then, it will determine the streaks of the random numbers. Then, it will check if the list of random int's includes all the numbers from the "check list", if it does it will print out the end statements and the program will end, if it does not, it will carry on the loop, adding to the total number of times the program has been run.  
while True:
    random_result = randint(1,x)
    list.append(random_result)

    if random_result == previous_number:
        current_streak += 1
    else:
        current_streak = 1
        previous_number = random_result

    if current_streak > max_streak:
        max_streak = current_streak
        most_frequent_number = random_result

    if all(item in list for item in check_list) == True:
        print() # creating space between the lines, purely a style choice
        print(f"The function 'ranint' was called {ran_counter} times!")
        print(f"The last number called was {list[-1]}!")
        print(f"The most frequent number was {most_frequent_number} with a max streak of {max_streak}!")
        print(list)
        print() # creating space between the lines, purely a style choice
        break
    else:
        previous_number = random_result
        ran_counter += 1
        continue