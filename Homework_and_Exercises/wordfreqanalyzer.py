"""
This program will ask the user to enter a number to find words that appear that many times in a user selected text file.
Author: Joshua Hendrickson with the help of Copilot
"""

from string import punctuation

punctuation += '\n'
clean_text = ""

text_file = input("Enter the file path or name to a text file: ")
extension = text_file.split(".")

while True:
    if extension[-1] == "txt":
        break
    else:
        print(f".{extension[-1]} is not a valid extension for this program. Please enter a text file ending in .txt.")
        text_file = input("Enter the file path or name to a text file: ")
        extension = text_file.split(".")
        continue

try:
    with open(text_file) as file:
        book = file.read()

except OSError as x:
    print(x)

else:
    for c in book:
        clean_text += c.lower() if c not in punctuation else " "
    words = clean_text.split()
    
    tally = {}
    for word in words:
        tally[word] = tally.get(word, 0) + 1
    
    while True:
        user_input = input("Enter a number n (or q to quit) to find the word(s) appearing n times in the text: ")
        if user_input == "q":
            quit()
        elif user_input.isnumeric():
            user_input = int(user_input)
            found = False
            for k, v in tally.items():
                if v == user_input:
                    print(f"'{k}' appeared in '{text_file}', {user_input} times.")
                    found = True
            if not found:
                print(f"No words appeared in '{text_file}', {user_input} time(s)... sorry!")
        else:
            print(f"{user_input} is not a valid number!")