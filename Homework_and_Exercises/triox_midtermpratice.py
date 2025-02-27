"""
This is pratice for the midterm
"""

candidates = list(range(3,333+1,3))
triox = []
for number in candidates:
    if number % 3 == 0 and number % 7 != 0:
        triox.append(number)

print(len(candidates))
print(len(triox))
print(f"The 33rd triox number is {triox[32]}.")

print(f"The sum of every third triox number is {sum(triox[::3])}.")