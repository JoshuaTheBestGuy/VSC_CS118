"""
This is a program that calculates the properties of a squared pyramid.
Authur: Joshua Hendrickson. 
"""

print("This program will calculate the properties of a squared pyramid.")
basel = input("Please enter the base length: ")
h = input("Please enter the height: ")


length = float(basel)
height = float(h)


sa = (length ** 2) + (2 * length) * ((((length ** 2) / 4) + (height ** 2)) ** 0.5)
volume = (length ** 2) * (height / 3)

print(f"The surface area of this squared pyramid is {sa} squared inches!")
print(f"The volume of this squared pyramid is {volume} cubic inches!")