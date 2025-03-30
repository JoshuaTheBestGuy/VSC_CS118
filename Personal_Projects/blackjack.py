"""
This program will simulate a game of blackjack. The game will record your high score, and store it in a separate file. 
Author: Joshua Hendrickson, alone and unafraid.
Date Work Began: 03/29/2025
"""

from random import randint

user_money = 500
deck = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
user_cards = []
dealer_cards = []
bust = False
last_card = None

print("Welcome to blackjack!")

bet = input("Please place your bet, or 'q' to exit the casino: ")

while True:
    if bet == "q":
        exit()
        # record high score
        break
    else:
        if bet.isnumeric == True:
            bet = int(bet)
            continue
        elif bet.isnumeric() == False:
            print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
            bet = input("Please place your bet, or 'q' to exit the casino: ")
        elif bet == "0":
            print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
            bet = input("Please place your bet, or 'q' to exit the casino: ")
        elif int(bet) > user_money:
            print(f"Your bet of '{bet}' dollars exceeds your total balance of '{user_money}' dollars. Please place a bet above this. ")
            bet = input("Please place your bet, or 'q' to exit the casino: ")
        else:
            print(f"Your bet of '{bet}' dollars has been placed! Good luck!")
            bet = int(bet)
            break

while len(user_cards) < 2:
    last_card = randint(1,13)
    while True: # this will check if the card is actually in the deck, if it's not it will get a new card
        if deck[(last_card)] > 0:
            break
        else:
            last_card = randint(1,13)
    # these next few if / elif statements will give you what card you got and remove it from the deck
    if last_card == 1: 
        print("You got an 'A'!")
        user_cards.append("A")
        deck[1] -= 1
    elif last_card == 11:
        print("You got an 'J'!")
        user_cards.append("J")
        deck[11] -= 1
    elif last_card == 12:
        print("You got an 'Q'!")
        user_cards.append("Q")
        deck[12] -= 1
    elif last_card == 13:
        print("You got an 'K'!")
        user_cards.append("K")
        deck[13] -= 1
    else:
        print(f"You got a {last_card}!")
        user_cards.append(last_card)
        deck[(last_card)] -= 1
    print(f"Your deck currently consists of {user_cards}.")

while len(dealer_cards) < 2:
    last_card = randint(1,13)
    while True: # this will check if the card is actually in the deck, if it's not it will get a new card
        if deck[(last_card)] > 0:
            break
        else:
            last_card = randint(1,13)
    # these next few if / elif statements will give you what card you got and remove it from the deck
    if last_card == 1: 
        dealer_cards.append("A")
        deck[1] -= 1
    elif last_card == 11:
        dealer_cards.append("J")
        deck[11] -= 1
    elif last_card == 12:
        dealer_cards.append("Q")
        deck[12] -= 1
    elif last_card == 13:
        dealer_cards.append("K")
        deck[13] -= 1
    else:
        dealer_cards.append(last_card)
        deck[(last_card)] -= 1

# check for blackjack, check value of cards.... maybe dictionary of values? 

print(f"You begin this round with {user_cards}. The dealer's top card is {dealer_cards[-1]}.") # include values

action = input("Would you like to stand, hit, double-down, or split?: ")
action = action.lower()

while True:
    if action == "stand":
        break
    elif action == "hit":
        break
    elif action == "double-down":
        break
    elif action == "split":
        break
    else:
        print(f"Your action of '{action}' is not a valid action.")
        action = input("Would you like to stand, hit, double-down, or split?: ")