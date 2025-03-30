"""
This program will simulate a game of blackjack. The game will record your high score, and store it in a separate file. 
Author: Joshua Hendrickson, alone and unafraid.
Date Work Began: 03/29/2025
"""

from random import randint

user_money = 500

while True: 
    deck = {1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
    user_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    dealer_deck_values = {"A":11, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10}
    user_cards = []
    user_value = 0
    dealer_cards = []
    dealer_value = 0
    card1_bet = 0
    card2_bet = 0
    card3_bet = 0
    card4_bet = 0
    user_bust = False
    dealer_bust = False
    last_card = None
    blackjack = False
    dealer_changed = False
    user_changed = False
    hit_again = "no"
    print(f"\nWelcome to blackjack! Your current balance is {user_money}.")
    bet = input("Please place your bet, or 'q' to exit the casino: ")
    while True:
        if blackjack == True:
            break
        if bet == "q":
            exit()
            # record high score
            break
        else:
            if str(bet).isnumeric == True:
                bet = int(bet)
                continue
            elif str(bet).isnumeric() == False:
                print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            elif str(bet) == "0":
                print(f"Your bet of '{bet}' dollars is not a valid bet. Please place a bet above '1'.")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            elif int(bet) > user_money:
                print(f"Your bet of '{bet}' dollars exceeds your total balance of '{user_money}' dollars. Please place a bet above this. ")
                bet = input("Please place your bet, or 'q' to exit the casino: ")
            else:
                print(f"Your bet of '{bet}' dollars has been placed! Good luck!")
                bet = int(bet)
                user_money -= bet
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
            user_cards.append("A")
            deck[1] -= 1
        elif last_card == 11:
            user_cards.append("J")
            deck[11] -= 1
        elif last_card == 12:
            user_cards.append("Q")
            deck[12] -= 1
        elif last_card == 13:
            user_cards.append("K")
            deck[13] -= 1
        else:
            user_cards.append(last_card)
            deck[(last_card)] -= 1

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
    for i in range(len(user_cards)):
        user_value += user_deck_values[user_cards[i]]
    for i in range(len(dealer_cards)):
        dealer_value += dealer_deck_values[dealer_cards[i]]
    if user_value == 21:
        blackjack = True
    if blackjack == True:
        print(f"You got {user_cards}, with a value of {user_value}. That's a blackjack, congrats!")
        user_money += bet * 3
    if blackjack == False:
        print(f"You begin this round with {user_cards}, with a value of {user_value}. The dealer's top card is {dealer_cards[-1]}.")
        if user_cards[0] == user_cards[-1]:
            print(f"Split is available because you have two of the same cards!")
        action = input("Would you like to stand, hit, double-down, or split?: ")
        action = action.lower()

        while True:
            if action == "stand":
                print(f"You chose to stand. Good luck!")
                print(f"The dealer has {dealer_cards} with a value of {dealer_value}.")
                while True:
                    if dealer_value > 21:
                        dealer_deck_values["A"] = 1
                        if dealer_changed == False:
                            if "A" in dealer_cards:
                                dealer_value -= 10
                                dealer_changed = True
                        if dealer_value > 21:
                            break
                    if dealer_value >= 17:
                        print("The dealer must stand, good luck!")
                        break
                    else:
                        for i in range(1,2):
                            last_card = randint(1,13)
                            while True: # this will check if the card is actually in the deck, if it's not it will get a new card
                                if deck[(last_card)] > 0:
                                    break
                                else:
                                    last_card = randint(1,13)
                            # these next few if / elif statements will give you what card you got and remove it from the deck
                            if last_card == 1: 
                                dealer_cards.append("A")
                                dealer_value += dealer_deck_values["A"]
                                deck[1] -= 1
                                last_card = "A"
                            elif last_card == 11:
                                dealer_cards.append("J")
                                dealer_value += dealer_deck_values["J"]
                                deck[11] -= 1
                                last_card = "J"
                            elif last_card == 12:
                                dealer_cards.append("Q")
                                dealer_value += dealer_deck_values["Q"]
                                deck[12] -= 1
                                last_card = "Q"
                            elif last_card == 13:
                                dealer_cards.append("K")
                                dealer_value += dealer_deck_values["K"]
                                deck[13] -= 1
                                last_card = "K"
                            else:
                                dealer_cards.append(last_card)
                                dealer_value += dealer_deck_values[(last_card)]
                                deck[(last_card)] -= 1
                    print(f"The dealer got a {last_card}, for a total value of {dealer_value}.")
                break
            elif action == "hit" or hit_again == True:
                while True:
                    print(f"You chose to hit. Good luck!")
                    if user_value > 21:
                        user_deck_values["A"] = 1
                        if user_changed == False:
                            if "A" in user_cards:
                                user_value -= 10
                                user_changed = True
                        if user_value > 21:
                            print(f"You went over '21' and busted with a value of {user_value}.")
                            break
                    elif user_value == 21:
                        print(f"You hit '21', good luck!")
                        break
                    else:
                        for i in range(1,2):
                            last_card = randint(1,13)
                            while True: # this will check if the card is actually in the deck, if it's not it will get a new card
                                if deck[(last_card)] > 0:
                                    break
                                else:
                                    last_card = randint(1,13)
                            # these next few if / elif statements will give you what card you got and remove it from the deck
                            if last_card == 1: 
                                user_cards.append("A")
                                user_value += user_deck_values["A"]
                                deck[1] -= 1
                                last_card = "A"
                            elif last_card == 11:
                                user_cards.append("J")
                                user_value += user_deck_values["J"]
                                deck[11] -= 1
                                last_card = "J"
                            elif last_card == 12:
                                user_cards.append("Q")
                                user_value += user_deck_values["Q"]
                                deck[12] -= 1
                                last_card = "Q"
                            elif last_card == 13:
                                user_cards.append("K")
                                user_value += user_deck_values["K"]
                                deck[13] -= 1
                                last_card = "K"
                            else:
                                user_cards.append(last_card)
                                user_value += user_deck_values[(last_card)]
                                deck[(last_card)] -= 1
                            if user_value > 21:
                                user_deck_values["A"] = 1
                                if user_changed == False:
                                    if "A" in user_cards:
                                        user_value -= 10
                                        user_changed = True
                                if user_value > 21:
                                    user_bust = True
                            print(f"You got a {last_card}, the values of your cards is {user_value}.")
                        if user_value < 21:
                            user_bust = False
                        elif user_value > 21:
                            user_bust = True
                            break
                        elif user_value == 21:
                            break
                        hit_again = input("Would you like to hit again? Yes or No: ")
                        hit_again = hit_again.lower()
                        while True:
                            if hit_again == "no":
                                hit_again == False
                                hit_again = False
                                break
                            elif hit_again == "yes":
                                hit_again == True
                                hit_again = True
                                break
                            else:
                                print(f"Your action of '{hit_again}' is not a valid action.")
                                hit_again = input("Would you like to hit again? Yes or No: ")
                                hit_again = hit_again.lower()
                        while user_bust == False and hit_again == True:
                            while True:
                                last_card = randint(1,13)
                                while True: # this will check if the card is actually in the deck, if it's not it will get a new card
                                    if deck[(last_card)] > 0:
                                        break
                                    else:
                                        last_card = randint(1,13)
                                # these next few if / elif statements will give you what card you got and remove it from the deck
                                if last_card == 1: 
                                    user_cards.append("A")
                                    user_value += user_deck_values["A"]
                                    deck[1] -= 1
                                    last_card = "A"
                                elif last_card == 11:
                                    user_cards.append("J")
                                    user_value += user_deck_values["J"]
                                    deck[11] -= 1
                                    last_card = "J"
                                elif last_card == 12:
                                    user_cards.append("Q")
                                    user_value += user_deck_values["Q"]
                                    deck[12] -= 1
                                    last_card = "Q"
                                elif last_card == 13:
                                    user_cards.append("K")
                                    user_value += user_deck_values["K"]
                                    deck[13] -= 1
                                    last_card = "K"
                                else:
                                    user_cards.append(last_card)
                                    user_value += user_deck_values[(last_card)]
                                    deck[(last_card)] -= 1
                                if user_value > 21:
                                    user_deck_values["A"] = 1
                                    if user_changed == False:
                                        if "A" in user_cards:
                                            user_value -= 10
                                            user_changed = True
                                    if user_value > 21:
                                        user_bust = True
                                        print(f"You got a {last_card}, the values of your cards is {user_value}.")
                                        break
                                print(f"You got a {last_card}, the values of your cards is {user_value}.")
                                if user_value < 21:
                                    user_bust = False
                                elif user_value > 21:
                                    user_bust = True
                                    break
                                elif user_value == 21:
                                    break
                                hit_again = input("Would you like to hit again? Yes or No: ")
                                hit_again = hit_again.lower()
                        while hit_again == False:
                            print(f"The dealer has {dealer_cards} with a value of {dealer_value}.")
                            while True:
                                if dealer_value > 21:
                                    dealer_deck_values["A"] = 1
                                    if dealer_changed == False:
                                        if "A" in dealer_cards:
                                            dealer_value -= 10
                                            dealer_changed = True
                                    if dealer_value > 21:
                                        print("The dealer busted!")
                                        break
                                elif dealer_value >= 17:
                                    print("The dealer must stand, good luck!")
                                    break
                                if hit_again == False:
                                    for i in range(1,2):
                                        last_card = randint(1,13)
                                        while True: # this will check if the card is actually in the deck, if it's not it will get a new card
                                            if deck[(last_card)] > 0:
                                                break
                                            else:
                                                last_card = randint(1,13)
                                        # these next few if / elif statements will give you what card you got and remove it from the deck
                                        if last_card == 1: 
                                            dealer_cards.append("A")
                                            dealer_value += dealer_deck_values["A"]
                                            deck[1] -= 1
                                            last_card = "A"
                                        elif last_card == 11:
                                            dealer_cards.append("J")
                                            dealer_value += dealer_deck_values["J"]
                                            deck[11] -= 1
                                            last_card = "J"
                                        elif last_card == 12:
                                            dealer_cards.append("Q")
                                            dealer_value += dealer_deck_values["Q"]
                                            deck[12] -= 1
                                            last_card = "Q"
                                        elif last_card == 13:
                                            dealer_cards.append("K")
                                            dealer_value += dealer_deck_values["K"]
                                            deck[13] -= 1
                                            last_card = "K"
                                        else:
                                            dealer_cards.append(last_card)
                                            dealer_value += dealer_deck_values[(last_card)]
                                            deck[(last_card)] -= 1
                                    print(f"The dealer got a {last_card}, for a total value of {dealer_value}.")
                                
                            break
                        break
                    break
                break
            elif action == "double-down":
                break
            elif action == "split": # make sure you can split, if you can't go to else.... sep card bets (card1, card2....)
                break
            else:
                print(f"Your action of '{action}' is not a valid action.")
                action = input("Would you like to stand, hit, double-down, or split?: ")
                action = action.lower()
        if dealer_value > 21:
            print(f"You won! You had a value of {user_value} and the dealer had a value of {dealer_value}.")
            user_money += bet * 2
        elif user_value > 21:
            print(f"You lost! You had a value of {user_value} and the dealer had a value of {dealer_value}.")
        elif user_value == dealer_value:
            print(f"You tied with the dealer! You had a value of {user_value} and the dealer had a value of {dealer_value}.")
            user_money += bet
        elif user_value > dealer_value:
            print(f"You won! You had a value of {user_value} and the dealer had a value of {dealer_value}.")
            user_money += bet * 2
        elif user_value < dealer_value:
            print(f"You lost! You had a value of {user_value} and the dealer had a value of {dealer_value}.")