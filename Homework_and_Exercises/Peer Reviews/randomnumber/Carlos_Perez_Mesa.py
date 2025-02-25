"""List and random numbers Write a Python program that generates random numbers 1 to n (inclusive), until all integers 1 to n have been generated at least once.
Author: Carlos perez-mesa"""

import random

print('Creating all integers from 1 to n (inclusive) randomly.')

while True:
    n = ''
    while type(n) != int and n != 'q':
        n = (input("Please enter a number, or 'q' to quit: "))
        try:
            n = int(n)
            break
        except:
            pass
    if n == 'q':
        break

    full_arr = []
    arr  = []
    count = 0
    while len(arr) < n:
        gen_num = random.randint(1,n)
        full_arr.append(gen_num)
        count += 1
        if gen_num not in arr:
            arr.append(gen_num)

    best = 0
    best_num = 0
    counter = 0
    for i in range(1,len(full_arr)):
        if full_arr[i] == full_arr[i-1]:
            if counter == 0:
                counter = 2
            else:
                counter += 1
        else:
            counter = 0
        if counter > best:
            best_num = full_arr[i]
            best = counter

    print(f"Creating a random sequence of all integers 1 .. {n} required {count} randint(1,{n}) calls.")
    print(f"The integer that was created last was {arr[-1]}.")
    print(f"The integer that was created the most times in a row, {best} times, was {best_num}.")
    print(arr)
