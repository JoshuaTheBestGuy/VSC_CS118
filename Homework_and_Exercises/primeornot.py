"""
The purpose of this program is to determine if any number above 1 is a prime number or not.
Written by Joshua Hendrickson with the help of Copilot.
"""

print("This is a program that will determine if your number of choice is a prime number or not.")

while True:
    inputnumber = input("Please enter any number above 1: ")
    int_inputnumber = int(inputnumber)
    if int_inputnumber > 1:
        is_prime = True
        lowest_divisor = None
        for i in range(2, int(int_inputnumber**0.5) + 1):
            if int_inputnumber % i == 0:
                is_prime = False
                lowest_divisor = i
                break
        if is_prime:
            print(f"{int_inputnumber} is a prime number!")
        else:
            print(f"{int_inputnumber} is not a prime number because it's lowest divisor is {lowest_divisor}.")
    else:
        print(f"{int_inputnumber} is not a prime number.")
        break
        