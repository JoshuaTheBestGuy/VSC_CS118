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


