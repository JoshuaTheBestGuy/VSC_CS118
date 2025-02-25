"""This program will generate integers from 1 to an input number randomly, giving a few statistics about how it got there
Made by Alexander Gagaza, alone and unafraid."""

from random import randint

y = 0
print("Creating all integers from 1 to n (inclusive) randomly.")
y = (input("Please enter a number, or 'q' to quit: "))
while y != 'q':
    mylist = []
    last = 0
    counter = 0
    y = int(y)
    frequency = [0,y]
    while [1,y] not in mylist:
        
        z = randint(1,y+1)
        counter += 1
        if z not in mylist:
            mylist.append(z)
            if z == last:
                e = frequency[z]
                e += 1
                frequency.insert(z,e)
            elif z != last:
                frequency.insert(z,1)
                last = z
        r = str(max(frequency))
        
    
    print(f"Creating a random sequence of all integers 1 to {y} required {counter} randint(1,{y}) calls.")
    print(f"The integer that was created last was {z}.")
    print(f"The integer that was created the most times in a row, {max(frequency)} times, was {frequency.index(max(frequency))}.")
    print(mylist)
    y = (input("Please enter a number, or 'q' to quit: "))

