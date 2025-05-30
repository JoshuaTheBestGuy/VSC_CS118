"""
This is an example of how to program something that only accepts numbers
Arthur: Joshua Hendrickson, with the help of Copilot
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
Arthur: Joshua Hendrickson with the help of Copilot. 
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
        print(f"{k} is NOT prime, it's divisible by 2.")
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
Is the number the user inputted a valid number? If not, loop until a valid number has been inputted. 
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
More lists! Neighbor wars?
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

while max_roll_counter != 6:
    while len(my_set) < 6:
        dice = randint(1,6)
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

for i in range(1000):
    dice = randint(1,6)
    tally[dice] = tally[dice] + 1
print(tally)

m = max(tally.values())

for k,v in tally.items():
    if v == m:
        print(f"'{k}' was rolled '{v}' times!")
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


"""
Sum of every other item in a random number sorted representation
"""

"""
from random import randint

random_list = []
n = 1000
k = 6

for _ in range(n):
    random_list.append(randint(1,k))
random_list.sort()

print(sum(random_list[::2]))
"""


"""
Rolling a dice... again.. and again
"""

"""
from random import randint

my_set = set()
counter = 0

while len(my_set) < 6:
    dice = randint(1,6)
    counter += 1
    my_set.add(dice)
print(f"Needed '{counter}' rolls.")
"""

"""
Practice with functions
"""

'''
def max_of_three(x:int, y:int, z:int) -> int:
    """ This function will return the max value of three values """
    lst = [x,y,z]
    return max(lst)

def multiply(lst:list[int]) -> int:
    """ This function will multiply all the integers in a list and return the result """
    result = 1
    for i in lst:
        result *= i
    return result if lst else 0

def squared(lst:list[int]) -> list[int]:
    """ This function will square all the integers in a list and return a new list with those squared values """
    squared_list = []
    for i in lst:
        squared_list.append(i*i)
    return squared_list
'''


"""
Functions calling themselves
"""

'''
def factorial(x:int) -> int:
    #print(f"func called with: {x}")
    if x == 0:
        return 1
    result = x * factorial(x-1)
    #print(f"func called with {x} returns {result}")
    return result

def is_palindrome(s: str) -> bool:
    s = s.strip()
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

def r_sum(x:int) -> int:
    """ Returns the sum of all integers 1 to x inclusively. """
    if x == 1:
        return 1
    result = x + r_sum(x-1)
    return result

numbers = [i for i in range (1,1001)]
numbers = list(range(1,1001)) # same effect

numbers = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
result = [i for i in numbers if i % 2 == 1]
'''


"""
Learning about mapping
"""

'''
from math import sqrt

words = ["231", "20", "-45", "99"]
sq = list(map(sqrt, map(abs, map(int, words))))
print(sq)
'''


"""
Reading a CSV file
"""

'''
#def my_filter(k:int) -> bool:
#    return k > 15

def get_numbers(file_name:str) -> list[int]:
    """ Reads a file containing CSV """
    try:
        with open(file_name) as file:
            los = file.read().strip().split(',')
            loi = list(map(int,los))
            fl = filter(lambda k:k > 15,loi)
            return sorted(fl)
    except OSError as err:
        print(err)
        exit(1)
print(get_numbers("numbers.csv"))
'''

"""
Practice
"""

'''
loi = [1, 2, 1, 2]

print(list(map(lambda x: x*3,loi)))
print([i*3 for i in loi])
'''


"""
Functions and more!
"""

'''
def item_sum(lst: list) -> int:
    """ Sum of all integers in the list(s) """
    total = 0
    for i in lst:
        total += i if isinstance(i, int) else item_sum(i)
    return total
print(item_sum([1, 2, 3, [10, 20, 30, [100, 200]], 4, 5]))

def is_power_of_three(n: int) -> bool:
    pot = [1, 3]
    while pot[-1] <= n:
        pot.append(pot[-1]*3)
    return n in pot
print(is_power_of_three(27))

def dict_transform(d: dict, f: callable) -> dict:
    for k, v in d.items():
        d[k] = f(v)
    return d
print(dict_transform({'a': 2, 'b':3}, lambda x: x*2))
'''


"""
Global variables?
"""

'''
def fibonacci(x: int) -> int:
    """ Returns the xth fibonacci number """
    global call_counter
    call_counter += 1
    return x if x <= 1 else fibonacci(x - 1) + fibonacci(x - 2)

call_counter = 0
print(fibonacci(20))
print(f"The function 'fibonacci' was called '{call_counter:,}' times.")
'''

"""

"""

s = 0
for i in range(3,1,-1):
        s-=i
print(s)