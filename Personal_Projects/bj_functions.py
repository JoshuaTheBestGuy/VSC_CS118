"""
This program will house all of the functions required for my blackjack program.
Author: Joshua Hendrickson
"""

from random import randint

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