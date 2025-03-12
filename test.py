"""
This is an example of how to program something that only accepts numbers
Authur: Joshua Hendrickson, with the help of Copilot
"""

"""

x = input("Enter the first number: ")

try:
    x = int(x)
except ValueError:
    print("You did not enter a number.")
    while True:
        x = input("Enter another number: ")
        try:
            x = int(x)
            break
        except ValueError:
            print("You did not enter a number.")

y = input("Enter the second number: ")

try:
    y = int(y)
except ValueError:
    print("You did not enter a number.")
    while True:
        y = input("Enter another number: ")
        try:
            y = int(y)
            break
        except ValueError:
            print("You did not enter a number. You are an idiot.")

s = int(x) + int(y)

print(f"The sum of {x} and {y} is {s}")

"""


"""
This is an example of how to program a rectangular prism.
Authur: Joshua Hendrickson with the help of Copilot. 
"""

"""
print("This program will calculate the properties of a rectangular prism.")
sw = input("Enter the width of the prism: ")
sh = input("Enter the height of the prism: ")
sl = input("Enter the length of the prism: ")

width = float(sw)
height = float(sh)
length = float(sl)

volume = width * height * length
sa = 2 * width * height + 4 * length * height

print(f"The volume of the prism is {volume}")
print(f"The surface area of the prism is {sa}")
"""

"""
English to Pig Latin
"""

"""

from sys import argv

# s = input("Please enter an English sentence: ")
result = ""
words = argv[1:]
for word in words:
    word = word + "-"
    if word[0] in "AEIOUaeiou":
        word += "yay"
    else:
        word += word[0]
        word += "a"
        word = word[1:]
    result += word + " "
print(result)
    
"""


"""
Multi-Way If Statements
"""

"""

number = int(input("Enter the numeric grade: "))
if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'
print(f"The letter grade is {letter}.")

"""


"""
Super Prime Checker
"""

"""
while True:
    k = int(input("What number do you want me to check for prime?: "))
    if k <= 1:
        break
    if k == 2:
        print(f"{k} is a prime number!")
    elif k % 2 == 0:
        print(f"{k} is NOT prime, it's divisbile by 2.")
    for i in range (3,int(1 + k ** 0.5),2): # 3, 5, 7, ... k-1
        print(i)
        if k % i == 0:
            print(f"{k} is NOT prime, it's divisible by {i}.")
            break
    else:
        print(f"{k} is a prime number!")
"""


"""
while True:
    k = input("Enter a number: ")
    print(k.isnumeric())
"""

"""
my_string = "12,34,22,11,45656,12121,11!"
print(my_string.split(','))
"""


"""
Reading a good book
"""


"""
with open("treasure.txt") as my_book:
    text = my_book.read()

print(len(text))
lc_book = text.lower()
print(text.count("rum"))
print(lc_book.count("rum"))
"""


"""
Is the number the user inputed a valid number? If not, loop until a valid number has been inputed. 
"""

"""
x = input("Please enter a number: ")

while True:
    if x.isnumeric() == True:
        break
    else:
        print(f"{x} is not a valid number!")
        x = input("Please enter a number: ")

print(x)
"""


"""
Roll a dice 10 times, store those results in a list
"""

"""
from random import randint

roll_count = 0
value_list = []

while True:
    if roll_count == 10:
        print(value_list)
        break
    else: 
        value_list.append(randint(1,6))
        roll_count += 1
"""


"""
Roll a dice until all values 1 to 6 have been rolled at least once
"""

"""
from random import randint

value_list = []
run_count = 0
total_sum = 0

while len(value_list) != 6:
    x = randint(1,6)
    total_sum += x
    run_count += 1
    if x not in value_list:
        value_list.append(x)
        x = 0
print(value_list)
print(f"randint was run {run_count} times!")
print(f"The sum of all the generated numbers was {total_sum}!")
"""


"""
Lists, lists, and more lists!
"""

"""
main_street = ["Smith", "Johnson", "Garcia", "Miller", "Lopez"]

for name in main_street:
    print(name, end="")
print()
for idx in range(0, len(main_street),2): # 0, 2, 4
    print(main_street[idx], end=", ")
print()
for idx in range(len(main_street)): # 0, 1, 2, 3, 4
    print(f"{main_street[idx]} ({idx + 1} Main Street), ", end="")
"""


"""
More lists! Neighboor wars?
"""

"""
main_street = ["Smith", "Johnson", "Garcia", "Miller", "Lopez"]

i = main_street.index("Johnson")
j = main_street.index("Miller")
main_street[i],main_street[j] = main_street[j], main_street[i]
print(main_street)
"""


"""
Separate positive and negative numbers with lists
"""

"""
from random import randint

value_list = []
positive_list = []
negative_list = []

while len(value_list) != 9:
    x = randint(-10,10)
    if x not in value_list:
        value_list.append(x)
    if x > 0:
        positive_list.append(x)
    if x < 0:
        negative_list.append(x)
print(value_list)
print(positive_list)
print(negative_list)
"""


"""
Messing with text files
"""

"""
from random import randint

lorn = []
for i in range(500):
    lorn.append(randint(1,500))

with open("numbers.txt","w") as f:
    for r in lorn:
        f.write(f"{r}\n")

with open("numbers.txt") as f:
    content = f.read()

l2 = []
for s in content.split():
    l2.append(int(s))

assert lorn == l2
"""

"""
Still messing with text files
"""

"""
with open("treasure.txt") as f:
    content = f.read()

words = content.split()
print(words)

doc_string = not here due to errors

with open("test.py") as f: 
    code = f.read()
print(code)

with open("test.py", "w") as f:
    f.write(doc_string)
    f.write(code)
print("Done.")
"""


"""
Rolling a dice... again
"""

"""
from random import randint

my_set = set()
counter = 0
max_roll_counter = 0
attempts = 0

while max_roll_counter != 10:
    while len(my_set) < 10:
        dice = randint(1,10)
        counter += 1
        my_set.add(dice)
        print(f"You rolled {dice}! Size of the set is {len(my_set)}.")
    print(f"Needed {counter} rolls.")
    max_roll_counter = counter
    counter = 0
    my_set = set()
    attempts += 1
print(f"It took {attempts} attempts to get a perfect combination of rolls.")
"""


"""
Are dice truly perfect? Dictionaries demo
"""

"""
from random import randint

tally = {}

for i in range(1,7): #1, 2, .. 6
    tally[i] = 0

for i in range(6000):
    dice = randint(1,6)
    tally[dice] = tally[dice] + 1
print(tally)

for k,v in tally.items():
    print(f"{k} -> {v}")
"""


"""
Most frequent word in Treasure Island
"""

"""
from string import punctuation

punctuation += '\n'
clean_text = ""

with open("treasure.txt") as file:
    book = file.read()

for c in book:
    clean_text += c.lower() if c not in punctuation else " "
words = clean_text.split()

tally = {}
for word in words:
    tally[word] = tally.get(word, 0) + 1

frequencies = list(tally.values())
frequencies.sort()
max_frequency = frequencies[-1]
for k,v in tally.items():
    if v == max_frequency:
        print(f"Max Freq. used word is '{k}'... used {v} amount of times.")
"""