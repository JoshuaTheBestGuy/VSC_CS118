"""
This program will house all of the functions required for my blackjack program.
Author: Joshua Hendrickson
"""

from random import randint

deck = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
user_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
dealer_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
user_cards = []
user_value = 0
dealer_cards = []
dealer_value = 0

def hit(deck: dict, cards: list, value: int, deck_values: dict, ha: int):
    for _ in range(1,ha+1):
        last_card = randint(1,13)
        while True: # this will check if the card is actually in the deck, if it's not it will get a new card
            if deck[(last_card)] > 0:
                break
            else:
                last_card = randint(1,13)
        # these next few if / elif statements will give you what card you got and remove it from the deck
        if last_card == 1: 
            cards.append("A")
            deck[1] -= 1
            last_card = "A"
            value += deck_values["A"]
        elif last_card == 11:
            cards.append("J")
            deck[11] -= 1
            last_card = "J"
            value += deck_values["J"]
        elif last_card == 12:
            cards.append("Q")
            deck[12] -= 1
            last_card = "Q"
            value += deck_values["Q"]
        elif last_card == 13:
            cards.append("K")
            deck[13] -= 1
            last_card = "K"
            value += deck_values["K"]
        else:
            cards.append(last_card)
            deck[(last_card)] -= 1
            value += deck_values[(last_card)]
    return deck, cards, last_card, value, deck_values

deck, dealer_cards, last_card, dealer_value, dealer_deck_values = hit(deck, dealer_cards, dealer_value, dealer_deck_values, 2)
print(deck)
print(dealer_cards)
print(last_card)
print(dealer_value)
print(dealer_deck_values)